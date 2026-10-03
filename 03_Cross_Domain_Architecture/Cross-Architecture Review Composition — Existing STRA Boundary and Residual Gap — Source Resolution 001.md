# Cross-Architecture Review Composition — Existing STRA Boundary and Residual Gap — Source Resolution 001

**Project:** The Concord Framework
**Date:** 3 October 2026
**Status:** SOURCE RESOLUTION / PARTIAL REDISCOVERY / RESIDUAL INTEGRATION GAP / NON-CANONICAL
**Primary sources:** State Triggered Review Architecture (STRA), KCS Change Propagation, Architectural Unit Resolution (AUR), ESCP Operational Companion

## 1. Question

When several cross-cutting Concord architectures independently indicate that the same substantive object should be reviewed, should the resulting review obligations:

- remain separate;
- be merged;
- be deduplicated;
- be coordinated;
- or be treated as a new architectural problem?

The immediate concern arose after integrating ESCP with KCS, STRA, MKA/ASCP, CWA, CBPR and BTA.

## 2. Source-resolution result

**PARTIAL REDISCOVERY.**

A generic duplicate-review suppression mechanism is **already present in STRA**.

STRA Cascade Control explicitly requires:

- preservation of parent/initiating-trigger provenance;
- direct-cycle detection where represented;
- suppression of duplicate activation of the same consequence for the same material condition where host semantics allow;
- independent satisfaction/activation rules for consequential child triggers;
- materiality gating;
- owner/routing validation.

STRA also permits additional bounded duplicate suppression.

Therefore:

> **Duplicate Trigger Activation Is Not A New Architectural Gap**

and:

> **Do Not Extract A Generic Review-Deduplication Module**

However, STRA does not by itself fully resolve the different problem:

> several independent architectures may generate **different material review grounds** concerning the same substantive object.

That residual problem is not simple duplication.

## 3. Duplicate activation versus distinct review grounds

Consider object O.

KCS may request review because dependency D changed.

ESCP may request review because evaluation-space completeness is disputed.

MKA/ASCP may require authority-space revalidation.

CWA may require contextual permission re-evaluation.

BTA may require transition-state re-evaluation.

STRA may route each review-due condition.

All signals may refer to O.

But:

`SameSubject != SameReviewGround`

and:

`SameDestination != DuplicateObligation`

A system that collapses all five into one generic “review O” flag may lose why the review is required and what questions must be answered.

## 4. Existing STRA ownership

STRA already owns:

- trigger representation;
- condition evaluation;
- review-due signalling;
- routing;
- parent-trigger provenance;
- cascade control;
- duplicate suppression where the same material condition/consequence is repeated;
- unresolved routing state;
- correction/supersession history.

Therefore STRA is the natural routing/control plane for review requests.

But STRA explicitly does not own the substantive outcome.

> **Triggering Review != Authority Over Outcome**

## 5. Existing KCS ownership

KCS owns material dependency/change-propagation review candidacy.

It already distinguishes:

`Change(x) -> CandidateReview(y)`

from automatic downstream rejection.

KCS review records preserve:

- why review was triggered;
- what relation/property changed;
- materiality/context;
- evidence;
- review outcome;
- resulting state;
- whether propagation continues.

Therefore KCS provides a strong precedent for retaining **review-ground provenance** rather than flattening review into a binary flag.

## 6. Existing AUR relevance

AUR asks whether a problem has been attributed to the correct architectural unit/family before declaring a gap.

Its relevance here is diagnostic.

Before treating two review requests as duplicates, resolve whether they refer to:

- the same substantive object;
- the same architectural unit;
- the same system family;
- or merely similarly labelled/adjacent objects.

AUR already warns:

> **Similar Topic != Same Architectural Family**

Therefore:

> **Apparent Duplicate Review != Proven Duplicate Review**

AUR does not itself coordinate review execution.

## 7. Existing ESCP relevance

ESCP adds another caution.

A coordinator may accurately represent every review ground it knows while omitting another material ground.

Therefore:

> **All Represented Review Grounds != All Material Review Grounds**

This is an ESCP completeness challenge, not a reason for infinite review.

