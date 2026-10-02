# Concord Contextual Trust Progression — Requiredness and Conformance Evaluation 003

**Project:** The Concord
**Date:** 2 October 2026
**Status:** ACTIVE DEVELOPMENT / CONFORMANCE EVALUATION / NOT CANONICAL
**Target:** Development Model 003

## 1. Objective

Determine whether Model 003 is sufficiently explicit to serialize without recreating ambiguity through omitted fields, null values, inconsistent mixed decisions or implicit prerequisite checks.

## 2. Test method

Construct representative record states and ask whether two materially different meanings can serialize identically.

A failure occurs where:
- NOT_APPLICABLE and NOT_CHECKED can collapse;
- UNKNOWN and negative can collapse;
- corrected and uncorrected evidence can collapse;
- partial and full approval can collapse;
- resource/authority/stewardship reasons can collapse;
- consequential exception checking can be omitted invisibly;
- lifecycle/supersession state can be lost.

## 3. ERR requiredness tests

### E1 — positive direct evidence

All core identity, target, relevance, consequence, freshness, correction and provenance fields present.

**PASS.**

### E2 — irrelevant evidence

RelevanceState = NOT_RELEVANT remains distinct from UNKNOWN.

**PASS.**

### E3 — no evidence

Represented by empty ETR ERR_Set, not fabricated ERR.

**PASS.**

### E4 — corrected adverse evidence

CORRECTED requires CorrectionRef; SUPERSEDED requires SupersedesRef.

**PASS with conditional schema rule required.**

### E5 — recommendation

EvidenceType = RECOMMENDATION survives transfer.

**PASS.**

### E6 — foreign evidence

SourceProviderRef and EvidenceProjectedAt required when cross-provider projection applies.

**PASS conceptually; schema needs applicability/conditional rule.**

### E7 — non-event evidence

ObservationCoverage explicitly prevents "nothing happened" from becoming evidence without known opportunity.

**PASS.**

### E8 — manipulated observation

ObservationIntegrity separates outcome from test integrity.

**PASS.**

### E9 — improperly obtained accurate evidence

EvidenceUseLegitimacy separates predictive/relevance value from legitimate use.

**PASS.**

### E10 — pseudonymous continuity

ESTABLISHED_FOR_PURPOSE does not require civil identity.

**PASS.**

## 4. ETR requiredness tests

### T1 — ordinary bounded approval

All exposure, evidence, prerequisites, decision, effective time and provenance present.

**PASS.**

### T2 — public first offer with no evidence

ERR_Set empty; EvidenceSufficiencyState = NOT_REQUIRED_FOR_TRANSITION; prerequisites explicit.

**PASS.**

### T3 — capacity refusal

ResourcePrerequisite REQUIRED/NOT_SATISFIED and DecisionState DECLINED_RESOURCE_UNAVAILABLE.

Cannot be confused with distrust.

**PASS.**

### T4 — authority refusal

AuthorityPrerequisite REQUIRED/NOT_SATISFIED and DecisionState DECLINED_AUTHORITY_ABSENT.

Cannot be confused with stewardship.

**PASS.**

### T5 — prerequisite not applicable

Applicability = NOT_REQUIRED_FOR_FUNCTION.

Cannot be confused with unperformed check.

**PASS.**

### T6 — required prerequisite unknown

Applicability REQUIRED + State UNKNOWN cannot validate ordinary approval.

**PASS conceptually; schema/harness cross-field validation required.**

### T7 — mixed approval

DimensionTransitions support APPROVED, APPROVED_WITH_CONTROLS and DECLINED in one ETR; overall PARTIALLY_APPROVED_BOUNDED.

**PASS.**

### T8 — controls required

APPROVED_WITH_ADDITIONAL_CONTROLS or dimension APPROVED_WITH_CONTROLS requires non-empty AddedControls at appropriate level.

**PASS conceptually; cross-field validation required.**

### T9 — consequential no adverse exceptions

MaterialAdverseEvidence and MaterialHighConsequenceExceptions explicitly empty.

Checked-none differs from omitted.

**PASS.**

### T10 — participant voluntarily narrows

TransitionTrigger PARTICIPANT_REQUEST; no adverse ERR required.

**PASS.**

### T11 — review missed

ReviewFailureDisposition explicit where review controls continuing exposure.

**PASS.**

### T12 — supersession

PreviousETRRef/SupersedesETRRef preserve chain; old decision remains provenance.

**PASS.**

### T13 — relationship ends

DecisionState ENDED requires EndReason.

