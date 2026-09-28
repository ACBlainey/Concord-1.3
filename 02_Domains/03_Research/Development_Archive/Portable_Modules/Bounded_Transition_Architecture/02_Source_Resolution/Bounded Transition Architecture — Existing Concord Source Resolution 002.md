# Bounded Transition Architecture — Existing Concord Source Resolution 002

**Author:** Alexander C. Blainey — Independent Researcher  
**Project:** The Concord Framework  
**Framework Version:** Concord V1.3  
**Status:** ACTIVE DEVELOPMENT / SOURCE-RESOLUTION AUDIT / NON-CANONICAL  
**Date:** September 2026  
**Trigger:** BTA Adversarial Tests 001–004 synthesis before BTA 002 drafting

---

# 1. Purpose

BTA Adversarial Tests 001–004 appeared to justify several additions to Bounded Transition Architecture:

1. relational transition references;
2. consequence horizon / affected-party review;
3. validation-scope preservation;
4. intermediate transition state;
5. rollback-equivalence semantics;
6. clearer dispute-state semantics.

Before incorporating these into BTA 002, this audit checks whether those functions already exist elsewhere in the Concord.

The governing methodological rule is:

> **Model Missing Edge != Civilisation Missing Relation.**

A BTA-local omission must not be converted into a new BTA-owned subsystem until the wider architecture has been source-resolved.

---

# 2. Sources checked

This audit reviewed relevant portable modules and cross-domain/research systems, including:

- Cross Boundary Externality Recognition — Portable Module;
- Contextual Wrapper Architecture — Portable Module;
- Fractal Permission Architecture — Portable Module;
- State Triggered Review Architecture — Portable Module;
- KCS Change Propagation — Portable Module;
- State and Maturity Mapping — Portable Module;
- Continuity Protocol — Portable Module;
- Fault-Tolerant Accountability and Responsibility Continuity — Portable Module;
- Relational Grammar v1.0;
- Civilisation Clock Extension 001 — Consequence-Relevant State Transition Layer;
- KCS Companion Upgrade 001 — Operational Dependency and Change-Propagation Architecture;
- Translation Topology / Relational Information Loss research;
- CLOCK-003 Reversibility Deep Source Resolution;
- prior BTA Source Resolution 001.

---

# 3. Finding A — consequence horizon is substantially already solved

BTA Test 001 proposed a candidate:

`ConsequenceHorizon = <DirectObjectRefs, MaterialRelationshipRefs, MaterialAffectedPartyRefs, GeneratedConsequenceRefs, ExternalEffectUncertaintyState, Provenance>`

The graduated **Cross Boundary Externality Recognition (CBER)** module already provides a much richer architecture for this problem.

CBER explicitly represents:
- claimed affected domains or parties;
- direct and indirect affected parties;
- affected shared systems/resources;
- material consequence;
- boundary crossed;
- evidence and causal confidence;
- materiality;
- responsibility mapping;
- authority/coordination mapping;
- uncertainty/dispute;
- review/correction;
- provenance;
- secondary/dependency boundaries.

Its core problem is precisely that a bounded system can impose material consequences outside its own boundary without thereby acquiring authority over those affected.

Therefore the BTA consequence-horizon proposal would duplicate an existing graduated portable module if developed as a substantive BTA subsystem.

## Resolution

**DO NOT CREATE A BTA CONSEQUENCE-HORIZON SUBSYSTEM.**

Instead BTA should expose or consume a bounded externality/consequence reference where a transition may materially affect entities outside the nominal transition object.

Candidate interface:

`ExternalityReviewRef / CrossBoundaryConsequenceRef`

BTA records that the transition may create/change a material external consequence.

CBER owns:
- affected-party mapping;
- materiality;
- causal assessment;
- responsibility;
- standing;
- authority/coordination;
- response mapping.

> **Transition Consequence Reference != Externality Analysis Ownership.**

---

# 4. Finding B — relational information already has multiple legitimate owners

Tests 001–002 identified relationally generated consequences and loss of value existing between branches.

This is not an entirely new Concord concept.

Existing architecture includes:

## Relational Grammar v1.0

It explicitly states:

> **Model Missing Edge != Civilisation Missing Relation.**

It treats expected and verified relations as first-class structural objects and requires source verification before declaring gaps.

