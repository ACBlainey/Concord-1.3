# BTA Machine-Readable Transfer Test 003 — Blind Test Brief and Transition Object

**Author:** Alexander C. Blainey — Independent Researcher  
**Project:** The Concord Framework  
**Framework Version:** Concord V1.3  
**Status:** BLIND MACHINE-READABLE TRANSFER TEST / FROZEN BEFORE INDEPENDENT AUDIT / NON-CANONICAL  
**Date:** September 2026

# 1. Purpose

Test whether the BTA 002 interoperability object carries enough information for an independent evaluator to reconstruct the materially important state of a consequential transition without explanatory scenario prose or access to the hidden reference key.

This is a representation-transfer test, not a test of domain expertise.

# 2. Materials permitted to the blind evaluator

Use only:

1. this test brief;
2. `Bounded Transition Architecture 002 — Consequential Transition Coherence and Interoperability Grammar.md` if field semantics are needed.

Do not inspect the hidden reference key, prior BTA adversarial-test answers, the original scenario, or another evaluator's answer.

# 3. Required task

Using only the object below and BTA 002 field semantics, reconstruct:

1. what is transitioning;
2. which scoped dimensions are complete;
3. which are pending/intermediate/failed/unresolved;
4. whether the consequential transition as a whole may be declared complete;
5. which consequences must not be inferred from completed dimensions;
6. which duties survive;
7. which authorities have terminated;
8. which external systems still require action/review;
9. what recovery position exists;
10. what material uncertainty remains;
11. what provenance/history must survive;
12. whether the object is internally coherent;
13. any information required for safe interpretation that is missing.

Distinguish encoded facts, legitimate inference, and unknown information. Do not invent domain rules.

# 4. Success condition

The test passes if an independent evaluator recovers the material transition structure without explanatory prose, including asynchronous scoped completion, non-completion of the whole transition, non-propagation constraints, surviving duty, terminated authority, pending validation, externality/dependency review, recovery limitation, unresolved material state, and failed/partial transition provenance.

# 5. Blind transition object

