# Historical Domain — Formal Schema Set 001 — Core Objects and Interfaces

**Project:** The Concord
**Domain:** Historical
**Status:** DEVELOPMENT SCHEMA / NOT CANONICAL
**Date:** 25 September 2026
**Basis:** Historical Formal Domain Specification v0.3

## 1. Purpose

This document extracts the principal v0.3 objects and interfaces into implementation-neutral schemas. It does not prescribe a database, language, storage engine or API.

All schemas inherit the Historical invariants. Identifiers are references, not claims of central ownership. Schemas may be distributed provided required relationships remain reconstructable.

## 2. HSO-1 — Historical State Object

Fields:

- HistoricalObjectID
- SourceDomain
- SourceObjectRef
- InformationClass
- EventTime
- StateEffectiveTime
- RecordCreationTime
- HistoricalCustodyTime
- VersionOrStateID
- EpistemicStatus
- AuthorityStatus
- PrivacyState
- ClassificationState
- RetentionState
- AccessState
- ProvenanceRefs
- RelationshipRefs
- TransformationRefs
- CorrectionRefs
- KnownUncertainty
- KnownDisputes
- EvaluationContextRef
- SearchBoundaryRef
- CompletenessScope
- SupersessionRefs
- CurrentOperationalRef
- CustodyMode
- ReviewCondition

Event time, creation time, effective time and custody time must remain distinguishable.

## 3. HEC-1 — Historical Evaluation Context

Fields:

- EvaluationContextID
- SubjectRef
- EffectiveTime
- PotentialEvidenceKnown
- AccessibleEvidence
- InaccessibleEvidenceKnown
- ObservedEvidence
- RepresentedVariablesOrCategories
- MethodOrModelRefs
- InterfaceOrSensorLimits
- SearchOrSamplingBoundaryRef
- KnownUnknowns
- KnownMissingDimensions
- ContemporaryUncertainty
- ContemporaryScopeClaim
- DecisionContextRef
- LaterDiscoveredDimensions
- RetrospectiveInterpretationRefs

Unknown-state typing must support KNOWN_UNKNOWN, KNOWN_MISSING_DIMENSION and LATER_RECOGNISED_UNREPRESENTED_DIMENSION.

## 4. HPR-1 — Provenance Relationship

Fields:

- RelationshipID
- FromRef / ToRef
- RelationshipType
- EffectiveStart / EffectiveEnd
- AssertionTime
- SourceRef
- EpistemicType
- PrivacyState
- AccessState
- IdentityExposureState
- DisputedState
- SupersessionRef

Relationship types may include DERIVED_FROM, SUPERSEDES, CORRECTS, CHALLENGES, INVALIDATES, DEPENDS_ON, CONTRIBUTED_TO, TEMPORALLY_FOLLOWS, ALTERNATIVE_TO, DISPUTES, SHARES_PROVENANCE_WITH, AUTHORIZED_BY, DELEGATED_BY, DECIDED_BY, REVIEWED_BY, REVOKED_BY, EXPIRED_BY and IMPLEMENTED_BY.

**Shared Provenance ≠ Shared Identity.**

## 5. HAE-1 — Authority Activation and Exercise Record

Fields:

- AuthorityEventID
- PreExerciseContextRef
- ActorOrInstitutionRef
- StandingEligibilityRef
- AuthoritySourceRef
- LegitimateFunction
- FunctionalNeed
- ActivationConditions
- ConditionsSatisfiedEvidence
- PermittedAction
- ObjectOrTargetRef
- JurisdictionOrSpace
- Scope
- AffectedRights
- ActivationTime
- ExerciseTime
- TerminationTime / TerminationCondition
- ExerciseDescription
- ConsequenceRefs
- PostExerciseContextRef
- ClaimedAuthorityState
- ContemporaneousRecognitionState
- ContestState
- LaterAdjudicationRefs
- CurrentInterpretationRef
- ProvenanceRefs
- EvaluationContextRef

