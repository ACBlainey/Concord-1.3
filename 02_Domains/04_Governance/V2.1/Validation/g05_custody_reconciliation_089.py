"""G05 custody reconciliation candidate.

Projection consistency checker only. No independent authority, no mutation of
source ledgers, and no inference that evidence references are verified.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class ReconciliationEvent:
    event_ref: str
    duty_id: str
    previous_custodian: str
    proposed_custodian: str
    expected_revision: int
    new_revision: int
    owner_decision_ref: str
    successor_acceptance_ref: str
    provenance_ref: str
    source_transition_ref: str

def reconcile(event, continuity, succession, orphans,
              owner_verified=False, successor_verified=False,
              provenance_verified=False, expected_source_revision=None):
    issues=[]
    if not all((event.event_ref,event.duty_id,event.previous_custodian,
                event.proposed_custodian,event.owner_decision_ref,
                event.successor_acceptance_ref,event.provenance_ref,
                event.source_transition_ref)):
        issues.append("INCOMPLETE_EVENT")
    if event.previous_custodian==event.proposed_custodian:
        issues.append("NO_CUSTODY_CHANGE")
    duty=continuity.duties.get(event.duty_id)
    custody=succession.records.get(event.duty_id)
    orphan=orphans.records.get(event.duty_id)
    if duty is None or custody is None or orphan is None:
        issues.append("SOURCE_RECORD_MISSING")
    else:
        if duty.origin_transition!=event.source_transition_ref or orphan.origin_transition!=event.source_transition_ref:
            issues.append("TRANSITION_PROVENANCE_MISMATCH")
        if duty.state!="OPEN" or custody.obligation_state!="OPEN":
            issues.append("DUTY_NOT_OPEN")
        if orphan.last_custodian!=event.previous_custodian:
            issues.append("ORPHAN_ORIGIN_MISMATCH")
        if custody.revision!=event.new_revision or event.new_revision!=event.expected_revision+1:
            issues.append("REVISION_MISMATCH")
        if custody.custodian!=event.proposed_custodian:
            issues.append("SUCCESSION_NOT_COMMITTED")
        if duty.owner!=event.previous_custodian:
            issues.append("CONTINUITY_OWNER_MISMATCH")
    if expected_source_revision is None or expected_source_revision!=event.expected_revision:
        issues.append("SOURCE_REVISION_NOT_CONFIRMED")
    if not owner_verified:issues.append("OWNER_ATTESTATION_REQUIRED")
    if not successor_verified:issues.append("SUCCESSOR_ATTESTATION_REQUIRED")
    if not provenance_verified:issues.append("PROVENANCE_VERIFICATION_REQUIRED")
    return {"issues":issues,"eligible_for_owner_controlled_projection":not issues,
            "mutation_performed":False,"authority_granted":False,
            "duty_closed":False,"orphan_cleared":False}
