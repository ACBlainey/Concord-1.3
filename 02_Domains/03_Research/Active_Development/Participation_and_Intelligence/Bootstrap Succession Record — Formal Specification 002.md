# Bootstrap Succession Record — Formal Specification 002

**Project:** The Concord  
**Date:** 1 October 2026  
**Version:** 0.2  
**Status:** ACTIVE DEVELOPMENT / IMPLEMENTATION FORMALISATION / PRE-SCHEMA / NOT CANONICAL  
**Predecessor:** Bootstrap Succession Record — Formal Specification 001  
**Revision basis:** BSuR Pre-Schema Adversarial Evaluation 001

## 1. Purpose

Define a relational succession record that preserves functional continuity while preventing authority laundering, accidental authority inheritance, identity collapse and hidden residual control during split, merger, replacement, rollback, retirement or failure.

> **Function Continuity != Authority Continuity**

> **Transition Completion != Constitutional Grounding**

> **BSuR != Authority Grant**

## 2. Formal Object

`BSuR = <RecordMeta, Parties, Trigger, FunctionTransitions, AssetTransitions, RecordTransitions, DependencyTransitions, AuthorityTransitions, IdentityMappings, ParticipantImpacts, ResidualObservations, RetirementState, LegacyAccess, TemporalState, Disputes, Provenance>`

Every material transition relation identifies its source/predecessor, destination/successor where applicable, scope and evidence.

## 3. Record Metadata

Required:
- SuccessionRecordID
- SpecificationVersion = BSUR-SPEC-002
- RecordCreatedAt
- RecordObservedAt
- RecordUpdatedAt

A BSuR may coexist with competing BSuRs.

> **Record Priority != Authority Priority**

## 4. Party Reference

`PartyReference = <PartyIDorReference, Role, IdentityEvidence, VerificationState>`

Roles may include:
- PREDECESSOR_SERVICE
- SUCCESSOR_SERVICE
- PREDECESSOR_OPERATOR
- SUCCESSOR_OPERATOR
- TECHNICAL_CONTROLLER
- EFFECTIVE_CONTROLLER
- AFFECTED_PARTICIPANT_OR_CLASS
- EXTERNAL_INSTITUTION
- REGISTRY_OBSERVER
- UNKNOWN_OR_DISPUTED

Roles are descriptive and may overlap.

## 5. Trigger

`Trigger = <TriggerType, ClaimedBy, ObservedAt, Evidence, VerificationState>`

Trigger types include planned graduation/retirement, withdrawal, failure, legal change, constitutional threshold crossing, new authority basis, split, merger, replacement, hostile/disputed control change, emergency continuity, dependency failure, insolvency/resource loss, voluntary transfer, supersession and UNKNOWN/DISPUTED.

> **Transition Trigger != Authority To Perform Transition**

## 6. FunctionTransition

`FunctionTransition = <TransitionID, SourceService, SourceFunctionID, DestinationService, DestinationFunctionID, TransitionType, SourceState, DestinationState, TransferState, ContinuityRequirement, MaterialConsequences, EffectiveTime, Evidence, Disputes>`

TransitionType may include:
- CONTINUE
- SPLIT
- MERGE
- REPLACE
- SUSPEND
- RETIRE
- RECONSTRUCT
- EXTERNALISE
- ROLLBACK
- FAIL
- UNKNOWN
- DISPUTED

Source or destination may be null/unresolved where genuinely absent or unknown.

Function IDs are therefore never assumed globally unique outside their service context.

## 7. AssetTransition

`AssetTransition = <TransitionID, AssetReference, SourceController, DestinationController, TransferMechanism, TransferState, EffectiveTime, ResidualControl, Evidence, Disputes>`

Assets include compute, domains, endpoints, facilities, funds, equipment, keys, software, databases, communications, contracts and legal entities.

ResidualControl is explicit.

> **Asset Transfer != Authority Transfer**

## 8. RecordTransition

`RecordTransition = <TransitionID, RecordClassOrReference, Source, Destination, TransferState, CopyState, ProtectionStateBefore, ProtectionStateAfter, AccessAuthorityBefore, AccessAuthorityAfter, RetentionOrDestructionState, IdentityMappingRefs, EffectiveTime, Evidence, Disputes>`

