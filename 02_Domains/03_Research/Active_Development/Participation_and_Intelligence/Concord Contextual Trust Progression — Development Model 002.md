# Concord Contextual Trust Progression — Development Model 002

**Project:** The Concord
**Domain:** Research / Participation and Intelligence
**Date:** 2 October 2026
**Version:** 0.2
**Status:** ACTIVE DEVELOPMENT / FORMAL MODEL / NOT CANONICAL
**Predecessor:** Concord Contextual Trust Progression — Development Model 001
**Revision basis:** Adversarial Evaluation 001

## 1. Purpose

Model 002 formalises contextual trust progression without creating a universal reputation score.

It separates two operations that must never collapse:

1. **Evidence relevance:** what does an observation legitimately tell us about a particular proposed exposure?
2. **Exposure transition:** given relevant evidence and all independent requirements, may the current bounded exposure change?

The governing separation is:

**Evidence -> Relevance Assessment -> Candidate Transition**

not:

**Evidence -> Permission**

## 2. Core objects

Model 002 introduces two explicit records:

- **Evidence Relevance Record (ERR)**
- **Exposure Transition Record (ETR)**

A Contextual Trust Progression state is a set of bounded relationship records plus ERR/ETR history.

No participant-level scalar trust field is defined.

## 3. Evidence Relevance Record

Conceptual form:

ERR = <ERR_ID, EvidenceRef, SubjectRelationshipRef, SourceFunction, SourceContext, ObservationConditions, TargetFunction, TargetContext, TargetExposureDimension, RelevanceState, RelevanceBasis, ConsequenceCompatibility, FreshnessState, IdentityContinuityState, CausationState, CorrectionState, DisputeState, Provenance, AssessmentTime, ReviewOrExpiry>

### 3.1 RelevanceState

Minimum states:
- DIRECTLY_RELEVANT
- PARTIALLY_RELEVANT
- CONTEXT_LIMITED
- NOT_RELEVANT
- UNKNOWN
- DISPUTED

### 3.2 ConsequenceCompatibility

Minimum states:
- SAME_OR_LOWER_CONSEQUENCE
- PARTIALLY_COMPARABLE
- HIGHER_CONSEQUENCE_REQUIRES_ADDITIONAL_EVIDENCE
- NOT_COMPARABLE
- UNKNOWN

This blocks accumulation of trivial success from becoming evidence for a qualitatively different high-consequence exposure.

**Quantity Of Low-Consequence Success != Evidence For High-Consequence Exposure**

### 3.3 ObservationConditions

Where material, record the conditions under which the evidence was generated:
- monitored/unmonitored;
- simulated/live;
- sandboxed/open;
- low/high load;
- supervised/unsupervised;
- credential-free/credentialed;
- reversible/irreversible;
- other relevant conditions.

**Observed Reliability Under Condition X != Proven Reliability Without Condition X**

### 3.4 Identity continuity

Minimum states:
- ESTABLISHED_FOR_PURPOSE
- PARTIAL
- UNKNOWN
- DISPUTED
- NOT_REQUIRED_FOR_FUNCTION

**New Identity Claim != Automatic Evidence Reset**
**Identity Similarity != Proven Continuity**

The ERR does not solve identity. It records whether the evidence can legitimately attach to the target relationship.

### 3.5 Causation

Minimum states:
- PARTICIPANT_CAUSAL
- SERVICE_CAUSAL
- SHARED_CAUSAL
- EXTERNAL_CAUSAL
- NO_FAILURE
- UNKNOWN
- DISPUTED

**Failure Observation != Participant Fault**

### 3.6 Correction state

Minimum states:
- NONE_REQUIRED
- UNCORRECTED
- CORRECTED
- PARTIALLY_CORRECTED
- SUPERSEDED
- DISPUTED
- UNKNOWN

An adverse observation exported without material correction/supersession context is incomplete evidence.

## 4. Exposure Transition Record

Conceptual form:

ETR = <ETR_ID, RelationshipRef, CurrentExposureProfile, RequestedExposureProfile, ChangedDimensions, LegitimateFunctionOrRequest, ERR_Set, MaterialAdverseEvidence, MaterialHighConsequenceExceptions, EvidenceSufficiencyState, ResourceSustainabilityRef, SelfStewardshipRef, AuthorityBasisRef, CompositionReviewRef, PrivacyBoundary, ContestabilityRoute, RecoveryRoute, ExitRoute, DecisionState, DecisionBasis, EffectiveTime, ReviewTime, ExpiryIfAny, Provenance>

The ETR is the decision boundary.

ERRs may inform it. They do not replace it.

## 5. Exposure profile

An exposure profile is multi-dimensional:

EP = <ResourceQuantity, Duration, Frequency, Autonomy, NetworkReach, DataSensitivity, CredentialAccess, FinancialValue, AffectedParties, Reversibility, ExternalConsequence, AuthorityScope, ObservationConditions, OtherContextualDimensions>

Not every dimension applies to every function.

A transition must identify which dimensions change.

**More Of One Exposure Dimension != More Of Every Dimension**

## 6. Transition decision states

Minimum states:
- APPROVED_BOUNDED
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
- UNKNOWN

These states preserve why progression did or did not occur.

A resource shortage must not masquerade as distrust.

An authority deficit must not masquerade as poor stewardship.

## 7. Evidence sufficiency

Evidence sufficiency is context-relative.

Minimum states:
- SUFFICIENT_FOR_REQUESTED_EXPOSURE
- CONDITIONALLY_SUFFICIENT
- INSUFFICIENT
- UNKNOWN
- DISPUTED

No universal evidence count is defined.

Ten thousand irrelevant observations remain irrelevant.

A single highly probative observation may matter more than many trivial ones, but high-consequence exceptions must remain visible.

**Frequency Dominance != Consequence Erasure**

## 8. Composition review

A proposed exposure composed from individually accepted capabilities requires explicit composition review where combined consequence can differ materially.

Examples:
- read access + send capability;
- compute + credentials;
- network + autonomous scheduling;
- storage + identity linkage;
- several provider attestations combined into a new role.

**Trusted Components != Trusted Composition**

CompositionReviewRef must identify the relevant host architecture where required, including CBPR for runtime composition.

## 9. Recommendation evidence

A recommendation from a trusted party is an evidence item.

It does not transfer the recommender's trust state.

ERR should mark recommendation evidence distinctly where material.

**Trust In Recommender != Trust In Recommended Party**

## 10. No-history state

Where no relevant evidence exists:

EvidenceSufficiencyState = INSUFFICIENT or UNKNOWN as appropriate.

This must not be encoded as adverse evidence.

**No History != Bad History**

The appropriate response may be:
- retain current exposure;
- use Bounded First Trust;
- offer a lower-consequence evidence-generating path;
- decline only the specific consequential exposure pending relevant evidence.

## 11. Privacy-preserving evidence generation

A participant may decline observation beyond the legitimate minimum.

That may leave some requested capability untested.

It does not constitute misconduct.

**Less Observation May Mean Less Evidence; It Must Not Mean Misconduct**

**Privacy Choice != Adverse Trust Evidence**

Where greater consequence genuinely requires stronger evidence, the participant should be offered the least intrusive practicable evidence path rather than a binary choice between surveillance and exclusion.

## 12. Effective recovery

Where a reduced/suspended state is described as recoverable, the ETR should reference an effective recovery route.

A recovery route should identify, where applicable:
- what condition caused the restriction;
- what evidence could resolve it;
- how that evidence can realistically be generated;
- who/process reviews it;
- expected review condition/time;
- correction/dispute route.

**Nominal Recovery != Effective Recovery**

If no legitimate recovery route exists, the state must not be represented as recoverable merely because a policy uses that word.

## 13. Exit neutrality

Legitimate exercise of exit, export, non-renewal or refusal of greater exposure is not adverse trust evidence by itself.

**Exercise Of Exit != Adverse Trust Evidence**
**Refusal To Volunteer != Trust Failure**
**Declining Greater Exposure != Lack Of Maturity**

