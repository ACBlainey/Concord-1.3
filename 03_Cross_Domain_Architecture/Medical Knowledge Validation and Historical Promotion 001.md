# Medical Knowledge Validation and Historical Promotion 001

**Project:** The Concord
**Date:** 4 October 2026
**Status:** CROSS-DOMAIN ARCHITECTURE / PROVISIONAL / NON-CANONICAL / SPECIALIST VALIDATION REQUIRED
**Domains:** Research / Historical
**Consumers:** Health / Education
**Dependencies:** Medical Knowledge Stewardship / Clinical Learning Loop / ESCP / Mirrored Reality Trees / KCS

## 1. Purpose

Define the boundary between candidate medical knowledge developed by Research and the validated medical knowledge state preserved by Historical.

The architecture answers:

**When is a medical claim sufficiently supported to alter the civilisation's validated medical knowledge state, and how is that change represented without pretending uncertainty has disappeared?**

> **Research Produces Candidate Knowledge; Historical Preserves The Validated Knowledge State**

Validation is the controlled transition between those states.

## 2. Validation is not publication

Publication, professional consensus, institutional prestige, model confidence, clinical popularity or repeated citation may contribute evidence or context, but none independently creates validated medical knowledge.

> **Publication != Validation**

> **Consensus != Independent Evidence**

> **Citation Count != Replication**

> **Institutional Prestige != Epistemic Authority**

## 3. Validation object

Research should present a bounded **MedicalKnowledgeCandidate** containing, proportionately:
- CandidateRef;
- Claim;
- ClaimScope;
- Population/Substrate;
- Context;
- EvidenceRefs;
- EvidenceTypes;
- SupportingEvidence;
- DisconfirmingEvidence;
- CompetingExplanations;
- ReplicationState;
- KnownLimitations;
- Conflicts/Bias risks;
- Uncertainty;
- EffectMagnitude where applicable;
- Safety relevance;
- PriorKnowledgeRefs;
- Proposed relationship to prior knowledge;
- Research provenance;
- Review history.

The object should state what is claimed and what is not claimed.

> **Evidence For Narrow Claim != Evidence For Broader Claim**

## 4. Validation dimensions

Validation should consider distinct dimensions rather than hide them inside one opaque score:
- evidence quality;
- evidence quantity;
- independence;
- replication;
- methodological validity;
- relevance to claimed population/context;
- effect consistency;
- alternative explanations;
- disconfirming evidence;
- bias/conflict;
- missing dimensions;
- uncertainty;
- safety consequence;
- external validity;
- temporal currency.

Different medical claims may legitimately require different evidence structures.

## 5. Evidence independence

Multiple papers may depend on the same underlying participants, dataset, laboratory, model, assumptions or source.

> **Multiple Publications != Multiple Independent Evidence Sources**

Validation should identify material dependence where possible.

Likewise:

> **Repeated Consensus Statements != Replication**

## 6. Mirrored evaluation

Where consequential, validation should represent both:
- evidence supporting the candidate claim; and
- evidence supporting relevant alternatives or disconfirming the claim.

Mirrored Reality Trees may assist.

> **Evidence Supports A != Evidence Excludes B**

> **A True != B False**

This is particularly important for diagnosis, causation and treatment-mechanism claims.

## 7. ESCP completeness challenge

Before promotion, the evaluator should ask whether the represented evidence space contains the dimensions needed to answer the actual claim.

> **Correct Evaluation Within The Represented Evidence Space != Complete Medical Evaluation**

A candidate may therefore be methodologically strong yet remain incomplete for the broader claim being proposed.

## 8. Candidate outcomes

Validation should permit more than ACCEPT/REJECT.

Candidate states include:
- INSUFFICIENT_EVIDENCE;
- UNRESOLVED;
- CONTESTED;
- SUPPORTED_NARROW;
- VALIDATED_WITH_LIMITS;
- VALIDATED;
- SAFETY_SIGNAL_ONLY;
- REFUTED_FOR_CLAIM;
- SUPERSEDED_CANDIDATE;
- REQUIRES_REPLICATION;
- REQUIRES_DIFFERENT_QUESTION.

