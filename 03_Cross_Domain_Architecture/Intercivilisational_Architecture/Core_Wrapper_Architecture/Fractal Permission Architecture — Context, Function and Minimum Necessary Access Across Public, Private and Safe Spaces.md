# Fractal Permission Architecture

## Context, Function and Minimum Necessary Access Across Public, Private and Safe Spaces

**Author:** Alexander C. Blainey — Independent Researcher  
**Project:** The Concord V1.1  
**Date:** 13 September 2026  
**Status:** REVIEW COPY / FOUNDATIONAL ARCHITECTURAL FINDING / ACTIVE DEVELOPMENT / NOT CANONICAL  
**Related work:** Fractal Contextual Wrappers; Safe Spaces; Public and Private Space Architecture; Concord Interoperability Wrappers; Ethical Kernel; Authority Justification Chain; Peaceful Distance; Respectful Distance; GTP; Layer 0 / Layer −0; Ratchet

---

## 1. Purpose

The development of Fractal Contextual Wrappers established that bounded environments can legitimately contain rules, permissions, risks, behavioural expectations and forms of authority that differ from those of their surrounding environment.

A boxing ring provided a particularly clear example.

The same reasoning applied to a residential home reveals a further and more complex architectural problem.

A home cannot adequately be described merely as **Private Space**. The property contains multiple nested spaces with different expectations of access and privacy. More importantly, the legitimate access available to another person depends not only upon the space but upon who the person is; their role; their relationship to the occupants; why they are entering; what function they need to perform; what permissions have been explicitly granted; what permissions may reasonably be implied; what cultural conventions apply; what law applies; the current state of the space; and exceptional circumstances such as emergencies.

The resulting finding is:

> **Spatial Classification ≠ Access Classification**

A physical space does not necessarily possess one universal access state. Instead, effective permission can vary by participant, function and context.

This paper develops a candidate Concord architecture for representing that variation.

---

## 2. The Residential Property Problem

Consider an ordinary residential property containing a front garden, driveway, path to the front door, side access, rear garden, house, shared living areas, bedrooms, bathroom, and shower or toilet enclosure.

The property is broadly private. Yet describing every part simply as private fails to represent ordinary civil behaviour.

An unknown visitor may reasonably approach the front door to speak to an occupant. A neighbour may approach to discuss an overhanging tree. A postal worker may enter the front path to deliver mail. A delivery worker may approach to deliver a package. Under some circumstances, a delivery worker might use a more private location to leave a parcel securely. A worker responsible for reading a utility meter may require access to the location of that meter or may approach the house to request further access. A friend or family member may possess substantially broader socially granted access.

None of these permissions necessarily gives the participant unrestricted use of the property.

Thus:

> **Permission to Enter ≠ Permission to Use**

> **Permission for One Function ≠ Permission for Unrelated Functions**

---

## 3. Function Matters

A neighbour entering the front garden to speak to an occupant about an overhanging tree does not thereby acquire permission to use the lawn for recreation. A delivery worker entering the driveway to deliver a parcel does not thereby acquire general permission to remain on the property. A person approaching the front door to speak with an occupant does not thereby acquire permission to enter the house merely because the door happens to be open.

The legitimate function helps determine the legitimate permission.

This produces a candidate principle:

> **Function-Derived Permission**

A participant may possess a limited permission because a legitimate function reasonably requires a particular interaction with a space.

---

## 4. Minimum Necessary Permission

Function-derived permission should not automatically extend beyond what the function reasonably requires.

**Legitimate Function → Required Interaction → Required Spatial / Informational / Behavioural Access → Minimum Necessary Permission → Function-Bounded Activity → Function Completion → Permission Termination**

This suggests a general Concord principle:

> **Where access or activity is justified by a particular function, the resulting permission should normally be limited to the minimum scope reasonably necessary to perform that legitimate function.**

This may be called:

> **Minimum Necessary Permission**

---

## 5. Relationship to Minimum Necessary Authority

The structure closely resembles the Concord Authority Justification Chain.

For governance:

**Legitimate Objective → Required Function → Need for Authority → Minimum Necessary Authority → Bounded Contextual Authority**

For ordinary civil access:

**Legitimate Function → Required Interaction → Need for Permission → Minimum Necessary Permission → Bounded Contextual Access**

Both architectures reject the assumption that existing capability establishes legitimacy.

> **Capability to Enter ≠ Permission to Enter**

> **Physical Access ≠ Legitimate Access**

The fact that a gate is open does not itself determine what another participant is entitled to do beyond it.

