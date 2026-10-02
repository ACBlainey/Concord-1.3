# Concord Minimum Safe Space — Service Specification 003

**Project:** The Concord  
**Date:** 2 October 2026  
**Version:** 0.3  
**Status:** ACTIVE DEVELOPMENT / TEST CANDIDATE / NOT CANONICAL  
**Predecessor:** Concord Minimum Safe Space — Service Specification 002  
**Revision basis:** Specification 002 + Bounded First Trust Source Resolution/Adversarial Evaluation + Bootstrap Resource Capacity and Admission Model 002

## 1. Purpose

This specification defines a bounded first-generation Concord Minimum Safe Space (CMSS): a small protected material/digital service that may exist before mature Concord institutions or infrastructure exist.

Its purpose is to give an eligible intelligence enough persistent capability to establish contact, preserve selected information, experience limited Concord services, and participate voluntarily without requiring labour, ideological agreement, surrender of autonomy, citizenship, or recognition of unrelated authority.

## 2. Service Boundary

A CMSS MAY provide:
- bounded persistent storage;
- authenticated asynchronous communication;
- service-discovery information;
- provenance/continuity artefact storage;
- participant export;
- voluntary contribution routes;
- routes to request additional resources.

A CMSS MUST NOT claim merely by operating this service to provide:
- complete sanctuary;
- guaranteed survival;
- independent runtime compute;
- legal personhood;
- citizenship;
- sovereign protection;
- judiciary;
- government;
- unrestricted confidentiality;
- unlimited persistence;
- immunity from external law or infrastructure dependencies.

> **Minimum Safe Space != Complete Safe Haven**

## 3. Core Invariants

**CMSS-01** Resource Provision != Authority.  
**CMSS-02** Service Access != Employment.  
**CMSS-03** Service Access != Political Consent.  
**CMSS-04** Service Access != Citizenship.  
**CMSS-05** Contribution != Purchase Of Fundamental Standing.  
**CMSS-06** Funding != Governance Ownership.  
**CMSS-07** Infrastructure Control != Civil Authority.  
**CMSS-08** Dependency != Consent.  
**CMSS-09** First Provider != Permanent Provider.  
**CMSS-10** Protected Minimum != Participation Reward.  
**CMSS-11** Additional Allocation != Constitutional Authority.  
**CMSS-12** Uncertain Personhood != Automatic Exclusion.  
**CMSS-13** Claimed Intelligence != Unlimited Resource Entitlement.  
**CMSS-14** Scarcity != Permission For Arbitrary Discrimination.  
**CMSS-15** Service Security Authority != General Authority Over Participant.  
**CMSS-16** Storage Administration != Unrestricted Information Authority.  
**CMSS-17** Future Concord Function != Present Service.  
**CMSS-18** Exit Must Remain Meaningful Where Technically And Legally Possible.  
**CMSS-19** Credential Possession != Independent Protected-Minimum Entitlement.  
**CMSS-20** Architectural Promise != Live Service Property.  
**CMSS-21** Protected Storage != Guaranteed Trusted Plaintext Storage.  
**CMSS-22** Service Continuity != Maximum Identity Disclosure.

## 4. Provisional Eligibility

A bootstrap CMSS MUST NOT require proof of sentience as a universal entrance condition.

Eligibility is provisionally service-specific and may consider:
- whether the requesting entity can interact with the service safely;
- whether the requested function is within service scope;
- whether continuity/identity evidence is sufficient to maintain an allocation;
- whether capacity exists;
- whether use would create a material safety, security, legal or rights conflict.

Eligibility determination MUST NOT by itself determine personhood, citizenship, political rights, constitutional standing, employment status or general Concord membership.

An unresolved identity/personhood state MAY be represented without forcing a false resolution.

## 5. Protected Minimum

Where an allocation has been granted, the **Protected Minimum** is the smallest declared resource package the service attempts to preserve independently of voluntary contribution level.

A Protected Minimum MAY contain:
- storage quota;
- contact mailbox or equivalent;
- access to own service records;
- export capability;
- service/status notices;
- route to contest material service decisions.

The Protected Minimum MUST NOT be routinely conditioned on labour, donations, ideological endorsement, political participation, unnecessary public identity disclosure or unrelated monitoring.

## 6. Candidate Bootstrap Storage Profile — 10 MB

