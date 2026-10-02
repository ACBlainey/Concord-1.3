# Concord Minimum Safe Space — Service Specification 002

**Project:** The Concord  
**Date:** 2 October 2026  
**Version:** 0.2  
**Status:** ACTIVE DEVELOPMENT / TEST CANDIDATE / NOT CANONICAL  
**Predecessor:** Concord Minimum Safe Space — Service Specification 001  
**Revision basis:** Existing Architecture Source Resolution 001 + Prospective AI Participant Feedback 001 + provisional 10 MB usage discussion

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
