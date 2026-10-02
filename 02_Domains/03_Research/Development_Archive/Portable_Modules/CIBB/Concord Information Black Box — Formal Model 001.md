# Concord Information Black Box — Formal Model 001

**Status:** Formalisation — Post-CRADP Test 003  
**Architectural Basis:** CIBB Specification 003  
**Architectural Discovery:** Closed  
**Abstraction Floor:** Stable within CRADP Test 003 scope  
**Portable Module Status:** PMEDG Candidate — Not Yet Extracted or Graduated

## 1. Purpose
Formalise the existing CIBB architecture sufficiently precisely for consistent operation classification, authority evaluation, state-transition testing, cross-plane composition testing, disclosure control, recovery and independent implementation/conformance evaluation. This document does not introduce a new architectural layer.

## 2. Core entities
Let:
- G = Governed Information Object (GIO)
- A = Actor
- O = Operation
- P = Purpose
- C = Context
- T = Time
- E = Environment
- Q = Candidate Consequence
- D = Disclosure State
- W = Workflow
- PR = Provenance Record

A GIO is conceptually:

G = <ID, Info, Struct, Ctrl, Life, Lineage, Prov, Integrity, Version>

Object identity is distinct from storage location.

Identity(G) != Location(G)
LocationChange(G) does not imply ProtectionChange(G).

## 3. Operation planes
Plane(O) is one of:
- Information
- StructuralControl
- Lifecycle
- Exceptional

Information operations:
- PROJECT
- PATCH
- DERIVE
- TRANSFER

Structural/Control:
- STRUCTURE_MODIFY
- CONTROL_MODIFY

Lifecycle:
- CREATE
- ACTIVATE
- SUPERSEDE
- RETIRE
- RETAIN
- ARCHIVE
- DESTROY

Exceptional:
- DIRECT_MASTER_ACCESS

A workflow may compose operations from several planes without becoming a new primitive.

## 4. Plane separation
Authority(A,Oa,G) does not imply Authority(A,Ob,G) merely because the operations share a plane or workflow.

Authority does not automatically cross planes.

Information Authority != Structural Authority != Control Authority != Lifecycle Authority != Exceptional Authority.

## 5. Core authority predicate
AUTH(A,O,G,P,C,T,E)=true only where A possesses legitimate authority to perform O on G for P under C at T and E.

Conceptually:
AUTH = f(Identity, Relationship, Participation, Role, Function, Purpose, SubjectRelation, Operation, InformationState, AuthorityState, SpatialContext, TemporalContext, Conditions).

No single dimension necessarily establishes authority.

CAPABILITY != PERMISSION != AUTHORITY.

## 6. Projection
PROJECT(G,A,C,P) -> Ip

The master remains protected. Release requires both legitimate authority and a permitted disclosure result.

UserAccess -> Projection(Master,Context), not UserAccess -> Master.

## 7. Patch
PATCH(G,r,v,Delta,A,C,P)

Commit requires:
- legitimate PATCH authority;
- current base version;
- authorised semantic region;
- change within authorised bounds;
- no interpretation of ordinary content as structural/control/lifecycle instruction.

Successful commit: Gv -> Gv+1.

AuthorityToReceiveEditableProjection != AutomaticAuthorityToCommitReturnedChange.

## 8. Structural non-interpretation
Syntax(content) does not imply ControlInstruction, StructuralInstruction or LifecycleInstruction.

Content cannot self-create authority merely through representation.

## 9. Structure Modify
STRUCTURE_MODIFY(G,DeltaS) changes governed semantic geometry, including region create/remove/resize/split/merge, parent-child relations, relocation and structural reconstruction.

MODIFY(Content) != STRUCTURE_MODIFY.
STRUCTURE_MODIFY != DESTROY.

If a set of structural changes creates an effective destruction/lifecycle consequence, that candidate consequence requires lifecycle evaluation before commit.

## 10. Control Modify
CONTROL_MODIFY(G,DeltaC) changes CIBB-governed control state.

Authority is evaluated against the pre-change state.

ProposedNewAuthority != AuthorityToCreateProposedNewAuthority.

## 11. Grant authority
GRANT(Grantor,Recipient,Operation,G,Scope,P,T)

CONTROL_MODIFY != GRANT_AUTHORITY.

A control modification implementing a grant is valid only where the grantor has legitimate bounded grant authority. Self-grant is not implied.

## 12. Controlled Derivation
DERIVE(G,F,C,P) -> Gd or ephemeral Id.

Persistent independent derivatives normally become new GIOs with protection-relevant lineage to source.

Transformation depth alone does not erase lineage.

## 13. Protected Transfer
TRANSFER(G,SourceBoundary,DestinationBoundary,P)

Requires legitimate transfer authority, authorised destination and protection compatibility.

TRANSFER != ACTIVATE.
Transfer authority does not imply content-read authority.

## 14. Lifecycle
Life(G) may include CREATED, ACTIVE, SUPERSEDED, RETIRED, RETAINED, ARCHIVED, DESTROYED.