**PASS conceptually; conditional validation required.**

## 5. Residual ambiguity found — applicability pattern inside ERR

Model 003 solves prerequisite null ambiguity but several ERR fields still have conditional applicability:
- SourceProviderRef;
- EvidenceProjectedAt;
- CausationState;
- ObservationCoverage;
- CorrectionRef;
- SupersedesRef;
- DisputeRef;
- ReviewOrExpiry.

If represented only as optional fields, omission may mean either not applicable or forgotten.

Not all require heavyweight prerequisite wrappers.

Recommended schema rule:

For semantically important conditional fields, pair with an explicit state/enumeration that makes omission interpretable, or require the field with a defined NOT_APPLICABLE value where its type permits.

Examples:
- CausationState includes NOT_APPLICABLE.
- ObservationCoverage already includes NOT_APPLICABLE.
- ProjectionState = NOT_PROJECTED / PROJECTED / UNKNOWN; when PROJECTED, EvidenceProjectedAt and source projection provenance required.
- CorrectionState controls CorrectionRef requiredness.
- DisputeState controls DisputeRef requiredness.
- ReviewState = NOT_REQUIRED / REQUIRED / UNKNOWN; when REQUIRED, ReviewOrExpiry required.

**Finding:** bounded representational repair, not architectural failure.

## 6. Residual ambiguity found — consequential classification

Several ETR requiredness rules depend on whether a transition is "consequential".

Serialization needs this as explicit data rather than inference from prose.

Add:

ConsequenceClass = LOW / MODERATE / HIGH / CRITICAL / CONTEXT_DEFINED / UNKNOWN

and/or ConsequentialTransition = true/false with basis.

Preferred: structured ConsequenceAssessment containing:
- Classification;
- Basis;
- Consequential = true/false;
- AssessedAt;
- Provenance/PolicyRef where applicable.

This avoids different implementations disagreeing over which fields become required.

**Finding:** required before schema.

## 7. Residual ambiguity found — current versus requested profile completeness

A profile may omit dimensions irrelevant to a function. Schema must distinguish:
- dimension not applicable;
- dimension unchanged;
- dimension unknown;
- dimension omitted accidentally.

Preferred: DimensionTransitions is authoritative for change; profiles may remain function-scoped maps, but every materially requested change must appear in DimensionTransitions.

A validation rule should reject a requested changed dimension not represented in DimensionTransitions.

## 8. Residual ambiguity found — exceptional path

R36 allows independently governed exceptional approval outside ordinary CTP.

The CTP schema should not implement an unspecified emergency override.

Preferred:
- ordinary CTP validation rejects approval with unsatisfied/unknown REQUIRED prerequisite;
- an external exceptional-authority system may create a separate authority/event record and then present the prerequisite as satisfied under that independent basis.

**Exceptional Path != CTP Bypass Flag**

This prevents a generic override boolean from becoming a back door.

## 9. Required repairs before schema

1. Add NOT_APPLICABLE to CausationState.
2. Add ProjectionState and conditional projection requiredness.
3. Ensure DisputeState is explicit and controls DisputeRef.
4. Add ReviewState controlling ReviewOrExpiry.
5. Add explicit ConsequenceAssessment to ETR.
6. Make DimensionTransitions authoritative for all material requested changes.
7. Remove any implication of an internal CTP exceptional-override flag.

## 10. Conformance invariants

**CTP-85** Conditional Omission Must Not Carry Ambiguous Semantic State.
**CTP-86** Consequentiality Must Be Explicit Before Consequence-Dependent Requiredness Is Applied.
**CTP-87** Every Material Requested Exposure Change Must Have A DimensionTransition.
**CTP-88** Exceptional Authority != CTP Override.
**CTP-89** Projected Evidence Must Declare Projection State.
**CTP-90** Required Review Must Declare Review State And Route/Time.
**CTP-91** Required Dispute Linkage Must Follow Explicit Dispute State.

## 11. Result

The conformance pass found **no new architectural layer** and no failure of ERR/ETR separation.

It did find seven bounded serialization ambiguities, all resolvable before schema construction.

The architecture is therefore at a stable formalisation floor, but Model 003 should not be serialized literally without the listed repairs.

## 12. Disposition

**Broad discovery:** CLOSED.
**Model architecture:** STABLE.
**Requiredness evaluation:** PASS WITH BOUNDED REPAIRS.
**Schema immediately from Model 003:** NO.
**Next:** produce Model 004 as serialization-ready normative record model containing only these repairs; then build Schema 001 + fixtures + deterministic cross-field validator.
