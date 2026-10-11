"""Revalidation of a reconciliation proposal immediately before execution.

Candidate fixture only. Owner decisions, mandate revisions, dependencies and
resource state must be verified externally; this code never issues authority.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Snapshot:
    resource_revision: int
    owner_revisions: tuple
    dependency_revision: int
    emergency_epoch: int
    clock_epoch: int

@dataclass(frozen=True)
class Approval:
    owner: str
    mandate_revision: int
    decision: str
    evidence_ref: str

def review_for_execution(proposal_snapshot,live_snapshot,approvals,required_owners,
                         resource_available,proposal_valid):
    issues=[]
    if not proposal_valid:
        issues.append("PROPOSAL_NOT_VALIDATED")
    if proposal_snapshot.resource_revision!=live_snapshot.resource_revision:
        issues.append("RESOURCE_CHANGED")
    if proposal_snapshot.dependency_revision!=live_snapshot.dependency_revision:
        issues.append("DEPENDENCY_CHANGED")
    if proposal_snapshot.emergency_epoch!=live_snapshot.emergency_epoch:
        issues.append("EMERGENCY_CONTEXT_CHANGED")
    if proposal_snapshot.clock_epoch!=live_snapshot.clock_epoch:
        issues.append("CLOCK_CONTEXT_CHANGED_REVIEW")
    if not resource_available:
        issues.append("RESOURCE_UNAVAILABLE")
    live=dict(live_snapshot.owner_revisions)
    if len(live)!=len(live_snapshot.owner_revisions):
        issues.append("DUPLICATE_OWNER_REVISION")
    for owner in required_owners:
        matches=[a for a in approvals if a.owner==owner]
        if len(matches)!=1:
            issues.append("MISSING_OR_DUPLICATE_APPROVAL:"+owner)
            continue
        a=matches[0]
        if a.decision!="APPROVED" or not a.evidence_ref:
            issues.append("APPROVAL_INVALID:"+owner)
        if live.get(owner)!=a.mandate_revision:
            issues.append("OWNER_REVISION_STALE:"+owner)
    if set(a.owner for a in approvals)!=set(required_owners):
        issues.append("EXTRANEOUS_APPROVAL_REVIEW")
    return {"issues":sorted(set(issues)),"ready_for_final_owner_check":not issues,
            "execution_authorised":False}
