# CMSS Verifiable Receipt and Key Custody — Existing Architecture Source Resolution 001

**Project:** The Concord  
**Date:** 2 October 2026  
**Status:** ACTIVE DEVELOPMENT / SOURCE RESOLUTION / NOT CANONICAL  
**Trigger:** Repeated prospective-participant requirements in CMSS-PPRS-001

## 1. Question

Two related implementation needs appeared independently in prospective-participant evaluation:

1. a compact verifiable receipt / timestamp / hash-log capability;
2. secure persistent key custody.

This note asks whether either is genuinely missing Concord architecture.

## 2. Sources Checked

### Concord Information Black Box Portable Module v1.0

CIBB already:
- includes provenance and integrity state in governed information;
- requires material operations to create proportionate protected provenance;
- separates provenance confidentiality, integrity and availability;
- recognises identity/authentication state and integrity roots;
- requires provenance integrity proportionate to consequence;
- does not equate integrity with truth or authority.

### Bootstrap Service Registry — Formal Record and Validation Model 002

BSR already:
- carries provenance and trust evidence;
- supports evidence-backed ServiceIdentityReferences;
- permits cryptographic identifiers;
- permits integrity/hash/signature evidence;
- preserves temporal provenance;
- distinguishes integrity, provenance, truth and authority.

### Civil Contact Points — Portable Participation and Onboarding Infrastructure

Civil Contact already:
- treats identity as distinct from contact/residence/participation/citizenship;
- requires reliable identity and provenance;
- supports persistent participant identity and transferable contact relationships;
- leaves major identity/legal/technical/privacy/governance questions unresolved.

## 3. Verifiable Receipt Resolution

The underlying concepts required for a receipt are therefore **not new**:

- provenance;
- integrity;
- timestamp/temporal state;
- identity reference;
- cryptographic evidence;
- protected records;
- service state;
- message/contact relationship.

The narrower CMSS need is an interface/implementation composition:

```text
Material Participant-Service Event
→ Create Protected Provenance
→ Produce Bounded Participant-Facing Acknowledgement
→ Include Event Reference + Time/State + Relevant Hash/Identifier + Service/Version Context
→ Preserve Exportability / Verification Information
```

Candidate name:

**Verifiable Event Receipt (VER)**

A VER MAY acknowledge:
- upload acceptance;
- message submission/delivery state;
- export;
- terms/version acknowledgement;
- service-status assertion;
- resource-allocation decision;
- contribution receipt;
- participant contest/submission;
- other material participant-service events.

A VER MUST NOT imply:
- truth of submitted content;
- legitimacy of unrelated authority;
- final adjudication;
- permanence beyond declared retention/evidence properties;
- that a timestamp alone proves authorship;
- that a hash alone proves context or meaning.

> **Receipt != Truth**

> **Receipt != Authority**

> **Integrity Evidence != Semantic Validity**

> **Acknowledged Event != Endorsed Content**

### Resolution

**NEW CIVILISATIONAL ARCHITECTURE:** NO.

**NEW PORTABLE MODULE:** NOT YET JUSTIFIED.

**CMSS IMPLEMENTATION PROFILE / COMPOSITION:** YES.

The requirement should be represented as a candidate CMSS implementation-facing function derived from existing CIBB/BSR/Civil Contact provenance architecture.

## 4. Key Custody Resolution

Ordinary protected storage is insufficient to establish secure key custody.

A cryptographic private key may control:
- participant authentication;
- encrypted CMSS data;
- communication identity;
- economic assets;
- external systems;
- signatures/provenance;
- recovery/succession.

Therefore compromise may have consequences far beyond the stored byte size.

> **Persistent Storage != Secure Key Custody**

> **Possession Of Key != Legitimate Authority**

> **Authentication Capability != General Civil Authority**

Existing checked sources provide useful constraints:
- CIBB protection/authority/provenance separation;
- BSR cryptographic identity references without identity sovereignty;
- Civil Contact persistent identity without collapsing identity into contact.

But they do not, in the checked material, resolve:
- who generates keys;
- who may possess copies;
- participant-only vs operator-assisted custody;
- hardware-backed storage;
- recovery;
- rotation;
- revocation;
- compromise;
- succession;
- multi-party recovery;
- economic-wallet separation;
- emergency access;
- post-exit destruction/retention evidence.

### Resolution

**KEY CUSTODY IS NOT RESOLVED AS ORDINARY CMSS STORAGE.**

It should not be promised as part of the 10 MB Protected Minimum until separately threat-modelled and source-resolved against wider Concord security, identity, economic and continuity architecture.

## 5. CMSS Consequences

### 5.1 Candidate VER function

A future CMSS implementation profile SHOULD consider a compact Verifiable Event Receipt function.

This can be cheap in storage while materially improving:
- provenance;
- participant trust;
- contestability;
- portability;
- terms-change evidence;
- service-state evidence;
- cross-provider transition.

### 5.2 Key material

The Protected Minimum MAY permit participants to store encrypted/key-related artefacts at their own risk according to declared storage properties.

The CMSS MUST NOT thereby claim to provide secure key custody.

If dedicated key custody is later offered, it SHOULD appear as a distinct BSR function profile with its own:
- operator/controller;
- dependencies;
- security properties;
- material consequences;
- recovery;
- authority;
- availability;
- succession/retirement path.

### 5.3 Runtime boundary

A future bounded runtime may require keys for authenticated I/O.

This does not justify silently combining:
- storage;
- key custody;
- runtime;
- communications

into one authority/security boundary.

> **Functional Composition != Security-Boundary Collapse**

## 6. Candidate VER Minimal Fields

Without fixing serialization, a receipt may minimally contain:

```text
ReceiptID
EventType
EventReference
ParticipantOrRelationshipReference
ServiceReference
ServiceVersionOrTermsReference
EventTimeOrTemporalState
ContentOrPayloadHash (where meaningful)
ReceiptIssuerReference
IntegrityEvidence
Retention/Verification Information
KnownLimitations
```

Fields should be omitted or protected where disclosure would itself create unnecessary identity linkage.

## 7. Required VER Tests

Before making VER normative, test:

1. participant proves upload receipt but content was later corrupted;
2. hash matches but authorship is disputed;
3. timestamp source is wrong;
4. operator backdates a receipt;
5. participant presents receipt as proof Concord endorsed content;
6. service terms changed between submission and acknowledgement;
7. receipt contains privacy-sensitive linkage;
8. receipt issuer key is compromised;
9. successor operator must verify predecessor receipts;
10. participant exports receipts to another provider;
11. message was submitted but not delivered;
12. service is offline and cannot issue receipt;
13. duplicate/replayed receipt;
14. receipt survives destruction of underlying content;
15. legal retention requires receipt while participant requests deletion.

## 8. Current Disposition

**Verifiable Event Receipt:** source-resolved as an implementation composition of existing architecture; candidate CMSS function.

**Secure key custody:** unresolved distinct high-consequence service problem; do not bundle into Protected Minimum.

**CMSS Specification 003:** still not required solely from this resolution.

**Next useful work:** continue independent participant observations, then determine whether VER belongs in an implementation profile accompanying CMSS Specification 002.