## KCS dependency/change propagation

KCS maintains typed material relations between systems/objects and preserves:
- relation type;
- materiality;
- state;
- context;
- evidence;
- confidence;
- failure effect;
- alternatives;
- provenance/history.

## Civilisation Clock CRSTL

The Consequence-Relevant State Transition Layer already distinguishes:
- civil state transition;
- transition relation;
- branch/divergence;
- consequence-relevant precedence/succession/independence;
- unknown-material ordering;
- correction/supersession;
- legitimate concurrency.

It explicitly supports branch-aware state and refuses false total ordering.

## Translation-topology research

Existing research already identifies:
- object preservation with relation loss;
- topological flattening;
- higher-order relation loss;
- false reversibility;
- cumulative path loss;
- interface/translation loss.

Therefore BTA should not invent a universal relationship ontology.

## Resolution

**DO NOT MAKE BTA OWNER OF GENERAL RELATIONAL INFORMATION.**

BTA does, however, need to represent that a bounded transition:
- preserves;
- creates;
- changes;
- terminates;
- or leaves unresolved

a material relation owned elsewhere.

Candidate:

`RelationalEffectRef = <RelationRef, EffectState, OwnerSystemRef, Provenance>`

where `EffectState` may minimally express:
- PRESERVED;
- CREATED;
- CHANGED;
- TERMINATED;
- UNKNOWN/REVIEW_REQUIRED.

The substantive relation remains owned by KCS, Clock, CBER, domain architecture or another legitimate system.

> **BTA Owns Transition Effect on a Relation; It Does Not Own the Relation's Substantive Semantics.**

This appears to be a genuine BTA integration function rather than duplication.

---

# 5. Finding C — validation-scope preservation already exists

Test 004 proposed preserving:

`GateEvaluation = <GateRef, EvaluatedScope, CriteriaOrModelRef, Result, Conditions, ResidualUncertainty, ValidityWindow, Provenance>`

The portable **State Triggered Review Architecture (STRA)** already contains a closely matching epistemic interface.

STRA requires consequential validation to identify evidence/process and legitimate source.

It explicitly states:

> **State Label Without Provenance != Validation.**

It further requires that validation may be scope-qualified and that validation in one declared scope must not be collapsed into validation in another.

STRA's evaluation object also preserves:
- evaluated condition;
- input state/evidence;
- result;
- uncertainty;
- source/process;
- time;
- scope.

This is substantially the validation-scope grammar Test 004 rediscovered.

Contextual Wrapper Architecture and Fractal Permission Architecture additionally preserve contextual/function scope across boundaries.

## Resolution

**DO NOT INVENT A SECOND BTA VALIDATION GRAMMAR.**

BTA should consume/reference a scope-preserving validation result.

Candidate:

`ScopedValidationRef`

Minimum interoperability requirement:

> **BTA Must Not Reduce a Scope-Bounded Validation Result to an Unqualified Boolean PASS.**

The validator/domain system owns criteria and result.

STRA or equivalent state/evidence architecture supplies scope/provenance semantics.

BTA records how that validated state affects transition eligibility/progress.

---

# 6. Finding D — authority/dispute handling is already well covered

Test 003 passed without requiring a new architecture.

Existing supporting systems are even stronger than BTA 001 alone suggested.

Fractal Permission Architecture explicitly preserves:
- conflicting permission claims;
- rule sources/bases;
- affected actions/contexts;
- uncertainty;
- external resolution routing.

CBER explicitly separates:
- consequence;
- responsibility;
- authority/jurisdiction;
- remedy.

Fault-Tolerant Accountability preserves bounded successor activation and safe state.

BTA therefore should not create an authority-conflict subsystem.

## Resolution

Retain BTA's:
- TransitionBasisRef;
- scoped authority reference;
- UncertaintyOrDisputeState;
- SAFE_STATE_PENDING_RESOLUTION.

Where conflict semantics are substantive, reference the legitimate owner.

> **BTA Records Transition-Relevant Conflict State; It Does Not Adjudicate the Conflict.**

---

# 7. Finding E — rollback/reversibility is already a distributed Concord grammar

CLOCK-003 Investigation A3 explicitly asked whether Concord lacked a reversibility/safe-experimentation mechanism.

