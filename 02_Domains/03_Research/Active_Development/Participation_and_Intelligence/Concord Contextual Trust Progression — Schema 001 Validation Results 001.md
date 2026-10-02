# Concord Contextual Trust Progression — Schema 001 Validation Results 001

**Date:** 2 October 2026
**Target:** JSON Schema 001 + Deterministic Validator 001
**Status:** DEVELOPMENT VALIDATION / NOT IMPLEMENTATION VALIDATION

## Fixture results

| Fixture | Expected | Result |
|---|---|---|
| 001 Valid Direct ERR | PASS | PASS |
| 002 Valid Mixed ETR | PASS | PASS |
| 003 Unknown Authority Approval | FAIL | FAIL — V-ETR-07 |
| 004 Partial Without Mixed Dimensions | FAIL | FAIL — V-ETR-02/V-ETR-16 |
| 005 Corrected ERR Without Link | FAIL | FAIL — V-ERR-02 |
| 006 Projected ERR Missing Projection Fields | FAIL | FAIL — V-ERR-01 |

**6/6 expected outcomes obtained by rule inspection.**

## Important limitation

This result validates the normative fixture set against the declared deterministic rules. It is not evidence of deployed software correctness, interoperability, security, or operational performance.

The JSON Schema handles structural validation. The deterministic validator owns semantic cross-field rules that JSON Schema 001 deliberately does not attempt to encode fully.

## Result

**Schema structure:** coherent with Model 004.
**ERR/ETR separation:** preserved.
**Requiredness ambiguity:** no blocking ambiguity exposed by initial fixture set.
**Cross-field validator:** required.
**Implementation validation:** outstanding.
**Transfer validation:** outstanding.

## Next test candidates

Before PMEDG:
- add broader fixtures for non-event coverage, review failure, ended relationships, prerequisite NOT_APPLICABLE mismatch, conditional controls, recommendation projection and correction/dispute propagation;
- implement or independently reproduce deterministic validation;
- then freeze a transfer-test package if the expanded fixture set remains stable.
