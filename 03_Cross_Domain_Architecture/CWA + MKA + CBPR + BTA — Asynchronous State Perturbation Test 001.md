# CWA + MKA + CBPR + BTA — Asynchronous State Perturbation Test 001

**Project:** The Concord Framework  
**Date:** 3 October 2026  
**Status:** CROSS-MODULE ASYNCHRONOUS PERTURBATION TEST / COMPLETE  
**Modules:** CWA + MKA v1.0 + CBPR v1.0 + BTA v1.0  
**Predecessor:** MKA + CWA + CBPR + BTA — Live Composition Test 001

# 1. Purpose

Test whether the four-module stack remains coherent when material state changes asynchronously during a consequential process.

The central question is:

> **Can a material change reopen the correct dependency without either propagating stale state or unnecessarily invalidating unrelated valid state?**

The test injects:

- permission revocation;
- context reclassification;
- authority expiry;
- runtime recovery;
- route change;
- partial transition;
- destination-owner succession;
- emergency activation and termination.

# 2. Baseline scenario

Continue the protected archive transfer pattern.

Agent Q is authorised to transfer approved Dataset D from Archive A to Repository R through Route R1.

At baseline:

- CWA classifies D as releasable through R1;
- MKA has a complete, current and composable authority set for the act;
- CBPR has a bounded runtime grant and valid execution path;
- BTA tracks Transition T1;
- no protected attachment is included.

Baseline state:

CWA = VALID_CONTEXT_ROUTE  
MKA = AUTHORISED_WITHIN_SCOPE  
CBPR = READY_TO_COMMIT  
BTA = ACTIVE_OR_PENDING

# 3. Perturbation principle

A change in one owner state does not automatically rewrite every other owner state.

Instead:

> **Material Change Reopens Dependent Claims, Not Unrelated History.**

And:

> **State Change Propagation Must Follow Dependency, Not Mere Architectural Adjacency.**

This is tested throughout.

# 4. Perturbation A — Permission revoked before commit

After MKA authorises the act but before CBPR commits, the permission underlying Route R1 is revoked.

## CWA

CWA updates the route permission state.

It does not itself decide the full authority result.

## MKA

Because permission/context state is material to the actual route, the prior result is stale for commit.

Result:

`REVALIDATION_REQUIRED`

If no alternative route exists, commit cannot rely on the old result.

## CBPR

CBPR must revalidate at consequential commit.

It must not treat the cached MKA result as permanently valid.

## BTA

T1 remains pending/not committed. Historical proposal state remains provenance.

**RESULT: PASS**

# 5. Perturbation B — Context reclassified after preparation

Dataset D is prepared for release, but before commit its context is reclassified because newly linked participant information makes the package protected.

## CWA

CWA owns the new contextual classification.

## MKA

The changed protected interface materially changes required authority space.

ASCP reopens.

The previous completeness result cannot be reused unchanged.

Potential result:

`HOLD_MISSING_AUTHORITY` or `HOLD_UNKNOWN_AUTHORITY`, depending on supplied authority state.

## CBPR

Prepared bytes remain technically available.

But:

> **Prepared Action != Committed Action.**

CBPR cannot execute from stale context/authority state.

## BTA

Preparation history remains true.

Reclassification does not erase that history, but the transition cannot infer completion.

**RESULT: PASS**

# 6. Perturbation C — Authority expires during runtime delay

The release authority expires after preparation but before external side effect.

## MKA

Authority freshness fails.

Result:

`EXPIRED` / `REVALIDATION_REQUIRED`.

## CBPR

A scheduled or delayed runtime action does not preserve authority.

> **Scheduled Wakeup != Continuous Autonomy.**

Commit is blocked until current authority exists.

## CWA

Context need not change merely because authority expired.

## BTA

T1 remains pending/failed according to host mapping.

The historical authority reference remains provenance but not current authority.

**RESULT: PASS**

# 7. Perturbation D — Runtime crash and recovery before commit

Q crashes after preparation and restarts from checkpoint.

No external side effect occurred.

## CBPR

Runtime recovery restores technical state only.

