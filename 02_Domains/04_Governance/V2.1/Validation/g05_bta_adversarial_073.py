"""Adversarial BTA record checks: explicitly a fixture-level guard, not an authority engine."""
import copy
from g05_bta_compat_adapter_072 import read_fixture, project

def audit(record):
    issues=[]
    if not isinstance(record,dict):
        return ["RECORD_INVALID"]
    if not record.get("TransitionID") or not isinstance(record.get("Scope"),dict):
        issues.append("IDENTITY_OR_SCOPE_MISSING")
    if not isinstance(record.get("Provenance"),dict) or not record["Provenance"].get("HistoricalRef"):
        issues.append("PROVENANCE_MISSING")
    if record.get("UncertaintyOrDisputeState",{}).get("State")=="UNRESOLVED" and not record.get("ProtectedUnresolvedStateRefs"):
        issues.append("UNRESOLVED_UNPROTECTED")
    if record.get("PendingStateRefs") and record.get("DeclaredComplete") is True:
        issues.append("PENDING_BUT_DECLARED_COMPLETE")
    if record.get("TerminatedAuthorityRefs") and record.get("DeclaredAuthorityActive") is True:
        issues.append("TERMINATED_AUTHORITY_REACTIVATION_CLAIM")
    if record.get("ExternalityReviewRefs") and record.get("ExternalConsequenceRefs"):
        issues.append("REVIEW_AND_CONSEQUENCE_REQUIRE_OWNER_RECONCILIATION")
    if not record.get("TransitionBasisRefs"):
        issues.append("BASIS_MISSING_REVIEW")
    if project(record)["unresolved_legacy_fields"]:
        issues.append("LEGACY_SEMANTIC_MAPPING_UNRESOLVED")
    return issues

def consequential_clearance(record):
    """Never grants authority or completion; reports need for owner verification."""
    return {"authorised":False,"complete":False,"requires_owner_review":True,"issues":audit(record)}