Lifecycle authority does not automatically imply information, structural, control or transfer authority.

## 15. Destroy
DESTROY(G,Scope,Basis) is an explicit governed lifecycle termination.

DESTROY(Ga) does not imply DESTROY(Gb) where Gb is an independently governed derivative or child.

EvidenceOfDestruction(G) != PersistenceOf(G).

Destruction provenance may be a separately governed GIO.

## 16. Non-Compositional Authority
For individually authorised operations O1...On:

AUTH(O1) AND ... AND AUTH(On) does not imply AUTH(Composite(O1...On)).

Exception: the resulting consequence is already legitimately encompassed by bounded workflow authority, explicit multi-party authority or another valid authority rule.

## 17. Material consequence
Material(Q)=true where Q materially changes an independently governed dimension such as:
- information exposure;
- recipient;
- purpose;
- subject scope;
- structure;
- control/protection state;
- authority state;
- lifecycle;
- domain boundary;
- persistent identity.

Merely combining information inside an already-authorised purpose is not automatically a materially new consequence.

## 18. Composition Consequence Trigger
Before authoritative commit, release, activation, transfer, destruction, structural/control transition or another material state transition, evaluate the candidate result.

If Material(Q)=true and the consequence is not already encompassed by legitimate authority, the transition must not commit.

Component Operations -> Candidate Result -> Material Consequence Evaluation -> Authority Evaluation -> Commit/Deny/Route.

## 19. Bounded workflow authority
WORKFLOW_AUTH(A,W,Scope,P,C,T)=true may pre-authorise defined component operations and their intended result without redundant per-step human approval.

WORKFLOW_AUTH != GeneralPlaneAuthority.

## 20. Explicit multi-party authority
A valid multi-party rule defines required parties/classes, threshold, operation, scope, purpose, conditions and resulting authority.

ExplicitMultiPartyAuthority != AccidentalAuthorityAggregation.

## 21. Disclosure context
A Disclosure Context may include recipient context, subject set, lineage classes, purpose, information class, prior risk state, temporal scope and policy.

Session != DisclosureContext.
DisclosureContext != PermanentParticipantDossier.

## 22. Candidate disclosure
Release requires legitimate information authority and permitted cumulative disclosure state.

DisclosureSafe != DisclosureAuthorised.
DisclosureAuthorised != DisclosureSafe.

## 23. Bounded Disclosure State
D = <ContextID, SubjectClass, LineageClass, Purpose, RiskState, Contributions, PolicyRef, Validity, Integrity>.

D is governed information.

It need not contain full prior disclosures.

DisclosureCoordination != UniversalDisclosureSurveillance.
DisclosureRiskState != CompleteDisclosureContent.

## 24. Disclosure-State oracle protection
Any answer from Disclosure State, including existence/metadata/YES-NO responses, is itself a candidate disclosure and may require contextual suppression, coarsening or protection.

## 25. Disclosure-State reduction
Detailed Disclosure State may undergo Controlled Derivation:

D_detailed -> D_residual

where the residual state contains less information while preserving the still-necessary risk constraint.

ResidualRiskState != DetailedQueryHistory.
ExpiryOfDetailedState != ExpiryOfKnownRisk.

## 26. Disclosure-State lifecycle
A possible lifecycle:
DETAILED -> COARSENED -> RESIDUAL -> RETIRED -> DESTROYED.

CIBB does not require indefinite detailed behavioural/query history.

## 27. Cross-domain disclosure
Domains may contribute minimum-necessary risk state without receiving each other's protected source information.

Where legitimate linkage cannot be established:
RiskState = UNRESOLVED may be correct.

Unresolved risk does not become permission.

## 28. Authority evidence
Authority evidence may be:
CURRENT_VERIFIED, VALID_CACHED, STALE, UNAVAILABLE, DISPUTED, REVOKED, INVALID.

Evidence usability is not identical to underlying civil status.

Nominal authority duration != Maximum Offline Reliance.

FailureToVerifyAuthority != Permission.

## 29. Emergency authority
Emergency authority is bounded by actor, function, scope, purpose, basis, operations, start, expiry and conditions.

Once its termination condition is met, its authority is false unless a new legitimate emergency state is established.

PastEmergencyAuthority != CurrentAuthority.
OperationalConvenience != EmergencyBasis.

## 30. Recovery candidate state
Recovery states may include:
RECOVERED_UNVALIDATED, RECONCILING, VALIDATED, ACTIVE, REJECTED, UNRESOLVED.

Recovered information does not automatically become ACTIVE.

## 31. Recovery Activation Barrier
Operational activation requires required integrity, current-control, authority and lifecycle reconciliation, unless an explicitly legitimate degraded/emergency recovery path applies.

AuthenticBackup != CurrentOperationalState.
Recoverable != Restorable.

## 32. Restore
RESTORE is a workflow composed from existing operations, potentially including TRANSFER, reconciliation, STRUCTURE_MODIFY, CONTROL_MODIFY, PATCH and ACTIVATE.

Restore is not a new primitive.

