# Concord Contextual Trust Progression — Development Model 003

**Project:** The Concord
**Domain:** Research / Participation and Intelligence
**Date:** 2 October 2026
**Version:** 0.3
**Status:** ACTIVE DEVELOPMENT / FORMAL MODEL / NOT CANONICAL
**Predecessor:** Concord Contextual Trust Progression — Development Model 002
**Revision basis:** Pre-Schema Adversarial Evaluation 002

## 1. Purpose

Model 003 incorporates the representational repairs found before serialization.

The architecture remains:

**Evidence -> Evidence Relevance Record (ERR) -> Exposure Transition Record (ETR)**

The separation is mandatory.

**Evidence != Permission**

**Evidence Relevance Assessment != Exposure Decision**

No universal participant trust score is defined.

## 2. Evidence Relevance Record — ERR 003

Conceptual record:

ERR = <
RecordMeta,
ERR_ID,
EvidenceRef,
EvidenceType,
SubjectRelationshipRef,
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
ReviewOrExpiry
>

## 3. ERR field semantics

### 3.1 EvidenceType

Candidate values:
- DIRECT_BEHAVIOURAL
- SERVICE_OPERATION
- INDEPENDENT_ATTESTATION
- RECOMMENDATION
- PARTICIPANT_DECLARATION
- AUDIT_RESULT
- TEST_RESULT
- INCIDENT
- REPAIR_OR_RECOVERY
- NON_EVENT_OBSERVATION
- HISTORICAL_RECORD
- OTHER_DECLARED

A recommendation cannot silently become direct behavioural evidence.

**Recommendation != Transferred Trust**

**Foreign Conclusion != Direct Behavioural Evidence**

### 3.2 SourceProviderRef

Required when evidence originates from another provider or service relationship.

Absence is legitimate only when not applicable and that state is explicit in serialization.

### 3.3 EvidenceObservedAt and EvidenceProjectedAt

EvidenceObservedAt records when the underlying observation occurred or the relevant observation interval.

EvidenceProjectedAt records when a provider produced/shared a contextual evidence projection, where applicable.

**Observation Time != Projection Time**

### 3.4 AcquisitionBasis

Records the declared basis under which evidence was acquired, such as:
- ORDINARY_SERVICE_OPERATION
- VOLUNTARY_TEST
- REQUIRED_BOUNDED_AUDIT
- INDEPENDENT_PUBLIC_EVIDENCE
- EMERGENCY_AUTHORISED
- OTHER_DECLARED
- UNKNOWN
- DISPUTED

This does not itself prove legitimacy.

### 3.5 EvidenceUseLegitimacy

Candidate states:
- LEGITIMATE_FOR_TARGET_USE
- LEGITIMATE_WITH_LIMITS
- NOT_LEGITIMATE_FOR_TARGET_USE
- UNKNOWN
- DISPUTED

**Evidence Accuracy != Legitimate Evidence Use**

Accurate but improperly obtained evidence cannot become automatically usable merely because it predicts well.

### 3.6 ObservationIntegrity

Candidate states:
- VALID
- QUESTIONED
- COMPROMISED
- UNKNOWN
- DISPUTED

This captures manipulated or unreliable test/observation conditions separately from the observed outcome.

**Observation Result != Observation Integrity**

### 3.7 ObservationCoverage

For NON_EVENT_OBSERVATION and other coverage-sensitive evidence, record the opportunity/coverage relevant to interpretation.

Candidate state:
- SUFFICIENT_FOR_ASSERTED_SCOPE
- PARTIAL
- MINIMAL
- UNKNOWN
- NOT_APPLICABLE
- DISPUTED

**Absence Of Recorded Incident != Evidence Without Observation Opportunity/Coverage**

### 3.8 RelevanceState

- DIRECTLY_RELEVANT
- PARTIALLY_RELEVANT
- CONTEXT_LIMITED
- NOT_RELEVANT
- UNKNOWN
- DISPUTED

UNKNOWN is not adverse.

### 3.9 ConsequenceCompatibility

- SAME_OR_LOWER_CONSEQUENCE
- PARTIALLY_COMPARABLE
- HIGHER_CONSEQUENCE_REQUIRES_ADDITIONAL_EVIDENCE
- NOT_COMPARABLE
- UNKNOWN

**Quantity Of Low-Consequence Success != Evidence For High-Consequence Exposure**

### 3.10 IdentityContinuityState

- ESTABLISHED_FOR_PURPOSE
- PARTIAL
- UNKNOWN
- DISPUTED
- NOT_REQUIRED_FOR_FUNCTION