CopyState may distinguish:
- MOVED
- COPIED
- PARTIALLY_COPIED
- RETAINED_BY_SOURCE
- DUPLICATED_UNRESOLVED
- LOST
- UNKNOWN
- DISPUTED

CIBB or other applicable protected-information rules remain controlling.

> **Possession Of Records != Authority Over Subjects Of Records**

## 9. DependencyTransition

`DependencyTransition = <TransitionID, DependencyReference, FunctionScope, SourceDependencyState, DestinationDependencyState, Criticality, ControllerBefore, ControllerAfter, IndependenceClaim, CommonDependencyRefs, FailureImplications, EffectiveTime, Evidence, VerificationState>`

A successor can therefore be organisationally separate while operationally dependent.

> **Organisational Separation != Operational Independence**

## 10. AuthorityTransition

`AuthorityTransition = <TransitionID, SourceService, SourceFunctionID, SourceHolder, AuthorityBefore, DestinationService, DestinationFunctionID, DestinationHolder, AuthorityAfter, AuthorityNotTransferred, ThresholdState, EffectiveTime, Evidence, Disputes>`

### 10.1 AuthorityBefore

`AuthorityBefore = <Claim, Basis, Scope, VerificationState, SunsetOrReview>`

Descriptive only.

### 10.2 AuthorityAfter

`AuthorityAfter = <Claim, IndependentBasis, Scope, VerificationState, SunsetOrReview>`

For authority-bearing functions, IndependentBasis MUST NOT consist solely of:
- predecessor authority;
- succession itself;
- asset possession;
- technical/effective control;
- popularity;
- dependency;
- registry agreement;
- same-identity assertion.

> **AuthorityAfter Requires Its Own Valid Basis**

### 10.3 AuthorityNotTransferred

Each entry binds:
- AuthorityOrPower
- SourceHolder
- SourceFunctionID
- SourceScope
- ProposedOrActualDestination
- DestinationFunctionID
- NonTransferStateOrReason
- Evidence

This is mandatory wherever the transition touches an authority-bearing function.

> **Silence About Authority Transfer != Authority Transfer**

## 11. Anti-Laundering Rule for Split and Merger

Authority is never unioned merely because functions/services merge.

For each successor function:

`AuthorityAfter(scope) <= independently justified authority for that successor function and context`

This is a bounding relation, not a claim that authority is numerically measurable.

A merger MUST preserve the provenance of each predecessor authority basis and explicitly state which authority did not transfer.

> **Merger != Authority Union**

> **Split != Authority Replication**

## 12. Rollback and Reverse Transition

Rollback is represented as a new FunctionTransition/AssetTransition/AuthorityTransition set.

It does not revive historical authority automatically.

> **Rollback Of Function != Automatic Restoration Of Prior Authority**

A rollback records:
- current technical controller;
- current effective controller;
- current authority claim/basis;
- current threshold state;
- participant impact;
- residual state of failed successor;
- provenance linking the prior transition.

If no valid current authority basis exists, authority remains unresolved even if the predecessor resumes operation.

## 13. IdentityMapping

`IdentityMapping = <MappingID, SourceReference, DestinationReference, MappingType, Scope, EffectiveTime, Evidence, VerificationState, DisputeState>`

MappingType:
- SAME_CONTINUING_IDENTITY
- SUCCESSOR_IDENTITY
- FORKED_IDENTITY
- MERGED_IDENTITY
- RECONSTRUCTED_IDENTITY
- IDENTITY_UNRESOLVED
- IDENTITY_DISPUTED

> **Identity Mapping != Identity Sovereignty**

> **Same Identity != Same Authority**

## 14. ParticipantImpact

`ParticipantImpact = <ImpactID, FunctionScope, PopulationOrObjectScope, ImpactType, MaterialConsequence, RequiredAction, ContactOrChallengeRoute, ExitOrPortabilityEffect, EffectiveTime, Evidence, VerificationState>`

Impact types may include service interruption, changed operator/controller/authority basis/terms/contact/data location/rights/challenge route/exit/dependency, required action and no-action-needed.

