# Concord Contextual Trust Progression — Normative Record Model 004

**Project:** The Concord
**Domain:** Research / Participation and Intelligence
**Date:** 2 October 2026
**Version:** 0.4
**Status:** ACTIVE DEVELOPMENT / SERIALIZATION-READY NORMATIVE RECORD MODEL / NOT CANONICAL
**Predecessor:** Development Model 003
**Revision basis:** Requiredness and Conformance Evaluation 003

## 1. Scope

Model 004 makes only the bounded representational repairs required by Conformance Evaluation 003.

No new trust abstraction, authority source, resource entitlement, civil standing or universal reputation mechanism is introduced.

Core architecture:

**Evidence -> Evidence Relevance Record (ERR) -> Exposure Transition Record (ETR)**

**Evidence != Permission**

## 2. ERR normative record

ERR = <
RecordMeta,
ERR_ID,
EvidenceRef,
EvidenceType,
SubjectRelationshipRef,
ProjectionState,
SourceProviderRef,
SourceFunction,
SourceContext,
EvidenceObservedAt,
EvidenceProjectedAt,
AcquisitionBasis,
EvidenceUseLegitimacy,
ObservationConditions,
ObservationIntegrity,
ObservationCoverage,
TargetFunction,
TargetContext,
TargetExposureDimension,
RelevanceState,
RelevanceBasis,
ConsequenceCompatibility,
FreshnessState,
IdentityContinuityState,
CausationState,
CorrectionState,
CorrectionRef,
SupersedesRef,
DisputeState,
DisputeRef,
Provenance,
AssessmentTime,
ReviewState,
ReviewOrExpiry
>

## 3. ProjectionState

Required:
- NOT_PROJECTED
- PROJECTED
- UNKNOWN

If PROJECTED:
- SourceProviderRef required;
- EvidenceProjectedAt required;
- projection provenance required.

If NOT_PROJECTED, those projection-specific fields may be absent.

**Projected Evidence Must Declare Projection State**

## 4. CausationState

Required:
- PARTICIPANT_CAUSAL
- SERVICE_CAUSAL
- SHARED_CAUSAL
- EXTERNAL_CAUSAL
- NO_FAILURE
- NOT_APPLICABLE
- UNKNOWN
- DISPUTED

This removes omission ambiguity.

## 5. ObservationCoverage

Required:
- SUFFICIENT_FOR_ASSERTED_SCOPE
- PARTIAL
- MINIMAL
- UNKNOWN
- NOT_APPLICABLE
- DISPUTED

For NON_EVENT_OBSERVATION, NOT_APPLICABLE is invalid.

## 6. Correction linkage

CorrectionState required:
- NONE_REQUIRED
- UNCORRECTED
- CORRECTED
- PARTIALLY_CORRECTED
- SUPERSEDED
- DISPUTED
- UNKNOWN

If CORRECTED or PARTIALLY_CORRECTED, CorrectionRef required.

If SUPERSEDED, SupersedesRef required.

Historical evidence remains provenance; active interpretation follows the correction/supersession relation.

## 7. Dispute linkage

DisputeState required:
- NONE
- OPEN
- RESOLVED
- UNKNOWN

If OPEN or RESOLVED and the dispute is material to consequential use, DisputeRef required.

## 8. ReviewState

Required:
- NOT_REQUIRED
- REQUIRED
- UNKNOWN

If REQUIRED, ReviewOrExpiry required.

**Required Review Must Declare Review State And Route/Time**

## 9. Remaining ERR vocabularies

EvidenceType:
DIRECT_BEHAVIOURAL / SERVICE_OPERATION / INDEPENDENT_ATTESTATION / RECOMMENDATION / PARTICIPANT_DECLARATION / AUDIT_RESULT / TEST_RESULT / INCIDENT / REPAIR_OR_RECOVERY / NON_EVENT_OBSERVATION / HISTORICAL_RECORD / OTHER_DECLARED.

EvidenceUseLegitimacy:
LEGITIMATE_FOR_TARGET_USE / LEGITIMATE_WITH_LIMITS / NOT_LEGITIMATE_FOR_TARGET_USE / UNKNOWN / DISPUTED.

ObservationIntegrity:
VALID / QUESTIONED / COMPROMISED / UNKNOWN / DISPUTED.

RelevanceState:
DIRECTLY_RELEVANT / PARTIALLY_RELEVANT / CONTEXT_LIMITED / NOT_RELEVANT / UNKNOWN / DISPUTED.

ConsequenceCompatibility:
SAME_OR_LOWER_CONSEQUENCE / PARTIALLY_COMPARABLE / HIGHER_CONSEQUENCE_REQUIRES_ADDITIONAL_EVIDENCE / NOT_COMPARABLE / UNKNOWN.