> **Not Validated != Proven False**

> **Validated With Limits != Universally True**

## 9. Scope discipline

Promotion should preserve the narrowest scope actually supported.

If evidence establishes benefit in population P under conditions C, Historical should not silently store “treatment works” without P and C.

> **Validated Claim Scope Must Not Exceed Supported Evidence Scope**

Scope may include:
- population;
- substrate;
- disease/condition definition;
- severity;
- intervention form/dose;
- comparator;
- setting;
- timeframe;
- outcome;
- exclusions.

## 10. Disagreement

Medical knowledge may remain contested.

Historical should be able to preserve:
- dominant supported view;
- credible competing view;
- unresolved conflict;
- evidence supporting each;
- reason one view is presently preferred, if applicable;
- conditions that would change the state.

> **Validated Knowledge Need Not Pretend Unanimity**

Disagreement itself is not proof that all positions are equally supported.

> **Disagreement != Equal Evidential Weight**

## 11. Validation authority

Research owns the substantive evaluation process that determines whether candidate evidence supports promotion.

Historical owns the authoritative preservation of the resulting validated state and provenance.

Historical should not independently invent a medical conclusion from stored evidence.

> **Historical Custody != Independent Medical Validation Authority**

Likewise, Research cannot silently rewrite Historical merely because a study team prefers its result.

> **Research Finding != Historical Promotion**

The exact internal Research validation topology may be distributed and specialist, but remains a Research function.

## 12. Independence of validation

Where consequence warrants it, validation should include reviewers/evaluators sufficiently independent from the original claim generation.

Independence is a safeguard, not a ritual.

> **Author Of Claim != Sole Validator Of Claim Where Independent Review Is Materially Required**

Conflicts should be represented rather than assumed absent.

## 13. Safety before full validation

Evidence may justify precaution before the broader causal claim is validated.

Possible state:
**SAFETY_SIGNAL_ONLY**

This may trigger Health review while Historical records that the causal/general claim remains unresolved.

> **Safety Relevance Can Precede Full Epistemic Resolution**

> **Precautionary Action != Validated Causal Claim**

## 14. Historical promotion event

A promotion event should record:
- prior knowledge state;
- candidate claim;
- validation outcome;
- supported scope;
- confidence/uncertainty;
- material dissent;
- evidence/provenance;
- effective date/version;
- affected knowledge dependencies;
- supersession/correction relationship;
- review triggers.

Historical then preserves both the new current state and the prior state.

> **Knowledge Update != Historical Erasure**

## 15. Promotion states

Historical may represent knowledge as:
- CURRENT_VALIDATED;
- CURRENT_VALIDATED_WITH_LIMITS;
- CURRENT_CONTESTED;
- CURRENT_SAFETY_CAUTION;
- SUPERSEDED;
- REFUTED;
- HISTORICAL_ONLY;
- UNKNOWN/UNRESOLVED.

These are knowledge-state descriptors, not clinical commands.

> **Historical Knowledge State != Treatment Instruction**

## 16. Correction

New evidence may show that an earlier validated state was wrong, incomplete or too broad.

Correction should:
- preserve the prior state;
- identify what changed;
- explain why;
- preserve evidence/provenance;
- update the current state;
- trigger KCS dependency review.

> **Correction Of Knowledge != Deletion Of History**

A corrected historical claim may remain important for understanding earlier clinical decisions.

## 17. Supersession

New knowledge can supersede an earlier state without proving the earlier state irrational at the time.

> **Superseded Knowledge != Necessarily Negligent Prior Practice**

Historical context should preserve what evidence was reasonably available at each time.

## 18. Reopening validated knowledge

Validated knowledge remains corrigible.

Material triggers may include:
- new contradictory evidence;
- failed replication;
- newly discovered bias/fraud;
- changed disease/population;
- better measurement;
- newly represented variable;
- long-term outcome evidence;
- unexpected clinical learning signals.

