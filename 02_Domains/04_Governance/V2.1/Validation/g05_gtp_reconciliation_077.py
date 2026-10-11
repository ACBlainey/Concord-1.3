"""Reconciliation proposal fixture for overlapping GTP resource claims.

No legal priority, physical allocation or constitutional authority is inferred.
"""
from dataclasses import dataclass
from g05_gtp_resource_collision_076 import assess

@dataclass(frozen=True)
class Resolution:
    resolution_id: str
    resource: str
    affected_claim_ids: tuple
    evidence_refs: tuple
    owner_approvals: tuple
    revision: int
    proposed_modes: tuple

def review_resolution(claims,resolution,required_owners,current_revision):
    issues=[]
    affected=[c for c in claims if c.resource==resolution.resource and c.state=="ACTIVE"]
    if not resolution.resolution_id or not resolution.evidence_refs:
        issues.append("RESOLUTION_EVIDENCE_MISSING")
    if resolution.revision!=current_revision:
        issues.append("STALE_RESOLUTION")
    if set(resolution.affected_claim_ids)!={c.claim_id for c in affected}:
        issues.append("INCOMPLETE_AFFECTED_CLAIMS")
    if set(resolution.owner_approvals)!=set(required_owners):
        issues.append("OWNER_APPROVAL_INCOMPLETE")
    if len(resolution.proposed_modes)!=len(affected):
        issues.append("PROPOSED_ALLOCATION_INCOMPLETE")
    if len(set(resolution.affected_claim_ids))!=len(resolution.affected_claim_ids):
        issues.append("DUPLICATE_CLAIM_REFERENCE")
    if assess(claims)["issues"] and not resolution.proposed_modes:
        issues.append("COLLISION_UNRESOLVED")
    return {"issues":sorted(set(issues)),"ready_for_owner_system_verification":not issues,
            "mandates_overridden":False,"allocation_activated":False}
