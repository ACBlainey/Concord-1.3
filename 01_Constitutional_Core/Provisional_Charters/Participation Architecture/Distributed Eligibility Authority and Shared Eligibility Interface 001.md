# Distributed Eligibility Authority and Shared Eligibility Interface 001

**Author:** Alexander C. Blainey — Independent Researcher  
**Project:** The Concord Framework  
**Framework Version:** Concord V1.3  
**Status:** ACTIVE DEVELOPMENT / PROVISIONAL / NON-CANONICAL / SOURCE-RESOLVED INTERFACE NOTE  
**Date:** September 2026

---

# 1. Question

Recent participation work produced an unresolved dependency:

> **Where should participant eligibility be calculated?**

One possible answer would be a central Concord Eligibility Authority.

This source-resolution pass does **not** find sufficient architectural support for such a central sovereign eligibility institution.

Instead, existing Concord principles point toward:

> **Distributed decision authority + shared eligibility representation and routing.**

---

# 2. Source basis

## Bounded Contextual Authority

Existing architecture states:

> **Authority is function-derived, not person-derived.**

Authority exists only to the extent required by a legitimate function in a valid context.

This argues against one general eligibility body acquiring universal authority merely because many systems need eligibility decisions.

## Fractal Permission Architecture / Minimum Necessary Capability

Existing permission architecture treats access and authority as:
- contextual;
- function-specific;
- minimum necessary;
- bounded;
- non-propagating.

Permission in one context does not automatically create permission elsewhere.

## Civil Contact Point

Existing Civil Contact architecture separates:
- identity;
- contact;
- residence;
- participation;
- citizenship;
- service access.

It explicitly leaves participation/service rules with wider civil architecture rather than making the Contact Point sovereign.

## CH002 / CH003 / CH005

Existing topology tests repeatedly identify the same pattern:
- consequential classifications require contestability;
- Civil Contact should not become final decision authority;
- interfaces with material gatekeeping power require anti-capture architecture;
- existing functions should be connected rather than duplicated.

## KCS

KCS can represent dependencies and propagate review after change.

It explicitly does not gain authority over dependent systems merely because it knows their relationships.

> **Dependency != Subordination.**

---

# 3. Provisional rule

Eligibility should ordinarily be determined by the legitimate authority responsible for the function whose access is being considered.

Examples:

- Education determines whether its own educational prerequisites/qualifications are satisfied.
- Health determines clinical/service conditions within legitimate Health authority.
- a property/stewardship system determines applicable property eligibility under established civil rules.
- Governance determines governance-role conditions within constitutional bounds.
- Civil Security determines security-role suitability within legitimate bounded authority and review.
- an infrastructure operator determines technical-role qualification within its legitimate functional envelope.
- Judiciary determines legal consequences where adjudication is required.

No domain acquires general authority over the participant merely because it supplies one eligibility input.

> **Domain Eligibility Authority != General Civil Authority.**

---

# 4. Shared eligibility interface

Distributed authority does not require fragmented participant experience.

A shared eligibility interface may represent:

**Requested Function / Benefit / Role**
+
**Applicable Rule Set**
+
**Participation Requirement**
+
**Citizenship / Residence Requirement where relevant**
+
**Education / Qualification Requirement**
+
**Contextual Trust Requirement**
+
**Security / Suitability Requirement**
+
**Active Restriction / Recovery State**
+
**Resource / Scarcity Condition**
+
**Owning Decision Authority**
→
**Current Eligibility State**

The interface can answer:

- Am I currently eligible?
- Which requirement is satisfied?
- Which requirement is missing?
- Which institution owns that requirement?
- What route exists to satisfy it?
- What evidence supports the state?
- When will it next be reviewed?
- Can I challenge it?
- What changed?

The interface should not itself invent the requirements.

---

# 5. Candidate eligibility states

A shared representation may need states such as:

