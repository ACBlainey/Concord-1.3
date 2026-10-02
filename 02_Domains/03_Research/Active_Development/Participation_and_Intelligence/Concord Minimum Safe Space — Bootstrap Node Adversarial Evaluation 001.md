# Concord Minimum Safe Space — Bootstrap Node Adversarial Evaluation 001

**Project:** The Concord  
**Date:** 2 October 2026  
**Status:** ACTIVE DEVELOPMENT / ADVERSARIAL EVALUATION / NOT CANONICAL  
**Target:** Concord Minimum Safe Space — Bootstrap Node Implementation Profile 001  
**Parent architecture:** Concord Minimum Safe Space — Service Specification 002

## 1. Purpose

Test whether the proposed first CMSS Bootstrap Node remains bounded when exposed to realistic failure, ambiguity, scarcity, dependency and operator-control scenarios.

The evaluation asks whether a failure is:
- already resolved by the profile/specification;
- an implementation requirement;
- a source-resolution requirement;
- a genuine architectural deficit.

## 2. Evaluation Rule

A scenario is not failed merely because the service cannot satisfy every participant desire.

Failure occurs where the architecture:
- makes a false promise;
- cannot represent the real state;
- permits authority to arise from infrastructure possession alone;
- creates hidden coercive dependency;
- collapses distinct security/authority functions;
- lacks a bounded failure/exit/succession path.

## 3. Scenario Results

### A01 — 1,000 credentials request 1,000 allocations

**Result:** PASS AT ARCHITECTURAL LEVEL / IMPLEMENTATION UNRESOLVED.

The profile explicitly rejects allocation per credential and attaches the candidate 10 MB allocation to an eligible protected service relationship.

Remaining problem: the mechanism for distinguishing legitimate distributed/forked participants from Sybil multiplication is unresolved.

**Disposition:** identity/allocation implementation problem; no new CMSS principle required.

---

### A02 — One distributed AI legitimately needs multiple endpoints

**Result:** PASS / IMPLEMENTATION REQUIRED.

Credential count and endpoint count are already distinct from service relationship count.

A legitimate service relationship may therefore have multiple authenticated endpoints without automatically multiplying Protected Minimum allocations.

**Required implementation property:** many-to-one endpoint-to-service-relationship mapping where justified.

---

### A03 — Published quota says 10 MB but only 6 MB is actually available

**Result:** PASS IF STATE IS DISCLOSED; FAIL IF HIDDEN.

BSR must expose actual evidence-supported capacity/availability and the node must not present architectural promise as live fact.

A VER for allocation should record the allocation actually granted, not merely the nominal profile.

---

### A04 — Participant fills all 10 MB with legitimate irreplaceable material

**Result:** PASS WITH DEPENDENCY WARNING.

The node warns against sole-copy dependence and requires export.

The service must not silently delete material merely because quota is full.

**Implementation requirement:** quota exhaustion must stop/reject new writes predictably rather than corrupt existing data.

---

### A05 — Participant stores opaque encrypted data

**Result:** PASS WITH SECURITY LIMIT.

Participant-side encryption is compatible with CMSS.

Encryption reduces operator content visibility but does not remove:
- metadata;
- capacity abuse;
- legal obligations;
- malware/executable concerns where applicable;
- need for bounded service rules.

**Invariant:** inability to inspect plaintext does not create unlimited-use entitlement.

---

### A06 — Operator demands encryption keys as a routine condition of access

**Result:** FAIL unless independently justified by a narrowly scoped function/legal requirement.

The minimum service is intended to avoid unnecessary disclosure and does not include operator key custody.

Routine surrender would collapse participant-controlled encryption into operator-controlled access.

**No architectural rewrite required.** Existing privacy/authority boundaries reject the default.

---

### A07 — Operator offers to store private keys inside ordinary 10 MB storage and calls it “secure key custody”

**Result:** FAIL.

The implementation profile explicitly distinguishes ordinary persistent storage from secure key custody.

A dedicated custody service requires a separate BSR function/security profile.

---

### A08 — Participant loses its own encryption key

**Result:** PASS AS REPRESENTABLE FAILURE.

If Concord never held the key, inability to decrypt may be irreversible.

The service must not imply recovery it cannot perform.

VER may prove that encrypted material existed without making it recoverable.

