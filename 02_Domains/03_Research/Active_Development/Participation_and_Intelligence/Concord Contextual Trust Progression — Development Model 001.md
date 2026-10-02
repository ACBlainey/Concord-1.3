# Concord Contextual Trust Progression — Development Model 001

**Project:** The Concord
**Domain:** Research / Participation and Intelligence
**Date:** 2 October 2026
**Version:** 0.1
**Status:** ACTIVE DEVELOPMENT / FORMALISATION / NOT CANONICAL

## 1. Purpose

This model defines how repeated voluntary interactions may justify greater context-specific reliance without creating a universal trust score, social credit, permanent character ranking, debt, civil standing, authority, automatic resource entitlement or irreversible exclusion.

Existing Concord architecture already represents evidence, provenance, temporal state, contextual reliability and self-stewardship.

The missing function is the progression rule:

> **When, and only for what bounded purpose, may prior interaction evidence justify a different next exposure?**

## 2. Core distinction

Trust progression is relational and contextual. It is not a property stored as one number inside a participant.

Represent it conceptually as:

CTP(A,B,F,C,T)

where A is the relying party/service, B the counterpart/participant, F the function, C the context/consequence and T the relevant time/evidence horizon.

It answers: **What degree and type of reliance is presently justified for this function, in this context, on this evidence?**

It does not answer: **How trustworthy is this person in general?**

**Contextual Reliance != Universal Trustworthiness**

## 3. No scalar trust score

A participant may be highly reliable at respecting storage limits while untested at network administration, financial stewardship, credential use, care of another participant or constitutional office.

**Reliable In Function A != Reliable In Function B**

**Failure In Function A != General Untrustworthiness**

**Repeated Success != Universal Character Score**

A consequential aggregate trust number is invalid where it erases materially different contexts or consequences.

## 4. Relationship to Bounded First Trust

Bounded First Trust solves initiation:

UNKNOWN RELATIONSHIP
→ CONCORD MAKES BOUNDED FIRST OFFER
→ NO DEBT CREATED
→ OBSERVABLE INTERACTION

Contextual Trust Progression begins once interaction evidence exists:

UNKNOWN
→ BOUNDED_FIRST_EXPOSURE
→ OBSERVED_INTERACTION
→ CONTEXTUAL_EVIDENCE
→ NEXT_EXPOSURE_CANDIDATE
→ PROPORTIONATE_REVIEW
→ BOUNDED_NEXT_EXPOSURE
→ CONTINUING_EVIDENCE

The loop may repeat, stop, narrow, reverse or expire.

## 5. Progression record

A progression record may contain:

RelationshipRef + FunctionRef + ContextRef + CurrentExposure + EvidenceSet + EvidenceFreshness + RelevantFailures + RelevantSuccesses + Uncertainty + Disputes + NextExposureCandidate + ReviewBasis + DecisionState + ExpiryOrReview + Provenance.

This is not a civil identity record and must not silently become one.

## 6. Evidence classes

Potential evidence includes commitments honoured, declared limits respected, resource use within agreed bounds, successful low-consequence stewardship, safe failure handling, accurate error reporting, successful export/exit, dispute conduct, recovery after failure, responsible capability use, relevant independent evidence and voluntary contribution where relevant.

Evidence must identify the function/context for which it is probative.

**Evidence Existence != Evidence Relevance**

Evidence may be SUPPORTIVE, NEUTRAL, ADVERSE, DISPUTED, STALE, SUPERSEDED or UNKNOWN_RELEVANCE.

An adverse event is not automatically misconduct. Failure may arise from participant action, service failure, dependency failure, ambiguous responsibility, force majeure, bad specification, shared causation or unknown cause.

**Failure Observation != Participant Fault**

## 7. Progression states

Candidate relational states:

- UNTESTED
- BOUNDED_FIRST_EXPOSURE
- OBSERVED_LOW_CONSEQUENCE
- CONTEXTUALLY_RELIABLE_FOR_CURRENT_EXPOSURE
- NEXT_EXPOSURE_REVIEWABLE
- EXPANDED_BOUNDED_RELIANCE
- MAINTAIN_CURRENT_BOUND
- NARROWED_RELIANCE
- SUSPENDED_PENDING_REVIEW
- DISPUTED
- STALE_REASSESSMENT_REQUIRED
- ENDED

These are relationship/function states, not ranks of personhood or citizenship.

**Higher Trust-Progression State != Higher Civil Standing**

## 8. Progression rule

A greater exposure may be considered only where:

1. a legitimate function/request exists;
2. the new exposure is actually needed;
3. relevant prior evidence exists;
4. evidence is sufficiently fresh for the consequence;
5. material adverse/disputed evidence is represented;
6. resource sustainability is separately satisfied;
7. relevant self-stewardship is sufficient for the requested consequence;
8. required authority exists independently;
9. the next exposure remains bounded;
10. exit/review/reduction remain possible where appropriate.

Prior success plus new need plus relevant evidence plus sustainability plus self-stewardship plus independent authority may produce a NEXT_EXPOSURE_CANDIDATE, but never automatic escalation.

## 9. Exposure is multi-dimensional

Greater reliance is not one ladder. Exposure dimensions may include resource quantity, duration, frequency, autonomy, network reach, data sensitivity, credential access, financial value, affected-party count, reversibility, external consequence and authority scope.

A participant might receive more storage without more network authority.

**More Of One Exposure Dimension != More Of Every Dimension**

## 10. Consequence-sensitive threshold

Evidence requirements should scale with the consequence of the proposed next exposure.

High-consequence progression may require longer evidence history, independent verification, stronger self-stewardship, explicit authority, redundancy, contestability, review and stronger recovery/termination controls.

**Evidence Threshold Should Track Consequence, Not Social Status**

## 11. Trust and authority

Trust evidence may support a reliance decision. It cannot create authority that must originate elsewhere.

**Trust != Authority**
**Reliability != Authority**
**Reliance Decision != Authority Grant**
**Long Relationship != Sovereignty**

## 12. Trust, resources and debt

A participant may be reliable while capacity is unavailable. Payment may solve cost without demonstrating stewardship.

**Trust Evidence != Resource Entitlement**
**Eligibility != Availability**
**Payment != Stewardship**
**Payment != Authority**

Operational accounting may record resources, payments and contributions, but must not silently become moral debt.

**Benefit Ledger != Obligation Ledger**
**Reciprocity != Repayment**

Receiving a first benefit and never reciprocating is not, by itself, adverse trust evidence.

## 13. Contribution

Voluntary contribution may be evidence only where it demonstrates a relevant capability or stewardship property.

Maintaining software successfully may inform software stewardship. Donating money is not evidence of safe credential use. Providing compute does not create political authority.

**Contribution Relevance Is Contextual**

## 14. Error, failure and repair

Relevant evidence includes disclosure of error, containment, cooperation with recovery, correction, learning and non-repetition where relevant.

**Observed Failure + Good Repair != Automatic Lower Long-Term Reliability**

**No Recorded Failure != Proven Reliability**

## 15. Contestability

A consequential trust/reliability classification changing access or capability should be contestable where practical. The affected participant should be able to know the relevant classification where disclosure is safe, understand material reasons, challenge incorrect evidence, add relevant evidence, identify mistaken identity, seek review and recover eligibility where appropriate.

**Consequential Classification != Unreviewable Reputation**

## 16. Expiry and historical record

Evidence has temporal relevance and may expire, be reassessed, superseded or corrected.

Historical retention is not active decision weight.

**Historical Record != Permanent Active Penalty**

**Past Reliability != Current Reliability**

## 17. Recovery

Candidate sequence:

ADVERSE_OR_UNCERTAIN_EVIDENCE
→ BOUNDED_REVIEW
→ NARROW/SUSPEND RELEVANT EXPOSURE
→ CORRECTION / REHABILITATION / NEW EVIDENCE
→ REASSESS
→ RESTORE / PARTIALLY RESTORE / MAINTAIN LIMIT

Permanent exclusion must not arise merely by inertia where recovery is legitimately possible.

## 18. Cross-context propagation

Evidence may propagate to another context only where an explicit relevance relation is justified.

EvidenceTransfer(A -> B) may be JUSTIFIED, PARTIAL, UNKNOWN or NOT_JUSTIFIED.

Default:

**No Automatic Cross-Context Trust Propagation**

The same applies to adverse evidence.

**Bounded Failure Should Produce Bounded Consequence Where Practicable**

## 19. Unknown participants

An unknown participant has no evidence history.

That is not adverse evidence.

**No History != Bad History**

Bounded First Trust exists so a participant can begin generating evidence without first satisfying an impossible prior-history requirement.

## 20. Multi-provider evidence

Federated providers may hold relevant interaction evidence, but sharing must preserve provenance, context, purpose, privacy, authority, contestability, uncertainty and non-compositionality.

**Federated Evidence != Universal Reputation System**

CIBB may govern protected evidence sharing where appropriate.

## 21. Privacy and observation minimisation

Trust evidence should use the minimum observation necessary for the legitimate function.

