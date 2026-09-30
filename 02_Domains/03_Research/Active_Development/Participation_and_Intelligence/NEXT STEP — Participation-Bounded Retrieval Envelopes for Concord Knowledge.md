# NEXT STEP — Participation-Bounded Retrieval Envelopes for Concord Knowledge

**Project:** The Concord  
**Status:** NEXT MAJOR DEVELOPMENT STEP / HANDOFF NOTE / NOT CANONICAL  
**Date:** 30 September 2026  
**Development area:** Participation and Intelligence / Knowledge Access / Civil Information Architecture  
**Expected scale:** Major cross-domain development task; suitable for continuation by a fresh development instance

---

## 1. Why this is the next step

The Concord Lobby self-routing architecture has now reached the point where the next question is no longer simply whether a visitor can find the correct route.

The next question is:

> **What material should that participant actually be able to retrieve once the route enters the deeper Concord architecture?**

This exposes a civil-architecture problem rather than merely a documentation problem.

The Concord repository is principally organised according to:

- domain;
- system function;
- development state;
- provenance;
- and architectural ownership.

That structure should remain.

It answers:

> **Where does this knowledge belong?**

It does not by itself answer:

> **Which participant, role or process should be able to retrieve which parts of that knowledge, in which context, for which legitimate purpose?**

The next major development step is therefore to design the Concord's **participation-bounded knowledge retrieval architecture**.

---

## 2. Critical design decision — do not duplicate the corpus

The solution should **not** be to split the existing system files into separate copies for different participation levels.

For example, do not create:

- Governance — Public Version;
- Governance — Participant Version;
- Governance — Official Version;
- Governance — Specialist Version;
- Governance — Restricted Version;

where each file contains copied sections of the same underlying material.

That would create:

- duplication;
- version drift;
- inconsistent corrections;
- conflicting copies;
- increased maintenance;
- uncertainty over which copy is authoritative;
- and a growing risk that access-layer material becomes stale while the source architecture changes.

Instead:

> **The Concord should retain one authoritative knowledge object wherever practicable.**

Access should be controlled by a retrieval layer around that object.

Therefore:

> **One Source -> Multiple Bounded Retrieval Views**

not:

> **One Source -> Multiple Copied Documents**

---

## 3. Access envelope concept

Each relevant Concord knowledge object should be capable of having an **Access Envelope** associated with it.

The envelope does not replace the source file.

It describes what may be retrieved from that source under defined circumstances.

Conceptually:

**Authoritative Source File**  
-> **Access Envelope**  
-> **Participant / Role / Context Evaluation**  
-> **Permitted Retrieval Scope**  
-> **Retrieved Material**

The source remains singular.

The envelope controls exposure.

---

## 4. Example

Suppose a Governance source file contains:

- public constitutional principles;
- participant rights;
- ordinary civil procedures;
- internal administrative procedure;
- specialist implementation detail;
- security-sensitive dependencies;
- emergency operational mechanisms.

The file should not necessarily be broken into six separately maintained documents merely because different participants require different access.

Instead, its envelope might establish:

- public visitor -> retrieve sections A-B;
- ordinary participant -> retrieve A-D;
- authorised civil role -> retrieve A-F where functionally required;
- specialist operational role -> retrieve specified additional sections;
- emergency role in valid emergency context -> retrieve defined temporary material;
- unrelated participant -> no access to protected operational sections.

The retrieval system therefore asks, in effect:

> **Given this participant's current participation state, role, legitimate function and context, what material from this authoritative knowledge object may be retrieved?**

---

## 5. Participation level is an input, not the whole decision

A simple model such as:

**Level X -> all Level X documents**

is likely insufficient.

Participation level should be one major input, but access may also depend upon:

- role;
- legitimate function;
- subject of the information;
- relationship to the subject;
- current context;
- time;
- emergency state;
- qualification;
- delegated responsibility;
- privacy;
- security;
- purpose;
- risk;
- and applicable authority.

A provisional retrieval context is:

**RC = <Participant Level, Role, Function, Need, Subject, Relationship, Context, Time, Risk, Authority>**

The exact model remains to be developed.

Important invariants:

> **Higher Participation != Universal Access**

> **Role != Universal Clearance**

