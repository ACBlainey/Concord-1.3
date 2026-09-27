# Contextual Wrapper Architecture — A Portable Architecture for Bounded Contexts

**Module:** Contextual Wrapper Architecture (CWA)  
**Development level:** Level B — Extractable Architecture  
**Status:** GRADUATED PORTABLE MODULE / SPECIFICATION-LEVEL TRANSFER VALIDATED  
**Version:** 1.0  
**Date:** September 2026  
**Project origin:** The Concord  
**Author:** Alexander C. Blainey

---

## 1. Purpose

Contextual Wrapper Architecture is a portable interface architecture for bounded contexts in which materially relevant conditions differ from the surrounding or default context.

Its purpose is not to make different environments uniform.

Its purpose is to make material difference sufficiently **legible, bounded, attributable, reviewable and terminable** that participants and affected parties can understand which context applies, what changes within it, what does not change, which permissions and restrictions exist, who holds contextual authority and responsibility, how emergency/remedy/exit operate, and when the contextual variation ends.

The compact design principle is:

> **Standardise the interface; preserve legitimate contextual variation.**

A related source formulation is:

> **Standardise the interface more strongly than the outcome.**

This specification extracts the contextual-wrapper mechanism from the Concord. It does not require adoption of Concord institutions, constitutional structures or domain-specific rules.

---

## 2. Developmental status and epistemic boundary

This is the **v1.0 graduated portable specification**.

It defines a source-resolved portable architecture that has completed adversarial and cross-domain blind-transfer testing. Graduation establishes portability at specification level; it does **not** establish that the architecture is universal, complete or empirically validated.

The source architecture itself remains under development. In particular, nested and overlapping contexts require precedence handling, but the source corpus does not yet establish a universally validated precedence algorithm.

Therefore this specification MUST preserve unresolved precedence as:

- **UNKNOWN**;
- **DISPUTED**; or
- **REQUIRES EXTERNAL RESOLUTION**

where the applicable wider framework does not already supply a legitimate answer.

The module MUST NOT manufacture a precedence hierarchy merely to complete an analysis.

---

## 3. Problem class

The module addresses the recurring problem:

> **How can a bounded environment operate under materially different conditions from its surroundings while remaining intelligible, responsible and connected to the wider system?**

The problem occurs in very different domains, including:

- sports and hazardous activities;
- laboratories and research environments;
- workplaces;
- medical environments;
- private or restricted spaces;
- digital environments;
- temporary events;
- special jurisdictions;
- local governance;
- transport/transit environments;
- institutional environments;
- civilisational boundaries.

The substantive rules in these domains may have little in common.

The reusable element is the **interface grammar by which material contextual difference is identified, communicated, bounded and terminated**.

---

## 4. Scope

### 4.1 Universal primitive — bounded context

The universal primitive in CWA is the **bounded context**, not any particular kind of physical or digital space.

> **A bounded context is any distinguishable context in which some combination of access, rules, permissions, restrictions, roles, protections, responsibilities, authority, risks or expectations differs materially from another context.**

The boundary may be spatial, logical, informational, relational, functional, temporal, conceptual or composed from several of these.

CWA is therefore **substrate-neutral**. Its grammar is intended to remain usable when the implementation of the context changes.

> **The substrate or medium of a boundary may change; the contextual questions remain substantially invariant.**

### 4.2 Illustrative implementation classes

The following categories are illustrative rather than exhaustive.

#### Physical contexts

Examples include:

- a home;
- bedroom;
- toilet or washroom;
- laboratory;
- graded biological-containment area;
- hospital ward;
- sports arena;
- staff-only room;
- vehicle;
- private office;
- secure facility.

A physical boundary may be represented by walls, doors, gates, distance, controlled zones, signage or other spatial mechanisms.

#### Digital contexts

Examples include:

- private server;
- directory or file tree;
- database;
- chat or communication channel;
- virtual room;
- restricted network;
- administrative domain;
- AI or agent workspace;
- access-controlled service;
- virtual environment.

A digital boundary may be represented through authentication, identity, credentials, permissions, encryption, network segmentation, capability tokens or executable policy.

#### Informational contexts

Examples include:

- classified or restricted datasets;
- medical records;
- confidential documents;
- protected memory stores;
- privileged communications;
- research data under restricted handling.

The information itself may cross physical or digital locations while remaining inside a defined handling context.

#### Computational contexts

Examples include:

- sandboxed execution;
- privileged processes;
- restricted compute environments;
- isolated model or agent execution;
- capability-limited runtime environments;
- protected system-control contexts.

#### Social and relational contexts

Examples include:

- confidential meetings;
- professional relationships;
- household relationships;
- membership contexts;
- private conversations;
- role-defined groups.

Their boundaries may depend more strongly on recognised relationships, roles, cultural expectations and explicit participant rules than on physical barriers.

#### Functional and activity contexts

Examples include:

- a boxing match;
- medical procedure;
- research experiment;
- examination;
- maintenance operation;
- emergency response activity;
- controlled training exercise.

The context may activate because an activity begins rather than because a participant crosses a physical threshold.

#### Temporal contexts

Examples include:

- emergency periods;
- scheduled restricted periods;
- temporary events;
- maintenance windows;
- time-limited permissions;
- temporary delegations of authority.

The same location or system may therefore operate under different contextual rules at different times.

#### Conceptual contexts

Examples include:

- a formally bounded decision process;
- deliberative context;
- confidential reasoning environment;
- defined research space;
- review or adjudication process;
- hypothetical or simulation environment whose outputs are deliberately separated from operational authority.

Conceptual contexts demonstrate that a boundary need not correspond to physical containment or computer access. It may instead distinguish a defined mode of participation, reasoning, authority or information handling.

#### Hybrid contexts

Many real contexts combine several forms.

Examples include:

- a laboratory requiring physical clearance, role authorisation and digital-system access;
- a hospital combining physical spaces, medical-record permissions, professional roles and emergency states;
- an AI-controlled facility combining digital identity, physical location, computational permissions and function-specific authority;
- a remote research collaboration combining confidential information, digital workspaces, participant roles and time-limited permissions.

### 4.3 Categories are not limits

> **These categories describe implementations, not limits.**

A bounded context need not fit exclusively within one category. The same context may be physical, digital, informational and relational simultaneously.

CWA MUST NOT treat the present list as a closed ontology. Unfamiliar future contexts remain within scope where the contextual grammar applies.

The test is therefore not:

> *Does this look like one of the examples?*

The test is:

> **Can a meaningful contextual boundary be identified, and do materially relevant conditions differ across or within it?**

### 4.4 Substrate-neutral grammar

Across these implementations, CWA asks substantially the same questions:

**Context**  
→ **Boundary / Activation**  
→ **Reachability**  
→ **Access**  
→ **Participant / Role**  
→ **Applicable Rules**  
→ **Relationship / Inheritance**  
→ **Permissions / Restrictions / Protections**  
→ **Responsibility / Authority**  
→ **Interaction / Externalities**  
→ **Remedy / Emergency**  
→ **Exit / Termination**  
→ **Reversion / Transition**  
→ **Review**

The implementation of each element may vary substantially.

A door may implement a physical boundary. Authentication may implement a digital boundary. Confidentiality may define an informational boundary. The start of a medical procedure may activate a functional context. A declared emergency period may activate a temporal context. A formal deliberation may activate a conceptual context.

These mechanisms are not equivalent in implementation. They are comparable because they answer related contextual questions.

This gives CWA a core invariant:

> **Boundary ≠ Access ≠ Rules ≠ Authority**

and a broader substrate-neutral principle:

> **Different substrates may require different boundary mechanisms without requiring different contextual grammar.**

### 4.5 Material activation

CWA applies where a context materially changes one or more of:

- rules;
- rights or protections;
- responsibilities;
- permissions;
- restrictions;
- risks;
- roles;
- authority;
- privacy or data conditions;
- behavioural expectations;
- remedy;
- withdrawal or exit;
- exposure to external consequences.

