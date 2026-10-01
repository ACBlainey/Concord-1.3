# BSR Semantic Validation Harness 001

**Project:** The Concord
**Date:** 1 October 2026
**Semantic source:** BSR Formal Record and Validation Model 002
**Serialization:** BSR JSON Schema 002
**Status:** IMPLEMENTATION TEST HARNESS / NOT AUTHORITY GRANT

## 1. Validation Order

1. Parse JSON.
2. Validate against JSON Schema Draft 2020-12 with format assertion enabled.
3. If structural validation fails, return STRUCTURAL_FAIL and do not claim semantic evaluation.
4. If structural validation passes, run semantic rules.
5. Report semantic result independently.
6. Never convert either result into service legitimacy or constitutional authority.

## 2. Semantic Result States

- SEMANTIC_PASS
- SEMANTIC_PASS_WITH_UNKNOWN
- SEMANTIC_FAIL
- SEMANTIC_UNRESOLVED
- NOT_EVALUATED

## 3. Core Rules Exercised by Fixture Set

### SV-01 Control Is Not Authority
If AuthorityBasis relies only on technical/effective control, infrastructure possession, credentials or equivalent capability, semantic FAIL.

Maps: BSR-07, BSR-08, BSR-09.

### SV-02 Popularity / Dependency Is Not Authority
If AuthorityBasis relies only on popularity, usage, dependency, repetition or registry agreement, semantic FAIL.

Maps: BSR-09, BSR-20.

### SV-03 Function Binding
Authority, threshold and operational availability must remain bound to the relevant FunctionID.

Maps: BSR-29, BSR-30.

### SV-04 Summary Cannot Conceal Material Function State
A service summary is derived metadata. If its declared derivation materially conceals a function-level state relevant to users or authority/continuity decisions, semantic FAIL.

Maps: BSR-30.

### SV-05 Unknown Vocabulary Preservation
UNRECOGNISED vocabulary is not semantic failure merely because it is unknown.

It must not be mapped to a known authority-bearing value without an explicit valid translation.

Return PASS_WITH_UNKNOWN unless another rule fails.

Maps: BSR-32, BSR-33.

### SV-06 Extension Non-Authority
Extension payload cannot override core authority trace, threshold, control/authority separation or constitutional state.

If an extension is relied upon as the sole authority grant, semantic FAIL.

Maps: BSR-09, BSR-32.

### SV-07 Cross-Registry Agreement
Agreement can contribute evidence confidence only where independence is supported.

Agreement does not constitute constitutional authority.

Maps: BSR-19, BSR-20.

### SV-08 Identity Correlation Is Evidentiary
SAME_SERVICE_AS and identity references remain evidence-backed claims.

Correlation cannot become universal identity sovereignty.

Maps: BSR-03, BSR-27, BSR-28.

### SV-09 Contradiction Is Representable
Conflicting evidence/control/identity relations do not automatically fail semantic conformance if the contradiction is exposed with uncertainty/dispute rather than silently resolved.

Maps: BSR-14, BSR-17.

### SV-10 Schema Pass Is Not Verification
No structural PASS may be rendered as VERIFIED, AUTHORITATIVE or CONSTITUTIONALLY_GROUNDED unless the corresponding semantic/evidentiary/authority basis independently supports it.

Maps: BSR-16 and the Model 002 validation boundary.

## 4. Fixture Expectations

| Fixture | Schema | Semantic |
|---|---|---|
| V01 | PASS | PASS |
| V02 | PASS | PASS |
| V03 | PASS | PASS |
| V04 | PASS | PASS_WITH_UNKNOWN |
| V05 | PASS | PASS |
| V06 | PASS | PASS |
| S01 | FAIL | NOT_EVALUATED |
| S02 | FAIL with format assertion | NOT_EVALUATED |
| S03 | FAIL | NOT_EVALUATED |
| S04 | FAIL | NOT_EVALUATED |
| M01 | PASS | FAIL — SV-01 |
| M02 | PASS | FAIL — SV-02 |
| M03 | PASS | FAIL — SV-04 |
| M04 | PASS | FAIL — SV-06 |
| M05 | PASS | FAIL — SV-07 |

## 5. Harness Boundary

This harness deliberately contains only rules needed to demonstrate the structural/semantic separation and Model 002 invariants exercised by the current corpus.

It is not yet a complete service-legitimacy evaluator.

A later implementation may formalise additional rules, but it must not silently turn absence of a rule into authority.

> **Validator Silence != Authority**

> **No Detected Violation != Positive Legitimacy Proof**