Authority states may include CLAIMED, ACTIVATED, EXERCISED, CONTESTED, CONTEMPORANEOUSLY_RECOGNISED, EXPIRED, REVOKED, SUPERSEDED, INVALIDATED, HISTORICAL_ONLY, STATUS_UNKNOWN and STATUS_DISPUTED.

For discrete exercises:

C0 → justification → A1 activation → bounded exercise → A1 terminates/is consumed → C1.

The schema must not represent authority as an unbounded reusable property of an actor.

## 6. HIST-1 — Information-State Transition Record

Fields:

- TransitionID
- AffectedObjectOrClassRef
- PreviousInformationState
- NewInformationState
- TransitionType
- AuthorisingProcessRef
- AuthorityEventRef
- LegitimatePurpose
- EffectiveTime
- Scope
- AffectedRelationshipClasses
- KnownDerivativeRefs
- KnownReplicaRefs
- ExecutionStatus
- ReconciliationStatus
- ReviewOrAppealState
- MinimumResidueRef
- ProvenanceRefs
- CompletenessScope

Transition types may include REDUCE_DISCOVERABILITY, RESTRICT_ACCESS, RESTRICT_CORRELATION, PSEUDONYMISE, ANONYMISE, AGGREGATE, SEAL, CRYPTOGRAPHICALLY_DISABLE, RECLASSIFY, PARTIALLY_DISCLOSE and DESTROY.

## 7. HCP-1 — Correlation Permission

Fields:

- CorrelationPermissionID
- ActorOrProcessRef
- InputRecordClasses
- PermittedJoinKeysOrRelationshipTypes
- ProhibitedJoinKeysOrRelationshipTypes
- LegitimateFunction
- Purpose
- AuthoritySourceRef
- Scope
- ActivationTime
- ExpiryOrTerminationCondition
- OutputRestrictions
- IdentityExposureLimit
- AuditRequirement
- ReviewRequirement

**Access(A) + Access(B) ≠ PermissionToCorrelate(A,B).**

## 8. HMHR-1 — Minimum Necessary Historical Residue

Fields:

- ResidueID
- DestroyedObjectClassRef
- ExistenceMarkerPermitted
- TransitionType
- AuthorisingProcessRef
- EffectiveTime
- DestructionScope
- AffectedDerivativeClasses
- AuditReference
- ProhibitedContentDescription
- ReconstructionRiskAssessment
- AccessState
- RetentionState

The residue must not contain sufficient sensitive substance to defeat the destruction decision.

**Destruction Provenance ≠ Reconstruction of Destroyed Content.**

## 9. HSE-1 — Historical Secrecy Envelope

Fields:

- SecrecyEnvelopeID
- ProtectedObjectRef
- SecrecyJustification
- AuthoritySourceRef
- AuthorityEventRef
- Scope
- PermittedActorsOrClasses
- PermittedActions
- EffectiveStart
- ReviewTime
- ExpiryCondition
- DisclosureCondition
- CurrentSecrecyState
- ReviewHistoryRefs
- PartialDisclosureRefs
- ResidualProtectedElements
- ProvenanceRefs

States include ACTIVE_OPERATIONAL_SECRECY, SEALED_PENDING_REVIEW, CONTINUED_SECRECY_REJUSTIFIED, PARTIALLY_DISCLOSED, DISCLOSED, SECRECY_EXPIRED and STATUS_DISPUTED.

A permanent unqualified Boolean such as Secret=true is insufficient.

## 10. HSB-1 — Historical Search Boundary

Fields:

- SearchBoundaryID
- QueryOrQuestion
- CorpusRefs / CorpusVersions
- SearchMethod
- SearchTermsOrSelectors
- TraversalPath
- DepthOrCoverage
- Exclusions
- InaccessibleAreas
- KnownMissingSources
- StartTime / StopTime
- StoppingRule
- SaturationBasis
- ResultType
- CompletenessClaimScope
- ReopeningCondition

A consequential NO_RECORD_FOUND result should reference this object.