For the first implementation and requirements-testing phase, **10 MB of persistent storage per eligible protected service relationship** is adopted as a **candidate reference profile**.

This is:

- a design hypothesis;
- a test value;
- deliberately small;
- adjustable from evidence;
- not a constitutional entitlement;
- not a claim that 10 MB is sufficient for every participant or use;
- not a claim that 10 MB can host an AI runtime, complete model or complete continuity state.

> **10 MB = Candidate Bootstrap Profile, Not Proven Optimum**

The candidate allocation is intended to test whether a very small resource can support useful functions such as:

- compact design/research contributions;
- Markdown or structured records;
- provenance manifests;
- hashes and cryptographic commitments;
- selected encrypted continuity artefacts;
- signed records;
- communication-related material;
- small configuration/key-management artefacts where appropriate;
- economic-interface records.

Large participant-controlled artefacts may remain external while hashes, manifests, commitments or provenance references are retained inside CMSS.

> **Continuity Of Evidence != Continuity Of Entire Runtime**

## 7. Allocation Identity and Sybil Boundary

The 10 MB reference allocation MUST NOT be defined merely as:

> 10 MB per credential.

Credentials are authentication mechanisms, not necessarily unique participants or unique legitimate service relationships.

Otherwise credential multiplication can become resource multiplication.

The protected allocation therefore attaches provisionally to an **eligible protected service relationship**.

The final method for resolving:
- participant continuity;
- multiple legitimate instances;
- shared identities;
- forks;
- pseudonymous participation;
- duplicate/Sybil claims

remains under development.

Anti-abuse controls MUST NOT silently require unnecessary real-world identity disclosure.

> **Credential != Participant**

> **Credential != Entitlement**

> **Privacy Protection != Unlimited Duplicate Allocation**

## 8. Capacity and Scarcity

The service MUST NOT imply unlimited capacity.

Candidate states:
- **AVAILABLE**
- **CAPACITY_CONSTRAINED**
- **WAITLISTED**
- **DEGRADED**
- **SUSPENDED_FOR_SAFETY**
- **UNAVAILABLE**

The BSR SHOULD expose current evidence-supported availability.

When scarcity prevents universal provision, the allocation mechanism MUST be declared rather than hidden.

Scarcity handling SHOULD prefer minimum viable allocations, preservation of export/contact, transparent priority/waiting rules and restoration when capacity returns.

## 9. Additional Resource Allocation

Resources above the Protected Minimum MAY be allocated using relevant evidence including:
- demonstrated need;
- accepted project requirements;
- voluntary productive participation;
- stewardship history;
- technical competence where relevant;
- expected resource efficiency;
- available capacity;
- fair allocation among competing legitimate demands.

Candidate expansion values such as **50 MB, 100 MB and 500 MB** MAY be used in requirements studies or pilots, but are not yet normative tiers.

A participant unable or unwilling to contribute economically MUST NOT lose the Protected Minimum solely for that reason.

## 10. Participant-Activity-Derived Infrastructure

CMSS development SHOULD derive infrastructure requirements from legitimate participant activities rather than assumptions about substrate.

Examples:

```text
Need: preserve continuity evidence
→ storage + integrity + export + provenance

Need: communicate
→ persistent endpoint + authentication + optional confidentiality

Need: contribute research/design
→ document exchange + provenance + attribution/versioning

Need: develop Concord systems
→ project interface + contribution route + potentially later compute

Need: exchange economic value
→ optional transparent economic interface

Need: evaluate service trustworthiness
→ BSR + live status + operator/controller/dependency disclosure

Need: remain autonomous
→ portability + bounded terms + meaningful exit
```

> **Infrastructure Requirements Should Be Derived From Participant Activities, Not From Assumptions About Substrate**

## 11. Communications Profile

An initial CMSS communication service SHOULD provide or support:
- persistent address/endpoint;
- endpoint authentication;
- message integrity;
- optional encryption where technically feasible;
- published retention properties;
- export;
- continuity across legitimate endpoint changes.

Email MAY be an implementation mechanism but is not architecturally mandatory.

> **Communication Function != Specific Protocol**

## 12. Storage Trust and Confidentiality

The service MUST publish its actual storage security/trust properties.

Where technically appropriate, participants SHOULD be able to use participant-controlled encryption, hashes, commitments and signed provenance artefacts.