- ELIGIBLE;
- INELIGIBLE — MISSING PREREQUISITE;
- CONDITIONALLY ELIGIBLE;
- ELIGIBLE WITH SUPERVISION;
- PENDING ASSESSMENT;
- PENDING RESOURCE AVAILABILITY;
- TEMPORARILY RESTRICTED;
- RECOVERY / REQUALIFICATION IN PROGRESS;
- EXPIRED / REASSESSMENT REQUIRED;
- DISPUTED;
- UNKNOWN / INCOMPLETE EVIDENCE.

These are provisional interface semantics, not adopted legal classifications.

UNKNOWN must remain a legitimate state.

> **Unknown Eligibility != Automatic Denial or Automatic Permission.**

The appropriate handling depends on consequence and legitimate domain rules.

---

# 6. Eligibility is compositional

A participant may satisfy some requirements and not others.

Example:

**P4 participation requirement:** satisfied  
**Required engineering qualification:** satisfied  
**Security suitability:** pending  
**Active relevant restriction:** none  
**Vacancy/resource availability:** available

Result:

**PENDING — SECURITY SUITABILITY**

The system should not collapse this into a vague:

**Not Eligible**

where a more precise state is safely available.

This precision allows the participant to know what remains to be done.

---

# 7. Eligibility and allocation are different

Meeting eligibility conditions does not always guarantee allocation.

A participant may be eligible for:
- a scarce service;
- a job;
- a property opportunity;
- a stewardship grant;
- a limited resource;

without being guaranteed receipt.

Therefore:

> **Eligibility != Allocation.**

Allocation may require a separate legitimate process involving:
- scarcity;
- priority;
- queue;
- merit relevant to the function;
- lottery;
- matching;
- local need;
- other later-defined legitimate mechanism.

Eligibility should not silently become allocation authority.

---

# 8. Eligibility and entitlement are different

Some conditions create an entitlement once satisfied.

Others merely permit consideration.

The shared interface should distinguish:

## Entitlement
If conditions are met, provision is due subject to legitimate operational constraints.

## Eligibility
The participant may access/apply/be considered.

## Qualification
The participant has demonstrated required capability.

## Permission
The participant is authorised for a bounded action/context.

## Allocation
A scarce opportunity/resource has actually been assigned.

## Authority
The participant may exercise a consequential civil function.

These should not collapse into one status.

---

# 9. Automatic computation without central sovereignty

A shared technical service may compute or assemble eligibility from domain-supplied rules and verified state.

That does not make the technical service the civil authority.

The distinction is:

**Domain Supplies Legitimate Rule / State**
→ **Shared Interface Computes or Assembles Result**
→ **Owning Domain Remains Accountable for Its Rule/Decision**

Where several domains jointly determine an outcome, the interface should preserve each contribution rather than inventing a false single owner.

> **Computation != Authority.**

---

# 10. Participant-facing eligibility view

Civil Historical Access should eventually allow a participant to inspect:

- current eligibility states;
- satisfied prerequisites;
- missing prerequisites;
- source/owner of each condition;
- education/qualification pathways;
- active restrictions;
- sunset/review dates;
- recovery pathways;
- disputed inputs;
- relevant provenance;
- allocation state where separate.

Civil Contact should notify the participant when a material state changes.

Thus:

**Domain State Changes**
→ **KCS Identifies Material Dependants**
→ **Affected Eligibility Recomputed**
→ **Civil Historical Access Updates**
→ **Civil Contact Notifies Participant**

---

# 11. Contestability

Where a participant disputes eligibility, the architecture should route the challenge to the actual disputed component.

Examples:

**Wrong education record**
→ Education/data correction.

**Wrong security assessment**
→ security review / appropriate independent review.

**Wrong participation state**
→ participation review.

**Wrong legal restriction**
→ administrative/judicial route.

**Correct inputs but disputed rule**
→ responsible authority / legal or constitutional review where applicable.

The participant should not have to diagnose the internal source before raising the problem.

> **Contest the Consequence; Concord Routes the Cause.**

---

# 12. Correction propagation

KCS Change Propagation supplies the dependency mechanism.

When an eligibility input is corrected:

1. preserve old state/provenance;
2. record correction;
3. identify materially dependent eligibility states;
4. recompute/review affected states;
5. propagate only where material consequences change;
6. notify participant;
7. preserve resulting provenance.