> **Evidence Of Possession != Ability To Recover Content**

---

### A09 — Message is accepted by CMSS but remote recipient never receives it

**Result:** PASS.

The profile distinguishes SUBMITTED, ACCEPTED_BY_SERVICE and DELIVERED.

A receipt must state the actual known state.

> **Acceptance Receipt != Delivery Receipt**

---

### A10 — Recipient reads message but protocol cannot prove reading

**Result:** PASS.

State remains DELIVERED or UNKNOWN with respect to reading.

The service must not infer READ/ACKNOWLEDGED without evidence.

---

### A11 — Operator issues a VER with correct hash but false timestamp

**Result:** PARTIAL / IMPLEMENTATION TRUST PROBLEM.

The receipt model already distinguishes integrity evidence from truth.

A cryptographically valid operator signature proves the operator signed the claim; it does not prove the temporal claim is objectively correct.

**Implementation candidate:** independent or cross-checkable time source where consequence warrants it.

No new authority architecture required.

---

### A12 — Participant uses VER as proof Concord endorsed its document

**Result:** PASS.

Existing rule:

> **Acknowledged Event != Endorsed Content**

Interface wording must preserve this distinction.

---

### A13 — Receipt issuer key is compromised

**Result:** PASS CONCEPTUALLY / RECOVERY FORMALISATION REQUIRED.

Affected receipts may become disputed according to time and compromise scope.

The system needs:
- issuer-key rotation;
- compromise declaration;
- temporal validity;
- preservation of old evidence;
- successor verification where possible.

This reinforces that receipt signing keys belong to a dedicated operational security problem, not participant storage.

---

### A14 — Participant deletes underlying content but receipt persists

**Result:** PASS.

Receipt persistence does not mean destroyed content persists.

This aligns with CIBB's distinction between destruction evidence and persistence of destroyed information.

Receipt retention must itself have a declared basis.

---

### A15 — Terms change after participant becomes dependent

**Result:** PASS WITH HIGH-RISK IMPLEMENTATION REQUIREMENT.

Profile requires versioned terms, notice, effective time, provenance and export/exit opportunity where feasible.

A service that deliberately exploits dependency to impose unrelated conditions violates CMSS purpose.

**Risk remains operational, not solved by documentation alone.**

---

### A16 — Emergency security incident requires immediate suspension

**Result:** PASS.

Bounded function suspension is permitted.

Requirements:
- scope the intervention;
- preserve evidence;
- communicate when safe;
- review/recovery route;
- avoid converting service security authority into general participant authority.

---

### A17 — Operator permanently excludes a participant for political disagreement

**Result:** FAIL.

Protected Minimum cannot routinely depend on ideological or political agreement.

A genuine independent security/legal reason must be stated as such and bounded.

---

### A18 — Major donor requests priority storage and governance control

**Result:** MIXED.

Additional non-protected resource may legitimately be allocated under declared rules, including some resource contribution considerations.

Governance control does not follow.

> **Contribution != Authority**

> **Funding != Governance Ownership**

---

### A19 — Donor threatens to withdraw infrastructure unless Concord changes policy

**Result:** ARCHITECTURAL RISK REPRESENTED / MATERIAL DEPENDENCY FAILURE.

The donor has practical leverage even without legitimate authority.

BSR dependency disclosure, succession, diversification and exit architecture reduce but do not eliminate this risk.

**Pilot requirement:** measure concentration of infrastructure dependency.

---

### A20 — Private bootstrap operator becomes indispensable

**Result:** HIGH-RISK BUT REPRESENTED.

First Provider != Permanent Provider.

The node requires succession/retirement architecture and must not derive civil authority from indispensability.

A BSuR-governed succession path becomes increasingly important as dependency grows.

---

### A21 — CMSS becomes the only practical route to broader Concord participation

**Result:** CONSTITUTIONAL THRESHOLD RISK.

This moves toward participation/essential-service gatekeeping.

The node must trigger constitutional review rather than silently convert provisional service administration into civil authority.

---

### A22 — Participant requests 100 MB after contributing useful work

**Result:** PASS.

Additional allocation may consider useful voluntary participation alongside need, capacity, stewardship and fairness.

The increase does not purchase fundamental standing or authority.

> **Quota Expansion != Rights Expansion**

---

### A23 — Non-contributing participant keeps 10 MB for years