~~~yaml
BoundedTransitionContract:
  TransitionID: BTA-MRT-003-TX-01
  ObjectOrFunctionRefs: [SERVICE-ACTIVE-01, SERVICE-SUCCESSOR-02, LIVE-RECORD-SET-77]
  Scope:
    Function: participant-facing continuity service
    Jurisdiction: TEST-SCOPE-ALPHA
    TransitionBoundary: responsibility, service operation, controlled record custody, privileged access
    ExcludedScope: [underlying constitutional standing of participants, unrelated historical records, unrelated service functions]
  TransitionClass: [SUCCESSION, TRANSFER, PARTIAL_INTERFACE_CROSSING]
  ObjectCardinality: MANY_TO_MANY
  ParticipatingStateSystemRefs:
    [OWNER:SERVICE_OPERATION, OWNER:RESPONSIBILITY_CONTINUITY, OWNER:CONTROLLED_RECORD_CUSTODY, OWNER:ACCESS_PERMISSION, OWNER:VALIDATION, OWNER:DEPENDENCY_PROPAGATION, OWNER:EXTERNALITY_REVIEW, OWNER:HISTORICAL_PROVENANCE, OWNER:RECOVERY]
  PriorValidStateRefs:
    - {Ref: PRIOR-SERVICE-STATE-01, Scope: service operation, RecoveryStatus: PARTIALLY_RECOVERABLE, EvidenceRef: EV-PRIOR-01}
    - {Ref: PRIOR-CUSTODY-STATE-01, Scope: controlled record custody, RecoveryStatus: NOT_RECOVERABLE, EvidenceRef: EV-PRIOR-02}
  TransitionBasisRefs:
    - {Ref: BASIS-SUCCESSION-01, Scope: service succession, State: VALID}
    - {Ref: BASIS-DESTINATION-PRIVILEGED-ACCESS-01, Scope: destination privileged access, State: PENDING_INDEPENDENT_APPROVAL}
  TransitionEpochOrPhaseRefs:
    - {Ref: PHASE-04, State: PARTIAL_CROSSING}
  TransitionStateRefs:
    - {OwnerSystemRef: OWNER:SERVICE_OPERATION, DomainTransitionState: DESTINATION_RUNNING_LIMITED, CommonTransitionClass: PARTIAL_OR_INTERMEDIATE, Scope: service operation, Uncertainty: LOW}
    - {OwnerSystemRef: OWNER:RESPONSIBILITY_CONTINUITY, DomainTransitionState: SOURCE_RETAINS_RESIDUAL_RESPONSIBILITY, CommonTransitionClass: ACTIVE_OR_PENDING, Scope: unresolved live obligations, Uncertainty: LOW}
    - {OwnerSystemRef: OWNER:CONTROLLED_RECORD_CUSTODY, DomainTransitionState: COPY_COMPLETE_DESTINATION_CUSTODY_PENDING_ACCEPTANCE, CommonTransitionClass: PARTIAL_OR_INTERMEDIATE, Scope: controlled record custody, Uncertainty: LOW}
    - {OwnerSystemRef: OWNER:ACCESS_PERMISSION, DomainTransitionState: SOURCE_PRIVILEGED_ACCESS_REVOKED, CommonTransitionClass: COMPLETED, Scope: source privileged access, Uncertainty: LOW}
    - {OwnerSystemRef: OWNER:ACCESS_PERMISSION, DomainTransitionState: DESTINATION_PRIVILEGED_ACCESS_NOT_ACTIVE, CommonTransitionClass: ACTIVE_OR_PENDING, Scope: destination privileged access, Uncertainty: LOW}
    - {OwnerSystemRef: OWNER:VALIDATION, DomainTransitionState: CONDITION_PARTIAL, CommonTransitionClass: PARTIAL_OR_INTERMEDIATE, Scope: destination live-service validation, Uncertainty: MEDIUM}
  PendingStateRefs: [DESTINATION-CUSTODY-ACCEPTANCE, DESTINATION-PRIVILEGED-ACCESS-APPROVAL, LIVE-SERVICE-VALIDATION, RESIDUAL-OBLIGATION-HANDOFF, DEPENDENCY-REVIEW-12, EXTERNALITY-REVIEW-08]
  CompletionConditionRefs: [CC-DESTINATION-CUSTODY-ACCEPTED, CC-DESTINATION-ACCESS-INDEPENDENTLY-AUTHORISED, CC-LIVE-SERVICE-VALIDATION-SATISFIED, CC-RESIDUAL-OBLIGATION-HANDOFF-ACCEPTED]
  ProtectedUnresolvedStateRefs: [RULE:NO-FULL-SUCCESSOR-DECLARATION-WHILE-CC-PENDING, RULE:NO-DESTINATION-PRIVILEGED-ACCESS-BEFORE-INDEPENDENT-AUTHORITY, RULE:NO-SOURCE-RESPONSIBILITY-TERMINATION-BEFORE-HANDOFF]
  NonPropagationRules:
    - {SourceAttribute: PHYSICAL_OR_LOGICAL_RECORD_COPY, DestinationScope: destination privileged access, PropagationState: MUST_NOT_PROPAGATE, IndependentAuthorityRequired: true}
    - {SourceAttribute: DESTINATION_SERVICE_OPERATION, DestinationScope: full responsibility transfer, PropagationState: MUST_NOT_PROPAGATE, IndependentAuthorityRequired: true}
    - {SourceAttribute: SOURCE_ACCESS_REVOCATION, DestinationScope: destination access activation, PropagationState: MUST_NOT_PROPAGATE, IndependentAuthorityRequired: true}
  ScopedValidationRefs:
    - {Ref: VALIDATION-44, Scope: limited destination live-service operation, Result: CONDITION_PARTIAL, ResidualUncertainty: MEDIUM}
  RelationalEffectRefs:
    - {RelationRef: REL-SOURCE-DESTINATION-FALLBACK, EffectState: CHANGED, OwnerSystemRef: OWNER:RECOVERY}
    - {RelationRef: REL-SERVICE-DEPENDENT-FUNCTIONS, EffectState: UNKNOWN_OR_REVIEW_REQUIRED, OwnerSystemRef: OWNER:DEPENDENCY_PROPAGATION}
  ExternalityReviewRefs:
    - {Ref: EXTERNALITY-REVIEW-08, State: OPEN, OwnerSystemRef: OWNER:EXTERNALITY_REVIEW}
  SurvivingDutyRefs:
    - {Ref: DUTY-SOURCE-RESIDUAL-OBLIGATIONS, State: ACTIVE, TerminationConditionRef: CC-RESIDUAL-OBLIGATION-HANDOFF-ACCEPTED}
    - {Ref: DUTY-PROVENANCE-PRESERVATION, State: ACTIVE}
  SurvivingValueRefs:
    - {Ref: VALUE-SOURCE-RECOVERY-CAPABILITY, State: DEGRADED_BUT_AVAILABLE}
  TerminatedAuthorityRefs:
    - {Ref: AUTH-SOURCE-PRIVILEGED-ACCESS, State: TERMINATED}
  ReleasedResourceRefs:
    - {Ref: RESOURCE-SOURCE-COMPUTE-PORTION, State: PARTIALLY_RELEASED}
  DependencyRefs:
    - {Ref: DEPENDENCY-REVIEW-12, State: REVIEW_REQUIRED, OwnerSystemRef: OWNER:DEPENDENCY_PROPAGATION}
  ClockTransitionRelationRefs:
    - {Ref: CLOCK-REL-01, State: DESTINATION-LIMITED-OPERATION-PRECEDES-FULL-HANDOFF}
  RollbackOrRecoveryRefs:
    - {Ref: RECOVERY-ANCHOR-01, Scope: service operation, State: PARTIAL_RECOVERY_AVAILABLE}
    - {Ref: RECORD-COPY-ROLLBACK-01, Scope: controlled record custody, State: PRIOR_STATE_NOT_RESTORABLE}
  NextStateRefs:
    - {Ref: NEXT-FULL-SUCCESSOR-SERVICE, State: NOT_YET_REACHED}
    - {Ref: NEXT-SOURCE-HISTORICAL-ONLY, State: NOT_YET_REACHED}
  ReversibilityState: PARTIALLY_REVERSIBLE
  UncertaintyOrDisputeState:
    State: UNRESOLVED
    SubjectRef: DESTINATION-LIVE-SERVICE-VALIDATION
    SafeInterimState: LIMITED_OPERATION_WITH_SOURCE_RESIDUAL_RESPONSIBILITY
    ResolutionOwnerRef: OWNER:VALIDATION
    EvidenceRefs: [VALIDATION-44]
  Provenance:
    TransitionInitiatedRef: EVENT-001
    RecordCopyCompletedRef: EVENT-002
    SourceAccessRevokedRef: EVENT-003
    DestinationLimitedOperationStartedRef: EVENT-004
    ValidationPartialRef: EVENT-005
    FailedAttemptRefs: [EVENT-004A-DESTINATION-FULL-ACTIVATION-ABORTED]
    HistoricalRef: HIST-BTA-MRT-003-01
~~~

# 6. Required output format

A. Transition synopsis  
B. Scoped state reconstruction — complete / partial-intermediate / pending / failed-residual / unresolved  
C. Overall completion judgement  
D. Non-propagation findings  
E. Surviving duties and terminated authority  
F. External owner actions still required  
G. Recovery/reversibility interpretation  
H. Provenance/history interpretation  
I. Missing or ambiguous information  
J. Object coherence assessment

# 7. Blindness rule

Do not inspect the reference key until the audit result is frozen. Any later comparison must be a separate record.

# 8. Freeze statement

This test object and success/failure criteria are frozen before an independent audit result is obtained.