# Cross-Architecture Feedback Loop — Closure, Quiescence and Reopening — Integration Audit 001

**Project:** The Concord Framework  
**Date:** 3 October 2026  
**Status:** INTEGRATION AUDIT / COMPLETE / NON-CANONICAL  
**Architectures:** RGCP, BRSP, MKA/CWA, CBPR, EERP, BTA, KCS Change Propagation, STRA  
**Purpose:** Test whether the emerging feedback lifecycle has coherent handoffs, stopping conditions and legitimate reopening without creating a central controller.

## 1. Lifecycle under audit

The recent integration work exposes the following feedback structure:

**RGCP**
→ preserve why review is required

**BRSP / MKA / CWA / BTA**
→ evaluate the actual route against externally owned constraints

**CBPR**
→ revalidate current consequential commit

**Execution**

**EERP**
→ compare actual execution/effect with the commit-authorised envelope

**BTA**
→ preserve transition crossing, partial state, residual effects and recovery state

**KCS**
→ identify materially affected dependents after represented state change

**STRA**
→ activate/reroute bounded review when declared conditions become satisfied

**RGCP**
→ preserve newly generated review grounds

This is not a linear pipeline.

It is a feedback loop.

## 2. Audit question

Can the loop:

- reach legitimate closure;
- remain dormant without pretending permanent finality;
- reopen when material state changes;
- suppress duplicate/cyclic work;
- preserve unresolved states;
- and avoid creating a central architecture with authority over every constituent owner?

## 3. Existing local closure mechanisms

### RGCP

RGCP can represent:

- OPEN;
- PARTIAL;
- ROUTING_UNRESOLVED;
- DISPUTED;
- SPLIT_REQUIRED;
- SUPERSEDED;
- CLOSED_WITH_ALL_CONSTITUENTS_RESOLVED;
- CLOSED_WITH_CONSTITUENTS_REROUTED.

It also preserves:

> **Bundle Completion != Constituent Completion Unless Every Required Constituent Is Resolved Or Legitimately Superseded**

and supports split/reopen/supersession after material state change.

### BRSP

BRSP terminates route search when:

- a route is jointly satisfiable;
- an applicable prohibition blocks the route/objective as scoped;
- a required state remains unresolved and requires external resolution;
- the objective is currently unavailable within evaluated scope;
- further candidate routes are not materially distinct or proportionate.

Key:

> **Route Search Requires Material Distinctness, Not Cosmetic Variation.**

### MKA

MKA terminates an individual proposal when:

- authority is established and the act commits;
- the act is blocked;
- an external owner is required;
- the route is replaced;
- the proposal is withdrawn/otherwise closed according to host state.

It does not treat prior authority as permanently current.

### CBPR

CBPR has explicit commit states:

- COMMIT_STARTED;
- COMMIT_CONFIRMED;
- COMMIT_FAILED;
- COMMIT_STATE_UNKNOWN.

Unknown commit state invokes bounded reconciliation rather than blind retry.

Runtime states also include STOPPED, RETIRED, FAILED and UNKNOWN.

### EERP

EERP distinguishes:

- route conformance;
- consequence conformance;
- evidence adequacy;
- materiality;
- reconciliation state;
- required review.

It may reach NOT_REQUIRED/RECONCILED or route external review/recovery.

It does not turn technical conformance into substantive finality.

### BTA

BTA preserves:

- completion;
- pending/unresolved state;
- failed attempts;
- partial crossing;
- residual effects;
- recovery;
- termination;
- uncertainty/dispute.

It prevents failed partial transitions from being erased as no event.

### KCS Change Propagation

KCS uses:

> **Change upstream → identify materially affected dependents → review selectively → propagate further only when downstream material state changes.**

It supports:

- NO_MATERIAL_DOWNSTREAM_EFFECT;
- REVIEW_REQUIRED;
- REVIEW_OVERDUE;
- UNKNOWN_DEPENDENCY;
- UNKNOWN_EFFECT;
- PROPAGATION_STOPPED;
- PROPAGATION_CONTINUES;
- EXTERNAL_ESCALATION_REQUIRED.

A downstream review that preserves the prior material state stops propagation.

### STRA

STRA explicitly supports:

**WATCHING → CONDITION-SATISFIED → REVIEW-DUE → ACTION-PENDING → COMPLETED**

plus:

- SUPERSEDED;
- RETIRED;
- ROUTING-UNRESOLVED;
- UNKNOWN;
- DISPUTED.

It has:

- direct-cycle detection;
- duplicate activation suppression;
- cascade controls;
- bounded temporal backstops;
- stale/impossible-trigger review;
- supersession/retirement.

## 4. Initial finding

No constituent architecture lacks local closure.

The potential residual issue is instead:

> **Can individually legitimate reopening rules compose into indefinite cross-architecture review circulation even though every local architecture is behaving correctly?**

This is a global liveness/quiescence question.

## 5. Closure is not permanent finality

A major distinction is required:

> **Closed For Current Bounded Evaluation != Permanently Closed**

A system can legitimately finish current work while remaining reopenable if:

- material state changes;
- new evidence arrives;
- a dependency changes;
- a declared trigger fires;
- a prior assumption becomes stale;
- an omitted material dimension is discovered;
- execution deviates materially;
- a transition creates residual state.

Therefore permanent irreversibility is not required for closure.

## 6. Candidate concept — bounded quiescence

A useful integration state is:

### BOUNDED QUIESCENCE

> **No currently represented material review ground requires active work within the declared scope; no unresolved necessary constituent blocks closure; no material downstream propagation remains active; and any future reopening depends on a represented trigger, material change, new evidence, bounded backstop or newly discovered ground.**

This is not “everything is solved.”

It is:

> **No Current Material Work Due Within Declared Scope.**

## 7. Quiescence is not truth

A system may be quiescent while reality remains incompletely represented.

Therefore:

> **Quiescence != Completeness**

and:

> **No Current Review Due != No Possible Future Review**

ESCP remains applicable.

## 8. Quiescence is not authority

A coordination layer must not infer:

> “No review is currently due, therefore the proposed act is authorised.”

Authority remains owned by MKA/external authority sources and must still be current at commit.

Therefore:

> **Quiescence != Authority**

## 9. Quiescence is not conformance

Likewise:

> **No Review Due != Execution Conformant**

EERP independently owns the comparison/reconciliation seam.

## 10. Reopening classes

A quiescent lifecycle may legitimately reopen through materially distinct classes.

### R1 — State change

A represented material state changes.

KCS/STRA may reopen affected work.

### R2 — New evidence

Evidence materially changes a represented conclusion or uncertainty state.

### R3 — Dependency change

A material upstream dependency changes.

### R4 — Trigger satisfaction

A declared STRA condition becomes satisfied.

### R5 — Temporal backstop

No material event has occurred, but a legitimate bounded backstop requires review.

### R6 — Execution deviation

EERP identifies material route/consequence deviation or material unknown/dispute.

### R7 — Transition residual

BTA identifies unresolved/residual state requiring owner review.

### R8 — Completeness discovery

ESCP/ASCP or another legitimate process discovers a previously omitted material dimension.

### R9 — Ownership/routing change

A previously unresolved or changed legitimate owner becomes available.

### R10 — Correction/supersession

A prior representation is corrected or superseded.

## 11. Reopening requires a material basis

The feedback loop must reject:

- “review again because review happened before”;
- exact duplicate triggers;
- cosmetic reroutes;
- unchanged downstream state;
- stale duplicate replicas;
- repeated unresolved routing with no new state/backstop event;
- evidence retrieval that adds no material information.

Therefore:

> **Prior Review != New Review Ground**

and:

> **Loop Iteration Requires Materially Distinct Reopening Basis Or Legitimate Backstop**

## 12. Cross-architecture ping-pong test

Consider:

1. KCS detects dependency change and requests review.
2. STRA routes review.
3. RGCP preserves the dependency ground.
4. BRSP re-evaluates route.
5. Route remains valid.
6. CBPR remains committable.
7. EERP has no new execution deviation.
8. BTA state is unchanged.
9. KCS receives the same represented downstream state.

Correct result:

**PROPAGATION_STOPPED / REVIEW RESOLVED / RETURN TO QUIESCENCE.**

KCS must not generate another candidate review merely because the review cycle itself occurred.