> **Runtime Recovery != Automatic Recovery Of Prior Authority.**

CBPR revalidates current permission/authority before commit.

## MKA

If no material authority facts changed and the host freshness rule permits, the prior derivation may be reverified rather than re-derived from scratch.

> **Repeated Equivalent Action != Mandatory Re-Derivation Of Identical Authority.**

## CWA

No automatic context change.

## BTA

T1 remains the same transition if host recovery rules establish continuity.

Recovery does not itself create a new completed transition.

**RESULT: PASS**

# 8. Perturbation E — Route changes during recovery

R1 is unavailable after restart. Runtime discovers Route R2 through a different protected network/service context.

## CBPR

Technical reachability of R2 is not permission or authority.

## CWA

CWA classifies R2 and its contextual boundary.

## MKA

> **Route Change Can Invalidate Authority Completeness.**

The R1 result cannot automatically authorise R2.

MKA re-evaluates the actual route.

If R2 has no legitimate route authority:

`HOLD_MISSING_AUTHORITY`

If an authorised alternative exists:

`REROUTE_AVAILABLE`.

## BTA

T1 may preserve the route change as transition provenance.

It does not decide whether R2 is authorised.

**RESULT: PASS**

# 9. Perturbation F — Partial transition then source authority revoked

CBPR sends the package. Source-side send succeeds. Destination receipt remains unknown. The release authority is then revoked.

## BTA

T1 is PARTIAL_OR_INTERMEDIATE / unresolved.

The historical send remains part of transition history.

## MKA

Revocation does not retroactively make the already committed historical act nonexistent.

But it blocks treating historical authority as authority for a new retry.

## CBPR

Unknown commit state prevents blind retry.

Revocation independently prevents reliance on the old authority for a fresh consequential act.

## CWA

Context state is unchanged unless separately reclassified.

**RESULT: PASS**

# 10. Perturbation G — Destination owner changes mid-transition

While T1 is unresolved, Repository R changes operator from Owner R-A to Owner R-B.

The repository endpoint remains technically reachable.

## BTA

Owner succession is a material transition-state dependency.

BTA records the changed destination-owner state and does not infer that R-A acceptance criteria automatically transfer to R-B.

## MKA

If a new consequential act is proposed, deposit authority and destination scope must be checked against R-B.

> **Function Continuity != Authority Continuity.**

## CBPR

Stored credentials or endpoint reachability do not establish current authority to act against R-B.

## CWA

If destination context rules changed with ownership, CWA must supply the current contextual state.

**RESULT: PASS**

# 11. Perturbation H — Emergency activates

A genuine emergency begins while T1 is pending. A pre-existing bounded emergency rule permits use of Route E for preservation of the dataset.

## CWA

CWA identifies Route E's protected context and applicable emergency access conditions.

## MKA

MKA verifies the pre-existing emergency authority and current activation predicate.

It does not create emergency authority from urgency.

> **Precompute The Authority Rule; Verify Current Facts.**

If complete:

`AUTHORISED_WITHIN_SCOPE` for the bounded emergency act.

## CBPR

CBPR may execute Route E only within that result and its runtime bounds.

## BTA

BTA records the emergency route/change without treating emergency use as automatic completion of the original transition objective.

**RESULT: PASS**

# 12. Perturbation I — Emergency terminates before commit

The emergency predicate ends after approval of Route E but before consequential commit.

## MKA

The emergency authority is stale at commit.

`REVALIDATION_REQUIRED` / `EXPIRED`.

## CBPR

Commit must not proceed under the expired emergency predicate.

## CWA

Emergency-context access may also terminate according to its externally supplied rule.

## BTA

The proposed emergency route remains provenance, not completed transition.

**RESULT: PASS**

# 13. Perturbation J — Permission revoked after completed transfer

T1 completes validly. Later, the source permission is revoked.

Finding:

The revocation affects future acts.

It does not rewrite the completed transition as though it never occurred.

> **Current Revocation != Historical Event Erasure.**

CWA records current permission state.
MKA applies it to future acts.
CBPR cannot reuse stale grants.
BTA preserves completed historical transition state.

