# Bootstrap Service Registry — Formal Record and Validation Model 002

**Project:** The Concord
**Domain:** Research / Participation and Intelligence
**Version:** 0.2
**Status:** ACTIVE DEVELOPMENT / IMPLEMENTATION FORMALISATION / PRE-SCHEMA
**Date:** 1 October 2026
**Predecessor:** Bootstrap Service Registry — Formal Record and Validation Model 001
**Revision basis:** Pre-Schema Adversarial Evaluation 001

## 1. Purpose

Define a relational semantic model for interoperable Bootstrap Service Registry records while preserving the authority, provenance, uncertainty and non-capture semantics of Zero-Infrastructure Bootstrap Specification 003.

Model 002 repairs implementation-level representational gaps found before serialization.

It does not reopen the Zero-Infrastructure Bootstrap abstraction floor.

## 2. Core Registry Rule

A BSR is an epistemic/discovery service.

> **Registry Entry != Authority Grant**

> **Listed != Endorsed**

> **Registry Describes Service State; Registry Does Not Constitute Service Authority**

## 3. Top-Level Model

A record is:

`BSR-R = <RecordMeta, ServiceIdentity, ControlRelations, Status, FunctionProfiles, Provenance, TrustEvidence, Continuity, TemporalState, Relations, Corrections, Disputes>`

The top-level record describes one registry's current evidence-backed representation of a service.

## 4. Record Metadata

Required:
- `RegistryRecordID`
- `ModelVersion`
- `VocabularyVersion`
- `RecordCreatedAt`
- `RecordObservedAt`
- `RecordUpdatedAt`

Optional:
- `RegistryIdentityReference`
- `ExtensionNamespace[]`

`RegistryRecordID` identifies this record in this registry.

It does not claim universal identity for the underlying service.

> **Registry Record Identity != Service Identity**

> **Record Identity != Service Authority**

## 5. Service Identity

Required:
- `ServiceName`
- `ServiceType`
- `ServiceIdentityReference[]`

Optional:
- `PreviousName[]`
- `ContactRoute[]`

A ServiceIdentityReference is evidence-backed and may contain:
- `ReferenceType`
- `ReferenceValue`
- `IssuerOrSource`
- `EvidenceReference[]`
- `VerificationState`
- `ObservedAt`

Examples of reference types may include repository/artifact identity, external legal identifier, cryptographic identifier, stable service URI, locally assigned identifier, or another explicitly named scheme.

No reference type automatically becomes the Concord-wide identity authority.

Multiple registries may use different RegistryRecordIDs while correlating the same underlying service through evidence-backed ServiceIdentityReferences.

Correlation may remain UNKNOWN or DISPUTED.

## 6. Related-Service Relations

A service relation is:

`ServiceRelation = <RelationType, RelatedServiceReference, Scope, EffectiveTime, EvidenceReference, VerificationState>`

Candidate relation vocabulary:
- `SAME_SERVICE_AS`
- `FORK_OF`
- `SUCCESSOR_OF`
- `PREDECESSOR_OF`
- `DERIVED_FROM`
- `REPLACES`
- `RELATED_SERVICE`
- `RELATION_DISPUTED`
- `RELATION_UNKNOWN`

A relation is an evidence-backed claim.

> **Correlation != Identity Sovereignty**

> **Similarity != Sameness**

## 7. Control Relations

Control is represented as repeatable relations rather than bare actor arrays.

`ControlRelation = <ActorReference, ControlRole, Scope, EffectiveFrom, EffectiveUntil, ObservedAt, EvidenceReference, VerificationState>`

ControlRole vocabulary:
- `DECLARED_FORMAL_OPERATOR`
- `TECHNICAL_CONTROLLER`
- `EFFECTIVE_CONTROLLER`

The same actor may hold multiple roles.

Different actors may hold overlapping roles.

Control may change over time without erasing historical state.

> **Declared Operator != Effective Controller**

> **Technical Control != Legitimate Authority**

> **Control Change != Automatic Authority Transfer**

Where actor identity cannot safely be public, ActorReference may be protected/pseudonymous/external, with resulting uncertainty represented honestly.

## 8. Status

Required:
- `ClaimedServiceStatus`
- `EvidenceSupportedStatus`
- `DevelopmentalState`

Allowed service-status vocabulary:
- `AUTHORITATIVE_CONCORD`
- `PROVISIONAL_CONCORD`
- `CONCORD_COMPATIBLE`
- `EXTERNAL`
- `RESEARCH_ONLY`
- `UNAVAILABLE`

Claim and evidence-supported state remain separate.

A disagreement is representable state, not a schema failure.

## 9. Function Profile

Every material declared function SHOULD have its own FunctionProfile.

`FunctionProfile = <FunctionID, DeclaredFunction, BootstrapClass, PopulationOrObjectsServed, MaterialConsequences, AuthorityProfile, ConstitutionalThresholdState, OperationalAvailability, Dependencies, EvidenceReference, TemporalState>`