Different populations may have different impacts.

> **Participant Dependency != Consent**

## 15. ResidualObservation

`ResidualObservation = <ObservationID, SubjectReference, ResidualType, Scope, DeclaredOrDiscovered, ObservedAt, EffectiveFromIfKnown, EffectiveUntilIfKnown, VerificationState, Evidence, DisputeState>`

ResidualType may include:
- KEY_ACCESS
- DATA_COPY
- ADMIN_ACCESS
- DOMAIN_CONTROL
- CONTRACTUAL_CONTROL
- FINANCIAL_CONTROL
- INFRASTRUCTURE_CONTROL
- DEPENDENCY_CONTROL
- LEGACY_READ_ACCESS
- OTHER
- UNKNOWN

DeclaredOrDiscovered distinguishes:
- DECLARED_AT_TRANSITION
- DISCOVERED_LATER
- UNKNOWN

Historical transition records are not rewritten merely because later residual control is discovered.

## 16. RetirementState

Retirement is a relation between declared institutional state and observed residual reality.

`RetirementState = <PredecessorReference, DeclaredState, EffectiveTime, ResidualObservationRefs, VerificationState, DisputeState>`

DeclaredState:
- RETIRED
- PARTIALLY_RETIRED
- LEGACY_READ_ONLY
- ARCHIVAL
- LIMITED_RESIDUAL_FUNCTION
- DORMANT
- FAILED_TO_RETIRE
- DISPUTED
- UNKNOWN

> **Declared Retirement != Demonstrated Loss Of Control**

> **Residual Access != Residual Governance**

## 17. Top-Level Transition Summary

A BSuR MAY provide a top-level TransitionSummaryState for navigation.

It is derived/non-authoritative when component transitions differ.

Examples:
- IN_PROGRESS
- PARTIALLY_COMPLETED
- COMPLETED
- FAILED
- DISPUTED
- ABORTED
- REVERSED
- MIXED
- UNRESOLVED

The summary MUST NOT overwrite component states.

> **Summary State != Component Truth**

## 18. Constitutional Threshold

Threshold state belongs to each AuthorityTransition/function where constitutionally material.

Relevant states remain:
- BELOW_THRESHOLD
- REVIEW_TRIGGERED
- THRESHOLD_UNRESOLVED
- CONSTITUTIONAL_BASIS_REQUIRED
- CONSTITUTIONALLY_GROUNDED
- CONSTITUTIONAL_BASIS_DISPUTED
- CONSTITUTIONAL_PROCESS_UNAVAILABLE

> **Institutional Continuity != Constitutional Grandfathering**

> **Constitutional Process Unavailable != Self-Authorisation**

## 19. Emergency Succession

Emergency continuity must record:
- emergency trigger;
- bounded function/scope;
- authority basis;
- start;
- sunset/review;
- current authority state;
- transition out of emergency;
- participant impact.

Expiry does not renew itself through usefulness or dependency.

> **Emergency Continuity != Permanent Authority**

## 20. Failed / Competing Succession

The model permits:
- no successor;
- several successors;
- competing successor claims;
- infrastructure without authority;
- authority without infrastructure;
- hostile takeover;
- predecessor refusal;
- hidden residual control;
- incomplete records;
- dependency capture;
- exit failure;
- fraudulent succession;
- identity dispute;
- failed successor;
- rollback;
- competing BSuRs.

Uncertainty remains explicit.

> **Unresolved Succession != Infrastructure-Holder Authority**

## 21. Legacy Access

LegacyAccess records:
- subject/system;
- purpose;
- access route;
- holder;
- authority basis;
- scope;
- review/sunset;
- evidence.

Legacy access for audit/history/recovery does not imply operational authority.

## 22. Provenance and Corrections

Preserve:
- predecessor/successor evidence;
- relation evidence;
- timestamps;
- disputes;
- corrections;
- source architecture;
- registry observations;
- dependency evidence;
- prior BSuR references.

Corrections append; they do not erase.

## 23. BSR Interaction

BSR = current service-state representation.

BSuR = transition representation.

A BSR current state may reference one or more BSuRs.

