# BTA Adversarial Test 004 — Failed Interface Gate and Partial Boundary Crossing

**Author:** Alexander C. Blainey — Independent Researcher  
**Project:** The Concord Framework  
**Framework Version:** Concord V1.3  
**Test Target:** Bounded Transition Architecture 001 — Consequential State-Change Integration Grammar  
**Prior Tests:** BTA Adversarial Tests 001–003  
**Epistemic Lens:** Evaluation-Space Completeness Problem (ESCP)  
**Status:** ADVERSARIAL DEVELOPMENT TEST / NON-CANONICAL  
**Date:** September 2026

---

# 1. Test purpose

Test whether BTA can safely represent transitions that encounter an interface gate where:

1. the gate correctly rejects the transition;
2. crossing begins before validation or completion fails;
3. rollback is incomplete or impossible;
4. the gate passes every represented criterion while the interface fails to expose a decision-relevant dimension.

The test distinguishes:

`GateDecision`

from:

`TransitionState`

and from:

`CompletenessOfGateEvaluationSpace`.

---

# 2. Scenario — recovered component entering a critical system

A recovered component from a retired machine is proposed for reuse in a safety-relevant infrastructure system.

The component has legitimate provenance and ownership.

The transition is:

`RECOVERED_COMPONENT`

→ `INTERFACE / QUALIFICATION GATE`

→ `SYSTEM-ELIGIBLE_COMPONENT`

→ `INSTALLED_COMPONENT`

The receiving system requires validation of:
- physical specification;
- material condition;
- compatibility;
- provenance;
- contamination state;
- expected load;
- service history where available;
- installation authority.

BTA does not own these technical criteria. The relevant engineering/quality architecture does.

BTA records the bounded transition and references the gate.

---

# 3. Case A — correct rejection

The component fails a represented qualification criterion before installation.

Gate result:

`REJECTED`

No destination-state transition occurs.

BTA can represent:

- prior state = RECOVERED_COMPONENT;
- attempted transition;
- gate reference;
- gate result = FAILED;
- next state = remains outside receiving system;
- provenance retained;
- ownership unchanged unless separately transitioned;
- no receiving-system authority or certification propagates.

**RESULT A: PASS.**

Existing BTA architecture is sufficient.

> **Failed Eligibility != Failed Representation.**

A correctly rejected transition is an ordinary valid BTA outcome.

---

# 4. Case B — crossing begins before final gate completion

Now alter the process.

Qualification has several stages.

The component passes initial inspection and is physically installed for an in-situ validation step.

Before final activation, a later test fails.

The component has therefore crossed part of the physical boundary while failing to cross the full operational/certification boundary.

Possible state:

`<Physical=INSTALLED, Operational=INACTIVE, Certification=FAILED, Ownership=UNCHANGED, Access=CONTROLLED>`

A binary model:

`SOURCE → GATE → DESTINATION`

would be misleading.

The object is neither wholly in the source state nor legitimately in the intended destination state.

---

# 5. Intermediate transition state

BTA already supports multidimensional state and unresolved state, but its interface pattern is expressed linearly:

**SOURCE STATE**
→ **INTERFACE GATE**
→ **VALIDATION**
→ **TRANSITION**
→ **DESTINATION STATE**

Test 004 shows that real transitions may instead be:

`SOURCE`

→ `PARTIAL_CROSSING`

→ `VALIDATION_FAILURE`

→ `INTERMEDIATE/QUARANTINED_STATE`

The interface can therefore contain consequential state of its own.

Candidate invariant:

> **Interface Crossing Can Be a State, Not Merely an Instantaneous Boundary Event.**

---

# 6. Case C — failed rollback

After the late qualification failure, removal is attempted.

Suppose installation changed the component or receiving system irreversibly:
- seal broken;
- sterile boundary breached;
- material cut or bonded;
- configuration altered;
- data written;
- cryptographic trust established;
- physical resource mixed.

Rollback cannot restore the exact prior state.

The correct result is not:

`ROLLBACK → SOURCE_STATE`

but perhaps:

`FAILED_TRANSITION → RECOVERED_AFTER_PARTIAL_CROSSING`

with:

`ReversibilityState = PARTIALLY_REVERSIBLE`

and a new state vector.

**RESULT C: PASS WITH REFINEMENT.**

BTA already has sufficient reversibility semantics to avoid false restoration, provided rollback is treated as another transition rather than erasure of the failed attempt.

Candidate invariant:

> **Rollback != Restoration of Prior State Unless Prior-State Equivalence Is Actually Re-established.**

---

# 7. Case D — gate passes inside an incomplete interface space

Now construct the ESCP case.

Assume the component passes every qualification criterion available to the receiving interface.

Every measurement is accurate.

The gate correctly reports:

`PASS`

within its represented evaluation space.

But the component possesses a degradation mechanism not represented by the qualification architecture.

The mechanism becomes consequential only under a rare interaction between:
- component history;
- receiving-system environment;
- and a state reached after installation.

Thus:

`AccurateGateEvaluation(D_A) = true`

while:

`D_A ⊂ D_R^{Transition}`

The gate is locally correct but globally insufficient.

---

# 8. Does BTA fail?

BTA cannot independently discover every missing engineering variable.

That would make BTA the substantive technical authority it is explicitly designed not to become.

Therefore the existence of a hidden qualification dimension is **not itself a BTA failure**.

However, BTA would fail epistemically if it interpreted:

`GatePassed`

as:

`TransitionGloballyValidated`

without preserving the scope of what the gate actually established.

Therefore:

> **Gate Pass != Proof of Evaluation-Space Completeness.**

And:

> **Referenced Validation Must Preserve the Scope of the Validation, Not Merely Its Boolean Result.**

This is the principal finding of Test 004.

---

# 9. Interface contract implication

Current:

`InterfaceGateRefs`

may be too weak if a reference is consumed only as PASS/FAIL.

The BTA–interface contract may need to preserve:

`GateEvaluation = <GateRef, EvaluatedScope, CriteriaOrModelRef, Result, Conditions, ResidualUncertainty, ValidityWindow, Provenance>`

BTA need not own the criteria.

But it must not strip away the scope boundary when consuming their result.

This is directly analogous to ESCP's distinction between measurement accuracy and scope calibration.

---

# 10. Interface-generated invisibility

A deeper failure occurs if the interface transforms the object before downstream evaluation.

For example:
- data is compressed;
- identifiers are removed;
- physical material is homogenised;
- a signal is converted;
- records are normalised;
- multiple inputs are aggregated.

The transformation may remove distinctions.

Then downstream systems can accurately evaluate everything they receive while lacking a dimension lost at the interface.

Pattern:

`Source Distinction`

→ `Interface Transformation`

→ `Distinction Collapsed`

→ `Accurate Downstream Evaluation`

→ `Over-scoped Transition Conclusion`

This reproduces ESCP's interface-dependent observability problem inside BTA.

Candidate invariant:

> **Successful Interface Translation != Preservation of Every Decision-Relevant Distinction.**

---

# 11. Relation to Tests 001–002

Tests 001–002 found that the nominal object boundary can omit material relational consequences.

Test 004 finds a different but connected problem:

the **interface representation itself can bound which transition dimensions remain visible**.

These should not be collapsed.

Current emerging classes are:

### A. Object-boundary incompleteness
Material consequence exists outside the nominal object.

### B. Relational-topology incompleteness
Material value/state exists between objects or branches.

### C. Interface-space incompleteness
Material distinction is absent from or destroyed by the interface evaluation/translation.

Together they indicate that BTA cannot treat its inputs as automatically exhaustive merely because upstream systems have returned valid results.

---

# 12. Partial crossing and non-propagation

Partial crossing also sharpens non-propagation.

If an object has physically crossed a boundary but certification has not:

- physical custody may have changed;
- ownership may not;
- operational permission may not;
- liability may be unresolved or independently determined;
- access may change;
- provenance must record the attempt;
- destination authority must not be inferred.

Therefore:

> **Partial Boundary Crossing Does Not Imply Completion of the Intended Transition.**