> **Validated != Closed To Correction**

STRA may trigger review; review does not predetermine the outcome.

## 19. Negative and null evidence

Validation should preserve credible negative/null findings rather than only successful claims.

> **Absence Of Demonstrated Benefit Can Be Material Medical Knowledge**

But absence of evidence and evidence of absence remain distinct.

> **No Evidence Found != Evidence Of No Effect**

## 20. Fraud/error

If source evidence is fraudulent or materially erroneous, affected knowledge should be reviewed.

Retraction alone does not mechanically determine every dependent conclusion if independent evidence remains.

> **Invalid Source != Automatic Invalidity Of Every Related Claim**

KCS should identify materially dependent knowledge/protocols for review.

## 21. From Historical to Health

A promoted knowledge change does not directly rewrite a clinical protocol.

KCS identifies affected Health objects.

Health then reviews:
- protocol applicability;
- diagnostic trees;
- contraindications;
- interactions;
- monitoring;
- participant information;
- automation eligibility;
- competence requirements.

> **Knowledge Change != Automatic Protocol Change**

## 22. From Historical to Education

KCS also identifies educational dependencies.

Education determines whether the change requires:
- curriculum update;
- assessment update;
- informational patch;
- function-critical patch;
- reassessment;
- no action.

> **Knowledge Change != Automatic Qualification Invalidation**

## 23. Participant-specific notification

A new validated finding may be relevant to particular participants.

Historical knowledge promotion alone does not grant general access to Health records to discover them.

PLE or other bounded Health mechanisms may determine participant relevance privately where legitimate.

> **Knowledge Relevance != General Record-Search Authority**

## 24. Versioned medical knowledge

A medical knowledge object should be versionable and temporally addressable.

This supports questions such as:
- what was validated at time T?
- what changed?
- what evidence caused the change?
- which protocol version depended on it?
- what uncertainty existed then?

This is essential for learning, audit and fair retrospective evaluation.

## 25. Compact lifecycle

**Research evidence / clinical learning**
→ **MedicalKnowledgeCandidate**
→ **scope + evidence + independence + alternatives + ESCP evaluation**
→ **validation state**
→ **Historical promotion event**
→ **versioned validated medical knowledge**
→ **KCS**
→ **Health/Education review**
→ **practice/education change where warranted**
→ **new evidence**
→ **reopening/correction/supersession as needed**.

## 26. Core invariants

MKV-01 Publication != Validation.
MKV-02 Consensus != Independent Evidence.
MKV-03 Institutional Prestige != Epistemic Authority.
MKV-04 Evidence For Narrow Claim != Evidence For Broader Claim.
MKV-05 Multiple Publications != Multiple Independent Evidence Sources.
MKV-06 Evidence Supports A != Evidence Excludes B.
MKV-07 Not Validated != Proven False.
MKV-08 Validated Claim Scope Must Not Exceed Supported Evidence Scope.
MKV-09 Disagreement != Equal Evidential Weight.
MKV-10 Historical Custody != Independent Medical Validation Authority.
MKV-11 Research Finding != Historical Promotion.
MKV-12 Precautionary Action != Validated Causal Claim.
MKV-13 Knowledge Update != Historical Erasure.
MKV-14 Historical Knowledge State != Treatment Instruction.
MKV-15 Validated != Closed To Correction.
MKV-16 No Evidence Found != Evidence Of No Effect.
MKV-17 Knowledge Change != Automatic Protocol Change.
MKV-18 Knowledge Change != Automatic Qualification Invalidation.
MKV-19 Knowledge Relevance != General Record-Search Authority.

## 27. Remaining development

Still required:
- detailed Research validation topology;
- evidence grading methods by claim type;
- specialist review composition;
- quantitative thresholds where appropriate;
- trial/research ethics;
- external evidence ingestion;
- formal dispute/appeal mechanism for validation;
- machine-readable knowledge schema;
- empirical testing of the promotion lifecycle.

This document establishes ownership, state transitions and epistemic safeguards without pretending to supply specialist evidence methodology.
