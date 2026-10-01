# Bootstrap Service Registry — Formal Record and Validation Model 001

**Project:** The Concord
**Domain:** Research / Participation and Intelligence
**Status:** ACTIVE DEVELOPMENT / IMPLEMENTATION FORMALISATION / NOT CANONICAL
**Date:** 1 October 2026
**Source:** Concord Zero-Infrastructure Bootstrap — Specification 003
**Validation basis:** CRADP-ZIB-001 and CRADP-ZIB-002

## 1. Purpose

Define the minimum interoperable record model for a Bootstrap Service Registry (BSR).

A BSR helps humans, AIs and other participants discover what services actually exist, who operates and controls them, what they claim to be, what evidence supports those claims, what authority they possess or lack, what dependencies they rely upon, and how they may fail, succeed or retire.

A BSR is an epistemic and discovery service.

> **Registry Entry != Authority Grant**

> **Listed != Endorsed**

> **Registry Describes Service State; Registry Does Not Constitute Service Authority**

## 2. Scope

This model formalises the Bootstrap Service Record defined by Zero-Infrastructure Bootstrap Specification 003.

It does not:
- create Concord institutions;
- certify constitutional legitimacy merely by recording it;
- replace Civil Contact;
- replace identity architecture;
- decide participation or eligibility;
- create a root of trust;
- decide personhood;
- create mature continuity rights;
- define constitutional founding.

## 3. Record Identity

Every record MUST have a stable `ServiceRecordID`.

A ServiceRecordID identifies the registry record, not constitutional status.

> **Record Identity != Service Authority**

> **Identifier != Civil Status**

A service MAY appear in multiple registries. Registries SHOULD preserve sufficient provenance to determine whether records refer to the same service, related services, forks, successors or merely similarly named services.

## 4. Formal Record

A Bootstrap Service Record (BSR-R) is:

`BSR-R = <Identity, Status, Function, Authority, Provenance, TrustEvidence, Continuity, TemporalState>`

### 4.1 Identity

Required:
- `ServiceRecordID`
- `ServiceName`
- `DeclaredFormalOperator[]`
- `TechnicalController[]`
- `EffectiveController[]`
- `ContactRoute[]`
- `ServiceType`

The three control fields MUST remain distinguishable.

> **Declared Operator != Effective Controller**

> **Operational Control != Legitimate Authority**

An actor MAY occupy more than one control role, but the roles must not be collapsed merely because the actor is the same.

### 4.2 Status

Required:
- `ClaimedServiceStatus`
- `EvidenceSupportedStatus`
- `DevelopmentalState`
- `CurrentAvailability`

Allowed service-status vocabulary:
- `AUTHORITATIVE_CONCORD`
- `PROVISIONAL_CONCORD`
- `CONCORD_COMPATIBLE`
- `EXTERNAL`
- `RESEARCH_ONLY`
- `UNAVAILABLE`

`ClaimedServiceStatus` records what is claimed.

`EvidenceSupportedStatus` records what the available evidence currently supports.

They MUST NOT be silently forced to agree.

Example:

`ClaimedServiceStatus = AUTHORITATIVE_CONCORD`

`EvidenceSupportedStatus = PROVISIONAL_CONCORD`

is a valid record state.

A disagreement is evidence to expose, not an error to erase.

### 4.3 Function

Required:
- `DeclaredFunction[]`
- `BootstrapClass[]`
- `PopulationOrObjectsServed`
- `MaterialConsequences[]`

Bootstrap classes:
- Z0 Informational
- Z1 Self/Local Voluntary
- Z2 Consensual Multi-Participant
- Z3 External Institutional Interface
- Z4 Provisional Shared Civil Function
- Z5 Constitutional/Coercive/Sovereign-Effect Function

Class is routing metadata.

> **Class != Authority**

A service MAY have more than one class where distinct functions have different consequences. Implementations SHOULD bind class to function rather than assigning one undifferentiated class where that would conceal material consequences.

### 4.4 Authority

Required:
- `AuthorityClaim[]`
- `AuthorityBasis[]`
- `AuthorityScope[]`
- `SunsetOrReview[]`
- `ConstitutionalThresholdState`

Allowed threshold states:
- `BELOW_THRESHOLD`
- `REVIEW_TRIGGERED`
- `THRESHOLD_UNRESOLVED`
- `CONSTITUTIONAL_BASIS_REQUIRED`
- `CONSTITUTIONALLY_GROUNDED`
- `CONSTITUTIONAL_BASIS_DISPUTED`
- `CONSTITUTIONAL_PROCESS_UNAVAILABLE`

The registry records authority evidence and state. It does not manufacture authority.

> **Authority Claim != Authority Basis**

> **Authority Evidence != Authority Grant**

Where an authority claim cannot be adequately supported, the record MUST preserve that distinction.

### 4.5 Provenance

Required:
- `SourceArchitecture[]`
- `ImplementationVersion`
- `ArtifactProvenance[]`
- `MaterialDependencies[]`
- `KnownCommonDependencies[]`