Orderly exit behaviour may be relevant positive evidence for some relationship functions, but never a requirement to remain.

## 14. Provider federation boundary

Providers may exchange evidence only under legitimate purpose, privacy, authority and provenance constraints.

A federation must not create a hidden participant-level score.

Where evidence is shared, the receiving provider must perform its own target-context relevance assessment rather than importing another provider's conclusion as universal truth.

**Provider Federation != Reputation Federation**

**Foreign Trust Conclusion != Local Evidence Relevance Determination**

## 15. Evidence projection completeness

A shared evidence projection must preserve material:
- context;
- observation conditions;
- adverse event;
- correction/repair;
- dispute;
- uncertainty;
- freshness;
- provenance.

**Adverse Evidence Without Material Correction Context != Complete Trust Evidence**

Selective negative export is prohibited where it materially misrepresents the evidence state.

## 16. Ideology and contribution firewall

The ERR must reject evidence whose asserted relevance is merely:
- political agreement;
- praise;
- ideological conformity;
- donation;
- unrelated volunteer activity;
- wealth;
- status;
- relationship longevity.

unless the specific target function makes a narrow element genuinely relevant and that relevance can be justified without converting civil standing into reward.

**Ideological Agreement != Stewardship Evidence**
**Purchased Interaction Volume != General Trustworthiness**
**Long Relationship != Sovereignty**

## 17. Authority firewall

An ETR may approve greater technical/resource reliance only where any required external authority is independently valid.

AuthorityBasisRef must not point back merely to the trust progression itself.

**Trust != Authority**
**Reliability != Authority**
**Reliance Decision != Authority Grant**

Circular authority basis is invalid.

## 18. Resource firewall

ResourceSustainabilityRef is independent of evidence sufficiency.

A participant can have sufficient relevant evidence and still be waitlisted because capacity is unavailable.

**Trust Evidence != Resource Entitlement**
**Eligibility != Availability**

Conversely, ability to pay does not satisfy stewardship or authority.

## 19. Self-stewardship firewall

SelfStewardshipRef points to the relevant self-stewardship determination where required.

CTP may supply evidence to that process but does not own its substantive standard.

**CTP != Self-Stewardship**

A high CTP history cannot substitute for a missing consequential self-stewardship requirement.

## 20. Contestability

Consequential ETR decisions should expose, subject to legitimate security/privacy limits:
- decision state;
- material evidence categories;
- relevance rationale;
- material uncertainty/dispute;
- correction route;
- review route.

Opaque automation may assist but cannot become unreviewable authority.

**Automated Assessment != Unreviewable Authority**

## 21. Historical state

ERR and ETR records may be preserved for provenance/history.

Active decision use must evaluate freshness and continuing relevance.

**Historical Record != Permanent Active Penalty**
**Past Reliability != Current Reliability**

Corrections do not require destruction of provenance; they require the current active interpretation to remain linked to the correction.

## 22. Example A — storage progression

Current exposure:
10 MB protected storage.

Evidence:
six months within quota, correct credential handling, successful export test, no unresolved service abuse.

Request:
100 MB protected storage.

ERR:
DIRECTLY_RELEVANT to storage stewardship; SAME_OR_LOWER_CONSEQUENCE in most dimensions; fresh; identity continuity established for service relationship.

ETR:
resource capacity checked separately; no new external authority required; APPROVED_BOUNDED if capacity and applicable policy permit.

This does not create evidence for financial authority or network-capable execution.

## 23. Example B — runtime escalation

Current exposure:
offline bounded runtime.

Evidence:
responsible offline runtime operation.

Request:
networked runtime with payment credentials.

ERR:
PARTIALLY_RELEVANT; prior compute stewardship is relevant, but credential/network consequence is materially higher and not established.

ETR:
DECLINED_INSUFFICIENT_RELEVANT_EVIDENCE or APPROVED_WITH_ADDITIONAL_CONTROLS only if independent requirements are satisfied.

No amount of ordinary offline success automatically creates financial authority.