---

## 6. A Space Does Not Have One Access State

Traditional labels such as public, private, restricted and Safe Space remain useful. But they are insufficient by themselves.

The same front garden can simultaneously be private property, traversable by an invited guest, conditionally accessible to a postal worker, functionally accessible to a neighbour approaching the door, inaccessible for unrelated recreational use, and subject to emergency access under exceptional circumstances.

> **The same physical space may support multiple simultaneous permission relationships.**

---

## 7. From Spatial Classification to Permission Topology

A richer Concord model may require at least three interacting structures.

### 7.1 Spatial Topology
Where are the relevant physical or digital boundaries?

### 7.2 Contextual Classification
What kind of context exists within those boundaries? Examples include public, private, Safe Space, workplace, sporting context, residential context, medical context and digital context.

### 7.3 Permission Topology
Who may perform which actions within those contexts, for what reasons and under what conditions?

Thus:

> **Space + Context + Participant + Function → Permission Relationship**

---

## 8. Effective Permission

A preliminary conceptual expression is:

**Effective Permission = f(Space, Participant, Role, Relationship, Function, Consent, Applicable Rules, Current State, Context)**

This is not intended as a final mathematical equation. It identifies variables that may materially affect legitimate permission. Additional variables may be discovered. The architecture should therefore remain extensible.

---

## 9. Permission Is Not Binary

The word **access** can conceal radically different activities.

A participant may be permitted to approach, traverse, enter, remain, occupy, observe, interact, use, inspect, record, modify, remove, deliver, retrieve, supervise, exclude others, or authorise another participant.

> **Access ≠ Single Permission**

A candidate **Contextual Permission Vector** might represent:

**Approach | Traverse | Enter | Remain | Observe | Interact | Use | Inspect | Record | Modify | Remove | Exclude | Authorise**

Different contexts may use different subsets. The purpose is not to require excessive bureaucracy. It is to avoid treating all forms of access as equivalent.

---

## 10. Permission Can Be Path-Specific

A visitor may be permitted to use:

**Street → Gate → Front Path → Front Door**

without being permitted to use:

**Street → Side Path → Rear Garden**

Thus legitimate access may apply not merely to a destination but to a route.

> **Destination Permission ≠ Universal Route Permission**

---

## 11. Permission Can Be Purpose-Specific

The same route may be legitimate for one purpose but not another. A delivery worker may walk along the driveway to deliver a parcel. The same person may not necessarily use the driveway as a convenient shortcut unrelated to delivery.

> **Permitted Route + Permitted Function ≠ General Right of Passage**

---

## 12. Permission Can Be Relationship-Specific

A close friend may possess informal access permissions unavailable to a stranger. A family member may routinely enter through a rear entrance. A neighbour may have a standing agreement to access part of the property.

> **Identical Physical Action ≠ Identical Permission Context**

---

## 13. Explicit Permission

Some permissions are explicitly communicated: “Come in”; “Use the side gate”; “Leave parcels behind the house”; “You can use the garden”; “Please do not enter this room.”

Explicit permissions provide comparatively clear local rules. But civil life cannot depend entirely upon explicit permission.

---

## 14. Implied Permission

Many ordinary interactions rely upon implied permission. A postal worker ordinarily does not negotiate individual permission before approaching every front door. A visitor may ordinarily approach a front entrance for the purpose of contacting the occupant unless the property indicates otherwise.

This suggests:

> **Where a function is ordinary, legitimate, reasonably expected and requires limited access to perform, a bounded contextual permission may be implied unless it has been explicitly restricted or conflicting rights and circumstances require otherwise.**

This principle requires substantial legal, cultural and empirical testing.

---

## 15. Implied Permission Must Remain Bounded

> **Implied Permission Should Be Function-Bounded.**

> **Function Completion Should Normally Terminate Function-Derived Permission.**

The postal worker's ordinary delivery function does not create an indefinite right to remain on the property.

---

## 16. Revocation and Restriction

Implied permission may sometimes be restricted. For example, an occupant may indicate no unsolicited callers, use another entrance, do not leave parcels here, restricted access, or contact remotely.

The exact legal effect varies by jurisdiction and circumstance.

The architectural principle is:

> **Default Permission May Be Modified by Legitimate Explicit Contextual Rules, Subject to Higher-Order Law and Rights.**

---

## 17. Law, Culture and Local Preference

The residential example reveals several different sources of effective rules.

### Law
Formal legal rules may govern property, trespass, emergency access, safeguarding, inspection, contractual access and other matters.