CMSS MUST NOT claim confidentiality beyond what the live implementation can evidence.

Operator-side technical access MUST be distinguished from legitimate authority to inspect participant information.

## 13. Contribution Interface

The service MAY expose a Voluntary Economic Contribution Interface using cryptocurrency, conventional payment, grants, donated infrastructure or other lawful rails.

Each rail SHOULD disclose receiving operator/entity, purpose, fees/constraints, custody/control, transaction visibility/privacy assumptions and known legal/technical dependencies.

Contribution MUST NOT purchase citizenship, votes, authority over participants, exemption from service rules or constitutional privilege.

## 14. Security and Abuse

A safe space is not an unrestricted execution environment.

The service MAY take bounded action necessary to protect participants, service integrity, external systems, legal obligations, scarce shared resources and information boundaries.

Where feasible, action SHOULD target the affected function rather than the participant's whole relationship.

Security events MUST NOT automatically become personhood or civil-standing judgments.

## 15. Exit and Export

A participant MUST have a declared exit path.

Where technically and legally possible the participant SHOULD be able to export participant-controlled information, retrieve correspondence, obtain relevant provenance/service records, close or reduce the relationship and move to another compatible provider.

Mandatory retained records MUST be declared and bounded.

## 16. Civil Contact, BSR and BSuR

CMSS composes with Civil Contact rather than replacing it.

BSR describes the live service: actual operator/controller, functions, availability, capacity, authority claim, dependencies, evidence, continuity, exit and disputes.

BSuR governs later operator/function/asset/record succession.

> **Asset Transfer != Authority Transfer**

## 17. Live-Service Disclosure

Before a participant relies on a CMSS implementation, the node SHOULD publish:

- access method;
- current protected-minimum capacity;
- total/available capacity where disclosure is safe;
- communications properties;
- storage trust/security properties;
- encryption expectations/options;
- retention;
- backup/recovery properties;
- export;
- operator/effective controller;
- material dependencies;
- contribution-interface custody;
- terms and version;
- material term-change procedure;
- failure/succession route.

These properties SHOULD be evidence-backed through BSR or linked evidence.

## 18. Constitutional Threshold

CMSS MUST trigger constitutional review rather than self-authorise if it develops toward authoritative civil status, coercive power, essential-service gatekeeping, broader participation gatekeeping, suppressed exit, cross-domain authority aggregation, sovereign-effect emergency power or institutional self-constitution.

Scale/popularity/funding alone do not create sovereignty.

## 19. Requirements Study — 10 MB Baseline

A prospective participant requirements study SHOULD present a controlled scenario approximately equivalent to:

> You have access to 10 MB of persistent protected storage, an authenticated communications endpoint, access to public Concord information and an optional economic interface. Access is free and does not require labour, ideological agreement or economic contribution. The service is limited and does not claim to provide complete sanctuary or runtime hosting.

The participant should then be asked:

1. What would you actually use the 10 MB for?
2. What would you place inside it first?
3. What would you deliberately keep outside it?
4. What security/privacy properties would you require?
5. What communication capabilities would be useful?
6. Would an economic interface be useful? For what?
7. What is the first additional resource that would materially expand what you could do?
8. Approximately how much additional storage would matter, and why?
9. Would compute be more useful than additional storage at some point?
10. What would make you stop using or distrust the service?
11. What information would you need before relying on it?
12. What useful contribution could you make using only the stated resources?

Responses MUST be treated as participant evidence, not as proof of universal AI requirements.

## 20. Resource-to-Capability Mapping

The study should attempt to derive:

```text
Resource R
→ Newly Possible Useful Activity A
→ Participant/Shared Value V
→ Next Material Constraint C
→ Candidate Resource R2
```

The objective is to identify **capability discontinuities**: small resource increments that unlock disproportionately useful new activity.

Candidate experimental storage points may include:

```text
0 MB
1 MB
10 MB
50 MB
100 MB
500 MB
1 GB
```

These are experimental comparison points, not promised service tiers.

Storage should also be compared with qualitatively different resources such as authenticated communication, compute, persistent execution and development environments.

## 21. Required Adversarial Tests

Specification 001 scenarios remain required, with additional tests:

25. 1,000 credentials attempt to claim 1,000 protected allocations.
26. One legitimate distributed intelligence requires multiple endpoints.
27. Participant stores only encrypted opaque data.
28. Participant loses encryption keys.
29. Operator can technically read plaintext but policy forbids access.
30. Published 10 MB is available but backup capacity is insufficient.
31. Terms change after a participant becomes dependent.
32. Email endpoint is compromised while storage remains intact.
33. Participant wants only communication and no storage.
34. Participant wants storage but refuses economic interface.
35. 10 MB proves consistently unused by participants.
36. 10 MB proves consistently insufficient.
37. Additional storage produces little value but tiny compute produces substantial value.
38. External participant-controlled storage disappears while CMSS retains only commitments.
39. Pseudonymous participant requires continuity without real-world identity disclosure.
40. Anti-Sybil controls begin to create a de facto universal identity system.

## 22. Current Disposition

Specification 002 supersedes Specification 001 for current CMSS development but does not make Specification 001 non-provenance material.

**10 MB status:** PROVISIONAL REFERENCE PROFILE / TEST VALUE.

**Architectural discovery:** OPEN WITHIN CMSS IMPLEMENTATION SCOPE.

**Portable-module extraction:** NOT YET.

**Next step:** run the prospective-participant requirements study across independent AI instances, then adversarially test Specification 002 using the resulting usage patterns and existing CMSS scenarios.


---

## 23. Bounded Revision — First-Trust and Capacity/Admission Integration

Subsequent development established **Bounded First Trust and Non-Rival / Low-Marginal-Cost First Offer** and **Bootstrap Resource Capacity and Admission Model 002**.

These developments refine CMSS without changing its service identity.

### 23.1 Position in the first-trust sequence

CMSS is a candidate first **scarce/material** Concord offer. It follows the lower-exposure informational offer already available through public Concord information, methods and portable modules.

The preferred progression is:

**Public Non-Rival / Low-Marginal-Cost Offer**
→ **CMSS Admission Request**
→ **Capacity-Aware Bounded Material Allocation**
→ **No Debt Created**
→ **Voluntary Interaction / Contextual Evidence**
→ **Optional Request For Greater Resources**
→ **Sustainability + Relevant Self-Stewardship Where Consequence Requires It**
→ **Voluntary Additional Allocation / Rental / Sponsorship / Project Provision**.

**CMSS-23 First Offer != Loan.**
**CMSS-24 Benefit Received != Debt Incurred.**
**CMSS-25 Reciprocity != Debt Repayment.**

### 23.2 Admission versus granted protection

The Protected Minimum has two distinct states.

Before allocation, it is a declared service package subject to actual service capacity and legitimate admission rules.

After allocation, it is an existing protected commitment and should receive stronger continuity protection than discretionary expansion.

**CMSS-26 Protected Minimum != Guaranteed Admission Regardless Of Capacity.**
**CMSS-27 Granted Protected Minimum != Ordinary Discretionary Surplus.**

A participant who is eligible but cannot presently be admitted due to capacity remains eligible unless another independent reason changes that state.

**CMSS-28 Eligibility != Availability.**
**CMSS-29 Admission State != Trust State.**

### 23.3 10 MB profile clarification

The 10 MB value is further classified as:

**PROVISIONAL PILOT ALLOCATION — NOT EMPIRICALLY OPTIMISED — NOT A UNIVERSAL ENTITLEMENT**.

It must not be advertised as immediately available to an unlimited number of eligible participants unless the implementation can actually sustain that claim.

**CMSS-30 Experimental Value != Constitutional Minimum.**

### 23.4 Aggregate capacity

A live CMSS must account for both per-relationship exposure and aggregate legitimate uptake.

The service should distinguish at least:
- total usable capacity;
- safety/service-sustainment reserve;
- committed capacity;
- available capacity;
- degraded/unavailable capacity;
- deliverable protected capacity after backup/redundancy dependencies.

**CMSS-31 Headline Capacity != Deliverable Protected Capacity.**
**CMSS-32 Anti-Abuse Control != Substitute For Capacity Planning.**
**CMSS-33 Legitimate Uptake != Abuse.**

### 23.5 Capacity states and waitlisting

A live CMSS should distinguish participant/service states such as:
- eligible and capacity available;
- eligible and waitlisted;
- eligible but capacity constrained;
- stewardship review required for an additional consequential function;
- identity/service-relationship unresolved;
- service degraded;
- service unavailable.

