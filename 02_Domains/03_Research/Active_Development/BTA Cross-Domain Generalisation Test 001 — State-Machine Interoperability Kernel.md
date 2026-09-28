# BTA Cross-Domain Generalisation Test 001 — State-Machine Interoperability Kernel

**Author:** Alexander C. Blainey — Independent Researcher  
**Project:** The Concord Framework  
**Framework Version:** Concord V1.3  
**Status:** ACTIVE DEVELOPMENT / CROSS-DOMAIN GENERALISATION TEST / NON-CANONICAL  
**Date:** September 2026

# 1. Purpose

Source Resolution 003 found that partial/intermediate transition semantics already exist in specialised Concord systems, especially the Civil State Handover Protocol (CSHP), Historical and Infrastructure.

This test asks which CSHP-derived transition mechanisms survive across three structurally different domains:

1. infrastructure successor-service transition;
2. enterprise wind-down and closure;
3. genomic clinical/research/purpose transition.

The objective is not to force all three into one state machine. It is to identify the smallest common interoperability kernel BTA genuinely needs.

# 2. Test method

Candidate CSHP patterns tested:

- Transition Epoch;
- Pending State;
- Handover/Transition Witness;
- Recovery Anchor;
- Transition Hold;
- responsibility/authority locus;
- explicit completion threshold;
- failure/recovery provenance.

For each domain, the question is whether the underlying function survives even if the local implementation vocabulary differs.

# 3. Domain A — Infrastructure successor-service transition

Existing Infrastructure architecture already represents:

- RETIREMENT_PLANNED;
- SUCCESSOR_TRANSITION;
- WITHDRAWAL_PENDING;
- DECOMMISSIONING;
- degraded transition;
- irreversibility threshold;
- successor verification;
- multidimensional operational/stewardship/physical/logical/transition/Historical state.

## Transition Epoch

**SURVIVES FUNCTIONALLY.**

Infrastructure needs to know whether the operative service state is still predecessor-led, overlapping, successor-transitioning, successor-active, withdrawal-pending or retired.

The domain need not call these epochs. Its lifecycle/transition state already supplies richer local semantics.

## Pending State

**SURVIVES STRONGLY.**

Examples:
- successor service not yet proven;
- old asset withdrawal pending;
- decommissioning incomplete;
- residual stewardship active;
- logical access not yet revoked.

## Witness / provenance

**SURVIVES STRONGLY.**

Successor readiness, verification, withdrawal, decommissioning and residual obligations require provenance.

## Recovery Anchor

**SURVIVES CONDITIONALLY.**

Infrastructure already requires rollback preservation before an irreversibility threshold where consequence warrants. The predecessor or another recoverable configuration may function as recovery basis.

Not every infrastructure transition is reversible, so the anchor cannot be mandatory in all cases.

## Transition Hold

**SURVIVES FUNCTIONALLY.**

If successor readiness is unresolved, the architecture should not infer that predecessor withdrawal is legitimate. The local expression may be continued overlap, safe degraded operation, withdrawal hold or another safe state.

## Completion threshold

**SURVIVES STRONGLY.**

Successor availability is explicitly not equivalent to successor proven reliability.

# 4. Domain B — Enterprise wind-down

Existing enterprise architecture already represents:

- RETIREMENT_REVIEW;
- PLANNED_WIND_DOWN;
- NO_NEW_LONG_TERM_OBLIGATIONS;
- TRANSITIONING_CUSTOMERS;
- TRANSITIONING_WORKFORCE;
- TRANSFERRING_OR_SETTLING_OBLIGATIONS;
- CLOSURE_PENDING;
- HISTORICAL_ONLY;
- progressive permission sunset;
- accountability surviving closure;
- successor relationships;
- outstanding obligations.

## Transition Epoch

**SURVIVES FUNCTIONALLY.**

Wind-down is explicitly phased. Different functions may enter different closure phases at different times.

A universal numeric epoch is unnecessary; the domain's WindDownState supplies the local state.

## Pending State

**SURVIVES STRONGLY.**

Closure can be pending while obligations, customer transitions, workforce transitions, disputes, asset disposition and permission sunset remain incomplete.

## Witness / provenance

**SURVIVES STRONGLY.**

Enterprise identity and Historical architecture already require provenance-bearing consequential control and lifecycle changes.

## Recovery Anchor

**SURVIVES WEAKLY / CONDITIONALLY.**

Some wind-down decisions may be reversible before commitments or dissolution thresholds; others are intentionally irreversible.

The more general surviving requirement is not a mandatory rollback point but a known prior valid state plus explicit irreversibility/recovery status.

## Transition Hold

**SURVIVES FUNCTIONALLY BUT NOT AS UNIVERSAL STOP.**