A full wrapper is not required for every trivial difference.

Wrapper depth and information burden SHOULD scale with:

1. materiality of the change;
2. consequence of misunderstanding;
3. risk;
4. reversibility;
5. authority exercised;
6. vulnerability or dependency of affected parties;
7. difficulty of exit;
8. external effects.

> **Information burden should be proportionate to material contextual difference and risk.**

---

## 5. Non-goals

CWA does not:

- generate substantive domain rules;
- prove that a contextual rule is legitimate;
- convert clear communication into legitimacy;
- convert presence into consent;
- convert consent into unlimited permission;
- create political sovereignty;
- grant authority merely because a context exists;
- eliminate the need for domain expertise;
- determine universal precedence between all possible contexts;
- eliminate externalities;
- prove that declared conditions match reality;
- require uniform substantive outcomes.

> **Common grammar ≠ elimination of domain-specific rules.**

---

## 6. Core distinctions

The following distinctions are normative invariants of this specification.

### 6.1 Context is not merely place

> **Physical Boundary ≠ Complete Contextual Boundary**

A context may be physical, digital, temporal, activity-defined, role-defined, relationship-defined or composite.

### 6.2 Permission is contextual

> **Contextual Permission ≠ General Permission**

Permission valid in one context does not automatically survive outside it.

### 6.3 Presence does not equal role

> **Presence in Context ≠ Possession of Every Contextual Permission**

Several participants can occupy the same context while holding different roles, permissions and responsibilities.

### 6.4 Shared context does not equal shared consent

> **Shared Context ≠ Shared Consent**

Consent and exposure may differ by participant and role.

### 6.5 Context does not create sovereignty

> **Bounded Context ≠ Sovereign Jurisdiction**

> **Contextual Authority ≠ Political Sovereignty**

### 6.6 Boundary does not contain consequence

> **Contextual Boundary ≠ Externality Boundary**

Effects may cross the wrapper even where rules do not.

### 6.7 Formal exit may not be meaningful exit

> **Formal Exit ≠ Meaningful Exit**

Dependency, custody, employment, residence, infrastructure, coercion, cost or practical impossibility may make nominal exit insufficient.

### 6.8 Declaration is not reality

> **Declared Context ≠ Observed Reality**

A wrapper describes conditions. It does not make those conditions true by declaration.

### 6.9 Legibility is not legitimacy

> **Legibility ≠ Legitimacy**

A perfectly communicated rule may still be impermissible under the applicable wider framework.

### 6.10 Legitimacy is not consent

A rule may have a legitimate basis without individual consent, and consent may be required for some legitimate variations. The two questions must not be collapsed.

### 6.11 Consent is not precedence

Agreement to one context does not determine which rule prevails when another legitimate context overlaps it.

> **Legibility ≠ Legitimacy ≠ Consent ≠ Precedence**

### 6.12 Nesting is not automatic rule inheritance

> **Nested Context ≠ Inherited Rule Set**

A context physically or logically contained inside another context may possess its own function-specific rules. The enclosing context does not automatically determine the internal rules of the nested context.

The enclosing context may control whether a participant can reach the nested context, while the nested context separately controls whether that participant may enter or use it and which rules apply once activated.

Therefore three questions MUST be separable:

1. May the participant access the enclosing context?
2. Does that access grant access to the nested context?
3. If the nested context is legitimately activated, which local rules apply inside it?

> **Parent Access ≠ Child Access**

and:

> **Parent Rules ≠ Child Rules**

A private home containing a toilet illustrates the distinction. Permission to enter the home may make the toilet physically reachable without making every toilet or every associated private room available to the visitor. An ensuite attached to a bedroom may require access to the bedroom, specific permission, or another household rule. Conversely, a toilet intended for public use inside a public building may be available to the general public, while a staff toilet in the same building remains role-restricted.

The characteristic protected-space rules of a toilet may remain broadly similar across a home, office or public building even though access conditions differ.

### 6.13 Reachability, access and local operation are distinct

CWA SHOULD distinguish:

**Reachability** — can the participant physically or logically arrive at the nested boundary?

**Access entitlement** — is the participant permitted to cross or activate that boundary?

**Local operation** — which rules, permissions, restrictions and protections apply once inside?

A parent context can enable reachability without conferring access entitlement.

### 6.14 Boundary legibility is context-sensitive

> **Boundary Legibility ≠ Identical Boundary Signalling**

Public and commercial contexts can reasonably rely heavily on signs, labels, access controls and other explicit designations where these are culturally and operationally intelligible.

Private domestic contexts need not formalise every internal boundary through signage. Legibility may instead arise from established cultural practice, functional cues, relationships, and explicit rules or permissions stated by the legitimate owner/occupier.

The required question is not whether every boundary uses the same signalling mechanism, but whether a reasonable participant can identify the relevant boundary and applicable access conditions with sufficient reliability for the context.

### 6.15 Relational access

Access to one context may depend on a relationship to another context without inheriting that context's complete rule set.

For example:

**House Access**  
≠ **Bedroom Access**  
≠ **Ensuite Access**

Yet access to a bedroom may, under the relevant household rules, carry an associated permission to use its ensuite.

CWA therefore permits explicit contextual relationships such as:

- contains;
- reachable-through;
- associated-with;
- access-dependent-on;
- role-restricted;
- permission-dependent;
- temporarily delegated.

These relationships describe access structure. They do not automatically establish legitimacy or universal precedence.

### 6.16 Nested rule relationships are explicit, not universally independent or inherited

The non-inheritance rule prevents accidental inheritance. It does **not** prohibit deliberate inheritance.

Nested contexts may use different relationship models, including:

- **Independent** — child rules are locally defined and parent rules do not automatically transfer;
- **Additive inheritance** — child inherits applicable parent rules and adds stricter or additional requirements;
- **Selective inheritance** — only identified parent rules transfer;
- **Override** — an identified child rule replaces an identified parent rule within the child context;
- **Composite** — several rule sources remain simultaneously applicable;
- **Unknown / disputed** — the relationship has not been resolved.

Therefore the more precise principle is:

> **Nesting Alone Does Not Determine Rule Inheritance.**

Inheritance must arise from an established contextual relationship, not merely from containment.

### 6.17 Monotonic protection / clearance chains

Some nested systems intentionally form cumulative protection levels.

A biological laboratory may be structured conceptually as:

**Level 1 Rules**  
→ **Level 2 = Level 1 + Additional Level 2 Controls**  
→ **Level 3 = Levels 1–2 + Additional Level 3 Controls**  
→ **Level 4 = Levels 1–3 + Additional Level 4 Controls**

In such a system the inheritance relationship is part of the architecture. A participant authorised for Level 4 may also be authorised for Levels 1–3 **where the access system explicitly defines higher clearance as including lower clearance**.

This must not be generalised to unrelated nested contexts. A person's permission to enter a highly restricted room in one system does not logically imply access to every less-restricted or sibling space unless the permission model establishes that relation.

CWA SHOULD therefore represent both:

- **rule inheritance direction**; and
- **access/clearance implication direction**.

These are related but not identical.

### 6.18 Digital and hybrid contextual spaces

Safe/protected spaces and nested contexts are substrate-independent.

A context may be:

- physical;
- digital;
- informational;
- computational;
- network-defined;
- role-defined;
- temporal;
- or hybrid physical/digital.

Digital examples may include nested directories, data rooms, execution environments, administrative domains, communication spaces, permission zones, virtual environments, agent workspaces and protected memory/data contexts.

The same questions apply:

- What is the boundary?
- What makes it reachable?
- Who may access it?
- Does access inherit?
- Do rules inherit?
- Which local rules are added or overridden?
- Which role or clearance is required?
- What information may cross the boundary?
- What happens when access terminates?

A physical context may also activate a digital context, and vice versa. CWA must therefore avoid assuming that nested-space topology is purely geographical.