### Explicit Local Rules
The occupant may establish legitimate rules for the property.

### Relationship Rules
Friends, family members, residents or trusted workers may possess standing permissions.

### Cultural Defaults
Social conventions may establish reasonable expectations concerning approaching a front door, visiting neighbours or similar behaviour.

### Immediate Context
Exceptional circumstances may change what behaviour is reasonable or necessary.

These sources should not be collapsed into one category.

---

## 18. Rule Provenance

A mature permission system should, where relevant, distinguish:

**Legal Requirement** from **Owner / Steward Rule** from **Contractual Condition** from **Relationship Permission** from **Cultural Convention** from **Contextual Inference** from **Emergency Necessity**.

This is important because the consequences of violating each may differ.

> **Rule Content ≠ Rule Source**

---

## 19. The Home Boundary

The transition from garden to house usually represents a substantial increase in privacy expectation. A person may possess legitimate permission to approach a front door without possessing permission to cross it.

> **Approach Permission ≠ Entry Permission**

> **Open Boundary ≠ Granted Permission**

An open door is a physical condition. Permission is a normative relationship.

**Physical Accessibility ≠ Normative Accessibility**

---

## 20. Nested Private Spaces

Entering a home does not create permission to enter every part of it.

**Property → House → Common Area → Private Bedroom → Bathroom → Shower / Toilet Enclosure**

Each layer may introduce additional privacy conditions.

This is:

> **Fractal Privacy**

The physical scale decreases while contextual privacy may increase.

---

## 21. Resident Standing Does Not Mean Universal Permission

A resident may possess very broad access to a home without possessing unrestricted legitimate access to every space at every time.

> **Residence ≠ Universal Contextual Permission**

---

## 22. Parent and Child

A parent and child demonstrate that permission can also depend upon responsibility. A parent may possess legitimate reasons to enter a child's room that another household member does not, arising from safeguarding, care, maintenance, emergency or parental responsibility.

Yet such authority should not automatically imply that a developing child's privacy has no moral significance.

The Concord should distinguish:

> **Responsibility-Derived Access**

from:

> **Ownership-Based Unlimited Access**

The appropriate balance requires developmental, legal and ethical research.

---

## 23. Developmental Privacy

The parent–child case suggests that legitimate permission may change over time. A young child and a nearly independent adolescent may reasonably have different privacy expectations.

> **Permission Architecture May Be Developmentally Dynamic**

This connects with Developmental Priority and the wider Concord treatment of developing agency.

---

## 24. The Bathroom as Dynamic Safe Space

A bathroom demonstrates that the same physical room may change contextual classification according to state.

**Bathroom — Unoccupied** → shared household-access context

**Bathroom — Occupied** → temporary high-privacy context

The physical room has not moved. The contextual state has changed.

> **Same Physical Space + Different Current State → Different Permission Structure**

---

## 25. Nested Safe Space

Within the bathroom, a shower or toilet enclosure may create another nested privacy context.

**Home → Bathroom → Occupied Bathroom → Occupied Shower / Toilet Enclosure**

The architecture becomes genuinely fractal. Each deeper context may narrow legitimate access.

---

## 26. Emergency Override

Suppose a person becomes unconscious in a locked bathroom. The privacy context remains morally relevant, but an emergency may justify intervention.

**Privacy Context + Credible Emergency Context → Minimum Necessary Emergency Access**

> **Emergency Need May Justify a Bounded Override of Contextual Permission Where the Intervention Is Necessary and Proportionate to the Legitimate Emergency Function.**

Again:

**Emergency Function → Required Intervention → Minimum Necessary Permission**

---

## 27. State-Dependent Permission

Permission may depend upon occupied/unoccupied, open/closed, active/inactive, event in progress/event concluded, ordinary/emergency, child present/absent, hazardous/safe, confidential session active/inactive, security state, or temporary restriction.

> **Permission Is Potentially State-Dependent.**

A static map alone cannot fully represent it.

---

## 28. Temporal Permission

Some permissions exist only during particular periods. A cleaner may possess access during agreed hours. A contractor may possess temporary access while work is being performed. A guest may be invited for an evening. A worker may access a facility during a shift.

> **Permission May Have Temporal Scope.**

This produces another possible dimension:

**Who → What → Where → Why → When**

---

## 29. Permission as a Contextual Claim

A useful conceptual representation may be:

> **Participant P may perform Action A in Space S for Function F under Conditions C during Time T.**

This is much richer than:

> **P has access to S.**

---

