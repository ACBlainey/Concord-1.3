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