ESCP does not own the review result.

## 8. Residual gap

The remaining integration question is:

> **How can multiple distinct review grounds concerning the same substantive object share work and produce a coherent review record without erasing independent grounds, duplicating equivalent work, or creating a new substantive authority?**

This is narrower than generic review deduplication.

It is a **review-ground composition** problem.

## 9. Minimum distinctions

A review coordination layer must distinguish:

### A. Exact duplicate activation

Same material condition, same consequence, same subject/scope, same effective review obligation.

STRA duplicate suppression applies.

### B. Same ground, different source

Two independent sources identify the same material review ground.

The review may be coalesced operationally while preserving both source/provenance records.

### C. Different grounds, shared evidence

Example: KCS dependency change and ESCP completeness challenge both require inspection of the same dependency evidence.

Evidence retrieval/evaluation may be shared.

The grounds remain distinct.

### D. Different grounds, different questions, same owner

One domain owner may answer several questions in one bounded review session.

The outputs must remain ground-addressable.

### E. Different grounds, different owners

No merger into a single substantive decision is implied.

Coordination may share routing/provenance only.

### F. Conflicting review conclusions

Different architectures may legitimately return different dimensional states.

These should not be forced into one scalar status.

## 10. Candidate review-request form

A cross-architecture review request may be represented as:

`ReviewRequest = <RequestID, SubjectRef, Scope, GroundType, GroundRef, TriggerRef, RequiredQuestion, EvidenceRefs, ConsequenceClass, OwnerRef, Route, State, Provenance, Freshness>`

The important field is **GroundRef**.

Two requests should not be deduplicated merely because SubjectRef matches.

## 11. Candidate review bundle

Operational coordination may create:

`ReviewBundle = <BundleID, SubjectRef, Scope, RequestRefs, SharedEvidenceRefs, OwnerRefs, BundleState, Provenance>`

A bundle is a coordination object.

It is not a new substantive authority.

> **Review Bundle != Merged Authority**

> **Shared Work != Shared Semantic Ownership**

## 12. Deduplication key

A safe duplicate test requires more than subject identity.

Candidate equivalence dimensions:

- subject;
- bounded scope;
- material condition/ground;
- required question;
- consequence;
- owner/route;
- freshness/time;
- relevant context.

Only where the host can establish material equivalence should duplicate activation be suppressed.

> **Same Object != Same Review**

> **Same Label != Same Ground**

> **Equivalent Review Ground Must Be Established, Not Assumed**

## 13. Composition rule

Candidate rule:

> **Coalesce operational work where review grounds are materially compatible, but preserve each independent ground, source, owner, required question and outcome.**

This permits:

- one evidence retrieval serving several requests;
- one owner session answering several questions;
- one notification instead of five equivalent notifications;
- one provenance-linked bundle.

It forbids:

- deleting independent grounds;
- treating one answered question as answering every ground;
- transferring authority between grounds;
- flattening conflicting states.

## 14. Completion semantics

A bundle must not be marked complete merely because one constituent request is complete.

Each request requires its own terminal/continuing state.

Possible bundle state can be derived from constituent states but must not overwrite them.

> **Bundle Completion != Constituent Completion Unless Every Required Constituent Is Resolved Or Legitimately Superseded**

A host may close a bundle while preserving unresolved requests only if those requests have been rerouted into another live bounded process.

## 15. Reuse of evidence

Evidence may be reused where:

- it is relevant to the required question;
- scope matches;
- freshness is adequate;
- provenance is preserved;
- access/permission allows reuse;
- domain interpretation remains valid.

> **Evidence Reuse != Conclusion Reuse**

The same evidence can support different substantive evaluations without forcing identical conclusions.

## 16. Freshness and stale review

A prior review may satisfy a new request only where its:

- question;
- scope;
- material ground;
- evidence freshness;
- context;
- authority/owner state

remain adequate.

> **Prior Review != Current Review By Default**

STRA/KCS freshness mechanisms may support this determination.

## 17. Authority boundary

A review coordinator may:

- group requests;
- suppress established duplicates;
- share evidence retrieval;
- route requests;
- track constituent states;
- preserve provenance.

