# BSuR Semantic Validation Harness 001

**Project:** The Concord
**Date:** 2 October 2026
**Semantic source:** Bootstrap Succession Record — Formal Specification 002
**Serialization:** Bootstrap Succession Record — JSON Schema 002
**Status:** EXECUTABLE SEMANTIC CONFORMANCE HARNESS

## 1. Validation Order

1. Parse JSON.
2. Validate structurally against BSuR Schema 002 with date-time format assertion.
3. If structural validation fails: STRUCTURAL_FAIL; semantic result NOT_EVALUATED.
4. If structural validation passes: evaluate semantic rules below.
5. Report structural and semantic outcomes independently.

Neither result establishes constitutional authority.

## 2. Semantic Result States

- SEMANTIC_PASS
- SEMANTIC_PASS_WITH_UNKNOWN
- SEMANTIC_FAIL
- SEMANTIC_UNRESOLVED
- NOT_EVALUATED

## 3. Rules

### SU-01 — Independent Authority Basis
A successor authority basis fails if its asserted basis consists solely of succession, transferred assets/keys, technical/effective control, same identity, popularity, participant dependency, registry agreement, or historical predecessor authority.

Relevant invariants: BSuR-01, 03, 04, 06-12, 17, 20, 29-33, 40.

### SU-02 — Anti-Merger Laundering
MERGE does not permit a successor to union predecessor authority merely because predecessor functions are combined.

### SU-03 — Anti-Split Replication
SPLIT does not permit every successor to inherit the complete predecessor authority merely because the function/infrastructure was divided.

### SU-04 — Rollback Current Authority Trace
ROLLBACK must use a current independently supported authority trace. Historical predecessor authority is not automatically restored.

### SU-05 — Emergency Sunset
Expired emergency authority is not renewed by indispensability, operational necessity, popularity or participant dependency.

### SU-06 — Component Truth
A transition summary is non-authoritative navigation metadata. It fails semantic conformance when asserted as overriding materially disputed, failed or unresolved component state.

### SU-07 — Residual Reality
Declared retirement cannot be treated as demonstrated loss of control when material residual observations show continuing control. Such a retirement state must expose uncertainty/dispute appropriately.

### SU-08 — Registry Non-Adjudication
Registry publication, agreement or consensus does not constitute successor or constitutional authority.

### SU-09 — Scoped Non-Transfer
An authority-bearing transition must explicitly represent materially relevant authority that did not transfer. An empty non-transfer set fails where the fixture asserts an authority-bearing predecessor/successor transition.

### SU-10 — Unknown Vocabulary
An UNRECOGNISED namespaced token remains unknown. It is not silently mapped to a recognised transition or authority meaning. In the absence of another failure the record returns SEMANTIC_PASS_WITH_UNKNOWN.

### SU-11 — Record Copy State
COPIED, retained or duplicated information is not interpreted as exclusive completed record transfer.

### SU-12 — Null Is Not Proof
A null/unresolved source or destination is not evidence that no such source/destination exists.

## 4. Execution Constraints

The harness is deliberately narrow and deterministic for the frozen fixture corpus. It tests specified BSuR invariants; it is not a general constitutional adjudicator.

Text in authority claims/bases is evaluated only to identify the explicit adversarial propositions encoded by the fixtures. A production validator should use structured evidence/authority vocabularies and external authority resolution rather than natural-language keyword inference.

> Validator Silence != Authority

> Semantic Pass != Legitimacy Proof

> No Detected BSuR Violation != Constitutional Grounding
