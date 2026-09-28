# BTA PMEDG Cross-Test Convergence 001

**Candidate:** Bounded Transition Architecture — Portable Specification v0.1
**Method:** PMEDG v1.2 — Stage 10 Cross-Test Convergence
**Status:** FORMAL CROSS-TEST CONVERGENCE / NON-CANONICAL
**Date:** September 2026

# 1. Evidence compared

Blind Transfer Test 001:
Museum collection relocation.

Blind Transfer Test 002:
Payment service cutover.

The domains are materially different. Test 001 primarily pressures physical movement, custody, conservation, display permission, insurance and partial physical crossing. Test 002 pressures dual-running services, concurrent bounded authority, data synchronisation, security scopes, accounting authority, downstream validation and non-restorative software rollback.

# 2. Core mechanism survival

The same BTA kernel survived both tests:

- stable bounded transition identity and scope;
- independently owned state dimensions;
- asynchronous completion;
- explicit pending/partial/unresolved state;
- non-propagation between consequential dimensions;
- externally owned authority and validation;
- surviving duties;
- failed-event provenance;
- non-restorative rollback/recovery;
- minimum sufficient representation;
- owner-system non-absorption;
- ESCP boundary.

**Finding: STRONG CONVERGENCE.**

# 3. Completion semantics

Test 001:
Most objects had physically moved, but custody, conservation, display and insurance dimensions remained incomplete.

Test 002:
The new service was deployed and carried most traffic, but synchronisation, accounting authority, refund security, downstream finance validation and retirement remained incomplete.

Both independent evaluations rejected local-majority completion as integrated completion.

**Converged invariant:**

> **Local or Majority Completion != Integrated Transition Completion.**

This is already represented by BTA v0.1 principles and does not require a new primitive.

# 4. Non-propagation

Test 001 independently preserved:

- arrival != custody;
- custody != title;
- prior display approval != destination display approval;
- store commissioning != object clearance;
- transit cover != permanent cover.

Test 002 independently preserved:

- technical capability != write authority;
- copied/queryable data != authoritative accounting state;
- production security approval != refund-console approval;
- functional testing != reconciliation validation;
- management intent != retirement.

The mechanism therefore transfers beyond any one domain-specific attribute type.

**Finding: STRONG CONVERGENCE.**

# 5. Owner-system boundaries

In both tests the evaluator explicitly refused to make BTA the substantive owner.

Museum:
BTA did not become conservation, custody, access, display, insurance, title, catalogue or recovery authority.

Payment:
BTA did not become payment, security, accounting, fraud, refund, routing or recovery authority.

This directly supports the portable owner-interface model.

**Finding: STRONG CONVERGENCE.**

# 6. Authority discipline

Test 001 exercised authority non-transfer across physical movement.

Test 002 additionally exercised concurrent bounded authority: B legitimately held new B-routed write authority while A retained bounded authority/responsibility for already-open A transactions and current refund operations.

The second domain therefore broadened rather than merely repeated the first authority test.

BTA represented coexistence without forcing singular ownership or manufacturing authority.

**Finding: STRONG CONVERGENCE.**

# 7. Failure provenance

Test 001:
A repaired transport-vehicle fault remained provenance despite no object being aboard.

Test 002:
A fixed duplicate-notification defect remained incident history despite no duplicate ledger entries.

Both evaluators preserved failed/degraded events without inventing consequences.

**Finding: STRONG CONVERGENCE.**

# 8. Recovery and rollback

Test 001:
Some unmoved objects retained a true prior-state recovery path, while moved objects could not simply be restored to the exact pre-transition state.

Test 002:
Traffic could return to the old service, but new-system ledger entries and transition history would remain.

Both independently preserved:

> **Rollback != Restoration Unless Prior-State Equivalence Is Actually Re-established.**

**Finding: STRONG CONVERGENCE.**

# 9. ESCP discipline

Both evaluations preserved unknowns and refused to treat a coherent BTA representation as proof that every materially relevant dimension had been represented.

Neither used ESCP as a reason to declare the transition failed merely because unknown dimensions might exist.

**Finding: STRONG CONVERGENCE.**

# 10. Specification stability

No bounded revision was required after Test 001.

Test 002 therefore pressured the same unchanged Portable Specification v0.1.

Test 002 exposed no material missing primitive and no contradiction requiring revision.

This is stronger evidence than a second test of a modified mechanism because the same portable specification survived both domains.

**Finding: CORE STABLE.**

# 11. Domain independence

The tests differ materially in:

- physical versus digital/service objects;
- custody versus ledger/write authority;
- conservation versus security/reconciliation validation;
- insurance versus accounting/reporting dependencies;
- physical return versus traffic-routing rollback;
- sequential physical crossing versus dual-running concurrent operation.

Success therefore does not appear to depend on the museum scenario's domain structure.

**Finding: MATERIAL DOMAIN DIVERSITY ACHIEVED.**

# 12. Remaining issues

No unresolved architectural issue currently requires a new BTA primitive.

Remaining matters are implementation/profile questions, including:

- how a host serialises references;
- how owner identities are authenticated;
- how host-specific materiality thresholds are supplied;
- how long provenance is retained;
- how a host renders or queries transition state.

These remain host/implementation responsibilities unless future evidence shows they belong in the portable kernel.

# 13. PMEDG Stage 11 decision — is a third blind test required?

PMEDG states that a third test is not automatic.

The reasons that would justify another test are assessed as follows:

- materially new mechanism introduced after Test 002: **NO**;
- unresolved transfer risk exposed by Test 002: **NO MATERIAL RISK IDENTIFIED**;
- weak or contradictory convergence: **NO**;
- critical boundary not exercised: **NO CURRENTLY IDENTIFIED CORE BOUNDARY**;
- apparent success dependent on domain similarity: **NOT SUPPORTED; DOMAINS ARE MATERIALLY DIFFERENT**;
- graduation review has identified insufficient evidence: **NOT YET APPLICABLE**.

**DECISION: A THIRD BLIND TRANSFER TEST IS NOT CURRENTLY REQUIRED.**

This does not prohibit future testing. It means another test is not justified merely to increase test count.

# 14. Cross-test conclusion

**CROSS-TEST CONVERGENCE: STRONG.**

The same unchanged BTA v0.1 mechanism survived two materially different non-Concord blind transfer conditions.

No fundamental missing primitive was exposed.

No specification revision is currently justified.

# 15. PMEDG next step

Proceed to Stage 12:

> **Create BTA Graduation-Candidate Specification v0.3 / NOT YET RELEASED.**

The graduation candidate should preserve Portable Specification v0.1 substantively unless a mechanical consistency check identifies an actual mismatch.

Before formal Graduation Review, PMEDG section 23.3 requires the Graduation-Candidate Consistency Check.