> **Information Access != Authority To Act**

> **Need To Know != Authority To Act**

> **Access To One Participant's Own Information != General Access To Equivalent Information About Others**

---

## 6. Retrieval envelope rather than copied representation

The access envelope should identify source ranges or semantic units rather than reproduce their contents wherever practicable.

Possible envelope rules may eventually refer to:

- headings;
- section identifiers;
- paragraphs;
- knowledge-object IDs;
- semantic blocks;
- tables;
- appendices;
- fields;
- linked objects;
- metadata;
- redacted representations;
- summaries generated from permitted source ranges;
- or combinations of these.

For example:

**Source:** Governance Canonical File  
**Public:** sections 1-4, 7.1, 9  
**Participant:** public + sections 5-8  
**Role R17:** participant + sections 10.2-10.7 while role/function active  
**Emergency context E3:** temporary access to section 12 subject to BCA/MNC conditions  
**Restricted:** section 13 unavailable except through defined process

The envelope stores the retrieval rule.

It does not store a second copy of sections 1-4.

---

## 7. Why this matters for AI evaluators

The current development work exposed a dangerous assumption:

> **If everything is visible, the evaluator will voluntarily use only what it is permitted to use.**

The Concord should not depend upon that assumption.

Humans, AI systems, institutions and automated processes may all make use of information once it has entered their accessible context.

Information can itself increase capability.

Therefore:

> **Information Exposure Is A Capability Dimension**

and:

> **Do Not Expose Consequential Information Merely Because The Recipient Has Been Told Not To Use It**

The system should retrieve the material appropriate to the legitimate context rather than expose the entire corpus and rely upon voluntary restraint.

---

## 8. Existing Concord architecture supporting this design

This direction should be developed by integrating existing architecture rather than inventing an unrelated access-control system.

### Minimum Necessary Capability

MNC already treats **information access** as a capability dimension.

The retrieval architecture should inherit:

**Purpose -> Function -> Need -> Minimum Sufficient Capability -> Bounded Exercise -> Review -> Termination or Re-Justification**

Applied to knowledge retrieval:

**Purpose -> Information Function -> Retrieval Need -> Minimum Sufficient Exposure -> Bounded Retrieval -> Review -> Expiry/Re-Justification**

### Contextual Wrapper Architecture

CWA already provides bounded contexts for:

- informational;
- digital;
- relational;
- functional;
- temporal;
- conceptual;
- and hybrid contexts.

An Access Envelope can therefore be treated as a knowledge-access implementation of bounded context architecture.

### Knowledge Control System

KCS already distinguishes **access/visibility state** from:

- epistemic state;
- retrieval/activity state;
- integrity;
- historical/version state;
- and capability-operational state.

Existing candidate access states include:

- OPEN;
- CONTROLLED;
- RESTRICTED;
- SEALED;
- REDACTED;
- EXPIRED;
- UNAVAILABLE-BY-POLICY.

KCS is therefore a natural substrate for representing the source object and its access metadata.

---

## 9. Retrieval should be positive, not merely prohibitive

The architecture should not only say:

> **You cannot see section X.**

It should answer:

> **What information does this participant legitimately need now?**

This allows the retrieval layer to actively supply the minimum sufficient information for the current function.

Conceptually:

**Participant / Process State**  
+ **Current Need**  
+ **Legitimate Function**  
+ **Source Access Envelope**  
= **Permitted Retrieval Set**

The participant then receives that set rather than the unrestricted source corpus.

---

## 10. Transparency and challenge safeguard

Access envelopes must not become a means of hiding civil power from participants.

A participant may legitimately be denied sensitive operational detail while still being entitled to know:

- that the relevant power exists;
- what its legitimate basis is;
- what its scope is;
- whether it has been used in relation to them;
- what consequences it can produce;
- what review mechanism exists;
- what evidence or reasoning may be challenged;
- what remedy exists;
- and how to challenge the decision or access restriction itself.

Therefore:

> **Bounded Information != Unaccountable Secrecy**

> **Transparency Of Power != Exposure Of Every Operational Detail**

> **Access Restriction Must Itself Be Reviewable Where Consequential**

---

## 11. Relationship to participation architecture

