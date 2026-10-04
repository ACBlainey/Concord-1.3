# Clinical Learning Signal Intake, Triage and Research Routing 001

**Project:** The Concord
**Date:** 4 October 2026
**Status:** CROSS-DOMAIN ARCHITECTURE / PROVISIONAL / NON-CANONICAL
**Domains:** Health / Research
**Downstream:** Historical / Education
**Dependencies:** Clinical Experience to Medical Knowledge Learning Loop 001 / Civil Attention / PLE / CIBB / ESCP / Mirrored Reality Trees

## 1. Purpose

Define the bounded interface by which observations arising from clinical practice become visible to Research without:
- requiring a formal paper;
- exposing unnecessary participant information;
- losing rare but important observations;
- allowing anecdote to become established medical knowledge;
- allowing triage to become covert knowledge validation.

> **Low-Friction Intake; Independent Evidential Promotion**

## 2. Sources

A learning signal may originate from:
- participant feedback;
- clinician/professional observation;
- case outcome;
- adverse event;
- near miss;
- diagnostic mismatch;
- unexpected treatment response;
- protocol failure or ambiguity;
- device/equipment behaviour;
- repeated service pattern;
- automated outcome/pattern detection;
- another Health function.

Source identity and competence may affect interpretation and follow-up, but do not determine truth.

> **Source Credibility != Claim Validity**

## 3. Minimal signal structure

A ClinicalLearningSignal should preserve, where available:
- SignalRef;
- SourceClass;
- ReporterRef or protected/pseudonymous route where legitimate;
- ClinicalContextRef;
- Observation;
- ExpectedState/Outcome;
- ObservedState/Outcome;
- Discrepancy;
- Timing;
- Intervention/Protocol/DiagnosticVersion refs;
- Interpretation, explicitly separate from observation;
- ProposedExplanation, if any;
- SafetySeverity;
- RecurrenceKnown/Unknown;
- ParticipantImpact;
- EvidenceRefs under protected access;
- Uncertainty;
- PrivacyClass;
- Urgency;
- RelatedSignalRefs;
- Provenance.

A signal may be incomplete and still worth preserving.

> **Incomplete Report != Worthless Report**

## 4. Observation, interpretation and hypothesis

The intake must preserve three different layers:

**Observation:** what was seen/reported/measured.

**Interpretation:** what the reporter thinks it may mean.

**Hypothesis:** an explanation capable of Research testing.

> **Observation != Interpretation != Hypothesis**

This prevents professional confidence or automated classification from silently converting interpretation into fact.

## 5. Triage purpose

Triage determines **what should happen to the signal next**.

It does not determine whether the proposed medical conclusion is true.

> **Triage Priority != Evidential Strength**

> **Research Routing != Knowledge Validation**

A weakly evidenced report of a catastrophic possible harm may deserve urgent review; a strongly evidenced but low-consequence observation may not require urgent action.

## 6. Independent triage dimensions

Signals should be considered across distinct dimensions such as:
- possible severity;
- urgency;
- novelty;
- recurrence;
- evidential specificity;
- plausibility/known mechanism where relevant;
- population reach;
- reversibility;
- detectability;
- current exposure;
- protocol dependency;
- uncertainty;
- privacy/sensitivity;
- availability of alternative explanations.

These dimensions should not be collapsed prematurely into one opaque score.

## 7. Routing states

Candidate routing outcomes:

- RECORD_ONLY;
- LINK_TO_EXISTING;
- REQUEST_CLARIFICATION;
- ROUTINE_RESEARCH_REVIEW;
- PRIORITY_RESEARCH_REVIEW;
- AGGREGATION_WATCH;
- FORMAL_INVESTIGATION_CANDIDATE;
- URGENT_SAFETY_REVIEW;
- IMMEDIATE_HEALTH_SAFETY_ESCALATION;
- OTHER_DOMAIN_ROUTE;
- INSUFFICIENT_TO_ROUTE;
- CLOSED_WITH_REASON.

A signal may occupy more than one legitimate route.

> **One Signal != One Mandatory Route**

## 8. Rare severe events

A single severe or unusual event may warrant urgent review even where causality is uncertain.

> **Low Frequency != Low Importance**

> **Single Case != No Signal**

Urgent review should preserve the distinction between:
- event occurred;
- association suspected;
- causality established.

## 9. Repeated weak signals

Individually weak observations may become important when they recur.

The system should support semantic linking across related signals without requiring reporters to know that similar cases exist.

Potential recurrence should trigger Research comparison, not automatic causal promotion.

> **Weak Signals May Aggregate Into A Strong Research Question Without Automatically Becoming A Strong Conclusion**

## 10. Diagnostic mismatch

A learning signal should be available when:
- observed course does not fit diagnosis;
- repeated tests contradict the working model;
- treatment response exposes an unexplained branch;
- later evidence reveals a previously unrepresented explanation.

Mirrored Reality Trees may help Research ask whether the problem is:
- wrong diagnosis;
- incomplete diagnosis;
- multiple conditions;
- incorrect treatment model;
- measurement error;
- unrepresented variable;
- genuinely unusual case.

> **Failure Of Expected Course -> Reopen The Question, Not Merely Intensify The Existing Answer**

## 11. Professional feedback without punishment default