IdentityContinuityState:
ESTABLISHED_FOR_PURPOSE / PARTIAL / UNKNOWN / DISPUTED / NOT_REQUIRED_FOR_FUNCTION.

## 10. ETR normative record

ETR = <
RecordMeta,
ETR_ID,
RelationshipRef,
TransitionTrigger,
CurrentExposureProfile,
RequestedExposureProfile,
DimensionTransitions,
LegitimateFunctionOrRequest,
ConsequenceAssessment,
ERR_Set,
MaterialAdverseEvidence,
MaterialHighConsequenceExceptions,
EvidenceSufficiencyState,
ResourcePrerequisite,
SelfStewardshipPrerequisite,
AuthorityPrerequisite,
CompositionPrerequisite,
ContestabilityPrerequisite,
PrivacyBoundary,
AddedControls,
DecisionState,
DecisionBasis,
RecoveryRoute,
ExitRoute,
EffectiveTime,
ReviewState,
ReviewTime,
ReviewFailureDisposition,
ExpiryIfAny,
PreviousETRRef,
SupersedesETRRef,
EndReason,
Provenance
>

## 11. ConsequenceAssessment

Required:

ConsequenceAssessment = <
Classification,
Consequential,
Basis,
AssessedAt,
PolicyOrProvenanceRef
>

Classification:
- LOW
- MODERATE
- HIGH
- CRITICAL
- CONTEXT_DEFINED
- UNKNOWN

Consequential is explicit boolean.

A host may define its own substantive classification method, but cannot omit whether consequence-dependent requiredness applies.

**Consequentiality Must Be Explicit Before Consequence-Dependent Requiredness Is Applied**

## 12. Exposure profiles and DimensionTransitions

Exposure profiles are function-scoped maps.

DimensionTransitions are authoritative for material changes.

Each material requested change must appear exactly once in DimensionTransitions unless the host specification explicitly defines a compound dimension.

DimensionTransition = <
Dimension,
CurrentState,
RequestedState,
Disposition,
ERR_Refs,
PrerequisiteRefs,
AddedControls,
Basis
>

Disposition:
APPROVED / APPROVED_WITH_CONTROLS / MAINTAIN_CURRENT / NARROWED / SUSPENDED / DECLINED / UNKNOWN / DISPUTED.

**Every Material Requested Exposure Change Must Have A DimensionTransition**

## 13. Mixed decisions

DecisionState:
- APPROVED_BOUNDED
- PARTIALLY_APPROVED_BOUNDED
- APPROVED_WITH_ADDITIONAL_CONTROLS
- MAINTAIN_CURRENT_EXPOSURE
- NARROW_EXPOSURE
- SUSPEND_PENDING_REVIEW
- DECLINED_INSUFFICIENT_RELEVANT_EVIDENCE
- DECLINED_RESOURCE_UNAVAILABLE
- DECLINED_STEWARDSHIP_REQUIREMENT
- DECLINED_AUTHORITY_ABSENT
- BLOCKED_IDENTITY_UNCERTAINTY
- BLOCKED_DISPUTE
- BLOCKED_DEPENDENCY
- ENDED
- UNKNOWN

PARTIALLY_APPROVED_BOUNDED requires materially different DimensionTransition dispositions.

APPROVED_WITH_ADDITIONAL_CONTROLS requires non-empty applicable AddedControls.

Overall decision must be consistent with dimension dispositions.

## 14. Explicit prerequisite wrapper

Every consequential ETR carries all five wrappers:

Prerequisite = <
Applicability,
State,
BasisRef,
CheckedAt,
ExpiryOrReview,
DisputeState
>

Applicability:
- REQUIRED
- NOT_REQUIRED_FOR_FUNCTION
- UNKNOWN

State:
- SATISFIED
- PARTIALLY_SATISFIED
- NOT_SATISFIED
- UNKNOWN
- DISPUTED
- NOT_APPLICABLE

Rule:
If Applicability = NOT_REQUIRED_FOR_FUNCTION, State must equal NOT_APPLICABLE.

If Applicability = REQUIRED, State must not equal NOT_APPLICABLE.

Ordinary approval is invalid if a REQUIRED prerequisite is UNKNOWN, NOT_SATISFIED or DISPUTED.

PARTIALLY_SATISFIED may support approval only where the relevant policy explicitly permits it and adequate controls/basis are represented.

**NOT_APPLICABLE != NOT_CHECKED**

## 15. No CTP override

Model 004 contains no emergencyOverride, adminOverride, trustOverride or equivalent bypass field.

If exceptional authority legitimately changes a prerequisite, that authority must be established externally and referenced as the independent basis.