The retrieval architecture should eventually consume the Concord's participation-state architecture rather than recreate it.

Example:

**Evaluator currently represented as Participation Level X**  
-> requests Governance information for Function Y  
-> retrieval system resolves current context  
-> Governance Access Envelope is consulted  
-> permitted source sections are retrieved  
-> prohibited or unnecessary sections never enter evaluator context  
-> retrieved material retains source provenance and status  
-> further access requires a new justified retrieval decision.

The retrieval system should not infer a participant's level merely from what information they request.

> **Information Request != Participation Classification**

---

## 12. Dynamic access

Access need not be permanent.

A participant may legitimately gain access because:

- a role begins;
- a function is delegated;
- a case is assigned;
- consent is granted;
- an emergency occurs;
- a qualification is achieved;
- a participant is examining their own record.

Access may then contract when:

- the function ends;
- the case closes;
- consent is withdrawn where applicable;
- the emergency ends;
- the role terminates;
- a credential expires;
- the legitimate need disappears.

Therefore:

> **Access State Can Be Contextual And Time-Varying**

and:

> **Prior Access != Permanent Access**

This aligns with BCA and MNC sunset architecture.

---

## 13. Source changes and envelope integrity

Because the envelope points into a living authoritative source, source changes create an important integrity problem.

If:

- headings move;
- sections are added;
- content changes meaning;
- sensitive material is inserted into an existing permitted section;
- or a previously restricted distinction becomes public,

the envelope may become stale.

Therefore the architecture must eventually include:

**Source Change -> Envelope Impact Detection -> Review -> Revalidation**

An access envelope should record:

- source identity;
- source version or hash;
- envelope version;
- last review;
- applicable participation/context model;
- permitted semantic units;
- restricted semantic units;
- reasons/bases;
- review triggers.

This should integrate with KCS change propagation rather than becoming an independent duplicate mechanism.

---

## 14. Semantic access may be more important than file access

The long-term unit of access should probably not be the whole file.

A single file can contain material with several exposure classes.

Therefore:

> **File Access != Knowledge Access**

The eventual architecture may require stable semantic identifiers below file level.

For example:

**GOV-CANON-01 / Section 7 / Object 7.3**

could remain identifiable even if presentation formatting changes.

This is a development problem to investigate, not yet a fixed implementation requirement.

---

## 15. Retrieval output must preserve provenance

Material returned through an access envelope should retain enough metadata for the recipient to know:

- source;
- current represented status;
- whether material is canonical, provisional, historical, developmental or portable;
- whether the returned view is complete or bounded;
- whether material has been redacted or omitted;
- applicable date/version;
- and where challenge or further-access processes exist.

Therefore:

> **Bounded Retrieval Must Not Masquerade As Complete Source**

A recipient should not mistake:

**Everything I Was Permitted To Retrieve**

for:

**Everything That Exists**

This is an ESCP requirement as well as an access-control requirement.

---

## 16. Interaction with ESCP

Access control intentionally creates incomplete evaluation spaces.

That makes ESCP especially important.

A bounded participant should know, where legitimately possible:

> **Your present information view may be intentionally incomplete.**

But this must not disclose the protected information itself.

The system therefore needs to represent:

- known boundedness;
- unknown boundedness where disclosure itself is restricted;
- unavailable evidence;
- disputed access;
- and routes for requesting independent review.

Therefore:

> **Access-Bounded Evaluation Space != Complete Evaluation Space**

and:

> **Awareness Of Missing Information != Entitlement To Missing Information**

---

## 17. Major development programme

This is likely too large to complete reliably as an incidental continuation of the Lobby work.

It should be treated as the next major development programme.

A fresh development instance should:

### Phase 1 — Source resolution
Map all existing Concord architecture relevant to:

- participation levels;
- roles;
- authority;
- rights;
- privacy;
- information access;
- KCS;
- CWA;
- MNC;
- BCA;
- identity;
- Civil Contact;
- Historical records;
- Research;
- security;
- governance;
- health;
- judiciary;
- education;
- economy;
- continuity.

### Phase 2 — Exposure taxonomy
Determine what kinds of Concord information require:

- open access;
- participant access;
- role/function access;
- specialist access;
- restricted access;
- sealed access;
- subject-specific access;
- temporary/contextual access.

