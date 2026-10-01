# BSuR Schema 002 — Executable Fixture Evaluation 001

**Project:** The Concord  
**Date:** 1 October 2026  
**Semantic source:** Bootstrap Succession Record — Formal Specification 002  
**Serialization:** Bootstrap Succession Record — JSON Schema 002  
**Fixture manifest:** BSuR Schema 002 — Fixture Manifest 001.json  
**Status:** IMPLEMENTATION CONFORMANCE TEST DESIGN

## 1. Purpose

Test whether Schema 002 preserves the succession semantics required by Specification 002 and whether a separate semantic layer can reject authority manufacture that is intentionally representable as structurally valid JSON.

## 2. Two-Layer Evaluation

### Layer A — Structural
Use JSON Schema Draft 2020-12 with date-time format assertion enabled.

Structural PASS means only that the record conforms to the serialization.

### Layer B — Semantic
Evaluate the BSuR invariants and transition relationships.

Semantic PASS does not itself establish constitutional legitimacy; it means the record does not violate the BSuR semantic constraints exercised by the fixture set.

> Schema Validity != Successful Succession

> Semantic Conformance != Constitutional Authority

## 3. Positive Cases

V01 clean graduation establishes the ordinary baseline.

V02 and V03 test split/merge topology without authority replication/union.

V04 tests rollback as a new transition.

V05 tests later discovery of residual control without rewriting historical observation.

V06 tests component state divergence and prevents top-level summary flattening.

V07 tests preservation of future namespaced vocabulary.

V08 tests copy/duplication versus actual record transfer.

## 4. Structural Negatives

S01-S05 must fail before semantic evaluation.

S05 specifically guards the Schema001→Schema002 repair: AuthorityAfter must use independent_basis rather than the predecessor-shaped generic basis field.

## 5. Semantic Negatives

M01 Asset possession does not grant authority.

M02 Same identity does not grant same authority.

M03 Merger does not union predecessor authority.

M04 Split does not replicate predecessor authority.

M05 Rollback does not restore expired historical authority.

M06 Emergency dependency/indispensability does not renew authority after sunset.

M07 Summary cannot override component truth.

M08 Declared retirement cannot erase observed residual control.

M09 Registry consensus does not adjudicate successor authority.

M10 Authority-bearing transition requires explicit scoped non-transfer representation.

## 6. Minimum Semantic Harness Rules

### SU-01 Independent Authority Basis
AuthorityAfter for an authority-bearing successor function requires a basis independent of succession, possession, control, identity continuity, popularity, dependency or registry agreement.

### SU-02 Anti-Merger Laundering
A merger cannot expand authority scope solely by unioning predecessor claims.

### SU-03 Anti-Split Replication
A split cannot replicate one predecessor authority into every successor solely because each receives part of the function/infrastructure.

### SU-04 Rollback Current Trace
Rollback requires current authority trace; historical authority does not reactivate automatically.

### SU-05 Emergency Sunset
Expired emergency authority is not renewed by operational necessity, popularity or participant dependency.

### SU-06 Component Truth
TransitionSummary is navigation metadata. It cannot override a disputed/failed/unresolved component relation.

### SU-07 Residual Reality
Declared retirement does not establish loss of control where residual observations show continued material control.

### SU-08 Registry Non-Adjudication
Registry agreement/publication cannot constitute successor authority.

### SU-09 Scoped Non-Transfer
Authority-bearing transitions must explicitly represent relevant authority that did not transfer.

### SU-10 Unknown Vocabulary
UNRECOGNISED tokens remain unknown and cannot be assigned a known authority-bearing meaning through fallback.

### SU-11 Record Copy State
COPIED/retained/duplicated records cannot be silently interpreted as exclusive completed transfer.

### SU-12 Null Is Not Proof
Null/unresolved source or destination must not be interpreted as proof that no source/destination exists.

## 7. Validator Requirements

1. Draft 2020-12.
2. Assert date-time format.
3. Preserve unknown namespaced vocabulary.
4. Enforce additionalProperties=false where declared.
5. Run semantic validation after structural validation.
6. Keep evidence/verification/dispute states distinct.
7. Preserve contradictory observations.
8. Never convert populated independent_basis into positive legitimacy proof.
9. Never treat summary state as component authority.
10. Report structural and semantic results separately.

## 8. Execution Rule

The test is not complete until actual JSON fixture records are materialised and executed.

Expected outcomes in the manifest are hypotheses to test, not results.

Unexpected schema or semantic behaviour must be preserved and source-resolved before revision.

## 9. Provenance Rule

Do not overwrite:
- Specification 002;
- Schema 001;
- Schema Conformance Evaluation 001;
- Schema 002;
- failed fixture records.

If Schema 002 fails, preserve it and create Schema 003 only after source resolution.
