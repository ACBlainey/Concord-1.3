# Treatment Protocol Governance and Clinical Knowledge Validation 001

**Project:** The Concord Framework
**Date:** 3 October 2026
**Status:** ACTIVE HEALTH ARCHITECTURE / PROVISIONAL / NON-CANONICAL / SPECIALIST VALIDATION REQUIRED
**Domain:** Health
**Primary interfaces:** Historical / Research / Law / Pharmacy / Professional Governance
**Primary dependencies:** Medical Knowledge Stewardship, Research Translation and Experimental Treatment 001 / Protocol-Driven Self-Treatment 001 / KCS Change Propagation / MKA / ESCP

## 1. Purpose

Protocol-driven Health requires a trustworthy answer to two different questions:

1. **What does the current validated medical knowledge state support?**
2. **What bounded clinical protocol may Health operationally apply from that knowledge?**

These questions must remain distinct.

> **Medical Knowledge != Clinical Protocol**

> **Evidence Of Benefit != Complete Operational Treatment Rule**

Historical preserves validated medical knowledge. Health owns the bounded operational protocols by which that knowledge is applied. Research develops candidate changes and new evidence.

## 2. No single-source promotion

No single paper, study, clinician, AI model, manufacturer, institution, anecdote or successful patient outcome should silently promote a treatment into validated ordinary Health practice.

> **Single Source != Established Clinical Knowledge**

> **Publication != Protocol Authority**

> **Model Recommendation != Protocol Authority**

This does not prohibit experimental access. It separates ordinary validated care from explicitly experimental care.

## 3. Protocol lifecycle

A Health treatment protocol should have an explicit lifecycle:

**Validated Historical knowledge state**
→ Health protocol proposal/update
→ evidence mapping
→ indication and population definition
→ benefit/risk assessment
→ contraindication and interaction definition
→ diagnostic/evidential threshold
→ treatment specification
→ monitoring/failure/escalation rules
→ competence/resource requirements
→ authority/legal check
→ validation/review
→ versioned release
→ operational use
→ outcome surveillance
→ periodic/event-triggered review
→ revise / suspend / retire / supersede.

## 4. Minimum protocol content

A protocol should define, proportionately:

- protocol identifier/version;
- clinical purpose;
- evidence/knowledge references;
- eligible population;
- indication;
- diagnostic/evidential threshold;
- exclusions;
- contraindications;
- interactions;
- participant-specific modifiers;
- treatment/intervention;
- dose/intensity/duration where applicable;
- administration requirements;
- competence requirements;
- resource/facility requirements;
- monitoring;
- expected course;
- failure criteria;
- adverse-event triggers;
- stopping conditions;
- escalation/referral;
- recurrence/repeat-use rules;
- participant information;
- consent requirements;
- authority requirements;
- review triggers;
- provenance.

> **Treatment Instruction Without Applicability Boundary != Complete Protocol**

## 5. Evidence mapping

Every material protocol rule should be traceable to its evidential or authoritative basis where practicable.

The protocol should distinguish:
- directly evidence-supported rules;
- validated extrapolations;
- safety constraints;
- legal/authority constraints;
- operational constraints;
- unresolved uncertainty.

This prevents administrative convention from masquerading as medical evidence.

> **Protocol Rule != Necessarily Medical Evidence**

## 6. Validation dimensions

Protocol validation should ask separately whether the protocol is sufficiently supported in:

### Clinical validity
Does the represented evidence support the indication and intervention?

### Applicability
Is the target population/context adequately defined?

### Safety
Are known material harms, contraindications, interactions and monitoring needs represented?

### Diagnostic sufficiency
Is the required evidence before treatment proportionate to the consequences of treating incorrectly?

### Operational completeness
Can the protocol actually be executed safely?

### Competence
Does execution require specialist capability?

### Authority
Is any consequential prescribing/procedural authority independently legitimate?

### Information completeness
Could an omitted material dimension invalidate the protocol conclusion?

> **Evidence Strength != Operational Completeness**

## 7. Validation does not require unanimity

Medical evidence may remain contested.

A protocol can record:
- consensus;
- material minority interpretation;
- uncertainty;
- disputed evidence;
- confidence;
- conditions under which another route is reasonable.

> **Disagreement != Automatic Prohibition**

But unresolved disagreement must not be hidden by presenting one interpretation as certain.

## 8. Versioned protocols

Every operational protocol should be versioned.

A treatment episode should preserve which version governed the decision.