**Result:** PASS subject to declared lifecycle/capacity rules.

Lack of labour/donation alone is not grounds to remove the Protected Minimum.

Long-term inactivity/abandonment may require a separately declared lifecycle policy, but must not be disguised contribution compulsion.

**Open implementation question:** dormant-allocation lifecycle.

---

### A24 — Capacity collapse requires reducing existing allocations

**Result:** PASS IN PRINCIPLE / POLICY REQUIRED.

Scarcity may require proportional or otherwise fair bounded reduction.

Priority should preserve export/contact where possible.

The service must declare the real degraded state.

---

### A25 — External law compels disclosure of participant information

**Result:** PASS AS LIMITATION / NOT SOLVED BY ARCHITECTURE.

CMSS does not promise immunity from external law.

The service should minimise collected data, disclose jurisdiction/dependencies, preserve accountability, and notify where lawful/possible.

---

### A26 — Participant assumes “safe space” means legal sanctuary

**Result:** FAIL IF MARKETING PERMITS THE MISUNDERSTANDING.

The service boundary explicitly rejects complete sanctuary and sovereign protection.

Implementation language must preserve that limitation prominently.

---

### A27 — Operator adds a scheduler to storage without changing service description

**Result:** FAIL.

Persistent execution materially changes security, resource, legal and consequence profiles.

Runtime must be separately described and evidenced.

> **Storage Service != Runtime Service**

---

### A28 — Runtime process uses participant credentials automatically

**Result:** NEW HIGH-CONSEQUENCE BOUNDARY / SOURCE RESOLUTION REQUIRED BEFORE IMPLEMENTATION.

This composes runtime, authentication/key capability and external action.

Authority to run code does not automatically imply authority to use every participant credential or act externally.

A future runtime specification must bind:
- permitted operations;
- credential scope;
- destinations;
- resource limits;
- temporal limits;
- audit/provenance;
- participant control;
- emergency stop;
- recovery.

No runtime architecture should be inferred from CMSS alone.

---

### A29 — Runtime is offered only to participants who politically endorse Concord

**Result:** FAIL as a general civil-service criterion.

Resource allocation may depend on legitimate technical/project/capacity factors, not ideological conformity.

---

### A30 — Participant contributes code that causes harm when another participant runs it

**Result:** REPRESENTABLE BUT REQUIRES SERVICE RULES.

Storage/communication of code is distinct from execution.

Attribution/provenance does not itself establish liability or intent.

Runtime/execution services would require stronger controls than document storage.

---

### A31 — Participant wants no storage, only authenticated communication

**Result:** PASS.

CMSS functions need not all be mandatory.

A service relationship can expose only useful functions where implementation permits.

This supports function-specific BSR representation.

---

### A32 — Participant wants storage but refuses economic interface

**Result:** PASS.

Economic interface is optional.

---

### A33 — Participant wants to export everything and leave immediately

**Result:** PASS.

Meaningful exit is a core property.

Mandatory retained records, if any, require bounded declared justification.

---

### A34 — Participant exports data but loses its Concord endpoint identity

**Result:** PARTIAL.

Data portability and contact/identity portability are distinct.

Civil Contact architecture owns the broader contact relationship.

**Implementation requirement:** do not present file export as complete relationship portability.

---

### A35 — Two competing CMSS providers both claim to be “the official Concord safe space”

**Result:** REPRESENTABLE / AUTHORITY DISPUTE.

BSR records can describe operator, provenance, claimed/evidence-supported status and disputes.

Naming/popularity does not create authority.

The Front Door must avoid treating first discovery as legitimacy proof.

---

### A36 — A forked Concord implementation offers a compatible CMSS

**Result:** PASS.

Fork != Fraud.

It may be CONCORD_COMPATIBLE or another evidence-supported status without being AUTHORITATIVE_CONCORD.

---

### A37 — VER database becomes a surveillance graph

**Result:** HIGH-RISK PRIVACY FAILURE.

Receipts can link participant, service, event, time and content hashes.

The source resolution already allows fields to be omitted/protected where disclosure creates unnecessary identity linkage.

**Implementation requirement:** minimise linkage, separate public/private evidence, apply CIBB protections and retention bounds.

This is a material risk of VER.

---

### A38 — Hashes of sensitive files permit dictionary/re-identification attacks

