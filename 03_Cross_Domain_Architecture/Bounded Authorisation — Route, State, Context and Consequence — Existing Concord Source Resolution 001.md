# Bounded Authorisation — Route, State, Context and Consequence — Existing Concord Source Resolution 001

**Project:** The Concord Framework  
**Date:** 3 October 2026  
**Status:** SOURCE RESOLUTION / STRONG REDISCOVERY / UNIFYING INVARIANT / NON-CANONICAL  
**Trigger:** Execution Envelope Reconciliation Pattern — Adversarial Integration Test 001  
**Primary sources:** Multi-Key Authority (MKA), Concord Bounded Participant Runtime (CBPR), Contextual Wrapper Architecture (CWA), Bounded Transition Architecture (BTA)  
**Related integration patterns:** BRSP, EERP

## 1. Question

Recent RGCP → BRSP → CBPR → EERP integration work exposed the following apparent principle:

> **Authorisation should be treated as a bounded, state-dependent claim about a specified route and consequence, not as a durable label attached to an objective or actor.**

Is this a genuinely new Concord principle, or is it already present in the existing bounded-authority architecture?

## 2. Result

**STRONG REDISCOVERY.**

The principle is already deeply encoded across multiple independently developed/graduated Concord architectures.

It should **not** be extracted as a new portable module or new constitutional principle.

The useful contribution of this source resolution is to identify a common invariant already expressed through:

- MKA act/route/context/consequence binding;
- MKA scope/current-predicate/commit revalidation;
- CBPR Action Grants and commit-time revalidation;
- CBPR non-expansion through repeated use;
- CWA contextual permission and authority termination;
- CWA function/time/context binding;
- BTA non-propagation of authority through continuity or transition.

The common form can be stated:

> **Authorisation Is A Bounded Relation, Not A Durable Actor Property.**

More precisely:

> **An authorisation claim is valid only to the scope in which its legitimate basis applies, including the relevant actor/holder, act or function, route where material, target, context, consequence, time/current predicates and applicable composition/prohibition state.**

This is a synthesis of existing rules, not a new source of authority.

## 3. MKA already establishes route-bound authority

MKA states that a person, institution, software agent or mixed system may possess individually legitimate authorities while still lacking authority for the actual combined act, route or consequence.

Its core rule is:

> **A consequential act may proceed only where every independently necessary authority for the actual route, context and consequence is represented to a proportionate completeness standard, independently legitimate, current, within scope, validly composable where composition is required, and not blocked by an applicable upstream prohibition.**

MKA evaluates:

`<Objective, Act, Route, Target, Context, Consequence>`

and states:

> **Same Objective != Same Authority Path**

> **Valid Authority Outside Required Scope != Authority For This Act**

> **Authority At Proposal != Authority At Commit**

Therefore authority is already represented as a relation between a legitimate basis and a bounded actual act.

It is not an unqualified property of the holder.

## 4. MKA already establishes state-dependent authority

MKA key validity includes:

- holder/subject;
- scope;
- context;
- temporal validity;
- current predicates;
- revocation/termination.

Examples of current predicates include:

- consent remains current;
- required resource state persists;
- validity window remains open.

MKA therefore establishes:

> **Precompute The Authority Rule; Verify The Current Facts.**

The authority rule may persist while the factual state required to exercise it changes.

Thus:

> **Persistent Authority Rule != Continuously Satisfied Authority Predicates**

## 5. MKA already establishes route replacement

MKA states:

> **Blocked Route != Forbidden Objective By Default**

and requires a rerouted act to be evaluated on its actual route.

For an individual proposal, MKA can terminate when the route is replaced.

Therefore:

> **Authority For Route A != Authority For Route B By Default**

even where both routes serve the same objective.

## 6. CBPR already establishes operation/consequence binding

CBPR Action Grants bind an AuthorityBasis to explicit dimensions such as:

- operation;
- target;
- consequence;
- credential;
- resource;
- frequency/duration;
- affected-population scope.

CBPR states:

> **Grant Record != Source Of Legitimacy**

> **Repeated Use Does Not Enlarge A Grant**

and:

> **Material Scope Expansion Requires A New Or Explicitly Reauthorised Grant**

This directly rejects the idea that successful or repeated exercise turns bounded authority into a durable general entitlement.

## 7. CBPR already establishes commit-time state dependence

CBPR requires current state to be revalidated immediately before material commit, including:

- credential validity/revocation;
- action grant;
- effective target;
- output consequence;
- terms/policy;
- service relationship;
- temporal validity;
- dependency/safety state;
- required approval/authority;
- composition state.

It explicitly states:

> **Previously Valid Proposal State Does Not Freeze Authority.**

and:

> **Authority At Proposal != Authority At Commit**

Therefore historical authorisation is not a permanent property carried by the action or actor.

## 8. CBPR already rejects continuity-based authority

CBPR states:

> **Recovered State != Recovered Authority**

and:

> **Function Continuity != Authority Continuity**

A successor host possessing infrastructure, records or runtime state does not thereby possess predecessor authority.

Therefore:

> **Technical Continuity != Authority Continuity**

## 9. CWA already establishes context-bound permission

CWA states:

> **Contextual Permission != General Permission**

Permission valid in one context does not automatically survive outside it.

It also states:

> **Presence In Context != Possession Of Every Contextual Permission**

and represents precise contextual permission in a form such as:

> **Participant P may perform Action A in Context/Space S for Function F under Conditions C during Time T on Legitimate Basis B.**

This is already a strongly relational representation.

## 10. CWA already establishes function-bound permission

CWA states:

> **Permission For One Function != Permission For Unrelated Functions**

> **Permission To Use != Authority To Control**

> **A Permitted Route For One Function Does Not Create A General Right Of Passage**

Function-derived permission normally terminates when its justifying function completes.

Therefore:

> **Permission Exercise != Permission Expansion**

## 11. CWA already establishes context-bound authority

CWA's authority pattern is:

**Contextual Function / Problem**
→ **Need For Local Authority**
→ **Minimum Necessary Authority**
→ **Role-Bounded Authority**
→ **Context-Bounded Authority**
→ **Authority Terminates When Its Justifying Function / Context Ends**

It states:

> **Contextual Authority Should Not Escape Its Context Without Independent Justification.**

This is the same bounded-authorisation invariant expressed through context topology.

## 12. CWA already rejects automatic inheritance

CWA states:

> **Nested Context != Inherited Rule Set**

and:

> **Nesting Alone Does Not Determine Rule Inheritance.**

Where inheritance exists, it must arise from an established contextual relationship.

Thus authority/permission cannot be inferred merely from topology, containment or reachability.

## 13. BTA already rejects transition-based authority propagation

BTA states:

> **Do Not Infer Transfer Of Consequential Authority, Consent, Rights, Identity Or Liability Merely From Object Continuity.**

Its non-propagation architecture exists precisely because movement/transition of an object or function does not automatically move every attached consequential attribute.

Therefore:

> **Object/Function Transition != Authority Transition**

## 14. BTA already preserves authority termination separately

BTA may preserve externally supplied terminated-authority references but does not itself terminate authority.

It also recognises that:

> **End Of Authority != Automatic End Of Responsibility**

This is important because bounded authorisation must not be confused with bounded consequence or bounded duty.

Authority may end while residual obligations continue.

## 15. Unified authorisation relation

The common architecture can be represented conceptually as:

`AuthorisationClaim = <BasisRef, HolderRef, ActOrFunction, RouteRef?, TargetRef?, ContextRef?, ConsequenceClass?, Scope, TimeOrValidityWindow?, CurrentPredicateRefs?, CompositionRefs?, ProhibitionState?, RevocationOrTerminationState?, Provenance>`

Question marks indicate dimensions that are materially conditional rather than universally mandatory.

The representation is explanatory.

It does not replace MKA's own schema or create a new canonical object.

## 16. The actor-property fallacy

A recurring failure pattern can now be named:

### Actor-property fallacy

> Because actor X was legitimately authorised to perform consequential act A under conditions C, X is treated as generally “authorised” for related acts, routes, contexts or future states.

This inference is invalid unless a legitimate authority basis actually has that broader scope.

Compactly:

> **Authorised(X,A,C) != GenerallyAuthorised(X)**

This applies equally to:

- humans;
- AI participants;
- institutions;
- services;
- offices;
- credentials;
- roles;
- runtimes.

## 17. The objective-property fallacy

A parallel failure is:

> Because objective O was legitimate or previously approved, any route serving O is treated as authorised.

MKA already rejects this:

> **Same Objective != Same Authority Path**

Therefore:

> **Legitimate Objective != Authority For Every Means**

## 18. The historical-authorisation fallacy

Another failure is:

> Because authority existed earlier, it is presumed to continue.

Existing modules reject this through freshness, temporal validity, current predicates, termination and commit-time revalidation.

Therefore:

> **Prior Authority != Current Authority By Default**

This aligns with the existing policing lifecycle rule:

> **Prior Authority != Continuing Authority**

The same structural logic appears across domains.

## 19. The possession fallacy

Authority must not be inferred from possession of:

- credential;
- capability;
- infrastructure;
- registry state;
- access;
- role label;
- prior execution state.

Existing rules include:

> **Capability != Permission != Authority**

> **Credential Possession != Authority**

> **Registry State != Authority Itself**

> **Function Continuity != Authority Continuity**

Thus:

> **Possession Of Authority-Relevant Artefact != Authority**

## 20. The successful-use fallacy

A successful prior use does not enlarge scope.

CBPR already states repeated use does not enlarge a grant.

Therefore:

> **Successful Exercise Of Authority != Expansion Of Authority**

Likewise:

> **Absence Of Prior Challenge != Proof Of Broader Authority**

The second statement is a source-compatible synthesis and should remain non-canonical unless separately developed.

## 21. Route/state/consequence boundedness

The recent BRSP/EERP work does not create this principle.

It reveals why the existing principle matters operationally.

### BRSP

Tests the actual proposed route against current externally owned constraints.

### CBPR

Revalidates the route/effect at consequential commit.

### EERP

Compares actual execution/effect against the commit-authorised envelope.

Thus the lifecycle is:

**Authority Basis**
→ **Bounded Route Evaluation**
→ **Current Commit Authorisation**
→ **Execution**
→ **Observed Consequence**
→ **Reconciliation/Review**

At no stage does authorisation become an unqualified durable actor label.

## 22. Continuous operations

The bounded relation does not imply that every continuing service requires a fresh human/institutional decision for every micro-action.

MKA already distinguishes precomputed authority rules from current factual verification.

CBPR supports continuous-within-bound activation.

Therefore:

> **Bounded Authorisation != Repeated Manual Reauthorisation**

A legitimate authority basis may support repeated or continuous operation where its scope explicitly does so and required current predicates remain satisfied.

## 23. Delegation and inheritance

The bounded relation also does not imply that authority can never be delegated or inherited.

MKA states:

> **No Automatic Inheritance != No Possible Inheritance**

Legitimate delegation/inheritance may exist where independently established.

Therefore:

> **Bounded Authorisation != Non-Delegable Authorisation**

The question remains whether the legitimate basis actually establishes the delegation/inheritance relation and scope.

## 24. Emergency authority

Emergency does not break the invariant.

An emergency may activate a different bounded authority relation.

MKA states:

> **Emergency != Authority Vacuum**

and:

> **Emergency Need != Unlimited Emergency Authority**

Therefore:

> **Emergency Activation != General Authority Expansion**

unless a legitimate external source specifically establishes the additional scope.

## 25. Relationship to participant standing

Bounded authorisation should not be confused with participant standing.

A participant may possess enduring standing while particular permissions/authorities remain contextual, functional and time/state bounded.

Therefore:

> **Participant Standing != Particular Action Authority**

and:

> **Termination Of Particular Authority != Termination Of Participant Standing**

This is consistent with the Concord's existing separation between standing, authority and protected relations.

## 26. Relationship to responsibility

Authority and responsibility can have different temporal boundaries.

BTA already recognises:

> **End Of Authority != Automatic End Of Responsibility**

Therefore a system must not infer:

> **Authority Ended -> Responsibility Ended**

Residual duties may persist after authority terminates.