Professionals should be able to report uncertainty, mistakes, near misses and protocol weaknesses without the learning route automatically becoming disciplinary intake.

Where independent evidence indicates misconduct or unlawful behaviour, a separate route may be opened.

> **Learning Intake != Disciplinary Intake**

> **Separation Of Routes != Immunity From Accountability**

## 12. Participant-originated signals

Participant reports receive the same structural separation of observation, interpretation and hypothesis.

A participant does not need professional status to report a potentially important effect.

Where a report indicates an unresolved personal Health need, Research routing must not substitute for clinical care.

> **Research Interest != Participant Care**

The signal can therefore create two bounded routes:
- care/reassessment for the participant;
- Research learning where broader significance may exist.

## 13. Automated signals

Automated monitoring may create signals from outcome patterns.

The system should record:
- detection method/version;
- data scope;
- threshold;
- known limitations;
- whether cases are independent;
- possible duplicate/correlation effects.

> **Automated Detection != Independent Replication**

## 14. Duplicate and linked reports

Duplicate reports should not simply be discarded.

They may provide evidence of recurrence.

The system should distinguish:
- literal duplicate of same event;
- correlated report of same event;
- independent similar event;
- semantically related but different event.

> **Duplicate Record != Independent Evidence**

## 15. Privacy at intake

Research should receive the minimum information necessary for triage.

Detailed protected clinical evidence remains in Health unless legitimate Research access is established.

PLE may answer bounded questions locally.

CIBB/contextual projections may expose necessary case details without transferring the master record.

> **Triage Need != Full Record Access**

## 16. Safety branch

Where a signal suggests serious current danger, the safety branch may run in parallel with Research.

**Signal**
→ urgent safety triage
→ bounded Health/protocol precaution where independently justified
while
→ Research investigation continues.

> **Safety Action Need Not Wait For Epistemic Certainty**

but:

> **Safety Precaution != Final Causal Finding**

## 17. Research intake conversion

Once Research accepts a signal for substantive work, it should create a Research object distinct from the original clinical signal.

Possible objects:
- research question;
- anomaly cluster;
- safety hypothesis;
- protocol-performance question;
- diagnostic hypothesis;
- candidate interaction;
- observational study proposal;
- experimental study proposal.

The original signal remains provenance.

> **Clinical Signal != Research Project**

## 18. Aggregation watch

Some signals should remain open for future comparison without immediate investigation.

AGGREGATION_WATCH can ask:
- has this occurred again?
- does it cluster around a treatment/protocol/device?
- is a subgroup emerging?
- does incidence exceed expected background?

The watch itself must not create unlimited surveillance authority.

> **Aggregation Need != General Surveillance Authority**

## 19. Reporter feedback

The reporter should receive useful status where legitimate:
- accepted;
- linked to existing signal;
- clarification requested;
- under Research review;
- aggregation watch;
- investigation opened;
- safety escalated;
- closed with reason;
- downstream validated change where appropriate.

Feedback should not expose other participants or protected Research material.

## 20. Triage audit

The system should preserve enough provenance to detect:
- ignored safety reports;
- systematic dismissal of participant reports;
- prestige bias;
- institutional suppression;
- duplicate inflation;
- excessive escalation;
- conflicts of interest;
- recurring closure reasons.

Audit should examine routing quality without becoming a shadow clinical database.

> **Triage Audit != Centralised Case Archive**

## 21. Escalation by pattern

A later signal may change the significance of earlier closed or watch-state signals.

New recurrence can trigger reopening.

> **Closed For Insufficient Evidence != Permanently Irrelevant**

This is a STRA/KCS-compatible state change.

## 22. Compact lifecycle

**Observation / Outcome / Feedback**
→ **ClinicalLearningSignal**
→ **privacy-preserving intake**
→ **multidimensional triage**
→ **record/link/clarify/watch/research/safety route**
→ **Research object where warranted**
→ **investigation/validation**
→ **Historical promotion where warranted**
→ **KCS**
→ **Health/Education change**
→ **new clinical outcomes**.

## 23. Core invariants

CLS-01 Low-Friction Intake; Independent Evidential Promotion.
CLS-02 Source Credibility != Claim Validity.
CLS-03 Observation != Interpretation != Hypothesis.
CLS-04 Triage Priority != Evidential Strength.
CLS-05 Research Routing != Knowledge Validation.
CLS-06 Low Frequency != Low Importance.
CLS-07 Duplicate Record != Independent Evidence.
CLS-08 Learning Intake != Disciplinary Intake.
CLS-09 Research Interest != Participant Care.
CLS-10 Automated Detection != Independent Replication.
CLS-11 Triage Need != Full Record Access.
CLS-12 Safety Precaution != Final Causal Finding.
CLS-13 Clinical Signal != Research Project.
CLS-14 Aggregation Need != General Surveillance Authority.
CLS-15 Closed For Insufficient Evidence != Permanently Irrelevant.

## 24. Remaining implementation

Still required:
- exact forms/UI;
- specialty-specific severity criteria;
- pharmacovigilance-specific mandatory reporting;
- exact Research staffing/authority;
- automated clustering implementation;
- cross-provider signal federation;
- quantitative alert thresholds;
- formal validation/promotion architecture.

This document defines routing grammar rather than medical thresholds.