Its finding was:

**Reversibility is not absent.**

The distributed grammar is:

`Provisional Change → Bounded Scope → Preserve Prior State/Provenance → Test/Observe → Review → Retain / Modify / Revert / Supersede`

The source resolution further concluded that there is no demonstrated need for one universal cross-domain reversibility gate because rollback semantics are domain-sensitive.

Translation-topology research also identifies **False Reversibility**: a transformation may appear reversible at vocabulary/object level while original relational structure cannot be reconstructed.

Continuity similarly distinguishes restoration from verified recovery.

## Resolution

**DO NOT MAKE BTA THE OWNER OF GENERAL REVERSIBILITY.**

BTA should preserve:
- reversibility state supplied by the relevant domain;
- rollback/recovery transition references;
- residual state;
- provenance.

The Test 004 invariant remains useful:

> **Rollback != Restoration of Prior State Unless Prior-State Equivalence Is Actually Re-established.**

But BTA should treat equivalence as an externally evidenced/domain-sensitive determination.

Candidate:

`RollbackTransitionRef`

plus:

`PriorStateEquivalence = <CLAIMED / VERIFIED / PARTIAL / NOT_RESTORED / UNKNOWN>`

if required by implementation.

---

# 8. Finding F — intermediate/partial transition state is not clearly owned elsewhere

This is the strongest surviving BTA-specific refinement.

Existing systems contain partial states:
- STRA has CONDITION-PARTIAL;
- continuity has degraded/recovery/succession states;
- Clock CRSTL has branching, concurrency and transition relations;
- KCS has degraded/failed/unknown dependency states;
- CBER has partial responsibility and unresolved classifications.

But these are **partial states inside their own substantive functions**.

No reviewed system clearly owns the generic question:

> **What is the bounded state of an object/function while a consequential transition itself has begun but has not completed?**

Examples from Test 004:
- physically installed but not certified;
- transferred but not accepted;
- mixed but not validated;
- custody changed but authority not activated;
- partially decommissioned;
- rollback underway;
- failed after crossing with residual state.

This is not merely:
- maturity;
- review trigger;
- dependency state;
- externality state;
- authority state;
- Clock ordering.

It is the state of the **transition relation itself**.

## Resolution

**BTA SHOULD OWN TRANSITION PROGRESS / INTERMEDIATE TRANSITION STATE.**

Candidate minimum semantics:

`TransitionProgressState = <NOT_STARTED, PENDING, PARTIAL_CROSSING, CONDITIONAL/INTERMEDIATE, COMPLETED, FAILED_PRE_CROSSING, FAILED_POST_CROSSING, ROLLBACK/RECOVERY_ACTIVE, RESIDUAL_STATE>`

Exact vocabulary remains provisional.

> **Interface Crossing Can Be a State, Not Merely an Instantaneous Boundary Event.**

> **Partial Boundary Crossing Does Not Imply Completion of the Intended Transition.**

---

# 9. Finding G — transition relation remains the distinct BTA kernel

Civilisation Clock CRSTL is close to BTA but does not eliminate it.

CRSTL owns consequence-relevant temporal/dependency relation among **civil state transitions**:
- precedence;
- succession;
- concurrency;
- divergence;
- ordering uncertainty.

It deliberately leaves exact transition schema unspecified.

BTA addresses a different question:

> what transfers, survives, terminates, fails to propagate, crosses a gate, remains unresolved or enters intermediate state when a bounded consequential transition occurs?

Thus:

**Clock CRSTL**
= relation/order among transitions.

**BTA**
= internal integration grammar of a consequential transition.

They should interoperate.

Candidate:

`ClockTransitionRelationRefs`

where civil-scale ordering matters.

No duplication is required.

---

# 10. Finding H — KCS remains owner of dependency propagation

Nothing in Tests 001–004 changes the prior source resolution.

KCS already owns:
- typed material dependencies;
- change events;
- downstream candidate-review sets;
- selective propagation;
- correction propagation;
- alternatives/recovery paths;
- unknown/disputed dependencies.

BTA should expose transition events and DependencyRefs.

KCS determines propagation/review.

> **Transition != Dependency Propagation.**

Retain unchanged.

---

# 11. Finding I — responsibility continuity remains externally owned

