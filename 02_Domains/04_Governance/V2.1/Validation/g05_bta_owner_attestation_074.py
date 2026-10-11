"""Owner-attestation boundary experiment, not a cryptographic or constitutional authority verifier."""
from dataclasses import dataclass

@dataclass(frozen=True)
class OwnerAttestation:
    owner_ref: str
    scope: str
    transition_id: str
    revision: int
    decision: str
    evidence_ref: str

def assess_transition(record, attestations, current_revisions, required):
    """Reject consequential activation unless every independent owner confirms its own scope."""
    issues=[]
    if not record.get("TransitionID") or not record.get("Scope"):
        issues.append("MISSING_TRANSITION_IDENTITY")
    if record.get("PendingStateRefs"):
        issues.append("PENDING_CONDITIONS")
    if record.get("UncertaintyOrDisputeState",{}).get("State")=="UNRESOLVED":
        issues.append("UNRESOLVED_STATE")
    for owner,scope in required:
        matches=[a for a in attestations if a.owner_ref==owner and a.scope==scope
                 and a.transition_id==record.get("TransitionID")]
        if len(matches)!=1:
            issues.append("MISSING_OR_DUPLICATE_OWNER_ATTESTATION:"+owner+":"+scope)
            continue
        a=matches[0]
        if not a.evidence_ref or a.decision!="APPROVED":
            issues.append("OWNER_NOT_APPROVED:"+owner+":"+scope)
        if current_revisions.get((owner,scope))!=a.revision:
            issues.append("STALE_OWNER_REVISION:"+owner+":"+scope)
    return {"eligible_for_owner_review":not issues,"issues":issues,
            "authority_granted":False,"transition_complete":False}