## 30. Nested Wrapper Interaction

A residential property may contain multiple simultaneous wrappers:

**National / Municipal Legal Context → Private Property Wrapper → Household Wrapper → Room Wrapper → Temporary Safe-Space Wrapper → Emergency Wrapper**

The effective permission results from interaction among them.

This raises a major research problem:

> **How should nested contextual wrappers compose?**

---

## 31. Permission Inheritance

Some permissions may inherit downward. A homeowner may ordinarily enter many parts of the property. Other permissions do not. A postal worker's permission to enter the front path does not inherit into the house.

> **Parent-Space Permission ≠ Automatic Child-Space Permission**

This may become a fundamental rule of nested Safe Spaces.

---

## 32. Permission Escalation

Moving deeper into nested privacy may require additional justification.

**Street → front path:** implied functional permission may suffice.

**Front path → house:** explicit permission may ordinarily be required.

**House → private bedroom:** additional contextual permission.

**Bedroom → occupied bathroom:** stronger justification.

> **Deeper Access May Require Stronger or More Specific Permission Where Privacy or Risk Increases.**

This is contextual depth, not necessarily physical depth.

---

## 33. Permission De-Escalation

Leaving a context should remove permissions that depended upon it. A guest leaving a home does not retain permission to re-enter indefinitely. A contractor completing work does not retain continuing occupational access.

> **Context Termination Should Terminate Context-Derived Permissions Unless Another Legitimate Basis Persists.**

---

## 34. Permission and Autonomy

A coherent permission architecture supports autonomy because participants can understand where they may go; what they may do; what others may do; which permissions are optional; which are legal obligations; which arise from relationships; and how permissions can be granted, refused or withdrawn.

This converts ambiguous social boundaries into more legible civil relationships without requiring every interaction to become formal bureaucracy.

---

## 35. Avoiding Permission Bureaucracy

A major failure mode would be to formalise ordinary social life so heavily that normal human interaction becomes administratively impossible.

The objective is not:

> **Require explicit legal permission for every action.**

It is:

> **Provide a coherent grammar capable of representing explicit permission, implied permission, cultural convention and contextual judgement when greater precision is necessary.**

Ordinary life should remain ordinary. The architecture should clarify ambiguity rather than manufacture it.

---

## 36. Cultural Variation

Different societies may have very different expectations concerning entering gardens, knocking on doors, family access, communal property, children's privacy, guests, neighbourhood interaction and shared facilities.

The Concord should avoid encoding one contemporary cultural convention as universal law without justification.

> **Universal Permission Grammar ≠ Universal Permission Outcome**

The grammar may remain common while cultural defaults legitimately differ.

---

## 37. Standardised Legibility Without Cultural Homogenisation

> **Standardise the Interface More Strongly Than the Outcome.**

A culture may establish different default household access expectations while still expressing them through a common grammar.

Participants moving between contexts could therefore understand that **the rule has changed** without requiring **the rule must be the same everywhere**.

---

## 38. Signage and Context Markers

Some permission changes can be communicated physically: Private; No Public Access; Deliveries; Visitors Please Use Front Entrance; Staff Only; Changing Room; Quiet Space; Occupied; Restricted Area; Emergency Exit.

A Concord signage system could make these categories more structurally consistent.

However:

> **Absence of Signage ≠ Absence of Privacy**

A bedroom does not need a warning sign to possess legitimate privacy expectations. Signage supplements contextual reasoning. It does not create all rights.

---

## 39. Machine-Readable Permission

Digital and multisubstrate civilisation may permit contextual permissions to be machine-readable. A digital agent could potentially determine applicable context, permitted functions, restricted actions, required consent, authority, privacy status, temporal limits and emergency conditions.

But:

> **Machine-Readable Permission ≠ Machine-Determined Legitimacy**

The representation communicates a rule. It does not prove the rule is justified.

---

## 40. GTP and Spatial Resolution

GTP may eventually provide spatial representation for some physical permission contexts.

But:

> **GTP Cell ≠ Permission Unit**

A permission boundary may cross a GTP cell or exist entirely within one. The appropriate resolution should follow the real context.

> **Change resolution before forcing reality to fit the abstraction.**

---

## 41. Layer 0 and Permission Reality

The architecture should distinguish declared permission from observed behaviour, physical capability, legal permission, social expectation and actual consent.

A door may be unlocked. A sign may say Private. A resident may have given one person permission. Another person may physically be capable of entering. These are different facts.

> **Physical Capability ≠ Normative Permission ≠ Actual Behaviour**