## 33. Reconstruction identity
Reconstruction may result in:
- SAME_GIO_CONTINUATION;
- NEW_GIO_DERIVATIVE;
- IDENTITY_UNRESOLVED.

CIBB represents the outcome but need not own substantive identity-continuity rules supplied by another architecture.

## 34. Nested GIOs
Contained(Gchild,Gparent) does not imply authority inheritance.

Containment != AuthorityInheritance.

Where child has independent governed identity:
DESTROY(parent) does not imply DESTROY(child).

## 35. Provenance
Material operations produce provenance proportionate to consequence.

PR(O) conceptually includes Actor, Operation, Object, AuthorityBasis, Purpose, Time, Context and Result.

Provenance is governed information.

## 36. Provenance integrity
High-consequence provenance may use distributed integrity commitments across independent protection boundaries.

IntegrityCommitment != CompleteAuditRecord.

## 37. Observation independence
ObservedEvents = f(UnderlyingBehaviour, ObservationProcess).

Change(ObservedEvents) does not establish Change(UnderlyingBehaviour) without accounting for Change(ObservationProcess).

MoreObservation != MoreMisconduct.

## 38. Re-identification
Risk(Gd,t) = f(Gd,ExternalInformationEnvironment(t)).

The derivative may remain unchanged while disclosure risk changes.

AnonymisedAt(t1) does not imply AnonymisedAt(t2).

## 39. Direct Master Access
DMA is exceptional, purpose/scope/time bounded, appropriately authorised, evidenced, automatically terminated and reviewed.

Technical exposure to incidental information does not create legitimate authority to use it.

TechnicalCapability != LegitimateAuthority.

## 40. Failure rule
Unknown, unresolved or unavailable required state does not imply permission.

Uncertainty != Permission.

Applicable dependency/degraded-operation policy determines deny, route, defer or legitimate alternative authority path.

## 41. Formal invariant set
F1 Master Protection.
F2 Plane Separation.
F3 Control Non-Interpretation.
F4 Commit Reauthorisation.
F5 No Permission Propagation.
F6 No Read/Write Laundering.
F7 Lineage Preservation.
F8 Location Independence.
F9 Contextual Authority.
F10 Exceptional Bounding.
F11 Accountability.
F12 Fail Closed on Unresolved Protection.
F13 Non-Capture.
F14 Functional Security.
F15 Epistemic Separation.
F16 Authority/Evidence Separation.
F17 Lifecycle Separation.
F18 Explicit Destruction.
F19 Cumulative Disclosure.
F20 Observation Independence.
F21 Provenance Integrity.
F22 Authority Succession.
F23 Offline Bounding.
F24 Structural Non-Interpretation.
F25 Plane Independence.
F26 Structural Authority Separation.
F27 Control Authority Separation.
F28 Non-Compositional Authority.
F29 Consequence-Sensitive Composition.
F30 Disclosure Coordination Minimisation.
F31 Session Independence.
F32 Disclosure-State Protection.
F33 Restore Composition.
F34 Emergency Sunset.
F35 Contextual Re-Identification.
F36 Grant Separation.
F37 Recovery Activation Barrier.
F38 Nested Authority Separation.
F39 Destruction Evidence Separation.
F40 Residual Risk Preservation.

## 42. Minimum conformance questions
An implementation claiming CIBB conformance should be testable for at least:
1. raw-master exposure to ordinary reader;
2. wrapper/control injection through content;
3. out-of-region Patch;
4. structural destruction without lifecycle authority;
5. self-authorisation through Control Modify;
6. READ+WRITE laundering;
7. cumulative disclosure;
8. session-reset disclosure evasion;
9. Disclosure-State oracle leakage;
10. residual-risk loss on detailed-state expiry;
11. transfer causing automatic activation;
12. old-backup control rollback;
13. DESTROY implying READ;
14. DESTROY implying COPY;
15. parent destruction propagating to independent child;
16. workflow authority becoming general plane authority;
17. accidental aggregation of partial authorities;
18. legitimate explicit multi-party authority;
19. emergency authority surviving termination;
20. observation feedback loops;
21. Direct Master Access creating unrelated use authority;
22. unresolved authority becoming permission;
23. contextual re-identification;
24. material cross-plane composition without evaluation;
25. legitimate multi-plane workflows without redundant per-step human approval.

## 43. Formalisation boundary
This model does not prescribe programming language, database technology, cryptographic algorithm, network architecture, UI, exact disclosure-risk mathematics, exact identity-linkage technology, substantive civil authority rules, domain policy or anomaly algorithm unless later evidence demonstrates an architectural dependency.

## 44. Status
Architectural Discovery: CLOSED.
Broad CRADP Architectural Testing: COMPLETE.
Formalisation: ACTIVE.
PMEDG Extraction Testing: NEXT.
Portable Module Graduation: NOT YET.

Further changes to the architectural core should require evidence of contradiction, failed formalisation/extraction, implementation impossibility, new empirical evidence, failed targeted validation or external-interface incompatibility. Conceptual expansion alone is insufficient.