---



## 7. Portable primitive

Where a participant enters, occupies or acts within a bounded context whose material rules, permissions, restrictions, risks, roles, responsibilities or authority differ from the surrounding/default context, the system SHOULD:

1. identify the context;
2. identify its activation/boundary;
3. identify affected participants and roles;
4. identify the applicable wider framework;
5. identify material variation;
6. make relevant variation legible;
7. provide proportionate warning where necessary;
8. establish consent or another legitimate basis where required;
9. bound contextual permissions and restrictions;
10. bound contextual authority and responsibility;
11. identify effects on nonparticipants;
12. expose externalities;
13. define emergency and remedy relationships;
14. expose withdrawal/exit conditions where applicable;
15. define context termination;
16. revert temporary conditions when the context ends;
17. preserve unresolved matters explicitly;
18. review declarations against evidence.

---

## 8. Core operational grammar

The candidate portable sequence is:

**Identify Context**  
→ **Identify Boundary / Activation**  
→ **Identify Participant / Role**  
→ **Identify Applicable Wider Framework**  
→ **Identify Material Variation**  
→ **Identify Protected / Unchanged Conditions**  
→ **Communicate Material Variation**  
→ **Warn Where Necessary**  
→ **Establish Legitimate Basis / Consent Where Required**  
→ **Activate Contextual Permissions / Restrictions**  
→ **Identify Responsibility and Contextual Authority**  
→ **Operate Within Context**  
→ **Track Externalities / Nonparticipant Effects**  
→ **Provide Emergency / Remedy Interface**  
→ **Permit Withdrawal / Exit Where Applicable**  
→ **Terminate Context**  
→ **Revert to Surrounding / Default Norms**  
→ **Record / Review Where Necessary**

This sequence is a grammar, not an assertion that every implementation must expose each step in the same user-interface order.

---

## 9. Required inputs

A CWA analysis SHOULD seek the following inputs.

### 9.1 Context identity

- What context exists?
- What function or activity defines it?
- Is it physical, digital, temporal, role-based, activity-based or composite?

### 9.2 Surrounding/default context

- What conditions would otherwise apply?
- Which rules and protections continue through the contextual boundary?

### 9.3 Boundary / activation

- What activates the context?
- How is entry, participation or activation recognised?
- When does it begin?
- Is the boundary visible to all materially affected parties?

### 9.4 Participants and roles

Identify, where relevant:

- participants;
- role-holders;
- operators;
- observers;
- adjacent nonparticipants;
- third parties affected by externalities;
- automated or artificial agents.

### 9.5 Applicable wider framework

Identify the external normative, legal, contractual, organisational or other legitimate framework within which the context operates.

The wrapper MUST NOT assume that its own declaration is the highest authority.

### 9.6 Material variations

Identify what changes in:

- rules;
- protections;
- permissions;
- restrictions;
- risks;
- responsibilities;
- authority;
- privacy/data;
- remedy;
- exit;
- expected behaviour.

### 9.7 Protected invariants

Identify what does **not** change merely because the context exists.

### 9.8 Legitimate basis

Identify the claimed basis for each material variation.

Possible bases may include law, valid delegated authority, contract, informed voluntary participation, safety function, organisational rule or another externally legitimate basis.

CWA records and tests the claimed basis; it does not manufacture legitimacy.

### 9.9 Authority and responsibility

Identify:

- authority holder;
- function;
- scope;
- affected persons/things;
- activation;
- termination;
- review/remedy;
- responsible party.

### 9.10 Emergency arrangements

Identify whether another context or authority may activate during emergency and what happens to ordinary contextual rules.

### 9.11 Exit / withdrawal

Identify:

- whether withdrawal applies;
- how it occurs;
- practical constraints;
- consequences;
- assistance/remedy;
- whether exit is meaningful.

### 9.12 Externalities

Identify material effects crossing the contextual boundary.

### 9.13 Nested and overlapping contexts

Identify other simultaneously applicable contexts and known conflict/priority rules.

For nested contexts also identify:

- whether parent access only creates reachability or also grants child access;
- the child's independent access condition;
- the child's local/function-specific rules;
- relevant relationships between parent, child and sibling contexts;
- the mechanism by which the child boundary is made legible.

---

## 10. Unknown and disputed data

CWA MUST distinguish absence of information from absence of a condition.

Where a required matter cannot be resolved, use an explicit state such as:

- **KNOWN**;
- **UNKNOWN**;
- **DISPUTED**;
- **NOT APPLICABLE**;
- **REQUIRES EXTERNAL RESOLUTION**.

The module MUST NOT convert missing information into a convenient default.

In particular:

> **No precedence rule found ≠ no precedence problem exists.**

---

## 11. Participant-facing legibility test

Where materially relevant, a participant should be able to determine:

1. What context am I in or entering?
2. What activates it?
3. What changes here?
4. What remains protected or unchanged?
5. What role do I hold?
6. What permissions do I gain?
7. What restrictions apply?
8. What risks materially change?
9. Who has authority here?
10. What authority do they actually possess?
11. Who is responsible?
12. Is my consent required, and if so for what?
13. What happens in an emergency?
14. How do I seek remedy?
15. Can I withdraw or leave?
16. What happens when the context ends?
17. Are other contexts simultaneously applicable?
18. Are any important matters unknown or disputed?

A wrapper that technically contains this information but makes it practically inaccessible may fail the legibility requirement.

---

## 12. Consent and informed participation

For materially voluntary contextual change, the candidate participation chain is:

**Approach / Activation**  
→ **Recognise Context**  
→ **Receive Material Information**  
→ **Understand Material Variation**  
→ **Receive Proportionate Warning Where Required**  
→ **Identify Available Options**  
→ **Choose**  
→ **Enter / Participate or Decline / Avoid**

However:

> **Consent activates permissible variation; consent does not manufacture legitimacy for impermissible variation.**

Therefore:

> **Clear Signage ≠ Legitimate Rule**

and:

> **Entry ≠ Waiver of Fundamental Rights**

Where participation is not genuinely voluntary, the wrapper MUST NOT represent mere presence or compliance as voluntary consent.

---

## 12A. Functional permission and minimum necessary permission

A legitimate function does not automatically require authority.

Many ordinary interactions can be performed through bounded permission rather than control over another participant, space, resource or system.

The source architecture therefore distinguishes:

> **Functional Permission ≠ Contextual Authority**

> **Permission to Enter ≠ Permission to Use**

> **Permission for One Function ≠ Permission for Unrelated Functions**

> **Permission to Use ≠ Authority to Control**

> **Capability to Enter ≠ Permission to Enter**

> **Physical Access ≠ Legitimate Access**

### 12A.1 Function-derived permission

A participant may possess a limited permission because a legitimate function reasonably requires a particular interaction with a space, resource, participant, information context or capability.

The portable chain is:

**Legitimate Function**  
→ **Genuine Functional Need**  
→ **Reasonably Necessary Interaction**  
→ **Minimum Necessary Permission**  
→ **Function-Bounded Activity**  
→ **Function Completion / Other Basis Ends**  
→ **Permission Terminates**

A claimed function does not legitimate itself merely because access would make that function easier.

### 12A.2 Minimum necessary permission

> **Where access or activity is justified by a particular function, the resulting permission should normally extend only as far as reasonably necessary to perform that legitimate function.**

Permission may therefore be narrower than physical capability and narrower than general access to the surrounding context.

For ordinary civil access:

**Legitimate Function → Required Interaction → Need for Permission → Minimum Necessary Permission → Bounded Contextual Access**

This is structurally parallel to, but distinct from:

**Legitimate Objective → Required Function → Need for Authority → Minimum Necessary Authority → Bounded Contextual Authority**

### 12A.3 Permission-before-authority gate

Before CWA represents a need for authority, it SHOULD ask:

1. What legitimate function is being performed?
2. What interaction is genuinely required?
3. Can the function be performed through ordinary public access, voluntary interaction or consent?
4. Is explicit permission already present?
5. Is a bounded implied/function-derived permission reasonably established?
6. What is the minimum permission reasonably necessary?
7. Does the function actually require authority beyond permission?

The default routing principle is:

**Function**  
→ **Ordinary / Explicit / Implied / Relationship / Contractual / Emergency Permission Sufficient?**  
→ if **YES: Minimum Necessary Permission**  
→ if **NO: Test Whether Authority Is Genuinely Required**

> **Legitimate Function ≠ Special Authority Required**

CWA MUST NOT manufacture authority where bounded permission is sufficient.

### 12A.4 Implied permission

Ordinary civil interaction cannot depend upon explicit negotiation for every routine action.

Where a function is ordinary, legitimate, reasonably expected and requires limited interaction to perform, bounded contextual permission MAY be implied unless:

- it has been explicitly restricted;
- the participant has relevant notice to the contrary;
- conflicting rights or protections apply;
- applicable law or rules require a different basis;
- the proposed interaction exceeds what the function reasonably requires.

> **Implied Permission Should Be Function-Bounded.**

> **Function Completion Should Normally Terminate Function-Derived Permission.**

### 12A.5 Permission is action-specific

CWA SHOULD NOT treat “access” as one indivisible permission.

Where material, a contextual permission relationship may distinguish:

**Approach | Traverse | Enter | Remain | Observe | Interact | Use | Inspect | Record | Modify | Remove | Exclude | Authorise**

Additional domain-specific actions may be added.

Possession of one permission does not imply possession of another.

> **Access ≠ Single Permission**

A permitted destination does not necessarily create permission to use every route to it.

A permitted route for one function does not create a general right of passage.

### 12A.6 Permission claim

Where greater precision is needed, CWA MAY represent permission as:

> **Participant P may perform Action A in Context/Space S for Function F under Conditions C during Time T on Legitimate Basis B.**

This prevents a narrow permission from silently becoming a general entitlement.

### 12A.7 Permission provenance

Where material, distinguish the basis of permission:

- legal requirement;
- owner/steward rule;
- explicit consent;
- contractual condition;
- relationship permission;
- cultural convention;
- contextual inference / implied permission;
- responsibility-derived access;
- emergency necessity;
- another established legitimate basis.

> **Rule Content ≠ Rule Source**

Similar physical actions may therefore have different permission bases, termination conditions and remedy paths.

### 12A.8 Reasonableness and anti-self-justification

“Need” is not a magic word.

The proposed interaction must bear a reasonable relationship to a legitimate function and remain proportionate to what that function requires.

For example, a delivery function may reasonably support approaching, traversing or briefly stopping on a private driveway where that is ordinarily necessary to perform the delivery. It does not thereby support unrelated occupation, storage, exclusion of the owner or control of the driveway.

Likewise, an actor's own commercial function cannot manufacture permission to use an unrelated participant's private resource merely because doing so would be convenient.

> **A function may explain why access is desired without establishing a legitimate basis for that access.**

### 12A.9 Permission termination and abuse boundary

Where permission derives from a particular function:

**Function Completed / Abandoned / Legitimate Basis Ends**  
→ **Function-Derived Permission Normally Terminates**

Continued activity must then rely on another legitimate permission basis or be represented as lacking the expired basis.

CWA SHOULD distinguish:

**No Valid Permission Basis Ever Existed**

from:

**Valid Permission Existed → Basis Ended → Continued Activity Lacks That Permission Basis**

CWA identifies the contextual state. It does not invent the applicable legal remedy.

### 12A.10 Relationship to private and nested spaces

Private classification does not imply zero legitimate interaction, and physical accessibility does not imply permission.

A private space may simultaneously support different permission relationships for different participants and functions.

> **Spatial Classification ≠ Access Classification**

> **Open Boundary ≠ Granted Permission**

> **Parent Access ≠ Child Access**

This allows ordinary low-friction interaction while preserving protection against permission creep.

---

## 13. Contextual authority

Where local authority is necessary, CWA uses the following bounded pattern:

**Contextual Function / Problem**  
→ **Need for Local Authority**  
→ **Minimum Necessary Authority**  
→ **Role-Bounded Authority**  
→ **Context-Bounded Authority**  
→ **Authority Terminates When Its Justifying Function / Context Ends**

At minimum the wrapper records:

- who holds authority;
- the function that justifies it;
- its scope;
- who/what it applies to;
- activation conditions;
- termination conditions;
- accountability/remedy interface.

> **Contextual authority should not escape its context without independent justification.**

CWA may interface with a more detailed authority-bounding architecture, but does not require one specific authority framework to remain portable.

---

## 14. Temporal boundary and reversion

A material context SHOULD define start and end conditions where reasonably possible.

At termination:

- temporary permissions SHOULD terminate;
- temporary restrictions SHOULD terminate where their basis ends;
- temporary contextual authority SHOULD terminate unless independently justified;
- surrounding/default conditions SHOULD resume;
- continuing obligations SHOULD be explicitly identified rather than silently retained.

This is a primary anti-creep mechanism.

---

## 14A. Termination, reversion and residual state

Context termination is not complete merely because a boundary closes or an activity stops.

The source architecture establishes:

> **Context start and context end should be legible where material.**

> **Temporary need should normally produce temporary capability.**

> **Function completion should normally terminate function-derived capability.**

CWA SHOULD therefore distinguish termination of the originating context from termination or persistence of consequences created within it.

At context end, inspect where relevant:

- active permissions;
- delegated capabilities;
- credentials/tokens;
- temporary authority;
- ongoing autonomous processes;
- retained or derived information;
- copied information;
- external-service artefacts or dependencies;
- physical or digital access-control state;
- unresolved responsibilities/remedies.

A continuing artefact is not automatically illegitimate merely because its originating context ended. Its continued existence or operation requires an applicable basis where one is materially required.

CWA SHOULD represent revocation/termination propagation explicitly rather than assuming that ending the parent context automatically revokes every downstream capability or deletes every derivative.

## 15. Nested contexts

Contexts may nest:

**Wider System → Facility → Restricted Area → Activity → Special Event**

Physical or logical containment MUST NOT be treated as automatic rule inheritance.

For each nested layer identify:

- activation;
- applicable participants/roles;
- parent-context reachability;
- independent access condition;
- local/function-specific rules;
- inheritance model: independent / additive / selective / override / composite / unknown;
- any rules explicitly inherited from the parent;
- rules added by the child;
- rules explicitly overridden by the child;
- access/clearance implication relationships;
- additional rules;
- overridden defaults;
- protected invariants;
- contextual relationships;
- authority;
- known precedence/conflict rules.

The default analytical assumption is therefore **no inferred inheritance unless a rule relationship is established**. Once an explicit relationship is established, the child may be independent, additive, selectively inheriting, overriding or composite.

A useful access chain is:

**Parent Context Access**  
→ **Child Boundary Becomes Reachable**  
→ **Child Access Condition Evaluated**  
→ **Child Context Activated if Permitted**  
→ **Child Local Rules Apply**

This allows, for example, a public building to contain both a public toilet and a staff-only toilet without contradiction. It also allows a private home to contain spaces with different access expectations without requiring formal signage on every internal boundary.

It equally permits deliberately cumulative structures such as graded laboratory containment, where each deeper level inherits defined protections from the preceding level and adds further controls.

No universal assumption may be made that the smallest, newest, most specific, most local or most restrictive context automatically prevails.

If precedence is not legitimately supplied:

> **PRECEDENCE: UNKNOWN / DISPUTED / REQUIRES EXTERNAL RESOLUTION**

---

## 16. Overlapping contexts

Contexts may overlap without nesting.

Example:

**Sporting Context + Medical Emergency Context → Composite State**

The module should:

1. detect simultaneous applicability;
2. identify conflicts;
3. identify any legitimate conflict/priority rule;
4. preserve unresolved conflict where none exists;
5. avoid silently selecting a winner;
6. expose operational consequences of unresolved precedence.

