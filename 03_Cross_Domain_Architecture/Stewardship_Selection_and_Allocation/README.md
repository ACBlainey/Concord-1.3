# Stewardship Selection and Allocation — Development

**Project:** The Concord  
**Status:** ACTIVE DEVELOPMENT / SHARED CROSS-DOMAIN DEPENDENCY  
**Date opened:** 10 October 2026

## 1. Purpose

This folder is the development home for a common Concord architecture governing the **selection and allocation of qualified, eligible participants into entrusted or representative offices**.

The mechanism is intentionally **not designed yet**.

The immediate purpose is to prevent Judiciary, Governance, Civil Security, Defence and other domains from independently inventing incompatible appointment systems while the common architecture remains unresolved.

## 2. Scope

The architecture is expected to be reusable, with domain-specific companion requirements, for offices including:

- Governance Stewards;
- Judicial Stewards / judges;
- police chiefs, sheriffs or equivalent Civil Security leadership;
- Defence command or entrusted Defence stewardship offices;
- other representative offices;
- other consequential entrusted Steward positions where selection from an eligible candidate pool is required.

The shared mechanism may also prove applicable to additional civil offices after source resolution and testing.

## 3. Existing architectural boundary

Current Concord architecture already separates several states that must not be collapsed:

**Participation / Standing != Qualification != Eligibility != Selection / Allocation != Appointment != Mandate != Authority**

A provisional cross-domain lifecycle is:

**Participation / Standing**  
→ **Function-Specific Qualification**  
→ **Current Eligibility / Suitability / Conflict Review**  
→ **Selection / Allocation**  
→ **Appointment / Office Constitution**  
→ **Mandate**  
→ **Bounded Exercise of Authority**  
→ **Monitoring / Audit**  
→ **Rotation / Continuation**  
→ **Recall / Suspension / Removal where justified**  
→ **Succession / Replacement**

For consequential decisions, Concord's general triadic principle should be presumed applicable wherever practicable, including appointment decisions, but the architecture must still resolve **how the selecting/appointing triad itself is legitimately constituted**.

## 4. Shared core, domain-specific companions

The intended pattern is:

> **Common Selection / Allocation Core + Domain-Specific Qualification and Eligibility + Domain-Specific Mandate = Legitimately Constituted Office**

The common architecture should determine reusable questions such as:
- how an eligible candidate pool becomes a selection set;
- who has standing or authority to participate in selection;
- how selectors are constituted;
- whether and where triadic selection applies;
- how conflicts and capture risks are handled;
- how local/functional representation is preserved;
- how rotation and succession interact with selection;
- how vacancies and temporary appointments are handled;
- how selection is audited and contested;
- how failed or deadlocked selections are resolved;
- how selector dependence is prevented from becoming ownership of the office-holder;
- how GTP spatial contexts interact with representative selection where relevant;
- how selection remains substrate-neutral without assuming identical qualification requirements.

Domain companions should determine:
- required competence;
- role-specific qualification;
- role-specific eligibility;
- role-specific conflicts;
- jurisdiction;
- mandate;
- term/continuity requirements;
- special removal or disciplinary interfaces.

## 5. Known source constraints

Existing source resolution already establishes:

> **Qualification != Authority.**

> **Eligibility != Allocation.**

> **Competence != Authority.**

> **Authority Verification != Authority Creation.**

> **Triadic Governance Vote != Public Election.**

> **Steward Selection != Presumed Popular Election.**

> **Appointment Creates Responsibility, Not Political Debt.**

V1 governance establishes extensive selection-adjacent architecture but does not settle a universal selector.

V1.2 Historical source resolution likewise records that the actual Concord public-election mechanism remained unresolved.

Judiciary V2 identifies selection as a major capture point and warns against political appointment, judicial self-selection/guild capture, election/popularity capture, professional-body capture, algorithmic selection and reputation-based conformity.

Therefore no one conventional mechanism should be inserted by assumption.

## 6. Development question

The central development question is:

> **Given a pool of independently qualified and currently eligible candidates, how does the Concord select and allocate participants to entrusted or representative offices without allowing the selector, incumbent institution, profession, political faction, algorithm, geography or temporary majority to own the resulting office?**

Subsidiary questions include whether one mechanism is sufficient for all office classes or whether a common grammar should support bounded variants.

## 7. Current rule

Until this architecture is developed:

> **Dependent domains should declare the selection/allocation dependency rather than invent a local final mechanism.**

Existing valid domain-specific qualification, eligibility, authority, discipline and succession architecture remains in force and should not be overwritten.

## 8. Initial dependent domains

- Governance
- Judiciary
- Civil Security
- Defence

Likely later dependencies should be added only after source resolution demonstrates that the domain contains an entrusted/representative office requiring this mechanism.

## 9. Development status

**OPEN — ARCHITECTURE RESERVED FOR LATER DESIGN**

No final rule for election, nomination, sortition, matching, appointment, selector composition, weighting or allocation is established by this file.

## 10. Authorial direction — Steward ascension pathway (12 October 2026)

**Status: AUTHORIAL DESIGN DIRECTION / PROPOSED SELECTION PREFERENCE; NOT YET A FINALISED CONSTITUTIONAL APPOINTMENT RULE.**

