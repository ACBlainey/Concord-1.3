"""Independent owner-controlled authority evidence fixture.

Owner registry holds issued/revoked grants; verifier reads owner state, not
caller-provided verified_issuers. Test-only SQLite, no cryptographic signatures.
"""
import sqlite3
from dataclasses import dataclass

@dataclass(frozen=True)
class Request:
    subject:str
    action:str
    target:str
    purpose:str
    revision:int

class OwnerRegistry:
    def __init__(self,path,issuer):
        self.path=str(path);self.issuer=issuer
        with self.db() as c:
            c.execute("CREATE TABLE IF NOT EXISTS grants (ref TEXT PRIMARY KEY, subject TEXT, action TEXT, target TEXT, purpose TEXT, revision INTEGER, starts INTEGER, expires INTEGER, revoked INTEGER NOT NULL DEFAULT 0)")
    def db(self):
        c=sqlite3.connect(self.path,timeout=5,isolation_level=None)
        c.execute("PRAGMA busy_timeout=5000")
        c.execute("PRAGMA synchronous=FULL")
        return c
    def issue(self,ref,request,starts,expires):
        if not ref or starts>=expires:raise ValueError("invalid grant")
        with self.db() as c:
            c.execute("INSERT INTO grants(ref,subject,action,target,purpose,revision,starts,expires) VALUES(?,?,?,?,?,?,?,?)",(ref,request.subject,request.action,request.target,request.purpose,request.revision,starts,expires))
    def revoke(self,ref):
        with self.db() as c:
            return c.execute("UPDATE grants SET revoked=1 WHERE ref=?",(ref,)).rowcount
    def check(self,ref,request,now):
        with self.db() as c:
            row=c.execute("SELECT subject,action,target,purpose,revision,starts,expires,revoked FROM grants WHERE ref=?",(ref,)).fetchone()
        if row is None:return "UNKNOWN"
        if row[7]:return "REVOKED"
        if not(row[5]<=now<row[6]):return "OUT_OF_TIME"
        if row[:5]!=(request.subject,request.action,request.target,request.purpose,request.revision):return "SCOPE_MISMATCH"
        return "VALID"

def commit_gate(request,owners,grant_refs,*,now,required_issuers,context_allowed,host_ready,current_revision):
    """No grant may be created by this gate; each issuer checks its own ledger."""
    if not context_allowed or not host_ready:return "DENY_CONTEXT"
    if request.revision!=current_revision:return "DENY_REVISION"
    if not required_issuers:return "DENY_NO_AUTHORITY_BASIS"
    for issuer in required_issuers:
        owner=owners.get(issuer)
        ref=grant_refs.get(issuer)
        if owner is None or owner.issuer!=issuer or not ref:return "DENY_MISSING_OWNER"
        if owner.check(ref,request,now)!="VALID":return "DENY_AUTHORITY"
    return "ALLOW"
