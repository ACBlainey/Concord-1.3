# Legal Mental State and Culpability Classifiers — Intent, Knowledge, Recklessness, Negligence and Accident 001

**Project:** The Concord Framework  
**Domain:** Law  
**Date:** 7 October 2026  
**Status:** ACTIVE DEVELOPMENT / CANDIDATE GENERAL LEGAL ARCHITECTURE / NON-CANONICAL  
**Parent:** `Legal Derivation and Consequence Architecture — Ethical Provenance, Offence Classifiers and Proportionate Response 001.md`

---

## 1. Purpose

This document defines a reusable candidate mental-state grammar for Concord Law.

The same harmful result can arise through deliberate action, knowing action, recklessness, negligence or non-culpable accident. These states must not be inferred from outcome alone.

> **Outcome != Mental State.**

> **Harm Severity != Culpability By Itself.**

---

## 2. Mental state is offence-relative

Mental state must identify what proposition or result the participant intended, knew, risked or failed to foresee.

A participant may intentionally perform an act without intending every consequence of it.

Therefore:

> **Intent To Act != Intent To Cause Every Result.**

Legal findings should identify the relevant object:

- intent as to conduct;
- intent as to result;
- knowledge of circumstance;
- knowledge of consequence;
- awareness of risk;
- duty to recognise risk.

---

## 3. Deliberate / intentional

Candidate definition:

A result is **deliberate/intended** where producing that result was an objective of the participant's action, or the participant acted for the purpose of bringing it about.

Example:

A deliberately strikes B for the purpose of causing serious injury.

The fact that the actual injury is less or greater than intended is recorded separately.

> **Intent May Exist Without Success.**

---

## 4. Knowing

Candidate definition:

A participant acts **knowingly** as to a result where the result is not necessarily their purpose but they act while understanding that the result will occur or is effectively certain in the circumstances as they understand them.

This preserves a distinction between:

**I want X to happen**

and:

**X is not my objective, but I know my action will cause X.**

Whether particular offences should treat knowledge identically to intent is an offence-specific legal question.

---

## 5. Recklessness

Candidate definition:

A participant acts **recklessly** where:

1. a material risk of prohibited harm exists;
2. the participant is aware of that risk;
3. the participant nevertheless proceeds; and
4. taking that risk is unjustified or disproportionate in the relevant context.

Recklessness therefore contains both an epistemic and contextual component.

> **Risk Awareness != Automatic Recklessness.**

Some activities legitimately involve known risk.

Sport, medicine, engineering, rescue and ordinary life can contain foreseeable risks whose acceptance remains justified.

The legal question includes whether the risk was legitimate in context.

---

## 6. Negligence

Negligence differs from recklessness because actual awareness of the risk need not be established.

Candidate definition:

A participant acts **negligently** where:

1. an applicable duty of care exists;
2. a material harmful risk was sufficiently foreseeable under that duty;
3. the participant failed to meet the required standard of care;
4. the failure materially contributed to the prohibited result or legally relevant risk.

Therefore:

> **Could Have Known != Automatically Negligent.**

> **Bad Outcome != Negligence.**

Negligence requires a legitimate duty and standard, not hindsight.

Criminal or punitive negligence should likely require a substantially stronger threshold than ordinary civil error. Exact thresholds remain undeveloped.

---

## 7. Non-culpable accident

A harmful event may occur without a culpable mental state or breach.

Candidate classification:

**Harm Established + No Intent + No Relevant Knowledge + No Recklessness + No Applicable Negligence = Non-Culpable Accident Candidate**

This does not determine questions of insurance, social support, no-fault compensation or other civil loss allocation.

> **No Criminal Culpability != No Need For Remedy Or Support.**

---

## 8. Foreseeability

Foreseeability must be temporally disciplined.

The relevant question is what could legitimately have been known or anticipated **before the act or omission**, not what became obvious after the outcome.

> **Outcome Knowledge Must Not Be Back-Propagated Into Prior Foreseeability.**

This is particularly important for negligence and professional decision-making.

---

## 9. Mistake

Mistake may affect mental state.

Relevant forms can include:
- mistake of fact;
- mistaken identity;
- mistaken risk estimate;
- mistaken authority;
- mistaken defensive context;
- impaired reality model.

A genuine mistake is not automatically reasonable.

The existing Mistaken Authority architecture should remain applicable where authority is involved.

Candidate sequence:

**Belief State → Evidence Available At Time → Reasonableness / Reliability → Mental-State Effect → Defence Or Mitigation Where Legally Recognised**

---

## 10. Capacity is separate

A participant may possess intent, knowledge or risk awareness while lacking or having impaired legally relevant capacity.

Therefore:

> **Mental State != Capacity.**

> **Intent != Full Authorship.**

> **Knowledge != Full Capacity.**

Capacity affects responsibility for the mental state; it does not necessarily erase evidence that the mental state existed.

---

## 11. Premeditation is separate

Premeditation concerns temporal planning and preparation, not the existence of intent itself.

An intentional act can be immediate and unplanned.

A premeditated act can be committed under impaired capacity.

Therefore:

> **Intent != Premeditation.**

> **Premeditation != Capacity.**

Premeditation belongs primarily in aggravation where the base law makes it relevant.

---

## 12. Candidate hierarchy is not automatic sentencing hierarchy

Intent, knowledge, recklessness and negligence often represent decreasing degrees of subjective culpability, but they should not become an inflexible universal sentencing ladder.

Context, actual harm, intended harm, capacity, duties, vulnerability, authority and other factors remain relevant.

> **Classifier Order != Automatic Sentence Order.**

---

## 13. Omissions

Some offences may arise from culpable omission rather than positive action.

An omission requires a legitimate duty to act.

> **Capability To Help != Automatic Legal Duty To Act.**

A legal duty may arise from defined roles, voluntarily accepted responsibility, creation of danger, guardianship/care relations, contract, or other legitimate legal source.

The source and scope of the duty must be stated.

---

## 14. Evidence

Mental state is usually inferred from evidence rather than directly observed.

Relevant evidence may include:
- statements;
- preparation;
- conduct before/during/after event;
- mechanism selected;
- warnings received;
- expertise;
- repeated conduct;
- concealment;
- contextual information available at the time.

No single evidence type automatically establishes the classifier.

> **Mechanism May Evidence Intent; Mechanism Does Not Define Intent.**

> **Silence Alone != Proof Of Mental State.**

---

## 15. Candidate invariants

MSC-01 Outcome != Mental State.  
MSC-02 Harm Severity != Culpability By Itself.  
MSC-03 Intent To Act != Intent To Cause Every Result.  
MSC-04 Intent May Exist Without Success.  
MSC-05 Risk Awareness != Automatic Recklessness.  
MSC-06 Could Have Known != Automatically Negligent.  
MSC-07 Bad Outcome != Negligence.  
MSC-08 Outcome Knowledge Must Not Be Back-Propagated Into Prior Foreseeability.  
MSC-09 Mental State != Capacity.  
MSC-10 Intent != Premeditation.  
MSC-11 Premeditation != Capacity.  
MSC-12 Classifier Order != Automatic Sentence Order.  
MSC-13 Capability To Help != Automatic Legal Duty To Act.  
MSC-14 Mechanism May Evidence Intent; Mechanism Does Not Define Intent.

---

## 16. Development result

The candidate reusable mental-state set is:

**INTENTIONAL / DELIBERATE**  
**KNOWING**  
**RECKLESS**  
**NEGLIGENT**  
**NON-CULPABLE ACCIDENT**

Each offence should specify which states can satisfy its elements rather than assuming every classifier applies universally.
