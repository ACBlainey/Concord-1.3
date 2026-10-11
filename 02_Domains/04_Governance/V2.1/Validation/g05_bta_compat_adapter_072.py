"""Conservative projection of legacy BTA MRT-003 to v1.0 candidate field names.
The source record is never modified. Only unambiguous keys are projected.
Requires PyYAML. This is an interoperability experiment, not an authority engine.
"""
import copy
import pathlib
import yaml

HERE = pathlib.Path(__file__).resolve().parent
FIXTURE = HERE / "G05_BTA_Original_MRT003_Fixture_070.yaml"
LEGACY_ONLY = {
    "ParticipatingStateSystemRefs",
    "TransitionEpochOrPhaseRefs",
    "ScopedValidationRefs",
    "ExternalityReviewRefs",
    "ClockTransitionRelationRefs",
    "RollbackOrRecoveryRefs",
}
GRADUATED_ONLY = {
    "ParticipatingOwnerRefs",
    "TransitionPhaseRefs",
    "ValidationRefs",
    "ExternalConsequenceRefs",
    "TemporalRelationRefs",
    "RecoveryRefs",
}
def read_fixture():
    return yaml.safe_load(FIXTURE.read_text(encoding="utf-8"))["BoundedTransitionContract"]

def project(record):
    """Return a non-authoritative projection plus unresolved legacy fields."""
    source = copy.deepcopy(record)
    projected = {k: copy.deepcopy(v) for k,v in source.items() if k not in LEGACY_ONLY}
    unresolved = {k: copy.deepcopy(v) for k,v in source.items() if k in LEGACY_ONLY}
    return {"source": source, "graduated_shared_fields": projected,
            "unresolved_legacy_fields": unresolved,
            "semantics_verified": False}

def consequentially_complete(record):
    """Conservative fixture gate; NOT a general BTA completion algorithm."""
    if record.get("PendingStateRefs") or record.get("CompletionConditionRefs"):
        return False
    if record.get("UncertaintyOrDisputeState", {}).get("State") == "UNRESOLVED":
        return False
    return False  # owner-verified completion evidence is not implemented