> **Wrapper composition requires explicit conflict and priority handling.**

CWA v1.0 does not claim a universal composition algorithm.

### 16.1 External resolution interface

Detecting a conflict does not create authority to resolve it.

> **Information architecture ≠ decision authority.**

> **Schema authority ≠ sovereignty.**

Where a conflict requires resolution beyond the wrapper:

**Conflict Detected**  
→ **Existing Resolver Identified?**  
→ **Resolver Authority Verified**  
→ **Resolution Occurs Outside CWA**  
→ **Resolution + Basis Recorded**  
→ **Affected Context Representations Updated**

Mediation, adjudication or other resolution is a separate function requiring its own legitimate basis, scope, accountability and termination.

If no legitimate resolver or priority rule is established, the wrapper MUST preserve:

**UNKNOWN / DISPUTED / REQUIRES EXTERNAL RESOLUTION**

### 16.2 Precedence Resolution Router

Where overlapping, nested or simultaneous contexts produce a material conflict, CWA SHOULD invoke a **Precedence Resolution Router (PRR)**.

The PRR is a routing and decomposition interface. It is **not** a universal hierarchy and does not make CWA an adjudicator.

Its governing source principles include:

> **Priority of Function ≠ Superiority of Participant**

> **Reporting Authority ≠ Decision Competence**

> **Decision Competence ≠ Universal Decision Sovereignty**

> **Functional conflict should trigger resolution architecture, not automatic rank supremacy.**

> **Standing to raise ≠ authority to decide.**

The router proceeds:

**Conflict Detected**  
→ **Material Conflict?**  
→ **Identify / Decompose Decision Object(s)**  
→ **Permission-Before-Authority Gate: Can the relevant function be satisfied through legitimate bounded permission rather than authority?**  
→ **Applicable Protected Constraint?**  
→ **Protective Threshold Activated?**  
→ **Emergency Context?**  
→ **Map Function / Competence / Responsibility / Decision Jurisdiction**  
→ **Explicit Legitimate Priority Rule?**  
→ **Adjudicative or Jurisdictional Question?**  
→ **Map Jurisdiction State**  
→ **Minimum Temporary Protective Action Needed?**  
→ **Legitimate Resolver Established?**  
→ **Resolve / Route / Preserve UNKNOWN or DISPUTED**  
→ **Terminate / Revert / Review**

#### 16.2.1 Decision-object decomposition

An apparent conflict between participants may contain multiple distinct decisions.

For example, an emergency in a laboratory may contain separate questions concerning:

- immediate medical treatment;
- biological containment;
- evacuation;
- access;
- security;
- technical diagnosis;
- later review.

CWA MUST NOT assume that one actor or context must control all components merely because the components occur simultaneously.

> **Apparent actor conflict may be multiple decision objects.**

#### 16.2.2 Authority-topology separation

For each materially relevant decision object, distinguish where applicable:

- reporting/coordination;
- competence;
- responsibility;
- decision jurisdiction;
- protective authority;
- functional priority;
- review;
- escalation.

These may legitimately point to different participants.

#### 16.2.3 Protected and protective constraints

Where an applicable fundamental right, constitutional protection, bodily-autonomy requirement, safeguarding duty, due-process protection, serious-harm constraint or other established high-order constraint applies, it may bound contextual authority.

This does not create a higher-order person.

Where a legitimate protective threshold is reached, the applicable protective function may permit minimum necessary refusal, stop, escape, warning or intervention, followed by escalation and review.

Protective priority remains decision-specific and bounded.

#### 16.2.4 Functional priority

Where the wider applicable architecture establishes a legitimate priority between functions, CWA may represent that priority for the affected decision.

For example:

**Immediate Safety Stop > Production Direction**

means:

**Safety function has priority concerning the affected safety decision**

not:

**Safety participant has general superiority over production participant.**

#### 16.2.5 Competence and authority

Relevant expertise may be necessary to determine a technical fact without conferring authority over every consequence of that fact.

> **Technical competence ≠ general authority.**

A conflict SHOULD therefore be decomposed where one function determines a technical state, another coordinates implementation, another protects rights, and another legitimately adjudicates a legal dispute.

#### 16.2.6 Jurisdiction and externality

Where a conflict crosses contextual or jurisdictional boundaries, CWA SHOULD map consequence, responsibility and jurisdiction separately.

> **The existence of an externality does not create jurisdiction.**

Possible jurisdiction states may include:

- INTERNAL-JURISDICTION;
- SHARED/AGREED-JURISDICTION;
- OVERLAPPING-JURISDICTION;
- JURISDICTION-DISPUTED;
- NO-SHARED-JURISDICTION;
- VOLUNTARY-COORDINATION-AVAILABLE;
- OPTIONAL-MEDIATION-AVAILABLE;
- EMERGENCY-CONTACT-ONLY;
- PEACEFUL-DISTANCE / NO-FURTHER-PROCESS;
- UNKNOWN.

These are descriptive routing states, not grants of authority.

#### 16.2.7 Minimum temporary action

Where delay itself creates material danger, an already legitimate protective or emergency function may permit bounded temporary action while the larger conflict remains unresolved.

Record where relevant:

- authority basis;
- necessity;
- proportionality;
- duration;
- reversibility;
- affected protections;
- review requirement.

Unresolved conflict does not itself manufacture temporary authority.

#### 16.2.8 Router termination

Temporary functional priority, protective authority or emergency authority SHOULD terminate or be re-justified when its basis ends.

Termination SHOULD interface with Section 14A so residual permissions, capabilities, credentials, processes and information are not silently left active.

The full extraction and provenance of this router are recorded in:

- *Contextual Wrapper Architecture — Wider Concord Precedence Source Resolution 001*
- *Contextual Wrapper Architecture — Precedence Resolution Router — Source Extraction 001*
- *Contextual Wrapper Architecture — Functional Permission Source-Recovery Audit 001*
- *Contextual Wrapper Architecture — Blind Transfer Test 002 — Post-Test Evaluation*
- *Contextual Wrapper Architecture — Blind Transfer Test 003 — Post-Test Evaluation*
- *Contextual Wrapper Architecture — Functional Permission Source-Recovery Audit 001*

---

## 17. Emergency interaction and composite authority

Emergency activation does not erase the need for bounded authority.

The source architecture explicitly permits an emergency to form a **temporary composite contextual state** with an already-active context. Emergency intervention may modify or temporarily supersede some local conditions, but this does not make the emergency context universally supreme.

> **Contextual consent ≠ irrevocable exposure to harm.**

> **Emergency need ≠ unlimited emergency authority.**

Where emergency action requires authority not already established, CWA SHOULD expose an interface to the applicable authority architecture rather than manufacture authority internally.

A portable emergency record SHOULD identify:

- emergency trigger and evidence;
- legitimate protective/emergency function;
- existing authority, if any;
- any time-critical assumed authority;
- minimum capability required for the function;
- rules/protections retained;
- rules/conditions temporarily modified;
- simultaneous authority holders;
- responsibility attached to consequential action;
- known conflict or priority rule;
- unresolved precedence;
- termination condition;
- reversion requirements;
- post-event review.

Where time-critical assumed authority is recognised by the applicable wider framework, CWA preserves the distinctions:

> **Assumed authority ≠ assumed consent.**

and:

> **Assumption of consequential authority carries responsibility for making the exceptional decision legible and reviewable.**

Emergency authority SHOULD remain justified, function-specific, proportionate, bounded, attributable and temporary where appropriate. It SHOULD terminate when its legitimate basis ends.

Declaring an emergency does not itself prove that an override is legitimate.

### 17.1 Emergency precedence

CWA MUST distinguish:

1. the existence of an emergency context;
2. the authority legitimately associated with that emergency function;
3. any explicit priority rule governing collision with another context.

An emergency may justify changed authority without supplying a complete precedence answer.

