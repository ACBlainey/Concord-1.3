# Bounded Dependency and Invalidation Architecture — Existing Concord Source Resolution 001

**Project:** The Concord Framework  
**Date:** 3 October 2026  
**Status:** SOURCE-RESOLVED / REDISCOVERY OF EXISTING KCS CHANGE-PROPAGATION FUNCTION / DO NOT EXTRACT AS NEW MODULE  
**Origin:** CWA + MKA + CBPR + BTA — Asynchronous State Perturbation Test 001

# 1. Question

The asynchronous four-module composition test exposed a candidate architecture provisionally described as:

> **Bounded Dependency and Invalidation Architecture**

Candidate mechanism:

> **Owner-State Change → Material Dependency Identification → Selective Claim Invalidation → Owner Re-evaluation → Downstream Revalidation Where Required**

The source-resolution question is:

> Is this a genuinely new Concord architecture, an extension of an existing architecture, or an independently rediscovered manifestation of an existing Concord mechanism?

# 2. Source-resolution result

**NOT A NEW PORTABLE MODULE.**

The core mechanism is already substantially and explicitly owned by:

`04_Portable_Modules/KCS Change Propagation — Portable Module.md`

and is complemented by:

`04_Portable_Modules/State Triggered Review Architecture — Portable Module.md`

The asynchronous test therefore constitutes new **integration evidence and vocabulary**, not a new architecture requiring extraction.

# 3. KCS Change Propagation source match

KCS Change Propagation states its purpose as:

> **When an upstream object changes, what downstream objects should be reconsidered—and how can that review propagate without automatically invalidating everything connected to the change?**

Its compact architecture is:

> **Change upstream → identify materially affected dependents → review selectively → propagate further only when downstream material state changes.**

Its core invariant is:

> **Change(x) → CandidateReview(y)**

not:

> **Change(x) → AutomaticRejection(y)**

Its operating workflow is:

> **Represent → Change → Traverse → Filter → Review → Update → Propagate-if-material**

This directly covers the candidate mechanism exposed by the asynchronous composition test.

# 4. Direct concept mapping

| Asynchronous-test finding | Existing KCS Change Propagation ownership |
|---|---|
| Owner-state change | ChangeEvent / changed object |
| Material dependency identification | typed material dependency graph + traversal/filter |
| Selective claim invalidation/review | CandidateReview rather than AutomaticRejection |
| Preserve unaffected state | stopping rules / Connected != Affected |
| Continue only where material | propagate further only when downstream material state changes |
| Preserve historical provenance | historical state/change record; correction/supersession preserve old state |
| Scoped change | Object Change != Necessarily Every Instance or Every Time Period |
| Unknown dependency | UNKNOWN_DEPENDENCY / No Recorded Dependency != No Dependency |
| Freshness | first recorded / last confirmed / last changed / next review |
| Dependency without sovereignty | Dependency != Subordination / Dependency State != System Authority |
| Cross-owner relation | distributed suppliers/responsibilities without false single-owner model |

The overlap is architectural, not merely thematic.

# 5. STRA source match

State Triggered Review Architecture owns a different but complementary function.

STRA represents:

> **Reconsider A when prerequisite B reaches required state S.**

It consumes represented dependency state but explicitly states:

> **STRA does not inherently discover every dependency, calculate full propagation, or own the dependency graph.**

STRA also distinguishes trigger satisfaction from substantive authority and routes review/action candidacy to a legitimate external owner.

Therefore:

- **KCS Change Propagation** owns dependency-aware propagation and bounded downstream review generation.
- **STRA** owns state/event/condition-triggered reopening and routing.
- **Domain/module owners** own substantive reevaluation.
- **MKA** owns consequential authority completeness/composition where authority is implicated.
- **CWA** owns contextual classification/permission topology.
- **CBPR** owns bounded runtime commit/recovery.
- **BTA** owns transition coherence/state.

# 6. Why the candidate appeared new

The asynchronous test did not begin from KCS.

It began from four independently composed portable architectures:

CWA → MKA → CBPR → BTA.

When their states were perturbed asynchronously, the same structural requirement emerged independently:

- changed upstream state;
- identify which derived claims materially depend upon it;
- reopen those claims;
- preserve unrelated valid state;
- preserve historical provenance;
- avoid centralising semantic ownership.

This is a strong independent convergence on the KCS Change Propagation architecture.

# 7. Novel contribution from the asynchronous test

Although the architecture is not new, the test contributes useful integration-level formulations.

## 7.1 Dependency-scoped invalidation

