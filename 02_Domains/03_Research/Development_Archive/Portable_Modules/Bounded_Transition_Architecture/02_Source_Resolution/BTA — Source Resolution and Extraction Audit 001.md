# BTA — Source Resolution and Extraction Audit 001

**Candidate:** Bounded Transition Architecture (BTA)
**Project:** The Concord Framework
**Framework Version:** Concord V1.3
**PMEDG Level:** Level B — Extractable Architecture
**Status:** FORMAL PMEDG SOURCE RESOLUTION AND EXTRACTION AUDIT / NON-CANONICAL
**Date:** September 2026

# 1. Purpose

This audit begins formal PMEDG extraction of BTA as a candidate portable module.

It determines the resolved source architecture, portable problem, smallest surviving kernel, Concord-specific dependencies, overlap boundaries, external interfaces, failure modes and extraction decision.

# 2. Hard preservation constraint

Portable extraction must not remove, replace, supersede, merge away or transfer ownership from any existing Concord system.

> **Portable Abstraction != Concord Architectural Replacement.**

> **Genericising an Interface Does Not Genericise Away Its Concord Owner.**

> **BTA Is an Added Interoperability Layer, Not a Successor Architecture.**

The portable module may describe a Concord owner through a generic interface when operating outside Concord. Inside Concord, the original named system remains the legitimate owner.

No existing system is deprecated by this extraction.

# 3. Resolved source set

Primary BTA development sources include:

- `Bounded Transition Architecture — Existing Concord Source Resolution 001.md`;
- `Bounded Transition Architecture 001 — Consequential State-Change Integration Grammar.md`;
- BTA Adversarial Tests 001–004;
- `BTA Adversarial Tests 001-004 — Synthesis and Refinement Decision.md`;
- `Bounded Transition Architecture — Existing Concord Source Resolution 002.md`;
- `Bounded Transition Architecture — Existing Concord Source Resolution 003 — State Machines, Handover and Partial Transition.md`;
- `BTA Cross-Domain Generalisation Test 001 — State-Machine Interoperability Kernel.md` where present in the development record;
- `Bounded Transition Architecture 002 — Consequential Transition Coherence and Interoperability Grammar.md`;
- `BTA Clean Cross-Domain Test 002 — Constitutional Emergency State Transitions.md`;
- BTA Machine-Readable Transfer Test 003 brief, hidden reference key and blind-audit comparison;
- `BTA Interface-Boundary Audit 004 — Owner-System Non-Absorption Review.md`;
- `BTA Materiality and Proportionality Test 005 — Minimum Sufficient Transition Representation.md`;
- `BTA PMEDG Candidacy Assessment 001.md`.

Material neighbouring Concord sources include:

- Civil State Handover Protocol;
- KCS Change Propagation;
- State Triggered Review Architecture;
- Cross Boundary Externality Recognition;
- Civilisation Clock / consequence-relevant state-transition architecture;
- Fractal Permission Architecture and bounded authority architecture;
- Continuity Protocol;
- Historical domain architecture;
- Infrastructure lifecycle/successor-transition architecture;
- enterprise wind-down/resource-stewardship development;
- genomic/data-purpose transition material;
- Constitutional Emergency architecture.

# 4. Source architecture before portability abstraction

BTA emerged from a recurring Concord problem: independently valid systems can represent different dimensions of the same consequential change, yet no single existing owner necessarily binds those states into one coherent bounded transition.

Examples include:

- an object moves but its authority does not;
- service operation changes before responsibility handoff completes;
- physical crossing occurs before validation;
- authority terminates while duties survive;
- a failed transition leaves residual state;
- rollback occurs without restoring the prior world state;
- one subsystem declares completion while another remains legitimately pending;
- an externality or dependency review remains open after an internal state change;
- Historical provenance must survive without reactivating expired authority.

Source resolution repeatedly showed that the missing function was **not** another authority system, state machine, dependency engine, validator, externality detector, recovery architecture or Historical system.

The residual function was transition coherence across them.

# 5. Portable problem

The Concord-independent problem is:

> **How can independently owned systems coordinate one consequential transition when different state dimensions may change asynchronously, without allowing completion, authority, permission, responsibility, validation, recovery or other consequential state in one dimension to be silently inferred in another?**

This problem is not inherently Concord-specific.

# 6. Candidate portable kernel

The smallest kernel surviving source resolution and testing is:

1. **Bounded transition identity and scope** — identify the consequential transition being integrated.
2. **Independent state ownership** — participating systems retain ownership of their own substantive state and semantics.
3. **Scoped multidimensional state references** — bind relevant prior/current/next states without flattening them.
4. **Asynchronous transition state** — dimensions may be complete, pending, partial, failed or unresolved independently.
5. **Owner-supplied completion conditions** — integrated completion cannot be inferred from one dimension.
6. **Non-propagation rules** — consequential attributes do not silently transfer merely because an object/function crosses a boundary.
7. **Pending/unresolved-state preservation** — incomplete transition does not manufacture completion or authority.
8. **Surviving-duty / terminated-authority separation** where material.
9. **External interface references** for validation, dependencies, externalities, authority, recovery, temporal relations and provenance where material.
10. **Failed/partial-transition provenance and residual effects** where material.
11. **Minimum sufficient representation** proportional to consequence.
12. **Owner-system non-absorption** — integration never becomes sovereignty.
13. **Evaluation-space boundary** — correct representation does not prove all material dimensions were represented.

