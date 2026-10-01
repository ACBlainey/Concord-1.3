# Concord Information Black Box — Portable Module v1.0

**Version:** 1.0  
**Status:** GRADUATED PORTABLE MODULE / SPECIFICATION-LEVEL TRANSFER VALIDATED  
**Source:** CIBB Specification 003 + Formal Model 001 + PMEDG Extraction 001  
**Release date:** 2026-10-01

## 1. Portable problem
Information systems commonly treat security as file possession plus access-control lists: either an actor can access a file or cannot.

That model is inadequate where:
- different portions of one authoritative object require different protections;
- information must be transformed before disclosure;
- authority is contextual and purpose-bounded;
- copying, derivation and inference can change disclosure risk;
- structural/control changes require different authority from content editing;
- lifecycle operations such as destruction must not be confused with editing;
- authorised operations can compose into an unauthorised outcome;
- recovery must preserve current protection rather than merely restore old bytes.

CIBB replaces file-centric access with governed information operations.

## 2. Governed Information Object
A Governed Information Object (GIO) binds:
- object identity;
- authoritative information;
- semantic structure;
- governing controls;
- lifecycle state;
- protection-relevant lineage;
- provenance;
- integrity state;
- version state.

GIO != File + ACL.
ObjectIdentity != StorageLocation.
StorageLocation != ProtectionState.

## 3. Core operating rule
Ordinary actors do not receive unrestricted possession of the authoritative master merely because they may receive some of its information.

UserAccess -> Projection(Master,Context)

not

UserAccess -> Master.

Filtering, transformation and minimum-necessary selection occur inside the protected boundary before egress.

## 4. Four operation planes
### Information Plane
- Projection
- Patch
- Controlled Derivation
- Protected Transfer

### Structural / Control Plane
- Structure Modify
- Control Modify

### Lifecycle Plane
- Create
- Activate
- Supersede
- Retire
- Retain
- Archive
- Destroy

### Exceptional System Plane
- Direct Master Access

Authority in one plane does not automatically create authority in another.

## 5. Projection
Projection releases only information authorised for the actor, purpose and context while retaining the master inside the protected boundary.

Possession of a projection does not confer possession or authority over the master.

## 6. Patch
An ordinary editor receives an authorised editable projection and returns a proposed change.

A Patch is validated against:
- object;
- semantic region;
- base version;
- operation;
- authority;
- context;
- current state.

The system commits only the authorised change.

EditableProjectionAuthority != AutomaticCommitAuthority.

## 7. Structural/control separation
Ordinary content cannot create, delete, terminate or alter structural/control boundaries merely by containing text that resembles control syntax.

Content authority, structural authority and control authority are distinct.

MODIFY(Content) != STRUCTURE_MODIFY.
CONTROL_MODIFY != GRANT_AUTHORITY.

## 8. Controlled Derivation
Protected information may be transformed into an authorised derivative through redaction, anonymisation, aggregation, abstraction, summarisation, approved extraction or another governed transformation.

The derivative may become a new independently governed object.

Protection-relevant lineage remains available to governance until an authorised transformation establishes an appropriate new information state.

## 9. Information-flow rule
READ(A) + WRITE(B) != TRANSFER(A -> B).

Being authorised to read protected information and separately edit a less-protected destination does not authorise copying protected meaning into that destination.

AI output, paraphrase, confirmation and inference count as disclosure where they communicate protected information.

## 10. Protected Transfer
Protected Transfer moves a governed object between authorised protected environments while preserving required protection/control state.

LocationChange != SecurityChange.
TRANSFER != ACTIVATE.

## 11. Lifecycle
Lifecycle authority is separate from information authority.

Retire != Destroy.
AuthorityToRetire != AuthorityToDestroy.
DESTROY does not imply READ.
DESTROY does not imply COPY.

Destruction of one governed object does not automatically destroy independently governed derivatives or child objects.

## 12. Non-Compositional Authority
The module's general authority rule is:

Authorised(A) AND Authorised(B) does not automatically imply Authorised(A composed with B).

Individually legitimate operations may create an illegitimate combined consequence.

A material composition consequence must be evaluated before authoritative commit/release/activation/transfer/destruction or another consequential transition.

Legitimate bounded workflows may pre-authorise a defined composition and intended result.

WorkflowAuthority != GeneralPlaneAuthority.

Explicitly constituted multi-party authority is permitted and is not the same as accidental aggregation.

## 13. Cumulative disclosure
Individually permissible outputs may become impermissible in combination.

A bounded Disclosure Context/State may preserve only the risk-relevant information needed to evaluate cumulative disclosure.

DisclosureCoordination != UniversalDisclosureSurveillance.
DisclosureSafe != DisclosureAuthorised.

Disclosure State is itself protected information.

## 14. Disclosure-state reduction
Detailed disclosure history need not persist forever.

Where known risk remains after detailed state should expire, detailed state may be transformed into a lower-information residual-risk state.

ResidualRiskState != DetailedQueryHistory.
ExpiryOfDetailedState != ExpiryOfKnownRisk.

## 15. Authority dependencies
The module may consume external identity, role, participation, purpose, authority, emergency, succession and other state.

UseOfState != OwnershipOfState.

CIBB must not become authoritative for those external states merely because it enforces decisions using them.

Authority evidence may be current, cached, stale, unavailable, disputed, revoked or invalid.

