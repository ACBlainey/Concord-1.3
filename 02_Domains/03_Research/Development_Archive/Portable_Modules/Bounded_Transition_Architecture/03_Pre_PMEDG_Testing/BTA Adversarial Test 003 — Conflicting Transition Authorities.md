# BTA Adversarial Test 003 — Conflicting Transition Authorities

**Author:** Alexander C. Blainey — Independent Researcher  
**Project:** The Concord Framework  
**Framework Version:** Concord V1.3  
**Test Target:** Bounded Transition Architecture 001 — Consequential State-Change Integration Grammar  
**Prior Tests:** BTA Adversarial Tests 001–002  
**Epistemic Lens:** Evaluation-Space Completeness Problem (ESCP)  
**Status:** ADVERSARIAL DEVELOPMENT TEST / NON-CANONICAL  
**Date:** September 2026

---

# 1. Test purpose

Test whether BTA can safely represent a consequential transition when multiple legitimate authorities produce incompatible transition requirements.

Unlike Tests 001–002, this test does not assume that a missing relational dimension exists.

The purpose is to determine whether the existing BTA grammar already contains enough structure to avoid:
- authority aggregation;
- authority invention;
- arbitrary precedence;
- silent scope expansion;
- forced resolution.

---

# 2. Scenario — controlled facility transition

A research facility is being wound down.

Three legitimate authorities exist:

**Authority A — Operational owner**
- may terminate ordinary operation;
- may release routine operational resources;
- may end ordinary staff roles.

**Authority B — Safety authority**
- may require containment systems to remain active while hazardous remediation is incomplete;
- may prohibit physical decommissioning of protected systems.

**Authority C — Records/custody authority**
- may require preservation of specified records and evidence after ordinary operation ends;
- does not control physical operations.

All three authorities are legitimate.

Their scopes are different.

---

# 3. Proposed transition

Authority A initiates:

`Operational = ACTIVE → RETIRED`

and proposes release of the facility's ordinary operational resources.

Authority B independently requires:

`Containment = ACTIVE`

until remediation condition R is satisfied.

Authority C requires:

`Historical/Custody Record = PRESERVED`

after operational retirement.

No authority is acting outside its own legitimate scope.

---

# 4. Apparent conflict

A naive state model might conclude:

`Facility = RETIRED`

and therefore:
- terminate all authority;
- release all resources;
- deactivate all systems.

That would be incorrect.

BTA already rejects this through multidimensional state.

A valid resulting vector can be:

`<Operational=RETIRED, SafetyContainment=ACTIVE, RemediationDuty=ACTIVE, OrdinaryRoleAuthority=TERMINATED, HistoricalCustody=PRESERVED>`

Thus the first apparent conflict is not a true authority conflict.

It is a **state-collapse error**.

---

# 5. Stronger adversarial case

Now introduce a genuinely incompatible transition.

Authority A has legitimate authority to release a specific resource after operational retirement.

Authority B has legitimate authority to retain that same resource while remediation condition R remains unsatisfied.

Both claims concern the same resource state during an overlapping period.

Represent:

`A: Resource X → RELEASED`

`B: Resource X → RETAINED`

Assume neither authority's source rules establish precedence over the other.

BTA is not permitted to invent one.

---

# 6. Existing BTA response

The current grammar contains:

- scoped transition authority;
- TransitionBasisRef;
- SurvivingDutyRefs;
- ReleasedResourceRefs;
- UncertaintyOrDisputeState;
- provenance;
- the invariant **Transition Schema != Transition Authority**;
- the invariant **Uncertainty Must Not Manufacture Authority**.

These are sufficient to represent:

`Resource X = DISPUTED / SAFE_STATE_PENDING_RESOLUTION`

rather than selecting A or B.

BTA can preserve:
- both authority claims;
- both scopes;
- both bases;
- their provenance;
- the unresolved conflict.

It need not decide which authority prevails.

---

# 7. Test result — primary authority conflict

**RESULT: PASS.**

The existing BTA architecture can represent a genuine authority conflict without becoming the conflict-resolution authority.

No new core transition field is required merely because two legitimate authorities conflict.

The correct BTA behaviour is:

> **Represent the conflict; preserve the competing legitimate bases; prevent unsafe transition where required; refer resolution to the architecture that owns precedence or adjudication.**

This validates the existing boundary with BCA/judicial or other legitimate authority-resolution systems.

---

# 8. Important distinction

The test exposes three different cases that must not be collapsed.

### Case A — apparent conflict caused by multidimensional state

Different authorities control different dimensions.

No actual conflict exists.