# 7. Non-removal and non-replacement map

The following mapping is normative for Concord integration.

| Existing Concord owner | Existing function retained | Portable generic interface | Extraction effect inside Concord |
|---|---|---|---|
| Civil State Handover Protocol | specialised civil handover, Transition Epoch, Pending-State Capsule, Handover Witness, Recovery Anchor, Transition Hold | specialised handover-state interface | **RETAINED UNCHANGED; BTA REFERENCES IT** |
| KCS Change Propagation | dependency representation and downstream propagation/review | dependency/change-propagation interface | **RETAINED UNCHANGED; BTA REFERENCES IT** |
| State Triggered Review Architecture | trigger/review/condition semantics | validation/review/trigger interface | **RETAINED UNCHANGED; BTA REFERENCES IT** |
| Cross Boundary Externality Recognition | external consequence, affected party, materiality, causal/responsibility routing | external-consequence interface | **RETAINED UNCHANGED; BTA REFERENCES IT** |
| Civilisation Clock / CRSTL | temporal/relational ordering among transitions | transition-relation/time interface | **RETAINED UNCHANGED; BTA REFERENCES IT** |
| FPA / bounded authority architecture | permission and authority legitimacy/state | permission/authority interface | **RETAINED UNCHANGED; BTA REFERENCES IT** |
| Continuity Protocol | continuity object, recovery basis/path, restoration/succession verification | recovery/continuity interface | **RETAINED UNCHANGED; BTA REFERENCES IT** |
| Historical | provenance custody, historical state, reconstruction and long-term context | provenance/history interface | **RETAINED UNCHANGED; BTA REFERENCES IT** |
| Domain-specific state machines | substantive domain transition/state semantics | domain-state interface | **RETAINED UNCHANGED; BTA REFERENCES THEM** |

> **No generic portable interface authorises deletion or consolidation of its Concord counterpart.**

# 8. Dependency classification

## Civil State Handover Protocol

Classification: **already-owned specialised architecture / external interface**.

BTA may reuse general lessons but must not absorb civil handover semantics.

## KCS

Classification: **already-owned portable architecture / external interface**.

Dependency propagation remains external.

## STRA

Classification: **already-owned portable architecture / external interface**.

Trigger, review and validation semantics remain external.

## CBER

Classification: **already-owned portable architecture / external interface**.

Affected-party and externality analysis remain external.

## Clock / CRSTL

Classification: **Concord cross-domain architecture / generic temporal-relation interface**.

Transition ordering remains external.

## FPA / authority architecture

Classification: **already-owned authority/permission architecture / generic authority interface**.

Legitimacy and permission remain external.

## Continuity

Classification: **already-owned portable architecture / recovery interface**.

Recovery sufficiency and restoration remain external.

## Historical

Classification: **Concord domain architecture / provenance-history interface**.

Long-term custody and reconstruction remain external.

## Domain-specific state machines

Classification: **host-owned state semantics / generic state-owner interface**.

BTA standardises only the interoperability boundary.

# 9. What is removed from the portable specification

Only **Concord-specific naming and assumed availability** are removed from the standalone portable specification.

The underlying functions are not removed from Concord.

For example:

`KCS` becomes `DependencyPropagationOwner` in the portable specification.

This means:

- outside Concord, a host may supply its own dependency system;
- inside Concord, KCS remains the concrete owner;
- BTA does not implement dependency propagation.

The same rule applies to all genericised interfaces.

# 10. What must not be abstracted away

The following boundaries are part of the portable mechanism itself and must survive abstraction:

- state ownership remains external;
- authority remains external;
- validation remains external;
- dependency propagation remains external;
- externality analysis remains external;
- recovery sufficiency remains external;
- temporal relation semantics remain external;
- provenance/history custody remains external;
- BTA cannot manufacture completion from local state;
- BTA cannot manufacture authority from transition need;
- BTA cannot treat object continuity as attribute transfer;
- BTA cannot treat rollback as proven restoration;
- BTA cannot claim evaluation-space completeness.

# 11. Candidate portable inputs

A host implementation may supply, where material:

- transition object/function reference;
- scope;
- participating owner-system references;
- prior/current/next state references;
- transition basis reference;
- pending/unresolved state;
- completion-condition references;
- non-propagation constraints;
- validation/review references;
- dependency references;
- external-consequence references;
- authority/permission references;
- recovery references;
- temporal-relation references;
- provenance/history references.

Not every transition requires every input.

# 12. Candidate portable outputs

BTA should output a coherent bounded-transition representation containing only materially applicable fields and preserving:

- transition identity;
- scoped state relationship;
- integrated completion status within declared scope;
- pending/partial/failed/unresolved dimensions;
- prohibited propagation;
- surviving duties/terminated authority where supplied;
- external owner actions still required;
- recovery position where supplied;
- provenance;
- uncertainty.

BTA output is representational. It is not substantive authority.

# 13. Candidate generic owner interface

A portable host may expose owner state through a generic structure such as:

`OwnerStateRef = <OwnerRef, StateRef, Scope, State, EvidenceOrBasisRef, Uncertainty, Provenance>`

This is an interoperability envelope only.

The owner retains the meaning of `State`, its legitimacy and its decision procedure.

# 14. Candidate transition contract

A portable BTA contract may retain the BTA 002 structure while replacing Concord-specific names with generic interfaces:

`BoundedTransition = <TransitionID, ObjectOrFunctionRefs, Scope, TransitionClass, ParticipatingOwnerRefs, PriorValidStateRefs, TransitionBasisRefs, TransitionPhaseRefs, TransitionStateRefs, PendingStateRefs, CompletionConditionRefs, ProtectedUnresolvedStateRefs, NonPropagationRules, ValidationRefs, RelationalEffectRefs, ExternalConsequenceRefs, SurvivingDutyRefs, SurvivingValueRefs, TerminatedAuthorityRefs, ReleasedResourceRefs, DependencyRefs, TemporalRelationRefs, RecoveryRefs, NextStateRefs, ReversibilityState, UncertaintyOrDisputeState, Provenance>`

Fields remain materially optional.

# 15. Overlap boundary

BTA is not:

- a state machine for every domain;
- a workflow engine;
- an authority system;
- a permission system;
- a validator;
- an externality detector;
- a dependency graph;
- a scheduler;
- a continuity/recovery system;
- a Historical archive;
- an adjudicator;
- a universal transaction database.

BTA is the integration grammar binding references from those functions where one consequential transition crosses them.

# 16. Failure modes

Portable extraction must preserve at least:

- premature integrated completion;
- state flattening;
- authority inheritance;
- consent/purpose inheritance;
- stale permission;
- orphaned duty;
- hidden partial crossing;
- false rollback;
- relation loss;
- externality blindness;
- dependency omission;
- owner-system absorption;
- universal logging / bureaucracy;
- materiality laundering;
- uncertainty collapse;
- schema inflation;
- evaluation-space overclaim.

# 17. Epistemic boundary

> **Correct Representation Within the Transition Schema != Demonstrated Completeness of the Transition Schema.**

> **Small Represented Transition != Demonstrated Small Real Consequence.**

A portable BTA implementation must preserve a mechanism for uncertainty and host-owned escalation/review without converting unknown dimensions into assumed failure or assumed safety.

# 18. Implementation minimum

A minimal portable implementation requires:

1. stable TransitionID;
2. declared scope;
3. at least one externally owned state reference;
4. prior/current/next transition representation sufficient for the material case;
5. owner-supplied completion condition or explicit completion basis where completion matters;
6. provenance;
7. ability to add materially relevant interfaces without changing the core grammar.

If no consequential dimension crosses the materiality gate, no BTA object is required.

# 19. Extraction risks

## Generic-state-machine collapse

If BTA is reduced to generic state transitions without ownership, non-propagation and cross-system coherence, the portable mechanism has been lost.

## Concord-owner erasure

If generic interface names are interpreted as replacements for Concord systems, extraction has failed.

## Interface absorption

If BTA starts implementing dependency, authority, validation, recovery or externality semantics, extraction has failed.

## Mandatory-schema inflation

If every host must populate every field, proportionality has been lost.

## Weak-host ambiguity

A host lacking legitimate owner systems may expose state references without trustworthy semantics. BTA cannot repair that by becoming the missing owner.

# 20. Source-resolution sufficiency

The development record has repeatedly expanded the source space when apparent BTA gaps were discovered. This process removed duplicate ownership rather than hiding it.

No current evidence indicates that another existing Concord system already owns the remaining cross-system transition-coherence function in full.

Existing specialised transition architectures cover parts of the problem but do not replace the generic integration residue.

# 21. Extraction decision

**SOURCE RESOLUTION SUFFICIENT FOR PORTABLE EXTRACTION.**

**PMEDG DECISION: PROCEED TO PORTABLE SPECIFICATION v0.1.**

Conditions:

1. every existing Concord owner remains intact;
2. portable generic interfaces must map back explicitly to Concord owners;
3. BTA must remain representational/integrative rather than substantive;
4. non-material interfaces remain optional;
5. authority, validation, dependencies, externalities, recovery and Historical semantics remain externally owned;
6. provenance must record BTA's derivation from Concord rather than presenting it as source-free abstraction.

# 22. Next artifact

Create:

> **Bounded Transition Architecture — Portable Specification v0.1**

The specification should be readable without knowledge of Concord while retaining a provenance/interface appendix showing how generic portable interfaces map back to the unchanged Concord systems.