"""Stage 110 contextual early acceptance, a source-shaped policy adapter.

Two matching votes determine the arithmetic outcome; acceptance for progression
depends on independently justified current context. The third Steward's ballot
remains independently recordable. No external host effect is authorised here.
"""
import sqlite3
from glass_hammer_state_108 import BallotMachine

class ContextualDecision:
    def __init__(self,path):
        self.machine=BallotMachine(path)
        with self.machine.connection() as db:
            db.execute("CREATE TABLE IF NOT EXISTS acceptance110 (decision_id TEXT PRIMARY KEY, accepted_result TEXT NOT NULL, basis TEXT NOT NULL, early INTEGER NOT NULL)")
            db.execute("CREATE TABLE IF NOT EXISTS late_ballots110 (decision_id TEXT NOT NULL, position TEXT NOT NULL, steward TEXT NOT NULL, choice TEXT NOT NULL, event_id TEXT NOT NULL UNIQUE, PRIMARY KEY(decision_id,position), UNIQUE(decision_id,steward))")
    def create(self,decision_id,question):
        self.machine.create(decision_id,question)
    def vote(self,*,decision_id,position,steward,choice,event_id,eligible,context_ok):
        if not eligible:return "DENY_ELIGIBILITY"
        if not context_ok:return "DENY_CONTEXT"
        if position not in ("P1","P2","P3") or choice not in ("F","A","U"):return "DENY_INPUT"
        with self.machine.connection() as db:
            db.execute("BEGIN IMMEDIATE")
            try:
                row=db.execute("SELECT state FROM decisions WHERE id=?",(decision_id,)).fetchone()
                if row is None:out="DENY_UNKNOWN_DECISION"
                else:
                    prev=db.execute("SELECT decision_id,position,steward,choice FROM ballots WHERE event_id=?",(event_id,)).fetchone()
                    prevlate=db.execute("SELECT decision_id,position,steward,choice FROM late_ballots110 WHERE event_id=?",(event_id,)).fetchone()
                    if prev or prevlate:
                        out="DUPLICATE" if (prev or prevlate)==(decision_id,position,steward,choice) else "DENY_EVENT_COLLISION"
                    elif db.execute("SELECT 1 FROM ballots WHERE decision_id=? AND position=?",(decision_id,position)).fetchone() or db.execute("SELECT 1 FROM late_ballots110 WHERE decision_id=? AND position=?",(decision_id,position)).fetchone():
                        out="DENY_CONSUMED"
                    elif db.execute("SELECT 1 FROM ballots WHERE decision_id=? AND steward=?",(decision_id,steward)).fetchone() or db.execute("SELECT 1 FROM late_ballots110 WHERE decision_id=? AND steward=?",(decision_id,steward)).fetchone():
                        out="DENY_REPEATED_STEWARD"
                    elif row[0]=="OPEN":
                        db.execute("INSERT INTO ballots VALUES (?,?,?,?,?)",(decision_id,position,steward,choice,event_id))
                        counts=[r[0] for r in db.execute("SELECT choice FROM ballots WHERE decision_id=?",(decision_id,))]
                        if len(counts)==3:db.execute("UPDATE decisions SET state='CLOSED' WHERE id=?",(decision_id,))
                        db.execute("INSERT INTO transitions VALUES (?,?,?,?,?)",(event_id,decision_id,position,"OPEN","CLOSED" if len(counts)==3 else "OPEN"))
                        out="ACCEPTED"
                    elif row[0]=="CLOSED":
                        accepted=db.execute("SELECT early FROM acceptance110 WHERE decision_id=?",(decision_id,)).fetchone()
                        if accepted and accepted[0] and db.execute("SELECT COUNT(*) FROM ballots WHERE decision_id=?",(decision_id,)).fetchone()[0]<3:
                            db.execute("INSERT INTO late_ballots110 VALUES (?,?,?,?,?)",(decision_id,position,steward,choice,event_id))
                            out="LATE_RECORDED"
                        else:out="DENY_CLOSED"
                    else:out="DENY_STATE"
                db.execute("COMMIT")
                return out
            except Exception:
                db.execute("ROLLBACK")
                raise
    def accept(self,decision_id,*,early_context_justified=False,basis=None):
        """An emergency may provide a basis; other contexts are deliberately open."""
        with self.machine.connection() as db:
            db.execute("BEGIN IMMEDIATE")
            try:
                old=db.execute("SELECT accepted_result FROM acceptance110 WHERE decision_id=?",(decision_id,)).fetchone()
                if old:out="ALREADY_ACCEPTED"
                else:
                    row=db.execute("SELECT state FROM decisions WHERE id=?",(decision_id,)).fetchone()
                    if row is None:out="DENY_UNKNOWN_DECISION"
                    else:
                        counts=[r[0] for r in db.execute("SELECT choice FROM ballots WHERE decision_id=?",(decision_id,))]
                        result="F" if counts.count("F")>=2 else "A" if counts.count("A")>=2 else "U"
                        if result=="U":out="DENY_UNRESOLVED"
                        elif len(counts)<3 and (not early_context_justified or not basis):out="WAIT_FOR_THIRD"
                        else:
                            early=int(len(counts)<3)
                            db.execute("INSERT INTO acceptance110 VALUES (?,?,?,?)",(decision_id,result,basis or "ALL_THREE_RECORDED",early))
                            db.execute("UPDATE decisions SET state='CLOSED' WHERE id=?",(decision_id,))
                            out="EARLY_ACCEPTED" if early else "ACCEPTED"
                db.execute("COMMIT")
                return out
            except Exception:
                db.execute("ROLLBACK")
                raise
    def status(self,decision_id):
        with self.machine.connection() as db:
            a=db.execute("SELECT accepted_result,basis,early FROM acceptance110 WHERE decision_id=?",(decision_id,)).fetchone()
            regular=db.execute("SELECT position,steward,choice FROM ballots WHERE decision_id=?",(decision_id,)).fetchall()
            late=db.execute("SELECT position,steward,choice FROM late_ballots110 WHERE decision_id=?",(decision_id,)).fetchall()
            return {"determined":"F" if [v[2] for v in regular].count("F")>=2 else "A" if [v[2] for v in regular].count("A")>=2 else "U",
                    "accepted":a[0] if a else None,"early":bool(a[2]) if a else False,
                    "regular":tuple(regular),"late":tuple(late),"execution_authorised":False}
