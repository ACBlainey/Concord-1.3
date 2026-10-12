"""SQLite-backed ACKS recovery fixture. NOT a production authority or effects engine.

One local durable SQLite journal; no remote consensus, network authentication,
distributed transactions or exactly-once physical effect guarantee.
"""
import sqlite3

class DurableDecisionRecovery:
    def __init__(self, path):
        self.path = str(path)
        with self._db() as c:
            c.execute("CREATE TABLE IF NOT EXISTS decisions (id TEXT PRIMARY KEY, result TEXT NOT NULL, authorised INTEGER NOT NULL)")
            c.execute("CREATE TABLE IF NOT EXISTS actions (decision_id TEXT NOT NULL, action_id TEXT NOT NULL, state TEXT NOT NULL, receipt TEXT, PRIMARY KEY(decision_id,action_id))")
            c.execute("CREATE TABLE IF NOT EXISTS acks (decision_id TEXT NOT NULL, action_id TEXT NOT NULL, owner TEXT NOT NULL, nonce TEXT NOT NULL, revision INTEGER NOT NULL, evidence TEXT NOT NULL, decision TEXT NOT NULL, PRIMARY KEY(decision_id,action_id,owner), UNIQUE(nonce))")
    def _db(self):
        c = sqlite3.connect(self.path, timeout=5, isolation_level=None)
        c.execute("PRAGMA busy_timeout=5000")
        c.execute("PRAGMA synchronous=FULL")
        return c
    def decision(self, decision_id, result, authorised):
        if result not in ("F","A","U"): raise ValueError("invalid result")
        with self._db() as c:
            c.execute("INSERT INTO decisions VALUES(?,?,?)",(decision_id,result,int(bool(authorised))))
    def claim(self, decision_id, action_id, *, host_authorised=False):
        with self._db() as c:
            c.execute("BEGIN IMMEDIATE")
            row=c.execute("SELECT result,authorised FROM decisions WHERE id=?",(decision_id,)).fetchone()
            if not row or row[0]=="U" or not row[1] or not host_authorised:
                c.execute("ROLLBACK");return "REJECTED"
            row=c.execute("SELECT state FROM actions WHERE decision_id=? AND action_id=?",(decision_id,action_id)).fetchone()
            if row:
                c.execute("COMMIT")
                return "DUPLICATE" if row[0]=="DONE" else "RECONCILE"
            c.execute("INSERT INTO actions(decision_id,action_id,state) VALUES(?,?,?)",(decision_id,action_id,"CLAIMED"))
            c.execute("COMMIT")
            return "CLAIMED"
    def effect(self, decision_id, action_id, *, receipt=None):
        with self._db() as c:
            c.execute("BEGIN IMMEDIATE")
            row=c.execute("SELECT state FROM actions WHERE decision_id=? AND action_id=?",(decision_id,action_id)).fetchone()
            if not row or row[0]!="CLAIMED":
                c.execute("ROLLBACK");return "REJECTED"
            state="DONE" if receipt else "UNCERTAIN"
            c.execute("UPDATE actions SET state=?,receipt=? WHERE decision_id=? AND action_id=?",(state,receipt,decision_id,action_id))
            c.execute("COMMIT")
            return state
    def status(self, decision_id, action_id):
        with self._db() as c:
            row=c.execute("SELECT state,receipt FROM actions WHERE decision_id=? AND action_id=?",(decision_id,action_id)).fetchone()
            return row if row else ("NOT_CLAIMED",None)
    def ack(self, decision_id, action_id, owner, nonce, revision, evidence, decision, *, authenticated=False, scope_verified=False):
        if not authenticated or not scope_verified or not evidence or not nonce or decision not in ("ACK","REJECT"):
            return "REJECTED"
        with self._db() as c:
            c.execute("BEGIN IMMEDIATE")
            row=c.execute("SELECT owner,nonce,revision,evidence,decision FROM acks WHERE decision_id=? AND action_id=? AND owner=?",(decision_id,action_id,owner)).fetchone()
            payload=(owner,nonce,revision,evidence,decision)
            if row:
                c.execute("COMMIT")
                return "IDEMPOTENT" if row==payload else "OWNER_CONFLICT"
            if c.execute("SELECT 1 FROM acks WHERE nonce=?",(nonce,)).fetchone():
                c.execute("ROLLBACK");return "REPLAY_CONFLICT"
            if not c.execute("SELECT 1 FROM actions WHERE decision_id=? AND action_id=?",(decision_id,action_id)).fetchone():
                c.execute("ROLLBACK");return "UNKNOWN_ACTION"
            c.execute("INSERT INTO acks VALUES(?,?,?,?,?,?,?)",(decision_id,action_id,owner,nonce,revision,evidence,decision))
            c.execute("COMMIT")
            return "RECORDED"
