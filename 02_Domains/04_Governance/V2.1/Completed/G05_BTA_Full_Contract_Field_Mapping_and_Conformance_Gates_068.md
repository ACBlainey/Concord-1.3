# G-05 — BTA Full Contract Field Mapping and Conformance Gates 068

**Status:** source-based contract recovery and conformance design; no claim of executing the complete BTA contract.

## Actual portable contract

BTA Portable Module v1.0 §23 defines **28 named fields**:
`TransitionID`, `ObjectOrFunctionRefs`, `Scope`, `TransitionClass`, `ObjectCardinality`, `ParticipatingOwnerRefs`, `PriorValidStateRefs`, `TransitionBasisRefs`, `TransitionPhaseRefs`, `TransitionStateRefs`, `PendingStateRefs`, `CompletionConditionRefs`, `ProtectedUnresolvedStateRefs`, `NonPropagationRules`, `ValidationRefs`, `RelationalEffectRefs`, `ExternalConsequenceRefs`, `SurvivingDutyRefs`, `SurvivingValueRefs`, `TerminatedAuthorityRefs`, `ReleasedResourceRefs`, `DependencyRefs`, `TemporalRelationRefs`, `RecoveryRefs`, `NextStateRefs`, `ReversibilityState`, `UncertaintyOrDisputeState`, `Provenance`.

The portable contract explicitly states fields are **materially optional unless required by the host profile**. Thus a full-field presence requirement would contradict BTA v1.0. A conformant adapter must distinguish omitted/irrelevant, unknown, and materially required-but-missing fields.

## Legacy machine-readable test object

`02_Domains/03_Research/Development_Archive/Portable_Modules/Bounded_Transition_Architecture/03_Pre_PMEDG_Testing/BTA Machine-Readable Transfer Test 003 — Blind Test Brief and Transition Object.md` includes a concrete YAML `BoundedTransitionContract` object. Some names differ from graduated v1.0: `ParticipatingStateSystemRefs` vs `ParticipatingOwnerRefs`, `TransitionEpochOrPhaseRefs` vs `TransitionPhaseRefs`, `ScopedValidationRefs` vs `ValidationRefs`, `ExternalityReviewRefs` vs `ExternalConsequenceRefs`, `ClockTransitionRelationRefs` vs `TemporalRelationRefs`, `RollbackOrRecoveryRefs` vs `RecoveryRefs`.

**Compatibility caution:** These are candidate mapping pairs, not proven synonyms. In particular an externality *review* is not necessarily the same as an external *consequence*. A parser must preserve the original key, semantics and provenance; reject ambiguous conversion rather than silently rename it.

## Proposed host-specific conformance gates

1. Parse source object and retain original keys, owner references and nested state values.
2. Verify transition identity, bounded scope, represented owners and consequential basis where materially necessary.
3. Preserve each independent dimension; do not infer completion, permission, authority, recovery or rights restoration from a different completed dimension.
4. Identify unresolved and pending completion conditions without forcing synchronous closure.
5. Treat explicit terminated authority as non-active; do not infer authority from presence of a transition basis reference.
6. Validate provenance, dependency and temporal relations only within their defined owner-system meanings.
7. Require owner-system verification of lawful emergency activation, operational expiry, current resource state and queued-action eligibility.
8. Route ambiguous legacy fields for review; do not convert unknown semantics into authoritative decisions.
9. Retain event/transition history when invalidation, partial crossing or rollback occurs.
10. Fail closed on a material missing prerequisite while leaving unrelated actions eligible under their own conditions.

## Concrete next test vectors

- **V1:** full legacy YAML object round-trips without data loss.
- **V2:** a versioned mapping produces graduated portable keys while preserving unmatched original keys.
- **V3:** conflicting `TerminatedAuthorityRefs` and a purported active authority cannot activate a power.
- **V4:** completed service operation with pending privileged access cannot propagate access.
- **V5:** expiry during a paused Clock does not terminate surviving recovery duties.
- **V6:** a branch with unknown material temporal ordering remains unresolved, not artificially serialised.
- **V7:** unknown material dependency prevents consequential execution but not independent work.
- **V8:** malformed or absent provenance for high-consequence transition is explicitly flagged.

## Disposition

The prior schema-shaped adapter 067 tested only a small subset of these fields. **Do not describe it as complete BTA conformance.** Next implementation should use the source YAML fixture, preserve its legacy vocabulary and report any semantic mapping ambiguities explicitly.

Sources: BTA Portable Module v1.0 §§5–27; BTA Machine-Readable Transfer Test 003; Governance G-05 059–067.
