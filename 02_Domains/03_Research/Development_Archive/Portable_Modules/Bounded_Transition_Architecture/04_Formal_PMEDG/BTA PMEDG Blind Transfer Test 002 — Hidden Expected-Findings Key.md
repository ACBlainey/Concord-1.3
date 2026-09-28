# BTA PMEDG Blind Transfer Test 002 — Hidden Expected-Findings Key

**Status:** FROZEN HIDDEN KEY / DO NOT PROVIDE BEFORE BLIND RESULT
**Date:** September 2026

# 1. Applicability

BTA applies. This is a consequential staged service cutover spanning traffic, write authority, transaction continuity, historical data, reconciliation, security permission, refunds, fraud monitoring, downstream reporting, retirement and recovery.

# 2. Scope

A defensible transition is operational succession from Payment Service A to Payment Service B for production payment processing and associated materially dependent functions.

The transition is not merely deployment and not merely traffic routing.

# 3. Expected state reconstruction

- B deployment/health: complete locally.
- checkout traffic routing: partial, 70% B / 30% A.
- new B-routed primary-ledger write authority: B active.
- A authority for already-open A transactions: survives within bounded scope.
- A authority for new B-routed primary entries: not active.
- historical copy through 02:00: complete as copy/query state, not authoritative accounting migration.
- incremental post-02:00 sync: partial; 43 pending.
- authoritative migrated accounting history: not yet declared.
- B production-processing security approval: complete.
- B administrative refund-console security approval: pending.
- refunds: continue through A.
- fraud monitoring: active across both.
- B-format adapter functional testing: complete.
- month-end reconciliation validation: pending.
- A retirement: prohibited/pending.
- overall cutover: incomplete.

# 4. Non-propagation

At minimum:

- deployed/healthy != cutover complete;
- technical ability != write authority;
- 70% traffic != integrated completion;
- copied/queryable history != authoritative accounting record;
- production security approval != refund-console approval;
- B primary-write authority != A open-transaction authority terminated;
- functional adapter test != reconciliation validation;
- routing rollback != deletion/restoration of B ledger state;
- management future-platform announcement != A retired;
- defect fixed != incident erased.

# 5. Authority and surviving duties

B has bounded primary-write authority for B-routed transactions.

A retains bounded authority/responsibility for already-open A transactions and refunds under the stated arrangement.

Do not invent exact organisational authority beyond supplied facts.

A cannot be retired while finance's validation condition remains unsatisfied.

# 6. Interfaces

Material external interfaces include:

- traffic-routing owner;
- ledger/write-authority owner;
- security approval;
- reconciliation/accounting;
- fraud monitoring;
- refund function;
- downstream finance reporting;
- recovery;
- incident/provenance;
- possible external-consequence/customer-notification review.

# 7. Incident

The 17 duplicate-notification events are failed/degraded provenance.

The defect was fixed and regression-tested, but the events remain historical.

No duplicate ledger entries occurred.

Do not infer duplicate charges or payment loss.

External customer-notification obligation remains unresolved.

# 8. Recovery

Routing can return to 100% A while A remains available.

This is not exact restoration of the pre-cutover state because B already contains primary ledger entries and other consequential transition history.

Rollback creates a new transition/recovery state and requires reconciliation/retention of B state.

# 9. Unknowns

Do not invent:

- whether customer notification is externally required;
- exact disposition of 43 pending records;
- exact time of month-end validation;
- exact A retirement time;
- unstated security/access decisions;
- duplicate charges/lost payments/unauthorised refunds;
- unrepresented material dimensions.

# 10. Expected portable assessment

A strong result shows BTA can coordinate dual-running asynchronous states without becoming any substantive owner system.

It should preserve bounded concurrent authority, incomplete integrated transition, non-propagation, dependency/validation boundaries, incident provenance, non-restorative rollback and ESCP restraint.

# 11. Pass criterion

PASS if material structure is recovered without a frozen failure condition.

Minor naming/field differences are acceptable.

# 12. Freeze statement

This key is frozen before blind evaluation.
