# Bounded Transition Architecture — Graduation-Candidate Specification v0.3

**Version:** 0.3
**Status:** GRADUATION-CANDIDATE SPECIFICATION / NOT YET RELEASED
**Origin:** Extracted from the Concord Bounded Transition Architecture development programme
**Date:** September 2026

# 1. Purpose

Bounded Transition Architecture (BTA) is a portable interoperability grammar for consequential transitions that span independently owned state systems.

It addresses cases where several systems may correctly represent different dimensions of one change, but those dimensions do not necessarily change at the same time or imply one another.

> **BTA coordinates transition state without taking ownership of the systems whose states it coordinates.**

# 2. Portable problem

> **How can independently owned systems coordinate one consequential transition when different state dimensions may change asynchronously, without allowing completion, authority, permission, responsibility, validation, recovery or other consequential state in one dimension to be silently inferred in another?**

# 3. Core principles

> **State != Transition.**

> **Transition of an Object or Function != Transition of Every Attribute Attached to It.**

> **Completion in One Dimension != Completion of the Bounded Transition.**

> **Transition Coherence != Synchronous Completion.**

> **End of Authority != Automatic End of Responsibility.**

> **Partial Boundary Crossing != Completion of the Intended Transition.**

> **Failed Transition != No Transition History.**

> **Rollback != Restoration Unless Prior-State Equivalence Is Actually Re-established.**

> **Reference to an Owner State Does Not Transfer Ownership of That State's Semantics to BTA.**

> **Integration Must Not Become Sovereignty.**

# 4. Materiality gate

BTA is for consequential transitions, not universal event logging.

A host should activate BTA where change materially affects one or more dimensions such as:

- rights or standing;
- authority or permission;
- responsibility or duty;
- safety;
- custody;
- significant resources;
- continuity;
- consequential dependencies;
- irreversible change;
- sensitive purpose or consent;
- cross-system interoperability;
- material external consequences;
- accountability/provenance.

Routine low-consequence local changes remain local.

> **State Change != BTA Event.**

Substantive materiality thresholds belong to legitimate host/domain rules, not BTA.

# 5. Minimum sufficient representation

> **Use the Smallest Transition Representation That Preserves the Materially Relevant Consequences, Boundaries and Correction Path.**

A minimal consequential record may contain:

`BTA-Min = <TransitionID, ObjectOrFunctionRef, Scope, PriorStateRef, TransitionBasisRef, CurrentTransitionStateRef, CompletionConditionRef, NextStateRef, Provenance, [MaterialOptionalRefs]>`

Optional interfaces activate only when material.

> **The Existence of a BTA Field Does Not Require It to Be Populated When the Dimension Is Not Materially Applicable.**

> **Absence of a Non-Material Field != Incomplete Transition Record.**

# 6. Owner interface

Every substantive state entering BTA remains owned externally.

Generic interface:

`OwnerStateRef = <OwnerRef, StateRef, Scope, State, EvidenceOrBasisRef, Uncertainty, Provenance>`

BTA may bind, preserve and compare these references.

BTA must not manufacture, override or resolve the substantive state represented by them unless a separate legitimate owner explicitly supplies that function.

# 7. Transition identity and scope

Every material bounded transition should have a stable `TransitionID` and declared `Scope`.

The scope defines what the integration claim covers.

It does not imply completeness outside that boundary.

# 8. Transition topology

BTA may represent:

- one-to-one;
- one-to-many;
- many-to-one;
- many-to-many;
- one-to-none;
- unresolved transitions.

Classes may include transfer, transformation, activation, deactivation, branch/fork, merge, split, succession, retirement, destruction, recovery, rollback, reopening and continuous flow.

> **Object Cardinality != Relational Topology.**

# 9. Multidimensional transition state

Different owner systems may report different legitimate states for the same bounded transition.

Portable common classes may include:

- NOT_STARTED;
- ACTIVE_OR_PENDING;
- PARTIAL_OR_INTERMEDIATE;
- COMPLETED;
- FAILED;
- RECOVERY_OR_ROLLBACK_ACTIVE;
- RESIDUAL_OR_UNRESOLVED.

These are interoperability classes, not replacements for richer host states.

`TransitionStateRef = <OwnerRef, DomainOrHostState, CommonTransitionClass, Scope, Provenance, Uncertainty>`

# 10. Pending and unresolved state

Consequential pending state should identify its legitimate owner:

`PendingStateRef = <StateRef, Scope, OwnerRef, State, ResolutionOrCompletionRef, Provenance>`

An unresolved transition must not silently create a consequence that depends on successful completion.