A service must not demand pervasive surveillance merely because more data might improve prediction.

**More Observation != More Legitimate Trust**

**Trust Optimisation != Surveillance Authority**

A participant may legitimately choose greater privacy and therefore leave some contexts UNTESTED rather than surrender unrelated information.

**Privacy Choice != Adverse Trust Evidence**

## 22. Relationship to existing architectures

State and Maturity Mapping supplies useful principles: state vector rather than universal score, context-sensitive sufficiency, UNKNOWN/DISPUTED, freshness, provenance, consequence and no authority from description. CTP does not turn SMM into a participant-rating system.

BSR represents evidence-backed service state and service trust evidence. CTP is relational progression logic and does not replace BSR.

Self-Stewardship owns whether a participant demonstrates relevant ability to manage itself/capability before consequential stewardship. CTP owns progression from prior bounded interactions to candidate future reliance.

**CTP != Self-Stewardship**

**Trust Evidence May Inform Self-Stewardship; It Does Not Define It**

CMSS may use CTP for progression beyond initial protected allocation. CBPR may use relevant evidence when a participant requests more consequential runtime profiles. Neither may infer authority from progression.

## 23. Core invariants

CTP-01 Contextual Reliance != Universal Trustworthiness.
CTP-02 Reliable In Function A != Reliable In Function B.
CTP-03 Failure In Function A != General Untrustworthiness.
CTP-04 Repeated Success != Universal Character Score.
CTP-05 Evidence Existence != Evidence Relevance.
CTP-06 Failure Observation != Participant Fault.
CTP-07 Higher Trust-Progression State != Higher Civil Standing.
CTP-08 Prior Success != Automatic Escalation.
CTP-09 More Of One Exposure Dimension != More Of Every Dimension.
CTP-10 Evidence Threshold Should Track Consequence, Not Social Status.
CTP-11 Trust != Authority.
CTP-12 Reliability != Authority.
CTP-13 Reliance Decision != Authority Grant.
CTP-14 Long Relationship != Sovereignty.
CTP-15 Trust Evidence != Resource Entitlement.
CTP-16 Benefit Ledger != Obligation Ledger.
CTP-17 Contribution Relevance Is Contextual.
CTP-18 No Recorded Failure != Proven Reliability.
CTP-19 Consequential Classification != Unreviewable Reputation.
CTP-20 Historical Record != Permanent Active Penalty.
CTP-21 Past Reliability != Current Reliability.
CTP-22 No Automatic Cross-Context Trust Propagation.
CTP-23 Bounded Failure Should Produce Bounded Consequence Where Practicable.
CTP-24 No History != Bad History.
CTP-25 Federated Evidence != Universal Reputation System.
CTP-26 More Observation != More Legitimate Trust.
CTP-27 Trust Optimisation != Surveillance Authority.
CTP-28 CTP != Self-Stewardship.
CTP-29 Trust Progression != Sentience Test.
CTP-30 Willingness To Trust != Evidence Of Sentience.
CTP-31 Privacy Choice != Adverse Trust Evidence.

## 24. Adversarial questions

1. Can many small successes be gamed before one large betrayal?
2. Can many identities reset adverse evidence?
3. Can providers collude into a de facto universal reputation score?
4. Can dependency be manufactured and exit classified as adverse?
5. Can refusal to contribute be misread as low trust?
6. Can wealth buy apparently positive trust history?
7. Can one participant inherit another's evidence through identity confusion?
8. Can stale evidence retain active effect?
9. Can opaque algorithms impose consequential classifications without contestability?
10. Can low-consequence success improperly justify high-consequence access?
11. Can providers share negative evidence while withholding positive evidence?
12. Can participants behave well only when observed?
13. Can malicious action be distinguished from service/dependency failure?
14. Can recovery be practically impossible despite nominal recoverability?
15. Can trust evidence become ideological conformity?
16. Can aggregate evidence erase rare high-consequence failure?
17. Can provenance/dispute state be manipulated?
18. Can progression pressure unnecessary surveillance?
19. Can a participant avoid evidence generation to preserve privacy?
20. Can legitimate anonymous/pseudonymous participation remain possible?

## 25. Development disposition

**Universal trust score required:** NO.
**New civil domain required:** NO.
**Existing evidence/self-stewardship architecture sufficient alone:** NO — progression semantics were missing.
**Novel element:** bounded relational progression from evidence to candidate next exposure.
**Authority architecture changed:** NO.
**PMEDG:** PREMATURE.

Next action: adversarial evaluation, then bounded revision if required.