## 27. Source-resolution classification

The apparent principle is not:

- a new Blainey's Law;
- a new constitutional right;
- a new authority source;
- a new portable module;
- a new cross-domain control layer.

It is best classified as:

**UNIFYING INVARIANT / SOURCE-RESOLVED SYNTHESIS OF EXISTING BOUNDED-AUTHORITY ARCHITECTURE**

## 28. Stable formulation

The strongest compact formulation supported by the existing architecture is:

> **Authorisation Is A Bounded Relation, Not A Durable Actor Property.**

Expanded:

> **Authority or permission for a consequential act exists only within the scope established by its legitimate basis and applicable current state. It does not automatically transfer across acts, routes, contexts, consequences, times, actors, transitions, repeated uses or successor systems.**

This formulation synthesises existing architecture; it does not itself grant, revoke or rank authority.

## 29. Supporting invariants

BA-01 **Authorisation Is A Bounded Relation, Not A Durable Actor Property.**

BA-02 **Same Objective != Same Authority Path.**

BA-03 **Valid Authority Outside Required Scope != Authority For This Act.**

BA-04 **Authority At Proposal != Authority At Commit.**

BA-05 **Prior Authority != Current Authority By Default.**

BA-06 **Authority For Route A != Authority For Route B By Default.**

BA-07 **Repeated Use != Expanded Grant Scope.**

BA-08 **Technical Continuity != Authority Continuity.**

BA-09 **Contextual Permission != General Permission.**

BA-10 **Permission Exercise != Permission Expansion.**

BA-11 **Object/Function Transition != Authority Transition.**

BA-12 **Legitimate Objective != Authority For Every Means.**

BA-13 **Possession Of Authority-Relevant Artefact != Authority.**

BA-14 **Successful Exercise Of Authority != Expansion Of Authority.**

BA-15 **Bounded Authorisation != Repeated Manual Reauthorisation.**

BA-16 **Bounded Authorisation != Non-Delegable Authorisation.**

BA-17 **Emergency Activation != General Authority Expansion.**

BA-18 **Participant Standing != Particular Action Authority.**

BA-19 **Termination Of Particular Authority != Termination Of Participant Standing.**

BA-20 **End Of Authority != Automatic End Of Responsibility.**

## 30. Architectural significance

The same bounded-authorisation grammar now appears independently in:

- general authority composition;
- runtime execution;
- contextual permissions;
- transition architecture;
- policing lifecycle;
- recent route synthesis;
- recent execution reconciliation.

This repeated convergence is evidence of architectural consistency.

It also explains why the recent integration chain closes coherently:

**RGCP**
→ preserve why review exists

**BRSP**
→ determine whether the actual route satisfies current owned constraints

**MKA/CWA/BTA**
→ preserve authority/context/transition semantics

**CBPR**
→ revalidate at consequential commit

**EERP**
→ compare execution/consequence against the bounded authorised envelope

**KCS/STRA**
→ reopen materially affected state when conditions change.

The feedback loop works because authorisation is not treated as a permanent label.

## 31. Extraction decision

**DO NOT EXTRACT.**

No new portable module is justified.

No PMEDG candidate is required for the invariant itself.

BRSP and EERP remain PMEDG candidates as integration patterns, but this bounded-authorisation finding is already a cross-source synthesis of mature existing architecture.

## 32. Recommended use

Use the invariant as:

- a source-resolution reference;
- an architectural audit question;
- a cross-domain consistency check;
- a design warning against authority laundering.

Suggested audit question:

> **What exact bounded relation authorises this act now, on this route, in this context, toward this target/consequence, and what material state change would cause that claim to require revalidation?**

If the answer is merely:

- “this actor is authorised”;
- “this system owns it”;
- “this objective was approved”;
- “the credential is valid”;
- “it worked before”;
- “the service is continuous”;

then the authority representation may be under-specified.

## 33. Result

**SOURCE RESOLUTION: STRONG REDISCOVERY**

The apparent new principle is already established structurally across the Concord.

Retain the synthesis:

> **Authorisation Is A Bounded Relation, Not A Durable Actor Property.**

Do not create a new module or constitutional rule from it.