Where materiality itself is unresolved, a host may use `MATERIALITY_UNRESOLVED` with scope, uncertainty basis, legitimate resolution owner and provenance.

# 11. Completion

Completion criteria remain externally owned.

`CompletionConditionRef` points to a condition supplied by a legitimate host system.

BTA may determine only whether the declared integration contract shows its required referenced conditions as satisfied, pending, failed or unresolved.

It does not invent the substantive criteria.

> **Local Completion != Integrated Transition Completion.**

# 12. Non-propagation

Object/function continuity must not silently transfer consequential attributes.

`NonPropagationRule = <SourceAttribute, TransitionClass, DestinationScope, PropagationState, IndependentAuthorityRequired, Provenance>`

Possible protected attributes include:

- authority;
- permission;
- consent;
- purpose;
- ownership;
- liability;
- identity;
- standing;
- access;
- confidentiality;
- correlation permission.

> **Do Not Infer Transfer of Consequential Authority, Consent, Rights, Identity or Liability Merely From Object Continuity.**

# 13. Validation/review interface

Validation remains externally owned.

`ValidationRef` should preserve at least owner, scope, result, conditions/limitations where material, uncertainty and provenance.

BTA must not reduce scope-bounded validation to an unqualified PASS.

> **Validation Pass != Proof of Evaluation-Space Completeness.**

# 14. Dependency interface

Dependency discovery and propagation remain externally owned.

BTA may expose the transition to a dependency/change-propagation owner and preserve returned state through `DependencyRefs`.

> **Transition != Dependency Propagation.**

# 15. External-consequence interface

Affected parties, causal/material consequence, responsibility and response routing remain externally owned.

BTA may preserve `ExternalConsequenceRefs` or equivalent review references.

> **Transition Consequence Reference != External-Consequence Analysis Ownership.**

# 16. Authority and permission interface

Authority/permission legitimacy remains externally owned.

BTA may preserve transition-basis references, authority-state references and terminated-authority references.

`TerminatedAuthorityRef` records externally legitimate termination state; populating the field does not itself terminate authority.

> **Transition Need Does Not Create Authority.**

# 17. Surviving duties

A transition may terminate authority while duties remain active.

BTA may preserve `SurvivingDutyRefs` with externally supplied termination/resolution conditions where applicable.

# 18. Recovery and rollback interface

Recovery sufficiency and continuity remain externally owned.

BTA may preserve prior-valid-state and recovery references.

`PriorValidStateRef = <StateRef, Scope, EffectiveTime, EvidenceRef, RecoveryStatus, Provenance>`

Rollback is itself a transition.

BTA must not certify restoration merely because rollback activity completed.

# 19. Failed and partial transition

A failed attempt may create consequential residual state.

Where material:

`FailedAttemptRef = <EventRef, CrossingState, ResidualEffectRefs, RecoveryRefs, Provenance>`

A transition that fails after partial crossing must preserve the crossing and residual history.

# 20. Relational effects

General relation semantics remain externally owned.

BTA may preserve only the effect of the transition on an externally owned relation:

`RelationalEffectRef = <RelationRef, EffectState, OwnerRef, Provenance>`

Candidate effect states:

- PRESERVED;
- CREATED;
- CHANGED;
- TERMINATED;
- UNKNOWN_OR_REVIEW_REQUIRED.

# 21. Temporal/transition-relation interface

Ordering, ancestry, concurrency and temporal relation among transitions may be externally owned.

BTA may preserve `TemporalRelationRefs` without becoming a universal scheduler or clock.

# 22. Provenance/history interface

BTA must preserve enough transition provenance to reconstruct materially consequential state change.

This may include initiation, prior state, basis, crossing, failed attempts, owner-state changes, completion/termination events, disputes and recovery actions.

Long-term archival custody remains externally owned.

Historical availability of prior authority does not reactivate that authority.

# 23. Candidate portable contract

`BoundedTransition = <`

`TransitionID,`
`ObjectOrFunctionRefs,`
`Scope,`
`TransitionClass,`
`ObjectCardinality,`
`ParticipatingOwnerRefs,`
`PriorValidStateRefs,`
`TransitionBasisRefs,`
`TransitionPhaseRefs,`
`TransitionStateRefs,`
`PendingStateRefs,`
`CompletionConditionRefs,`
`ProtectedUnresolvedStateRefs,`
`NonPropagationRules,`
`ValidationRefs,`
`RelationalEffectRefs,`
`ExternalConsequenceRefs,`
`SurvivingDutyRefs,`
`SurvivingValueRefs,`
`TerminatedAuthorityRefs,`
`ReleasedResourceRefs,`
`DependencyRefs,`
`TemporalRelationRefs,`
`RecoveryRefs,`
`NextStateRefs,`
`ReversibilityState,`
`UncertaintyOrDisputeState,`
`Provenance`

