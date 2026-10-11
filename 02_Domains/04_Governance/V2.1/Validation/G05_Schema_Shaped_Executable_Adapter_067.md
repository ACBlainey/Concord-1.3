# G-05 — Schema-Shaped Executable Adapter 067

**Date:** 11 October 2026. **Method:** local Python 3 unittest; synthetic adapter using Concord source-shaped records, not live Concord services.

## Execution result

**8 tests passed** (`Ran 8 tests ... OK`). Executed source SHA256: `d1e6d368628019a632e9f7d30c4a534cf9bceff01289c527db99c4ef2119a7d6`. The Python source and raw test output are provided in the companion downloadable test archive from this working session.

## Tested contracts

- BTA-style transition fields: `TransitionID`, `Scope`, `TransitionBasisRefs`, with scoped owner-state and expiry references.
- KCS KDR full field set from Operational Dependency Dataset 001: ID, Source, Relation, Target, Capability, Context, Materiality, State, Failure Effect, Evidence, Confidence, Freshness.
- Clock companion trigger fields: type, subject, condition, evidence, owner, review-path, consequence, state.

The adapter deliberately uses additional fixture fields (`expires_at`, `area`, `resource`, `new_owner`) and does not claim these constitute the complete native BTA contract.

## Eight tests

1. Reject malformed transition and absent/mismatched authority references.
2. Emergency transition and expiry while Clock remains paused; review duty survives and physical resource is not automatically restored.
3. Reject replay of transition ID, time rewind, and expired activation.
4. Hold stale material dependency while unrelated queued action executes once.
5. Require fresh resource-state attestation after restoration.
6. Reject malformed KDR, wrong trigger owner, and unresolved KDR state.
7. Do not infer area B authority from area A transition.
8. Emergency events do not force Clock advancement.

## Important limits

An authority reference is not a constitutional authorisation check. The code validates only presence/scope; actual owner-system legitimacy, necessity, proportionality, renewal and jurisdiction remain unimplemented. The resource version is an illustrative local integer, not a distributed authoritative revision. The test is deterministic, in-memory and single-process. It does not validate concurrency, persistence, network partitions, time-source failure, complete BTA semantics, or deployment readiness. The adapter's check that a Clock trigger owner is `governance` is a fixture-specific assumption, not a universal Concord requirement.

**Disposition:** executable feasibility demonstrated for eight synthetic interface behaviours. Next: genuine source-format conformance and adversarial distributed-state validation, without replacing the graduated BTA or KCS modules.

**Source references:** `04_Portable_Modules/Bounded Transition Architecture — Portable Module v1.0.md`; `03_Cross_Domain_Architecture/Knowledge_Control_System/Operational_Dependency_Datasets/KCS Operational Dependency Dataset 001 — Initial Live Dependency Records and Change-Propagation Test.md`; `03_Cross_Domain_Architecture/Civilisational_Developmental_Topology/Civilisation Clock Companion Extension 001 - State Functional and Compound Trigger Architecture.md`; Governance G-05 059–066.