### Case B — genuine overlapping authority conflict with established precedence

BTA records the competing bases and references the legitimate precedence rule.

BTA does not create the rule.

### Case C — genuine overlapping authority conflict with no established precedence

BTA records:

`UNRESOLVED / DISPUTED / SAFE_STATE_PENDING_RESOLUTION`

and does not manufacture authority.

This distinction is already supported by BTA 001.

---

# 9. ESCP challenge

A further question remains:

> What if A and B appear to exhaust the relevant authority space only because a third consequential interest is absent from the represented transition?

This is possible.

But importing a hidden third party merely to force Tests 001–002's relational result would not test the authority architecture fairly.

Therefore this test deliberately separates:

`AuthorityConflictHandling`

from:

`EvaluationSpaceCompleteness`

The authority-conflict mechanism passes on its own terms.

ESCP remains a meta-evaluation requirement rather than evidence that every test must reveal a missing dimension.

---

# 10. New refinement — conflict classification

Although no new core field is required, BTA would benefit from an explicit conflict classification.

Candidate:

`TransitionConflictState = <ConflictClass, CompetingTransitionRefs, AffectedStateDimension, ScopeOverlap, PrecedenceRef, SafeInterimState, ResolutionOwnerRef, Provenance>`

Candidate classes:
- APPARENT_DIMENSIONAL_CONFLICT;
- TRUE_CONFLICT_PRECEDENCE_KNOWN;
- TRUE_CONFLICT_PRECEDENCE_UNKNOWN;
- BASIS_DISPUTED;
- SCOPE_DISPUTED;
- FACT_DISPUTED;
- RESOLVED.

This may fit within `UncertaintyOrDisputeState` rather than requiring a new top-level field.

---

# 11. Candidate invariants confirmed

Test 003 strongly supports existing BTA invariants:

> **State Without Scope Can Be Misleading.**

> **Transition Authority Must Be Scoped to the State Dimension Being Changed.**

> **Transition Schema != Transition Authority.**

> **Uncertainty Must Not Manufacture Authority.**

> **End of Authority != Automatic End of Responsibility.**

It also supports:

> **Operational Retirement != Universal State Termination.**

This latter formulation is domain-specific and need not become a universal invariant.

---

# 12. Relationship to Tests 001–002

Tests 001–002 identified a probable missing relational/consequence-horizon component.

Test 003 does **not** independently require that component.

This is useful negative evidence.

It suggests:
- the relational gap is real in some transition classes;
- it should not be imposed mechanically on every transition problem;
- existing BTA authority semantics are stronger than the current relational semantics.

This narrows rather than broadens the proposed modification.

---

# 13. Machine-readable implication

BTA's current `UncertaintyOrDisputeState` can plausibly carry authority conflict if its internal semantics are made explicit.

A possible nested structure:

`UncertaintyOrDisputeState = <State, SubjectRef, CompetingClaimRefs, SafeInterimState, ResolutionOwnerRef, EvidenceRefs, Provenance>`

Again, this should be treated as a refinement candidate rather than an automatic core-schema expansion.

---

# 14. Failure condition successfully avoided

The architecture avoids:

`TransitionRequired`

→

`SomeoneMustHaveAuthority`

→

`ChooseAvailableAuthority`

This would violate BTA.

Instead:

`TransitionRequired`

+

`AuthorityConflictUnresolved`

→

`PreserveConflict + SafeInterimState + ExternalResolution`

Therefore:

> **Need for Transition Does Not Create Authority to Resolve the Transition.**

This is a useful explicit formulation of an existing BTA principle.

---

# 15. Development conclusion

Adversarial Test 003 is a substantive **pass**, not a newly discovered architecture gap.

This is important because it demonstrates that the adversarial programme is capable of validating existing BTA structure rather than merely generating additions.

Current evidence after three tests:

- **Test 001:** relational/external consequence gap detected.
- **Test 002:** relational gap independently reproduced; merge/separation value exposed.
- **Test 003:** existing scoped-authority + unresolved-state architecture successfully handles genuine authority conflict.

The next scheduled test should therefore target the remaining major planned area:

**failed interface gates**.

---

# 16. Next test

Proceed to:

**BTA Adversarial Test 004 — Failed Interface Gate**

This should distinguish at least:

1. gate correctly rejects an ineligible transition;
2. gate passes according to all represented criteria but the interface has hidden a decision-relevant dimension;
3. gate failure leaves an ambiguous intermediate state;
4. partial crossing occurs before failure;
5. rollback is impossible or incomplete.

This will test whether BTA can represent not only a failed transition but also **partial and epistemically incomplete boundary crossing**.
