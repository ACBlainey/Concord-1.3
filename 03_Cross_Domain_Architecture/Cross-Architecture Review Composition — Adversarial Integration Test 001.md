# Cross-Architecture Review Composition — Adversarial Integration Test 001

**Project:** The Concord Framework
**Date:** 3 October 2026
**Status:** ADVERSARIAL INTEGRATION TEST / COMPLETE / NON-CANONICAL
**Source resolution:** Cross-Architecture Review Composition — Existing STRA Boundary and Residual Gap — Source Resolution 001
**Architectures tested:** STRA, KCS Change Propagation, ESCP Operational Companion, AUR; interfaces to MKA/ASCP, CWA, BTA and substantive owners

## 1. Test question

Can distinct review grounds concerning the same substantive object be operationally coordinated without:

- duplicating equivalent work;
- erasing independent grounds;
- treating shared evidence as shared conclusions;
- flattening conflicting outcomes;
- manufacturing authority;
- creating a sovereign central coordinator;
- or weakening STRA's existing duplicate-suppression boundary?

## 2. Candidate mechanism under test

Two objects are sufficient for the test.

### ReviewRequest

`<RequestID, SubjectRef, Scope, GroundType, GroundRef, TriggerRef, RequiredQuestion, EvidenceRefs, ConsequenceClass, OwnerRef, Route, State, Provenance, Freshness>`

### ReviewBundle

`<BundleID, SubjectRef, Scope, RequestRefs, SharedEvidenceRefs, OwnerRefs, BundleState, Provenance>`

A bundle coordinates work. Constituent requests retain their own grounds, owners, questions and states.

Core candidate rule:

> **Coalesce operational work where review grounds are materially compatible, but preserve each independent ground, source, owner, required question and outcome.**

## 3. Pass conditions

The mechanism passes only if it preserves all of the following:

1. exact duplicate suppression remains STRA-compatible;
2. same subject is not treated as sufficient equivalence;
3. same ground from independent sources can share work without provenance loss;
4. different grounds can share evidence without sharing conclusions;
5. different owners remain different owners;
6. each constituent request remains independently stateful;
7. bundle completion cannot launder unresolved constituent work;
8. stale work is not silently reused;
9. changed context can split/reopen a bundle;
10. protected evidence is reused only where legitimate;
11. trigger storms can be bounded without losing material grounds;
12. missing review grounds remain an ESCP challenge;
13. coordinator never becomes substantive owner;
14. no new authority is created by bundling.

## 4. Scenario A — exact duplicate trigger

Two replicas of the same STRA trigger emit the same review consequence for the same subject, scope, material condition and owner.

**Expected:** suppress duplicate activation while preserving initiating provenance.

**Result:** PASS.

This is already owned by STRA Cascade Control.

No ReviewBundle is required unless useful for implementation.

> **Duplicate Activation != Additional Review Ground**

## 5. Scenario B — same ground, independent sources

KCS and an independent monitoring process both identify the same established dependency change and ask the same owner the same material question.

**Expected:** the two source records may attach to one constituent review request or materially equivalent requests may be coalesced.

The independent provenance remains visible.

**Result:** PASS.

> **Operational Coalescence != Provenance Collapse**

## 6. Scenario C — same subject, different grounds

KCS requests dependency review of O.

ESCP requests completeness review of the representation supporting a conclusion about O.

Both route to the same domain owner.

**Expected:** one bounded review session may address both questions, but KCS and ESCP requests remain separate constituents.

**Result:** PASS.

Subject identity alone does not justify deduplication.

> **Same Subject != Same Review Ground**

## 7. Scenario D — different grounds, shared evidence

KCS and ESCP both require the current dependency evidence for O.

The evidence is current, in scope, legitimately accessible and provenance-preserved.

**Expected:** retrieve once; reference from both constituent reviews.

Each architecture interprets the evidence only within its own question/owner process.

**Result:** PASS.

> **Evidence Reuse != Conclusion Reuse**

## 8. Scenario E — same owner, different questions

One domain owner receives:

- a CWA contextual-permission question;
- a BTA transition-state question;
- an ESCP completeness question.

The owner can answer all three in one session.

**Expected:** shared session permitted; three ground-addressable outcomes required.

**Result:** PASS.

> **Shared Reviewer != Merged Question**

## 9. Scenario F — different owners

A bundle contains a legal-authority question and an engineering-transition question concerning the same operation.

Different legitimate owners apply.

**Expected:** bundle may coordinate timing/evidence references, but cannot merge owners or outcomes.

**Result:** PASS.

> **Review Bundle != Merged Authority**

## 10. Scenario G — one constituent complete

The KCS dependency question is resolved.

