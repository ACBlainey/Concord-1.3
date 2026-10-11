"""Shared-resource collision fixture for concurrent nonhierarchical GTP mandates.

This does not arbitrate legal priority or establish physical exclusivity.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Claim:
    claim_id: str
    area: str
    owner: str
    resource: str
    revision: int
    mandate_ref: str
    mode: str  # EXCLUSIVE or SHARED
    state: str # ACTIVE or EXPIRED

def assess(claims):
    issues=[]
    ids=set()
    for c in claims:
        if c.claim_id in ids: issues.append("DUPLICATE_CLAIM_ID")
        ids.add(c.claim_id)
        if not c.mandate_ref or c.revision<0: issues.append("INVALID_MANDATE_REFERENCE")
    active=[c for c in claims if c.state=="ACTIVE"]
    for i,a in enumerate(active):
        for b in active[i+1:]:
            if a.resource==b.resource and a.area!=b.area and ("EXCLUSIVE" in (a.mode,b.mode)):
                issues.append("CROSS_AREA_RESOURCE_COLLISION:"+a.resource)
    return {"issues":sorted(set(issues)),"automatic_winner":None,
            "requires_owner_reconciliation":bool(issues)}

def can_execute(claim,claims,owner_attested):
    report=assess(claims)
    if not owner_attested or claim.state!="ACTIVE" or report["issues"]:
        return False
    return claim in claims