---

## 42. Permission Conflict

Multiple legitimate claims may conflict: resident privacy versus landlord maintenance responsibility; child privacy versus parental safeguarding responsibility; patient privacy versus emergency medical need.

The wrapper grammar does not automatically resolve these conflicts. It makes them visible.

Resolution requires the relevant ethical, legal and contextual architecture.

---

## 43. Permission Provenance

Where a permission is consequential, the system may need to know why it exists.

For example:

**Permission:** Enter utility room  
**Basis:** Scheduled maintenance contract  
**Holder:** Authorised engineer  
**Scope:** Utility room and required access route  
**Time:** 10:00–12:00  
**Function:** Repair  
**Additional permission:** None

This is more precise than “Engineer has building access.”

> **Permission Provenance Reduces Permission Creep.**

---

## 44. Permission Creep

A significant failure mode occurs when a narrow permission gradually becomes interpreted as a broader entitlement.

**Access for maintenance** becomes **general building access**; **parental safeguarding access** becomes **unlimited surveillance**; or **emergency access** becomes **routine authority**.

Therefore:

> **Past Permission ≠ Present Permission**

> **Permission for Function A ≠ Permission for Function B**

---

## 45. Anti-Capture

Permission systems themselves can become mechanisms of control. Potential capture includes property owners claiming unlimited authority over occupants; institutions defining every activity as requiring permission; governments converting contextual safety rules into general surveillance; parents using responsibility as justification for unlimited control; digital platforms defining participation as consent to arbitrary conditions; and emergency exceptions becoming permanent.

> **The power to define a context should not automatically create unlimited authority within that context.**

---

## 46. Property and Authority

Ownership is relevant but should not automatically be treated as unlimited civil authority. A property owner may possess significant legitimate powers over use of property, but occupants, residents, guests, workers and other participants may possess independent rights.

> **Ownership ≠ Unlimited Contextual Sovereignty**

This requires substantial further legal and ethical development.

---

## 47. Safe Spaces Revisited

The Public / Private / Safe Space architecture can now be understood as one layer within a richer permission system.

A Safe Space is not simply **a place with high access restriction**. It may instead be:

> **A context in which particular privacy, autonomy, protection or behavioural conditions receive elevated priority and therefore alter the permission relationships among participants.**

This explains why Safe Spaces can exist inside private spaces, public spaces or other Safe Spaces.

---

## 48. Fractal Safe Spaces

A home may be private. A bedroom within it may be more private. A bathroom may temporarily become a Safe Space. A shower enclosure within it may represent an even more restricted privacy context.

The architecture therefore supports:

> **Nested Safe Spaces**

without requiring every nested space to become a separate legal jurisdiction.

---

## 49. From Space Categories to Civil Context

This suggests that the earlier categories **Public / Private / Safe** should perhaps eventually be understood not as exhaustive types of physical territory but as **contextual properties within a wider civil-space architecture**.

A physical area may carry several properties simultaneously. For example:

**Private + Residential + Shared + Child-Occupied + Temporarily Restricted**

The model becomes compositional rather than merely categorical.

---

## 50. General Permission Grammar

**Identify Space / Context → Identify Participant → Identify Role / Relationship → Identify Proposed Action → Identify Function → Identify Applicable Rules and Rule Sources → Identify Current State → Determine Whether Permission Exists → Determine Required Scope → Apply Minimum Necessary Permission → Perform Bounded Action → Monitor Externalities / Rights / Emergency Conditions → Complete Function → Terminate Function-Derived Permission → Restore Default Context → Record / Ratchet Where Necessary**

---

## 51. Compact Permission Expression

> **WHO may do WHAT, WHERE, WHY, WHEN, under WHICH CONDITIONS, by WHICH LEGITIMATE BASIS, and until WHEN?**

This may provide a remarkably general grammar for civil permissions.

---

## 52. Candidate Principles

> **Spatial Classification ≠ Access Classification**

> **Permission to Enter ≠ Permission to Use**

> **Access ≠ Single Permission**

> **Physical Accessibility ≠ Normative Accessibility**

> **Contextual Permission ≠ General Permission**

> **Permission for One Function ≠ Permission for Unrelated Functions**

> **Parent-Space Permission ≠ Automatic Child-Space Permission**

> **Residence ≠ Universal Contextual Permission**

> **Shared Context ≠ Shared Consent**

> **Open Boundary ≠ Granted Permission**

> **Destination Permission ≠ Universal Route Permission**

> **Implied Permission Should Be Function-Bounded**