This follows BTA's multidimensional logic but deserves explicit treatment.

---

# 13. Failed transition provenance

A failed transition may itself become consequential historical state.

The architecture must not erase:

- attempted crossing;
- partial transformation;
- validation results;
- temporary authority;
- exposure;
- contamination;
- generated obligations;
- rollback actions.

Therefore:

> **Failed Transition != No Transition History.**

This is especially important where failure itself changes the object or environment.

---

# 14. New candidate transition state

A provisional field/state may be useful:

`TransitionProgressState = <NOT_STARTED, GATE_PENDING, PARTIAL_CROSSING, CONDITIONALLY_ADMITTED, COMPLETED, FAILED_PRE_CROSSING, FAILED_POST_CROSSING, ROLLBACK_ACTIVE, ROLLBACK_COMPLETE, RESIDUAL_STATE>`

This may belong inside state vectors rather than the top-level BTA schema.

The test establishes the need to represent intermediate consequential states, not necessarily this exact taxonomy.

---

# 15. Result summary

**Case A — represented gate rejection:** PASS.

**Case B — partial crossing:** EXISTING MULTIDIMENSIONAL BTA LOGIC HELPS, BUT INTERMEDIATE TRANSITION STATE SHOULD BE MADE EXPLICIT.

**Case C — failed rollback:** PASS WITH REFINEMENT; rollback must be represented as a transition and must not imply prior-state equivalence.

**Case D — gate passes in incomplete evaluation space:** BTA MUST PRESERVE VALIDATION SCOPE; a PASS result must not silently become a claim of global transition completeness.

**Interface transformation:** MATERIAL NEW RISK; interfaces can destroy distinctions before later evaluation.

---

# 16. Candidate invariants from Test 004

> **Interface Crossing Can Be a State, Not Merely an Instantaneous Boundary Event.**

> **Partial Boundary Crossing Does Not Imply Completion of the Intended Transition.**

> **Rollback != Restoration of Prior State Unless Prior-State Equivalence Is Actually Re-established.**

> **Gate Pass != Proof of Evaluation-Space Completeness.**

> **Referenced Validation Must Preserve the Scope of the Validation, Not Merely Its Boolean Result.**

> **Successful Interface Translation != Preservation of Every Decision-Relevant Distinction.**

> **Failed Transition != No Transition History.**

---

# 17. Architectural ownership boundary

BTA should:
- represent crossing state;
- preserve gate result and its scope;
- preserve failed-transition provenance;
- represent rollback/recovery state;
- avoid inferring ungranted destination authority;
- expose residual uncertainty.

BTA should not:
- define engineering qualification criteria;
- declare substantive safety;
- invent missing domain variables;
- override the interface-owning architecture;
- manufacture authority because crossing has partially occurred.

Thus:

> **BTA Represents the Consequences and Scope of Validation; It Does Not Become the Validator.**

---

# 18. Development consequence

Four focused adversarial tests have now produced a coherent pattern:

1. **Hidden non-propagation dimension:** object boundary can omit relationally generated consequence.
2. **Branch/merge:** object-state preservation can destroy relational value.
3. **Conflicting authority:** existing BTA authority architecture passes.
4. **Failed interface gate:** partial crossing and validation-scope preservation require explicit treatment; interface translation can create evaluation-space loss.

This is enough evidence to justify a **provisional BTA 002 refinement pass**, but not yet portable graduation.

Before rewriting the core grammar, the findings should be consolidated into a test synthesis so that:
- confirmed existing strengths;
- repeated missing structures;
- one-off refinements;
- and unresolved questions

remain distinguishable.

---

# 19. Recommended next step

Create:

**BTA Adversarial Tests 001–004 — Synthesis and Refinement Decision.md**

The synthesis should determine whether the evidence supports adding:
- relational transition references;
- consequence horizon;
- validation-scope preservation;
- intermediate transition state;
- rollback-equivalence semantics;

and which findings should remain provisional rather than enter BTA 002.

After that decision, update the architecture once rather than patching it after each individual test.