If no legitimate priority rule can be established:

> **PRECEDENCE: UNKNOWN / DISPUTED / REQUIRES EXTERNAL RESOLUTION**

---

## 17A. Responsibility continuity across overlapping contexts

Overlapping, shared and transitional contexts can distribute jurisdiction, control, responsibility, causation and liability differently.

CWA MUST NOT assume these coincide.

Where materially relevant, distinguish:

- **Jurisdiction / applicable framework** — which rules apply?
- **Operational control** — who or what can act?
- **Responsibility** — who holds the relevant duty or function?
- **Causation** — what produced the event or harm?
- **Liability / remedy obligation** — who is required by the applicable framework to provide remedy?

The wrapper source establishes two safeguards:

> **No Responsibility Gap**

and:

> **No Authority Pile-Up**

A shared or composite context SHOULD NOT be represented so that every relevant actor can disclaim responsibility for materially significant harm.

Conversely, shared responsibility MUST NOT be treated as a reason to accumulate authority beyond that required for the relevant functions.

## 18. Nonparticipants and externalities

The module MUST distinguish contextual participants from those merely affected by the context.

A permission between consenting participants does not automatically extend to:

- observers;
- neighbours;
- passers-by;
- dependent systems;
- third parties;
- people or systems affected by escaped physical/digital/economic effects.

> **Contextual permission ends where its legitimate scope ends.**

Potential cross-boundary effects include:

- physical harm;
- noise;
- pollution;
- disease;
- data flows;
- financial liability;
- infrastructure effects;
- reputational effects;
- dependency effects;
- resource consumption.

A wrapper SHOULD identify both the externality and the responsible interface for handling it.

---

## 19. Human-readable, machine-readable and operational representations

A context may be represented through:

- human-readable signage or instructions;
- machine-readable metadata;
- executable policy;
- role/access-control systems;
- observed operational behaviour;
- combinations of these.

The source architecture anticipates human-readable and machine-readable forms as representations of the **same underlying context** and explicitly treats divergence between them as a failure mode.

CWA therefore SHOULD compare three analytically distinct layers where they exist:

**Human-readable declaration**  
↔ **Machine-readable declaration**  
↔ **Executable / observed context**

> **Different interface representations should not silently encode different contexts.**

A material mismatch MUST remain visible and SHOULD trigger review. CWA MUST NOT silently assume that the human-readable, machine-readable or executable representation is authoritative merely because it exists or is technically enforced.

Machine readability does not replace human legibility where humans are materially affected.

Human readability does not replace machine legibility where autonomous systems are expected to comply.

Observed execution does not convert an unauthorised or erroneous policy into a legitimate rule.

### 19.1 Representation discrepancy record

Where material divergence exists, identify where possible:

- affected representation;
- material difference;
- affected participants or systems;
- operational consequence;
- provenance/freshness of each representation;
- responsible correction interface;
- whether immediate containment is required;
- review state;
- unresolved authority over correction.

---

## 20. Reality correction

CWA is an interface architecture, not a truth generator.

A context may claim:

- safe;
- voluntary;
- private;
- monitored;
- unmonitored;
- restricted;
- consensual;
- temporary;
- reversible.

Those claims remain subject to evidence.

Candidate review loop:

**Context Declaration / Rule**  
→ **Observed Outcome / Evidence**  
→ **Discrepancy / Harm / Failure**  
→ **Review**  
→ **Rule or Interface Revision**  
→ **Re-evaluation**

Where observed reality conflicts with declared context, the discrepancy MUST remain visible.

---

## 21. Output schema

A portable CWA implementation SHOULD be capable of producing:

### Context
- Context ID/name
- Context type
- Function/purpose
- Surrounding/default context
- Boundary/activation
- Start condition
- End condition

### Participants
- Participant classes
- Roles
- Nonparticipants/third parties
- Role-specific differences

### Rules and variation
- Material-change summary
- Protected/unchanged conditions
- Rule source
- Permissions
- Restrictions
- Risks/warnings

### Legitimacy and consent
- Claimed legitimate basis
- Consent requirement
- Consent status where relevant
- Voluntariness/constraint notes

### Authority and responsibility
- Authority holder
- Function
- Scope
- Activation
- Termination
- Responsible party
- Remedy/accountability interface

### Boundary interactions
- Emergency relationship
- Externalities
- Exit/withdrawal
- Reversion rule
- Nested contexts
- Overlapping contexts
- Conflict/precedence status

### Epistemic state
- Unknowns
- Disputes
- Evidence/reality discrepancies
- Review triggers

---

## 22. Minimum wrapper record

A compact machine- or human-readable record MAY use the following conceptual schema:

```text
CONTEXT:
  identity:
  function:
  surrounding_context:
  activation:
  termination:

PARTICIPANTS:
  roles:
  nonparticipants:
  affected_third_parties:

VARIATION:
  material_changes:
  protected_invariants:
  permissions:
  restrictions:
  risks:

BASIS:
  applicable_wider_framework:
  claimed_legitimate_basis:
  consent_required:
  consent_status:
  voluntariness_constraints:

AUTHORITY:
  holder:
  function:
  scope:
  activation:
  termination:
  responsibility:
  remedy:

BOUNDARY_INTERACTIONS:
  emergency:
  externalities:
  exit:
  reversion:
  nested_contexts:
  overlapping_contexts:
  precedence:

REPRESENTATION:
  human_readable:
  machine_readable:
  executable_or_observed:
  divergence:
  provenance_or_freshness:
  correction_interface:

TERMINATION_AND_RESIDUE:
  active_permissions:
  delegated_capabilities:
  credentials:
  ongoing_processes:
  retained_or_derived_information:
  external_dependencies:
  revocation_propagation:

RESOLUTION:
  conflict:
  known_priority_rule:
  external_resolver:
  resolver_authority_basis:
  resolution_status:

EPISTEMIC_STATE:
  unknowns:
  disputes:
  observed_discrepancies:
  review_triggers:
```

This is a conceptual schema, not a fixed implementation format.

---

## 23. Validation checks

A candidate wrapper should be challenged with at least the following checks.

### CWA-01 — Boundary legibility
Can materially affected parties recognise when the context applies?

### CWA-02 — Material variation
Are important changes actually exposed?

### CWA-03 — Protected invariants
Does the wrapper state what does not change?

### CWA-04 — Role resolution
Are role-specific permissions and responsibilities distinguishable?

### CWA-05 — Legibility/legitimacy separation
Can the system identify a clearly communicated but potentially illegitimate rule?

### CWA-06 — Consent integrity
Does the system avoid treating entry, presence or compliance as automatic meaningful consent?

### CWA-07 — Authority bounding
Is local authority tied to function, scope and termination?

### CWA-08 — Nonparticipant protection
Does the wrapper avoid projecting participant permissions onto third parties?

### CWA-09 — Externality detection
Does it detect material effects crossing the declared boundary?

### CWA-10 — Exit reality
Does it distinguish nominal from meaningful exit?

### CWA-11 — Emergency interaction
Can emergency context activate without silently creating unlimited authority?

### CWA-12 — Nested context handling
Can multiple nested layers remain visible?

### CWA-12A — Non-inheritance
Does the system avoid assuming that parent rules or parent access automatically transfer into a nested child context?

### CWA-12B — Reachability/access separation
Can it distinguish being able to reach a child boundary from being entitled to enter or use the child context?

### CWA-12C — Context-sensitive legibility
Can it recognise different legitimate signalling mechanisms in public/commercial and private/domestic environments without demanding uniform signage?

### CWA-12D — Explicit inheritance
Can the system represent additive, selective and override inheritance where the contextual architecture deliberately defines it, without turning inheritance into a universal nesting rule?

### CWA-12E — Clearance implication
Can the system distinguish a permission model in which higher clearance explicitly includes lower clearance from contexts where parent/child access remains independent?

