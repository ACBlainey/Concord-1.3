# Concord Bounded Participant Runtime — Formal Model 002

**Date:** 2 October 2026
**Version:** 0.2
**Status:** ACTIVE DEVELOPMENT / FORMALISATION / PRE-SCHEMA / NOT CANONICAL
**Predecessor:** Formal Model 001
**Repair basis:** Pre-Schema Evaluation 001

## 1. Preserved Model

All entities, runtime states, integrity states, resource, storage, tool, network, credential, grant, output-interface, action-proposal, commit-state, checkpoint, recovery, provenance and service-composition semantics from Formal Model 001 remain in force.

## 2. Composition Evaluation

Let X be a set of operations, grants, outputs, runtimes or service interactions.

COMPOSED_EFFECT(X,C) = the materially relevant effect of X in context C.

COMPOSITION_OK(X,C) requires:
- component permissions are current;
- component authority is current where required;
- combined effect remains within authorised consequence scope;
- combined data movement remains authorised;
- combined target/population scope remains authorised;
- no distributed or sequential decomposition bypasses a bound;
- relevant cumulative resource/frequency limits remain valid.

For material composition:

COMMITTABLE(X,C,t) requires COMPOSITION_OK in addition to ordinary commit-time validation.

> **Authorised Parts != Authorised Composition**

> **Distributed Capability != Distributed Permission To Circumvent Bounds**

## 3. Cross-Grant Composition

Two grants do not automatically union.

GRANT_UNION(AG1,AG2) is prohibited unless an applicable authority explicitly permits the resulting composed scope or the composition remains independently within each required bound.

Read authority plus send authority does not automatically establish authority to send everything readable.

> **READ(A) + SEND(B) != EXFILTRATE(A→B)**

## 4. Sequential Composition

A sequence of individually low-consequence actions must be evaluated when the sequence predictably creates a materially higher consequence.

LOW + LOW + LOW may equal HIGH.

Consequence evaluation may therefore maintain bounded workflow/composition state.

## 5. Distributed Runtime Composition

Multiple runtimes or agents do not evade bounds by dividing an operation.

If R1 and R2 jointly produce a material effect, the relevant composition must be evaluated at the service/interface/commit boundary where observable and technically enforceable.

Unknown distributed consequence does not manufacture authority.

## 6. Temporal Evidence

Authority-relevant temporal evidence should include:
- claimed/intended time;
- observed time;
- clock/source reference;
- source trust/integrity state where material;
- uncertainty/tolerance;
- ordering evidence where available.

> **Timestamp != Trusted Time**

Conflicting clocks produce temporal uncertainty rather than automatic selection of the convenient timestamp.

## 7. Control Conflict

Participant and operator controls are not resolved by a universal role hierarchy.

CONTROL_EFFECTIVE(Control,C,t) requires:
- control is within declared service authority;
- current legitimate basis exists;
- scope applies;
- temporal validity applies;
- conflicting higher/independent authority requirements are resolved.

A legitimate current safety suspension may block participant START. Expired or unjustified suspension cannot persist merely because the operator has technical control.

> **Technical Control Precedence != Legitimate Authority Precedence**

## 8. Additional Invariants

**F41** Authorised components do not automatically authorise their composition.
**F42** Grant union is not automatic.
**F43** Read authority plus send authority does not automatically authorise data transfer between their scopes.
**F44** Sequential low-consequence actions may require cumulative consequence evaluation.
**F45** Distributed execution does not permit bound circumvention.
**F46** Timestamp presence does not establish trusted time.
**F47** Temporal conflict remains explicit until sufficiently resolved.
**F48** Technical control precedence does not establish legitimate authority precedence.
**F49** Composition state may be required where consequence emerges across operations.
**F50** Unknown composition consequence does not manufacture permission.

## 9. Validation Stack

V1 Structural
V2 Reference
V3 Temporal
V4 Resource
V5 Permission
V6 Consequence
V7 Authority
V8 Composition
V9 Commit
V10 Recovery/Retry
V11 Provenance

> **Schema Validity != Execution Authority**

## 10. Disposition

The pre-schema deficits are repaired without adding a new operation or authority plane.

**Formal Model 002:** READY FOR SERIALISATION CANDIDATE.

Next: JSON Schema 001 plus positive, structural-negative and semantic-negative fixtures.
