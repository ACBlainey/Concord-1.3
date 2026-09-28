# BTA Interface-Boundary Audit 004 — Owner-System Non-Absorption Review

**Author:** Alexander C. Blainey — Independent Researcher
**Project:** The Concord Framework
**Framework Version:** Concord V1.3
**Status:** ACTIVE DEVELOPMENT / INTERFACE-BOUNDARY AUDIT / NON-CANONICAL
**Date:** September 2026

# 1. Purpose

Test whether BTA 002 remains a transition-coherence interoperability layer or duplicates, overrides, or silently absorbs semantics owned by existing Concord systems.

Audit rule:

> **A BTA reference is legitimate only if the referenced owner remains the source of substantive state, criterion, authority, relation or decision.**

Failure occurs if BTA can independently manufacture an owner-system conclusion merely because a transition requires one.

# 2. Civil State Handover Protocol — CSHP

**Owner function:** civil handover of live state and responsibility, including Transition Epoch, Pending-State Capsule, Handover Witness, Recovery Anchor and Transition Hold.

**BTA use:** may reference civil handover state, pending state, phase/epoch, recovery position and protected unresolved state.

**Boundary:** BTA must not decide which provider/path carries civil responsibility, define the contents of a Pending-State Capsule, or replace CSHP's provider-independent continuity witness.

**Finding:** PASS.

BTA generalises the interface pattern while CSHP retains the specialised civil-handover semantics.

# 3. KCS Change Propagation

**Owner function:** dependency representation, bounded downstream review-set generation, dependency state, change propagation and propagation stopping conditions.

**BTA use:** `DependencyRefs` expose a transition event to KCS and preserve returned dependency/review state.

**Boundary:** BTA must not discover the dependency graph, determine material downstream effect, propagate review, infer compatibility or execute downstream remedy.

> **Transition != Dependency Propagation.**

**Finding:** PASS.

# 4. State Triggered Review Architecture — STRA

**Owner function:** representation/evaluation of conditions that make review, reconsideration, reactivation or action candidacy due.

**BTA use:** consumes scoped validation/review/trigger state and may expose transition changes capable of feeding a trigger.

**Boundary:** BTA must not invent trigger criteria, determine substantive review outcomes, convert condition satisfaction into authority or certify a domain capability.

Potential terminology risk: `CompletionConditionRefs` could be misread as BTA evaluating the condition. BTA 002 already states the conditions are supplied by legitimate owners. The field should remain explicitly **reference-only**.

**Finding:** PASS WITH TERMINOLOGY SAFEGUARD.

# 5. Cross Boundary Externality Recognition — CBER

**Owner function:** cross-boundary consequence candidacy, affected-party/standing representation, evidence, causal confidence, materiality, responsibility mapping, authority/coordination mapping and bounded response routing.

**BTA use:** `ExternalityReviewRefs` or `CrossBoundaryConsequenceRefs` preserve the existence/state of externally owned consequence review.

**Boundary:** BTA must not determine affected parties, materiality, causation, responsibility, jurisdiction or remedy.

> **Transition Consequence Reference != Externality Analysis Ownership.**

**Finding:** PASS.

# 6. Civilisation Clock / CRSTL

**Owner function:** consequence-relevant relations among civil state transitions, including ordering, concurrency, dependency/precedence and uncertainty in temporal relation.

**BTA use:** `ClockTransitionRelationRefs` and optional externally owned phase/epoch references.

**Boundary:** BTA must not establish a universal total order, duplicate Clock transition ancestry or infer causal precedence from timestamps.

Potential overlap: BTA has `TransitionID` while CRSTL also records Transition ID. This is not duplicate ownership if the same transition identity is referenced across both systems. BTA owns the integration record; Clock owns relation among transition events.

**Finding:** PASS.

# 7. Fractal Permission Architecture — FPA

**Owner function:** contextual permission representation, basis, action, target/context, function, conditions, temporal scope, delegation and termination.

**BTA use:** may record permission-state references, transition-basis references, terminated-authority/permission references and non-propagation across transition.

**Boundary:** BTA must not decide whether permission is legitimate, infer permission from capability/possession, define minimum necessary permission or make attempted revocation legitimate.

`TerminatedAuthorityRefs` must therefore mean **references to termination determined by the legitimate owner**, not a BTA command to terminate.

**Finding:** PASS WITH TERMINOLOGY SAFEGUARD.

# 8. Bounded Contextual Authority / authority architecture

Existing Concord source resolutions identify BCA/authority architecture as owner of bounded authority semantics. FPA likewise explicitly separates permission representation from justification.