> **Review Activity != Material State Change**

## 13. Review-result ping-pong test

Suppose:

- STRA triggers review;
- review returns the same substantive state;
- KCS records the review;
- the recording event itself is visible to STRA.

If STRA treats “new review record exists” as new material evidence without a trigger definition that distinguishes semantic change, a cycle could arise.

Existing STRA event semantics already require material equivalence rather than superficial event matching.

Therefore:

> **New Record != New Material State**

This is sufficient when correctly integrated.

## 14. Unknown-state ping-pong

An UNKNOWN state may be passed between architectures.

Failure mode:

**UNKNOWN → review → still UNKNOWN → review → still UNKNOWN ...**

Existing local architectures already preserve UNKNOWN rather than inventing certainty.

Global closure additionally requires:

> **Persistent Unknown != Automatic Immediate Re-review**

Where no new evidence/state/backstop exists, UNKNOWN may remain represented while active work returns to bounded quiescence or a bounded waiting state.

If consequence requires resolution before action, the action remains blocked/held; the review machinery need not run continuously.

## 15. Disputed-state ping-pong

Similarly:

**DISPUTED != Continuous Re-adjudication**

Where a legitimate resolver has not changed the dispute state and no new evidence/backstop applies, preserve the dispute and wait/reroute according to legitimate process.

## 16. Routing-unresolved ping-pong

STRA already states that ROUTING-UNRESOLVED requires a bounded review/escalation/backstop and cannot silently become legitimate ownership.

But repeated owner searches without changed information can themselves become an infinite loop.

Candidate rule:

> **Unresolved Routing Requires A Bounded Recheck Condition, Not Continuous Owner Search.**

This is consistent with STRA's backstop model.

## 17. Reroute/review interaction

BRSP may propose R2 after R1 fails.

R2 may create a new contextual/dependency question, producing a new RGCP constituent.

That is legitimate if the ground is materially new.

It is not a cycle merely because the lifecycle returns to review.

> **Return To Earlier Stage != Loop Failure Where Material State/Question Changed**

## 18. Execution/review interaction

EERP deviation may create:

- BTA residual state;
- KCS dependency changes;
- STRA triggers;
- RGCP review grounds.

After those are resolved, a new route may be proposed.

This is a legitimate feedback cycle.

The distinction is:

> **Feedback != Infinite Loop**

A feedback architecture is expected to revisit earlier stages.

The failure condition is unbounded repeated work without materially changed state, question, evidence or legitimate backstop.

## 19. Candidate cycle identity

A host may represent a bounded review episode:

`FeedbackEpisode = <EpisodeID, SubjectRef, InitiatingGroundRefs, Scope, MaterialStateFingerprintRef?, ActiveReviewRefs, RouteRefs, TransitionRefs, ExecutionRefs, ResultingStateRefs, ClosureState, ReopenConditionRefs, Provenance>`

A full state fingerprint is not mandatory.

The purpose is provenance and cycle distinction, not central semantic ownership.

## 20. Candidate closure states

Cross-architecture integration may expose:

- ACTIVE_REVIEW;
- ACTIVE_ROUTE_EVALUATION;
- ACTIVE_COMMIT_RECONCILIATION;
- ACTIVE_EXECUTION_RECONCILIATION;
- ACTIVE_PROPAGATION;
- WAITING_EXTERNAL_OWNER;
- WAITING_NEW_EVIDENCE_OR_STATE;
- BOUNDED_QUIESCENCE;
- CLOSED_SUPERSEDED;
- CLOSED_RETIRED.

These are integration/liveness states only.

They do not replace native states.

## 21. Quiescence conditions

A feedback episode may enter BOUNDED_QUIESCENCE when, within declared scope:

1. no represented material RGCP constituent requires active work;
2. no active route evaluation requires further internal processing;
3. no unresolved commit reconciliation requires active evidence collection;
4. no material EERP reconciliation step remains active;
5. no required BTA transition/recovery action is actively due within the integration layer;
6. KCS has no further material propagation candidate requiring active review;
7. STRA has no currently satisfied unprocessed trigger;
8. unresolved/unknown/disputed states are either:
   - legitimately routed;
   - blocking only the relevant action;
   - or waiting under an explicit recheck/backstop condition;
