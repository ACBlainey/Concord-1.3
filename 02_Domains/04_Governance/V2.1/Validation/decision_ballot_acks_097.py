"""SQLite ballot-to-action recovery contract fixture (not an authority service).

Authorisation, host scope and owner identity are externally asserted test inputs.
No distributed consensus, verified credentials or physical-effect exactly-once claim.
"""
import sqlite3

class BallotAckJournal:
    def __init__(self,path):
        self.path=str(path)
        with self.db() as c:
            c.execute("CREATE TABLE IF NOT EXISTS decisions (id TEXT PRIMARY KEY, revision INTEGER NOT NULL DEFAULT 0, result TEXT NOT NULL DEFAULT 'U', active INTEGER NOT NULL)")
            c.execute("CREATE TABLE IF NOT EXISTS ballots (decision_id TEXT, position TEXT, steward TEXT, ballot TEXT, PRIMARY KEY(decision_id,position), UNIQUE(decision_id,steward))")
            c.execute("CREATE TABLE IF NOT EXISTS actions (decision_id TEXT, action_id TEXT, revision INTEGER, state TEXT, receipt TEXT, PRIMARY KEY(decision_id,action_id))")
            c.execute("CREATE TABLE IF NOT EXISTS acknowledgements (decision_id TEXT, action_id TEXT, owner TEXT, nonce TEXT UNIQUE, revision INTEGER, evidence TEXT, decision TEXT, PRIMARY KEY(decision_id,action_id,owner))")
    def db(self):
        c=sqlite3.connect(self.path,timeout=10,isolation_level=None)
        c.execute("PRAGMA busy_timeout=10000")
        c.execute("PRAGMA synchronous=FULL")
        return c
    def create(self,decision_id,*,authorised=False):
        with self.db() as c:
            c.execute("INSERT INTO decisions(id,active) VALUES(?,?)",(decision_id,int(authorised)))
    def vote(self,decision_id,position,steward,ballot,*,mandate=False):
        with self.db() as c:
            c.execute("BEGIN IMMEDIATE")
            d=c.execute("SELECT revision,result,active FROM decisions WHERE id=?",(decision_id,)).fetchone()
            if not d or not d[2] or not mandate or position not in ("P1","P2","P3") or ballot not in ("F","A","U"):
                c.execute("ROLLBACK");return "REJECTED"
            prior=c.execute("SELECT steward,ballot FROM ballots WHERE decision_id=? AND position=?",(decision_id,position)).fetchone()
            if prior:
                c.execute("COMMIT")
                return "DUPLICATE" if prior==(steward,ballot) else "CONFLICT"
            if c.execute("SELECT 1 FROM ballots WHERE decision_id=? AND steward=?",(decision_id,steward)).fetchone():
                c.execute("ROLLBACK");return "REPEATED_STEWARD"
            if d[1]!="U":
                c.execute("COMMIT");return "PROVENANCE_ONLY"
            c.execute("INSERT INTO ballots VALUES(?,?,?,?)",(decision_id,position,steward,ballot))
            votes=[x[0] for x in c.execute("SELECT ballot FROM ballots WHERE decision_id=?",(decision_id,))]
            result="F" if votes.count("F")>=2 else "A" if votes.count("A")>=2 else "U"
            c.execute("UPDATE decisions SET revision=revision+1,result=? WHERE id=?",(result,decision_id))
            c.execute("COMMIT");return "ACCEPTED"
    def state(self,decision_id):
        with self.db() as c:
            return c.execute("SELECT revision,result FROM decisions WHERE id=?",(decision_id,)).fetchone()
    def claim(self,decision_id,action_id,*,host_authorised=False,expected_revision=None):
        with self.db() as c:
            c.execute("BEGIN IMMEDIATE")
            d=c.execute("SELECT revision,result,active FROM decisions WHERE id=?",(decision_id,)).fetchone()
            if not d or not d[2] or d[1]=="U" or not host_authorised or d[0]!=expected_revision:
                c.execute("ROLLBACK");return "REJECTED"
            a=c.execute("SELECT state FROM actions WHERE decision_id=? AND action_id=?",(decision_id,action_id)).fetchone()
            if a:
                c.execute("COMMIT");return "DUPLICATE" if a[0]=="DONE" else "RECONCILE"
            c.execute("INSERT INTO actions(decision_id,action_id,revision,state) VALUES(?,?,?,'CLAIMED')",(decision_id,action_id,d[0]))
            c.execute("COMMIT");return "CLAIMED"
    def effect(self,decision_id,action_id,receipt=None):
        with self.db() as c:
            c.execute("BEGIN IMMEDIATE")
            a=c.execute("SELECT state FROM actions WHERE decision_id=? AND action_id=?",(decision_id,action_id)).fetchone()
            if not a or a[0]!="CLAIMED":
                c.execute("ROLLBACK");return "REJECTED"
            state="DONE" if receipt else "UNCERTAIN"
            c.execute("UPDATE actions SET state=?,receipt=? WHERE decision_id=? AND action_id=?",(state,receipt,decision_id,action_id))
            c.execute("COMMIT");return state
    def ack(self,decision_id,action_id,owner,nonce,revision,evidence,decision,*,authenticated=False,scope_verified=False):
        if not authenticated or not scope_verified or not owner or not nonce or not evidence or decision not in ("ACK","REJECT"):
            return "REJECTED"
        with self.db() as c:
            c.execute("BEGIN IMMEDIATE")
            a=c.execute("SELECT revision FROM actions WHERE decision_id=? AND action_id=?",(decision_id,action_id)).fetchone()
            if not a:
                c.execute("ROLLBACK");return "UNKNOWN_ACTION"
            if a[0]!=revision:
                c.execute("ROLLBACK");return "REVISION_CONFLICT"
            prior=c.execute("SELECT nonce,revision,evidence,decision FROM acknowledgements WHERE decision_id=? AND action_id=? AND owner=?",(decision_id,action_id,owner)).fetchone()
            if prior:
                c.execute("COMMIT")
                return "IDEMPOTENT" if prior==(nonce,revision,evidence,decision) else "OWNER_CONFLICT"
            if c.execute("SELECT 1 FROM acknowledgements WHERE nonce=?",(nonce,)).fetchone():
                c.execute("ROLLBACK");return "REPLAY_CONFLICT"
            c.execute("INSERT INTO acknowledgements VALUES(?,?,?,?,?,?,?)",(decision_id,action_id,owner,nonce,revision,evidence,decision))
            c.execute("COMMIT");return "RECORDED"
