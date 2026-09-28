# BTA Adversarial Tests 001–004 — Synthesis and Refinement Decision

**Author:** Alexander C. Blainey — Independent Researcher  
**Project:** The Concord Framework  
**Framework Version:** Concord V1.3  
**Target:** Bounded Transition Architecture  
**Evidence Base:** BTA Adversarial Tests 001–004  
**Epistemic Lens:** Evaluation-Space Completeness Problem (ESCP)  
**Status:** ACTIVE DEVELOPMENT SYNTHESIS / REFINEMENT DECISION / NON-CANONICAL  
**Date:** September 2026

---

# 1. Purpose

This document consolidates the first focused adversarial programme against Bounded Transition Architecture (BTA).

The purpose is to avoid modifying the core architecture after every individual test.

It separates:
- existing BTA mechanisms that survived testing;
- missing structures independently rediscovered across tests;
- useful one-test refinements;
- unresolved questions;
- changes justified for a BTA 002 revision.

---

# 2. Test set

## Test 001 — Hidden Non-Propagation Dimension

Target:
whether every represented BTA field can be correct while a consequential dimension remains outside the transition object.

Finding:
a genomic transition can legitimately move a participant's data while generating consequential inference about a biological relative who is not a transitioned object.

Result:
**GAP DETECTED.**

Core insight:

> **No Attribute Transfer != No Consequential State Creation.**

and:

> **The Boundary of the Transition Object != Necessarily the Boundary of the Transition's Consequences.**

---

## Test 002 — Branch/Merge Relational Information Loss

Target:
whether many→1 or 1→many topology can preserve object states while losing relational value.

Finding:
two infrastructure subsystems can be merged while preserving both nominal functions but destroying independent fallback/failure diversity created by their separation.

Result:
**GAP INDEPENDENTLY REPRODUCED.**

Core insight:

> **Object Cardinality != Relational Topology.**

and:

> **Preservation of Source-State Content != Preservation of Relational System Function.**

---

## Test 003 — Conflicting Transition Authorities

Target:
whether multiple legitimate scoped authorities force BTA to become a precedence/adjudication system.

Finding:
BTA can distinguish dimensional non-conflict from true overlapping conflict and preserve unresolved state without inventing authority.

Result:
**PASS.**

Core insight:

> **Need for Transition Does Not Create Authority to Resolve the Transition.**

Existing BTA authority semantics are sufficient in principle.

---

## Test 004 — Failed Interface Gate and Partial Boundary Crossing

Target:
gate rejection, partial crossing, rollback failure and incomplete interface evaluation space.

Findings:
- ordinary gate rejection is safely represented;
- crossing can itself occupy consequential intermediate states;
- rollback may create a new state rather than restore the old one;
- a valid gate result can be over-scoped if its evaluation boundary is discarded;
- interface transformation can destroy distinctions before downstream evaluation.

Result:
**PASS IN PART / REFINEMENT REQUIRED.**

Core insight:

> **Gate Pass != Proof of Evaluation-Space Completeness.**

and:

> **Referenced Validation Must Preserve the Scope of the Validation, Not Merely Its Boolean Result.**

---

# 3. Existing BTA components validated

The adversarial programme supports retaining the following existing architecture.

### Multidimensional state

Test 003 showed that many apparent authority conflicts disappear when state dimensions remain separate.

Retain.

### Dimension-scoped authority

Test 003 strongly validates:

> **Transition Authority Must Be Scoped to the State Dimension Being Changed.**

Retain.

### Schema/authority separation

BTA correctly refuses to become substantive authority merely because a transition needs resolution.

Retain.

### Unresolved/disputed state

The ability to represent:
- UNKNOWN;
- DISPUTED;
- UNRESOLVED_NO_LEGITIMATE_OWNER;
- NO_VALID_SUCCESSOR;
- SAFE_STATE_PENDING_RESOLUTION

is essential.

Retain and clarify internal conflict semantics.

### Reversibility state

Test 004 validates the existing concept but requires stronger rollback semantics.

Retain and refine.

### Non-propagation

Tests 001–002 do not invalidate non-propagation.

They show that non-propagation solves only one class of transition failure.

Retain.

### Provenance

All four tests increase rather than reduce the importance of transition provenance.

Retain and strengthen for failed/partial transitions.

---

# 4. Repeated missing structure — relational transition

Tests 001 and 002 independently expose consequential state that exists in relationships rather than solely in transitioned objects.

Test 004 also shows that interfaces can create or destroy distinctions between source and destination representations.

Evidence now supports adding an explicit relational component to BTA.

Provisional:

`RelationalTransitionRef = <RelationRef, ParticipantRefs, PriorRelationalState, TransitionEffect, NextRelationalState, Materiality, OwnerSystemRef, Provenance, Uncertainty>`

BTA does not own the substantive semantics of the relation.

It records that a material relation:
- exists;
- is created;
- changes;
- survives;
- terminates;
- or remains unresolved.

**REFINEMENT DECISION: ADD IN BTA 002.**

---

# 5. Repeated missing structure — consequence horizon

Test 001 establishes that object boundaries do not necessarily bound consequences.

Test 002 establishes that relation boundaries can contain system value.

Test 004 establishes that interface representations can constrain what consequences remain visible.

A consequence-horizon concept is therefore justified, but it must not imply exhaustive prediction.

Recommended form:

`ConsequenceHorizon = <DirectObjectRefs, MaterialRelationshipRefs, MaterialAffectedPartyRefs, GeneratedConsequenceRefs, ExternalEffectUncertaintyState, Provenance>`

Its role is diagnostic, not omniscient.

It asks:

> What materially affected entities, relationships, states or consequences are plausibly outside the nominal transition object?

It does not claim to enumerate all possible consequences.

**REFINEMENT DECISION: ADD AS CONSEQUENCE-SCALED DIAGNOSTIC / REFERENCE STRUCTURE.**

---

# 6. Validation-scope preservation

Test 004 independently identifies a clear interoperability requirement.

An interface or validator may return a correct result over a bounded evaluation space.

BTA must not strip that scope away.

Replace conceptual consumption of:

`GateRef → PASS`

with:

`GateEvaluationRef → <EvaluatedScope, Result, Conditions, ResidualUncertainty, ValidityWindow, Provenance>`

The domain architecture remains owner of substantive validation.

BTA preserves the epistemic boundary of the validation.

**REFINEMENT DECISION: ADD IN BTA 002.**

---

# 7. Intermediate transition state

Test 004 demonstrates that crossing can be consequential before the intended destination state is reached.

Examples:
- partial installation;
- data partially transferred;
- resource mixed;
- temporary credential activated;
- custody changed before certification;
- physical boundary crossed before final validation.

BTA therefore needs explicit support for intermediate transition state.

This need not require a universal rigid taxonomy.

Minimum requirement:

`TransitionProgressState`

capable of distinguishing at least:
- not started;
- pending;
- partial crossing;
- conditional/intermediate;
- completed;
- failed before crossing;
- failed after crossing;
- rollback/recovery active;
- residual state.

**REFINEMENT DECISION: ADD SEMANTIC CAPABILITY; KEEP TAXONOMY PROVISIONAL.**

---

# 8. Rollback equivalence

Existing BTA says reversibility is a property of the transition.

Test 004 adds:

> **Rollback != Restoration of Prior State Unless Prior-State Equivalence Is Actually Re-established.**

A rollback operation may itself:
- alter the object;
- leave residue;
- create new duties;
- preserve exposure;
- fail partially.

Therefore rollback should be represented as a transition, not deletion of transition history.

**REFINEMENT DECISION: ADD AS INVARIANT AND REVERSIBILITY SEMANTIC.**

---

# 9. Conflict-state refinement

Test 003 does not justify a new top-level field.

Existing `UncertaintyOrDisputeState` can contain:
- competing claims;
- scope dispute;
- basis dispute;
- fact dispute;
- known/unknown precedence;
- safe interim state;
- resolution owner.

**REFINEMENT DECISION: CLARIFY NESTED SEMANTICS; DO NOT EXPAND TOP-LEVEL SCHEMA SOLELY FOR THIS.**

---

# 10. ESCP integration boundary

ESCP materially improved the adversarial programme.

However:

> **BTA Must Not Become a General Evaluation-Space Completeness Engine.**

BTA should incorporate limited ESCP safeguards relevant to transitions:
- preserve validation scope;
- avoid claiming schema completeness;
- preserve unresolved external-effect uncertainty;
- scale review with consequence and irreversibility;
- preserve pathways for later correction.

ESCP remains its own portable epistemic model.

BTA references the principle rather than absorbing the full module.

**REFINEMENT DECISION: LIMITED INTERFACE / META-EVALUATION CONTRACT ONLY.**

---

# 11. Revised conceptual transition object

Evidence supports moving from the BTA 001 candidate:

`<TransitionID, ObjectOrFunctionRef, Scope, PriorStateVector, Trigger, Cardinality, TransitionBasisRef, ConsentOrPurposeState, InterfaceGateRefs, NextStateVectorRefs, SurvivingDutyRefs, SurvivingValueRefs, TerminatedAuthorityRefs, ReleasedResourceRefs, DependencyRefs, Provenance, ReversibilityState, UncertaintyOrDisputeState, NonPropagationRules>`

