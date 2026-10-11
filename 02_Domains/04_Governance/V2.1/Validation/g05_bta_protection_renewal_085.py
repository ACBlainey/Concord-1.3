"""Emergency protective mandate renewal audit fixture.

Renewal is a NEW decision with a new authority check, never an extension by inertia.
No authority is created or granted by this prototype.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Renewal:
    duty_id: str
    prior_mandate_ref: str
    new_mandate_ref: str
    new_issuer_ref: str
    new_evidence_ref: str
    new_review_ref: str
    necessity_ref: str
    proportionality_ref: str
    start_tick: int
    expiry_tick: int
    revision: int

def review_renewal(prior,renewal,now_tick,owner_verified,live_revision,
                   cumulative_review_verified,independent_review_verified):
    issues=[]
    if renewal.duty_id!=prior.duty_id or renewal.prior_mandate_ref!=prior.mandate_ref:
        issues.append("PRIOR_MANDATE_MISMATCH")
    if not renewal.new_mandate_ref or renewal.new_mandate_ref==prior.mandate_ref:
        issues.append("NEW_MANDATE_REQUIRED")
    if not all((renewal.new_issuer_ref,renewal.new_evidence_ref,renewal.new_review_ref,
                renewal.necessity_ref,renewal.proportionality_ref)):
        issues.append("FRESH_JUSTIFICATION_INCOMPLETE")
    if renewal.start_tick<prior.expiry_tick or renewal.expiry_tick<=renewal.start_tick:
        issues.append("TEMPORAL_BOUNDARY_INVALID")
    if now_tick<renewal.start_tick or now_tick>=renewal.expiry_tick:
        issues.append("RENEWAL_NOT_CURRENT")
    if renewal.revision!=live_revision:
        issues.append("REVISION_STALE")
    if not owner_verified:
        issues.append("NEW_OWNER_VERIFICATION_REQUIRED")
    if not cumulative_review_verified:
        issues.append("CUMULATIVE_EFFECTS_REVIEW_REQUIRED")
    if not independent_review_verified:
        issues.append("INDEPENDENT_REVIEW_REQUIRED")
    return {"issues":issues,"eligible_for_external_approval":not issues,
            "authority_granted":False,"prior_mandate_extended":False,
            "permanent_custody_assigned":False}