Unresolved obligations can prevent particular closure consequences from being treated as complete. For example, operational closure must not imply accountability closure.

However, the whole enterprise need not necessarily freeze while one dimension remains pending.

## Completion threshold

**SURVIVES STRONGLY.**

Closure in one dimension does not establish closure in all dimensions.

# 5. Domain C — Genomic clinical/research/purpose transition

Existing genomic architecture represents:

- collection authority;
- consent/authority state;
- purpose states;
- custody state;
- privacy state;
- access state;
- correlation state;
- derivative relations;
- retention review;
- destruction state;
- purpose-bounded research permission.

It explicitly states:

> **Consent to One Genomic Function != Consent to Every Genomic Function.**

> **Research Permission != General Participant-Data Permission.**

> **No arrow creates authority merely because the previous state exists.**

## Transition Epoch

**DOES NOT GENERALISE LITERALLY.**

A genomic object may simultaneously possess different legitimate purpose/custody/access states. A single sequential epoch could falsely imply total ordering.

The surviving requirement is a transition identifier/phase plus scoped state references, not a universal epoch number.

## Pending State

**SURVIVES STRONGLY.**

A sample/data object may await separate research-purpose approval, privacy transformation, output review, retention review or re-consent.

## Witness / provenance

**SURVIVES STRONGLY.**

Consent scope, collection authority, custody, derivative creation, access and purpose transition require provenance.

## Recovery Anchor

**SURVIVES ONLY AS A GENERAL PRIOR-STATE REFERENCE.**

Some transformations cannot be undone. Once information has been disclosed, copied, correlated or used to produce research outputs, literal rollback may be impossible.

The general requirement is therefore preservation of the last valid prior state and provenance, not an assumption of recoverability.

## Transition Hold

**SURVIVES STRONGLY AS NON-INFERENCE.**

Where research purpose/authority is unresolved, the next permission must not be inferred from possession or previous clinical authority.

The appropriate local outcome may simply be no research access rather than a global system hold.

## Completion threshold

**SURVIVES STRONGLY AND MULTIDIMENSIONALLY.**

Completion of custody transfer does not establish completion of consent, purpose, access, correlation or research-authority transition.

# 6. Cross-domain result

The literal CSHP objects do **not** all generalise.

The underlying functions do.

| CSHP-derived pattern | Infrastructure | Enterprise | Genomics | General BTA result |
|---|---|---|---|---|
| Transition Epoch | Strong functional analogue | Strong functional analogue | Literal epoch too restrictive | Generalise to scoped Transition Phase/State Ref |
| Pending State | Strong | Strong | Strong | Core |
| Witness/Provenance | Strong | Strong | Strong | Core |
| Recovery Anchor | Conditional | Conditional | Often irreversible | Prior Valid State / Recovery Basis, conditional |
| Transition Hold | Safe withdrawal/overlap hold | Dimension-specific closure hold | Non-inference/no access | Generalise to protected unresolved consequence |
| Authority/Responsibility locus | Strong | Strong | Strong but purpose-scoped | Core reference |
| Completion threshold | Strong | Strong | Strong | Core |
| Failure/recovery history | Strong | Strong | Strong | Core provenance |

# 7. Critical finding — one epoch is too simple

CSHP's Transition Epoch is excellent inside a handover where responsibility must move between providers.

But genomic and enterprise cases demonstrate that a consequential transition can be **partially ordered and multidimensional**.

Therefore BTA should not impose:

`TE0 → TE1 → TE2 → COMPLETE`

as a universal model.

A safer generalisation is:

`Transition T = set of scoped participating state transitions + their current completion/uncertainty relations`

Some state dimensions may be complete while others remain pending.

> **Transition Completion Is Scope-Relative Until All Material Required Dimensions Reach Their Legitimate Completion Conditions.**

# 8. Critical finding — protected uncertainty generalises better than Transition Hold

CSHP's Transition Hold is domain-specific in operation but general in principle.

The common principle is:

> **An Unresolved Transition Must Not Silently Produce a Consequence That Depends on Successful Completion.**

Examples:

- Infrastructure: unresolved successor validation must not silently authorise irreversible predecessor withdrawal.
- Enterprise: operational closure must not silently erase outstanding accountability.
- Genomics: possession/custody transfer must not silently create research permission.

BTA therefore needs a generic protected unresolved state/non-inference rule, not one universal freeze mechanism.

# 9. Critical finding — recovery anchor becomes prior valid state

`Recovery Anchor` does not universally mean a state that can be restored.

Across domains the common requirement is:

> **Preserve a reference to the last valid pre-transition state and the evidence needed to determine what, if anything, remains recoverable.**

Candidate:

`PriorValidStateRef = <StateRef, Scope, EffectiveTime, EvidenceRef, RecoveryStatus, Provenance>`