toward a BTA 002 candidate containing additional references:

`<TransitionID, ObjectOrFunctionRef, Scope, PriorStateVector, Trigger, ObjectCardinality, TransitionBasisRef, ConsentOrPurposeState, GateEvaluationRefs, TransitionProgressState, NextStateVectorRefs, RelationalTransitionRefs, ConsequenceHorizonRef, SurvivingDutyRefs, SurvivingValueRefs, TerminatedAuthorityRefs, ReleasedResourceRefs, DependencyRefs, Provenance, ReversibilityState, UncertaintyOrDisputeState, NonPropagationRules>`

Important:

This remains a representation.

It does not become authority, validator, dependency engine, relational ontology or consequence predictor.

---

# 12. Revised conceptual sequence

BTA 001 can appear as:

`Prior State → Gate → Transition → Next State`

BTA 002 should permit:

`Prior Object + Relational State`

→ `Transition Basis`

→ `Scoped Gate Evaluation`

→ `Partial/Intermediate Crossing`

→ `Object + Relational Effects`

→ `Consequence-Horizon Review`

→ `Next / Failed / Residual / Unresolved State`

→ `Dependency Propagation References`

with provenance across the entire sequence.

This is not necessarily chronological in every implementation.

---

# 13. Candidate invariants supported for BTA 002

Retain all BTA 001 invariants and add:

> **Correct Representation Within the Transition Schema != Demonstrated Completeness of the Transition Schema.**

> **The Boundary of the Transition Object != Necessarily the Boundary of the Transition's Consequences.**

> **Transition Can Generate Consequential Relational State Without Transferring an Existing Attribute.**

> **Preservation of Source-State Content != Preservation of Relational System Function.**

> **Object Cardinality != Relational Topology.**

> **Interface Crossing Can Be a State, Not Merely an Instantaneous Boundary Event.**

> **Partial Boundary Crossing Does Not Imply Completion of the Intended Transition.**

> **Rollback != Restoration of Prior State Unless Prior-State Equivalence Is Actually Re-established.**

> **Gate Pass != Proof of Evaluation-Space Completeness.**

> **Referenced Validation Must Preserve the Scope of the Validation, Not Merely Its Boolean Result.**

> **Successful Interface Translation != Preservation of Every Decision-Relevant Distinction.**

> **Failed Transition != No Transition History.**

> **Need for Transition Does Not Create Authority to Resolve the Transition.**

---

# 14. What should not be added

The tests do not justify:
- exhaustive consequence prediction;
- universal relationship mapping;
- BTA-owned technical validation;
- BTA-owned authority precedence;
- automatic legal interpretation;
- automatic consent interpretation;
- universal logging of trivial transitions;
- a claim that every transition schema can be proven complete.

These would violate BTA's integration role and/or ESCP discipline.

---

# 15. Materiality remains essential

The refinements increase representational power and therefore increase bureaucratisation risk.

Formal relational/consequence-horizon review should remain proportionate to:
- rights/standing;
- authority/permission;
- responsibility/duty;
- safety;
- custody;
- significant resources;
- continuity;
- consequential dependencies;
- irreversibility;
- Historical accountability;
- sensitive consent/purpose;
- cross-system interoperability;
- material effects on non-participating parties;
- material relational resilience/value.

Routine low-consequence changes remain local.

---

# 16. Adversarial programme result

The first four tests have done three useful things.

### They found a genuine repeated gap

Relational and external consequence state was underrepresented.

### They validated existing architecture

Scoped authority and unresolved-state handling survived a focused adversarial case.

### They clarified interfaces

BTA must preserve validation scope and partial transition history without becoming the validator.

This is sufficient evidence for a BTA 002 revision.

It is not sufficient evidence for PMEDG graduation.

---

# 17. Refinement decision

**DECISION: PROCEED TO BTA 002.**

BTA 002 should integrate:
1. relational transition references;
2. consequence-horizon diagnostic/reference;
3. validation-scope preservation;
4. intermediate transition state;
5. rollback-equivalence semantics;
6. clearer dispute-state semantics;
7. explicit ESCP scope boundary.

After BTA 002 is written, it should be tested against:
- a clean cross-domain case not used in development;
- machine-readable transfer;
- source resolution against the Interoperability Wrapper;
- and only then PMEDG candidacy.

---

# 18. Status

**BTA 001:** preserved as the first formal integration grammar.

**Adversarial Tests 001–004:** completed.

**BTA 002:** justified and ready to draft.

**Portable graduation:** not yet justified.