A BSuR may reference predecessor/successor BSR records as observations, but neither registry nor succession record adjudicates authority by publication.

## 24. Validation Layers

U1 Structural validity.  
U2 Referential validity.  
U3 Function source/destination binding.  
U4 Asset/control trace.  
U5 Record/protection trace.  
U6 Dependency/independence trace.  
U7 Authority before/after separation.  
U8 Independent authority basis.  
U9 Explicit non-transfer.  
U10 Anti-laundering split/merge check.  
U11 Constitutional threshold.  
U12 Temporal coherence.  
U13 Participant impact scope.  
U14 Identity mapping uncertainty.  
U15 Residual-control observation.  
U16 Retirement/residual consistency.  
U17 Rollback current-authority trace.  
U18 Provenance/dispute/correction trace.

> **BSuR Validity != Successful Succession**

> **Successful Functional Succession != Legitimate Authority Succession**

## 25. Invariants

BSuR-01 Function Continuity != Authority Continuity.  
BSuR-02 Infrastructure Continuity != Institutional Continuity.  
BSuR-03 Successor Claim != Successor Authority.  
BSuR-04 Asset Transfer != Authority Transfer.  
BSuR-05 Record Transfer != Authority Transfer.  
BSuR-06 Technical Control != Legitimate Authority.  
BSuR-07 Effective Control != Legitimate Authority.  
BSuR-08 AuthorityAfter Requires Independent Basis.  
BSuR-09 BSuR != Authority Grant.  
BSuR-10 Silence About Authority Transfer != Authority Transfer.  
BSuR-11 Popularity != Constitutional Authority.  
BSuR-12 Dependency != Authority.  
BSuR-13 Organisational Separation != Operational Independence.  
BSuR-14 Institutional Continuity != Constitutional Grandfathering.  
BSuR-15 Constitutional Process Unavailable != Self-Authorisation.  
BSuR-16 Identity Mapping != Identity Sovereignty.  
BSuR-17 Same Identity != Same Authority.  
BSuR-18 Multiple Successor Claims Must Remain Representable.  
BSuR-19 Failed Succession Must Remain Representable.  
BSuR-20 Unresolved Succession != Infrastructure-Holder Authority.  
BSuR-21 Emergency Continuity != Permanent Authority.  
BSuR-22 Residual Access != Residual Governance.  
BSuR-23 Retirement != Provenance Erasure.  
BSuR-24 Correction != Erasure.  
BSuR-25 Participant Dependency != Consent.  
BSuR-26 Service Discoverability != Recognition.  
BSuR-27 Registry Observation != Succession Adjudication.  
BSuR-28 BSuR Validity != Successful Succession.  
BSuR-29 Functional Success != Legitimacy Proof.  
BSuR-30 Transition Completion != Constitutional Grounding.  
BSuR-31 Merger != Authority Union.  
BSuR-32 Split != Authority Replication.  
BSuR-33 Rollback Of Function != Automatic Restoration Of Prior Authority.  
BSuR-34 Declared Retirement != Demonstrated Loss Of Control.  
BSuR-35 Summary State != Component Truth.  
BSuR-36 FunctionID Requires Service Context Across Succession.  
BSuR-37 Authority Non-Transfer Must Be Function/Scope Bound.  
BSuR-38 Hidden Residual Control Must Be Append-Representable.  
BSuR-39 Record Duplication != Transfer Completion.  
BSuR-40 Authority Scope Cannot Expand Solely Through Succession Topology.

## 26. Implementation Boundary

Downstream:
- JSON Schema;
- cryptographic/log integrity;
- network protocol;
- legal transfer instruments;
- constitutional founding/delegation procedure;
- identity provider;
- automated adjudication;
- UI.

## 27. Pre-Schema Status

Specification 002 repairs the relational failures found in Pre-Schema Adversarial Evaluation 001:
- source/destination binding;
- authority-transition binding;
- explicit scoped non-transfer;
- merger/split authority laundering;
- rollback;
- identity mapping;
- record/dependency transitions;
- scoped participant impact;
- residual observations;
- retirement/residual contradiction;
- component-vs-summary state.

It requires a second adversarial pass before serialization.
