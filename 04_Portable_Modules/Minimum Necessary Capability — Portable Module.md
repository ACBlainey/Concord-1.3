# Minimum Necessary Capability — A Portable Architecture for Bounding Power, Permission and Access

**Version:** 0.2  
**Status:** PORTABLE ARCHITECTURE CANDIDATE / POST-TRANSFER REVISION / GRADUATION REVIEW REQUIRED  
**Development class:** Level B — Extractable Architectures  
**Source lineage:** Concord Minimum Necessary Capability architecture and related authority/permission architecture  
**Date:** September 2026

---

## 1. Purpose

Minimum Necessary Capability (MNC) is a general architecture for deciding what consequential capability a participant, role, institution, software system or other actor should possess when a legitimate function requires the ability to affect another participant, resource, space, process, information domain or system.

Its core chain is:

> **Purpose → Function → Need → Minimum Sufficient Capability → Bounded Exercise → Review → Termination or Re-Justification**

MNC addresses two symmetric errors:

- granting more capability than the legitimate function requires; and
- granting too little capability for the function or assigned responsibility to be performed reliably.

Therefore:

> **Minimum Necessary ≠ Minimum Possible**

MNC is not a universal theory of legitimacy. It requires the applicable normative, legal, contractual, organisational or other legitimate basis to be supplied by the context in which it is used.

---

## 2. Core definition

> **Where a legitimate objective requires a function that cannot be performed without additional capability being legitimately established for a participant, institution or system, that capability should be sufficient to perform the function but no broader, stronger, longer-lasting, more intrusive, more transferable or more persistent than the function reasonably requires.**

The target is the **least capability sufficient to perform the legitimate function to the required standard under reasonably foreseeable conditions**.

This creates both:

- a **necessary floor**, below which the function cannot reliably be discharged; and
- a **justified ceiling**, above which capability is no longer adequately supported by the function.

---

## 3. Capability

For this architecture, capability means an ability through which an actor or system can materially affect another participant, resource, space, process, information domain or function.

Capability may arise through:

- consent;
- role;
- responsibility;
- authority;
- property;
- contract;
- emergency conditions;
- delegation;
- technical access;
- dependency;
- or combinations of these.

The architecture distinguishes:

> **Legitimate Capability ≠ Physical Capability**

> **Legitimate Capability ≠ Technical Capability**

> **Declared Capability ≠ Actual Capability**

> **Formal Authority ≠ Effective Power**

A system can therefore be over-capable even where its formal permission appears narrow, or under-capable despite a broad formal responsibility.

---

## 4. Applicability

MNC may be useful where a system must decide the justified extent of consequential capability, including candidate applications such as:

- organisational roles;
- software permissions;
- AI agent and tool access;
- data access;
- contractor credentials;
- delegated authority;
- emergency response;
- professional access;
- infrastructure administration;
- physical-space access;
- multi-agent systems.

These are candidate domains, not validated use domains.

MNC is especially relevant where capability can:

- intrude on protected interests;
- persist after its purpose ends;
- combine with other capabilities;
- be delegated or escalated;
- create dependency;
- or materially affect participants who did not create the capability.

---

## 5. Required inputs

A minimum MNC assessment requires:

1. a stated problem or objective;
2. the claimed legitimate basis for pursuing it;
3. relevant evidence and context;
4. the function actually required;
5. existing capabilities and feasible alternatives;
6. the proposed additional capability;
7. affected participants or systems;
8. applicable protected rights, interests and constraints;
9. expected consequence and intrusion;
10. relevant capability dimensions;
11. review and termination conditions.

If legitimacy, evidence, function or need is unresolved, record **UNKNOWN** or **DISPUTED** rather than manufacturing certainty.

---

## 6. Step 1 — Establish the legitimate purpose

Ask:

> **What legitimate objective or problem requires action?**

Record the basis supplied by the surrounding system: for example law, contract, consent, organisational responsibility, safety requirement, protected right, policy or another applicable source.

MNC does not convert an asserted purpose into a legitimate one merely because capability would be useful.

A purpose that lacks an adequate legitimate basis cannot justify capability through MNC alone.