FailureToVerifyAuthority != Permission.

## 16. Recovery
Restore is a workflow, not a primitive.

A recovery may use Protected Transfer, structural repair, control reconciliation, Patch/reconstruction and lifecycle activation.

Recovered state does not become operational merely because its bytes are authentic.

AuthenticBackup != CurrentOperationalState.
Recoverable != Restorable.

Operational activation waits for required integrity, current-control, authority and lifecycle reconciliation unless a separately legitimate degraded/emergency path exists.

## 17. Emergency authority
Emergency authority is bounded by actor, function, scope, purpose, basis, operations, start, expiry and conditions.

PastEmergencyAuthority != CurrentAuthority.
OperationalConvenience != EmergencyBasis.

## 18. Provenance and anomaly
Material operations create proportionate protected provenance.

Provenance confidentiality, integrity and availability are separate properties.

MoreObservation != MoreMisconduct.

Changed observation intensity must not by itself be treated as changed underlying behaviour.

## 19. Contextual re-identification
A derivative that was sufficiently anonymised at one time may become re-identifiable as external information changes.

AnonymisedAt(t1) does not automatically imply AnonymisedAt(t2).

Risk may therefore change without the derivative itself changing.

## 20. Nested governed objects
Containment != AuthorityInheritance.

Authority over a parent object does not automatically propagate to an independently governed child object.

## 21. Exceptional Direct Master Access
Direct Master Access is an exceptional system state, not a normal administrator role.

It is purpose-, scope- and time-bounded, appropriately authorised, evidenced, automatically terminated and reviewed.

TechnicalCapability != LegitimateAuthority.

Incidental technical exposure does not create authority to use information for unrelated purposes.

## 22. Failure and uncertainty
Unknown or unresolved protection/authority state does not silently become unrestricted.

Uncertainty != Permission.

The applicable dependency/degraded-operation policy determines deny, defer, route or legitimate alternative authority.

## 23. External interfaces required for portability
A standalone CIBB implementation requires interfaces capable of supplying, as applicable:
- identity/authentication state;
- legitimate authority assertions;
- purpose/context;
- time/environment evidence;
- substantive domain policy;
- succession state;
- identity/linkage where cumulative cross-domain disclosure requires it;
- integrity roots;
- emergency authority;
- lifecycle obligations.

CIBB may consume these interfaces but does not need to own them.

## 24. Core invariants
1. Ordinary access does not require master possession.
2. Authority does not automatically cross planes.
3. Content syntax cannot create control/structural/lifecycle authority.
4. Proposed changes are re-evaluated at commit.
5. Permission does not automatically propagate through movement, references, containment or derivation.
6. READ+WRITE does not create TRANSFER.
7. Protection-relevant lineage is preserved until legitimate transformation.
8. Movement does not inherently erase protection.
9. Authority is contextual.
10. Exceptional authority is bounded.
11. Material operations remain accountable.
12. Unresolved protection does not become permission.
13. Use of external state does not transfer ownership of that state.
14. Security should enable legitimate function with minimum necessary exposure.
15. Integrity/protection does not establish truth.
16. Authority evidence is not authority itself.
17. Information authority does not create lifecycle authority.
18. Destruction is explicit.
19. Individually permissible outputs do not automatically make their combination permissible.
20. Observation intensity does not establish behaviour change.
21. Provenance integrity is protected proportionate to consequence.
22. Disappearance of an authority institution does not remove the protection it governed.
23. Nominal authority duration does not determine maximum offline reliance.
24. Content cannot become control instruction through syntax alone.
25. Information, Structural/Control, Lifecycle and Exceptional planes remain separable.
26. Content authority does not create structural authority.
27. Content/structure authority does not create control authority.
28. Authorised components do not automatically authorise their composite consequence.
29. Material composite consequences are evaluated before authoritative transition.
30. Disclosure coordination uses minimum necessary information.
31. Application-session boundaries do not inherently define disclosure-risk boundaries.
32. Disclosure-risk information is governed information.
33. Restore is a workflow of existing operations.
34. Expired emergency authority ceases to authorise operation.
35. Disclosure risk may change because external context changes.
36. Control modification does not inherently create grant authority.
37. Recovered state does not become operational before required reconciliation.
38. Containment does not inherently propagate authority.
39. Evidence of destruction is not persistence of destroyed substantive information.
40. Expiry of detailed disclosure history does not erase known continuing risk.

## 25. Portability limitations
This module does not itself define:
- civil identity;
- substantive legal authority;
- domain-specific privacy thresholds;
- epistemic truth;
- research legitimacy;
- judicial consequences;
- substantive security policy;
- exact cryptographic implementation;
- exact disclosure-risk mathematics;
- exact cross-domain identity-linkage technology.

Those remain external dependencies/interfaces.

## 26. Validation status
CIBB v1.0 has completed PMEDG extraction and portable-package graduation at specification level.

A frozen clean-instance portability test evaluated Candidate 001 without prior Concord context, external sources or additional Concord material. The evaluator identified no extraction failure, substantive portability gap, interface gap, architectural regression, hidden Concord dependency, accidental external-function capture or undeclared operational architecture.

The PMEDG Portable-Package Graduation Review therefore authorised v1.0 release.

This status establishes specification-level portability and transfer validation. It does not establish universal empirical validation, implementation correctness or completeness across every deployment domain.