Fault-Tolerant Accountability and Responsibility Continuity already provides:
- primary/concurrent/successor roles;
- failure triggers;
- bounded successor activation;
- authority-transfer limits;
- residual duties;
- safe state;
- correlated-failure analysis;
- handoff;
- accountability continuity;
- retirement boundary.

BTA may represent the transition event.

It should not duplicate responsibility-succession semantics.

---

# 12. Revised BTA 002 ownership map

After source resolution, the apparent BTA 002 additions should be reclassified.

| Apparent addition | Resolution | Primary owner |
|---|---|---|
| Consequence horizon | Existing solution; interface only | Cross Boundary Externality Recognition |
| Affected-party mapping | Existing solution | CBER / relevant domain |
| General relational model | Existing solution; reference effects only | KCS / Clock / Relational Grammar / domains |
| Relational transition effect | BTA integration residue | BTA |
| Validation-scope grammar | Existing solution; consume scoped result | STRA / validator / contextual systems |
| Authority conflict resolution | Existing solution/external | FPA/BCA/Judiciary/domain |
| Dependency propagation | Existing solution | KCS |
| General reversibility | Existing distributed solution | Domain + continuity/review architectures |
| Rollback transition recording | BTA integration residue | BTA |
| Intermediate/partial crossing | No clear existing generic owner | BTA |
| Failed-transition provenance | Existing provenance systems + BTA event record | BTA → Historical/KCS |
| Transition internal integration grammar | Distinct | BTA |

---

# 13. Revised candidate BTA 002 object

The source-resolution result argues for a **smaller** BTA 002 than the Test 001–004 synthesis initially proposed.

Candidate:

`BoundedTransition = <TransitionID, ObjectOrFunctionRef, Scope, PriorStateVector, Trigger, ObjectCardinality, TransitionBasisRef, ConsentOrPurposeState, ScopedValidationRefs, TransitionProgressState, NextStateVectorRefs, RelationalEffectRefs, ExternalityReviewRefs, SurvivingDutyRefs, SurvivingValueRefs, TerminatedAuthorityRefs, ReleasedResourceRefs, DependencyRefs, ClockTransitionRelationRefs, RollbackTransitionRef, Provenance, ReversibilityState, UncertaintyOrDisputeState, NonPropagationRules>`

The new fields are primarily **references and transition-state semantics**, not absorbed subsystems.

This preserves BTA as integration grammar.

---

# 14. Key architectural lesson

The adversarial tests did reveal real missing information.

But source resolution shows that much of the **solution already existed elsewhere in the Concord**.

This is a strong example of the distinction:

`Local Representation Gap != Global Architectural Gap`

The correct response is not to copy all required functions into BTA.

It is to connect BTA to their legitimate owners.

Thus BTA becomes stronger by becoming **smaller and better interfaced**, not larger.

---

# 15. Revised BTA 002 refinement decision

Proceed to BTA 002, but revise the earlier synthesis decision.

BTA 002 should add or clarify only:

1. **TransitionProgressState** for intermediate/partial/failed crossing;
2. **RelationalEffectRefs** rather than a BTA relational ontology;
3. **ScopedValidationRefs** rather than a BTA validation grammar;
4. **ExternalityReviewRefs** rather than a BTA consequence-horizon subsystem;
5. **RollbackTransitionRef / residual-state semantics** rather than universal reversibility ownership;
6. explicit interoperability with Clock CRSTL;
7. explicit preservation of failed/partial transition provenance;
8. existing dispute/authority/dependency boundaries.

Do not absorb:
- CBER;
- STRA;
- KCS;
- FPA/BCA;
- Clock transition ordering;
- general reversibility architecture.

---

# 16. Status

**SOURCE-RESOLUTION RESULT: BTA 002 REMAINS JUSTIFIED, BUT ITS SCOPE IS NARROWER THAN THE FIRST ADVERSARIAL SYNTHESIS SUGGESTED.**

The surviving distinct kernel is:

> **Represent the consequential transition itself—including its progress, partial/failed crossing, explicit non-propagation, survival/termination effects, and effects on externally owned relations—while preserving scoped references to validation, external consequences, dependencies, authority, temporal transition relations, reversibility and provenance without absorbing the systems that own those semantics.**

This should be the basis for BTA 002.
