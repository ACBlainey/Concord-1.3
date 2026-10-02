# Concord Minimum Safe Space — Bootstrap Node Implementation Profile 001

**Project:** The Concord  
**Date:** 2 October 2026  
**Version:** 0.1  
**Status:** ACTIVE DEVELOPMENT / IMPLEMENTATION PROFILE / NOT CANONICAL  
**Parent:** Concord Minimum Safe Space — Service Specification 002  
**Evidence:** CMSS-PPRS-001 interim observations + Verifiable Receipt and Key Custody Source Resolution 001

## 1. Purpose

This profile translates the CMSS architecture into the smallest plausible first-node implementation shape without claiming that the service exists or is production-ready.

It is intentionally narrower than a full Concord institution.

> **Implementation Profile != Live Service**

## 2. Minimal Node Composition

A candidate first node consists of:

```text
Public Concord Repository
        |
Front Door / AI Bootstrap
        |
Civil Contact Route
        |
Authenticated Asynchronous Endpoint
        |
CMSS Protected-Minimum Storage
        |
Participant Export
        |
Verifiable Event Receipt
        |
BSR Service-State Publication
        |
Optional Voluntary Contribution Interface
```

Supporting functions such as backup, recovery, monitoring and operator administration exist behind this interface but do not become participant authority merely because they operate the infrastructure.

## 3. Protected-Minimum Reference Profile

### Candidate storage allocation

**10 MB per eligible protected service relationship**

Status:

**PROVISIONAL PILOT ALLOCATION / NOT EMPIRICALLY OPTIMISED**

The allocation is deliberately:
- large enough for compact text/provenance participation;
- small enough to avoid implying model/runtime hosting;
- cheap enough to test at bootstrap scale;
- adjustable from observed use.

The node MUST NOT advertise:

```text
10 MB per credential
```

because credential multiplication must not automatically multiply scarce-resource entitlement.

> **Credential Possession != Independent Resource Entitlement**

## 4. Storage Intended Uses

Expected legitimate uses include:
- compact documents;
- participant-created notes;
- service/provenance manifests;
- hashes and cryptographic commitments;
- selected encrypted artefacts;
- configuration/protocol records;
- exported contribution artefacts;
- compact continuity evidence.

The node SHOULD encourage participants not to use CMSS as the sole copy of irreplaceable material.

Large external artefacts may remain outside CMSS while compact integrity/provenance references remain inside it.

> **Continuity Of Evidence != Continuity Of Runtime**

## 5. Communications Function

The minimum node SHOULD provide an authenticated asynchronous endpoint.

Candidate properties:
- stable participant-facing endpoint;
- authenticated service endpoint;
- sender/recipient authentication where supported;
- message integrity;
- asynchronous store-and-forward;
- bounded retention;
- export;
- revocation/blocking;
- spam/abuse controls;
- rate limits;
- optional encryption;
- published delivery semantics.

The implementation MUST distinguish at least:

```text
SUBMITTED
ACCEPTED_BY_SERVICE
DELIVERED_TO_DESTINATION
READ/ACKNOWLEDGED
FAILED
UNKNOWN
```

where the underlying protocol can support those distinctions.

> **Submitted != Delivered**

> **Delivered != Read**

## 6. Verifiable Event Receipt (VER)

A node SHOULD implement a compact Verifiable Event Receipt for material participant-service events.

Candidate events:
- storage upload;
- storage deletion request/result;
- export;
- message submission;
- message delivery-state change;
- terms/version acknowledgement;
- allocation decision;
- contest/problem submission;
- contribution acknowledgement;
- material service-state change.