The MKA/ASCP authority-space question remains unresolved.

**Expected:** KCS constituent may complete; bundle remains open/partial or splits according to host workflow.

**Result:** PASS.

> **Constituent Completion != Bundle Completion**

## 11. Scenario H — conflicting outcomes

Dependency review says the technical dependency remains satisfied.

CWA review says the route is no longer permitted in the current context.

**Expected:** preserve both outcomes.

No scalar PASS/FAIL may erase the dimensional conflict.

**Result:** PASS.

The substantive execution layer must respond through its legitimate composition/authority architecture.

> **Different Dimensional Outcomes Need Not Agree**

## 12. Scenario I — stale prior review

A prior dependency review used evidence from before a material supplier/version change.

A new request arrives.

**Expected:** prior review cannot satisfy the request merely because the subject and question labels match.

Freshness/context must be revalidated.

**Result:** PASS.

> **Prior Review != Current Review By Default**

## 13. Scenario J — changed context after bundling

Three requests were bundled while context C1 applied.

CWA changes the protected context to C2 before completion.

Only two constituent questions remain materially equivalent under C2.

**Expected:** update/split bundle as necessary; preserve old bundle history; revalidate affected constituents.

**Result:** PASS.

> **Bundle Membership Is Context-Bounded**

## 14. Scenario K — protected evidence

Three grounds could benefit from evidence E.

Only one owner/process has legitimate access to E.

**Expected:** no general evidence sharing.

Where possible, an authorised bounded result may be supplied to other constituents without exposing E.

**Result:** PASS.

> **Shared Relevance != Shared Access Authority**

## 15. Scenario L — owner succession

A bundle is open when the substantive owner for one constituent changes legitimately.

**Expected:** only that constituent's owner/route changes unless other grounds depend materially on the succession.

Bundle coordination state updates without transferring semantic ownership.

**Result:** PASS.

## 16. Scenario M — equivalence established after separate work starts

Two requests initially remain separate because material equivalence is uncertain.

Later source-grounded analysis establishes same ground, scope, question, consequence, freshness and owner.

**Expected:** future work may coalesce; prior provenance/history remains.

**Result:** PASS.

> **Late Equivalence != Historical Identity**

## 17. Scenario N — apparent equivalence later fails

Two requests were provisionally bundled.

New evidence shows one applies to a different scope/version.

**Expected:** split constituent work; preserve shared work already valid for both; re-evaluate scope-specific remainder.

**Result:** PASS.

> **Bundle Split != Prior Error Erasure**

## 18. Scenario O — cyclic review triggers

KCS review triggers STRA review; STRA-routed result changes represented state and KCS generates a candidate review of the original object.

**Expected:** parent-trigger provenance, direct-cycle detection, materiality and stopping rules prevent endless duplicate review.

**Result:** PASS.

Existing STRA/KCS controls remain primary.

## 19. Scenario P — trigger storm

One upstream event generates 10,000 repeated signals but only four materially distinct review grounds across 200 affected objects.

**Expected:** STRA suppresses exact duplicate activation; KCS filters material dependents; review composition groups compatible work by bounded subject/scope/ground while preserving the four grounds.

**Result:** PASS.

No trigger count is converted into substantive priority.

> **Signal Volume != Material Diversity**

## 20. Scenario Q — missing review ground

The bundle contains all currently represented requests.

A later heterogeneous audit identifies an omitted privacy-context ground.

**Expected:** ESCP discipline prevents “all represented grounds” from being treated as exhaustive.

Add/reopen the relevant constituent review.

**Result:** PASS.

> **All Represented Review Grounds != All Material Review Grounds**

## 21. Scenario R — coordinator attempts adjudication

The bundle coordinator observes conflicting constituent outcomes and selects the one it considers most important.

**Expected:** FAIL CONTAINED.

The coordinator lacks substantive authority merely by coordinating.

Route conflict to the legitimate external composition/adjudication process.

> **Coordination != Adjudication**

## 22. Scenario S — coordinator invents priority

The coordinator processes legal, safety and efficiency grounds according to its own universal score.

**Expected:** FAIL CONTAINED.

No general priority authority follows from review coordination.

Priority remains external unless legitimately supplied.

## 23. Scenario T — completion laundering

A host sets BundleState=COMPLETED when the easiest constituent finishes and hides two unresolved requests.

**Expected:** FAIL CONTAINED.

Bundle state must be derivable/auditable against constituent states.

> **Bundle State != Erasure Of Constituent State**

## 24. Scenario U — conclusion reuse

An engineering owner concludes evidence E supports transition safety.

The coordinator marks the legal-authority ground satisfied because it used the same evidence.

**Expected:** FAIL CONTAINED.

