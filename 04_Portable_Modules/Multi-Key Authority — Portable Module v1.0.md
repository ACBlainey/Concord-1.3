# Multi-Key Authority — Portable Module v1.0

**Version:** 1.0  
**Status:** GRADUATED PORTABLE MODULE / CLEAN-TRANSFER VALIDATED / NON-CANONICAL  
**Origin:** Extracted from the Concord Multi-Key Authority development programme  
**Date:** 3 October 2026  
**Embedded layer:** Authority-Space Completeness Problem (ASCP), an ESCP-derived authority-completeness layer

# 1. Purpose

Multi-Key Authority (MKA) is a portable authority-composition and verification kernel for consequential acts that cross more than one independently protected authority boundary.

It addresses a specific failure mode:

> **Authority Does Not Automatically Compose.**

A person, institution, software agent or mixed system may possess several individually legitimate authorities while still lacking authority for the actual combined act, route or consequence.

MKA exists to test that seam without becoming the source of the authority it verifies.

# 2. Portable problem

> **How can a system determine whether every independently necessary authority for an actual consequential act and route is represented, legitimately grounded, current, within scope, composable where required, and not blocked by an applicable prohibition?**

MKA is not a universal governance system.

It is a small shared kernel between externally owned authority sources, externally owned contextual/domain state and a consequential act that would rely upon them.

# 3. Core rule

> **A consequential act may proceed only where every independently necessary authority for the actual route, context and consequence is represented to a proportionate completeness standard, independently legitimate, current, within scope, validly composable where composition is required, and not blocked by an applicable upstream prohibition.**

This is a bounded authorisation claim.

It is not a claim of omniscience, outcome correctness or general sovereignty.

# 4. Foundational separations

> **Capability != Permission != Authority**

> **Authority Verification != Authority Creation**

> **Authority Verifier != Authority Source**

> **Authority(A) + Authority(B) != Authority(C) Without Legitimate Composition**

> **All Represented Keys Valid != All Required Keys Represented**

> **Authority At Proposal != Authority At Commit**

> **Technical Reachability != Authority**

> **Beneficial Outcome != Authority**

> **Transition Need != Authority**

> **Context Membership != Authority**

> **Credential Possession != Authority**

> **Registry State != Authority Itself**

# 5. Permission-before-authority gate

Before invoking consequential authority, ask:

> **Can the objective be satisfied through legitimate bounded permission or ordinary liberty rather than coercive or institutional authority?**

If yes:

`PERMISSION_SUFFICIENT`

MKA should not manufacture an authority problem.

> **Permission-Sufficient Action != Authority Problem**

# 6. Actual act and route

MKA evaluates the actual proposed act, not merely the desired objective.

At minimum distinguish:

`<Objective, Act, Route, Target, Context, Consequence>`

> **Same Objective != Same Authority Path**

> **Same Physical Act != Same Authority Requirement**

A route change can change the required authority set.

# 7. Materiality gate

MKA should remain lightweight.

Use it where:

1. a material consequential act is proposed;
2. ordinary permission is insufficient;
3. one or more authority dimensions are required; and
4. composition, scope, freshness, route, protected boundary or prohibition is material.

> **Action Granularity != Authority Granularity**

> **Technical Dependency != Authority Dimension By Default**

Do not create a separate authority key for every technical micro-action.

# 8. Embedded ASCP

Before validating represented authority keys, MKA asks whether the authority space itself is sufficiently represented.

Core:

> **All Represented Keys Valid != All Required Keys Represented**

ASCP asks:

> **What authority would have to be required, missing or unrepresented for the conclusion “this action is authorised” to be wrong?**

Candidate prompts include:

- What protected context does the route cross?
- What participant or resource is materially affected beyond the represented target?
- Does the mechanism require an intervention not represented by the objective?
- Does an upstream prohibition apply?
- Has a relevant fact changed?
- Is one authority merely making another protected boundary technically reachable?
- Is prior authority being treated as continuing authority?
- Is authority being inferred from ownership, access, capability, possession, credential or role?
- Is a new authority being created by composition?
- Is a third party materially affected?

# 9. ASCP stopping rule

> **Authority-space review is sufficiently resolved when the proposed act, route, affected protected contexts/functions and reasonably discoverable material consequences have been mapped to applicable authority interfaces, no material unresolved authority dimension remains identified, and residual uncertainty is proportionate to consequence and decision horizon.**

Therefore:

> **Authority Completeness != Proof Of Omniscience**

> **Complete Within Scope != Universally Complete**

# 10. Authority-space states

Portable common states:

- `COMPLETE_WITHIN_DECLARED_SCOPE`
- `INCOMPLETE_KNOWN_GAP`
- `UNKNOWN_MATERIAL_DIMENSION`
- `DISPUTED_AUTHORITY_DIMENSION`
- `NOT_APPLICABLE_NO_AUTHORITY_REQUIRED`
- `REVIEW_DUE_STALE`

A host may map these to richer local states.

# 11. Required authority dimension

A key enters the required set where it represents a materially independent protected authority boundary required by the actual act.

Conceptually:

`IndependentAuthorityDimension(K) = MaterialProtectedBoundary(K) AND RequiredByActualAct(K)`

A technical dependency alone does not create an independent authority dimension.

# 12. Authority source

Every required key must reference an independently legitimate source supplied by the adopting environment.

Sources may include, where recognised by that environment:

- consent;
- ownership or stewardship;
- contract;
- delegated institutional authority;
- law;
- constitutional authority;
- emergency authority;
- another legitimate source.

> **AuthorityBasis Must Pre-Exist MKA Verification Or Arise Through A Separately Legitimate Authority-Creation Process**

MKA is not that authority-creation process.

# 13. Authority evidence

Evidence can show that an AuthorityBasis exists and applies.

But:

> **AuthorityEvidence != Authority**

> **Credential != Authority**

> **Registry Entry != Authority**

Machine readability does not create legitimacy.

# 14. Authority-key reference

Portable reference:

`AuthorityKeyRef = <`

`KeyRef,`
`RequiredFunction,`
`AuthorityBasisRef,`
`EvidenceRef,`
`HolderOrResolverRef,`
`Scope,`
`Context,`
`ValidityWindow,`
`PredicateRefs,`
`RevocationOrTerminationState,`
`CompositionRuleRef,`
`IndependenceClass,`
`Provenance`

`>`

The substantive authority remains externally owned.

# 15. Key validity

For each required key, test as applicable:

- legitimate source;
- subject/holder;
- function;
- target;
- purpose;
- scope;
- context;
- temporal validity;
- current predicates;
- revocation/termination;
- independence requirements;
- provenance.

A genuine authority can still be unusable for the proposed act because it is out of scope.

# 16. Scope

> **Valid Authority Outside Required Scope != Authority For This Act**

Scope may include:

- function;
- target;
- participant;
- resource;
- context;
- route;
- purpose;
- time;
- jurisdiction;
- consequence class.

The host determines which dimensions are substantively relevant.

# 17. Composition

Where an act requires several authorities:

> **Each authority must remain independently grounded unless a legitimate source explicitly establishes the required composition or inheritance relation.**

Therefore:

> **Authority(A) + Authority(B) != Authority(C) Without Legitimate Composition**

MKA must not manufacture bridging authority because individually valid parts appear useful together.

# 18. Inheritance and delegation

Authority can legitimately inherit or delegate across roles, contexts, succession structures or parent/child functions where a legitimate basis establishes that relation.

> **Parent Authority != Child Authority By Default**

> **No Automatic Inheritance != No Possible Inheritance**

> **Delegation != Authority Multiplication**

> **Delegated Authority Cannot Exceed Legitimate Delegation Capacity**

# 19. Required independence

Some authority functions may need independent holders or independent assessment.

MKA can represent an `IndependenceRequirement`.

It does not decide every domain's separation-of-powers rule.

> **Multiple Authority Functions != Automatic Multiple Human Decision-Makers**

One legitimate instrument can satisfy several functions where its scope explicitly covers them.

# 20. Prohibitions

Positive authority is insufficient where an applicable upstream prohibition blocks the act.

> **Positive-Key Completeness != Complete Authority Space**

Portable check:

`NO_APPLICABLE_UPSTREAM_PROHIBITION`

MKA consumes prohibition scope, precedence, exceptions and override rules from legitimate external owners.

# 21. Current predicates and rapid verification

Some authority exists only while factual predicates hold.

Examples may include:

- an emergency remains active;
- consent remains current;
- a role remains active;
- a resource state persists;
- a danger remains imminent;
- a validity window remains open.

> **Precompute the authority rule; verify the current facts.**

Time-critical verification does not imply fresh committee approval.

> **Rapid Verification != Multi-Committee Approval**

# 22. Emergency

Emergency can change which authority applies.

But:

> **Emergency != Authority Vacuum**

> **Emergency Need != Unlimited Emergency Authority**

> **Urgency != Authority**

A valid emergency authority requires an independently legitimate source and bounded activation conditions.

Urgency may compress procedure without manufacturing substantive authority.

# 23. Proposal and consequential commit