This is functional continuity, not a demand for universal/civil identity.

### 3.11 CausationState

- PARTICIPANT_CAUSAL
- SERVICE_CAUSAL
- SHARED_CAUSAL
- EXTERNAL_CAUSAL
- NO_FAILURE
- UNKNOWN
- DISPUTED

### 3.12 Correction and dispute linkage

CorrectionState:
- NONE_REQUIRED
- UNCORRECTED
- CORRECTED
- PARTIALLY_CORRECTED
- SUPERSEDED
- DISPUTED
- UNKNOWN

If CORRECTED, PARTIALLY_CORRECTED or SUPERSEDED is consequentially relied upon, CorrectionRef or SupersedesRef must identify the relevant correction relation.

DisputeRef should identify material dispute state where applicable.

**Correction State Without Correction Link Is Insufficient For Consequential Use**

## 4. Exposure Transition Record — ETR 003

Conceptual record:

ETR = <
RecordMeta,
ETR_ID,
RelationshipRef,
TransitionTrigger,
CurrentExposureProfile,
RequestedExposureProfile,
DimensionTransitions,
LegitimateFunctionOrRequest,
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
ReviewTime,
ReviewFailureDisposition,
ExpiryIfAny,
PreviousETRRef,
SupersedesETRRef,
EndReason,
Provenance
>

## 5. TransitionTrigger

Candidate values:
- PARTICIPANT_REQUEST
- PROVIDER_REVIEW
- NEW_EVIDENCE
- CORRECTION
- DISPUTE
- EXPIRY
- RESOURCE_CHANGE
- AUTHORITY_CHANGE
- SAFETY_CHANGE
- EMERGENCY
- SUCCESSION
- PARTICIPANT_EXIT
- PROVIDER_CLOSURE
- OTHER_DECLARED

**Voluntary Narrowing != Adverse Evidence**

## 6. Exposure profiles

Exposure profile dimensions may include:
- ResourceQuantity
- Duration
- Frequency
- Autonomy
- NetworkReach
- DataSensitivity
- CredentialAccess
- FinancialValue
- AffectedParties
- Reversibility
- ExternalConsequence
- AuthorityScope
- ObservationConditions
- OtherDeclaredDimensions

A transition must identify materially changed dimensions.

## 7. DimensionTransition

Each materially changed dimension should be represented as:

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

Candidate Disposition:
- APPROVED
- APPROVED_WITH_CONTROLS
- MAINTAIN_CURRENT
- NARROWED
- SUSPENDED
- DECLINED
- UNKNOWN
- DISPUTED

**Mixed-Dimension Transition != Single Undifferentiated Approval**

## 8. Overall DecisionState

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

Overall state must be consistent with DimensionTransitions.

## 9. AddedControls

Conditional approval must expose controls that materially make approval valid.

Examples:
- sandboxing;
- transaction cap;
- destination allowlist;
- human/AI co-approval;
- shorter duration;
- reduced quota;
- additional audit;
- staged release;
- stronger recovery checkpoint.

**Conditional Approval Must Expose Its Added Controls**

## 10. Explicit prerequisite wrapper

Every consequential prerequisite interface uses:

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

State when REQUIRED:
- SATISFIED
- PARTIALLY_SATISFIED
- NOT_SATISFIED
- UNKNOWN
- DISPUTED

A blank/null value must not carry semantic meaning.

**NOT_APPLICABLE != NOT_CHECKED**

For ordinary approval:

If Applicability = REQUIRED, State must be SATISFIED or an explicitly permitted PARTIALLY_SATISFIED state paired with adequate controls and policy basis.

**Required Unknown Prerequisite != Ordinary Approval**

## 11. ResourcePrerequisite

References resource/capacity/admission architecture.

A lack of capacity may decline the transition without altering trust evidence.

**Resource Shortage != Distrust**

## 12. SelfStewardshipPrerequisite

References the relevant self-stewardship determination where required.

CTP may provide evidence but cannot define the substantive requirement.

**CTP != Self-Stewardship**

## 13. AuthorityPrerequisite

References independent authority basis where the exposure includes consequential action requiring authority.

AuthorityBasisRef cannot derive solely from CTP/ETR approval.

**Trust Progression Cannot Be Its Own Authority Basis**

**Authority Absence != Stewardship Failure**

## 14. CompositionPrerequisite

Required where individually acceptable capabilities may compose into materially different consequence.