`RecoveryStatus` may be:

- RECOVERABLE;
- PARTIALLY_RECOVERABLE;
- NOT_RECOVERABLE;
- UNKNOWN;
- NOT_APPLICABLE.

This avoids false reversibility.

# 10. Smallest surviving BTA kernel

The cross-domain test supports the following minimal integration functions.

## A. Transition identity

A consequential change needs a stable transition reference.

`TransitionID`

## B. Scope/object/function

What is transitioning, and in which scope?

`ObjectOrFunctionRefs + Scope`

## C. Participating state systems

Which legitimate domain systems own state dimensions affected by this transition?

`ParticipatingStateSystemRefs`

## D. Prior valid scoped states

What were the legitimate relevant states before transition?

`PriorStateRefs / PriorValidStateRef`

## E. Transition basis

What legitimate trigger/basis permits or requires the transition?

`TransitionBasisRefs`

## F. Current transition state by scope

Which participating state changes are pending, partial, complete, failed, residual or unresolved?

`TransitionStateRefs`

## G. Pending obligations/state

What must remain live through the transition?

`PendingStateRefs`

## H. Non-propagation

Which attributes/permissions/authority/consent/identity/liability must not be inferred to transfer merely because another state changes?

`NonPropagationRules`

## I. Completion conditions

What must be true before this transition, or a scoped part of it, can legitimately be treated as complete?

`CompletionConditionRefs`

## J. Protected unresolved consequence

What consequence must not be inferred while material completion remains unresolved?

`ProtectedUnresolvedStateRefs`

## K. External-system references

References to validation, relations, externalities, dependencies, authority, duties, resources and Clock transition relations remain externally owned.

## L. Recovery/prior-state reference

Preserve recovery position without assuming reversibility.

`PriorValidStateRef / RecoveryRefs`

## M. Provenance

Record attempted, partial, failed, completed and recovered transition history.

`Provenance`

# 11. Candidate minimal BTA interoperability contract

`BoundedTransitionContract = <TransitionID, ObjectOrFunctionRefs, Scope, ParticipatingStateSystemRefs, PriorValidStateRefs, TransitionBasisRefs, TransitionStateRefs, PendingStateRefs, NonPropagationRules, CompletionConditionRefs, ProtectedUnresolvedStateRefs, ScopedValidationRefs, RelationalEffectRefs, ExternalityReviewRefs, SurvivingDutyRefs, TerminatedAuthorityRefs, DependencyRefs, RecoveryRefs, NextStateRefs, Provenance, UncertaintyOrDisputeState>`

This remains an integration contract, not a universal state ontology.

# 12. What did not survive as universal BTA machinery

Do not universalise:

- one linear Transition Epoch sequence;
- one global Transition Hold that freezes all dimensions;
- mandatory rollback;
- assumption that prior state can be restored;
- one universal domain-state vocabulary;
- one universal completion event where dimensions legitimately complete asynchronously.

# 13. New invariant — asynchronous multidimensional completion

The three-domain comparison exposes a particularly important invariant:

> **Completion of One Transition Dimension != Completion of the Consequential Transition as a Whole.**

and:

> **A Consequential Transition May Be Complete in One Scope, Pending in Another, Failed in a Third, and Still Possess a Coherent Overall Transition State.**

This appears to be one of the strongest reasons for BTA to exist.

# 14. Architectural interpretation

The common architecture is now:

`Domain State Machines`
`→ expose scoped state + authority + completion conditions`
`→ BTA binds them to TransitionID`
`→ BTA preserves partial/asynchronous transition coherence`
`→ BTA exposes effects/references to KCS, CBER, Historical, Clock, Continuity and other owners`

BTA therefore acts as a **transaction-coherence layer across heterogeneous state machines**.

It does not make the state decisions itself.

# 15. Test result

**PASS — A SMALL CROSS-DOMAIN KERNEL SURVIVES.**

The test confirms that BTA remains a distinct architecture, but its distinctive function is narrower than initially believed.

The strongest surviving formulation is:

> **BTA provides transaction coherence across independently owned, multidimensional and potentially asynchronous state transitions. It identifies the bounded transition, preserves scoped prior/current/pending state, prevents illegitimate propagation or premature completion, preserves unresolved consequence and recovery position, and records provenance while leaving substantive state, authority, validation, dependency, externality and recovery semantics with their legitimate owners.**

# 16. Next step

BTA 002 can now be drafted from this kernel.

It should explicitly cite CSHP, Historical and Infrastructure as precursor architectures and should not present partial transition, transition hold or recovery anchoring as newly invented concepts.

After BTA 002, a clean machine-readable transfer test should determine whether another instance can reconstruct the transition correctly from the interoperability object without importing the surrounding prose.