It must not:

- decide substantive legal/ethical/domain questions merely because it coordinates them;
- manufacture authority;
- erase disagreement;
- choose a universal priority absent external legitimate criteria;
- treat bundle ownership as ownership of constituent semantics.

> **Coordination != Adjudication**

## 18. Failure cases

### 18.1 Subject-only deduplication

Five requests concerning O are collapsed because they share O.

**FAIL** — grounds may differ.

### 18.2 Trigger-count execution

Five triggers produce five identical reviews despite established equivalence.

**FAIL** — STRA already permits/requires duplicate suppression where host semantics allow.

### 18.3 One-ground completion laundering

KCS dependency review passes; system marks ESCP completeness and MKA authority review complete.

**FAIL**.

### 18.4 Central coordinator sovereignty

Coordinator decides all constituent substantive outcomes.

**FAIL**.

### 18.5 Evidence duplication

Five architectures independently retrieve the same expensive evidence despite legitimate reusable access.

**INEFFICIENT / avoid where bounded reuse is valid.**

### 18.6 Stale evidence reuse

An old review is reused after context/authority/dependency state materially changed.

**FAIL**.

### 18.7 Provenance erasure

Requests are bundled and their original sources/grounds disappear.

**FAIL**.

## 19. Source-resolution classification

### Already owned

**STRA**
- duplicate activation suppression;
- cascade control;
- trigger provenance;
- review-due routing;
- owner/routing validation.

**KCS**
- dependency-originated review candidacy;
- review-ground/change provenance;
- material propagation and stopping.

**AUR**
- correct unit/family resolution before equivalence/gap assumptions.

**ESCP**
- completeness challenge against the represented set of review grounds.

### Not yet fully owned

A generic cross-architecture object for:

- preserving multiple independent review grounds;
- coalescing compatible operational work;
- tracking per-ground completion;
- reusing evidence without reusing conclusions;
- avoiding both duplicate work and ground erasure.

## 20. Is this a new portable module?

**NOT YET ESTABLISHED.**

The residual mechanism may be:

1. a STRA companion upgrade;
2. a cross-domain integration pattern;
3. a small review-bundling interface shared by existing modules;
4. or, after testing, a portable module.

The current evidence is insufficient to justify immediate extraction.

## 21. Candidate invariants

RC-01 **Same Subject != Same Review Ground.**

RC-02 **Same Destination != Duplicate Obligation.**

RC-03 **Apparent Duplicate Review != Proven Duplicate Review.**

RC-04 **Shared Work != Shared Semantic Ownership.**

RC-05 **Review Bundle != Merged Authority.**

RC-06 **Evidence Reuse != Conclusion Reuse.**

RC-07 **Prior Review != Current Review By Default.**

RC-08 **Coordination != Adjudication.**

RC-09 **Bundle State != Erasure Of Constituent State.**

RC-10 **Equivalent Review Ground Must Be Established, Not Assumed.**

## 22. Result

**SOURCE RESOLUTION: PARTIAL REDISCOVERY / RESIDUAL GAP CONFIRMED**

Do not create a generic “review deduplication” portable module.

STRA already owns duplicate trigger/consequence suppression.

The genuinely unresolved issue is narrower:

> **composition of distinct but overlapping review grounds concerning the same substantive object.**

This should be tested as an integration architecture before PMEDG extraction is considered.

## 23. Next test

Recommended:

**Cross-Architecture Review Composition — Adversarial Integration Test 001**

Test at minimum:

- exact duplicate triggers;
- same ground from independent sources;
- different grounds sharing evidence;
- different grounds sharing owner;
- different grounds with different owners;
- stale prior review;
- changed context after review;
- one constituent complete / others unresolved;
- conflicting constituent outcomes;
- protected evidence reusable by only some grounds;
- bundle split after owner change;
- bundle merge after equivalence established;
- cyclic review triggers;
- high-volume trigger storm;
- missing/unrepresented review ground;
- coordinator attempting substantive authority.

Do not extract a module unless this test demonstrates a stable mechanism not already owned by STRA/KCS/AUR/ESCP.