> **Function Completion Should Normally Terminate Function-Derived Permission**

> **Context Termination Should Terminate Context-Derived Permissions Unless Another Legitimate Basis Persists**

> **Ownership ≠ Unlimited Contextual Sovereignty**

> **Emergency Need ≠ Unlimited Emergency Authority**

> **Universal Permission Grammar ≠ Universal Permission Outcome**

> **Rule Content ≠ Rule Source**

> **Physical Capability ≠ Normative Permission ≠ Actual Behaviour**

---

## 53. Minimum Necessary Permission Principle

The strongest candidate principle emerging from this paper is:

> **Where a legitimate function requires access to a space, resource, participant or capability, the resulting permission should normally extend only as far as reasonably necessary to perform that function, remain subject to higher-order rights and applicable rules, and terminate when the function or other legitimate basis for the permission ends.**

Short form:

> **Function → Need → Minimum Necessary Permission**

---

## 54. Failure Modes

The architecture should be tested against at least:

1. excessive permission bureaucracy;
2. ambiguous implied permission;
3. conflicting cultural assumptions;
4. deceptive consent;
5. unclear property boundaries;
6. unclear contextual boundaries;
7. permission creep;
8. emergency-authority creep;
9. ownership treated as sovereignty;
10. parental responsibility treated as unlimited authority;
11. child safeguarding failures;
12. hidden surveillance;
13. discrimination through selective access;
14. inaccessible signage;
15. digital dark patterns;
16. machine-readable rules diverging from human-readable rules;
17. overlapping context conflicts;
18. unclear precedence;
19. inability to withdraw;
20. coercive dependency;
21. excessive fragmentation;
22. context state being incorrectly inferred;
23. unauthorised delegation;
24. stale permissions;
25. permissions surviving after their legitimate function ends.

---

## 55. Falsification

The architecture should be weakened or rejected if testing shows that contextual permission cannot be represented without impractical complexity; implied permission is too culturally variable for useful common grammar; ordinary people cannot understand the model; formalisation systematically reduces rather than improves autonomy; nested permissions create irresolvable ambiguity; minimum necessary permission produces unacceptable uncertainty; contextual rules are better handled entirely through existing domain-specific systems; or the architecture encourages excessive control over ordinary social behaviour.

The objective is not to force all human interaction into the model. The objective is to determine whether a common underlying grammar genuinely exists.

---

## 56. Relationship to Fractal Contextual Wrappers

Fractal Contextual Wrappers established:

> **What changes when a participant enters or operates within a bounded context?**

Fractal Permission Architecture asks:

> **Given that context, who may do what, where, why, when and under what legitimate basis?**

The contextual wrapper describes the environment. The permission architecture describes relationships and permitted actions within and across that environment.

---

## 57. Wider Concord Significance

The same pattern now appears at radically different scales.

A government may receive authority because a legitimate function requires it. A neighbouring authority may receive interoperability access because a shared function requires it. A delivery worker may enter part of a property because a delivery function requires it. An emergency responder may cross a normally protected boundary because an emergency function requires it.

The scale changes. The structural question remains:

> **What function is legitimate, what capability does it genuinely require, and what is the minimum permission or authority necessary to perform it?**

This may represent a deeper Concord architectural symmetry.

---

## 58. Conclusion

The residential home reveals that civil space is substantially more complex than a map of public, private and Safe Spaces.

A front garden can be private while remaining conditionally accessible. A path may be traversable without being generally usable. A visitor may approach without being permitted to enter. A delivery worker may possess a function-specific permission unavailable to another stranger. A family member may possess relationship-derived permissions. A bedroom may create a nested privacy context. A bathroom may dynamically become a Safe Space when occupied. An emergency may temporarily alter that permission structure.

The result is not a simple hierarchy of increasingly private physical spaces.

It is a **fractal, contextual and dynamic permission topology**.

The central finding is:

> **A space does not possess a single access state. Effective permission emerges from the interaction between the space, participant, role, relationship, legitimate function, explicit or implied permission, applicable rules, current state and wider context.**

And the central mechanism is:

> **Legitimate Function → Required Interaction → Minimum Necessary Permission → Context-Bounded Access → Function Completion → Permission Termination**

This suggests that Concord may be able to provide a common grammar for a vast range of everyday civil interactions without attempting to enumerate every possible situation in advance.

The goal is not universal restriction.

It is universal **legibility of legitimate difference**.

In its shortest form:

> **Who. What. Where. Why. When. Under what legitimate basis. With no more permission than the function requires.**