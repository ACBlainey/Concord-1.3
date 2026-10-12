"""External-effect crash window: independent host ledger and receiver journal.

Synthetic host ledger stands in for a queryable authoritative external system.
No real physical effect, cryptographic authentication, or distributed exactly-once guarantee.
"""
import sqlite3

class HostLedger:
    def __init__(self,path):
        self.path=str(path)
        with self.db() as c:
            c.execute("CREATE TABLE IF NOT EXISTS effects (action TEXT PRIMARY KEY, payload TEXT NOT NULL, receipt TEXT NOT NULL)")
    def db(self):
        c=sqlite3.connect(self.path,timeout=5,isolation_level=None)
        c.execute("PRAGMA busy_timeout=5000")
        c.execute("PRAGMA synchronous=FULL")
        return c
    def apply(self,action,payload,*,host_authorised=False):
        if not host_authorised:return ("REJECTED",None)
        with self.db() as c:
            c.execute("BEGIN IMMEDIATE")
            row=c.execute("SELECT payload,receipt FROM effects WHERE action=?",(action,)).fetchone()
            if row:
                c.execute("COMMIT")
                return ("IDEMPOTENT",row[1]) if row[0]==payload else ("CONFLICT",None)
            receipt="HOST:"+action+":"+payload
            c.execute("INSERT INTO effects VALUES(?,?,?)",(action,payload,receipt))
            c.execute("COMMIT")
            return ("APPLIED",receipt)
    def query(self,action):
        with self.db() as c:
            return c.execute("SELECT payload,receipt FROM effects WHERE action=?",(action,)).fetchone()

class Receiver:
    def __init__(self,path):
        self.path=str(path)
        with self.db() as c:
            c.execute("CREATE TABLE IF NOT EXISTS actions (action TEXT PRIMARY KEY,payload TEXT NOT NULL,state TEXT NOT NULL,receipt TEXT)")
    def db(self):
        c=sqlite3.connect(self.path,timeout=5,isolation_level=None)
        c.execute("PRAGMA busy_timeout=5000")
        c.execute("PRAGMA synchronous=FULL")
        return c
    def accept(self,action,payload,*,authorised=False):
        if not authorised:return "REJECTED"
        with self.db() as c:
            c.execute("BEGIN IMMEDIATE")
            row=c.execute("SELECT payload,state FROM actions WHERE action=?",(action,)).fetchone()
            if row:
                c.execute("COMMIT")
                return row[1] if row[0]==payload else "CONFLICT"
            c.execute("INSERT INTO actions VALUES(?,?,'CLAIMED',NULL)",(action,payload))
            c.execute("COMMIT");return "CLAIMED"
    def status(self,action):
        with self.db() as c:
            row=c.execute("SELECT payload,state,receipt FROM actions WHERE action=?",(action,)).fetchone()
            return row if row else None
    def reconcile(self,action,host,*,host_status_trusted=False):
        local=self.status(action)
        if not local:return "UNKNOWN_ACTION"
        if local[1]=="DONE":return "DONE"
        if not host_status_trusted:return "UNVERIFIED_HOST"
        remote=host.query(action)
        if remote is None:return "UNCONFIRMED_ABSENCE"
        if remote[0]!=local[0]:return "EFFECT_CONFLICT"
        with self.db() as c:
            c.execute("BEGIN IMMEDIATE")
            c.execute("UPDATE actions SET state='DONE',receipt=? WHERE action=? AND state!='DONE'",(remote[1],action))
            c.execute("COMMIT")
        return "RECONCILED"
    def mark_uncertain(self,action):
        with self.db() as c:
            c.execute("UPDATE actions SET state='UNCERTAIN' WHERE action=? AND state='CLAIMED'",(action,))
    def execute(self,action,host,*,host_authorised=False,crash_after_host=False):
        local=self.status(action)
        if not local or local[1]!="CLAIMED" or not host_authorised:return "RECONCILE"
        state,receipt=host.apply(action,local[0],host_authorised=True)
        if state not in ("APPLIED","IDEMPOTENT"):return state
        if crash_after_host:
            return "SIMULATED_CRASH"
        with self.db() as c:
            c.execute("UPDATE actions SET state='DONE',receipt=? WHERE action=? AND state='CLAIMED'",(receipt,action))
        return "DONE"