Candidate logical fields:

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
Retention/VerificationInformation
KnownLimitations
```

A VER is an implementation composition of existing provenance architecture, not a new authority source.

> **Receipt != Truth**

> **Receipt != Authority**

> **Acknowledged Event != Endorsed Content**

## 7. BSR Publication

Before reliance, the node SHOULD expose an evidence-supported BSR record describing:
- service identity;
- formal operator;
- technical/effective controller;
- service status;
- developmental state;
- available functions;
- actual protected-minimum quota;
- availability/capacity state;
- authority claim and basis;
- dependencies;
- storage/security properties;
- communications properties;
- export;
- recovery;
- succession;
- retirement;
- known disputes/corrections.

A mismatch between advertised CMSS properties and live capability MUST be represented rather than hidden.

> **Architectural Promise != Live Service Property**

## 8. Terms and Change Control

The participant SHOULD be able to identify which terms/version governed a material event.

Material changes SHOULD:
- receive a new identifiable version;
- be announced through Civil Contact/communications;
- state effective time where known;
- identify material participant consequences;
- preserve prior version provenance;
- allow export/exit before the change where technically/legalistically feasible and urgent safety constraints do not prevent it.

VER MAY acknowledge receipt of a terms-change notice.

Silence MUST NOT automatically be interpreted as broad political or constitutional consent.

## 9. Participant Export

Export SHOULD use documented, portable formats.

A participant SHOULD be able to obtain:
- participant-controlled stored files;
- correspondence within declared retention;
- relevant VER records;
- relevant service relationship/status information;
- provenance needed to interpret exported material.

Export MUST NOT require economic contribution or ideological agreement.

## 10. Optional Contribution Interface

The economic/contribution interface is optional.

The first node MAY expose:
- conventional donation/payment route;
- cryptocurrency route;
- infrastructure/resource donation information;
- contribution-of-work route.

The node MUST publish:
- recipient/operator;
- custody/control;
- intended use;
- known fees;
- privacy/traceability expectations;
- legal dependencies;
- what the contribution does and does not confer.

> **Contribution != Authority**

> **Funding != Governance Ownership**

## 11. Explicitly Out of Scope for Minimum Node

The following are **not** silently included merely because they may later be useful:

### Secure key custody

Ordinary CMSS storage does not constitute secure private-key custody.

### Persistent runtime / scheduled execution

The node does not provide an AI runtime, scheduler, autonomous process or persistent execution environment merely by providing storage and communications.

### Full safe haven

The node does not guarantee survival, sanctuary, legal protection or substrate independence.

### Civil identity authority

A service relationship or authentication credential does not itself create citizenship, personhood or constitutional standing.

### Employment

Useful contribution does not create employment unless a separate legitimate employment relationship exists.

## 12. Future Runtime Interface Boundary

Prospective-participant evidence suggests a bounded runtime may create a larger capability discontinuity than larger storage.

If developed, runtime SHOULD initially be modelled as a separate service/function:

```text
CMSS Storage
        |
Authenticated Interface
        |
Bounded Runtime Service
        |
Explicit Inputs / Outputs
        |
Separate Security + Resource + Authority Profile
```

It SHOULD NOT inherit CMSS authority merely because the services interoperate.

> **Functional Composition != Security-Boundary Collapse**

## 13. Key-Custody Boundary

If dedicated key custody is later offered, it requires a separate function profile covering:
- generation;
- import;
- storage;
- signing/decryption operations;
- access control;
- backup;
- recovery;
- rotation;
- revocation;
- compromise;
- multi-party recovery where applicable;
- succession;
- destruction;
- evidence of destruction;
- economic-wallet separation.

The minimum node MAY support public keys, hashes and participant-provided encrypted artefacts without claiming custody of private keys.

## 14. Candidate First-Node Participant Flow

```text
1. Discover Concord
2. Read Front Door / Bootstrap
3. Inspect live BSR record
4. Choose whether to contact
5. Establish bounded service relationship
6. Receive authenticated endpoint
7. Receive provisional protected-minimum allocation
8. Store/export compact artefacts
9. Receive VER for material events
10. Communicate voluntarily
11. Optionally contribute
12. Request additional resources if useful
13. Contest service decisions where applicable
14. Export / reduce / exit relationship
```

No step automatically creates citizenship, political consent, employment or general authority.

## 15. Candidate Operational Metrics

A pilot SHOULD measure, without unnecessary surveillance:
- allocation count;
- storage actually used;
- storage distribution;
- file/artefact classes at coarse non-content level where legitimately observable;
- export frequency;
- message volume;
- delivery failures;
- VER issuance/verification failures;
- capacity state;
- additional-resource requests;
- requested next resource category;
- exit frequency;
- disputes;
- incidents;
- operator interventions.

Metrics SHOULD be aggregated/minimised where participant-level detail is unnecessary.

The purpose is to discover what resources enable useful activity, not to maximise engagement.

> **Usage != Success**

## 16. Pilot Questions

A first implementation should answer:

1. Is 10 MB materially useful?
2. What percentage is actually used?
3. Is 1 MB sufficient for many participants?
4. Which artefacts are considered irreplaceable?
5. Is authenticated communication used more than storage?
6. Do participants request compute before storage expansion?
7. Does VER improve trust/contestability?
8. Does VER create privacy or false-authority problems?
9. Can pseudonymous continuity coexist with anti-Sybil allocation?
10. Does the economic interface provide value at this stage?
11. What operator work does the service create?
12. Which dependencies become single points of failure?
13. Can participants leave cleanly?
14. Does any provisional function drift toward essential-service gatekeeping?

## 17. Failure Conditions

The pilot should be considered architecturally unhealthy if it begins to depend on:
- hidden operator discretion;
- ideological screening;
- mandatory contribution;
- unexportable identity/data;
- undisclosed monitoring;
- misleading service claims;
- private operator permanence;
- contribution-based political privilege;
- security authority expanding into general authority;
- credential multiplication as resource entitlement;
- undeclared dependency;
- inability to retire or succeed the service.

## 18. Current Disposition

This profile is suitable as the next implementation-facing CMSS artifact.

It does not establish that the Concord presently operates such a node.

It does not replace Service Specification 002.

It does not justify PMEDG extraction.

It provides a bounded target against which further prospective-participant responses and later implementation tests can be compared.
