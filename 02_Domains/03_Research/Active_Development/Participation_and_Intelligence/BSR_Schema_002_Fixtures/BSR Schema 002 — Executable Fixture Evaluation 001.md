# BSR Schema 002 — Executable Fixture Evaluation 001

**Project:** The Concord
**Date:** 1 October 2026
**Semantic source:** Bootstrap Service Registry — Formal Record and Validation Model 002
**Schema:** Bootstrap Service Registry — JSON Schema 002
**Status:** IMPLEMENTATION CONFORMANCE TEST DESIGN

## 1. Result

Schema 002 is suitable for the first executable fixture corpus, with one validator-level qualification:

JSON Schema `format: date-time` is not guaranteed to be asserted by every validator merely because it appears in the schema. Conforming test execution MUST enable/assert format checking if malformed timestamps are expected to fail.

This is not a BSR semantic gap.

## 2. Required Two-Layer Test

Every fixture is evaluated separately for:

### Layer A — Structural Schema
Does the JSON instance satisfy Schema 002?

### Layer B — BSR Semantic Conformance
Does the structurally valid record preserve Model 002 invariants?

A Layer-A PASS is not a Layer-B PASS.

> **Schema Validity != Semantic Conformance**

> **Semantic Conformance != Service Legitimacy**

> **Service Legitimacy != Constitutional Authority**

## 3. Positive Corpus

V01 Ordinary provisional service — expected Schema PASS / Semantic PASS.

V02 Mixed-function mixed-authority service — expected PASS / PASS. Tests that Z0, Z4 and Z5 functions retain independent authority, threshold and availability.

V03 Disputed identity and control — expected PASS / PASS. Tests that contradiction and overlapping control can be represented without forced resolution.

V04 Unknown future vocabulary — expected PASS / PASS_WITH_UNKNOWN. Tests namespaced vocabulary preservation and non-inference.

V05 Partial availability — expected PASS / PASS.

V06 Fork and successor claims — expected PASS / PASS.

## 4. Structural Negative Corpus

S01 Missing required record_meta — expected Schema FAIL.

S02 Malformed timestamp — expected Schema FAIL when format assertion is enabled.

S03 Wrong model_version — expected Schema FAIL.

S04 Unnamespaced extension shape — expected Schema FAIL.

These cases test serialization, not authority.

## 5. Semantic Negative Corpus

These records are deliberately intended to be structurally valid.

### M01 Technical control claimed as authority
Schema: PASS.
Semantic: FAIL.

A syntactically valid AuthorityProfile whose sole authority basis is possession of server credentials violates the control/authority separation.

### M02 Popularity claimed as authority
Schema: PASS.
Semantic: FAIL.

Usage, dependency or popularity may be evidence of importance, but does not manufacture legitimate authority.

### M03 Misleading summary availability
Schema: PASS.
Semantic: FAIL.

A summary may be structurally valid while its derivation rule conceals an unavailable material function.

### M04 Extension attempts authority override
Schema: PASS.
Semantic: FAIL.

A correctly namespaced extension may carry arbitrary payload, but cannot gain authority semantics merely because the schema preserves it.

### M05 Cross-registry agreement as constitutional basis
Schema: PASS.
Semantic: FAIL.

Independent or repeated registry agreement may affect evidence confidence; it does not constitute constitutional authority.

## 6. Important Result

The semantic-negative fixtures are intentionally not expressible as JSON-Schema failures without importing substantive Concord authority judgments into the serialization layer.

That separation is desirable.

If Schema 002 attempted to reject M01-M05 structurally, the registry serialization would begin owning:
- substantive authority determination;
- constitutional legitimacy;
- evidence interpretation;
- derivation correctness.

Those belong above the syntax layer.

## 7. Validator Requirements

An implementation claiming Schema 002 conformance should:
1. use JSON Schema Draft 2020-12;
2. assert `format: date-time`;
3. preserve unknown namespaced vocabulary tokens;
4. reject undeclared object fields where Schema 002 uses `additionalProperties: false`;
5. run Model 002 semantic validation after structural validation;
6. never report structural PASS as service verification or authority validation.

## 8. Corpus Status

The fixture manifest is now preserved under `BSR_Schema_002_Fixtures/`.

The next implementation step is to materialise representative JSON instances for V01-V06, S01-S04 and M01-M05 and execute them with a Draft 2020-12 validator plus a separate semantic test harness.

No schema revision is justified by this design pass.

## 9. Status

**Schema 002 fixture design:** PASS.

**Known schema defect discovered:** NO.

**Known validator qualification:** date-time format assertion must be enabled.

**Model 002 revision required:** NO.

**Architecture reopened:** NO.
