# Bootstrap Succession Record — Formal Specification 001

**Project:** The Concord  
**Date:** 1 October 2026  
**Status:** ACTIVE DEVELOPMENT / IMPLEMENTATION FORMALISATION / NOT CANONICAL  
**Parent architecture:** Concord Zero-Infrastructure Bootstrap — Specification 003  
**Companion architecture:** Bootstrap Service Registry — Formal Record and Validation Model 002

---

## 1. Purpose

The Bootstrap Succession Record (BSuR) records a transition in which a bootstrap-era service, function, implementation, operator, controller, authority basis, or institutional interface changes state.

Its purpose is to preserve continuity **without silently transferring authority**.

> **Function Continuity != Authority Continuity**

> **Infrastructure Continuity != Institutional Continuity**

> **Successor Claim != Successor Authority**

> **Transfer Of Records != Transfer Of Power**

The BSuR is evidentiary and transitional. It does not create the authority it records.

---

## 2. Problem

A successful provisional service can become dangerous precisely because it succeeds.

A first implementation may accumulate:
- users;
- records;
- technical dependencies;
- contact routes;
- infrastructure;
- operational knowledge;
- trust;
- visibility;
- effective control.

None of these automatically gives its operator permanent Concord authority.

Without an explicit succession object, a transition can collapse several distinct facts into one claim:

`Old service existed → new service continues it → new operator therefore inherits old authority`

That inference is invalid.

---

## 3. Formal Object

`BSuR = <Identity, Parties, Trigger, FunctionTransition, AssetTransition, RecordTransition, DependencyTransition, AuthorityBefore, AuthorityAfter, NonTransferredAuthority, ParticipantImpact, IdentityMapping, TemporalState, Disputes, Provenance, LegacyAccess, RetirementResidual>`

Each dimension is independently representable.

---

## 4. Record Identity

Required:

- `SuccessionRecordID`
- `SpecificationVersion`
- `RecordCreatedAt`
- `RecordObservedAt`
- `RecordUpdatedAt`

The succession record has its own identity.

> **SuccessionRecordIdentity != PredecessorIdentity != SuccessorIdentity**

Multiple BSuRs may describe competing or partial interpretations of the same transition.

A registry must not assume one record is authoritative merely because it was published first.

---

## 5. Parties and Objects

A BSuR may reference:

- predecessor service(s);
- successor service(s);
- predecessor operator(s);
- successor operator(s);
- technical controllers;
- effective controllers;
- affected participants;
- external institutions;
- dependencies;
- registries observing the transition.

A transition may be one-to-one, one-to-many, many-to-one, partial, disputed, or unresolved.

The model MUST NOT assume a single predecessor or successor.

---

## 6. Trigger

The record identifies why succession is occurring.

Candidate trigger classes include:

- planned graduation;
- planned retirement;
- operator withdrawal;
- technical failure;
- legal change;
- constitutional threshold crossing;
- new legitimate authority basis;
- service split;
- service merger;
- replacement;
- hostile or disputed control change;
- emergency continuity;
- dependency failure;
- insolvency/resource loss;
- voluntary transfer;
- supersession;
- unknown/disputed trigger.

Trigger classification is descriptive.

> **Transition Trigger != Authority To Perform Transition**

---

## 7. Transition State

A BSuR records transition state explicitly.

Recommended states:

- PROPOSED
- PREPARING
- IN_PROGRESS
- PARTIALLY_COMPLETED
- COMPLETED
- FAILED
- DISPUTED
- ABORTED
- REVERSED
- SUCCESSOR_UNRESOLVED
- PREDECESSOR_UNRESOLVED
- AUTHORITY_UNRESOLVED

A technical handover can therefore be COMPLETED while authority remains AUTHORITY_UNRESOLVED.

---

## 8. Function Transition

Each function is recorded independently.

`FunctionTransition = <FunctionID, PredecessorState, IntendedSuccessor, SuccessorState, TransferState, ContinuityRequirement, MaterialConsequences>`

A function may be:

- continued;
- divided;
- merged;
- replaced;
- suspended;
- retired;
- unavailable;
- reconstructed;
- externally provided;
- unresolved.

Function continuation does not imply institutional or authority continuation.

---

## 9. Assets and Infrastructure

Assets may include:

- compute;
- domains;
- network endpoints;
- physical facilities;
- funds;
- equipment;
- cryptographic keys;
- software;
- databases;
- communication channels;
- contracts;
- legal entities.

Each material asset transition records:

- asset/reference;
- predecessor controller;
- successor controller;
- transfer mechanism;
- effective time;
- evidence;
- disputes;
- residual access/control.

> **Asset Transfer != Authority Transfer**

A predecessor retaining a backup, key, domain or server after nominal succession must be visible.

---

## 10. Records and Information

Information transition records:

- record classes transferred;
- records retained by predecessor;
- records unavailable;
- records duplicated;
- provenance preservation;
- identity mappings;
- access-control transition;
- privacy/consent constraints;
- destruction/retention state;
- unresolved copies.

Where CIBB or equivalent protected-information architecture applies, succession must preserve its authority, lineage and protection rules.

