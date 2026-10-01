# Bootstrap Succession Record — Schema Conformance Evaluation 001

**Project:** The Concord  
**Date:** 1 October 2026  
**Subject:** Bootstrap Succession Record — JSON Schema 001  
**Semantic source:** Bootstrap Succession Record — Formal Specification 002  
**Status:** SERIALIZATION CONFORMANCE EVALUATION

## 1. Method

Schema 001 was treated as fixed and compared against the frozen semantic requirements of Specification 002 and Pre-Schema Adversarial Evaluation 002.

The question is not whether JSON Schema can decide legitimacy. It cannot and should not. The question is whether the schema faithfully preserves the information required for the semantic validator to decide conformity without information loss or accidental semantic substitution.

## 2. Positive Findings

### S1 — Extensible vocabulary preservation — PASS

Vocabulary values use a structured namespaced token with version and mandatory recognition state.

Unknown future values can therefore be preserved as UNRECOGNISED rather than rejected or silently mapped to a known meaning.

### S2 — State-space separation — PASS

Verification, dispute and freshness states are separate structural types. Schema 001 does not repeat the state-space conflation found during BSR Schema 001 development.

### S3 — Record metadata/version binding — PASS

The schema binds:
- BSUR-SPEC-002;
- BSUR-SCHEMA-001;
- creation, observation and update timestamps.

### S4 — Function source/destination binding — PASS

FunctionTransition retains service-qualified source and destination FunctionIDs.

### S5 — Authority transition binding — PASS

AuthorityTransition retains source/destination service, function, holder, before/after authority, non-transfer list and threshold state.

### S6 — Authority non-transfer structure — PASS

AuthorityNotTransferred is scoped to source holder/function/scope and proposed/actual destination.

### S7 — Split/merge representability — PASS

Arrays of independent transition relations can preserve one-to-many, many-to-one and many-to-many transition topology without authority union in the syntax itself.

### S8 — Component-over-summary architecture — PASS

Transition summary is optional and explicitly marked declared_as_summary=true. Component relation states remain separately representable.

### S9 — Competing evidence/relations — PASS

No uniqueness rule forces contradictory transition, identity, dispute or residual observations to collapse into one record.

### S10 — Null/unresolved endpoints — PASS WITH SEMANTIC REQUIREMENT

Source/destination service/controller references can be null.

A semantic validator must distinguish "explicitly unresolved/not represented" from a claim that no source/destination exists. Null must not be treated as proof of nonexistence.

## 3. Serialization Defects

### D1 — Residual temporal semantics incompletely serialized — FAIL

Specification 002 defines ResidualObservation with:
- ObservedAt;
- EffectiveFromIfKnown;
- EffectiveUntilIfKnown.

Schema 001 serializes ObservedAt but omits effective_from_if_known and effective_until_if_known.

This loses the distinction between when residual control was discovered and when it may actually have existed.

**Classification:** SUBSTANTIVE SERIALIZATION DEFECT / NOT SEMANTIC-MODEL FAILURE.

### D2 — Effective time omitted from several relation types — FAIL

Specification 002 explicitly includes EffectiveTime in:
- DependencyTransition;
- AuthorityTransition;
- IdentityMapping;
- ParticipantImpact;
- RetirementState.

Schema 001 omits those fields.

FunctionTransition and AssetTransition retain effective_time, creating inconsistent temporal fidelity across the record.

This is especially dangerous for authority succession, rollback, delayed discovery and historical reconstruction.

**Classification:** SUBSTANTIVE SERIALIZATION DEFECT.

### D3 — RecordTransition under-serializes Specification 002 — FAIL

Specification 002 requires RecordTransition to retain:
- ProtectionStateBefore;
- ProtectionStateAfter;
- AccessAuthorityBefore;
- AccessAuthorityAfter;
- RetentionOrDestructionState;
- IdentityMappingRefs;
- EffectiveTime;
- Evidence;
- Disputes.

Schema 001 defines most as optional and omits effective_time and dispute_refs entirely.

A structurally valid record can therefore discard material protection/access/destruction/dispute state that the semantic model expects.

**Classification:** SUBSTANTIVE SERIALIZATION DEFECT.

