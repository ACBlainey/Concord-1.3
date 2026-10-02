# Concord Contextual Trust Progression — Deterministic Validator 002

Successor to Deterministic Validator 001. Frozen Validator 001 remains unchanged.

## ERR single-record rules

V-ERR-01 PROJECTED requires sourceProviderRef and evidenceProjectedAt.
V-ERR-02 CORRECTED/PARTIALLY_CORRECTED requires correctionRef.
V-ERR-03 SUPERSEDED requires supersedesRef.
V-ERR-04A disputeState NONE requires disputeMateriality NOT_APPLICABLE.
V-ERR-04B disputeState OPEN/RESOLVED forbids disputeMateriality NOT_APPLICABLE.
V-ERR-04C OPEN/RESOLVED plus MATERIAL_TO_TARGET_USE requires disputeRef.
V-ERR-05 NON_EVENT_OBSERVATION forbids observationCoverage NOT_APPLICABLE.
V-ERR-06 reviewState REQUIRED requires reviewOrExpiry.

## ERR cross-record rule

V-ERR-07 Recommendation evidence must remain typed RECOMMENDATION through projection/import.

This rule requires lineage/source-record context. A single-record validator must report it as NOT_EVALUABLE_SINGLE_RECORD rather than silently treating it as passed.

## ETR single-record rules

V-ETR-01 Every materially changed requested exposure dimension must have exactly one DimensionTransition.
V-ETR-02 PARTIALLY_APPROVED_BOUNDED requires mixed dispositions, with at least one approved/approved-with-controls and one non-approved.
V-ETR-03 APPROVED_WITH_ADDITIONAL_CONTROLS requires non-empty addedControls.
V-ETR-04 APPROVED_WITH_CONTROLS dimension requires dimension or applicable record controls.
V-ETR-05 NOT_REQUIRED_FOR_FUNCTION requires NOT_APPLICABLE state.
V-ETR-06 REQUIRED forbids NOT_APPLICABLE state.
V-ETR-07 ordinary approval cannot rely on REQUIRED UNKNOWN/NOT_SATISFIED/DISPUTED prerequisite.
V-ETR-08 in partial approval, an approved dimension cannot depend on a REQUIRED UNKNOWN/NOT_SATISFIED/DISPUTED prerequisite referenced by that dimension.
V-ETR-09 consequential=true requires all five prerequisite wrappers and both material exception arrays.
V-ETR-10 REQUIRED review requires reviewTime and non-NOT_APPLICABLE reviewFailureDisposition.
V-ETR-11 NOT_REQUIRED review permits only NOT_APPLICABLE reviewFailureDisposition when present.
V-ETR-12 ENDED requires endReason.
V-ETR-13 authorityPrerequisite.basisRef cannot identify CTP or the current ETR itself as sole authority basis.
V-ETR-14 empty errSet is valid and non-adverse.
V-ETR-15 NOT_REQUIRED_FOR_TRANSITION permits empty errSet.
V-ETR-16 overall decision must be consistent with dimension dispositions.
V-ETR-17 participant-requested narrowing must not require materialAdverseEvidence.

## Determinism boundary

Rules dependent on host-defined materiality of exposure-profile changes require a deterministic comparison declaration or host profile. The reference harness shall compare explicit profile keys/values and require DimensionTransitions for changed dimensions.

Cross-record lineage integrity remains a record-set validation concern.

Schema Validation != Full Semantic Conformance
Single-Record Validation != Cross-Record Validation
