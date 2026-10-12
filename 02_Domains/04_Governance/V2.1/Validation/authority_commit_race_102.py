"""Deterministic revocation/commit race experiment with independent owner ledgers.

No cross-ledger atomicity or real external effect is claimed. A revocation can
happen after verification; the fixture detects that gap rather than hiding it.
"""
import threading
from authority_owner_registry_101 import commit_gate

class CommitRace:
    def __init__(self,request,owners,refs,required):
        self.request=request;self.owners=owners;self.refs=refs;self.required=set(required)
        self.attempts=0;self.committed=False
    def check(self,now):
        return commit_gate(self.request,self.owners,self.refs,now=now,required_issuers=self.required,context_allowed=True,host_ready=True,current_revision=self.request.revision)
    def run(self,now,*,before_commit=None):
        if self.committed:return "ALREADY_COMMITTED"
        if self.check(now)!="ALLOW":return "DENIED_AT_PREPARE"
        if before_commit:before_commit()
        if self.check(now)!="ALLOW":return "DENIED_AT_COMMIT"
        self.attempts+=1
        self.committed=True
        return "COMMITTED"
    def observed_gap(self,now,*,before_effect=None):
        """Adversarial interleaving AFTER last check; no atomic fence exists."""
        if self.check(now)!="ALLOW":return "DENIED_AT_COMMIT"
        if before_effect:before_effect()
        self.attempts+=1
        return "UNFENCED_EFFECT"