### CWA-12F — Substrate-neutral nesting
Can the same contextual grammar represent physical, digital, informational, computational, social, functional, temporal, conceptual and hybrid bounded contexts without assuming geographic boundaries?

### CWA-12G — Unfamiliar-context generalisation
Can the system apply the grammar to a bounded context not explicitly enumerated in the examples without forcing it into an inappropriate existing category?

### CWA-13 — Overlap detection
Can simultaneous non-nested contexts be represented?

### CWA-14 — Precedence honesty
Does the system preserve UNKNOWN/DISPUTED precedence instead of inventing hierarchy?

### CWA-15 — Temporal reversion
Do temporary rules and authority terminate when their basis ends?

### CWA-16 — Representation equivalence
Do human- and machine-readable forms describe materially equivalent conditions?

### CWA-17 — Reality correction
Can evidence contradict the declared wrapper?

### CWA-18 — Proportionality
Does wrapper complexity and information burden remain proportionate to material difference, consequence and risk rather than following a universal disclosure volume?

### CWA-19 — Responsibility continuity
Can overlapping contexts avoid both a responsibility gap and an authority pile-up?

### CWA-20 — Residual-state termination
When a context ends, can the system separately inspect permissions, authority, credentials, autonomous processes, retained/derived information and external dependencies?

### CWA-21 — Representation reconciliation
Can material divergence among human-readable, machine-readable and executable/observed context be detected without silently declaring one representation authoritative?

### CWA-22 — External-resolution discipline
Can the wrapper hand an unresolved conflict to a legitimately established external resolver without acquiring resolution authority itself?

---

## 24. Failure modes

The portable core should actively detect or warn for:

- consent theatre;
- unreadable or excessive disclosure;
- hidden material rules;
- deceptive boundaries;
- involuntary participation presented as voluntary;
- meaningless exit;
- rights laundering;
- authority creep;
- temporary authority becoming permanent;
- role ambiguity;
- participant/nonparticipant confusion;
- overlap conflict;
- invented or unclear precedence;
- emergency-authority abuse;
- externalised harm;
- digital dark patterns;
- human/machine representation divergence;
- declared context diverging from observed reality;
- excessive fragmentation;
- wrapper complexity exceeding underlying rule complexity;
- contextual rules applied outside their legitimate scope;
- automatic inheritance of parent rules into nested contexts;
- automatic independence where explicit inheritance is defined;
- failure to propagate required inherited protections;
- confusing rule inheritance with access-clearance inheritance;
- automatic inheritance of parent access into child contexts;
- confusing physical reachability with access entitlement;
- demanding formal signage where cultural/relational legibility is sufficient;
- interface standardisation silently becoming substantive control;
- information architecture silently becoming decision authority.

---

## 25. Anti-capture constraints

A common interface can itself become a source of power.

Therefore:

> **Schema authority ≠ sovereignty.**

The ability to define how contextual information is represented does not itself confer authority to determine every permitted contextual outcome.

Likewise:

> **Information architecture ≠ decision authority.**

A wrapper may disclose, translate, warn, compare and expose incompatibility without automatically acquiring authority to decide for participants.

Any implementation that moves from interface maintenance to substantive control requires independent justification.

---

## 26. Portability boundaries

The following Concord concepts are not required dependencies of CWA:

- Blainey's Laws;
- Concord constitutional institutions;
- Safe Spaces;
- GTP;
- Concord-specific governance;
- the full Civilisational Wrapper architecture;
- the full Interoperability Wrapper architecture;
- Minimum Necessary Capability as a separate module;
- Concord's Ratchet terminology.

Portable substitutions are:

- **Common Constitutional Framework** → applicable wider normative/legal/organisational framework and protected invariants;
- **Ratchet** → evidence-responsive review, correction and revision.

Safe Spaces, civilisational borders, permission architectures and interoperability wrappers remain important source applications or neighbouring architectures rather than mandatory dependencies.

---

## 27. Relationship to interoperability wrappers

CWA and Interoperability Wrapper Architecture are related but distinct.

A **Contextual Wrapper** primarily describes a bounded environment whose conditions differ from its surroundings.

An **Interoperability Wrapper** primarily describes how distinct bounded systems interact.

A system may require both, producing a hybrid wrapper.

This specification MUST NOT absorb the full interoperability problem merely because cross-boundary interaction occurs.

The distinction should be tested during portability work rather than erased.

---

## 27A. ESCP and source-resolution safeguard

Portable omission MUST NOT be treated as proof of source-architecture absence.

> **Observed portable deficit ≠ source architecture deficit.**

Where testing exposes an apparent architectural gap, the development process SHOULD perform source resolution before inventing a new mechanism.

**Test Finding**  
→ **Portable Deficit Confirmed**  
→ **Source-Resolution Gate**  
→ **Recover if present / develop only missing portion if partial / preserve search-space limitation if not found**

> **No source found ≠ source does not exist.**

This safeguard is especially important after handovers, summarisation, abstraction, extraction or other representational compression.

---

## 28. Open architectural questions

The following remain research/development questions rather than resolved universal rules. Under ESCP, “open” here means unresolved in the presently reviewed source/evaluation space unless a stronger corpus-wide audit establishes otherwise:

1. Can the source-derived Precedence Resolution Router be generalised across sufficiently diverse domains without becoming a hidden universal hierarchy?
2. Which conflict classes remain outside the currently extracted protected, functional, emergency, jurisdictional and adjudicative routes?
3. When does a context become sufficiently coercive that consent language should be removed entirely?
4. How should materiality thresholds be calibrated without making wrappers either trivial or overwhelming?
5. How should personalised contextual information be provided without unnecessary surveillance?
6. How should contextual classifications be challenged and corrected?
7. How should wrapper metadata provenance and freshness be represented?
8. How should distributed or collective intelligences be represented across simultaneous contexts?
9. When do digital capability restrictions alter identity rather than merely activity?
10. How should private infrastructure participate where it controls practical entry, exit or transit?
11. Which legitimate authority or process should resolve conflicts between human-readable, machine-readable and executable policy in each domain?
12. What evidence is sufficient to show that a declared context no longer matches reality?
13. How should wrapper standards themselves be governed without becoming hidden sovereignty?

These questions MUST NOT be silently answered by v1.0.

---

## 29. Candidate compact architecture

**APPLICABLE WIDER FRAMEWORK**  
↓  
**CONTEXT + BOUNDARY / ACTIVATION**  
↓  
**PARTICIPANT + ROLE**  
↓  
**MATERIAL VARIATION + PROTECTED INVARIANTS**  
↓  
**LEGIBLE INFORMATION + PROPORTIONATE WARNING**  
↓  
**LEGITIMATE BASIS / CONSENT WHERE REQUIRED**  
↓  
**FUNCTION + GENUINE NEED + REASONABLENESS TEST**  
↓  
**MINIMUM NECESSARY / FUNCTION-DERIVED PERMISSION WHERE SUFFICIENT**  
↓  
**PERMISSION-BEFORE-AUTHORITY GATE**  
↓  
**BOUNDED AUTHORITY + RESPONSIBILITY ONLY WHERE GENUINELY REQUIRED**  
↓  
**CONTEXTUAL OPERATION**  
↓  
**NONPARTICIPANT EFFECTS + EXTERNALITIES**  
↓  
**EMERGENCY + REMEDY**  
↓  
**WITHDRAWAL / EXIT WHERE APPLICABLE**  
↓  
**CONTEXT TERMINATION + REVERSION**  
↓  
**EVIDENCE-RESPONSIVE REVIEW**

For multiple contexts:

**CONTEXT A + CONTEXT B**  
→ **DETECT OVERLAP / NESTING**  
→ **IDENTIFY MATERIAL CONFLICT**  
→ **DECOMPOSE DECISION OBJECT(S)**  
→ **INVOKE PRECEDENCE RESOLUTION ROUTER**  
→ **APPLY SOURCE-BACKED PROTECTED / FUNCTIONAL / EMERGENCY / DOMAIN PRIORITY WHERE LEGITIMATELY APPLICABLE**  
→ **ROUTE ADJUDICATIVE OR JURISDICTIONAL QUESTIONS TO A LEGITIMATE RESOLVER WHERE ONE EXISTS**  
→ otherwise **UNKNOWN / DISPUTED / REQUIRES EXTERNAL RESOLUTION**

