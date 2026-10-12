"""Two independent durable SQLite peers with deterministic fault injection.

Prototype only: the transport is simulated; no credentials, real sockets,
physical effect, constitutional mandate or distributed atomic commit.
"""
import sqlite3

class Peer:
    def __init__(self,path,role):
        self.path=str(path);self.role=role
        with self.db() as c:
            c.execute("CREATE TABLE IF NOT EXISTS messages (event TEXT PRIMARY KEY, payload TEXT NOT NULL, state TEXT NOT NULL, revision INTEGER NOT NULL)")
            c.execute("CREATE TABLE IF NOT EXISTS effects (event TEXT PRIMARY KEY, receipt TEXT NOT NULL)")
    def db(self):
        c=sqlite3.connect(self.path,timeout=5,isolation_level=None)
        c.execute("PRAGMA busy_timeout=5000")
        c.execute("PRAGMA synchronous=FULL")
        return c
    def prepare(self,event,payload,revision):
        with self.db() as c:
            c.execute("BEGIN IMMEDIATE")
            row=c.execute("SELECT payload,revision FROM messages WHERE event=?",(event,)).fetchone()
            if row:
                c.execute("COMMIT");return "IDEMPOTENT" if row==(payload,revision) else "CONFLICT"
            c.execute("INSERT INTO messages VALUES(?,?,?,?)",(event,payload,"PENDING",revision))
            c.execute("COMMIT");return "PENDING"
    def receive(self,event,payload,revision,*,owner_valid=False,scope_valid=False):
        if not owner_valid or not scope_valid:return "REJECTED"
        with self.db() as c:
            c.execute("BEGIN IMMEDIATE")
            row=c.execute("SELECT payload,revision,state FROM messages WHERE event=?",(event,)).fetchone()
            if row:
                c.execute("COMMIT")
                return row[2] if row[:2]==(payload,revision) else "CONFLICT"
            c.execute("INSERT INTO messages VALUES(?,?,?,?)",(event,payload,"ACCEPTED",revision))
            c.execute("COMMIT");return "ACCEPTED"
    def commit_effect(self,event,receipt,*,host_authorised=False):
        if not host_authorised or not receipt:return "REJECTED"
        with self.db() as c:
            c.execute("BEGIN IMMEDIATE")
            row=c.execute("SELECT state FROM messages WHERE event=?",(event,)).fetchone()
            if not row or row[0]!="ACCEPTED":
                c.execute("ROLLBACK");return "REJECTED"
            if c.execute("SELECT 1 FROM effects WHERE event=?",(event,)).fetchone():
                c.execute("COMMIT");return "DUPLICATE"
            c.execute("INSERT INTO effects VALUES(?,?)",(event,receipt))
            c.execute("UPDATE messages SET state='COMMITTED' WHERE event=?",(event,))
            c.execute("COMMIT");return "COMMITTED"
    def status(self,event):
        with self.db() as c:
            row=c.execute("SELECT state,revision FROM messages WHERE event=?",(event,)).fetchone()
            effect=c.execute("SELECT receipt FROM effects WHERE event=?",(event,)).fetchone()
            return (row[0],row[1],effect[0] if effect else None) if row else ("ABSENT",None,None)
    def reconcile(self,event,receiver):
        local=self.status(event)
        if local[0]=="ABSENT":return "UNKNOWN_LOCAL"
        remote=receiver.status(event)
        if remote[0]=="ABSENT":return "NOT_RECEIVED"
        if remote[1]!=local[1]:return "REVISION_CONFLICT"
        with self.db() as c:
            c.execute("BEGIN IMMEDIATE")
            c.execute("UPDATE messages SET state=? WHERE event=?",(remote[0],event))
            c.execute("COMMIT")
        return remote[0]
