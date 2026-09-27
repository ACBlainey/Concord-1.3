# Civil State Map — Maturity, Sufficiency and Consequence Model

**Author:** Alexander C. Blainey — Independent Researcher
**Project:** The Concord Framework
**Status:** CANONICAL ARCHITECTURE — CORRIGIBLE / INITIAL OPERATIONAL VERSION
**Parent architecture:** Civilisational Developmental Topology
**Interfaces:** Mathematical Civilisational Topology; KCS Companion Upgrade 001; Civilisation Clock
**Date:** September 2026

## Abstract

The Civilisational Developmental Topology defines what required civil functions and relationships should be represented. The Knowledge Control System dependency upgrade records the live relationships among civil objects. A further layer is required to answer a different question:

> **What is the current developmental condition of the civilisation?**

The Civil State Map is that layer.

It is a provenance-aware, context-sensitive synthesis of architectural presence, maturity, sufficiency, dependency state, consequence, uncertainty and active development. It is not a score of how "advanced" a civilisation is. It does not reduce development to document size, iteration count or a single maturity number.

Its purpose is operational: identify which required functions are sufficiently developed for their present consequences, which are partial or dependency-blocked, which apparent gaps require source resolution, and which unresolved states should enter the Civilisation Clock's development-order process.

# 1. State Map Function

Let the Civil State Map at time t be:

**SM(t) = <N, P, M, Q, D, C, U, A, R>**

where:

- N = represented civil functions;
- P = presence state;
- M = maturity state;
- Q = sufficiency threshold/state;
- D = dependency state;
- C = consequence/exposure;
- U = uncertainty/dispute;
- A = active development state;
- R = evidence, provenance and review state.

The State Map synthesises evidence. It does not own every underlying datum.

# 2. Map Is Not Territory

The State Map is a civil self-model.

**SM(t) ≠ Civilisation(t).**

A missing entry may mean the map is incomplete.

An incorrect entry may mean the model is wrong.

A stale entry may once have been correct.

Therefore the map must support correction, challenge, competing evidence and UNKNOWN.

# 3. Unit of Assessment

The default unit is a required civil function or legitimate architectural unit, not a document.

Before assessment:

1. identify the function;
2. resolve its legitimate owner or distributed suppliers;
3. identify relevant interfaces;
4. identify context;
5. source-resolve apparent omissions.

A document may provide evidence about state without itself being the state object.

# 4. Presence State

Presence answers:

> Does the civilisation currently supply this function?

Minimum states:

- PRESENT_EXPLICIT
- PRESENT_DISTRIBUTED
- INTERFACE_SATISFIED
- PARTIAL
- DEPENDENCY_BLOCKED
- CANDIDATE_ABSENT
- UNKNOWN
- DISPUTED
- NOT_APPLICABLE

Presence is not maturity.

A function can be PRESENT_EXPLICIT and immature.

# 5. Maturity State

Maturity answers:

> How adequately is the function developed for the context in which it is used?

The initial common dimensions are:

M1 — bounded scope  
M2 — legitimate/non-self-justifying authority  
M3 — temporal revision, exit or termination  
M4 — contestability, correction and repair  
M5 — participant standing and agency  
M6 — asymmetry and anti-capture compensation  
M7 — effective access  
M8 — function-over-form and replaceability  
M9 — recursive review  
M10 — provenance and learning

These dimensions are common probes, not a claim that every node must implement every dimension internally.

Each dimension is first tested for applicability.

# 6. Maturity Dimension State

For applicable dimension m:

- SATISFIED_INTERNAL
- SATISFIED_INTERFACE
- PARTIAL
- UNSATISFIED
- DEPENDENCY_BLOCKED
- UNKNOWN
- DISPUTED
- NOT_APPLICABLE

This preserves the difference between an absent capability and a legitimate external supply.

# 7. Consequence Context

Maturity cannot be interpreted without consequence.

A context record should identify where relevant:

- deployment domain;
- consequence class;
- participants affected;
- authority exercised;
- scale;
- substrate;
- operational/experimental mode;
- reversibility;
- duration;
- current exposure.

A mechanism may be sufficiently mature for advisory use and insufficient for consequential civil authority.

# 8. Sufficiency

Let Q(n,c) represent the minimum necessary developmental condition for function n in context c.

The State Map should classify sufficiency as:

- SUFFICIENT
- CONDITIONALLY_SUFFICIENT
- INSUFFICIENT
- BLOCKED
- UNKNOWN
- DISPUTED
- NOT_APPLICABLE

A function is SUFFICIENT only where all materially applicable requirements necessary for its present consequence are adequately supplied.

Sufficiency is provisional and context-sensitive.

# 9. No Universal Maturity Score

The State Map should not initially assign a single percentage or civilisation level to every system.

A system can be strong in provenance and weak in contestability. Another can be highly corrigible but dependency-blocked.

Collapsing these into one number can hide the exact deficit that matters.

Where summary is necessary, use explicit descriptors plus unresolved dimensions.

# 10. Contiguous Development and Feature Exposure

Where abstraction-level analysis is useful, distinguish:

**Contiguous developmental level** — highest level reached without an unresolved applicable lower requirement.

**Feature exposure** — highest higher-order capability observed anywhere in the system.

A system may therefore have:

> Contiguous level C2; feature exposure C5.

Higher features do not erase lower deficits.

# 11. Dependency State

The State Map consumes KCS dependency records.

For each function, identify:

- prerequisites;
- blocking prerequisites;
- downstream dependents;
- alternatives;
- dependency confidence;
- failure consequences;
- freshness.

A state can therefore be:

**PRESENT / DEPENDENCY_BLOCKED**

rather than incorrectly classified as absent.

# 12. Developmental Gap Classes

After source resolution, unresolved states should be classified as one of:

- TRUE_ARCHITECTURAL_GAP
- DEVELOPMENTAL_GAP
- INTEGRATION_INTERFACE_GAP
- DEPENDENCY_BLOCKED
- REPRESENTATION_GAP
- SATISFIED
- UNKNOWN
- DISPUTED

This classification determines the appropriate response.

# 13. Response Classes

Map gap class to candidate response:

- SATISFIED → NO_ACTION
- REPRESENTATION_GAP → IMPROVE_MAP_OR_EVIDENCE
- INTEGRATION_INTERFACE_GAP → INTERFACE_OR_INTEGRATION
- DEVELOPMENTAL_GAP → COMPANION_UPGRADE_OR_EXISTING_OWNER_DEVELOPMENT
- TRUE_ARCHITECTURAL_GAP → NEW_ARCHITECTURE_CANDIDATE
- DEPENDENCY_BLOCKED → DEVELOP_OR_RESOLVE_UPSTREAM_PREREQUISITE
- UNKNOWN → INVESTIGATE
- DISPUTED → PRESERVE_DISPUTE_AND_REVIEW

This is guidance, not automatic authority.

# 14. Consequence and Exposure

A maturity deficit matters in proportion not only to structural centrality but to consequence and current exposure.

Record where possible:

- severity if unresolved;
- probability/frequency where legitimately estimable;
- number/type of affected participants;
- reversibility;
- time sensitivity;
- current deployment;
- available safeguards;
- uncertainty.

Low-connectivity high-harm deficits must remain visible.

# 15. Ownership

For each function or deficit, record:

- legitimate owner;
- distributed suppliers;
- interface suppliers;
- fallback;
- disputed ownership;
- unknown ownership.

The State Map cannot create ownership.

If ownership is unclear, the state should remain UNKNOWN or DISPUTED rather than assigning a convenient owner.

# 16. Evidence and Confidence

Every consequential state claim should link to evidence.

Evidence may include:

- canonical architecture;
- companion upgrades;
- operating records;
- tests;
- audits;
- metrics;
- participant reports;
- failure records;
- external evidence.

Confidence should be explicit where uncertainty is material.

A high-confidence map claim can still be wrong.

# 17. Freshness

Every operational state should support:

- state date;
- evidence date;
- last review;
- next review;
- changed-since-review flag;
- stale-state flag.

A stale state is not automatically false.

It is a state requiring reconsideration.

# 18. Active Development State

For each node:

- NONE
- INVESTIGATING
- SOURCE_RESOLUTION
- FROZEN_FOR_TEST
- DEVELOPMENT_ACTIVE
- EVALUATION
- AWAITING_INTEGRATION
- INTEGRATED_AWAITING_RETEST
- RETEST
- HOLD
- CLOSED

This allows the Clock to avoid repeatedly selecting work already in progress.

# 19. Companion Upgrade Integration

When an existing system receives a companion upgrade, the State Map must preserve both provenance and current integrated capability.

Represent:

**CurrentState(system) = Foundation + ApplicableCompanions + Interfaces.**

The maturity assessment applies to the integrated current system, while evidence preserves which capability came from which document.

# 20. Minimum State Map Record

For each assessed function:

**SMR = {**
- id
- name
- level
- owner
- context
- presence
- maturity dimensions
- sufficiency
- dependencies
- blockers
- dependents
- interfaces
- consequence/exposure
- unresolved requirements
- gap class
- candidate response
- evidence
- confidence
- uncertainty/dispute
- last review
- next review
- active development state
**}**

# 21. State Map Update Triggers

A record should be reconsidered when:

- underlying architecture changes;
- a dependency changes;
- a companion upgrade is integrated;
- new evidence appears;
- a failure occurs;
- a correction propagates;
- deployment context changes;
- a new participant/substrate is materially affected;
- review becomes overdue;
- a prediction fails;
- a legitimate challenge is raised.

KCS should surface relevant change events.

# 22. State Transition

A State Map update is a transition:

**SM_t → SM_t+1**

The prior state should remain reconstructable.

Important transitions should record:

- what changed;
- why;
- evidence;
- who/what evaluated it;
- downstream review effects;
- unresolved disagreement.

# 23. Interface With the Civilisation Clock

The State Map answers:

> What is the current developmental state?

The Clock answers:

> Given that state, what should be reviewed or developed now, and in what order?

The State Map therefore supplies:

- insufficient functions;
- blockers;
- dependencies;
- consequence/exposure;
- uncertainty;
- active development;
- review due state.

