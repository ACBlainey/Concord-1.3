# G-05 — Executed Integration Adapter Test 066

**Date:** 11 October 2026. **Status:** locally executed illustrative Python adapter; not deployed Concord runtime or blind independent validation.

## Source contract recovery

- KCS Operational Dependency Dataset 001 defines `KDR = {ID, Source, Relation, Target, Capability, Context, Materiality, State, Failure Effect, Evidence, Confidence, Freshness}`.
- Civilisation Clock Companion Extension 001 describes `T = <type, subject, condition, evidence, owner, review-path, consequence, state>` and temporal/state/dependency/event/risk triggers. Triggering does not confer authority.
- BTA Portable Module v1.0 preserves independently owned, asynchronous transition states, non-propagation, expiry and surviving duties.
- BTA Clean Cross-Domain Test 002 already passes source-level emergency transition transfer.

## Execution

A Python 3 unittest fixture was run in the working container, with **five tests passing**:

1. Emergency activation requires an externally supplied authorisation flag and expiry occurs independently while the Clock is waiting.
2. A materially affected queued resource decision is held while an unrelated queued decision can execute.
3. Stale dependency feedback is rejected and repeat execution is idempotent.
4. Clock resumption does not resurrect expired emergency power.
5. Area A's authority does not imply authority for area B.

Console output: `Ran 5 tests ... OK`.

SHA256 of executed Python file: `5cdd68f7878aed78d7788e8922fcbd583875e7aa14a269a537a82e714d41da42`.
SHA256 of test output: `a1521b2493267fb68e5a93d2883f60d83497cdf0ebddf05d0347350377a3e7c5`.

## Boundary

This executable fixture uses simplified Python fields representing owner states, resource dependency versions, emergency expiry and pending decisions. It does **not** parse the complete BTA contract, KDR schema or Clock trigger records; nor does it validate constitutional authorisation, distributed consensus, actual network partition recovery, monotonic clock reliability, or event durability. The five passes prove only these five modeled behaviours. Do not confuse specification compatibility with deployed-system verification.

## Next stage

Construct an adapter accepting actual schema-shaped KDR, BTA and Clock trigger records, with owner-specific authority and expiry references; run invalid, missing and conflicting input tests. Preserve the already graduated BTA kernel rather than developing a competing module.

Related records: Governance G-05 059–065, KCS Companion Upgrade 001, KCS Operational Dependency Dataset 001, BTA v1.0, Civilisation Clock Companion Extension 001.