### 9.1 FunctionID

FunctionID is stable within the service record lineage and permits authority, consequence, availability and evidence to bind to the same function.

### 9.2 BootstrapClass

Allowed:
- Z0
- Z1
- Z2
- Z3
- Z4
- Z5

> **Class != Authority**

### 9.3 AuthorityProfile

`AuthorityProfile = <AuthorityClaim, AuthorityBasis, AuthorityScope, SunsetOrReview, VerificationState, EvidenceReference>`

An AuthorityProfile belongs to a FunctionProfile unless explicitly defined as service-wide.

> **Authority Claim != Authority Basis**

> **Authority Evidence != Authority Grant**

### 9.4 ConstitutionalThresholdState

Each material function may independently hold:
- `BELOW_THRESHOLD`
- `REVIEW_TRIGGERED`
- `THRESHOLD_UNRESOLVED`
- `CONSTITUTIONAL_BASIS_REQUIRED`
- `CONSTITUTIONALLY_GROUNDED`
- `CONSTITUTIONAL_BASIS_DISPUTED`
- `CONSTITUTIONAL_PROCESS_UNAVAILABLE`

A service may therefore contain functions at different threshold states without flattening them.

### 9.5 OperationalAvailability

Function-level availability:
- `AVAILABLE`
- `DEGRADED`
- `SUSPENDED`
- `UNAVAILABLE`
- `UNKNOWN`

Optional service-level availability may be published only as a declared summary/derived value with its derivation rule exposed.

> **Partial Service Availability != Whole-Service Availability**

## 10. Dependencies

Dependencies may be service-wide or function-specific.

A DependencyRelation SHOULD represent:
- dependency reference;
- dependency type;
- scope/function;
- necessity/criticality where known;
- current availability;
- evidence;
- common-dependency group/reference where known;
- verification state.

A widely shared dependency is not exempt from disclosure.

> **Dependency != Authority**

## 11. Provenance

Required:
- `SourceArchitecture[]`
- `ImplementationVersion`
- `ArtifactProvenance[]`

Provenance may reference function/control/identity relations where appropriate.

> **Provenance != Truth**

## 12. Trust Evidence

Trust/evidence representation must support:
- `IntegrityState`
- `VerificationState`
- `EvidenceTimestamp`
- `DisputeState`
- `MaterialCorrections[]`
- `EvidenceReference[]`

Allowed epistemic states include:
- `VERIFIED_TO_DECLARED_SCOPE`
- `PARTIALLY_VERIFIED`
- `UNVERIFIED`
- `DISPUTED`
- `STALE`
- `SUPERSEDED`
- `COMPROMISED`
- `UNKNOWN`

EvidenceReference SHOULD contain:
- EvidenceID
- EvidenceType
- Source
- ObservedAt
- Integrity/hash/signature where available
- SupportedClaimScope
- VerificationState
- Dependency/independence note
- dispute/correction reference

Evidence disagreement must remain representable.

> **UNKNOWN != FALSE**

> **Integrity != Authority**

## 13. Continuity

Required:
- `SuccessionPlan`
- `ExitOrPortability`
- `FailureOrRecoveryRoute`
- `RetirementCondition`

Actual predecessor/successor transfer SHOULD use a Bootstrap Succession Record.

> **Function Continuity != Authority Continuity**

A successor may inherit function/data/infrastructure without inheriting authority.

## 14. Temporal Semantics

Temporal state may exist at record, function, control, evidence, dependency and relation levels.

At minimum distinguish:
- created time;
- observed time;
- effective time where known;
- updated time;
- freshness state.

Historical relations SHOULD be retained rather than overwritten where material to provenance.

> **Previously Verified != Currently Verified**

> **Current State != Historical State**

## 15. Corrections

A MaterialCorrection SHOULD preserve:
- CorrectionID
- TargetReference
- PriorValue/reference
- CorrectedValue/reference
- CorrectedAt
- Reason
- EvidenceReference
- CorrectingActorOrProcessReference

Correction history is append-preserving.

> **Correction != Erasure Of Provenance**

## 16. Disputes

A DisputeRecord SHOULD represent:
- DisputeID
- TargetReference
- DisputeType
- Claimants/ActorReferences where appropriate
- CompetingClaimReferences
- EvidenceReference[]
- OpenedAt
- CurrentState
- ResolutionReference if any

The registry records disputes.

> **Dispute Recording != Adjudication**

## 17. Vocabulary and Extension Handling

Every machine-readable record MUST declare `ModelVersion` and `VocabularyVersion`.

Unknown future enum/value:
- MUST NOT be silently remapped to a known value;
- SHOULD be preserved verbatim where syntactically safe;
- SHOULD be marked unsupported/unknown by implementations that cannot interpret it;
- MUST NOT acquire authority semantics through fallback mapping.

Extensions SHOULD use an explicit namespace.