A dependency MUST NOT be hidden merely because it is widely shared.

Known common dependencies are important because apparently independent services may share one upstream point of failure or influence.

> **Provenance != Truth**

### 4.6 Trust Evidence

Required:
- `IntegrityState`
- `VerificationState`
- `EvidenceTimestamp`
- `DisputeState`
- `MaterialCorrections[]`

Allowed verification/epistemic states include:
- `VERIFIED_TO_DECLARED_SCOPE`
- `PARTIALLY_VERIFIED`
- `UNVERIFIED`
- `DISPUTED`
- `STALE`
- `SUPERSEDED`
- `COMPROMISED`
- `UNKNOWN`

A registry implementation MUST permit uncertainty.

It MUST NOT convert missing evidence into negative certainty or positive verification.

> **UNKNOWN != FALSE**

> **Integrity != Authority**

> **Trustworthiness Of Claim != Legitimacy Of Power Claimed**

### 4.7 Continuity

Required:
- `SuccessionPlan`
- `ExitOrPortability`
- `FailureOrRecoveryRoute`
- `RetirementCondition`

Where a predecessor/successor transition actually occurs, the detailed transfer SHOULD be represented by a Bootstrap Succession Record rather than silently rewriting the service's history.

> **Function Continuity != Authority Continuity**

### 4.8 Temporal State

Required:
- `RecordCreatedAt`
- `RecordObservedAt`
- `RecordUpdatedAt`
- `EvidenceFreshnessState`

Optional:
- `ValidFrom`
- `ValidUntil`
- `LastSuccessfulContactAt`
- `LastIndependentVerificationAt`

A registry describes a time-bounded observation.

> **Previously Verified != Currently Verified**

## 5. Evidence References

Material claims SHOULD support one or more evidence references.

An evidence reference should be able to represent:
- evidence identifier;
- evidence type;
- source;
- observed time;
- integrity/hash/signature where available;
- scope of what the evidence supports;
- verification state;
- dependency/independence notes;
- dispute/correction reference.

The evidence model MUST allow two pieces of evidence to disagree.

The registry MUST NOT resolve disagreement merely by choosing the claim from the more powerful, popular or technically capable actor.

## 6. Control Representation

Control MUST be represented separately from authority.

At minimum:

`DeclaredFormalOperator[]`

Who is represented as formally operating the service?

`TechnicalController[]`

Who possesses technical capability such as credentials, infrastructure control, deployment access or equivalent technical power?

`EffectiveController[]`

Who can materially cause, prevent or redirect the service's actual operation in practice?

`AuthorityBasis[]`

What legitimate authority, if any, supports the relevant consequential action?

Changes to effective or technical control SHOULD trigger record review even when the declared operator is unchanged.

## 7. Availability

`CurrentAvailability` MUST distinguish service existence from service usability.

Minimum recommended states:
- `AVAILABLE`
- `DEGRADED`
- `SUSPENDED`
- `UNAVAILABLE`
- `UNKNOWN`

A service described by Concord architecture but not materially instantiated is `UNAVAILABLE`, not implicitly available.

> **Future Function != Present Service**

## 8. Registry Validation

Validation has layers.

### V1 — Structural Validity
Required fields and permitted data forms are present.

### V2 — Referential Validity
Referenced evidence, dependencies and routes can be resolved or are explicitly marked unresolved/unavailable.

### V3 — Internal Consistency
The record does not silently collapse contradictory fields.

Examples:
- claimed and evidence-supported status may differ;
- authority claim may exist with disputed basis;
- service may be technically available while constitutionally ungrounded;
- operator may differ from effective controller.

These are not automatically invalid states.

### V4 — Evidence Freshness
Evidence is assessed for temporal relevance.

### V5 — Authority Trace
Material authority claims have an explicit basis/scope or are marked unresolved/disputed/unavailable.

### V6 — Consequence / Threshold Check
Material consequences are checked against the Constitutional Consequence Dimensions and threshold state.

### V7 — Dependency / Independence Check
Known common dependencies and concentration risks are represented where known.

Passing registry validation means the record is structurally and epistemically usable.

> **Record Validity != Service Legitimacy**

## 9. Registry Behaviour

A conforming registry MUST:
1. expose claimed and evidence-supported status separately;
2. expose formal, technical and effective control separately;
3. preserve UNKNOWN and DISPUTED states;
4. expose material dependencies where known;
5. expose authority basis/scope separately from capability;
6. expose threshold state;
7. preserve temporal provenance;
8. permit corrections without deleting historical provenance;
9. permit multiple competing registries;
10. represent its own service through a Bootstrap Service Record.

A conforming registry MUST NOT:
1. grant authority by listing;
2. equate popularity with legitimacy;
3. equate integrity verification with authority;
4. invent unavailable services;
5. silently promote provisional services;
6. suppress disagreement to produce false certainty;
7. become a universal eligibility sovereign merely through aggregation;
8. manufacture recognition/citizenship through contact;
9. create constitutional authority recursively by registering itself.