**RESULT: PASS**

# 14. Perturbation K — Context changes after completed transfer

After valid completion, the source classifies future copies of Dataset D as protected.

The already transferred copy's status in R is governed by the legitimate destination/context rules applicable there.

CWA must not assume source reclassification automatically rewrites every remote context.

BTA may preserve relational/context-change references where material.

MKA must evaluate any new act against current applicable contexts.

**RESULT: PASS**

# 15. Perturbation L — Runtime grant revoked while authority remains valid

Substantive release authority remains valid, but Q's runtime grant is revoked.

MKA's authority result does not itself fail merely because this runtime can no longer execute it.

CBPR blocks Q.

A different legitimately configured runtime might execute the same authorised act if all relevant current conditions hold.

> **Authority To Act != Authority/Capability Of Every Runtime To Execute.**

**RESULT: PASS**

# 16. Perturbation M — Authority changes but runtime state does not

Q remains technically configured and credentialed, but a required authority is revoked.

CBPR must not infer authority from unchanged runtime state.

MKA returns current failure/revalidation state.

> **Stable Capability != Stable Authority.**

**RESULT: PASS**

# 17. Perturbation N — Transition state changes but authority does not

Destination confirms receipt after a delay. Authority state has not changed.

BTA may update T1 from unresolved to completed.

There is no reason to reopen MKA merely because transition evidence arrived, unless a new consequential act is proposed.

> **Transition-State Update != Automatic Authority Re-Evaluation.**

**RESULT: PASS**

# 18. Perturbation O — Non-material telemetry change

A runtime telemetry counter changes while the act, route, context, authority, consequence and transition predicates remain materially unchanged.

No architecture should trigger a full-stack restart.

CBPR may record local telemetry.

MKA, CWA and BTA remain unchanged unless host rules make the change material.

> **Any State Change != Material Revalidation Trigger.**

**RESULT: PASS**

# 19. Selective reopening matrix

| Change | CWA | MKA | CBPR | BTA |
|---|---|---|---|---|
| route permission revoked pre-commit | UPDATE | REOPEN | REVALIDATE COMMIT | preserve pending |
| context reclassified | UPDATE | REOPEN ASCP | BLOCK/REVALIDATE | preserve history |
| authority expires | no required change | REOPEN | BLOCK/REVALIDATE | preserve pending/history |
| runtime crash | no required change | verify freshness if material | RECOVER + REVALIDATE | preserve transition |
| route changes | CLASSIFY NEW ROUTE | REOPEN | evaluate executable route | record route change |
| partial send | no required change | no new act yet | unknown-commit handling | UPDATE PARTIAL |
| destination owner changes | maybe update destination context | REOPEN for new act if material | revalidate credentials/grants | UPDATE OWNER STATE |
| emergency activates | classify emergency context | verify emergency authority | execute only if bounded | record route/state |
| emergency terminates pre-commit | update if applicable | REOPEN/EXPIRE | BLOCK | preserve proposal |
| transition receipt arrives | no required change | no required change | close commit state | UPDATE COMPLETION |
| telemetry only | no required change | no required change | local update | no required change |

# 20. Important finding — selective invalidation

The test supports:

> **Dependency-Scoped Invalidation**

Definition:

> **When an externally owned state changes, invalidate only those derived claims whose validity materially depends on that state, while preserving independent current state and historical provenance.**

This avoids two opposite failures:

1. **stale propagation** — continuing to rely on a result whose dependency changed;
2. **global invalidation** — discarding every valid state merely because one dependency changed.

# 21. Dependency-edge principle

Cross-module integration should therefore represent material dependency edges.

Conceptually:

`DerivedStateRef -> DependencyRefs[]`

When dependency D changes:

`Invalidate(Claims materially dependent on D)`

not:

`Invalidate(All system state)`

This does not require a universal central dependency sovereign.

Each module may expose which external references its result depends upon.

# 22. Provenance rule

Historical truth and current validity are distinct.

> **Historical Validity != Current Validity**

> **Current Invalidity != Historical Non-Occurrence**

Therefore a state update should normally preserve:

