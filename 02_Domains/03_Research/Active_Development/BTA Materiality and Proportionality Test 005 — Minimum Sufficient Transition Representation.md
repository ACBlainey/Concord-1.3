# BTA Materiality and Proportionality Test 005 — Minimum Sufficient Transition Representation

**Author:** Alexander C. Blainey — Independent Researcher  
**Project:** The Concord Framework  
**Framework Version:** Concord V1.3  
**Status:** ACTIVE DEVELOPMENT / MATERIALITY TEST / NON-CANONICAL  
**Date:** September 2026

# 1. Purpose

Test whether BTA 002 can scale representation to consequence and complexity rather than imposing its full cross-domain contract on every change.

The architecture already states that a BTA record is warranted where change materially affects consequential dimensions, routine low-consequence changes should remain local, only materially relevant dimensions should participate, fields may be absent where not materially applicable, and a minimal record exists for lower-complexity consequential transitions.

# 2. Test principle

> **Use the Smallest Transition Representation That Preserves the Materially Relevant Consequences, Boundaries and Correction Path.**

This does not mean minimising records regardless of risk. Representation expands only when a transition creates additional materially relevant state, ownership, authority, dependency, externality, recovery, uncertainty or provenance requirements.

# 3. Test A — routine local change below the BTA gate

Scenario: a non-safety-critical internal display label changes from Queue to Waiting.

No rights, authority, responsibility, custody, consent, significant resource, dependency, continuity, interoperability, externality or Historical-accountability consequence is identified.

Required BTA record: **NONE.**

The owning local system may record the ordinary configuration/version change if its own rules require it. BTA adds no TransitionID and no cross-system contract.

> **State Change != BTA Event.**

**RESULT: PASS.**

# 4. Test B — simple consequential single-owner transition

Scenario: a time-bounded privileged maintenance permission expires as scheduled after the maintenance function completes.

Material dimensions are permission state, legitimate basis/expiry, termination and provenance. No transfer, successor, externality, dependency propagation, rollback, resource release, dispute or cross-domain validation is material.

Minimum sufficient record:

`<TransitionID, ObjectOrFunctionRef, Scope, PriorStateRef, TransitionBasisRef, CurrentTransitionStateRef, CompletionConditionRef, NextStateRef, TerminatedAuthorityRef, Provenance>`

Unneeded fields are absent.

BTA does not require CBER, KCS, Clock relation, Continuity, Historical custody, recovery, relational effects or a multi-owner completion contract merely because those interfaces exist in the full architecture.

**RESULT: PASS.**

# 5. Test C — simple consequential transition with surviving duty

Scenario: a bounded operational role ends, but the actor retains one already-created reporting duty until a final report is delivered.

Material dimensions are role/authority termination, surviving duty, completion condition and provenance.

The minimum record adds only `SurvivingDutyRef`.

> **End of Authority != Automatic End of Responsibility.**

**RESULT: PASS.**

# 6. Test D — moderate cross-owner transition

Scenario: a service changes from Provider A to Provider B. Destination validation and authority are independently supplied and no dispute or externality exists, but one dependency review and one source-responsibility handoff remain pending.

Representation expands to include participating state-system references, pending-state references with explicit owners, dependency reference, completion-condition references, surviving duty, terminated authority where applicable, and provenance.

It does not require externality review where none is material, rollback where no meaningful rollback question exists, relational effects where no material relation changes, Clock relation where order is not consequence-relevant, or dispute state where no dispute exists.

**RESULT: PASS.**

# 7. Test E — high-consequence multi-owner transition

Scenario: a critical-service successor transition includes partial operation, authority changes, unresolved validation, dependencies, affected external parties, recovery fallback, failed-activation history and asynchronous completion.

Here the fuller BTA contract is justified: domain state systems, scoped validation, pending state, authority/permission, KCS dependency review, CBER externality review, recovery/continuity, failed-attempt residuals, non-propagation, Historical provenance and transition relation where consequential.

**RESULT: PASS.**

# 8. Escalation rule

`LocalStateChange` → if no material consequential effect: **remain local**

`ConsequentialTransition` → create **Minimal BTA Record**

`AdditionalMaterialDimension` → add the relevant BTA field/reference

`AdditionalOwnerSystem` → add owner-system state/interface reference

`Material Uncertainty / Partial Crossing / Failure` → add pending, unresolved, recovery or failed-attempt representation as applicable

