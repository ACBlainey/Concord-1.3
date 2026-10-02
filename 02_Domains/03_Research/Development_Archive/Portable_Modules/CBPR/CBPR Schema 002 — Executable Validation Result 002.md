# CBPR Schema 002 — Executable Validation Result 002

**Date:** 2 October 2026
**Status:** ACTIVE DEVELOPMENT / EXECUTABLE VALIDATION RESULT / NOT CANONICAL

## Test Set
12 fixtures: 3 positive, 4 structural-negative, 5 semantic-negative.

## Structural Result
V01-V03 satisfy the Schema 002 structural design.
S01 missing required composition_evaluations — rejected.
S02 negative temporal uncertainty — rejected.
S03 invalid control source — rejected.
S04 composition with fewer than two components — rejected.
M01-M05 remain structurally representable for semantic rejection.

**Structural expectations: 12/12.**

## Semantic Result
M01 unauthorised read+send composition — rejected by SV1.
M02 failed composition represented as committable — rejected by SV2.
M03 unresolved temporal validity represented as committable — rejected by SV3.
M04 unresolved participant/operator control conflict represented as simple RUNNING outcome — rejected by SV4.
M05 failed target validation represented as committable — rejected by SV5.

**Semantic expectations: 5/5.**

## Result

Schema 002 now machine-represents the principal additions of Formal Model 002:
- composition evaluation;
- temporal evidence/trust;
- control events/conflicts;
- commit-time validation state.

The structural/semantic separation remains intentional.

> **Schema Validity != Execution Authority**

## Remaining Formalisation Limits
Implementation-specific enforcement remains outside the schema: effective destination discovery, isolation strength, trusted-clock implementation, distributed-runtime observation completeness, cryptographic attestation, and reconciliation of external commit state.

These are implementation/security questions rather than a missing CBPR abstraction layer.

## Disposition
**Formal Model 002:** STABLE.
**Schema 002:** SERIALISATION MODEL STABLE FOR CURRENT FORMAL SCOPE.
**Fixture/harness architecture:** PASS.
**Broad CBPR architectural discovery:** CLOSED unless new evidence reopens it.
**Next:** prepare a PMEDG candidate package and independent transfer-test brief; do not graduate before blind transfer testing.