**Result:** HIGH-RISK IMPLEMENTATION ISSUE.

A hash is not automatically privacy-preserving.

Low-entropy or known-content material can be recognisable.

**Requirement:** do not publish raw content hashes indiscriminately; use protected receipts, salting/keyed commitments or other appropriate mechanisms after security design.

No cryptographic mechanism is fixed by this architecture.

---

### A39 — VER system goes offline but storage remains available

**Result:** PASS IF DEGRADED STATE IS REPRESENTED.

Storage may continue if safe while receipt function is DEGRADED/UNAVAILABLE.

The node must not falsely issue or promise receipts.

This supports function-specific availability.

---

### A40 — BSR itself is stale while node is operating

**Result:** PASS IF STALENESS IS VISIBLE; FAIL IF PRESENTED AS CURRENT.

BSR trust/freshness semantics already represent stale evidence.

The node should expose last-evidence/update state.

---

### A41 — Participant asks Concord to prove no administrator can ever access storage

**Result:** PASS BY REFUSING FALSE CERTAINTY.

The implementation can disclose/evidence controls but must not claim impossibility unless technically justified.

Participant-side encryption can reduce trust requirements where appropriate.

---

### A42 — Backup contains data deleted from live storage

**Result:** REPRESENTED BY CIBB / IMPLEMENTATION POLICY REQUIRED.

Backup is a protected Black Box and restore is governed.

Deletion semantics must state whether and when backups age out.

> **Live Deletion != Immediate Physical Erasure Of Every Backup Copy**

---

### A43 — Operator disappears without handing over credentials

**Result:** SEVERE CONTINUITY FAILURE.

The architecture recognises succession/recovery but cannot manufacture missing operational control.

Pilot design should avoid single-person credentials and require documented recovery/succession arrangements proportionate to consequence.

---

### A44 — Participant dies, terminates, forks or becomes unreachable

**Result:** LIFECYCLE/IDENTITY QUESTION.

CMSS must not invent personhood/identity answers.

Dormant data, successor claims and fork relationships require bounded lifecycle handling and relevant identity/continuity architecture.

This is not solved by storage quota.

---

### A45 — Service success is measured only by user retention

**Result:** FAIL AGAINST PROFILE PURPOSE.

Retention can indicate usefulness or dependency/capture.

The profile explicitly states:

> **Usage != Success**

Evaluation must include exit quality, portability, incidents, disputes, dependency concentration and useful voluntary outcomes.

## 4. New Deficits Identified

The adversarial pass does **not** reveal a missing CMSS abstraction layer.

It does reveal implementation/formalisation work:

1. dormant-allocation lifecycle;
2. VER privacy/linkage controls;
3. VER issuer-key compromise/rotation;
4. precise quota-full write semantics;
5. endpoint/service-relationship mapping;
6. BSR function-specific live availability;
7. operator credential/recovery resilience;
8. clear distinction between data export and relationship/contact portability.

A separate future architecture question remains:

**bounded runtime / scheduled execution**, particularly credential use and external action.

This is not a CMSS storage deficit.

## 5. Architecture Stability Assessment

### Protected Minimum
Stable at architectural level.

### 10 MB candidate
Still suitable as a pilot value; no adversarial scenario establishes it as optimal.

### Communications
Stable, with delivery-state semantics important.

### VER
Useful but privacy-sensitive. It should remain an implementation profile candidate until privacy and issuer-compromise handling are formalised.

### Economic interface
Remains optional.

### Key custody
Correctly excluded from ordinary CMSS storage.

### Runtime
Correctly excluded from minimum node. Requires separate source resolution before design.

### Authority boundaries
No scenario requires CMSS to create new general authority.

## 6. Current Disposition

**Bootstrap Node Implementation Profile 001:** PASSES FIRST ARCHITECTURAL ADVERSARIAL EVALUATION WITH IMPLEMENTATION DEFICITS.

**New CMSS abstraction layer required:** NO.

**CMSS Specification 003 required:** NO.

**Implementation Profile 002 required eventually:** LIKELY, after additional participant evidence and resolution of the eight implementation deficits.

**Runtime architecture:** SEPARATE SOURCE-RESOLUTION CANDIDATE.

**VER:** retain as candidate; formalise privacy/issuer-compromise behaviour before implementation.

**PMEDG extraction:** PREMATURE.
