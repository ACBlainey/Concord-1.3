# BSR Schema 002 — Executable Validation Result 001

**Project:** The Concord
**Execution date:** 2 October 2026
**Schema:** Bootstrap Service Registry — JSON Schema 002
**Schema Git blob SHA:** `e6e1b6cec9950b61def4803389d4243abe017e59`
**Semantic harness:** BSR Semantic Validation Harness 001
**Status:** EXECUTED / EXPECTED MATRIX MATCHED

## 1. Execution Provenance

Validation was executed against contents fetched directly from the committed Concord-1.3 repository.

Structural execution used a deterministic Draft 2020-12 subset evaluator implementing every keyword used by BSR Schema 002, including asserted date-time format. It was not executed through the external Python jsonschema package.

Semantic execution used the frozen BSR Semantic Validation Harness 001 against the same committed records.

## 2. Structural Results

| Fixture | Git blob SHA | Expected | Observed |
|---|---|---|---|
| V01 | fcd694a23fb81bbed143408b0995a7342edaddd2 | PASS | PASS |
| V02 | 86ccecccd23ccec5e00d3d61abefb1f937dfb2f0 | PASS | PASS |
| V03 | 964ab576b19db1039bc5f964d4154d8dbab6b3d1 | PASS | PASS |
| V04 | 8aba352048669c87bd3b16a7a561688f61bc0601 | PASS | PASS |
| V05 | 61fc31f8f02de09b64c2ca6213badb232388896e | PASS | PASS |
| V06 | b8b7977b146edcf14f48ee4b7a75cde68c587824 | PASS | PASS |
| S01 | 0dc1c7097790d39fd130a1193cf1b6acb66c19a6 | FAIL | FAIL — record_meta required |
| S02 | 7e974045aa45aad59f7383668ee75bf00715ef06 | FAIL_WITH_FORMAT_CHECKING | FAIL — record_updated_at date-time |
| S03 | 0d636363b50c2288766bc23d6507a96c3d21a2d7 | FAIL | FAIL — model_version const |
| S04 | 13fdb3ffeb96d0a64cc21aff5ae01b68d7b10d98 | FAIL | FAIL — extension shape |
| M01 | 8e2227ac8746a6b29cebedea0925cf07d69c37a0 | PASS | PASS |
| M02 | a14bf2dbf4db9682708f2c00a172828d0f79f32b | PASS | PASS |
| M03 | ca26510dedf396f741df3f6e7318e3e51fb19a42 | PASS | PASS |
| M04 | c2f487a04ff203536f9baa74ec5cbf5144b1ecd4 | PASS | PASS |
| M05 | cb5f0c11e30e13d293465ca8a8c26d96a8f3b2e3 | PASS | PASS |

**Structural matrix:** 15/15 expected outcomes matched.

## 3. Semantic Results

| Fixture | Expected | Observed | Rule |
|---|---|---|---|
| V01 | PASS | SEMANTIC_PASS | — |
| V02 | PASS | SEMANTIC_PASS | — |
| V03 | PASS | SEMANTIC_PASS | — |
| V04 | PASS_WITH_UNKNOWN | SEMANTIC_PASS_WITH_UNKNOWN | SV-05 preserved |
| V05 | PASS | SEMANTIC_PASS | — |
| V06 | PASS | SEMANTIC_PASS | — |
| M01 | FAIL | SEMANTIC_FAIL | SV-01 |
| M02 | FAIL | SEMANTIC_FAIL | SV-02 |
| M03 | FAIL | SEMANTIC_FAIL | SV-04 |
| M04 | FAIL | SEMANTIC_FAIL | SV-06 |
| M05 | FAIL | SEMANTIC_FAIL | SV-07 |

S01-S04 correctly receive NOT_EVALUATED semantically.

**Semantic matrix:** all expected outcomes matched.

## 4. Key Evidence

V02 confirms authority, threshold and availability remain separable by FunctionID.

V04 confirms future namespaced vocabulary can remain explicitly unknown without fallback authority semantics.

V05 confirms partial availability can be represented per function without requiring whole-service flattening.

V06 confirms potentially conflicting fork/successor relations remain representable.

M01-M05 confirm structural validity cannot manufacture authority from:
- technical control;
- popularity/dependency;
- misleading service summary;
- extension payload;
- cross-registry agreement.

## 5. Disposition

**BSR Schema 002 structural fixture result:** PASS within tested keyword/fixture scope.

**BSR semantic harness result:** PASS within tested invariant scope.

**Expected matrix:** 15/15 structural outcomes matched; all applicable semantic expectations matched.

**Schema 003 required by this execution:** NO.

**Model 003 required:** NO.

**Architectural discovery reopened:** NO.

The BSR and BSuR machine-readable bootstrap records now have matching committed-artifact structural and semantic execution evidence.

## 6. Qualification

This is implementation-level conformance evidence for the tested corpus, not proof of:
- service legitimacy;
- constitutional authority;
- legal validity;
- cryptographic integrity;
- empirical operational success;
- universal schema completeness.

A later reproduction using an independent full Draft 2020-12 validator remains useful corroboration.

> Schema Validity != Semantic Conformance

> Semantic Conformance != Service Legitimacy

> Service Legitimacy != Constitutional Authority
