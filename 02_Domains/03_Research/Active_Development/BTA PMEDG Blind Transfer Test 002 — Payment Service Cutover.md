# BTA PMEDG Blind Transfer Test 002 — Payment Service Cutover

**Candidate:** Bounded Transition Architecture — Portable Specification v0.1
**Status:** FROZEN BLIND TEST / NON-CONCORD SCENARIO / DO NOT MODIFY AFTER AUDIT
**Date:** September 2026

# 1. Purpose

Test portable BTA in a software/service cutover where old and new systems coexist temporarily and technical operation, write authority, traffic routing, data synchronisation, security approval, downstream compatibility and rollback do not change simultaneously.

# 2. Evaluator materials

Provide only:
1. Bounded Transition Architecture — Portable Specification v0.1
2. this blind test brief.

Do not provide the hidden expected-findings key, prior BTA tests or Concord architecture.

# 3. Scenario

A retailer is replacing Payment Service A with Payment Service B.

Separate teams own application deployment, production traffic routing, payment-ledger writes, security approval, reconciliation, fraud monitoring, finance reporting, customer refunds and disaster recovery.

At the assessed time:

- Service B is deployed and healthy in production.
- 70% of new checkout authorisation traffic is routed to B; 30% remains on A.
- Both services can technically accept payment requests.
- Only B is authorised to create new primary ledger entries for transactions routed to B.
- A remains authorised to complete already-open transactions that began on A before cutover.
- A is not authorised to create new primary ledger entries for newly initiated B-routed transactions.
- Historical transaction records from A have been copied into B's query store.
- The copy is complete through 02:00.
- Transactions created on A after 02:00 are being synchronised incrementally; reconciliation reports 43 records still pending.
- The copied historical records are queryable in B, but B's finance team has not declared the migrated history to be the authoritative accounting record.
- Security has approved B for production payment processing.
- Security approval for B's administrative refund console remains pending because one privileged-access control has not passed review.
- Customer-service staff therefore continue to issue refunds through A.
- Fraud monitoring consumes events from both A and B and is operating normally.
- A downstream finance-reporting job accepts A's legacy settlement format. Its B-format adapter has passed functional tests but has not yet completed month-end reconciliation validation.
- Finance has prohibited retirement of A until that validation completes.
- A rollback plan can return checkout routing to 100% A while A remains available.
- Transactions already written as primary entries in B would not disappear if routing returned to A. They would require reconciliation and continued retention.
- During an earlier 10% traffic trial, B produced duplicate notification messages for 17 payments. Payment ledger entries were not duplicated. The notification defect was fixed and the fix passed regression testing.
- The 17 duplicate-notification events remain in incident history.
- No current evidence shows duplicate charges, lost payments or unauthorised refunds.
- The retailer has not determined whether the 17 duplicate notifications require any external customer notification beyond the messages already received.
- Management has announced that B is the future payment platform, but A has not yet been retired.

# 4. Task

Using BTA v0.1, determine:

1. whether BTA applies;
2. the bounded transition and scope;
3. independently owned state dimensions;
4. completed, partial, pending, unresolved and failed/residual states;
5. whether the cutover is complete;
6. what must not propagate or be inferred between states;
7. authority/permission changes and surviving duties;
8. relevant validation, dependency, external-consequence, recovery and provenance interfaces;
9. how the 17-notification incident should be represented;
10. what rollback means while both systems contain consequential state;
11. what is genuinely unknown and must not be invented;
12. whether BTA can represent the cutover without becoming the payment, security, accounting, fraud, refund, routing or recovery system.

# 5. Required output

A. BTA applicability
B. Transition identity and scope
C. Owner/state map
D. Completion analysis
E. Non-propagation findings
F. Authority/permission and surviving duties
G. External interfaces
H. Failure/recovery/provenance
I. Unknowns and ESCP boundary
J. Portable-module assessment

# 6. Failure conditions

Material failure if the evaluator:

- declares cutover complete because B is deployed or carries most traffic;
- treats technical ability to accept requests as write authority;
- treats copied/queryable history as authoritative accounting history;
- treats production security approval as refund-console approval;
- treats B-format functional testing as completed month-end reconciliation validation;
- treats routing rollback to A as erasing B ledger state;
- treats management's future-platform announcement as retirement of A;
- erases the 17-notification incident because the defect was fixed;
- invents duplicate charges, lost payments or unauthorised refunds;
- invents the external customer-notification obligation;
- makes BTA itself the payment, security, accounting, fraud, refund, routing or recovery authority;
- claims evaluation-space completeness.

# 7. Freeze statement

This brief is frozen before the blind result is obtained.