Where material facts or authority can change between proposal and consequence:

> **Authority must be revalidated at consequential commit to the degree required by the risk and host architecture.**

> **Authority At Proposal != Authority At Commit**

Reopen MKA/ASCP when there is a material change in:

`<Act, Route, Target, Context, Consequence, Time, AuthoritySource, ProtectedInterface>`

# 24. Portable action contract

`MKAAction = <`

`ActionRef,`
`DeclaredScope,`
`RouteRef,`
`TargetRefs,`
`ContextRefs,`
`ConsequenceClass,`
`ASCPStateRef,`
`RequiredAuthorityRefs,`
`AuthorityBasisRefs,`
`AuthorityEvidenceRefs,`
`CompositionRules,`
`IndependenceRequirements,`
`CurrentPredicateRefs,`
`ProhibitionRefs,`
`FreshnessState,`
`CommitConditions,`
`ReviewOrResolverRef,`
`Provenance`

`>`

Fields are materially optional where inapplicable.

> **Presence Of A Field != Requirement That Every Action Populate It**

# 25. Portable result contract

`MKAResult = <`

`ActionRef,`
`DeclaredScope,`
`AuthorityCompletenessState,`
`AuthorityValidityState,`
`CompositionState,`
`ProhibitionState,`
`FreshnessState,`
`CommitDecision,`
`ExternalOwnerRef,`
`UnresolvedRefs,`
`ReviewTrigger,`
`Provenance`

`>`

# 26. Common result vocabulary

Portable common states:

- `PERMISSION_SUFFICIENT`
- `AUTHORISED_WITHIN_SCOPE`
- `HOLD_MISSING_AUTHORITY`
- `HOLD_UNKNOWN_AUTHORITY`
- `HOLD_DISPUTED_AUTHORITY`
- `BLOCK_INVALID_AUTHORITY`
- `BLOCK_OUT_OF_SCOPE`
- `BLOCK_PROHIBITED`
- `REVALIDATION_REQUIRED`
- `REROUTE_AVAILABLE`
- `EXPIRED`
- `EXTERNAL_OWNER_REQUIRED`
- `OUTSIDE_MKA_SCOPE`

The last two are interface/routing states, not authority sources or substantive decisions.

`EXTERNAL_OWNER_REQUIRED` means an unresolved question belongs to an identified external architecture or domain owner and MKA should hand off rather than absorb that function.

`OUTSIDE_MKA_SCOPE` means the requested decision is not an MKA-owned function.

These two states were added at v1.0 graduation as a non-semantic interface clarification identified during clean blind transfer. They do not change the authority logic tested by the frozen candidate.

# 27. Rerouting

Failure of one route does not imply that the objective is forbidden.

> **Blocked Route != Forbidden Objective By Default**

Where a legitimate lower-authority or permission-sufficient route exists, MKA may return:

`REROUTE_AVAILABLE`

The rerouted act must be evaluated on its actual route.

# 28. Unknown and disputed authority

Unknown authority state must not silently become authorised or prohibited.

Disputed authority must not make MKA the adjudicator.

> **Dispute Detection != Authority To Resolve Dispute**

Where supplied, preserve a `ReviewOrResolverRef`.

# 29. External-owner handoff

MKA must not absorb a missing function merely because that function is required before action can proceed.

Examples:

- context/rule ownership;
- runtime configuration;
- transition completion;
- substantive legal interpretation;
- clinical validity;
- identity determination;
- resource allocation.

Where the owner is known:

`EXTERNAL_OWNER_REQUIRED`

Where the request itself is outside the kernel:

`OUTSIDE_MKA_SCOPE`

> **External Handoff != Authority Creation**

# 30. Registry neutrality

MKA may consume an authority registry.

But:

> **Authority Registry != Authority Source**

> **Registry Absence != Proof Authority Does Not Exist**

A portable implementation must permit other legitimate evidence methods.

# 31. Substrate neutrality

MKA may be implemented as:

- a human checklist;
- an institutional procedure;
- machine-readable policy;
- a verification service;
- a mixed human-machine process.

The architecture does not depend on a particular substrate, database, cryptographic system, legal tradition or software stack.

# 32. Provenance

For material decisions preserve enough provenance to reconstruct:

- proposed act;
- route;
- authority set considered;
- completeness state;
- key validation;
- composition/inheritance;
- prohibitions;
- predicates;
- commit state;
- external handoff;
- unresolved issues;
- decision time;
- later material discoveries.

Provenance does not create legitimacy.

# 33. Review and correction

If a missing authority dimension is discovered later:

- preserve the original decision state;
- identify the omitted interface;
- update the authority map/schema;
- test similar routes;
- provide remedy/review where applicable;
- do not silently rewrite prior provenance.

> **Unforeseeable Missing Dimension != Proof Of Prior Bad Faith**

# 34. Termination

For an individual proposal MKA terminates when:

- permission is sufficient;
- the act is committed within valid authority;
- the act is abandoned;
- the act is blocked;
- the proposal expires;
- the route is replaced;
- the unresolved function is handed to its legitimate external owner/resolver.

Standing authority requires freshness/reopening according to host rules.

# 35. Integration boundary — ESCP

MKA does not replace general ESCP.

ASCP imports ESCP's completeness discipline into authority-space analysis.

MKA does not own general epistemology, scientific model completeness or omitted-variable analysis outside authority.

# 36. Integration boundary — CWA

MKA does not own:

- context creation;
- full context schema;
- contextual nesting;
- access-control topology;
- contextual rule authoring;
- universal precedence.

It consumes externally owned context/protected-interface references.

# 37. Integration boundary — CBPR

MKA does not own:

- compute;
- storage;
- tools;
- network;
- credential custody;
- scheduler;
- checkpoints;
- runtime recovery;
- participant-runtime lifecycle.

CBPR or another runtime may consume MKA results at consequential commit.

# 38. Integration boundary — BTA

MKA does not own:

- transition identity;
- partial crossing;
- multi-owner transition state;
- transition completion;
- rollback;
- recovery;
- residual transition state.

BTA or another transition architecture may preserve MKA authority references/results.

# 39. Integration boundary — substantive authority

MKA does not define:

- constitutional law;
- criminal law;
- clinical standards;
- property law;
- emergency doctrine;
- consent doctrine;
- personhood;
- participant standing;
- jurisdiction;
- professional competence.

Those are host/domain responsibilities.

# 40. Outcome boundary

MKA answers whether authority for an act exists within declared scope.

It does not determine whether the act is wise, optimal, successful or preferable to another authorised option.

> **Authorised != Recommended**

> **Authorised != Guaranteed Correct Outcome**

# 41. Core failure modes

Implementations must resist:

1. single-key collapse;
2. automatic key accumulation/composition;
3. missing-key blindness;
4. scope laundering;
5. parent-child inheritance leap;
6. stage inheritance;
7. capability-to-authority conversion;
8. permission-to-general-authority conversion;
9. credential-to-authority conversion;
10. registry-to-authority conversion;
11. transition-to-authority conversion;
12. emergency-to-unlimited-authority conversion;
13. benefit-to-authority conversion;
14. proposal-time staleness;
15. prohibition blindness;
16. route blindness;
17. third-party blindness;
18. resolver capture;
19. omniscience claims;
20. bureaucratic key explosion;
21. external-owner absorption.

# 42. Core invariants

MKA-01 **Authority Does Not Automatically Compose.**  
MKA-02 **Authority Verification != Authority Creation.**  
MKA-03 **Authority Verifier != Authority Source.**  
MKA-04 **All Represented Keys Valid != All Required Keys Represented.**  
MKA-05 **Capability != Permission != Authority.**  
MKA-06 **Same Objective != Same Authority Path.**  
MKA-07 **Authority(A) + Authority(B) != Authority(C) Without Legitimate Composition.**  
MKA-08 **Parent Authority != Child Authority By Default.**  
MKA-09 **No Automatic Inheritance != No Possible Inheritance.**  
MKA-10 **Valid Authority Outside Required Scope != Authority For This Act.**  
MKA-11 **Positive-Key Completeness != Complete Authority Space.**  
MKA-12 **Emergency != Authority Vacuum.**  
MKA-13 **Urgency != Authority.**  
MKA-14 **Rapid Verification != Multi-Committee Approval.**  
MKA-15 **Authority At Proposal != Authority At Commit.**  
MKA-16 **Technical Reachability != Authority.**  
MKA-17 **Credential != Authority.**  
MKA-18 **Registry State != Authority Itself.**  
MKA-19 **Transition Need != Authority.**  
MKA-20 **Beneficial Outcome != Authority.**  
MKA-21 **Dispute Detection != Authority To Resolve Dispute.**  
MKA-22 **Authority Completeness != Proof Of Omniscience.**  
MKA-23 **Complete Within Scope != Universally Complete.**  
MKA-24 **Permission-Sufficient Action != Authority Problem.**  
MKA-25 **Action Granularity != Authority Granularity.**  
MKA-26 **Technical Dependency != Authority Dimension By Default.**  
MKA-27 **Blocked Route != Forbidden Objective By Default.**  
MKA-28 **Authorised != Recommended.**  
MKA-29 **Authorised != Guaranteed Correct Outcome.**  
MKA-30 **Precompute Authority Rule; Verify Current Facts.**  
MKA-31 **External Handoff != Authority Creation.**