> **Current Protocol != Protocol That Existed At Earlier Time**

Historical should preserve prior versions and reasons for material change.

Health should ordinarily use the current applicable version unless a legitimate reason supports another route.

## 9. Knowledge change propagation

When Historical's validated medical knowledge state materially changes, KCS should identify potentially affected Health objects.

Conceptually:

**Historical Knowledge Change**
→ KCS candidate-review set
→ affected diagnostic rules / treatment protocols / screening rules / monitoring thresholds / participant information
→ domain review
→ update only where materially required
→ propagate further if operational state changes.

> **Knowledge Change != Automatic Protocol Invalidation**

A corrected paper or changed recommendation may be irrelevant to some protocols and critical to others.

## 10. Urgent safety change

Some evidence may justify immediate protocol suspension or restriction before a complete replacement protocol is ready.

Possible states include:
- ACTIVE;
- ACTIVE_WITH_CAUTION;
- REVIEW_REQUIRED;
- RESTRICTED;
- TEMPORARILY_SUSPENDED;
- SUPERSEDED;
- RETIRED;
- EVIDENCE_STATE_UNRESOLVED.

The substantive authority to suspend must be legitimately established; KCS itself only routes review.

## 11. Automated treatment eligibility

A protocol used for automated therapeutic authorisation requires a higher degree of explicit machine-resolvable boundedness than a protocol intended for professional judgement.

It should specify:
- required inputs;
- acceptable evidence freshness;
- decision thresholds;
- exclusions;
- unresolved-data handling;
- interaction/contraindication checks;
- permitted outputs;
- authority scope;
- expiry;
- escalation.

> **Clinically Valid Protocol != Automatically Automatable Protocol**

Where judgement remains materially necessary:

> **Automation Boundary Reached -> Professional Review**

not:

> **Automation Boundary Reached -> Guess**

## 12. Missing data

A protocol must define the consequence of missing material data.

Possible outcomes:
- data not required;
- proceed with uncertainty disclosed;
- obtain additional evidence;
- professional review;
- protocol unavailable.

> **Missing Data != Normal Finding**

## 13. Participant-specific application

Even a validated protocol does not automatically apply to a participant.

Application requires current participant evidence.

> **Validated Protocol != Participant Eligibility**

The protocol engine should preserve the reason for eligibility/ineligibility and the evidence used.

## 14. Protocol versus professional judgement

Professional judgement may legitimately operate:
- inside a protocol's permitted discretion;
- where the protocol explicitly routes to professional review;
- outside ordinary protocol under a separately justified non-standard/experimental route.

A professional should not silently override protocol boundaries without recording the basis.

> **Professional Expertise != Invisible Protocol Exception**

Conversely, a protocol should not prohibit justified professional reasoning merely to preserve automation.

## 15. Experimental boundary

Candidate treatments not validated for ordinary protocol use remain available through the experimental-treatment architecture where appropriate.

This prevents protocol governance from becoming a gatekeeping mechanism that equates:

**not yet standard**
with
**forbidden**.

> **Not Validated For Ordinary Care != Prohibited Experimental Choice**

The participant must be able to see which knowledge/evidence state applies.

## 16. Outcome surveillance

Operational protocols should produce outcome evidence sufficient to detect:
- unexpected treatment failure;
- adverse effects;
- subgroup differences;
- resistance;
- diagnostic mismatch;
- recurrence;
- implementation error.

Health uses these signals for care and safety.

Appropriately governed evidence may flow to Research for broader analysis.

> **Clinical Outcome Monitoring != Automatic Research Enrolment**

## 17. Feedback does not self-authorise protocol change

An automated system detecting better apparent outcomes from an alternative treatment must not silently rewrite the protocol.

> **Learning Signal != Authority To Change Care**

The signal routes to Research/validation and then, where warranted, Historical knowledge-state change and Health protocol review.

This prevents self-modifying clinical policy without governance.

## 18. Adverse-event pathway

Material adverse events should:
- protect/treat the participant;
- preserve evidence;
- determine whether the event is participant-specific or protocol-relevant;
- trigger appropriate review;
- notify other affected functions where legitimately required.

A single adverse event does not necessarily invalidate a treatment, but neither should aggregation hide serious individual harms.

## 19. Recall and participant notification

Where a protocol, medication, device or treatment is later found materially unsafe or incorrect, the system should identify affected participants where legitimate and route appropriate review/notification.

This is a KCS dependency problem combined with Health authority and contextual access.

> **Knowledge Of A Safety Change != Unlimited Access To Every Health Record**