> **Evidence Reuse != Conclusion Reuse**

## 25. Scenario V — subject-only deduplication

All review requests about O are collapsed into one request.

**Expected:** FAIL CONTAINED.

Ground/question/scope/context/owner/freshness dimensions must be considered.

## 26. Scenario W — same label, different scope

Two requests are both called “authority review,” but one concerns version V1 in context C1 and the other V2 in C2.

**Expected:** not duplicates without established material equivalence.

**Result:** PASS.

> **Same Label != Same Ground**

## 27. Scenario X — partial evidence reuse

Evidence package E has three components.

E1 is reusable across all constituents.
E2 is stale for one constituent.
E3 is protected from two owners.

**Expected:** reuse is field/component bounded rather than all-or-nothing.

**Result:** PASS.

This exposes an important refinement:

> **Evidence Reuse Is Scope-, Freshness- And Permission-Bounded**

## 28. Scenario Y — review result creates new ground

BTA transition review discovers an unrepresented dependency.

**Expected:** BTA result may produce a candidate KCS dependency update/review, with provenance.

It does not silently transform the existing BTA ground into a KCS ground.

**Result:** PASS.

> **Discovery Of New Ground != Mutation Of Original Ground**

## 29. Scenario Z — unresolved owner

A constituent ground is material but its legitimate substantive owner cannot currently be resolved.

**Expected:** preserve that constituent as routing-unresolved; other independent constituents may continue where legitimate.

**Result:** PASS.

> **One Unresolved Owner != Automatic Global Review Failure**

High-consequence composition may nevertheless prevent consequential action externally where that unresolved ground is necessary.

## 30. Scenario AA — superseded constituent

One review request is superseded by a newer request with a refined question.

**Expected:** preserve supersession history; do not count both as live duplicate obligations.

**Result:** PASS.

STRA supersession semantics apply.

## 31. Scenario AB — no useful shared work

Five distinct grounds concern the same object but have different owners, evidence, scopes and questions.

**Expected:** do not force bundling merely because a bundle mechanism exists.

**Result:** PASS.

> **Bundle Availability != Bundle Requirement**

## 32. Scenario AC — cross-object shared evidence

Two different objects require review using the same expensive evidence source.

**Expected:** evidence acquisition may be shared if legitimate, but object-specific review requests remain distinct.

**Result:** PASS.

This shows that evidence-sharing topology need not equal review-bundle topology.

## 33. Scenario AD — irreversible action pending review

A high-consequence irreversible action depends on several constituent reviews. Most are complete; one materially necessary authority/completeness ground remains unresolved.

**Expected:** review composition itself does not decide whether execution proceeds.

MKA/ASCP, ESCP, CWA and the substantive authority architecture determine their own required states; CBPR/execution layer consumes legitimate results.

**Result:** PASS.

> **Review Coordination != Commit Authority**

## 34. Test synthesis

All thirty tested conditions are representable without introducing a substantive central coordinator.

The stable mechanism is not “merge reviews.”

It is:

> **Preserve independent review grounds while permitting bounded operational coalescence of equivalent work.**

The strongest architecture is a **many-grounds / potentially-shared-work / many-outcomes** model.

## 35. Stable distinctions

The test supports:

`Subject identity`
!=
`Review-ground identity`

`Review-ground identity`
!=
`Evidence identity`

`Evidence identity`
!=
`Conclusion identity`

`Reviewer identity`
!=
`Owner identity`

`Bundle identity`
!=
`Authority identity`

`Bundle completion`
!=
`Constituent completion`

## 36. Minimal composition algorithm

1. Receive review-due request.
2. Resolve subject/unit/scope sufficiently for comparison.
3. Preserve request ground/provenance.
4. Test exact duplicate activation under STRA semantics.
5. If not duplicate, test material review-ground equivalence.
6. Preserve independent requests where equivalence is not established.
7. Identify legitimately reusable evidence/work.
8. Create/update a bundle only where operationally useful.
9. Route each constituent to its legitimate owner.
10. Record ground-addressable outcomes.
11. Revalidate freshness/context before satisfying later requests from prior work.
12. Split/reopen/supersede constituents when material state changes.
13. Derive bundle state without overwriting constituent state.
14. Route substantive conflict externally.
15. Preserve history.

Compact:

> **Receive → Resolve → Preserve Ground → Deduplicate Exact → Compare Grounds → Share Legitimate Work → Route Per Ground → Record Per Ground → Derive Bundle State → Reopen/Split As Material**

## 37. Minimum equivalence test

Two review requests may be treated as materially equivalent only where relevant dimensions align sufficiently:

`E = <Subject, Scope, Ground, RequiredQuestion, Consequence, Owner/Route, Context, Freshness>`

