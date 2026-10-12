"""Glass-hammer event-local authority fixture: NOT a Concord runtime.

Each Steward ballot is a context-guarded, atomic state transition. Identity and
context are prerequisites, not reusable authority tokens. SQLite is a test
implementation choice, not prescribed by the historical glass-hammer metaphor.
"""
import sqlite3
from contextlib import contextmanager


class BallotMachine:
    def __init__(self, path):
        self.path = str(path)
        with self.connection() as db:
            db.execute("CREATE TABLE IF NOT EXISTS decisions (id TEXT PRIMARY KEY, question TEXT NOT NULL, state TEXT NOT NULL CHECK(state IN ('OPEN','CLOSED')))")
            db.execute("CREATE TABLE IF NOT EXISTS ballots (decision_id TEXT NOT NULL, position TEXT NOT NULL, steward TEXT NOT NULL, choice TEXT NOT NULL CHECK(choice IN ('F','A','U')), event_id TEXT NOT NULL UNIQUE, PRIMARY KEY(decision_id,position), UNIQUE(decision_id,steward))")
            db.execute("CREATE TABLE IF NOT EXISTS transitions (event_id TEXT PRIMARY KEY, decision_id TEXT NOT NULL, position TEXT NOT NULL, before_state TEXT NOT NULL, after_state TEXT NOT NULL)")
    @contextmanager
    def connection(self):
        db=sqlite3.connect(self.path, timeout=5, isolation_level=None)
        try:
            yield db
        finally:
            db.close()
    def create(self, decision_id, question):
        with self.connection() as db:
            db.execute("INSERT INTO decisions VALUES (?,?,?)",(decision_id,question,"OPEN"))
    def submit(self, *, decision_id, position, steward, choice, event_id, expected_state, eligible, context_ok):
        if not eligible: return "DENY_ELIGIBILITY"
        if not context_ok: return "DENY_CONTEXT"
        if position not in ("P1","P2","P3") or choice not in ("F","A","U"): return "DENY_INPUT"
        with self.connection() as db:
            db.execute("BEGIN IMMEDIATE")
            try:
                existing=db.execute("SELECT decision_id,position,steward,choice FROM ballots WHERE event_id=?",(event_id,)).fetchone()
                if existing:
                    outcome="DUPLICATE" if existing==(decision_id,position,steward,choice) else "DENY_EVENT_COLLISION"
                else:
                    row=db.execute("SELECT state FROM decisions WHERE id=?",(decision_id,)).fetchone()
                    if row is None: outcome="DENY_UNKNOWN_DECISION"
                    elif row[0]!=expected_state or row[0]!="OPEN": outcome="DENY_STATE"
                    elif db.execute("SELECT 1 FROM ballots WHERE decision_id=? AND position=?",(decision_id,position)).fetchone(): outcome="DENY_CONSUMED"
                    elif db.execute("SELECT 1 FROM ballots WHERE decision_id=? AND steward=?",(decision_id,steward)).fetchone(): outcome="DENY_REPEATED_STEWARD"
                    else:
                        db.execute("INSERT INTO ballots VALUES (?,?,?,?,?)",(decision_id,position,steward,choice,event_id))
                        votes=[r[0] for r in db.execute("SELECT choice FROM ballots WHERE decision_id=?",(decision_id,))]
                        result="F" if votes.count("F")>=2 else "A" if votes.count("A")>=2 else "U"
                        after="CLOSED" if result!="U" or len(votes)==3 else "OPEN"
                        db.execute("UPDATE decisions SET state=? WHERE id=?",(after,decision_id))
                        db.execute("INSERT INTO transitions VALUES (?,?,?,?,?)",(event_id,decision_id,position,expected_state,after))
                        outcome="ACCEPTED"
                db.execute("COMMIT")
                return outcome
            except Exception:
                db.execute("ROLLBACK")
                raise
    def snapshot(self, decision_id):
        with self.connection() as db:
            state=db.execute("SELECT state FROM decisions WHERE id=?",(decision_id,)).fetchone()
            votes=[tuple(r) for r in db.execute("SELECT position,steward,choice,event_id FROM ballots WHERE decision_id=? ORDER BY position",(decision_id,))]
            return (state[0] if state else None,votes)
    def result(self, decision_id):
        state,votes=self.snapshot(decision_id)
        counts=[v[2] for v in votes]
        if counts.count("F")>=2:return "F"
        if counts.count("A")>=2:return "A"
        return "U"