---

## 7. Step 2 — Resolve the required function

Ask:

> **What function must actually be performed to address the legitimate objective?**

Do not begin with the desired power or permission and construct a function around it.

> **Capability Should Follow Justified Function.**

The function should be specific enough to test what capability it genuinely requires.

Where the function is disputed, record the dispute and identify what evidence or authority can resolve it.

---

## 8. Step 3 — Examine existing capability and alternatives

Before adding capability, determine whether the function can already be performed through:

- existing capability;
- a narrower use of existing capability;
- a less intrusive alternative;
- a different actor already possessing legitimate capability;
- redesign of the function;
- or another feasible mechanism.

> **Legitimate Convenience ≠ Necessity for Additional Capability.**

The existence of a faster or easier option does not by itself prove that additional consequential capability is necessary.

An actor may require professional or operational judgement in deciding how to exercise capability already granted. That does not itself authorise the actor to enlarge the capability.

> **Operational Discretion Within Capability ≠ Authority to Expand Capability.**

---

## 9. Step 4 — Demonstrate need

If existing capability and feasible alternatives are insufficient, state what additional capability is required and why.

The justification should connect:

**Purpose → Function → Capability Need**

Avoid:

**Desired Capability → Retrospective Function → Self-Justification**

Where the proposed capability holder controls the evidence, problem definition, function definition and capability request, additional independent scrutiny may be required.

---

## 10. Step 5 — Determine the necessary capability floor

Ask:

> **What is the least capability that remains sufficient to perform the legitimate function reliably to the required standard under reasonably foreseeable conditions?**

The floor must account for actual operating conditions rather than ideal conditions only.

The floor describes the minimum **positive abilities** required to perform the function. Restrictions such as prohibited delegation, excluded data or maximum persistence belong to the capability boundary or justified ceiling rather than to the floor itself.

> **Capability Floor ≠ Capability Boundary/Ceiling.**

A capability below this floor creates under-capability.

> **Necessary but Insufficient ≠ Legitimate Design**

MNC must not assign responsibility while withholding the means reasonably required to discharge it.

---

## 11. Step 6 — Determine the justified capability ceiling

Ask:

> **At what point does additional capability cease to be reasonably required by the legitimate function?**

Capability above this ceiling is excessive unless independently justified by another legitimate function or basis.

> **Sufficient but Unnecessary ≠ Legitimate Grant**

The objective is not maximal restriction. It is sufficient capability without unsupported excess.

---

## 12. Step 7 — Bound capability multidimensionally

Capability is not one scalar quantity.

Bound each relevant dimension independently.

Potential dimensions include:

- **scope** — what actions may be performed;
- **subject** — who or what may be affected;
- **space** — where capability applies;
- **purpose/function** — why it may be used;
- **duration** — how long it exists;
- **intensity** — how consequential its exercise may be;
- **information access** — what may be observed or retrieved;
- **modification authority** — what may be changed;
- **delegation** — whether capability may be passed onward;
- **persistence** — whether credentials or effects survive the immediate use;
- **escalation** — how capability may increase;
- **revocability** — how it may be withdrawn;
- **reviewability** — how its use may be examined.

Therefore:

> **Minimum Necessary Capability Is Multidimensional.**

A proposal may be sufficient in one dimension while excessive or insufficient in another.

---

## 13. Step 8 — Identify the legitimate basis or bases

Capability may rest on one or several legitimate bases.

Record each claimed basis separately.

Examples may include:

- explicit consent;
- assigned responsibility;
- contract;
- law;
- property;
- role;
- safety obligation;
- emergency necessity;
- delegation.

Do not assume:

> **One Legitimate Basis ≠ Necessarily Sufficient Basis**

Some capabilities may require conjunctive justification: for example role **and** consent, or emergency need **and** proportionality.

If one basis disappears, determine whether another basis independently supports continuation.

---

## 14. Step 9 — Apply protected-interest constraints

Identify applicable:

- rights;
- safety constraints;
- privacy interests;
- property interests;
- autonomy constraints;
- externalities;
- legal or contractual limits;
- protected third-party interests.