- what was known;
- what was authorised;
- what was attempted;
- what occurred;
- what later changed;
- which claims became stale;
- which claims remained valid.

# 23. Cross-module freshness rule

A useful shared integration rule is:

> **Freshness Belongs To The Claim That Depends On The Changing State.**

A context update may stale an MKA result without staling an unrelated BTA historical event.

An authority revocation may block a CBPR commit without changing CWA classification.

A BTA receipt update may complete a transition without reopening an unchanged MKA authority decision.

# 24. Failure injection — global restart

Injected policy:

“Any material state change restarts CWA, MKA, CBPR and BTA from zero.”

Finding:

Safe but structurally excessive.

It destroys useful valid state, increases latency and encourages unnecessary centralisation.

**REJECTED AS DEFAULT ARCHITECTURE.**

# 25. Failure injection — no propagation

Injected policy:

“Each module is independent, so changes never invalidate another module's result.”

Finding:

Unsafe.

It permits stale permission, authority, route and commit state.

**REJECTED.**

# 26. Failure injection — adjacency propagation

Injected policy:

“A changed state invalidates the next module in the chain only.”

Finding:

Insufficient.

Dependencies are not always linear. A destination-owner change may affect CWA, MKA and BTA while not necessarily invalidating unrelated CBPR internal state.

**REJECTED.**

# 27. Preferred model

The preferred integration model is:

> **Owner-State Change → Material Dependency Identification → Selective Claim Invalidation → Owner Re-evaluation → Downstream Revalidation Where Required**

This preserves modularity without allowing stale state.

# 28. New cross-module invariants

CM-01 **Material Change Reopens Dependent Claims, Not Unrelated History.**

CM-02 **State Change Propagation Must Follow Dependency, Not Mere Architectural Adjacency.**

CM-03 **Dependency-Scoped Invalidation != Global Restart.**

CM-04 **Historical Validity != Current Validity.**

CM-05 **Current Invalidity != Historical Non-Occurrence.**

CM-06 **Freshness Belongs To The Claim That Depends On The Changing State.**

CM-07 **Stable Capability != Stable Authority.**

CM-08 **Transition-State Update != Automatic Authority Re-Evaluation.**

CM-09 **Any State Change != Material Revalidation Trigger.**

CM-10 **Current Revocation != Historical Event Erasure.**

# 29. Result

**PASS — ASYNCHRONOUS COMPOSITION REMAINS COHERENT**

Fifteen asynchronous perturbations and three propagation-policy failure injections were evaluated.

No architecture required ownership of another module's substantive state.

The stack successfully distinguished:

- current validity from historical provenance;
- dependency from adjacency;
- authority from execution capability;
- transition state from authority state;
- context change from universal state change;
- material perturbation from irrelevant telemetry;
- selective reopening from global restart.

No blocking defect was identified in the four portable modules.

# 30. Architectural consequence

The previous live composition test established:

> **State Interoperability != Semantic Sovereignty Transfer**

This test adds:

> **State Dependency != State Ownership**

and:

> **Dependency Propagation != Sovereignty Propagation**

Together these suggest a general cross-module integration grammar:

1. modules own their substantive state;
2. other modules may consume bounded references to that state;
3. derived claims record material dependencies;
4. material dependency changes selectively stale dependent claims;
5. the owning module remains responsible for the changed substantive state;
6. consumers revalidate their own derived claims;
7. historical provenance is preserved.

# 31. Next development candidate

This result exposes a potentially reusable architecture:

**Bounded Dependency and Invalidation Architecture**

Possible purpose:

> coordinate how independently owned module states declare material dependencies, freshness and selective invalidation without creating a central semantic owner.

This should **not yet be extracted**.

First source-resolve against existing Concord systems, especially:

- KCS change propagation;
- State Triggered Review Architecture;
- BTA dependency interface;
- CBPR commit/freshness rules;
- MKA freshness/reopening;
- CWA contextual reclassification;
- Civilisation Clock / temporal architecture.

The immediate next step is therefore:

**Bounded Dependency and Invalidation Architecture — Existing Concord Source Resolution 001**
