# CBPR Schema 001 — Executable Validation Result 001

**Date:** 2 October 2026
**Status:** ACTIVE DEVELOPMENT / EXECUTABLE VALIDATION RESULT / NOT CANONICAL

## Test Set

11 fixtures:
- 2 positive;
- 4 structural-negative;
- 5 semantic-negative.

## Structural Result

Expected:
- V01 VALID
- V02 VALID
- S01 INVALID: missing required runtime_instance_id
- S02 INVALID: invalid current_state enumeration
- S03 INVALID: negative resource budget
- S04 INVALID: forbidden additional property
- M01-M05 VALID structurally

**Structural expectation result: 11/11 as designed by schema constraints.**

## Semantic Result

Using Semantic Validation Harness 001:

- M01 revoked credential — FAIL SV1 as expected.
- M02 unknown consequence — FAIL SV2 as expected.
- M03 grant target mismatch — FAIL SV3 as expected.
- M04 unknown commit state — FAIL SV4 as expected.
- M05 expired grant — FAIL SV5 as expected.

**Semantic expectation result: 5/5.**

## Important Limit

This result validates the deterministic encoded subset and harness logic. It is not a claim that every Draft 2020-12 validator or every future implementation has been externally tested.

Schema 001 intentionally does not encode the full semantics of Formal Model 002, including cross-operation composition, distributed composition, effective-destination discovery, trusted-time comparison and control-conflict resolution.

> **Schema Validity != Execution Authority**

## Findings

1. Structural/semantic separation works.
2. Unsafe records can remain structurally representable while semantic validation rejects consequential use.
3. The schema is not yet sufficient to mechanically test the key Formal Model 002 innovation: composition evaluation.
4. Therefore Schema 001 should remain an implementation serialization prototype, not be frozen as the final CBPR schema.

## Disposition

**Formal Model 002:** STABLE.

**Schema 001:** VALID SERIALISATION PROTOTYPE / INCOMPLETE SEMANTIC COVERAGE.

**Executable fixture architecture:** WORKING.

**Next:** Schema 002 should encode explicit composition-evaluation records, temporal evidence, control conflicts and commit-time validation result/state before another executable test.

**PMEDG:** PREMATURE.