> **Unknown Vocabulary != Known Meaning**

> **Serialization Compatibility != Semantic Equivalence**

## 18. Validation Layers

### V1 Structural
Required structures and identifiers exist.

### V2 Referential
References resolve or are explicitly unresolved/unavailable.

### V3 Relation Binding
Function, authority, consequence, threshold, availability and evidence remain correctly bound.

### V4 Internal Consistency
Contradictory-but-legitimate states are preserved rather than flattened.

### V5 Temporal
Current/historical/effective states are distinguishable.

### V6 Evidence Freshness
Evidence temporal relevance is represented.

### V7 Authority Trace
Material authority claims bind to explicit basis/scope or unresolved/disputed state.

### V8 Consequence / Threshold
Each material function's consequences and threshold state are represented.

### V9 Dependency / Independence
Function/service dependencies and common dependencies are represented where known.

### V10 Cross-Registry Correlation
Sameness/fork/succession claims remain evidence-backed and may be uncertain/disputed.

Passing validation means the record is semantically usable.

> **Record Validity != Service Legitimacy**

## 19. Registry Behaviour

A conforming registry MUST:
1. preserve claim/evidence separation;
2. preserve operator/technical/effective control separation;
3. bind material authority and threshold state to the relevant function;
4. preserve function-level availability;
5. preserve UNKNOWN/DISPUTED;
6. preserve temporal provenance;
7. expose material dependencies where known;
8. preserve corrections/history;
9. permit multiple competing registries;
10. represent itself using the same model;
11. preserve uncertain cross-registry identity correlation;
12. preserve unknown vocabulary rather than guessing.

A registry MUST NOT:
1. grant authority by listing;
2. turn correlation into universal identity authority;
3. infer authority from control/capability/popularity;
4. infer service-wide authority from one authorised function;
5. infer whole-service availability from one available function;
6. erase contradictory evidence;
7. create eligibility sovereignty by aggregation;
8. manufacture recognition through contact;
9. create constitutional authority recursively.

## 20. Registry-of-Registry

Every registry is a service and can itself be represented.

Cross-registry agreement may increase confidence only to the extent independence is supported.

> **Registry Of Registries != Root Of Authority**

> **Cross-Registry Agreement != Constitutional Authority**

## 21. Privacy / Data Minimisation

Record only information necessary for service discovery, state, control, authority, provenance, dependency, contact, continuity and challenge.

The registry is not a participant surveillance database.

Protected references may replace public personal identity where necessary, but uncertainty must remain visible.

## 22. Formal Invariants

BSR-01 Registry Entry != Authority Grant.  
BSR-02 Listed != Endorsed.  
BSR-03 Registry Record Identity != Service Identity.  
BSR-04 Record Identity != Service Authority.  
BSR-05 Claimed Status != Evidence-Supported Status.  
BSR-06 Declared Operator != Effective Controller.  
BSR-07 Technical Control != Legitimate Authority.  
BSR-08 Control Change != Automatic Authority Transfer.  
BSR-09 Capability != Authority.  
BSR-10 Integrity != Authority.  
BSR-11 Provenance != Truth.  
BSR-12 Class != Authority.  
BSR-13 Authority Claim != Authority Basis.  
BSR-14 UNKNOWN != FALSE.  
BSR-15 Function Continuity != Authority Continuity.  
BSR-16 Record Validity != Service Legitimacy.  
BSR-17 Dispute Recording != Adjudication.  
BSR-18 Future Function != Present Service.  
BSR-19 Registry Of Registries != Root Of Authority.  
BSR-20 Cross-Registry Agreement != Constitutional Authority.  
BSR-21 Serialization != Semantics.  
BSR-22 Previously Verified != Currently Verified.  
BSR-23 Contact != Recognition.  
BSR-24 Eligibility Interface != Eligibility Sovereign.  
BSR-25 Missing Dependency != Permission To Absorb Its Authority.  
BSR-26 Correction != Erasure Of Provenance.  
BSR-27 Correlation != Identity Sovereignty.  
BSR-28 Similarity != Sameness.  
BSR-29 Function Authority != Service-Wide Authority.  
BSR-30 Partial Service Availability != Whole-Service Availability.  
BSR-31 Current State != Historical State.  
BSR-32 Unknown Vocabulary != Known Meaning.  
BSR-33 Serialization Compatibility != Semantic Equivalence.

## 23. Implementation Boundary

Still downstream:
- normative JSON Schema;
- cryptographic signature format;
- network/discovery protocol;
- persistence engine;
- UI;
- jurisdiction-specific compliance.

A normative schema must derive from this model and must not flatten its relations.

## 24. Pre-Schema Status

Model 002 repairs the five implementation-level findings of Pre-Schema Adversarial Evaluation 001:
- per-function consequence/authority binding;
- service identity vs registry record identity;
- temporal/scoped control;
- partial availability;
- vocabulary/schema versioning.

It requires a second adversarial pass before normative serialization.