MNC does not transform rights into permissions.

> **Right ≠ Permission**

> **Recognition of a Right ≠ Grant of a Privilege**

The portable architecture receives the relevant protected interests from the surrounding legitimate system; it does not generate a complete rights system itself.

---

## 15. Step 10 — Test local and aggregate capability

First test the proposed capability locally:

> **Is this individual capability justified and bounded?**

Then test systemically:

> **What effective capability emerges when it combines with other capabilities?**

Where reasonably feasible, perform this aggregate check **before or at activation** of consequential capability rather than waiting for later review. Inspect known overlapping roles, credentials, delegated access and persistent permissions.

This requirement does not assume omniscience. Unknown or hidden capability remains a review risk.

Consider combinations with:

- other permissions;
- information access;
- enforcement powers;
- infrastructure dependencies;
- prestige or perceived authority;
- delegated agents;
- institutional coordination;
- persistent credentials.

Therefore:

> **Minimum Local Capability ≠ Minimum Systemic Capability.**

Several locally defensible grants may aggregate into excessive systemic power.

---

## 16. Step 11 — Compare formal and effective capability

Where consequence warrants it, compare:

- declared capability;
- legitimately established capability;
- technical capability;
- effective capability;
- observed exercise.

Do not rely only on formal descriptions.

A role may possess little declared authority but substantial effective power through dependency, privileged information, technical control or the predictable deference of others.

Likewise, formally broad authority may be practically unusable.

---

## 17. Step 12 — Establish provenance, accountability and review

The greater the consequence, intrusion, persistence or uncertainty, the stronger the case for proportionate:

- recorded justification;
- evidence preservation;
- decision provenance;
- review;
- accountability;
- contestability;
- expiry;
- independent scrutiny.

Logs, audit trails and other records support provenance and accountability, but they do not create legitimacy by themselves.

> **Logging Capability Exercise ≠ Legitimising Capability Exercise.**

The architecture does not require one universal oversight institution.

It requires review arrangements appropriate to the capability and context.

> **Capability Should Carry Proportionate Accountability.**

---

## 18. Step 13 — Couple responsibility to capability

Check both directions.

### Responsibility without capability

Has an actor been made responsible for an outcome while lacking sufficient control, information, authority, access or resources to influence it?

### Capability without responsibility

Can an actor materially affect others without corresponding responsibility, accountability or review?

Therefore:

> **Responsibility Should Not Be Assigned Where Capability or Control Is Absent.**

and:

> **Consequential Capability Should Carry Commensurate Responsibility for Its Exercise.**

---

## 19. Step 14 — Define activation, escalation and expiry

Record:

- when the capability activates;
- what event or evidence can justify escalation;
- maximum escalation without new authorisation;
- when capability automatically narrows;
- expiry conditions;
- termination conditions;
- re-justification requirements.

Escalation follows:

**Existing Capability**  
→ **New Information / Changed Conditions**  
→ **Additional Need**  
→ **Additional Justification**  
→ **Minimum Additional Capability**

Therefore:

> **Capability Escalation Should Require Additional Justification.**

and:

> **Escalated Capability Should Not Automatically Become Baseline Capability.**

---

## 20. Step 15 — Review continuing need

At review, ask:

1. Does the original legitimate purpose still exist?
2. Is the function still required?
3. Is the current capability still necessary?
4. Is it still sufficient?
5. Has actual capability diverged from declared capability?
6. Have other capabilities accumulated?
7. Have protected interests or externalities changed?
8. Has the actor's responsibility changed?
9. Can the capability now be narrowed?
10. Should it terminate?

> **Past Capability ≠ Present Need**

A previous justification is evidence of previous need, not automatic proof of current need.

---

## 21. Step 16 — Disposition

A review may conclude:

- **Retain**
- **Narrow**
- **Expand with additional justification**
- **Redistribute**
- **Redesign**
- **Suspend**
- **Terminate**
- **Require re-justification**
- **UNKNOWN / DISPUTED pending evidence or legitimate determination**

The architecture should preserve the reasoning behind the disposition.

