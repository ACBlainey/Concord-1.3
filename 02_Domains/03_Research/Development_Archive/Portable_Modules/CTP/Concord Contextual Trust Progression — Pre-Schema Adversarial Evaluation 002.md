# Concord Contextual Trust Progression — Pre-Schema Adversarial Evaluation 002

**Project:** The Concord
**Date:** 2 October 2026
**Status:** ACTIVE DEVELOPMENT / PRE-SCHEMA ADVERSARIAL EVALUATION / NOT CANONICAL
**Target:** Development Model 002 — ERR and ETR

## 1. Purpose

Test whether the Evidence Relevance Record (ERR) and Exposure Transition Record (ETR) can represent difficult cases without silently manufacturing certainty, permission, distrust or universal reputation.

## 2. Core tests and results

**Unknown target relevance:** represent RelevanceState = UNKNOWN. UNKNOWN must not become NOT_RELEVANT or ADVERSE. PASS.

**No evidence:** must differ from evidence that exists but is irrelevant. ERR_Set may be empty, but EvidenceSufficiencyState must remain explicit. REVISION.

**Conflicting evidence:** preserve both; do not average away dispute. PASS.

**Corrected adverse evidence:** CorrectionState alone is insufficient. Consequential use needs CorrectionRef/SupersedesRef. REVISION.

**Cross-provider evidence:** receiving provider needs originating source/provider, source context, observation time and projection time where applicable. REVISION.

**Foreign provider conclusion only:** "trusted" is recommendation/claim evidence, not direct behavioural evidence. Add EvidenceType.

**Identity continuity not required:** must support NOT_REQUIRED_FOR_FUNCTION. PASS.

**Identity continuity unknown:** consequential request may be blocked without negative participant classification. PASS.

**Resource unavailable after positive evidence:** DECLINED_RESOURCE_UNAVAILABLE; evidence remains positive. PASS.

**Authority absent after positive evidence:** DECLINED_AUTHORITY_ABSENT; trust state unchanged. PASS.

**Multiple changed dimensions:** each material exposure dimension needs its own disposition/reference. Add DimensionTransition[].

**Partial approval:** compute may be approved while network/credential expansion is not. Add PARTIALLY_APPROVED_BOUNDED and per-dimension transition state.

**Conditional approval:** added sandboxing, caps or controls must be explicit, not buried in prose DecisionBasis. Add AddedControls/Conditions.

**Temporary emergency exposure:** effective/expiry time plus independent emergency authority can represent it. PASS.

**Early supersession:** new evidence may narrow exposure before review date. Add PreviousETRRef/SupersedesETRRef.

**Review missed:** host policy must declare what happens when review/expiry is missed for consequential exposure. Add ReviewFailureDisposition where applicable.

**Item-level dispute:** attach dispute to relevant evidence/relevance record; do not automatically make whole relationship DISPUTED. Add DisputeRef.

**Privacy-redacted evidence:** protected projection is acceptable if relevance/provenance remain auditable. CIBB interface. PASS.

**Evidence deletion versus provenance:** CTP should allow durable decision provenance without requiring indefinite raw evidence retention. External lifecycle dependency. PASS.

**Pseudonymous credential rotation:** continuity may be ESTABLISHED_FOR_PURPOSE without civil identity disclosure. PASS.

**Recommendation chain:** recommendation must retain provenance and never recursively become direct behavioural evidence. REVISION.

**Coerced evidence generation:** factual relevance does not establish legitimate use. Add AcquisitionBasis / EvidenceUseLegitimacy.

**Improperly obtained predictive evidence:** **Evidence Accuracy != Legitimate Evidence Use.**

**Manipulated test conditions:** add ObservationIntegrity = VALID / QUESTIONED / COMPROMISED / UNKNOWN / DISPUTED.

**Fabricated automated evidence:** consequential use needs reference/provenance validation or explicit UNVERIFIED state.

**Evidence of non-event:** absence of incidents is meaningful only where opportunity/coverage is known. Add ObservationCoverage.

**Rare high-consequence exception:** MaterialHighConsequenceExceptions works, but should be explicit (empty allowed) for consequential transitions.

**Missing self-stewardship/authority/resource/composition prerequisite:** a blank field is ambiguous. Each consequential prerequisite needs explicit applicability/state.

> **NOT_APPLICABLE != NOT_CHECKED**

**Unknown required prerequisite:** ordinary high-consequence approval must not proceed where a required prerequisite remains UNKNOWN.

> **Required Unknown Prerequisite != Ordinary Approval**

**Evidence unnecessary:** public information/Bounded First Trust can legitimately proceed with empty ERR set. PASS.

**Participant requests narrowing:** add TransitionTrigger; voluntary narrowing is not adverse evidence.

**Relationship ends:** add EndReason; broader succession remains lifecycle/BSuR interface.

## 3. Required ERR additions

- EvidenceType
- EvidenceObservedAt
- SourceProviderRef where applicable
- EvidenceProjectedAt where applicable
- AcquisitionBasis
- EvidenceUseLegitimacy
- ObservationIntegrity
- ObservationCoverage
- CorrectionRef / SupersedesRef
- DisputeRef

## 4. Required ETR additions

- TransitionTrigger
- DimensionTransition[]
- PARTIALLY_APPROVED_BOUNDED
- AddedControls / Conditions
- PreviousETRRef / SupersedesETRRef
- ReviewFailureDisposition where applicable
- explicit prerequisite applicability/state wrappers
- EndReason
- explicit MaterialHighConsequenceExceptions for consequential transitions

## 5. New invariants

**CTP-61** Empty Evidence Set != Adverse Evidence.
**CTP-62** Correction State Without Correction Link Is Insufficient For Consequential Use.
**CTP-63** Foreign Conclusion != Direct Behavioural Evidence.
**CTP-64** Mixed-Dimension Transition != Single Undifferentiated Approval.
**CTP-65** Conditional Approval Must Expose Its Added Controls.
**CTP-66** Evidence Accuracy != Legitimate Evidence Use.
**CTP-67** Observation Result != Observation Integrity.
**CTP-68** Absence Of Recorded Incident != Evidence Without Observation Opportunity/Coverage.
**CTP-69** NOT_APPLICABLE != NOT_CHECKED.
**CTP-70** Required Unknown Prerequisite != Ordinary Approval.
**CTP-71** Voluntary Narrowing != Adverse Evidence.
**CTP-72** Recommendation != Transferred Trust.
**CTP-73** Consequential Decision Provenance != Requirement To Retain Raw Evidence Forever.

## 6. Disposition

**ERR/ETR separation:** VALIDATED AT PRE-SCHEMA LEVEL.
**New abstraction layer:** NO.
**Model 002 revision needed:** YES.
**Schema now:** NO.
**Next:** Model 003 incorporating these representational repairs, followed by a smaller requiredness/conformance pass. If stable, serialization can begin.