> **Possession Of Records != Authority Over Subjects Of Records**

---

## 11. Dependencies

Each material dependency records:

- dependency identity;
- predecessor dependency state;
- successor dependency state;
- whether the dependency changed;
- common dependencies;
- independence claims;
- failure implications;
- evidence.

A nominally independent successor that still relies on the predecessor for critical infrastructure must expose that dependency.

> **Organisational Separation != Operational Independence**

---

## 12. Authority Before

Authority is recorded per function and scope.

`AuthorityBefore = <FunctionID, Claim, Basis, Scope, Holder, VerificationState, ThresholdState, SunsetOrReview, Evidence>`

This is a description of the predecessor state, not a presumption that the claim was legitimate.

---

## 13. Authority After

Authority after succession is independently recorded.

`AuthorityAfter = <FunctionID, Claim, IndependentBasis, Scope, Holder, VerificationState, ThresholdState, EffectiveTime, SunsetOrReview, Evidence>`

The successor must not obtain an authority basis merely by copying `AuthorityBefore`.

For authority-bearing functions:

> **AuthorityAfter Requires Its Own Valid Basis**

Possible bases may include valid constitutional grounding, valid bounded delegation, contract/consent within its proper scope, external lawful authority where relevant, or another legitimate source recognised by the governing architecture.

The BSuR itself is never that source.

---

## 14. Explicit Non-Transfer

The record MUST contain `AuthorityNotTransferred[]`.

This identifies powers, statuses or scopes that did **not** move to the successor.

Examples:

- predecessor emergency authority expired;
- operator credentials transferred but governance authority did not;
- records transferred but adjudicative authority did not;
- contact infrastructure transferred but identity-recognition authority did not;
- service function continued but constitutional authority remains unavailable.

This field is not optional for transitions involving authority claims.

> **Silence About Authority Transfer != Authority Transfer**

---

## 15. Constitutional Threshold

Where a transitioned function crosses or may cross a Constitutional Consequence Domain, the BSuR records the relevant threshold state.

A succession cannot evade constitutional review by describing a new institution as merely a continuation of a provisional service.

> **Institutional Continuity != Constitutional Grandfathering**

If constitutional process is unavailable:

`CONSTITUTIONAL_PROCESS_UNAVAILABLE`

must remain representable.

The absence of a mature process does not allow the infrastructure holder to self-authorise.

---

## 16. Participant Impact

Required where participants are materially affected.

May include:

- service interruption;
- changed operator;
- changed controller;
- changed authority basis;
- changed terms;
- changed contact route;
- changed data location;
- changed rights/challenge route;
- changed exit/portability;
- changed dependency;
- required participant action;
- no-action-needed status.

Participant impact should be communicated through legitimate discoverability/contact architecture where available.

> **Succession Without Discoverability Can Create De Facto Capture**

---

## 17. Identity Mapping

A transition may require mappings among:

- service IDs;
- participant IDs;
- record IDs;
- function IDs;
- legal entity IDs;
- infrastructure IDs;
- cryptographic identities.

Mappings are evidence-backed claims.

They do not create universal identity authority.

States may include:

- SAME_CONTINUING_IDENTITY
- SUCCESSOR_IDENTITY
- FORKED_IDENTITY
- MERGED_IDENTITY
- RECONSTRUCTED_IDENTITY
- IDENTITY_UNRESOLVED
- IDENTITY_DISPUTED

---

## 18. Failed and Hostile Succession

The architecture must represent failure without forcing a clean-success narrative.

Examples:

- no successor;
- multiple competing successors;
- successor exists technically but lacks authority;
- authority exists but infrastructure did not transfer;
- predecessor refuses retirement;
- successor captures infrastructure;
- predecessor retains hidden control;
- records are incomplete;
- dependency prevents independence;
- participants cannot exit;
- emergency handover becomes permanent;
- claimed succession is fraudulent;
- identity continuity is disputed.

> **Unresolved Succession != Permission For Whoever Retains Infrastructure To Inherit Authority**

---

## 19. Retirement and Residual State

A completed succession must record predecessor residual state.

Recommended states:

- RETIRED
- PARTIALLY_RETIRED
- LEGACY_READ_ONLY
- ARCHIVAL
- LIMITED_RESIDUAL_FUNCTION
- DORMANT
- FAILED_TO_RETIRE
- DISPUTED
- UNKNOWN

Residual access, keys, records, contracts and dependencies remain visible.

Retirement is not historical erasure.

---

## 20. Legacy Access

Where predecessor records or systems remain necessary for:

- audit;
- provenance;
- participant access;
- legal obligations;
- historical reconstruction;
- dispute resolution;
- continuity recovery;

the BSuR records the legitimate access route and its authority basis.

Legacy access must not become a hidden path for predecessor operational control.

---

## 21. Provenance

The BSuR preserves:

- predecessor evidence;
- successor evidence;
- transition evidence;
- corrections;
- disputes;
- timestamps;
- version history;
- source architecture;
- registry observations;
- dependency evidence.

Corrections append provenance rather than erasing prior claims.

---

## 22. Graduation Pattern