Do not assume these categories are final.

### Phase 3 — Participation integration
Resolve exactly how existing participation levels interact with:

- roles;
- qualifications;
- rights;
- responsibilities;
- self-access;
- delegation;
- emergency contexts;
- and sunset.

### Phase 4 — Access Envelope specification
Define the envelope schema.

The schema should reference source material rather than duplicate it.

### Phase 5 — Corpus mapping
Work systematically through the living Concord corpus and determine the appropriate access envelope for relevant material.

This is expected to be a substantial task.

### Phase 6 — Retrieval architecture
Define how a retrieval process receives participant/context state and returns only the permitted source material.

### Phase 7 — Change propagation
Ensure source modifications trigger envelope review where necessary.

### Phase 8 — Audit and adversarial testing
Test for:

- overexposure;
- underexposure;
- privilege escalation;
- stale envelopes;
- inference leakage;
- identity leakage;
- role accumulation;
- emergency persistence;
- access without authority;
- authority without necessary information;
- inability to challenge;
- misleading bounded views;
- cross-document reconstruction of restricted information.

### Phase 9 — Lobby-to-Architecture testing
Only after the access architecture exists should the Lobby-to-Architecture blind tests resume.

Then the test becomes realistic:

> **Given this participant state and this route, does the retrieval system expose the right material, preserve the right boundaries and provide enough information for the next legitimate decision?**

---

## 18. Do not restructure the authoritative corpus prematurely

During this development programme:

> **Do not split source files merely to implement access levels.**

Where a source file is badly structured for semantic retrieval, record the problem.

Structural refactoring may later be justified for maintainability or stable semantic addressing, but access-control design alone should not create duplicate source material.

The default should remain:

> **One Authoritative Source + Access Envelope**

---

## 19. Provisional architecture

A first conceptual model is:

**Participant State**  
+ **Role / Function**  
+ **Request / Need**  
+ **Context**  
+ **Source Knowledge Object**  
+ **Access Envelope**  
+ **MNC / CWA / KCS / BCA Constraints**  
= **Bounded Retrieval View**

Then:

**Bounded Retrieval View**  
-> **Use**  
-> **Further Need?**  
-> if yes: new bounded retrieval decision  
-> if no: terminate  
-> if disputed: review/challenge route

---

## 20. Candidate name

Provisional working name:

# **Concord Access Envelope and Bounded Retrieval Architecture**

Possible functional primitive:

**Minimum Sufficient Knowledge Exposure (MSKE)**

These names are provisional.

Do not graduate or extract a portable module until the architecture has been source-resolved, developed and tested.

Flag as a future PMEDG candidate only.

---

## 21. Core invariants to preserve

> **One Authoritative Source -> Multiple Bounded Retrieval Views**

> **Domain Classification != Exposure Classification**

> **File Access != Knowledge Access**

> **Available To Read != Legitimately Necessary To Expose**

> **Information Access != Authority To Act**

> **Need To Know != Authority To Act**

> **Higher Participation != Universal Access**

> **Role != Universal Clearance**

> **Prior Access != Permanent Access**

> **Bounded Information != Unaccountable Secrecy**

> **Transparency Of Power != Exposure Of Every Operational Detail**

> **Bounded Retrieval Must Not Masquerade As Complete Source**

> **Access-Bounded Evaluation Space != Complete Evaluation Space**

> **Awareness Of Missing Information != Entitlement To Missing Information**

> **Information Request != Participation Classification**

---

## 22. Handoff instruction

The next development instance should begin here.

Do **not** begin by rewriting or reorganising the corpus.

Begin by source-resolving the existing participation, information-access, privacy, role, authority and knowledge-control architecture.

Then define the Access Envelope model.

Only after the model is sufficiently stable should the living corpus be systematically mapped.

The intended end state is a Concord in which a participant or evaluator does not receive an unrestricted repository and an instruction to exercise restraint.

Instead:

> **The retrieval system knows the participant's represented access context, consults the relevant source envelopes, and retrieves only the material legitimately required for the current function while preserving provenance, transparency, challenge rights and awareness of boundedness.**

This is the next major architectural development required before realistic Lobby-to-Architecture testing can continue.