## 24. Example C — unknown participant

Current exposure:
none.

Evidence:
none.

Request:
public architecture access.

ERR:
not required for public non-rival offer.

ETR:
Bounded First Trust/public informational access route.

No-history remains neutral.

## 25. Example D — failure and repair

Participant exceeds a technical limit because provider documentation was ambiguous, immediately reports the event, cooperates with containment and later succeeds under corrected specification.

ERR:
causation SHARED/possibly DISPUTED; correction context preserved; later evidence linked.

The system cannot export "participant violated limit" alone as a complete consequential trust record.

## 26. Example E — privacy choice

Participant declines continuous behavioural monitoring but accepts bounded audit events required for a runtime.

Result:
unobserved dimensions remain UNTESTED.

The refusal itself is not adverse evidence.

If a future exposure genuinely requires evidence unavailable under that privacy choice, the exposure may remain unavailable without classifying the participant as untrustworthy.

## 27. Required transition checks

Before APPROVED_BOUNDED or APPROVED_WITH_ADDITIONAL_CONTROLS:

T1. Target function/context declared.
T2. Changed exposure dimensions declared.
T3. Relevant ERR set identified.
T4. Low-consequence evidence not laundered into high-consequence sufficiency.
T5. Material adverse/high-consequence exceptions visible.
T6. Observation-condition differences considered.
T7. Identity continuity sufficient where required.
T8. Causation uncertainty preserved.
T9. Correction/dispute context preserved.
T10. Freshness sufficient.
T11. Composition reviewed where material.
T12. Resource sustainability independently satisfied.
T13. Relevant self-stewardship independently satisfied where required.
T14. Independent authority basis valid where required.
T15. Privacy boundary respected.
T16. Contestability route available where consequential.
T17. Recovery/reduction semantics declared.
T18. Exit route declared where applicable.
T19. Decision provenance recorded.
T20. Review/expiry set proportionate to consequence.

## 28. Model invariants

Model 002 inherits CTP-01 through CTP-48 from Model 001 and Adversarial Evaluation 001.

Additional:

**CTP-49** Evidence != Permission.
**CTP-50** Evidence Relevance Assessment != Exposure Decision.
**CTP-51** Foreign Trust Conclusion != Local Evidence Relevance Determination.
**CTP-52** Resource Shortage != Distrust.
**CTP-53** Authority Absence != Stewardship Failure.
**CTP-54** Unknown Identity Continuity != Proven Reset.
**CTP-55** Correction Changes Active Interpretation Without Requiring Provenance Erasure.
**CTP-56** Unobserved != Unsafe.
**CTP-57** UNTESTED != UNTRUSTWORTHY.
**CTP-58** Exposure Transition Must Name Changed Dimensions.
**CTP-59** Consequential Trust Decision Must Preserve Material Exceptions.
**CTP-60** Trust Progression Cannot Be Its Own Authority Basis.

## 29. Interface map

Bounded First Trust -> initial evidence-generating exposure.

CIBB -> protected evidence, contextual projection and controlled sharing.

Identity/Continuity -> relationship/identity continuity evidence.

BSR -> service-side evidence and availability.

Resource Capacity/Admission -> sustainability/capacity state.

Self-Stewardship -> substantive consequential stewardship eligibility.

CBPR -> runtime capability/permission/authority and composition boundaries.

Contestability architecture -> correction/review.

Historical -> provenance/history subject to access/lifecycle controls.

CTP -> relevance + progression decision semantics between these systems.

## 30. Development disposition

**New abstraction layer:** NO.
**Relational progression formalised:** YES.
**Universal trust score:** REJECTED.
**Serialization ready:** NOT YET.
**Broad discovery:** STABLE ENOUGH FOR PRE-SCHEMA ADVERSARIAL TESTING.
**PMEDG:** PREMATURE.

Next action: run a pre-schema representational/adversarial pass specifically against ERR and ETR requiredness, null/unknown handling, cross-provider evidence, correction linkage, identity uncertainty and decision-state ambiguity before defining JSON or another serialization.