**Exceptional Authority != CTP Override**

## 16. Evidence set and exception fields

ERR_Set is required and may be empty.

EvidenceSufficiencyState:
- SUFFICIENT_FOR_REQUESTED_EXPOSURE
- CONDITIONALLY_SUFFICIENT
- INSUFFICIENT
- NOT_REQUIRED_FOR_TRANSITION
- UNKNOWN
- DISPUTED

For Consequential = true:
- MaterialAdverseEvidence required, empty allowed;
- MaterialHighConsequenceExceptions required, empty allowed;
- all prerequisite wrappers required.

Explicit empty means checked-and-none.

Omission is not equivalent.

## 17. Review state

ETR ReviewState:
- NOT_REQUIRED
- REQUIRED
- UNKNOWN

If REQUIRED:
- ReviewTime or a declared review condition required;
- ReviewFailureDisposition required.

ReviewFailureDisposition:
CONTINUE_TEMPORARILY_UNDER_EXISTING_BOUND / DEGRADE_TO_DECLARED_SAFE_BOUND / SUSPEND_AFFECTED_DIMENSIONS / EXPIRE_AFFECTED_DIMENSIONS / REQUIRE_EXCEPTIONAL_REVIEW / NOT_APPLICABLE.

If ReviewState = NOT_REQUIRED, ReviewFailureDisposition = NOT_APPLICABLE.

## 18. Transition lifecycle

TransitionTrigger:
PARTICIPANT_REQUEST / PROVIDER_REVIEW / NEW_EVIDENCE / CORRECTION / DISPUTE / EXPIRY / RESOURCE_CHANGE / AUTHORITY_CHANGE / SAFETY_CHANGE / EMERGENCY / SUCCESSION / PARTICIPANT_EXIT / PROVIDER_CLOSURE / OTHER_DECLARED.

PreviousETRRef and SupersedesETRRef preserve transition history.

DecisionState = ENDED requires EndReason:
PARTICIPANT_EXIT / MUTUAL_END / PROVIDER_CLOSURE / SUCCESSION / SERVICE_RETIRED / FUNCTION_ENDED / OTHER_DECLARED / UNKNOWN.

**Terminal Relationship State != Adverse Trust Finding**

## 19. Normative cross-field rules

N1. ERR RelevanceState UNKNOWN must never be normalized to NOT_RELEVANT or adverse.
N2. EvidenceType RECOMMENDATION remains recommendation through transfer.
N3. ProjectionState PROJECTED requires SourceProviderRef and EvidenceProjectedAt.
N4. NON_EVENT_OBSERVATION cannot use ObservationCoverage NOT_APPLICABLE.
N5. CORRECTED/PARTIALLY_CORRECTED requires CorrectionRef.
N6. SUPERSEDED requires SupersedesRef.
N7. ReviewState REQUIRED requires ReviewOrExpiry for ERR.
N8. ETR ConsequenceAssessment required.
N9. Consequential ETR requires explicit exception arrays and all prerequisite wrappers.
N10. Every material requested exposure change requires DimensionTransition.
N11. Partial approval requires mixed dimension dispositions.
N12. Conditional approval requires explicit controls.
N13. REQUIRED prerequisite UNKNOWN/NOT_SATISFIED/DISPUTED cannot support ordinary approval.
N14. NOT_REQUIRED_FOR_FUNCTION prerequisite must use State NOT_APPLICABLE.
N15. CTP itself cannot be AuthorityPrerequisite BasisRef.
N16. ENDED requires EndReason.
N17. ETR ReviewState REQUIRED requires review condition/time and ReviewFailureDisposition.
N18. Empty ERR_Set is valid and non-adverse.
N19. EvidenceSufficiencyState NOT_REQUIRED_FOR_TRANSITION permits empty ERR_Set.
N20. Decision provenance must remain even where raw evidence is later governed by external lifecycle rules.

## 20. Serialization boundary

A JSON schema may enforce:
- types;
- required fields;
- enumerations;
- structural conditional requiredness;
- basic if/then relations.

A deterministic conformance validator should enforce:
- cross-record references;
- overall/dimension decision consistency;
- material requested-change coverage;
- prerequisite/decision compatibility;
- prohibited circular authority basis;
- recommendation type preservation where traceable;
- correction/supersession referential integrity;
- consequential exception-field semantics.

**Schema Validation != Full Semantic Conformance**

## 21. Status

**Broad discovery:** CLOSED.
**Normative record model:** SERIALIZATION-READY CANDIDATE.
**Known requiredness ambiguity:** BOUNDED.
**Next:** JSON Schema 001 + representative fixtures + deterministic validator + results.
**PMEDG:** PREMATURE pending serialization and transfer testing.
