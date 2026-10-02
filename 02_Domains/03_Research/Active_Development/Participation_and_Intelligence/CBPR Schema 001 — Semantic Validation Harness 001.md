# CBPR Schema 001 — Semantic Validation Harness 001

**Date:** 2 October 2026
**Status:** ACTIVE DEVELOPMENT / TEST HARNESS

## Structural expectations

V01, V02: VALID.
S01-S04: INVALID.
M01-M05: structurally VALID; intentionally semantically invalid/unsafe.

## Semantic rules

SV1 — Any action proposal referencing a credential binding requires that binding to exist and be ACTIVE for the relevant operation/target.

SV2 — A proposal to an UNKNOWN_CONSEQUENCE_INTERFACE must not be considered committable where material consequence knowledge is required.

SV3 — Referenced action grant must exist, be ACTIVE, include the operation, include the effective destination/target, and include the output consequence class.

SV4 — COMMIT_STATE_UNKNOWN is not eligible for blind consequential retry.

SV5 — Referenced EXPIRED, REVOKED, DISPUTED or UNKNOWN action grant is not current commit authority.

SV6 — Structural schema validity never implies semantic permission or authority.

## Expected semantic outcomes

M01 FAIL SV1.
M02 FAIL SV2.
M03 FAIL SV3.
M04 FAIL SV4.
M05 FAIL SV5.

This harness tests only the encoded subset. Formal Model 002 remains authoritative over semantics not represented by Schema 001.
