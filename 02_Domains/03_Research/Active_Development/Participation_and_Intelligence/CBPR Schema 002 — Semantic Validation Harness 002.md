# CBPR Schema 002 — Semantic Validation Harness 002

**Date:** 2 October 2026
**Status:** ACTIVE DEVELOPMENT / TEST HARNESS

## Structural expectations
V01-V03 VALID. S01-S04 INVALID. M01-M05 structurally VALID.

## Semantic rules
SV1 Composition marked PASS requires a sufficient authority basis for any material combined effect not independently contained within component scopes.
SV2 A commit validation cannot have composition_current PASS when its referenced composition result is FAIL or UNRESOLVED.
SV3 COMMITTABLE requires every applicable commit-validation dimension to be PASS or NOT_APPLICABLE; UNRESOLVED is not sufficient.
SV4 Conflicting simultaneously active controls whose legitimate precedence has not been resolved must not be represented as if one control simply prevailed.
SV5 Any FAIL dimension makes result NOT_COMMITTABLE; any required UNRESOLVED dimension makes result UNRESOLVED or NOT_COMMITTABLE, not COMMITTABLE.
SV6 Structural validity does not imply authority.

## Expected semantic negatives
M01 FAIL SV1.
M02 FAIL SV2.
M03 FAIL SV3.
M04 FAIL SV4.
M05 FAIL SV5.

Formal Model 002 remains authoritative over semantics not encoded here.