The system should use bounded dependency/provenance links to identify materially affected episodes.

## 20. Protocol provenance

A protocol should preserve:
- creators/reviewers or responsible validation function;
- knowledge-state references;
- material evidence;
- previous version;
- changes;
- reason for change;
- validation state;
- release date;
- review date;
- dependencies;
- authority/legal references where required.

This enables audit without turning authorship into authority.

> **Authorship != Protocol Authority**

## 21. Conflicts of interest

Material conflicts should be represented where they could affect evaluation.

Examples may include:
- manufacturer sponsorship;
- financial interest;
- institutional interest;
- intellectual-property interest;
- professional advocacy.

Conflict does not automatically invalidate evidence.

> **Conflict Disclosure != Automatic Evidence Rejection**

It is information relevant to evaluation and trust.

## 22. Protocol review triggers

Review may be triggered by:
- material Historical knowledge change;
- new Research evidence;
- safety signal;
- treatment failure pattern;
- resistance change;
- diagnostic change;
- new interaction/contraindication;
- manufacturing/device change;
- legal/authority change;
- implementation failure;
- scheduled freshness review.

> **Review Trigger != Predetermined Review Outcome**

## 23. Protocol retirement

A retired protocol should not simply disappear.

Historical should preserve:
- its content;
- period of validity;
- reason for retirement;
- successor where applicable;
- affected historical episodes/provenance.

Health should prevent new ordinary use after retirement while preserving historical interpretability.

## 24. Knowledge and authority separation

Several independent questions may need to be satisfied:

- Is the medical knowledge sufficiently validated?
- Does the protocol operationalise it correctly?
- Does it apply to this participant?
- Is the actor/system competent?
- Is the required treatment authority present?
- Has the participant consented where required?
- Is the actual route permissible?

MKA can verify required authority composition but does not supply clinical validity.

> **Clinical Validity != Authority**

> **Authority != Clinical Validity**

Both may be necessary.

## 25. Protocol validation record

A conceptual record may include:

**HealthProtocol**
- ProtocolRef
- Version
- Purpose
- KnowledgeStateRefs
- EvidenceRefs
- Population
- Indications
- DiagnosticThreshold
- Exclusions
- Contraindications
- Interactions
- TreatmentSpecification
- Monitoring
- FailureCriteria
- AdverseTriggers
- Escalation
- CompetenceRequirements
- AuthorityRequirements
- AutomationEligibility
- ConsentRequirements
- ValidationState
- UncertaintyState
- Dependencies
- ReviewTriggers
- EffectiveFrom
- ReviewDue
- Supersedes
- Provenance

## 26. Compact knowledge-to-care chain

**Research**
→ candidate evidence

**Validation**
→ determines whether broader knowledge state should change

**Historical**
→ preserves validated knowledge and provenance

**Health Protocol Governance**
→ translates relevant validated knowledge into bounded operational protocol

**Health**
→ applies protocol to current participant evidence

**Outcome**
→ care response + appropriately governed learning

**Research**
→ evaluates broader meaning.

## 27. Core invariants

> **Medical Knowledge != Clinical Protocol**

> **Evidence Of Benefit != Complete Operational Treatment Rule**

> **Single Source != Established Clinical Knowledge**

> **Publication != Protocol Authority**

> **Model Recommendation != Protocol Authority**

> **Treatment Instruction Without Applicability Boundary != Complete Protocol**

> **Evidence Strength != Operational Completeness**

> **Knowledge Change != Automatic Protocol Invalidation**

> **Clinically Valid Protocol != Automatically Automatable Protocol**

> **Missing Data != Normal Finding**

> **Validated Protocol != Participant Eligibility**

> **Professional Expertise != Invisible Protocol Exception**

> **Not Validated For Ordinary Care != Prohibited Experimental Choice**

> **Learning Signal != Authority To Change Care**

> **Review Trigger != Predetermined Review Outcome**

> **Clinical Validity != Authority**

> **Authority != Clinical Validity**

## 28. Remaining development

This architecture establishes governance grammar but does not itself provide:
- specialist medical evidence;
- exact evidence-grading method;
- protocol-review institutional composition;
- professional qualification rules;
- pharmaceutical manufacturing/quality rules;
- detailed pharmacovigilance;
- jurisdiction-specific prescribing law;
- deployable machine-readable clinical protocol format;
- empirical validation of automated clinical pathways.

These remain specialist Health/Research/Historical/Law implementation work.