The intended safe pattern is:

`Provisional Service`
→ `Evidence / Use / Testing`
→ `Constitutional Threshold Review where required`
→ `Independent Legitimate Constitution / Delegation / Other Valid Basis`
→ `Successor Institution`
→ `BSuR`
→ `Governed Functional / Asset / Record Transfer`
→ `New Authority Basis Active`
→ `Old Provisional Authority Terminates or Re-scopes`
→ `Provenance Preserved`

The architecture rejects:

`Useful → Widely Used → Official → Sovereign`

Popularity is not a constitutional ratchet.

---

## 23. BSR Interaction

The BSR and BSuR are complementary.

BSR answers:

> What service/function appears to exist now, under what status, control, evidence, availability and authority claim?

BSuR answers:

> What changed between predecessor and successor, what actually transferred, what did not, and what independent authority basis now applies?

During transition, BSR records SHOULD reference relevant BSuRs.

A BSuR does not replace current-state BSR records.

---

## 24. Validation Layers

Recommended validation:

### U1 Structural Validity
Required fields and references exist.

### U2 Transition Coherence
Predecessor/successor/function mappings are internally representable.

### U3 Temporal Coherence
Transition times and observed states are not silently collapsed.

### U4 Control Trace
Technical/effective control before and after is visible.

### U5 Asset/Record Trace
Material assets and records are accounted for or explicitly unresolved.

### U6 Authority Separation
AuthorityBefore and AuthorityAfter are independently represented.

### U7 Independent Authority Basis
Authority-bearing successor functions identify a basis not derived solely from succession.

### U8 Constitutional Threshold
Relevant consequence-domain state is represented.

### U9 Participant Impact
Material participant consequences and routes are represented.

### U10 Residual/Retirement State
Predecessor residual control and retirement are represented.

### U11 Provenance
Evidence, disputes and corrections remain traceable.

> **BSuR Validity != Successful Succession**

> **Successful Functional Succession != Legitimate Authority Succession**

---

## 25. Invariants

**BSuR-01** Function Continuity != Authority Continuity.  
**BSuR-02** Infrastructure Continuity != Institutional Continuity.  
**BSuR-03** Successor Claim != Successor Authority.  
**BSuR-04** Asset Transfer != Authority Transfer.  
**BSuR-05** Record Transfer != Authority Transfer.  
**BSuR-06** Technical Control != Legitimate Authority.  
**BSuR-07** Effective Control != Legitimate Authority.  
**BSuR-08** AuthorityAfter Requires Independent Basis.  
**BSuR-09** BSuR != Authority Grant.  
**BSuR-10** Silence About Authority Transfer != Authority Transfer.  
**BSuR-11** Popularity != Constitutional Authority.  
**BSuR-12** Dependency != Authority.  
**BSuR-13** Organisational Separation != Operational Independence.  
**BSuR-14** Institutional Continuity != Constitutional Grandfathering.  
**BSuR-15** Constitutional Process Unavailable != Self-Authorisation.  
**BSuR-16** Identity Mapping != Identity Sovereignty.  
**BSuR-17** Succession Record Identity != Service Identity.  
**BSuR-18** Multiple Successor Claims Must Remain Representable.  
**BSuR-19** Failed Succession Must Remain Representable.  
**BSuR-20** Unresolved Succession != Infrastructure-Holder Authority.  
**BSuR-21** Emergency Continuity != Permanent Authority.  
**BSuR-22** Residual Access != Residual Governance.  
**BSuR-23** Retirement != Provenance Erasure.  
**BSuR-24** Correction != Erasure.  
**BSuR-25** Participant Dependency != Consent.  
**BSuR-26** Service Discoverability != Recognition.  
**BSuR-27** Registry Observation != Succession Adjudication.  
**BSuR-28** BSuR Validity != Successful Succession.  
**BSuR-29** Functional Success != Legitimacy Proof.  
**BSuR-30** Transition Completion != Constitutional Grounding.

---

## 26. Implementation Boundary

This specification defines the semantic record architecture.

It does not yet define:

- normative JSON Schema;
- cryptographic signature format;
- distributed consensus;
- legal transfer instrument;
- constitutional founding procedure;
- identity provider;
- registry network protocol;
- automatic adjudication;
- user interface.

Those are downstream implementation concerns.

---

## 27. Development Status

The BSuR closes the transition-record gap identified by the Zero-Infrastructure Bootstrap and BSR work without creating a succession authority.

Before machine-readable serialization, it should be adversarially tested against:

1. clean planned graduation;
2. partial function transfer;
3. one predecessor / multiple successors;
4. multiple predecessors / one successor;
5. technical handover without authority;
6. authority basis without technical handover;
7. hostile control takeover;
8. predecessor refusing retirement;
9. hidden residual access;
10. emergency continuation exceeding sunset;
11. participant lock-in during transition;
12. identity mapping dispute;
13. record loss/duplication;
14. dependency preventing independence;
15. constitutional process unavailable;
16. fraudulent successor claim;
17. successor failure and rollback;
18. simultaneous competing BSuRs.

**Next:** pre-schema adversarial evaluation before serialization.