> **When an externally owned state changes, invalidate only those derived claims whose validity materially depends on that state, while preserving independent current state and historical provenance.**

This is consistent with KCS CandidateReview/selective propagation.

## 7.2 State dependency versus ownership

> **State Dependency != State Ownership**

KCS already establishes:

> **Dependency != Subordination**

The new formulation is especially useful for modular software/institutional composition because a module may depend on another module's state without owning the semantics of that state.

## 7.3 Dependency propagation versus sovereignty

> **Dependency Propagation != Sovereignty Propagation**

This is a cross-module expression of KCS's anti-centralisation boundary.

## 7.4 Claim-level freshness

> **Freshness Belongs To The Claim That Depends On The Changing State.**

KCS already represents freshness at dependency-record level. The asynchronous test demonstrates the value of carrying that principle into derived cross-module claims.

## 7.5 Historical/current separation

> **Historical Validity != Current Validity**

> **Current Invalidity != Historical Non-Occurrence**

KCS already preserves historical state rather than overwriting it. The test shows why this matters in authority, runtime and transition composition.

# 8. Candidate architecture disposition

The provisional **Bounded Dependency and Invalidation Architecture** should be retired as a separate extraction candidate.

Disposition:

**SOURCE-RESOLVED TO KCS CHANGE PROPAGATION + STRA INTERFACE**

Do not create:

`04_Portable_Modules/Bounded Dependency and Invalidation Architecture — Portable Module.md`

That would duplicate an already graduated module.

# 9. Existing-module ownership

Primary owner:

`04_Portable_Modules/KCS Change Propagation — Portable Module.md`

Trigger/review interface:

`04_Portable_Modules/State Triggered Review Architecture — Portable Module.md`

Broader knowledge-state context:

`04_Portable_Modules/Knowledge Control System — Portable Module.md`

# 10. Cross-module composition

The asynchronous test suggests the following integration grammar:

`Owner State Change`
→ `KCS Dependency Traversal / Materiality Filter`
→ `STRA Review Trigger/Route where required`
→ `Substantive Owner Re-evaluation`
→ `KCS Record Updated State`
→ `Further Propagation Only If Material`

Where consequential authority changes:

→ `MKA Revalidation`

Where runtime commit state changes:

→ `CBPR Commit/Recovery Revalidation`

Where transition state changes:

→ `BTA Transition Update`

Where contextual classification changes:

→ `CWA Context Update`

This is coordination, not ownership transfer.

# 11. Architectural boundary

KCS should not become a universal semantic owner merely because it maps dependencies.

STRA should not become the dependency graph.

MKA should not become the change-propagation engine.

CBPR should not decide substantive authority.

BTA should not decide why an upstream state changed.

CWA should not determine every downstream consequence of a context change.

The owner of each substantive state remains external to the propagation relation.

# 12. Source-resolution classification

**Classification: REDISCOVERY / INDEPENDENT CONVERGENCE / INTEGRATION VALIDATION**

Not:

- new Level B extraction;
- replacement for KCS;
- replacement for STRA;
- new authority architecture.

# 13. Developmental value

The rediscovery is valuable because it demonstrates KCS Change Propagation arising naturally from a separate composition problem.

The four-module asynchronous test did not need to assume KCS in order to expose the need for KCS-like propagation.

That strengthens confidence that the KCS mechanism represents a general systems requirement rather than an artefact of its original development path.

# 14. Recommended follow-up

Do not reopen PMEDG graduation for KCS solely because of this result.

Instead:

1. preserve the asynchronous test as independent integration evidence;
2. record this source-resolution result;
3. add the new formulations to KCS only through a versioned companion/integration note unless a future module revision is otherwise justified;
4. test the full five/six-module composition:
   - CWA;
   - MKA;
   - CBPR;
   - BTA;
   - KCS Change Propagation;
   - STRA;
5. verify that KCS/STRA selectively reopen the correct owner after asynchronous perturbation without becoming central authority.

# 15. Final result

> **The proposed Bounded Dependency and Invalidation Architecture is not a new Concord architecture. Its core function is already owned by the graduated KCS Change Propagation portable module, with STRA providing the complementary state-triggered review and routing function.**

The asynchronous composition test contributes independent validation and useful cross-module formulations, especially:

> **State Dependency != State Ownership**

> **Dependency Propagation != Sovereignty Propagation**

> **Freshness Belongs To The Claim That Depends On The Changing State**

These should be retained as integration findings rather than used to create a duplicate module.

**SOURCE RESOLUTION: COMPLETE.**
