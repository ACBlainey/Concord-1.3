# Bootstrap Service Registry — Schema Conformance Evaluation 001

**Project:** The Concord
**Date:** 1 October 2026
**Subject:** Bootstrap Service Registry — JSON Schema 001
**Semantic source:** Bootstrap Service Registry — Formal Record and Validation Model 002
**Status:** SERIALIZATION EVALUATION / REVISION REQUIRED

## 1. Purpose

Test whether JSON Schema 001 faithfully serializes Model 002 without flattening, rejecting or inventing semantic states.

Schema validity is not service legitimacy and is not authority validation.

## 2. Immediate Serialization Findings

### S1 — Unknown Vocabulary Preservation

**Result: FAIL.**

Model 002 requires unknown future vocabulary values to:
- not be silently remapped;
- be preserved verbatim where syntactically safe;
- be marked unsupported/unknown where necessary;
- never gain authority semantics through fallback.

Schema 001 defines closed JSON Schema enums for:
- epistemic state;
- service status;
- availability;
- constitutional threshold state;
- control role;
- Bootstrap class;
- service relation type.

A future value therefore fails structural validation instead of being preserved.

This directly conflicts with:
- BSR-32 Unknown Vocabulary != Known Meaning;
- BSR-33 Serialization Compatibility != Semantic Equivalence;
- Model 002 §17.

**Classification:** SUBSTANTIVE SERIALIZATION DEFECT / NOT SEMANTIC-MODEL FAILURE.

**Repair:** use an extensible vocabulary token pattern and distinguish recognised core values from extension/unknown values at semantic validation time, or use a structured vocabulary value carrying namespace/version/token.

### S2 — State-Space Conflation

**Result: FAIL.**

Schema 001 reuses one `epistemicState` vocabulary for:
- verification;
- integrity;
- freshness;
- dispute state.

These are distinct dimensions.

Examples:
- STALE is naturally a freshness state;
- COMPROMISED is naturally an integrity state;
- DISPUTED is naturally a dispute/verification state;
- VERIFIED_TO_DECLARED_SCOPE is naturally verification state.

Allowing every value in every field permits semantically nonsensical but schema-valid combinations such as:
- `integrity_state = STALE`;
- `freshness_state = COMPROMISED`.

**Classification:** SUBSTANTIVE SERIALIZATION DEFECT / NOT SEMANTIC-MODEL FAILURE.

**Repair:** separate vocabularies for VerificationState, IntegrityState, FreshnessState and DisputeState.

### S3 — Extension Namespace Enforcement

**Result: PARTIAL FAIL.**

Schema 001 records `extension_namespaces` but the `extensions` object accepts arbitrary keys without requiring them to correspond to declared namespaces.

This does not manufacture authority by itself, but it weakens the Model 002 rule that extensions should use an explicit namespace.

**Classification:** SERIALIZATION CONSTRAINT GAP.

**Repair:** define a namespaced extension-entry structure rather than unconstrained object properties.

### S4 — Authority Profile Binding

**Result: PASS.**

AuthorityProfile is nested inside FunctionProfile, preserving per-function binding.

### S5 — Partial Availability

**Result: PASS.**

Operational availability is function-level. Optional summary availability is explicitly marked as summary and requires a derivation rule.

### S6 — Record vs Service Identity

**Result: PASS.**

RegistryRecordID is separate from ServiceIdentityReference.

### S7 — Scoped/Temporal Control

**Result: PASS.**

ControlRelation preserves actor, role, scope, effective interval, observation time, evidence and verification.

### S8 — Contradictory Evidence

**Result: PASS at structural level.**

Arrays and dispute/correction structures do not require contradictory evidence to be deleted.

### S9 — Relation Contradiction

**Result: PASS at structural level.**

Multiple service relations can coexist; the schema does not force SAME_SERVICE_AS/FORK_OF/SUCCESSOR_OF claims into one truth value.

### S10 — Schema Validity vs Semantic Conformance

**Result: REQUIRES EXPLICIT TWO-LAYER VALIDATION.**

JSON Schema can enforce shape, types and local vocabularies. It cannot by itself establish:
- legitimate authority;
- truth of identity correlation;
- independence of evidence;
- constitutional legitimacy;
- whether a derivation rule is epistemically sound;
- whether a claimed scope actually matches authority evidence.

A conforming implementation therefore requires:
1. structural schema validation; and
2. semantic BSR validation against Model 002 invariants.

> **Schema Validity != Semantic Conformance**

> **Semantic Conformance != Service Legitimacy**

> **Service Legitimacy != Constitutional Authority**

## 3. Corpus Disposition

A full example corpus should not be frozen against Schema 001 because S1 and S2 would encode known defects into the fixtures.

First create Schema 002, then run:
- valid ordinary record;
- valid mixed-function record;
- valid disputed record;
- valid unknown-vocabulary record;
- valid partial-availability record;
- valid fork/succession relation record;
- invalid missing-required-field record;
- invalid malformed timestamp/reference record;
- structurally valid but semantically non-conforming authority-capture record;
- structurally valid but semantically non-conforming misleading-summary record.

## 4. Architecture Check

No finding requires:
- Model 003;
- reopening Zero-Infrastructure Bootstrap architecture;
- a new authority abstraction;
- a new identity authority;
- a new registry function.

The failures are strictly serialization-layer defects.

## 5. Disposition

**Schema 001:** REVISION REQUIRED.

**Model 002:** remains stable.

**Architectural discovery reopened:** NO.

**Next:** Schema 002 with extensible vocabulary representation, separated state spaces and namespaced extensions, followed by executable fixture validation.
