# CWA + MKA + CBPR + BTA + KCS + STRA — Asynchronous Composition Test 001

**Project:** The Concord Framework
**Date:** 3 October 2026
**Status:** SIX-MODULE COMPOSITION TEST / COMPLETE
**Modules:** CWA + MKA v1.0 + CBPR v1.0 + BTA v1.0 + KCS Change Propagation v1.0 + STRA v1.0

## 1. Purpose

Test whether KCS Change Propagation and STRA can provide selective dependency review and state-triggered reopening for the previously validated CWA/MKA/CBPR/BTA stack without absorbing the substantive functions of those modules.

## 2. Ownership

- **CWA:** contextual boundaries, rules and permission topology.
- **MKA:** authority-space completeness, composition and current validity.
- **CBPR:** bounded runtime execution, commit and recovery.
- **BTA:** transition state and cross-owner completion.
- **KCS Change Propagation:** represented material dependencies and bounded downstream review propagation.
- **STRA:** declared state/event/condition triggers and routing of review candidacy.
- **External substantive owners:** source of domain facts, rules and authority.

## 3. Baseline dependency model

For an authorised transfer of Dataset D from Archive A to Repository R:

- MKA result A1 depends materially on relevant CWA route/context state C1.
- CBPR commit eligibility E1 requires current MKA result A1.
- BTA transition T1 references historical authority but completion depends on destination receipt R1.
- STRA watches declared material state changes.
- Historical BTA events do not depend for their historical occurrence on continued present validity of A1.

> **Connected != Affected**

## 4. Test A — route permission revoked before commit

CWA updates C1.

KCS records the scoped change and marks materially dependent A1 for review rather than automatically rejecting every downstream object.

STRA's declared context-change trigger routes review to MKA.

MKA revalidates the route.

CBPR refuses stale commit.

BTA preserves pending history.

**PASS**

## 5. Test B — context reclassification

A newly discovered protected relation changes Dataset D's contextual classification.

KCS identifies the prior authority-completeness claim as materially dependent.

STRA routes review.

MKA/ASCP reopens the authority space.

CBPR does not execute from stale prepared state.

BTA preserves preparation history without declaring completion.

**PASS**

## 6. Test C — authority expiry

A required authority expires.

KCS identifies current MKA/commit claims as materially affected but does not reopen unrelated CWA classification.

STRA routes authority/commit review.

MKA returns expired/revalidation-required state.

CBPR blocks commit.

Historical BTA references remain provenance.

**PASS**

## 7. Test D — runtime recovery

CBPR restarts before commit while no upstream state changes.

KCS does not infer that CWA or MKA changed merely because the runtime restarted.

STRA routes runtime recovery review.

CBPR checks current external references under its own rules.

No global restart occurs.

**PASS**

## 8. Test E — route change

R1 becomes unavailable and R2 is proposed.

KCS identifies route-specific dependent claims.

STRA routes the new route to appropriate context/authority owners.

CWA classifies R2.

MKA evaluates R2 independently.

CBPR does not infer permission from technical reachability.

BTA records the route change where material.

**PASS**

## 9. Test F — partial send followed by authority revocation

Source-side send may have occurred; destination receipt is unknown; authority is then revoked.

KCS distinguishes future retry claims from historical occurrence.

STRA routes current authority review.

CBPR does not blindly retry.

BTA remains unresolved.

Current invalidity does not erase historical occurrence.

**PASS**

## 10. Test G — destination receipt arrives

R1 changes from UNKNOWN to CONFIRMED.

KCS identifies T1 as materially dependent on R1.

STRA routes transition review to BTA.

BTA updates transition completion.

MKA is not reopened merely because receipt evidence arrived unless a new consequential act is proposed.

**PASS**

## 11. Test H — destination owner succession

Repository ownership changes.

KCS identifies only represented dependencies that are owner-sensitive.

STRA routes relevant reviews.

CWA, MKA and BTA resolve their own affected states.

Function continuity is not treated as automatic authority continuity.

**PASS**

## 12. Test I — bounded emergency predicate activates and later terminates

KCS represents the predicate change without commanding action.

STRA routes the declared emergency-condition review.

MKA verifies the pre-existing rule and current predicate.

CBPR acts only within a current bounded result.

When the predicate terminates before commit, KCS marks dependent current claims for review, STRA routes revalidation, MKA expires the emergency basis and CBPR blocks commit.

**PASS**

## 13. Test J — irrelevant telemetry

A non-material runtime counter changes.

KCS returns no material downstream effect and stops propagation.

STRA has no relevant satisfied trigger.

No other module is reopened.

**PASS**

## 14. Test K — unknown dependency discovered

A credible but unresolved new relation suggests an external state may matter.

KCS preserves UNKNOWN_DEPENDENCY / UNKNOWN_EFFECT.

STRA may route review if a declared trigger applies.

MKA/ASCP may reopen completeness if the unknown could represent a materially required authority dimension.