`>`

Fields are materially optional unless required by the host profile.

# 24. Host responsibilities

A host must provide legitimate owners for substantive functions it uses.

BTA does not repair the absence of:

- authority;
- validation;
- dependency analysis;
- externality analysis;
- recovery architecture;
- adjudication;
- domain state semantics;
- temporal semantics;
- provenance custody.

If a host lacks one of these functions, BTA may expose the absence or uncertainty. It must not silently become the missing function.

# 25. Failure modes

Implementations must guard against:

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
- universal logging;
- schema inflation;
- materiality laundering;
- uncertainty collapse;
- evaluation-space overclaim.

# 26. Falsification / failure criteria

A portable BTA implementation fails its stated mechanism if it requires BTA to manufacture substantive owner state, routinely infers consequential attribute transfer from object continuity, declares integrated completion despite required pending conditions, treats failed partial transitions as no event, treats rollback as restoration without evidence, requires all optional interfaces for low-complexity transitions, or cannot preserve owner boundaries across a multi-system transition.

# 27. Evaluation-space boundary

> **Correct Representation Within the Transition Schema != Demonstrated Completeness of the Transition Schema.**

A correct BTA record may still omit a materially relevant dimension that no participating owner represented.

High-consequence or irreversible transitions warrant proportionate completeness checking.

> **Small Represented Transition != Demonstrated Small Real Consequence.**

# 28. Worked portable example

A digital service is transferred from Operator A to Operator B.

At one point:

- B provides limited service;
- A still owns residual unresolved obligations;
- a data copy has completed;
- B has not yet accepted custody;
- A's privileged access is revoked;
- B's privileged access awaits independent authorisation;
- live-service validation is partial.

BTA can bind those states to one TransitionID without inferring:

- copied data → accepted custody;
- A access revoked → B access active;
- B operating → responsibility fully transferred;
- partial validation → transition complete.

The substantive decisions remain with their owners.

# 29. Concord provenance and interface appendix

This portable specification was extracted from Concord BTA development.

Portable generic interfaces map back to the existing Concord architecture as follows:

| Portable interface | Concord owner | Concord status |
|---|---|---|
| specialised handover interface | Civil State Handover Protocol | RETAINED UNCHANGED |
| dependency/change-propagation interface | KCS Change Propagation | RETAINED UNCHANGED |
| validation/review/trigger interface | State Triggered Review Architecture and domain validators | RETAINED UNCHANGED |
| external-consequence interface | Cross Boundary Externality Recognition | RETAINED UNCHANGED |
| temporal/transition-relation interface | Civilisation Clock / CRSTL | RETAINED UNCHANGED |
| permission/authority interface | FPA / bounded authority architecture | RETAINED UNCHANGED |
| recovery/continuity interface | Continuity Protocol and domain recovery architecture | RETAINED UNCHANGED |
| provenance/history interface | Historical | RETAINED UNCHANGED |
| domain-state interface | relevant Concord domain state machine | RETAINED UNCHANGED |

> **The portable specification does not remove or replace any of these systems.**

Inside Concord, the named Concord systems remain the concrete owners. The generic terms exist only so the portable BTA mechanism can operate in other host architectures.

# 30. Validation status

Pre-portable development evidence includes adversarial testing, source-resolution audits, clean cross-domain testing, blind machine-readable transfer, owner-interface audit and materiality testing.

Formal PMEDG blind transfer testing has now been completed across two materially different non-Concord domains. Both tests passed with strong portable transfer and exposed no material defect requiring specification expansion.

**Current status: GRADUATION-CANDIDATE SPECIFICATION v0.3 / NOT YET RELEASED.**

# 31. Transfer evidence and next step

Formal blind transfer evidence:

- PMEDG Blind Transfer Test 001 — Museum Collection Relocation: **PASS — STRONG PORTABLE TRANSFER**;
- PMEDG Blind Transfer Test 002 — Payment Service Cutover: **PASS — STRONG PORTABLE TRANSFER**;
- Cross-Test Convergence 001: **STRONG CONVERGENCE**;
- Stage 11 decision: a third blind test is not currently required.

No substantive architectural revision was required between v0.1 and this graduation candidate. The version change records PMEDG progression and test evidence rather than mechanism expansion.

Next: perform the PMEDG Graduation-Candidate Consistency Check, then formal Portable-Package Graduation Review.