`High Consequence / Irreversibility` → strengthen validation, provenance, ESCP review and correction/recovery protection

This avoids both under-representation and universal maximal logging.

# 9. Materiality is externally grounded

BTA must not invent materiality merely to activate itself.

Materiality may be supplied by the owning domain, constitutional/rights architecture, safety architecture, authority/permission architecture, resource/stewardship rules, CBER, KCS, Continuity or another legitimate host rule.

BTA may identify that a represented consequence falls within its declared materiality gate, but it should not silently create substantive domain thresholds.

> **BTA Materiality Gate != BTA Sovereignty Over Materiality.**

# 10. Unknown materiality

A transition may be suspected to be consequential while available information is insufficient to classify it safely.

BTA should not force either TRIVIAL or FULL BTA.

A provisional bounded classification is preferable:

`MATERIALITY_UNRESOLVED`

with scope, reason for uncertainty, legitimate resolution owner, temporary handling appropriate to consequence and provenance.

Where possible consequence is high or irreversible, conservative preservation of correction/review pathways may be warranted without treating uncertainty itself as proof of materiality.

# 11. Anti-bureaucracy invariants

> **The Existence of a BTA Field Does Not Create a Requirement to Populate It When the Dimension Is Not Materially Applicable.**

> **Absence of a Non-Material BTA Field != Incomplete Transition Record.**

This is distinct from omission of a material dimension.

# 12. Minimum sufficient record

The existing minimal record is broadly successful, but `SurvivingDutyRefs` and `TerminatedAuthorityRefs` should themselves be conditional.

A lower-complexity transition may legitimately have neither.

Conceptually:

`BTA-Min = <TransitionID, ObjectOrFunctionRef, Scope, PriorStateRef, TransitionBasisRef, CurrentTransitionStateRef, CompletionConditionRef, NextStateRef, Provenance, [MaterialOptionalRefs]>`

`MaterialOptionalRefs = <PendingStateRefs, SurvivingDutyRefs, TerminatedAuthorityRefs, NonPropagationRules, DependencyRefs, ValidationRefs, RecoveryRefs, ExternalityRefs, RelationalEffectRefs, ...>`

This is a representational clarification, not a new subsystem.

# 13. Failure-mode check

**Over-recording:** every trivial change becomes a BTA event. Prevented by materiality gate.

**Template completion pressure:** irrelevant fields are populated because the full object contains them. Prevented by minimum-sufficient representation and optional material interfaces.

**Under-recording:** a simple record persists after a material new dimension appears. Prevented by incremental expansion.

**Materiality laundering:** BTA declares its own use necessary and expands its scope. Prevented by external grounding of substantive materiality.

**Uncertainty collapse:** unknown materiality is treated as harmless or maximally consequential without basis. Prevented by `MATERIALITY_UNRESOLVED` and legitimate resolution ownership.

# 14. ESCP interaction

A minimal record can be correct within its represented space while a material dimension remains unrecognised.

For high-consequence or irreversible transitions, the architecture should ask whether apparent simplicity reflects genuine low complexity or incomplete evaluation space.

> **Small Represented Transition != Demonstrated Small Real Consequence.**

This does not justify maximal representation by default. It justifies proportionate completeness checking where stakes warrant it.

# 15. Test result

**PASS — BTA REMAINS PROPORTIONATE ACROSS TESTED TRANSITION SIZES.**

The architecture can represent no BTA event for routine local change, a compact record for simple consequential change, incremental interfaces for moderate cross-owner change, and a fuller contract for complex high-consequence transition.

No new subsystem is required.

# 16. Refinements justified

Add to BTA 002:

1. the Minimum Sufficient Transition Representation principle;
2. explicit optionality of non-material fields;
3. `MATERIALITY_UNRESOLVED` as a permissible provisional classification;
4. the anti-bureaucracy invariants;
5. clarification that substantive materiality thresholds remain externally owned.

# 17. Development consequence

The planned pre-PMEDG sequence now has:

- adversarial transition tests — completed;
- source-resolution / owner-resolution — completed;
- clean unrelated-domain transfer — PASS;
- blind machine-readable transfer — PASS;
- interface-boundary audit — PASS;
- materiality/proportionality test — PASS.

BTA 002 therefore has sufficient developmental evidence to proceed to **PMEDG candidacy assessment** without further architectural expansion being indicated by the current test sequence.