"""Recovery outcome classification fixture; never equates compensation to restoration."""
from dataclasses import dataclass

KINDS={"RESUMPTION","COMPENSATION","RECONSTRUCTION","RESTORATION"}

@dataclass(frozen=True)
class Outcome:
    kind: str
    prior_state_ref: str
    resulting_state_ref: str
    evidence_refs: tuple
    unresolved_effect_refs: tuple
    owner_reviewed: bool
    equivalence_verified: bool
    surviving_duty_refs: tuple

def classify(outcome):
    issues=[]
    if outcome.kind not in KINDS:
        issues.append("UNKNOWN_OUTCOME")
    if not outcome.evidence_refs:
        issues.append("MISSING_EVIDENCE")
    if not outcome.owner_reviewed:
        issues.append("OWNER_REVIEW_REQUIRED")
    if not outcome.resulting_state_ref:
        issues.append("RESULTING_STATE_MISSING")
    if outcome.kind=="RESTORATION":
        if not outcome.prior_state_ref or not outcome.equivalence_verified:
            issues.append("RESTORATION_EQUIVALENCE_UNVERIFIED")
        if outcome.unresolved_effect_refs:
            issues.append("UNRESOLVED_EFFECTS_PREVENT_FULL_RESTORATION")
    if outcome.kind!="RESTORATION" and outcome.equivalence_verified:
        issues.append("EQUIVALENCE_CLAIM_REQUIRES_RECLASSIFICATION")
    return {"kind":outcome.kind,"issues":sorted(set(issues)),
            "full_restoration_verified":outcome.kind=="RESTORATION" and not issues,
            "duties_survive":bool(outcome.surviving_duty_refs),
            "authority_granted":False}