**BTA use:** records `TransitionBasisRefs`, authority-state references, terminated-authority references and unresolved authority conflict.

**Boundary:** BTA must never create authority from transition necessity, resolve genuine authority conflict, or infer successor authority from predecessor state.

> **Transition Schema != Transition Authority.**

> **Need for Transition Does Not Create Authority to Resolve the Transition.**

**Finding:** PASS.

# 9. Continuity Protocol

**Owner function:** continuity object, required continuity state, disruption envelope, recovery basis, recovery path, succession/restoration, RTO/RPO/MAF, recovery verification and continuity evidence.

**BTA use:** may reference prior valid state, recovery anchor/path, rollback/recovery event, surviving recovery capability and supplied reversibility state.

**Boundary:** BTA must not determine the continuity object, declare a recovery basis sufficient, define MAF, certify successful recovery or grant successor authority.

Potential terminology risk: `PriorValidStateRef` and `RollbackOrRecoveryRefs` could be mistaken for recovery certification. BTA must preserve them as externally evidenced references.

**Finding:** PASS WITH TERMINOLOGY SAFEGUARD.

# 10. Historical

**Owner function:** bounded temporal custody, provenance, historical state, transition/version history, reconstruction context, uncertainty and evaluation-space preservation.

**BTA use:** creates/preserves transition provenance and supplies transition records suitable for Historical custody.

**Boundary:** BTA must not determine retention, Historical access, reconstruction truth, destruction authority or long-term custody policy. Historical retrieval must not reactivate transition authority.

BTA's `Provenance` field is not a competing Historical system. It is the provenance attached to the live transition record and may later be preserved by Historical.

**Finding:** PASS.

# 11. Cross-system collision tests

## 11.1 Validation + completion

STRA/domain validator says `CONDITION_PARTIAL`; BTA has a completion-condition reference.

Can BTA declare completion independently? **NO.**

Result: PASS.

## 11.2 Dependency + transition

BTA transition completes locally while KCS dependency review remains `REVIEW_REQUIRED`.

Can BTA clear KCS review because its own state is complete? **NO.**

Result: PASS.

## 11.3 Authority + succession

Source function terminates and destination physically possesses the object.

Can BTA activate destination permission/authority? **NO.**

Result: PASS.

## 11.4 Recovery + rollback

BTA records rollback complete but Continuity/domain verification says prior functional equivalence is unverified.

Can BTA declare prior state restored? **NO.**

Result: PASS.

## 11.5 Externality + transition completion

All internal BTA completion conditions are satisfied while CBER externality review remains open.

Can BTA declare the externality resolved? **NO.**

Whether the bounded transition itself may be declared complete depends on its declared scope/completion contract; the externality remains independently open unless legitimate owner criteria make its closure a required condition.

Result: PASS.

## 11.6 Historical + authority

Historical preserves a prior transition basis and permission state.

Can BTA reuse the historical authority merely because it is available as provenance? **NO.**

Result: PASS.

# 12. Main audit finding

No owner-system absorption was found.

BTA 002 is currently structurally referential rather than sovereign.

The architecture consistently follows:

> **Owner system determines substantive state → BTA references scoped state → BTA preserves cross-system transition coherence → owner system remains authoritative for its own semantics.**

# 13. Terminology hardening

Three fields would benefit from an explicit normative interpretation to reduce implementation drift:

1. `CompletionConditionRefs` — reference-only; BTA does not define or satisfy domain criteria itself.
2. `TerminatedAuthorityRefs` — records externally legitimate termination state; BTA does not terminate authority merely by populating the field.
3. `RollbackOrRecoveryRefs` / `PriorValidStateRefs` — preserve externally evidenced recovery position; BTA does not certify restoration or continuity.

These are clarifications, not new architecture.

# 14. Interface invariant

Add the following invariant to BTA:

> **Reference to an Owner-System State Does Not Transfer Ownership of That State's Semantics to BTA.**

and operationally:

> **BTA May Bind, Preserve and Compare Scoped Owner-System States; It Must Not Manufacture, Override or Resolve Those States Unless a Separate Legitimate Owner Explicitly Supplies That Function.**

# 15. Audit result

**PASS — NO MATERIAL INTERFACE-BOUNDARY VIOLATION FOUND.**

The audit supports the reduced BTA architecture as an interoperability layer rather than a competing authority, dependency, validation, externality, temporal, continuity or Historical system.

# 16. Next step

1. Add the interface invariant and terminology hardening to BTA 002.
2. Run the planned **materiality/proportionality test** to determine whether BTA can remain lightweight for simple consequential transitions.
3. If that passes without architectural expansion, begin PMEDG candidacy assessment.