**Trusted Components != Trusted Composition**

CBPR remains the primary runtime composition interface.

## 15. ContestabilityPrerequisite

Required where a consequential classification/decision must be contestable.

This records whether an appropriate review/correction route exists; it does not imply every low-consequence action requires formal adjudication.

## 16. Evidence set semantics

ERR_Set may be empty.

An empty set means no ERR is being relied upon. It is not adverse evidence.

**Empty Evidence Set != Adverse Evidence**

For Bounded First Trust or public non-rival informational access, evidence may legitimately be unnecessary.

EvidenceSufficiencyState:
- SUFFICIENT_FOR_REQUESTED_EXPOSURE
- CONDITIONALLY_SUFFICIENT
- INSUFFICIENT
- NOT_REQUIRED_FOR_TRANSITION
- UNKNOWN
- DISPUTED

## 17. Material exception fields

For consequential transitions, MaterialAdverseEvidence and MaterialHighConsequenceExceptions must be explicitly present, even when empty.

This distinguishes:
- checked and none found;
from
- not checked/omitted.

**Consequential Decision Must Preserve Material Exceptions**

## 18. Review failure

Where continuing exposure depends on periodic review, ReviewFailureDisposition should state what happens if review does not occur.

Candidate values:
- CONTINUE_TEMPORARILY_UNDER_EXISTING_BOUND
- DEGRADE_TO_DECLARED_SAFE_BOUND
- SUSPEND_AFFECTED_DIMENSIONS
- EXPIRE_AFFECTED_DIMENSIONS
- REQUIRE_EXCEPTIONAL_REVIEW
- NOT_APPLICABLE

No universal policy is imposed; the behaviour must be explicit where material.

## 19. Supersession

A new ETR may supersede a prior ETR before its planned review/expiry.

PreviousETRRef preserves chain continuity.

SupersedesETRRef identifies a transition whose active effect is replaced.

Historical ETR remains provenance.

**Superseded Decision != Erased Decision**

## 20. EndReason

When DecisionState = ENDED, candidate reasons:
- PARTICIPANT_EXIT
- MUTUAL_END
- PROVIDER_CLOSURE
- SUCCESSION
- SERVICE_RETIRED
- FUNCTION_ENDED
- OTHER_DECLARED
- UNKNOWN

Ending a relationship is not inherently adverse evidence.

## 21. Privacy-preserving progression

A participant may choose not to generate evidence beyond the minimum legitimate observation.

Unobserved dimensions may remain UNTESTED.

**Unobserved != Unsafe**
**UNTESTED != UNTRUSTWORTHY**
**Privacy Choice != Adverse Trust Evidence**

Where a requested consequential exposure genuinely requires more evidence, the system should offer the least intrusive practicable evidence-generation path.

## 22. Cross-provider rule

A receiving provider must perform its own target-context relevance assessment.

It may receive:
- source evidence projection;
- recommendation;
- audit result;
- other legitimate evidence.

It may not import another provider's universal conclusion because no such universal CTP conclusion exists.

**Provider Federation != Reputation Federation**

**Foreign Trust Conclusion != Local Evidence Relevance Determination**

## 23. Recommendation chains

Recommendation evidence must remain typed as recommendation evidence through chains.

A recommendation may be relevant, but does not recursively transform into direct behavioural evidence.

A->B recommendation plus C's trust in A does not equal C's direct trust in B.

## 24. Evidence-use legitimacy

ERR separates:
- whether evidence is accurate/relevant;
from
- whether it may legitimately be used for the target decision.

This prevents surveillance or improperly obtained data from becoming self-justifying merely because it predicts behaviour.

## 25. Observation integrity

Where test/observation conditions are manipulated, compromised or uncertain, ObservationIntegrity preserves that state.

The model must not silently treat a compromised observation as ordinary evidence.

## 26. Recovery

If a restriction is represented as recoverable, RecoveryRoute should identify a feasible path where one exists:
- condition to resolve;
- evidence that could resolve it;
- realistic evidence-generation route;
- reviewer/process;
- correction/dispute route;
- review condition/time.

**Nominal Recovery != Effective Recovery**

## 27. Worked mixed-transition example

Current:
- 1 compute unit;
- no network;
- no credentials.

Request:
- 4 compute units;
- allowlisted network;
- payment credential.

Relevant evidence:
- strong bounded offline compute history;
- no network history;
- no financial credential evidence.

Possible DimensionTransitions:

Compute:
APPROVED — directly relevant evidence, capacity available.