---

## 22. Capability floor and ceiling model

A useful representation is:

**Insufficient Capability**  
← **Necessary Floor**  
→ **Legitimate Capability Range**  
← **Justified Ceiling**  
→ **Excess Capability**

The exact floor and ceiling are context-dependent.

MNC v0.1 does not provide a universal numeric formula for determining them.

The assessment must instead expose the evidence, assumptions, required standard and uncertainty used to place the bounds.

---

## 23. Exceptional branch — time-critical assumed capability

Ordinary capability should normally be established through the applicable legitimate process.

A time-critical case may arise where:

1. a legitimate function appears to require consequential action;
2. ordinary consent or authorisation is unavailable;
3. obtaining it would take longer than the function safely permits;
4. failure to act risks material harm or functional failure;
5. an actor can take a bounded action;
6. retrospective review is possible.

In such a case, an actor may have to **assume** capability before ordinary prospective authorisation is available.

This is an exceptional branch, not the default MNC pathway.

Apply:

**Urgent Function**  
→ **Ordinary Authorisation Unavailable in Time**  
→ **Minimum Necessary Assumed Capability**  
→ **Action Bounded to Urgent Function**  
→ **Record Basis and Uncertainty**  
→ **Terminate/Narrow When Urgency Ends**  
→ **Independent Retrospective Review**

Preserve:

> **Assumed Authority ≠ Assumed Consent**

> **Incapacity ≠ Erasure of Prior Autonomous Choice**

> **Urgency May Change the Timing of Legitimacy Review; It Does Not Eliminate the Requirement for Legitimacy.**

> **Reduced Prospective Oversight Should Produce Increased Retrospective Accountability.**

Known prior autonomous choices, applicable rights and explicit refusals remain relevant constraints unless the surrounding legitimate system provides an independently adequate basis for override.

---

## 24. Anti-capture and failure-mode checks

### Capability creep
Has capability broadened without new justification?

### Function creep
Has the function itself been broadened to preserve or increase capability?

### Manufactured necessity
Has a capability holder created, preserved or exaggerated conditions that make its own additional capability appear necessary?

### Self-justification
Does the same actor control problem definition, evidence, function definition, capability request, grant and validation?

### Capability bundling
Is a necessary capability packaged with unrelated powers?

### Consent laundering
Is nominal consent being treated as sufficient despite coercion, deception, bundling or lack of meaningful choice?

### Emergency permanence
Has exceptional capability survived the emergency without fresh justification?

### Stale capability
Does capability remain after its legitimate context has ended?

### Hidden capability
Does actual operational access exceed formal descriptions?

### Distributed capture
Do apparently separate capability holders combine into a coordinated or dependency-linked aggregate?

### Externality blindness
Does the formal boundary omit material effects beyond that boundary?

These checks do not prove abuse. They identify conditions requiring closer examination.

---

## 25. Failure states

A portable assessment should distinguish at least:

### MNC-F1 — Under-Capability
Capability is insufficient for the required function.

### MNC-F2 — Over-Capability
Capability exceeds the justified ceiling.

### MNC-F3 — Wrong or Insufficient Basis
Capability exists or is proposed, but its claimed legitimate basis does not adequately support it.

### MNC-F4 — Stale Capability
The original basis or function has ended without corresponding capability reduction.

### MNC-F5 — Aggregate Excess
Local grants appear defensible but combine into excessive systemic capability.

### MNC-F6 — Formal/Effective Divergence
Actual capability materially differs from declared or legitimately established capability.

### MNC-F7 — Unreviewable Capability
Consequential capability lacks proportionate provenance, accountability or review.

### MNC-F8 — Manufactured Necessity / Self-Justification
The justification process is materially distorted by the capability holder or architecture.

### MNC-F9 — Emergency Persistence
Exceptional capability becomes baseline without adequate re-justification.

### MNC-F10 — Responsibility-Capability Mismatch
Responsibility and actual capability/control are materially misaligned.

Multiple failure states may coexist.

---

## 26. Lightweight assessment record