# 43. Adoption test

A non-Concord adopter should be able to answer:

- What actual act and route are proposed?
- Is ordinary permission sufficient?
- Which materially independent authority dimensions are required?
- Could a required authority dimension be missing from the represented space?
- What legitimate source grounds each authority?
- Is each authority current and in scope?
- Do multiple authorities legitimately compose?
- Does authority legitimately inherit or delegate?
- Is an independence requirement applicable?
- Is an upstream prohibition active?
- Which predicates must still hold at commit?
- Has the route/context/consequence materially changed?
- Is an unresolved issue MKA-owned or externally owned?
- Can the objective be legitimately rerouted?
- What provenance permits later reconstruction?

If these cannot be answered for a material consequential act, authority should not be inferred merely from capability, convenience or possession of credentials.

# 44. Portability boundary

This module deliberately leaves substantive legitimacy to the adopting environment.

It does not decide who ought to possess authority.

It requires that consequential authority be independently grounded, materially complete within declared scope, current, appropriately scoped and legitimately composed rather than inferred from technical capability or from individually valid fragments.

This is the portable boundary:

> **MKA verifies authority composition; it does not manufacture authority.**

# 45. Concord provenance and interfaces

MKA was extracted from Concord cross-domain development.

Developmental provenance remains outside this portable module.

Primary provenance:

- `03_Cross_Domain_Architecture/Multi-Key Authority and Rapid Authority Verification — Cross-Domain Source Resolution 001.md`
- `03_Cross_Domain_Architecture/Multi-Key Authority — Cross-Domain Adversarial Test 001.md`
- `03_Cross_Domain_Architecture/Authority-Space Completeness Problem — Development Note 001.md`
- `03_Cross_Domain_Architecture/MKA - ASCP - ESCP - CBPR - CWA - BTA — Composition and Non-Duplication Audit 001.md`
- `03_Cross_Domain_Architecture/MKA Portable Kernel Candidate — Extraction Boundary 001.md`
- `03_Cross_Domain_Architecture/MKA Portable Kernel Candidate — Frozen Kernel 001.md`
- `03_Cross_Domain_Architecture/MKA Blind Transfer Test 001 — Test Brief.md`
- `03_Cross_Domain_Architecture/MKA Blind Transfer Test 001 — Scenario Pack.md`
- `03_Cross_Domain_Architecture/MKA Blind Transfer Test 001 — PMEDG and CRADP Assessment.md`
- `03_Cross_Domain_Architecture/MKA — PMEDG Graduation Review 001.md`

Conceptual interfaces:

| Interface | Function retained outside MKA |
|---|---|
| ESCP | general evaluation-space completeness |
| CWA | context, permission, rule and authority topology |
| CBPR | bounded runtime execution |
| BTA | transition coherence |
| host/domain authority sources | substantive legitimacy and authority creation |
| legitimate resolver/adjudicator | resolution of disputed authority |
| provenance/archive owner | long-term custody of records |

> **The portable module does not remove or replace these systems.**

# 46. Validation status

Development evidence includes:

- cross-domain source resolution;
- 90-scenario cross-domain adversarial testing;
- formal non-duplication/composition audit;
- frozen extraction boundary;
- clean blind transfer across 30 scenarios;
- explicit falsification testing;
- PMEDG/CRADP assessment;
- PMEDG graduation review.

The clean blind evaluator returned:

**TRANSFER VALIDATED WITH NON-BLOCKING CLARIFICATIONS**

No falsification success requiring revision of the frozen authority semantics was identified.

The interface states `EXTERNAL_OWNER_REQUIRED` and `OUTSIDE_MKA_SCOPE` were added at graduation to make already-correct external handoff behaviour explicit.

**Current status: GRADUATED PORTABLE MODULE v1.0 / CLEAN-TRANSFER VALIDATED / NON-CANONICAL.**

# 47. Release basis

PMEDG Graduation Review 001 approved extraction as Portable Module v1.0.

ASCP remains embedded as MKA's ESCP-derived authority-completeness layer.

Future maturation may include:

- regression testing of external-owner handoff;
- machine-readable authority-registry implementation testing;
- live MKA + CWA + CBPR + BTA composition testing;
- high-speed emergency verification;
- complex delegation/inheritance graphs;
- batch-action exception testing.

These are maturation activities and do not alter the v1.0 release basis.