Network:
APPROVED_WITH_CONTROLS — limited allowlist, bounded duration, additional audit.

Credential:
DECLINED — insufficient relevant evidence and/or authority basis absent.

Overall:
PARTIALLY_APPROVED_BOUNDED.

The participant is not labelled "partly trustworthy". The decision is about three bounded exposure dimensions.

## 28. Requiredness rules before serialization

R1. ERR_ID required.
R2. EvidenceRef required except for a formally defined evidence-summary type that itself has provenance.
R3. EvidenceType required.
R4. SubjectRelationshipRef required.
R5. TargetFunction and TargetContext required.
R6. RelevanceState required.
R7. ConsequenceCompatibility required.
R8. FreshnessState required.
R9. IdentityContinuityState required.
R10. CausationState required where incident/failure interpretation is material; otherwise explicit NOT_APPLICABLE will be needed in schema vocabulary.
R11. CorrectionState required.
R12. Provenance required.
R13. AssessmentTime required.
R14. ETR_ID required.
R15. RelationshipRef required.
R16. TransitionTrigger required.
R17. CurrentExposureProfile required.
R18. RequestedExposureProfile required except for terminal/end transitions where explicit NOT_APPLICABLE representation is used.
R19. DimensionTransitions required; may be empty only for defined non-dimensional lifecycle transitions.
R20. LegitimateFunctionOrRequest required.
R21. ERR_Set required but may be empty.
R22. EvidenceSufficiencyState required.
R23. MaterialAdverseEvidence required for consequential transitions; empty allowed.
R24. MaterialHighConsequenceExceptions required for consequential transitions; empty allowed.
R25. All five prerequisite wrappers required for consequential transitions, each with explicit Applicability.
R26. DecisionState required.
R27. DecisionBasis required.
R28. AddedControls required as a field for approvals; empty allowed.
R29. EffectiveTime required.
R30. Review/expiry applicability must be explicit.
R31. Provenance required.
R32. If DecisionState = ENDED, EndReason required.
R33. If correction/supersession state asserts a link, the link reference is required.
R34. If approval is partial, DimensionTransitions must contain at least two materially different dispositions.
R35. If approval depends on controls, AddedControls must be non-empty.
R36. If a REQUIRED prerequisite is UNKNOWN/NOT_SATISFIED, ordinary APPROVED states are invalid unless an independently governed exceptional path is explicitly represented outside ordinary CTP approval.

## 29. Invariants

Model 003 inherits CTP-01 through CTP-73.

Additional:

**CTP-74** Observation Time != Projection Time.
**CTP-75** Recommendation Type Must Survive Recommendation Chains.
**CTP-76** Explicit Prerequisite State != Nullable Prerequisite.
**CTP-77** Superseded Decision != Erased Decision.
**CTP-78** Overall Decision Must Be Consistent With Dimension Dispositions.
**CTP-79** Evidence Use Legitimacy != Evidence Predictiveness.
**CTP-80** Terminal Relationship State != Adverse Trust Finding.
**CTP-81** Review Failure Behaviour Must Be Declared Where Continued Consequential Exposure Depends On Review.
**CTP-82** Evidence Projection Must Preserve Material Correction And Dispute Context.
**CTP-83** Consequential Empty Exception Set Means Checked-And-None, Not Omitted.
**CTP-84** Partial Approval != Partial Person-Level Trustworthiness.

## 30. Architecture disposition

The trust problem has now separated into existing Concord systems plus one bounded progression function:

- Bounded First Trust: starts interaction.
- CTP: relates evidence to bounded next exposure.
- Self-Stewardship: evaluates relevant consequential stewardship.
- Resource Capacity/Admission: evaluates scarce capacity.
- Authority architecture: supplies legitimate authority.
- CBPR: bounds runtime consequence/composition.
- CIBB: governs protected evidence.
- Contestability: correction/review.
- Historical: provenance.
- BSR: service-side live evidence/status.

CTP does not replace any of them.

## 31. Development disposition

**Broad discovery:** CLOSED unless new evidence exposes another layer.
**ERR/ETR architecture:** STABLE CANDIDATE.
**Requiredness:** EXPLICIT ENOUGH FOR CONFORMANCE TEST.
**Serialization:** PENDING REQUIREDNESS/CONFORMANCE PASS.
**PMEDG:** PREMATURE until serialization and transfer testing.

Next action: Requiredness and Conformance Evaluation 003. If no structural ambiguity remains, create the first serialization/schema candidate and fixtures rather than continuing prose development.