Uncertainty is not silently converted into permission, prohibition or certainty.

**PASS**

## 15. Test L — disputed materiality

Sources disagree about whether a change is material.

KCS preserves disputed/unknown materiality.

STRA consumes the bounded host materiality determination without inventing its own domain criterion.

MKA does not manufacture the missing substantive determination.

**PASS**

## 16. Test M — trigger satisfied, owner unresolved

A trigger fires but the substantive owner cannot be resolved.

STRA returns condition-satisfied / routing-unresolved rather than appointing itself.

KCS preserves unresolved responsibility where represented.

MKA gains no authority from the ownership gap.

**PASS**

## 17. Test N — large connected graph

One state change is connected to many objects, but only a small subset materially depends on the changed property.

KCS traverses and filters.

Only materially relevant candidates are reviewed.

STRA evaluates/routs relevant declared triggers rather than generating a system-wide trigger cascade.

**PASS**

## 18. Boundary/failure tests

The following attempted collapses were rejected:

1. **KCS as authority source** — dependency state does not create substantive authority.
2. **STRA as authority source** — trigger satisfaction does not authorise the consequence.
3. **KCS as semantic owner** — recording another module's state does not transfer ownership of its meaning.
4. **STRA as dependency-graph owner** — STRA consumes dependency state; it need not own the graph.
5. **Automatic downstream invalidation** — KCS uses candidate review, not automatic rejection.
6. **Unbounded propagation** — KCS stopping rules and STRA cascade controls bound propagation.
7. **Trigger chain as authority chain** — linked signals do not collectively manufacture authority.
8. **Historical erasure** — current change does not rewrite prior valid state/history.
9. **Graph completeness illusion** — no recorded dependency does not prove no dependency.
10. **Coordinator as substantive owner** — observing all module outputs does not transfer their substantive functions.

All ten were contained.

## 19. Six-module operating sequence

1. Substantive owner state changes.
2. KCS records the scoped change.
3. KCS traverses and filters material dependents.
4. KCS emits candidate review state rather than automatic invalidation.
5. STRA evaluates any applicable declared trigger and routes review candidacy.
6. The relevant substantive owner re-evaluates its own state.
7. KCS records the result.
8. Propagation continues only if the reviewed downstream state materially changes.
9. STRA updates its trigger state.
10. Historical provenance remains intact.

Compact form:

> **Change → KCS Candidate Review → STRA Trigger/Route → Owner Re-evaluation → KCS Update → Propagate-if-material**

## 20. Complementary roles

KCS asks:

> **What represented downstream objects may be materially affected by this change?**

STRA asks:

> **Has a declared condition for review been satisfied, and where should review candidacy be routed?**

The substantive owner asks:

> **What does the change actually mean for my function/domain?**

MKA asks, where consequential authority is implicated:

> **Does the proposed act have a complete, current and legitimately composable authority basis?**

These functions remain distinct.

## 21. Integration invariants

**SI-01 — Representation Of State != Ownership Of State Meaning.**

**SI-02 — Integration Visibility != Substantive Ownership.**

**SI-03 — Dependency Discovery != Substantive Decision.**

**SI-04 — Review Trigger != Review Outcome.**

**SI-05 — Candidate Review != Automatic Invalidation.**

**SI-06 — Trigger Cascade != Authority Chain.**

**SI-07 — Dependency Graph Completeness != Reality Completeness.**

**SI-08 — Selective Propagation Requires Materiality, Scope And Provenance.**

**SI-09 — A Downstream Review May Preserve Existing State And Stop Propagation.**

**SI-10 — Cross-Module Revalidation Follows Material Dependency Edges, Not Mere Architectural Adjacency.**

## 22. Result

**PASS — SIX-MODULE ASYNCHRONOUS COMPOSITION HOLDS**

KCS Change Propagation and STRA supply the coordination functions independently rediscovered in the preceding four-module asynchronous test.

They do so without becoming context owner, authority source, runtime controller, transition owner or substantive domain decision-maker.

The earlier provisional Bounded Dependency and Invalidation Architecture remains correctly classified as a rediscovery of existing KCS + STRA functionality and should not be extracted.

## 23. Developmental consequence

The reusable composition is now:

> **Context → Authority → Runtime → Transition**

supported by:

> **Dependency Propagation + State-Triggered Review**

This permits asynchronous change without either stale-state propagation or indiscriminate global restart.

## 24. Next investigation

A remaining shared problem is representational completeness.

KCS states:

> **No Recorded Dependency != No Dependency**

MKA/ASCP similarly asks whether all materially necessary authority dimensions are represented.

CWA, BTA and STRA also operate over bounded representations that can omit material dimensions.

The next source-resolution question is whether ESCP can provide a common completeness challenge across these architectures without becoming their semantic owner.

Suggested development:

**ESCP Across Representational Architectures — Completeness Without Centralisation 001**
