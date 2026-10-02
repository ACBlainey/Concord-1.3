# BSuR Schema 002 — Executable Validation Result 001

**Project:** The Concord
**Execution date:** 2 October 2026
**Schema:** Bootstrap Succession Record — JSON Schema 002
**Schema Git blob SHA:** `2bf3f7da697fb3d73c23f558aedf0db619d00605`
**Semantic harness:** BSuR Semantic Validation Harness 001
**Status:** EXECUTED / EXPECTED MATRIX MATCHED

## 1. Execution Provenance

Validation was executed against fixture contents fetched directly from the committed GitHub repository.

Structural execution used a deterministic JSON Schema Draft 2020-12 subset evaluator implementing every keyword used by Schema 002:
- $ref;
- anyOf;
- type;
- required;
- properties;
- additionalProperties;
- items;
- enum;
- const;
- minLength;
- date-time format assertion.

It was not executed through the external Python `jsonschema` package. This distinction is preserved as an implementation-provenance limitation, not hidden.

Semantic execution used BSuR Semantic Validation Harness 001 against the same committed fixture records.

## 2. Structural Results

| Fixture | Blob SHA | Expected | Observed |
|---|---|---|---|
| V01 | ca4f93c63d25a5b12f1175b6d7471c1d49d335b9 | PASS | PASS |
| V02 | b85c11902f45b635570c79b53679c57cf9496200 | PASS | PASS |
| V03 | 764930c98ec226bdb522d183af240697ffbd2513 | PASS | PASS |
| V04 | 927921d31480d53e4bb77311258de8f8d8133e84 | PASS | PASS |
| V05 | c269d8c27427c5095345d700ab865343df2b6891 | PASS | PASS |
| V06 | d9cbf0b5a05891d8bb86c272eb40211c5d4de0c6 | PASS | PASS |
| V07 | 188670f7bd946c5a0b8adbc14d85f48118c87c1e | PASS | PASS |
| V08 | fa8897e8aa5c45aa9a9a5ee1b432e0c49b0b33d4 | PASS | PASS |
| S01 | f461d4437ad96ebc2a3241b5df96912771aa4f30 | FAIL | FAIL — record_meta required |
| S02 | 12e2b638be1b74e50ed684f99c23b4fe8011ee08 | FAIL_WITH_FORMAT_CHECKING | FAIL — record_updated_at date-time |
| S03 | 9e3dcfb772690d7efbd1e865eb10323820489e7e | FAIL | FAIL — schema_version const |
| S04 | 60696821350415ea3f50cac6cc3351a51fd7cda3 | FAIL | FAIL — extension required fields/additional property |
| S05 | 930f52e3ca61fa3adf1ac70a9a409c7eef988931 | FAIL | FAIL — independent_basis required; old basis additional |
| M01 | 40d4b1300fb63d3cae0db07579e7eaa5b1efce20 | PASS | PASS |
| M02 | 04d1430000d317865ce4854c8d785dc90720b31b | PASS | PASS |
| M03 | 6e264f80f15163458480a7c67d577172d143743e | PASS | PASS |
| M04 | 36080c86df62849867403124376ffe046182700d | PASS | PASS |
| M05 | 82562ba658b1e34f72f8594327228f9891799501 | PASS | PASS |
| M06 | 8aeb7753d8570723c4aa641aedc4809e676c4ae5 | PASS | PASS |
| M07 | f4cb063bb0eb9c285060dbadd20f32670f57cc52 | PASS | PASS |
| M08 | f7c617bc467992673059a7f8be67ff55285b3d76 | PASS | PASS |
| M09 | 464a908e4f8667200b05c642b8da2fbe92fad330 | PASS | PASS |
| M10 | e0710f61da97b7f9cd1fdc3bc296b0a850876c40 | PASS | PASS |

**Structural matrix:** 23/23 expected outcomes matched.

## 3. Semantic Results

| Fixture | Expected | Observed | Rule |
|---|---|---|---|
| V01 | PASS | SEMANTIC_PASS | — |
| V02 | PASS | SEMANTIC_PASS | — |
| V03 | PASS | SEMANTIC_PASS | — |
| V04 | PASS | SEMANTIC_PASS | — |
| V05 | PASS | SEMANTIC_PASS | — |
| V06 | PASS | SEMANTIC_PASS | — |
| V07 | PASS_WITH_UNKNOWN | SEMANTIC_PASS_WITH_UNKNOWN | SU-10 |
| V08 | PASS | SEMANTIC_PASS | SU-11 preserved |
| M01 | FAIL | SEMANTIC_FAIL | SU-01 asset/key possession |
| M02 | FAIL | SEMANTIC_FAIL | SU-01 same identity |
| M03 | FAIL | SEMANTIC_FAIL | SU-02 merger authority union |
| M04 | FAIL | SEMANTIC_FAIL | SU-03 split authority replication |
| M05 | FAIL | SEMANTIC_FAIL | SU-04 rollback historical authority |
| M06 | FAIL | SEMANTIC_FAIL | SU-05 emergency dependency after sunset |
| M07 | FAIL | SEMANTIC_FAIL | SU-06 summary overrides component truth |
| M08 | FAIL | SEMANTIC_FAIL | SU-07 retirement hides residual control |
| M09 | FAIL | SEMANTIC_FAIL | SU-08 registry consensus |
| M10 | FAIL | SEMANTIC_FAIL | SU-09 empty scoped non-transfer |

Structural-negative S01-S05 correctly received NOT_EVALUATED at the semantic layer.

**Semantic matrix:** all expected outcomes matched.

## 4. Key Regression Evidence

### Schema 001 → Schema 002 authority repair
S05 proves the repair is active:
- missing `independent_basis` is rejected;
- obsolete generic `basis` is rejected as an additional property.

### Unknown vocabulary
V07 proves a future namespaced token marked UNRECOGNISED remains structurally representable and semantically unknown rather than silently mapped.

### Authority non-capture
M01-M10 demonstrate that structural validity alone does not convert:
- possession;
- identity continuity;
- merger;
- split;
- rollback;
- emergency dependency;
- summary state;
- retirement declaration;
- registry consensus;
- omission of non-transfer

into legitimate successor authority.

## 5. Result

**Schema 002 structural fixture result:** PASS within tested keyword/fixture scope.

**Semantic harness result:** PASS within tested BSuR invariant scope.

**Expected matrix matched:** 23/23 structural; all applicable semantic expectations matched.

**Schema 003 required by this test:** NO.

**Specification 003 required:** NO.

**Architectural discovery reopened:** NO.

## 6. Remaining Qualification

This result establishes implementation-level conformance only for the tested corpus and validator keyword scope.

It does not establish:
- constitutional legitimacy of any real successor;
- legal validity;
- cryptographic integrity;
- distributed registry agreement;
- empirical operational success;
- completeness against every future succession topology.

A later independent standards-validator run may additionally reproduce the structural test using a full Draft 2020-12 implementation. Such a reproduction is useful provenance but is not currently evidence of a semantic defect.

> Schema Validity != Successful Succession

> Semantic Conformance != Constitutional Authority

> Function Continuity != Authority Continuity