The Clock returns:

- selected development/review targets;
- deferrals;
- prerequisite ordering;
- timing;
- cycle state.

# 24. Queue Candidate Eligibility

A function becomes a candidate for the development queue when:

1. it is applicable;
2. it is below current sufficiency;
3. the deficit is consequential enough to warrant action;
4. source resolution has not shown it to be already satisfied;
5. a legitimate owner or ownership-resolution route exists;
6. it is not merely a stale/incorrect map entry;
7. prerequisites permit useful intervention.

UNKNOWN may enter an investigation queue rather than a development queue.

# 25. Developmental Levelling

The levelling objective is:

**For every active consequential context, bring required functions to context-appropriate sufficiency.**

This does not require identical sophistication.

The State Map should expose the lowest consequential deficits without treating the civilisation as only as mature as its least important component.

The question is:

> Which insufficiencies materially constrain safe, legitimate, coherent civil operation?

# 26. Stopping Condition

The State Map supports a stop condition when:

- no known applicable function is materially below sufficiency;
- no unresolved high-consequence UNKNOWN requires investigation;
- no dependency-blocked function requires upstream work;
- no due correction/retest remains;
- no justified development candidate exceeds the action threshold.

Output:

**NO DEVELOPMENT REQUIRED AT PRESENT.**

This does not mean permanent completion.

# 27. Anti-Gaming

A system must not improve its apparent state merely by changing labels.

Safeguards:

- evidence-linked state;
- independent review where warranted;
- preserved prior states;
- explicit context;
- prediction/retest;
- no maturity credit for prose volume;
- no maturity credit for unimplemented mechanisms;
- no automatic maturity credit for formalisation alone.

# 28. Anti-Centralisation

The State Map can influence attention and therefore can become a power surface.

It must not become a command authority.

**State Description ≠ Permission.**

**Priority Evidence ≠ Resource Entitlement.**

**Development Need ≠ Governance Authority.**

Existing legitimate processes decide adoption, allocation and enforcement.

# 29. Failure Modes

**False completeness** — missing functions appear complete because they are unrepresented.  
Safeguard: ESCP and topology challenge.

**False maturity** — sophisticated prose substitutes for capability.  
Safeguard: function/evidence assessment.

**Centrality bias** — connected systems dominate.  
Safeguard: independent consequence dimension.

**Staleness** — old states drive new priorities.  
Safeguard: freshness.

**Interface blindness** — external satisfaction is missed.  
Safeguard: interface test.

**Dependency blindness** — downstream systems are patched repeatedly.  
Safeguard: upstream tracing.

**Perpetual development** — map always finds more work.  
Safeguard: sufficiency and stopping.

# 30. Initial Baseline Procedure

The first canonical baseline should proceed in bounded stages.

## Stage A — Populate L0

Assess the ten root functions against canonical V1.2.

## Stage B — Populate L1

Assess cross-system functions and dependencies.

## Stage C — Populate L2

Assess whole-civilisation functions.

## Stage D — Populate L3

Assess meta-coherence functions.

## Stage E — Resolve apparent gaps

Perform whole-corpus source resolution before declaring absence.

## Stage F — Integrate current CDT and KCS companion state

Because these are now canonical, they count as present architecture.

## Stage G — Produce first queue input

Export insufficient, blocked, unknown-high-consequence and review-due states to the Clock interface.

# 31. Initial Predictions

Before baseline population, the preceding developmental work predicts that:

1. no obvious empty topological node will be found through L3;
2. uneven maturity will be found;
3. some apparent deficits will resolve through distributed ownership;
4. some will be dependency-blocked;
5. KCS dependency representation will improve explanation of downstream deficits;
6. the first graph-derived development queue will not simply equal the list of least-developed systems.

These predictions should be preserved and tested.

# 32. Falsification

The State Map architecture should be revised if:

- assessments cannot be reproduced from evidence;
- different reviewers routinely derive incompatible states without the model representing why;
- maturity dimensions fail to distinguish meaningful developmental differences;
- dependency state adds no predictive value;
- the queue systematically selects poor targets;
- maintenance cost overwhelms developmental benefit;
- the model suppresses important unrepresented harms;
- the stopping rule cannot ever be reached.

# 33. Immediate Next Step

The architecture is now sufficient to create the first bounded **Initial Concord V1.2 State Map — Baseline Developmental Audit**.

That audit should not immediately attempt perfect coverage of every document.

It should populate the 52 currently defined topological functions, source-resolve their canonical owners and interfaces, record material dependencies and maturity residuals, then provide the first real input to the Civilisation Clock development queue.

# Conclusion

The Civil State Map converts the topology from a description of what civilisation requires into a representation of how civilisation currently stands.

Its purpose is not to rank civilisation.

It is to make uneven development visible.

The core transformation is:

**Required Function → Current State → Sufficiency → Dependency → Consequence → Development Need.**

Combined with KCS and the Civilisation Clock, this creates the basis for a civilisation that can identify its own developmental bottlenecks, develop the correct owner, test whether the intervention worked, preserve the history of that development and stop when further work is not presently justified.