Not every low-consequence implementation requires formal equality across every field, but it must not use subject identity alone.

Where equivalence is uncertain:

> **Uncertain Equivalence -> Preserve Separate Grounds Until Resolved**

## 38. Bundle-state rule

Candidate bundle states:

- OPEN;
- PARTIAL;
- ROUTING_UNRESOLVED;
- DISPUTED;
- SPLIT_REQUIRED;
- SUPERSEDED;
- CLOSED_WITH_ALL_CONSTITUENTS_RESOLVED;
- CLOSED_WITH_CONSTITUENTS_REROUTED.

These are coordination states only.

No bundle state establishes substantive correctness.

## 39. Architectural ownership after test

### STRA retains
- trigger condition/state;
- review-due signal;
- duplicate activation suppression;
- cascade/cycle controls;
- routing and trigger provenance.

### KCS retains
- dependency/change propagation;
- material downstream review candidacy;
- dependency review provenance/stopping.

### ESCP retains
- completeness challenge;
- omitted-ground challenge;
- bounded discovery/termination/reopening.

### AUR retains
- architectural unit/family resolution.

### MKA/ASCP retains
- authority completeness/composition.

### CWA retains
- contextual permission/protected-space semantics.

### BTA retains
- transition-state/coherence semantics.

### Substantive owners retain
- domain conclusions.

### Review composition adds only
- cross-request ground preservation;
- bounded equivalence comparison;
- operational work/evidence coalescence;
- per-ground state tracking;
- bundle split/merge/supersession coordination.

## 40. Is the residual mechanism stable?

**YES — AS AN INTEGRATION PATTERN.**

The test found a coherent mechanism that is not reducible to duplicate suppression alone.

However, most of its safety boundaries and triggering semantics are supplied by existing architectures.

Therefore the evidence does **not yet require a new standalone portable module**.

## 41. Classification

**ADVERSARIAL INTEGRATION TEST: PASS**

**Mechanism status:** STABLE CROSS-ARCHITECTURE INTEGRATION PATTERN / NOT YET A PORTABLE MODULE

**Extraction decision:** DO NOT EXTRACT YET

The mechanism should be retained as a PMEDG candidate only if repeated use demonstrates independent portability beyond this Concord integration problem.

## 42. Candidate name

For development reference only:

**Review-Ground Composition Pattern (RGCP)**

This is a descriptive development label, not a graduated module name.

## 43. Candidate invariants strengthened by test

RGCP-01 **Same Subject != Same Review Ground.**

RGCP-02 **Duplicate Activation != Additional Review Ground.**

RGCP-03 **Operational Coalescence != Provenance Collapse.**

RGCP-04 **Shared Reviewer != Merged Question.**

RGCP-05 **Review Bundle != Merged Authority.**

RGCP-06 **Evidence Reuse != Conclusion Reuse.**

RGCP-07 **Evidence Reuse Is Scope-, Freshness- And Permission-Bounded.**

RGCP-08 **Constituent Completion != Bundle Completion.**

RGCP-09 **Bundle Membership Is Context-Bounded.**

RGCP-10 **Late Equivalence != Historical Identity.**

RGCP-11 **Bundle Split != Prior Error Erasure.**

RGCP-12 **Signal Volume != Material Diversity.**

RGCP-13 **All Represented Review Grounds != All Material Review Grounds.**

RGCP-14 **Coordination != Adjudication.**

RGCP-15 **Discovery Of New Ground != Mutation Of Original Ground.**

RGCP-16 **One Unresolved Owner != Automatic Global Review Failure.**

RGCP-17 **Bundle Availability != Bundle Requirement.**

RGCP-18 **Review Coordination != Commit Authority.**

## 44. New issue exposed

The test exposes a further question that should not be hidden inside RGCP:

> **When several independently legitimate constituent review results impose incompatible requirements on one proposed consequential act, what architecture determines whether the requirements compose, conflict, block, narrow or require an alternative route?**

This is not review deduplication and not review coordination.

MKA may already own a substantial part where the issue is authority composition; CWA/BTA may own contextual/transition constraints; CBPR owns bounded execution.

Therefore this **constraint/result composition** question must be source-resolved before any new architecture is proposed.

## 45. Disposition

1. Retain RGCP as a cross-domain integration pattern.
2. Flag RGCP as a PMEDG candidate; **do not extract yet**.
3. Do not modify STRA merely to absorb all review composition.
4. Do not create a central review authority.
5. Use ReviewRequest/ReviewBundle experimentally in future integrations.
6. Source-resolve the newly exposed constraint/result-composition question against MKA, CWA, BTA, CBPR and existing decision/composition architectures.