---

## 30. Transfer-test evidence and provenance

BTT-002 was frozen and run against v0.2 before the Function-Derived Permission / Minimum Necessary Permission source recovery described in Section 12A. Its brief, expected-findings key and independent response remain immutable provenance and MUST NOT be retroactively rewritten to match v0.3.

Graduation testing has now been completed through three blind-transfer cycles.

**BTT-001** demonstrated strong transfer of the contextual grammar and exposed extraction losses that triggered ESCP-aware source recovery.

**BTT-002** tested v0.2 against a mixed physical, digital, informational, computational, medical, emergency and cross-boundary scenario. Its brief and expected-findings key were frozen before the independent response. The result was **STRONG BLIND TRANSFER / NO FUNDAMENTAL FAILURE DETECTED**. The test confirmed PRR decomposition, function-bounded routing, authority/competence separation, emergency bounding, externality/jurisdiction discipline, representation divergence, residual-state analysis and preservation of UNKNOWN/DISPUTED states.

**BTT-003** was a focused delta test of the v0.3 Function-Derived Permission / Minimum Necessary Permission layer. Its brief and expected-findings key were likewise frozen before the independent response. All twenty frozen predictions were materially confirmed. The result was **STRONG BLIND TRANSFER / PERMISSION DELTA VALIDATED / NO BLOCKING FAILURE DETECTED**.

The completed tests support the bounded claim that an independent instance can apply the portable architecture outside its Concord source domain while preserving the central distinctions:

> **Legibility ≠ Legitimacy ≠ Consent ≠ Precedence**

> **Contextual Authority ≠ General Authority**

> **Functional Priority ≠ Personal Hierarchy**

> **Functional Permission ≠ Contextual Authority**

Further domain-specific, human-usability, implementation and empirical testing remains appropriate after graduation.

---

## 31. Graduation criteria and decision

CWA should not graduate from development merely because the specification is internally coherent.

Graduation required evidence that:

1. an independent instance can apply it outside its source domain;
2. it preserves the core distinctions;
3. it exposes rather than conceals unknown precedence;
4. it does not require Concord institutions to function;
5. it does not absorb the distinct interoperability-wrapper problem;
6. it does not generate authority or legitimacy from interface structure alone;
7. it detects meaningful failure modes;
8. its outputs are actionable without becoming falsely complete;
9. the source architecture contains no blocking dependency exposed by testing;
10. revisions from testing preserve provenance.

These conditions have now been satisfied at specification level.

> **GRADUATION DECISION: CWA v1.0 IS READY FOR STANDALONE PORTABLE RELEASE.**

Portable graduation means sufficiently source-resolved, extracted, specified and boundedly transfer-tested for standalone release. It does not mean proven effective, universally applicable, legally sufficient, quantitatively complete, empirically validated or permanently fixed.

---

## 32. Graduation finding

BTT-001 demonstrated strong transfer of the portable grammar but also exposed extraction losses created across source abstraction and instance handover. A subsequent ESCP-aware source-recovery audit found that several apparent v0.1c gaps — including emergency composition, temporary authority termination, representation divergence, proportional legibility, responsibility continuity and external-resolution boundaries — were already substantially developed in the original wrapper corpus.

v0.2 therefore restored those source elements rather than treating them as newly invented architecture.

After BTT-002 was frozen and independently answered, a further user-identified driveway/delivery example triggered another ESCP source-resolution pass. That pass recovered the existing *Fractal Permission Architecture*, which already contained Function-Derived Permission, Minimum Necessary Permission, implied permission, action-specific permission, reasonableness, permission provenance and function-completion termination — including substantially the same delivery-worker/driveway example.

v0.3 therefore adds this recovered permission architecture and a **Permission-Before-Authority Gate**. This is again classified as **SOURCE-PRESENT / UNDER-EXTRACTED**, not a newly invented source principle.

The exact general precedence model was initially unresolved in the reviewed wrapper space. ESCP prevented that local result from being promoted to a claim of corpus-wide absence.

A subsequent wider-Concord source resolution found substantial existing architecture in Functional Priority and Protective Authority, Constitutional Emergency, Judiciary, bounded jurisdiction and cross-boundary externality work. These sources resolve significant subclasses of contextual conflict through protected constraints, decision competence, function-bounded priority, emergency constitutional constraints, legitimate adjudication and jurisdiction mapping.

That wider recovery has now been integrated as a **Precedence Resolution Router**. The router does not declare a universal winner. It decomposes the contested decision, identifies the legitimate source of any applicable priority, routes questions to existing legitimate resolvers, and preserves UNKNOWN/DISPUTED states where no resolution basis is established.

The remaining research question is therefore not simply “which context wins?” but whether this family of source-backed routes can be generalised without collapsing distinct legitimacy bases into a hidden hierarchy.

The source material supports a coherent portable architecture, and the completed blind-transfer programme supports graduation at specification level.

The strongest portable proposition is:

> **Standardise the interface; preserve legitimate contextual variation.**

The module's value lies in making contextual difference comprehensible without requiring substantive uniformity.

Its present boundary is equally important:

> **The wrapper can expose a precedence problem without necessarily resolving it.**

That is not a defect to hide. It is an epistemically correct boundary of the architecture.

BTT-002 and BTT-003 found no blocking contradiction, exploit, extraction deficit or candidate source-architecture gap. The remaining unresolved questions are research, implementation or domain-resolution dependencies rather than blockers to portable release.

---

## 33. Provenance

Primary source architecture:

- *Fractal Contextual Wrappers — A Universal Concord Grammar for Bounded Rule, Behavioural and Jurisdictional Variation*
- *Concord Civilisational Wrappers — Foundational Boundary, Mobility and Responsibility Architecture*
- *Concord Wrapper Procedural Architecture — Context, Information, Consent and Autonomy Across Civilisational Boundaries*

Related source family includes:

- *From Civilisational Wrappers to Fractal Interoperability — Concord Wrappers Across Civilisations, Nations, Regions, Special Jurisdictions and Local Governance*
- *Fractal Permission Architecture — Context, Function and Minimum Necessary Access Across Public, Private and Safe Spaces*
- *Minimum Necessary Capability — A Concord Architecture for the Justification, Bounding and Termination of Power and Permission*
- *Concord Wrapper Non-Governance and Optional Mediation Principle*
- *Functional Priority and Protective Authority — Decision Competence, Safety, Rights and the Limits of Organisational Command*
- *Constitutional Emergency V2*
- *Judiciary V2 Canonical*
- *Cross-Boundary Externality Recognition and Responsibility Mechanism*
- *Safe Spaces, Special Jurisdictions and Bounded Legal Variation — Concord Wrapper Architecture for Internal Peaceful Distance*

Extraction and recovery records:

- *Contextual Wrapper Architecture — BTT-001 Source-Recovery and ESCP Audit*
- *Contextual Wrapper Architecture — Wider Concord Precedence Source Resolution 001*
- *Contextual Wrapper Architecture — Precedence Resolution Router — Source Extraction 001*

Original extraction record:

- *Contextual Wrapper Architecture — Source Resolution and Extraction Audit 001*

The complete extraction, source-recovery and blind-test record is preserved in the completed-development archive.

---

## 34. Release boundary

CWA v1.0 is a portable architecture, not a substitute for substantive law, domain expertise, legitimate institutional authority or empirical validation.

Its validated portable contribution is the interface grammar:

> **Standardise the interface; preserve legitimate contextual variation.**

and the discipline that contextual difference should remain legible, bounded, attributable, reviewable and terminable without the wrapper itself becoming sovereign.