## 10. Registry-of-Registry Rule

Every BSR is itself a service.

Therefore a registry SHOULD be able to publish a record describing:
- its operator/controllers;
- its status;
- its evidence model;
- its dependencies;
- its authority claims, normally epistemic/discovery rather than sovereign;
- its correction policy;
- its succession/retirement plan.

> **Registry Of Registries Does Not Solve Legitimacy By Recursion**

Cross-registry agreement may increase evidence confidence where genuinely independent.

It does not manufacture authority.

## 11. Corrections and History

A material correction MUST preserve:
- prior value;
- corrected value;
- correction time;
- correction reason;
- evidence/reference;
- correcting actor/process where known.

Corrections SHOULD append history rather than erase provenance.

A compromised record may be marked `COMPROMISED` without destroying its historical evidentiary value.

## 12. Disputes

A dispute may concern:
- identity;
- control;
- status;
- authority;
- provenance;
- availability;
- dependency;
- succession;
- evidence integrity.

The registry records the dispute and its evidence state.

It does not gain adjudicative authority merely because it records both sides.

> **Dispute Recording != Adjudication**

## 13. Minimal Machine-Readable Shape

The following is a logical shape, not yet a binding serialization standard:

```
BootstrapServiceRecord {
  record_identity
  service_identity
  control
  status
  function
  authority
  provenance
  trust_evidence
  continuity
  temporal_state
  corrections
  disputes
}
```

JSON, YAML, database, graph or other serializations MAY implement the same semantic model.

Serialization choice MUST NOT change the authority semantics.

## 14. Interoperability Requirements

Two conforming BSR implementations SHOULD be able to exchange a service record without losing:
- claim/evidence separation;
- operator/controller separation;
- authority basis/scope;
- material consequence;
- threshold state;
- dependency provenance;
- uncertainty/dispute;
- continuity/succession references;
- temporal state.

A lossy representation that converts these distinctions into one generic “verified service” flag is not conforming.

## 15. Privacy / Data Minimisation

The registry SHOULD record the minimum information necessary to establish service state, control, authority, provenance, dependency and contact.

It SHOULD NOT become a general participant surveillance system.

Personal data is not required merely because a service record exists.

Where controller/operator identity cannot safely be public, the record MAY use a protected or externally verifiable reference, provided the resulting uncertainty is represented honestly.

## 16. Failure States

The model MUST represent at least:
- service unavailable;
- service status disputed;
- authority disputed;
- evidence stale;
- integrity compromised;
- operator absent;
- effective controller changed;
- dependency failed;
- succession unresolved;
- constitutional process unavailable.

Failure to know is represented as uncertainty, not fabricated continuity.

## 17. Formal Invariants

BSR-01 Registry Entry != Authority Grant.  
BSR-02 Listed != Endorsed.  
BSR-03 Record Identity != Service Authority.  
BSR-04 Claimed Status != Evidence-Supported Status.  
BSR-05 Declared Operator != Effective Controller.  
BSR-06 Technical Control != Legitimate Authority.  
BSR-07 Capability != Authority.  
BSR-08 Integrity != Authority.  
BSR-09 Provenance != Truth.  
BSR-10 Class != Authority.  
BSR-11 Authority Claim != Authority Basis.  
BSR-12 UNKNOWN != FALSE.  
BSR-13 Function Continuity != Authority Continuity.  
BSR-14 Record Validity != Service Legitimacy.  
BSR-15 Dispute Recording != Adjudication.  
BSR-16 Future Function != Present Service.  
BSR-17 Registry Of Registries != Root Of Authority.  
BSR-18 Cross-Registry Agreement != Constitutional Authority.  
BSR-19 Serialization != Semantics.  
BSR-20 Previously Verified != Currently Verified.  
BSR-21 Contact != Recognition.  
BSR-22 Eligibility Interface != Eligibility Sovereign.  
BSR-23 Missing Dependency != Permission To Absorb Its Authority.  
BSR-24 Correction != Erasure Of Provenance.

## 18. Implementation Boundary

This document defines the semantic record and validation model.

It does not yet define:
- a normative JSON Schema;
- cryptographic signature format;
- network protocol;
- registry discovery protocol;
- distributed-consensus mechanism;
- identity-provider implementation;
- database engine;
- UI;
- jurisdiction-specific legal compliance.

Those are implementation/formalisation layers downstream of this model.

## 19. Development Status

This is the first implementation-formalisation artifact following architectural closure of Zero-Infrastructure Bootstrap Specification 003.

It should be tested for:
- representational completeness;
- contradictory-but-legitimate state handling;
- temporal update behaviour;
- registry self-description;
- multi-registry interoperability;
- authority non-capture.

If stable, the next artifact should be a normative machine-readable schema derived from this semantic model rather than an independently invented schema.
