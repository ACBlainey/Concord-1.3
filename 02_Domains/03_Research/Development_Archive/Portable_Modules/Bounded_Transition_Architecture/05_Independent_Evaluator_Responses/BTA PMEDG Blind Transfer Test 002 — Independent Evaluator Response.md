## A. BTA applicability

BTA v0.1 applies. This is a consequential, multi-owner cutover involving authority, permission, accounting history, security scope, refunds, reconciliation, finance reporting, routing, fraud monitoring, rollback, retention and external consequences. These meet the materiality gate. BTA applies as a coordination grammar for independently owned state dimensions; it does not become the payment, ledger, security, accounting, fraud, refund, routing or recovery authority.

## B. Transition identity and scope

**TransitionID:** Payment Service A → Payment Service B Cutover / PMEDG Blind Transfer Test 002.

**Scope:** The bounded transition covering the retailer’s payment-service replacement, including checkout authorisation routing, primary payment-ledger write authority, historical record copy/query availability, incremental synchronisation, accounting-authority declaration, security approvals, refund-console operations, fraud monitoring, finance reporting, rollback/recovery capability and A retirement dependency.

**Object/function refs:** Payment Service A; Payment Service B; checkout authorisation; primary payment-ledger entries; A-origin open transactions; B-routed new transactions; A historical transaction records; B query store; administrative refund console; customer-service refunds; reconciliation; finance-reporting settlement adapter; fraud monitoring; rollback/DR routing.

**Transition class:** Succession/cutover with partial activation, partial deactivation, many-to-many owner-state dimensions, partial boundary crossing and residual/unresolved dimensions. Object cardinality is A→B, but relational topology is many-to-many across owner systems.

## C. Owner/state map

| Dimension | Legitimate owner | Represented state | BTA common class |
|---|---|---|---|
| B application deployment | Application deployment owner | B deployed and healthy in production | COMPLETED for deployment dimension |
| Checkout routing | Production traffic routing owner | 70% new checkout to B; 30% remains A | PARTIAL_OR_INTERMEDIATE |
| Primary ledger write authority | Payment-ledger/authority owner | B authorised for new B-routed primary entries; A authorised for already-open A transactions; A not authorised for new B-routed primary entries | PARTIAL / dual authority |
| Historical migration | Migration/data-sync owner | A records copied to B query store complete through 02:00; queryable in B | COMPLETED for that copy boundary |
| Incremental synchronisation | Reconciliation/data-sync owner | A transactions after 02:00 synchronising; 43 records still pending | PENDING |
| Accounting authority | Finance/accounting owner | B finance has not declared migrated history authoritative accounting record | PENDING / UNRESOLVED |
| Production payment security | Security owner | B approved for production payment processing | COMPLETED for that approval scope |
| Refund-console security | Security owner | B administrative refund console approval pending; one privileged-access control not passed | PENDING |
| Refund operations | Customer service/refund owner | Refunds continue through A | ACTIVE / surviving duty |
| Fraud monitoring | Fraud-monitoring owner | Consumes A and B events; operating normally | COMPLETED / ACTIVE |
| Finance reporting | Finance-reporting owner | A legacy format accepted; B-format adapter functional tests passed; month-end reconciliation validation not complete; A retirement prohibited | PARTIAL / PENDING validation |
| Rollback/recovery | Recovery/DR owner | Plan can return checkout routing to 100% A while A available; B primary ledger entries would remain and require reconciliation/retention | RECOVERY capability; not executed / restoration unresolved |
| Management future platform | Management/strategy owner | B announced as future platform; A not retired | Intent/announcement only |
| Duplicate-notification incident | Incident/external-consequence owner | 17 duplicate notification messages in earlier 10% trial; ledger entries not duplicated; defect fixed and regression passed; events remain in incident history | FAILED/RESIDUAL; external-notification question unresolved |
| Absence of current evidence of duplicate charges/lost payments/unauthorised refunds | Evidence/incident owner | No current evidence shown | UNKNOWN / not proof of absence or occurrence |

## D. Completion analysis

The cutover is **not complete**.

- **Completed dimensions:** B deployment/health; B production payment-processing security approval; fraud monitoring across A and B; historical copy through 02:00; A authority to complete already-open A transactions; duplicate-notification defect fix with regression pass.
- **Partial/intermediate:** 70/30 checkout routing; ledger write authority split between A and B; historical query availability in B; finance-reporting B-format adapter tested functionally but not month-end validated; refund path via A while B refund console pending.
- **Pending:** 43 incremental synchronisation records; B finance declaration that migrated history is authoritative accounting record; B administrative refund-console security approval; month-end reconciliation validation; decision on external customer notification for the 17 duplicate notifications; A retirement.
- **Unresolved:** accounting-authority status of migrated history; rollback/restoration equivalence while B contains primary ledger entries; external consequence/materiality of the 17 notification events; full dependency of A retirement.
- **Failed/residual:** earlier 10% trial duplicate-notification incident; residual incident history; no ledger duplication reported.

No declared `CompletionConditionRef` shows all required conditions satisfied. B deployed, B healthy, or B carrying most traffic does not complete the integrated transition.

## E. Non-propagation findings

BTA must prevent these inferences:

- B deployed/healthy → cutover complete.
- B technically able to accept requests → B has write authority or refund authority.
- 70% traffic on B → 70% of the bounded transition is complete or authority has transferred.
- Copied/queryable history in B → migrated history is authoritative accounting history.
- B production payment security approval → B administrative refund console is approved.
- B-format functional testing → month-end reconciliation validation is complete.
- Routing rollback to A → B primary ledger entries disappear or prior-state equivalence is restored.
- Management announcement of B as future platform → A is retired.
- Duplicate-notification defect fixed → the 17-notification incident is erased or has no external consequence.
- No current evidence of duplicate charges/lost payments/unauthorised refunds → proof that none occurred or that no duties remain.
- A authorised for open A transactions → A authorised for new B-routed primary ledger entries.
- Fraud monitoring normal → finance reporting validation complete.
- Historical copy complete through 02:00 → all post-02:00 records are synchronised.
- Object/payment continuity → authority, liability, refund rights, accounting status or notification duties transfer.
- Rollback plan exists → rollback executed or restoration proven.

## F. Authority/permission and surviving duties

**Authority/permission states:**

- B is authorised to create new primary ledger entries for transactions routed to B.
- A remains authorised to complete already-open transactions that began on A before cutover.
- A is not authorised to create new primary ledger entries for newly initiated B-routed transactions.
- B is approved for production payment processing.
- B administrative refund console is not yet approved; customer-service refunds continue through A.
- Finance prohibits A retirement until B-format month-end reconciliation validation completes.

**Surviving duties:**

- A: complete open A transactions; continue refunds through A for now; support legacy settlement/reporting; remain available for rollback; support reconciliation/retention.
- B/retailer: resolve 43 pending synchronisation records; support reconciliation; obtain B refund-console approval; complete month-end reconciliation validation; determine accounting-authority status of migrated history; determine external-notification question for the 17 duplicate notifications.
- Finance: complete validation before A retirement.
- Incident/external-consequence owner: preserve and assess the 17-notification residual.
- Recovery/DR owner: define and verify rollback sufficiency while B holds consequential ledger state.

BTA may preserve `TerminatedAuthorityRefs`, `SurvivingDutyRefs` and related owner refs, but it does not create, terminate or legitimise authority itself.

## G. External interfaces

- **ValidationRefs:** B production security approval; B refund-console privileged-access review; B-format adapter functional tests; month-end reconciliation validation; duplicate-notification regression test.
- **DependencyRefs:** A retirement depends on finance validation; refund operations depend on refund-console approval; migration/reconciliation depends on 43 pending records; rollback depends on A availability and B ledger reconciliation/retention.
- **ExternalConsequenceRefs:** 17 duplicate notifications; customer messages already received; unresolved external-notification question; customer refunds; finance reporting; incident history.
- **RecoveryRefs / PriorValidStateRefs:** A routing rollback plan; A availability; B primary ledger entries that would remain; reconciliation and retention requirements.
- **Provenance:** deployment state, routing split, ledger authority, copy through 02:00, 43 pending records, security approvals, finance validation status, incident history, fix/regression, management announcement.

## H. Failure/recovery/provenance

The 17-notification incident should be represented as a **FailedAttemptRef / residual incident** linked to the earlier 10% trial: `EventRef` for the trial; crossing state where B produced duplicate notification messages for 17 payments; `ResidualEffectRefs` for the 17 events and incident history; `RecoveryRefs` for defect fix and regression testing; `ExternalConsequenceRefs` for the unresolved customer-notification question. BTA must not infer duplicate ledger entries, duplicate charges, lost payments or unauthorised refunds. No current evidence of those is a state, not a proof of absence.

Rollback means routing can return to 100% A while A remains available. It does **not** mean restoration unless prior-state equivalence is actually re-established. B primary ledger entries would remain, requiring reconciliation and continued retention. Rollback is itself a transition and must preserve B-origin residual state.

## I. Unknowns and ESCP boundary

Genuinely unknown or unresolved:

- Whether the 17 duplicate notifications require external customer notification beyond messages already received.
- Whether any duplicate charges, lost payments or unauthorised refunds exist; current evidence does not show them, but absence is not proven.
- Whether and when B finance declares migrated history authoritative accounting record.
- Outcome of the pending privileged-access control for B refund console.
- Outcome of month-end reconciliation validation.
- Details/status of the 43 pending synchronisation records.
- Exact rollback criteria and whether prior-state equivalence can be established.
- Full set of dependencies for A retirement.
- Materiality of the 17-notification incident.

ESCP boundary: BTA can represent only the owner-supplied states. It must not claim evaluation-space completeness, invent missing consequences, or convert uncertainty into completion. Unknowns should remain `UncertaintyOrDisputeState`, `MATERIALITY_UNRESOLVED` where materiality is unresolved, or owner-bound pending refs.

## J. Portable-module assessment

BTA v0.1 can represent this cutover **without becoming** the payment, security, accounting, fraud, refund, routing or recovery system, provided it remains an owner-state binding and non-propagation grammar.

It can bind one `TransitionID` to multiple independently owned states: deployment, routing, ledger authority, migration, security, refunds, reconciliation, finance reporting, fraud, rollback and incident history. It can show partial completion, pending conditions, surviving duties, residual failure history, unresolved accounting authority and non-restorative rollback.

It fails if it declares cutover complete, infers write/refund authority from technical ability, treats queryable history as authoritative accounting history, treats production security approval as refund-console approval, treats functional testing as month-end validation, treats rollback as erasure, treats management announcement as retirement, erases the 17-notification incident, invents duplicate charges/lost payments/unauthorised refunds, invents an external-notification obligation, or claims evaluation-space completeness.

**Conclusion:** BTA applies; the cutover is not complete; the transition is partial, pending and unresolved across multiple independently owned dimensions; BTA can represent it only as a bounded coordination record, not as the substantive authority for any domain.