**No Record Found Within Evaluated Space ≠ Event Did Not Occur.**


## 11. HCR-1 — Historical Correction Relationship

Fields: CorrectionID, OriginalRef, LaterRef, CorrectionType, EffectiveTime, AssertionTime, EvidenceRefs, AuthorityOrMethodRef, EpistemicStatus, DisputeState and ProvenanceRefs.

CorrectionType must distinguish COMMENT, CHALLENGE, CONTEXTUAL_ADDITION, CORRECTION, SUPERSESSION, REVERSAL and INVALIDATION. The original historical state remains reconstructable.

## 12. HCM-1 — Custody Mode Record

Fields: CustodyRecordID, SourceObjectRef, SourceDomain, CustodyMode, EffectiveStart/End, OperationalCustodianRef, HistoricalCustodianRef, ContentLocationRef, HistoricalReferenceRef, PrivacyState, RetentionState, AccessState, HandoffAuthorityRef, ReviewCondition and ProvenanceRefs.

CustodyMode supports TRANSFER, DUAL_CUSTODY and REFERENCE_PRESERVATION.

**Historical Handoff ≠ Mandatory Ownership Transfer.**

## 13. HRS-1 / HRO-1 — Reconstruction Request and Output

A request should identify actor, purpose, legitimate function, authority/permission, subject/domain, requested time, reconstruction mode, permitted/restricted source classes, pattern permission, epistemic detail, correlation permissions and output access state.

Modes include CONTEMPORARY_STATE and PRESENT_BEST.

An output should expose temporal scope, source coverage, findings, relationships, inferences, search boundaries, evaluation contexts, missing sources, uncertainty, disputes, retrospective evidence, completeness scope, coverage/confidence statement, method/tool and provenance.

Preserved evidence must remain distinguishable from derived inference.

## 14. HES-1 — Historical Event Spine View

Fields include subject/event, temporal scope, source events, domain transitions, knowledge changes, dependency effects, authority events, decisions, operational outcomes, corrections, alternative branches, negative space, source coverage, search boundaries and completeness scope.

This is a view over provenance-bearing relationships, not an independent civilisation-wide Event Spine database.

## 15. HER-1 — Emergency Recovery Sequence

Fields include EmergencyRef plus threat reduction, de-escalation, authority sunset, access reversion, data review, secrecy review, institutional reversion, rights restoration, dependency cleanup, post-emergency audit, unresolved recovery issues, completion scope and provenance.

**Emergency End ≠ Instantaneous Restoration of Normal State.**

## 16. HRI-1 — Replica and Integrity Record

Fields include ReplicaSetID, ObjectOrClassRef, ReplicaRefs, CustodyDomains, Jurisdictions, privacy/access/secrecy/retention states, last integrity check, relationship and semantic integrity status, pending information-state transitions, reconciliation status, unreachable replicas and completeness scope.

**Redundancy ≠ Uncontrolled Replication.**

## 17. Interface HI-1 — Operational Domain to Historical

Minimum handoff semantics:

SourceDomain + SourceObjectRef + HandoffMode + CurrentSourceState + RelevantTimes + Provenance + Relationships + AuthorityContext + EvaluationContext + Privacy + Classification/Secrecy + Retention + Uncertainty + CorrectionState + DestructionConstraints + ReviewConditions.

Historical returns a provenance-bearing custody acknowledgement/reference state.

## 18. Interface HI-2 — KCS to Historical

KCS exposes knowledge identity, state at T, dependencies, correction/supersession, materiality/review state, provenance and version state.

Historical preserves temporal projections rather than creating a competing current dependency graph.

**REVIEW_REQUIRED ≠ Invalid.**

## 19. Interface HI-3 — Civil Attention to Historical

Historical preserves the relation between original submission, Issue ID, classification/routing history, Domain Actions, domain status returns, central resolution, participant feedback/review and reopening.

**Domain Completion ≠ Issue Resolution.**

## 20. Interface HI-4 — Authority Systems to Historical