### D4 — Relation evidence/dispute fields inconsistently mandatory — FAIL

Specification 002 treats evidence as part of the formal relation objects. Schema 001 leaves evidence_refs optional in several relations and omits dispute_refs from some relation types.

The schema must permit unknown/no evidence, but that should be represented explicitly rather than by silently deleting the evidence field where the semantic object requires it.

**Classification:** SERIALIZATION COMPLETENESS DEFECT.

### D5 — AuthorityAfter independent-basis naming weakened — PARTIAL FAIL

Specification 002 names the successor field IndependentBasis. Schema 001 reuses authorityState with generic "basis" for both AuthorityBefore and AuthorityAfter.

The data can still be stored, but the serialization loses an important semantic cue and makes accidental copying of predecessor basis easier.

**Classification:** SEMANTIC PRECISION DEFECT IN SERIALIZATION.

Recommended repair: distinct authorityBefore and authorityAfter definitions; authorityAfter uses independent_basis.

### D6 — Empty AuthorityNotTransferred is structurally accepted — PASS AT SCHEMA / SEMANTIC VALIDATOR REQUIRED

An authority-bearing transition can structurally contain an empty authority_not_transferred array.

This is not necessarily a JSON Schema defect because whether the function is authority-bearing and what must be explicitly non-transferred is semantic/contextual.

The semantic validator must enforce BSuR-37/U9.

### D7 — Populated authority basis can be illegitimate — PASS AT SCHEMA / SEMANTIC VALIDATOR REQUIRED

Any non-empty string can populate basis/independent_basis.

Correctly, JSON Schema does not adjudicate whether that basis is constitutionally valid.

### D8 — Summary/component contradiction structurally accepted — PASS AT SCHEMA / SEMANTIC VALIDATOR REQUIRED

A summary may say COMPLETED while component authority remains disputed.

This contradiction must remain representable. Semantic validation must prevent consumers from treating summary as component truth.

## 4. Additional Structural Observations

### O1 — Unused transitionCore definition

Schema 001 contains an unused transitionCore definition.

**Classification:** CLEANUP ONLY.

### O2 — Temporal state spaces remain intentionally two-layered

JSON Schema format=date-time requires a validator configured to assert format checking.

**Classification:** IMPLEMENTATION VALIDATOR REQUIREMENT.

### O3 — Unknown recognised-token claims

A record can structurally mark an arbitrary namespaced token as RECOGNISED.

A semantic vocabulary registry must verify namespace/version/token recognition. Structural schema must not infer authority from recognition_state.

**Classification:** SEMANTIC VALIDATOR REQUIREMENT.

### O4 — Empty top-level transition arrays

Schema 001 permits empty arrays for every transition category.

This is acceptable for a general BSuR because a transition may concern only some categories and failed/observational records must remain representable. Semantic validation can require relevant relations for specific claimed transition types.

## 5. Source Resolution

The failures do not require Specification 003.

Specification 002 already contains the missing semantics. Schema 001 simply failed to serialize all of them.

Required Schema 002 repairs:

1. add effective_from_if_known/effective_until_if_known to ResidualObservation;
2. restore effective_time to DependencyTransition, AuthorityTransition, IdentityMapping, ParticipantImpact and RetirementState;
3. restore effective_time and dispute_refs to RecordTransition;
4. make formal relation evidence/dispute fields explicit where required by Specification 002;
5. split AuthorityBefore and AuthorityAfter schema definitions;
6. serialize AuthorityAfter as independent_basis;
7. remove unused transitionCore;
8. retain mandatory vocabulary recognition_state;
9. retain separate state spaces;
10. retain semantic-validator boundary for legitimacy, authority, summary/component contradiction and scoped non-transfer.

## 6. Disposition

**Schema 001 result:** REVISION REQUIRED.

**Specification 002 failure:** NO.

**Specification 003 required:** NO.

**Architectural discovery reopened:** NO.

**New succession abstraction required:** NO.

**Schema 002 required:** YES.

The correct provenance chain is:

Specification 002 (stable semantic source)
→ Schema 001 (preserved serialization attempt)
→ Schema Conformance Evaluation 001 (defects identified)
→ Schema 002 (repair candidate).

Do not overwrite Schema 001.