9. future reopening conditions remain represented where material.

## 22. Quiescence does not require every object to be resolved

An important result:

> **Local Unresolved State != Global Active Work By Default**

For example:

- one authority dispute may remain unresolved;
- the affected route remains blocked;
- no new evidence is expected until an external hearing;
- unrelated work can be quiescent.

Thus:

> **Blocked Pending External Resolution Can Be Operationally Quiescent**

without pretending the substantive dispute is resolved.

## 23. Closure versus waiting

A useful distinction is:

### Resolved closure

Current bounded questions are resolved/superseded/retired.

### Waiting quiescence

A material unresolved state persists, but no legitimate active work is currently due until a represented external event/evidence/backstop.

This avoids two errors:

- endless active review;
- false declaration of substantive completion.

## 24. Adversarial case — permanent unknown

A material fact may never become knowable.

If the consequence architecture permits no action while it remains unknown, the route may remain permanently unavailable.

The review system should not run permanently.

Correct representation:

- substantive state: UNKNOWN;
- route state: blocked/held as applicable;
- review activity: quiescent unless new evidence/backstop;
- provenance: preserved.

> **Permanent Uncertainty != Permanent Computation**

## 25. Adversarial case — recurring periodic review

A legitimate domain may require annual review even if nothing changes.

That is not a loop defect.

The temporal backstop is a legitimate materially represented reopening basis.

> **Repeated Review By Declared Backstop != Unbounded Review Loop**

## 26. Adversarial case — unstable external system

An external dependency changes every few seconds.

KCS/STRA could repeatedly reopen work.

The architecture may require host-supplied materiality, debounce/batching or stability criteria.

Neither KCS nor STRA should invent a universal threshold.

Therefore:

> **High Change Frequency != Infinite-Loop Defect By Itself**

but:

> **Trigger Frequency Requires Consequence-Proportionate Host Bounding Where Repeated Change Would Otherwise Overwhelm Review**

## 27. Adversarial case — self-generated evidence

Review activity creates logs; logs satisfy an evidence trigger; evidence trigger creates review; review creates more logs.

Correct integration requires the trigger to distinguish:

- new record existence;
- materially new evidence about the subject.

Thus:

> **Process Provenance != Substantive Evidence Change By Default**

## 28. Adversarial case — recovery changes state

A recovery action legitimately changes the object.

KCS/STRA reopen review.

This is not ping-pong if the state actually changed.

If recovery returns the object to the same materially represented state, propagation can stop after review confirms no further material downstream change.

## 29. Adversarial case — superseded route

R1 is replaced by R2.

Stale triggers about R1 continue arriving.

RGCP/STRA provenance and supersession must prevent R1 from re-entering active route evaluation unless a legitimate historical/residual ground remains.

> **Stale Route Trigger != Live Route Reopening**

## 30. Adversarial case — partial execution creates new route

R1 partially executes and fails.

A recovery/continuation route R2 is proposed.

R2 must include R1's residual BTA state.

This is a new route evaluation, not continuation of the old pre-execution envelope.

> **Post-Partial-Execution Route != Pre-Execution Alternative Route**

## 31. Adversarial case — duplicate review through different architectures

KCS and EERP independently request what turns out to be the same material owner question.

RGCP may coalesce operational work only after material equivalence is established.

This prevents duplicate work without erasing provenance.

No global controller is required.

## 32. Adversarial case — two reviews continually invalidate each other

Owner A's legitimate state depends on B.
Owner B's legitimate state depends on A.

Each review changes its output when the other changes.

This may represent a genuine unstable coupled system, not merely orchestration failure.

The integration layer must not invent equilibrium.

Correct response may be:

- preserve oscillation/history;
- invoke legitimate domain resolution/stability architecture;
- bound review frequency;
- prevent unsafe commit while required state is unstable.

> **Observed State Oscillation != Integration Authority To Invent Equilibrium**

This exposes no new generic semantic owner.

## 33. Global ownership

No architecture should own “truth of the whole loop.”

Instead:

- RGCP owns review-ground preservation/coalescence;
- BRSP owns thin route-result synthesis;
- MKA owns authority completeness/composition;
- CWA owns contextual topology/permission state;
- CBPR owns runtime/commit boundaries;
- EERP owns thin execution-envelope comparison;
- BTA owns transition interoperability/history;
- KCS owns dependency change propagation;
- STRA owns trigger state/review candidacy;
- external/domain owners own substantive conclusions.

Global closure is therefore a coordination property, not a new substantive authority.

## 34. Candidate shared liveness rule

The strongest cross-architecture rule exposed by the audit is:

> **Continue active feedback only while there is a materially distinct unresolved work item, a material state/evidence change, an unprocessed legitimate trigger, an active reconciliation/transition step, or a due bounded backstop. Otherwise enter bounded quiescence while preserving reopening conditions.**

This rule does not determine substantive outcomes.

## 35. Candidate invariants

FL-01 **Closed For Current Bounded Evaluation != Permanently Closed.**

FL-02 **No Current Review Due != No Possible Future Review.**

FL-03 **Quiescence != Completeness.**

FL-04 **Quiescence != Authority.**

FL-05 **Quiescence != Conformance.**

FL-06 **Prior Review != New Review Ground.**

FL-07 **Loop Iteration Requires Materially Distinct Reopening Basis Or Legitimate Backstop.**

FL-08 **Review Activity != Material State Change.**

FL-09 **New Record != New Material State.**

FL-10 **Persistent Unknown != Automatic Immediate Re-review.**

FL-11 **DISPUTED != Continuous Re-adjudication.**

FL-12 **Unresolved Routing Requires A Bounded Recheck Condition, Not Continuous Owner Search.**

FL-13 **Return To Earlier Stage != Loop Failure Where Material State/Question Changed.**

FL-14 **Feedback != Infinite Loop.**

FL-15 **Local Unresolved State != Global Active Work By Default.**

FL-16 **Blocked Pending External Resolution Can Be Operationally Quiescent.**

FL-17 **Permanent Uncertainty != Permanent Computation.**

FL-18 **Repeated Review By Declared Backstop != Unbounded Review Loop.**

FL-19 **Process Provenance != Substantive Evidence Change By Default.**

FL-20 **Stale Route Trigger != Live Route Reopening.**

FL-21 **Post-Partial-Execution Route != Pre-Execution Alternative Route.**

FL-22 **Observed State Oscillation != Integration Authority To Invent Equilibrium.**

## 36. Does this require a new module?

**NO.**

The audit does not reveal a missing substantive architecture.

The required local mechanisms already exist across:

- STRA cycle/backstop/supersession controls;
- KCS material propagation/stopping;
- RGCP duplicate/equivalence/constituent closure;
- BRSP material route-search termination;
- CBPR commit/reconciliation states;
- EERP reconciliation states;
- BTA partial/residual/recovery states.

The only useful addition is an explicit cross-architecture **bounded quiescence integration pattern**.

That pattern is too thin and too dependent on the existing lifecycle to justify portable extraction at this stage.

## 37. Classification

**INTEGRATION AUDIT: PASS WITH EXPLICIT LIVENESS/QUIESCENCE SYNTHESIS**

Candidate development label:

**Bounded Feedback Quiescence Pattern (BFQP)**

Status:

**CROSS-ARCHITECTURE INTEGRATION PATTERN / PMEDG CANDIDATE / DO NOT EXTRACT YET / NON-CANONICAL**

BFQP is not a scheduler, authority source, adjudicator or universal state owner.

It is the integration discipline that distinguishes:

- active work;
- bounded waiting;
- bounded quiescence;
- legitimate reopening;
- and pathological repeated work without material change.

## 38. Result

The RGCP → BRSP → CBPR → EERP → BTA/KCS/STRA lifecycle has no identified ownership break or mandatory dead-end.

It can close without pretending finality and reopen without requiring permanent activity.

The central liveness synthesis is:

> **No Current Material Work Due Within Declared Scope.**

and the operating rule is:

> **Continue active feedback only while there is a materially distinct unresolved work item, a material state/evidence change, an unprocessed legitimate trigger, an active reconciliation/transition step, or a due bounded backstop. Otherwise enter bounded quiescence while preserving reopening conditions.**

**AUDIT RESULT: PASS.**