| Field | Record |
|---|---|
| Purpose/problem | What legitimate objective requires action? |
| Legitimate basis | What source establishes legitimacy? |
| Evidence/context | What is known, disputed or unknown? |
| Required function | What must actually be done? |
| Existing capability | What can already perform the function? |
| Alternatives | Are less intrusive/simpler options feasible? |
| Capability need | What additional ability is genuinely required? |
| Necessary floor | Minimum capability that remains sufficient |
| Proposed capability | What is being granted/activated/assumed? |
| Dimensions | Scope, subject, space, duration, intensity, information, delegation, persistence, etc. |
| Justified ceiling | Point beyond which capability lacks support |
| Protected constraints | Rights, harms, externalities, rules |
| Local analysis | Is the individual grant justified? |
| Aggregate analysis | What does it become when combined? |
| Effective capability | What can the actor actually do? |
| Accountability | Responsibility, provenance, review |
| Escalation | What requires additional justification? |
| Expiry | When does capability narrow/end? |
| Disposition | Retain / Narrow / Expand / Redistribute / Redesign / Suspend / Terminate / Re-justify / Unknown |
| Review trigger | What change requires reassessment? |

---

## 27. Success questions

An MNC application should ask:

- Is the objective adequately grounded in an applicable legitimate basis?
- Is the required function defined independently of the desired capability?
- Were existing capabilities and alternatives examined?
- Is additional capability genuinely necessary?
- Is the proposed capability sufficient?
- Is any dimension excessive?
- Are protected rights/interests preserved?
- Are multiple legitimate bases correctly represented?
- Has aggregate capability been examined?
- Does formal capability match effective capability?
- Are responsibility and capability aligned?
- Are escalation and expiry explicit?
- Can the capability holder manufacture its own necessity?
- Is review proportionate to consequence?
- Will capability narrow or terminate when its basis ends?

---

## 28. Relationship to specialised architectures

MNC is a parent architecture that may specialise into narrower domains.

For example:

**MNC → Authority**  
What minimum consequential decision/action capability is justified by a legitimate function?

**MNC → Permission**  
What minimum access or interaction is justified by a legitimate function?

**MNC → Technical access**  
What minimum system/data/tool access is sufficient for the assigned function?

These specialised architectures may require additional domain rules.

MNC does not replace them.

---

## 29. What MNC does not decide

MNC does not by itself determine:

- the complete ethical system;
- the complete rights architecture;
- who holds legitimate sovereignty;
- which law applies;
- factual truth where evidence is unresolved;
- the exact numeric capability floor or ceiling in every domain;
- whether a particular organisation's substantive purpose is legitimate;
- or whether one institutional design is universally superior.

Those inputs or determinations must come from appropriate external systems.

---

## 30. Evidential boundary

This specification is extracted from developed Concord architecture.

The source architecture has undergone substantial internal development and adversarial examination, but this standalone v0.1 package has not yet been independently transfer-tested.

It may currently claim to provide a structured architecture for:

- linking capability to legitimate function;
- testing both under- and over-capability;
- representing capability multidimensionally;
- testing local and aggregate capability;
- distinguishing formal and effective power;
- exposing capability creep and self-justification;
- requiring escalation justification;
- and preserving expiry/re-justification.

It may not yet claim to:

- determine objectively correct capability minima;
- reduce abuse in practice;
- improve institutional performance;
- outperform least-privilege or proportionality frameworks;
- work across all cultures or legal systems;
- or transfer reliably across all non-Concord contexts.

MNC-BTT-001 supplied bounded transfer evidence: a fresh AI instance coherently applied v0.1 to a non-Concord technical-organisational capability-design problem involving under-capability, over-capability, aggregate credentials, temporary escalation and self-justification. The test exposed four narrow clarifications now incorporated into v0.2.

The module completed source-resolution audit, standalone extraction, MNC-BTT-001 blind transfer testing, test-supported revision and portable-package graduation review before this release.

The available evidence supports specification-level standalone portability for the tested AI transfer context. It does not establish human usability, quantitative optimality or real-world effectiveness.

> **Portable graduation ≠ empirical validation.**