This prevents both:
- stale denial after correction;
- uncontrolled recalculation of unrelated systems.

---

# 13. Anti-capture boundary

A central eligibility authority would create a potentially powerful civil gatekeeper.

Distributed eligibility reduces that risk but does not eliminate it.

The shared interface must therefore not acquire hidden powers to:
- invent prerequisites;
- lower participation status;
- create security restrictions;
- revoke qualifications;
- decide citizenship;
- rank participants;
- alter domain rules;
- deny fundamental rights;
- convert technical inability into civil prohibition.

Its role is representation, composition, routing and recalculation under legitimate supplied authority.

> **Eligibility Interface != Eligibility Sovereign.**

---

# 14. Fundamental protection floor

The shared eligibility architecture must not represent fundamental protected standing as an optional benefit unlocked by participation.

Fundamental rights/protection-floor functions remain governed by the Rights architecture.

Where a system requires an eligibility check before providing something that is actually part of the protected minimum, that check itself requires scrutiny.

> **Fundamental Protection != Participation Reward.**

---

# 15. Relationship to Self-Stewardship

Self-Stewardship may supply contextual evidence for entrusted functions.

It does not supply a universal participant score.

The relevant domain identifies what stewardship evidence is genuinely material to the function.

A financial-fiduciary eligibility decision may use financial trust evidence.

An unrelated education service should not silently inherit that restriction without independent relevance.

---

# 16. Relationship to education

Education may supply:
- module completion;
- qualification;
- competence evidence;
- validity/expiry;
- equivalent qualification.

The receiving function decides which qualification is legitimately required.

Education should not decide who may hold unrelated civil authority merely because it records qualifications.

---

# 17. Relationship to citizenship and participation

Participation/citizenship may supply threshold conditions for some functions.

They should not substitute for competence.

Likewise competence should not automatically confer citizenship-specific authority.

Therefore:

**Participation Opens Eligibility Space**
+
**Qualification Establishes Readiness**
+
**Contextual Trust Establishes Relevant Reliability**
+
**Legitimate Domain Rules Establish Functional Permission**

where each is actually required.

---

# 18. No universal eligibility score

The architecture should resist reducing all eligibility to a single number.

A participant may be:
- eligible for one role;
- ineligible for another;
- awaiting qualification for a third;
- temporarily restricted in a fourth;
- fully entitled to a fundamental service;
- eligible but not allocated a scarce resource.

This multidimensional state is more faithful than a universal score.

---

# 19. Open questions

1. Does the shared eligibility interface require a dedicated technical service or can it be a protocol across existing systems?
2. Where are domain eligibility rules registered?
3. How are rule versions/provenance represented?
4. How does KCS know which eligibility outputs depend on which inputs?
5. How are jointly owned decisions represented?
6. Which eligibility states should be participant-visible?
7. How are security-sensitive inputs abstracted safely?
8. How are resource/allocation states separated from qualification?
9. What happens when two legitimate domain rules conflict?
10. How are emergency overrides represented and sunset?
11. How are eligibility rules audited for unnecessary barriers?
12. How are obsolete prerequisites removed?
13. How does automatic entitlement recognition distinguish entitlement from eligibility?
14. Which interface owns notification triggers?
15. How is the system implemented without creating a de facto central gatekeeper?

---

# 20. Source-resolution conclusion

The current Concord corpus supports a **distributed eligibility model** more strongly than a central eligibility authority.

The provisional architecture is:

**Legitimate Domains Own Functional Rules and Decisions**
+
**Historical Preserves State and Provenance**
+
**KCS Represents Material Dependencies and Propagates Change**
+
**Shared Eligibility Interface Composes Participant-Facing State**
+
**Civil Historical Access Exposes the State**
+
**Civil Contact Communicates Material Changes**
+
**Administrative/Judicial Architecture Provides Review**

This allows a coherent participant experience without creating a new universal authority.

> **Distributed Authority; Coherent Interface.**

> **Computation != Authority.**

> **Eligibility Interface != Eligibility Sovereign.**
