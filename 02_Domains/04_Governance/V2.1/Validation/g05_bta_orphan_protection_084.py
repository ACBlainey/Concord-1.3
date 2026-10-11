"""Temporary protective intervention for an orphaned duty: a negative-authority fixture.

A verified mandate is an external input, never issued by this code.
Emergency operational time remains independent of Civilisation Clock progress.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class ProtectiveMandate:
    duty_id: str
    mandate_ref: str
    issuing_owner: str
    scope: str
    permitted_actions: tuple
    issued_tick: int
    expiry_tick: int
    review_ref: str
    revision: int

def evaluate(mandate,action,now_tick,live_revision,owner_verified,
             necessity_verified,proportionality_verified,clock_paused=True):
    issues=[]
    if not mandate.mandate_ref or not mandate.issuing_owner or not mandate.review_ref:
        issues.append("MANDATE_PROVENANCE_INCOMPLETE")
    if not mandate.duty_id or not mandate.scope:
        issues.append("DUTY_OR_SCOPE_MISSING")
    if now_tick<mandate.issued_tick or now_tick>=mandate.expiry_tick:
        issues.append("OUTSIDE_OPERATIONAL_WINDOW")
    if mandate.expiry_tick<=mandate.issued_tick:
        issues.append("INVALID_TEMPORAL_BOUNDS")
    if mandate.revision!=live_revision:
        issues.append("MANDATE_REVISION_STALE")
    if action not in mandate.permitted_actions:
        issues.append("ACTION_OUT_OF_SCOPE")
    if not owner_verified:
        issues.append("AUTHORITY_NOT_VERIFIED")
    if not necessity_verified:
        issues.append("NECESSITY_NOT_VERIFIED")
    if not proportionality_verified:
        issues.append("PROPORTIONALITY_NOT_VERIFIED")
    return {"issues":issues,"eligible_for_external_execution_review":not issues,
            "permanent_custody_assigned":False,"authority_created":False,
            "clock_advanced":False,"clock_paused":clock_paused}

def expiry_record(mandate,now_tick):
    if now_tick<mandate.expiry_tick:return {"expired":False,"review_due":False}
    return {"expired":True,"review_due":True,
            "surviving_duties":("PROTECTIVE_ACTION_AUDIT","SUCCESSION_REVIEW"),
            "permanent_custody_assigned":False}