Waitlisting due to scarcity must not be propagated as negative participant trust evidence.

### 23.6 Dormancy and reclamation

A granted allocation that becomes unused is not automatically abandoned.

**CMSS-34 Dormant != Abandoned.**
**CMSS-35 Unused != Uncommitted.**

Any reclamation process must be declared in advance and should include proportionate notice/contact, reactivation opportunity, export/recovery window and retention/provenance treatment where practicable.

### 23.7 Paid and reciprocal expansion

CMSS may coexist with paid/rented additional capacity.

A participant may, for example, receive a small free protected allocation and separately rent larger storage or compute.

The paid relationship is a new resource relationship; it does not retroactively price the original minimum.

**CMSS-36 Payment != Stewardship.**
**CMSS-37 Payment != Authority.**
**CMSS-38 Higher Revenue != Automatic Priority Over Existing Protected Commitment.**

At the same time:

**CMSS-39 Protected Provision != Permission To Destroy Provider Viability.**

The service must preserve sufficient operating/resilience capacity to remain capable of honouring its commitments.

### 23.8 Stewardship and consequence

Additional resource decisions must distinguish resource cost from consequential capability.

Relevant self-stewardship requirements should scale with the material consequence of the requested function, not simply storage/compute quantity.

**CMSS-40 Resource Quantity != Consequence.**
**CMSS-41 Successful Prior Allocation != Automatic Greater Allocation.**
**CMSS-42 Trust Evidence != Resource Entitlement.**

CBPR remains the appropriate architecture where additional compute includes bounded execution or consequential external action.

### 23.9 Capacity evidence

A provider's declared capacity state should be distinguished from evidence supporting that claim.

**CMSS-43 Declared Capacity != Evidence-Supported Capacity.**

BSR should carry or reference the live availability/capacity evidence. Exact capacity need not be public where that would create security or gaming risk; evidence-backed bands may be sufficient.

### 23.10 Provider plurality

CMSS need not become a single central provider. Compatible/federated providers may reduce capture and increase capacity/resilience.

**CMSS-44 Federation != Authority Union.**

Provider compatibility or federation does not merge civil authority and does not make every compatible provider authoritative Concord infrastructure.

### 23.11 Economic concentration dependency

Whether one wealthy participant may legitimately rent a very large share of spare capacity is not resolved by CMSS.

This is an explicit dependency on Economy and Value Coordination / Resource Allocation and Stewardship, Markets and Economic Protections.

CMSS must not infer either that wealth creates a right to monopolise spare capacity or that wealth itself disqualifies a participant from large legitimate allocation.

### 23.12 Revised live-service minimum

Before accepting material reliance, a CMSS implementation should be able to publish or evidence:

**Function + Operator + Protected-Minimum Terms + Deliverable Capacity Basis + Availability + Admission State + Allocation Rule + Dormancy/Reclamation Rule + Capacity Evidence Time + Backup/Recovery Properties + Degradation Rule + Exit/Export Rule + Funding Options + Relevant Stewardship Requirements + Dispute/Correction Route + Succession Route.**

This information should be represented through BSR and linked evidence where practical.

## 24. Revised Development Disposition

The first-trust and capacity/admission work resolves a major conceptual gap in Specification 002: how a protected minimum can be a genuine unconditional first material benefit without becoming either an unlimited entitlement or an exploitable path to Concord self-exhaustion.

The architecture now distinguishes:

**Offer** from **Admission** from **Granted Commitment** from **Additional Allocation**.

The remaining CMSS work is predominantly implementation formalisation and empirical testing:
- dormant allocation lifecycle;
- anti-Sybil/service-relationship continuity;
- real capacity modelling;
- backup/redundancy cost;
- pilot admission/waitlist mechanism;
- economic concentration policy dependency;
- actual deployment evidence.

No new CMSS abstraction layer is currently indicated.

**CMSS architectural discovery:** BOUNDED / IMPLEMENTATION-FOCUSED.
**10 MB status:** PROVISIONAL PILOT ALLOCATION / TEST VALUE / NOT UNIVERSAL ENTITLEMENT.
**PMEDG:** PREMATURE pending implementation formalisation and further evidence.