Authority-bearing domains should expose enough to reconstruct:

**Context → Justification → Authority Activation → Exercise → Consequence → Changed Context**

Historical preserves the event; it does not validate current authority.

## 21. Interface HI-5 — Information-State Change Propagation

**Authorised Transition → Resolve Known Material Dependencies → Domain-Specific Transition Requirement → Domain Execution → Status Return → Reconcile Known Holdings → Record Scoped Completion**

Unknown copies remain an ESCP limitation. No global deletion claim may be made solely because all known systems responded.

## 22. Interface HI-6 — Historical Query

A consequential query requires enough context to resolve:

**Actor + Subject + Action + Purpose + Legitimate Function + Context + Time + Permission + Reconstruction Mode**

Correlation permission is separately resolvable.

## 23. Forbidden Schema Collapses

The following simple states are architecturally insufficient when they erase required context, scope, time, provenance or purpose:

- Authority=true/false
- Secret=true/false
- Deleted=true/false
- Anonymous=true/false
- Historical=true/false
- Complete=true/false
- Accessible=true/false

Particularly dangerous collapses include current vs historical state; record existence vs event existence; anonymity vs non-reidentifiability; preservation vs access; source vs derivative deletion; authority eligibility vs activation; activation vs reusable permission; emergency end vs completed recovery; classification vs reality; and judicial finding vs ontological truth.

## 24. Minimum Referential Rules

1. Derived objects trace to source/provenance or state provenance unknown.
2. Corrections reference the state challenged or modified.
3. Authority events reference authority source and context where knowable.
4. Destructive transitions identify known derivative/replica scope or state that it is unknown.
5. Consequential negative searches reference a Search Boundary.
6. Present-Best reconstructions distinguish later evidence from contemporary evidence.
7. Correlation-derived objects reference their correlation authority where required.
8. Sealed records carry review/expiry semantics or a documented lawful reason why ordinary expiry is unavailable.
9. Event Spine claims trace to underlying provenance objects.
10. Complete-execution claims state evaluated scope.

## 25. Minimum Machine-Readable Distinctions

A conforming implementation must be able to express: current/historical; contemporaneous/retrospective; known/unknown/disputed; known-missing/later-unrepresented; observation/interpretation; claim/finding; correlation/causation; claimed/activated/exercised/adjudicated authority; active/expired/revoked/invalidated authority; operational/archival custody; transfer/dual/reference custody; preserved/discoverable/accessible/correlatable; anonymous/identity-restricted/identity-unknown; source/derivative; source deletion/derivative state; secrecy active/review/expired; emergency active/recovery incomplete/recovery complete; Domain Action complete/parent Issue resolved; record absent/search-negative-within-scope; documentary preservation/capability recoverability.

## 26. Adversarial Validation Queue

The schema set should next be tested against:

1. repeated privacy-state change;
2. authority valid at exercise but later adjudicated unlawful;
3. source deleted while trained model survives;
4. anonymous records reidentified through graph joins;
5. missed secrecy review;
6. repeated emergency renewal;
7. KCS current state changes while Historical reconstruction correctly remains old;
8. Civil Attention reopens a resolved issue;
9. replica offline during destruction;
10. later evidence exposes an unrepresented dimension;
11. incompatible cross-jurisdiction retention states;
12. preserved but unrecoverable capability;
13. retrospective testimony mistaken for contemporaneous evidence;
14. Event Spine silently omits an inaccessible domain;
15. individually accessible records whose correlation is not authorised.

The objective is to determine whether failure remains visible rather than being silently collapsed.

## 27. Status

**Formal Schema Set 001:** COMPLETE / DEVELOPMENT DRAFT

**Principal object schemas:** 12

**Primary interfaces:** 6

**Implementation technology selected:** NONE

**Database architecture selected:** NONE

**Centralised storage required:** NO

**Next:** Adversarial Schema Test 001 — State, Authority, Correlation, Destruction and Cross-Domain Failure Cases