The author has specified a shared approach analogous to judicial selection:

- **Historical** owns and preserves stewardship knowledge, including training/experience provenance and decision-making records, subject to contextual access and privacy controls.
- **Education** owns training and accreditation of stewardship competence. Historical's custody of knowledge does not make it the accreditor or selector.
- **Participant tier** controls office eligibility together with current function-specific qualifications, suitability and conflict checks. Tier alone does not constitute an appointment or confer authority.
- The remaining selection alternatives are **democratic vote**, **meritocratic assignment**, and **ascension from a parallel Steward role**. Ascension is the **preferred development route**, not yet an exclusive or automatically operative selector.

**Ascension principle:** A trained, accredited, currently eligible parallel (shadow) Steward may accumulate time-served practice and an independently reviewable provenance record of reasoning, decisions and relevant competence before becoming a candidate for an authorised Steward vacancy. This is attractive because a candidate's experience can be assessed from prior practice rather than reputation or promises alone.

**Critical separation:** Parallel role ≠ constituted voting office; time served ≠ eligibility by itself; documented performance ≠ guaranteed promotion; qualification/eligibility/selection ≠ appointment/mandate/authority. Any shadow participation must have an explicitly bounded role, protect live decisions from unauthorised votes and preserve the independence and privacy of affected participants.

**Reusable existing mechanisms to evaluate:** Education accreditation, Historical records and provenance, State and Maturity Mapping (role readiness), Contextual Wrapper Architecture and Fractal Permission Architecture (parallel-role limits), Multi-Key Authority (appointment/mandate validity), STRA (review and readiness triggers), BTA (transition into or out of office), KCS (qualification/status changes), and fault-tolerant responsibility continuity (vacancy/succession). Reuse requires owner-system agreement and host-specific validation.

**Still genuinely unresolved:** Who chooses among several eligible time-served parallel Stewards; how shadow positions are allocated; minimum experience and evidence thresholds; evaluation of dissent, abstention and independently reasoned minority positions without rewarding conformity; capture resistance and appeal; whether public vote or merit assignment remains available for particular office types; who lawfully constitutes the appointing decision; rotation, vacancy and emergency succession. In particular, a favourable Historical record or Education accreditation must never silently become a self-executing promotion.

This section develops the shared core; Judiciary, Governance, Civil Security and Defence retain their independent qualification, jurisdiction and mandate requirements.

## 11. Reality-anchored comparative Steward evaluation — authorial direction (12 October 2026)

**Status: AUTHORIAL DESIGN DIRECTION; evaluation specification and thresholds remain to be developed.**

**Reality is the final arbiter of factual claims and observable consequences.** Incumbent and parallel Stewards should independently record their contemporaneous vote, reasoning, evidence, assumptions, predicted consequences and uncertainty for comparable decision events. Historical preserves the time-stamped provenance; the authorised evaluation function later compares the competing positions with what actually occurred, as evidence becomes available. Education may use the results for competence development and accreditation, without becoming the selector or historical custodian.

**Non-conformity rule:** A parallel Steward is **not** rewarded for matching an incumbent merely because they matched. Agreement is favourable evidence only insofar as both decisions withstand subsequent reality-based and process-quality assessment. A well-supported dissenting parallel Steward can outperform an incumbent; an incumbent can likewise outperform the parallel. The system must not institutionalise incumbency as ground truth.

**Minimum comparison record:** decision-event identity; question and lawful context; incumbent and parallel position/role; each independently frozen vote and abstention reason; contemporaneously available evidence and uncertainty; forecast or falsifiable claims where applicable; actual authorised implementation (which may differ from either recommendation); observed outcomes and time horizon; external conditions, interventions and confounders; retrospective evidential quality; attribution limits; and contestation/correction provenance. Preserve original predictions even when corrected later.

**Epistemic safeguards:** Outcomes are not always observable, attributable, immediate or reducible to one metric. Do not conflate a good ex-ante decision with a lucky ex-post result, or a justified decision with an unlucky outcome. Evaluate calibrated predictions, evidential reasoning, lawful process, appropriate abstention, consideration of alternatives, harms and benefits, and eventual observable consequences **separately** before any aggregate readiness judgement. A parallel Steward's unimplemented counterfactual remains a prediction, not an observed alternate world; score it only against outcomes that genuinely test its claims. Use multiple comparable cases and disclose uncertainty rather than manufacturing a single objective winner.

**Anti-capture:** Neither incumbent Stewards nor their appointing circle should unilaterally control case selection, metric design, scoring, record suppression or promotion. Historical custody is not endorsement. Protect private decision materials using contextual projections; permit independent audit, corrections and appeals. No performance score automatically creates eligibility, appointment, mandate or authority.

**Reusable Concord mechanisms for later host-specific design:** Historical provenance; Education accreditation; Reality Trees / mirrored alternative reasoning; SMM for readiness state; STRA for due-outcome review; KCS for evidence updates; CWA/CIBB for protected decision records; BTA for ascension transitions; MKA for appointment validity. **Still unresolved:** outcome definitions, comparator cohorts, case mix, observation windows, calibration methodology, evaluation authority, threshold, dispute mechanism and final selection among multiple qualified candidates.
