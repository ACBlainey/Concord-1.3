# Execution Conformance — Evaluated Route, Actual Execution and Consequence Reconciliation — Source Resolution 001

**Project:** The Concord Framework
**Date:** 3 October 2026
**Status:** SOURCE RESOLUTION / SUBSTANTIAL REDISCOVERY / NARROW RESIDUAL RECONCILIATION GAP / NON-CANONICAL
**Primary sources:** Concord Bounded Participant Runtime (CBPR), Bounded Transition Architecture (BTA), KCS Change Propagation, Multi-Key Authority (MKA), Bounded Route Synthesis Pattern (BRSP)

## 1. Question

How does the Concord preserve the relationship between:

- the route actually evaluated;
- the route actually authorised/permitted;
- the route actually attempted;
- the route actually executed;
- and the consequence that actually occurred,

especially where execution:

- drifts;
- decomposes across actors/runtimes;
- changes after proposal;
- partially crosses a boundary;
- fails after producing effects;
- or has an unknown commit outcome?

## 2. Source-resolution result

**SUBSTANTIAL REDISCOVERY.**

The Concord already contains most of the required architecture.

### CBPR already owns

- Action Proposal;
- effective target/interface;
- consequence classification;
- commit-time revalidation;
- Action Grants scoped to operation/target/consequence/resource/population;
- composed-effect evaluation;
- sequential/distributed decomposition controls;
- commit states;
- unknown-commit reconciliation;
- result/provenance;
- recovery/retry boundaries.

### BTA already owns

- transition identity/scope;
- multidimensional owner states;
- partial/intermediate crossing;
- failed attempts;
- residual effects;
- rollback/recovery distinction;
- consequential transition provenance/history.

### KCS already owns

- downstream review after material change;
- changed-property filtering;
- scoped change;
- propagation only after material downstream state changes;
- provenance and unknown/disputed effect.

### MKA/BRSP already own upstream route evaluation

- actual act/route/context/consequence;
- route-specific authority;
- rerouting;
- prohibition/context/transition/commit composition.

Therefore:

> **Execution Conformance Is Not A Blank Architectural Gap.**

The remaining issue is narrower:

> **How should the system compare the evaluated route/effect envelope with observed execution/effect and classify materially relevant deviation without becoming the owner of the underlying authority, transition or consequence semantics?**

## 3. Five distinct states

The architecture should not collapse the lifecycle into “approved” and “done.”

At minimum distinguish:

### E1 — Proposed route

What is intended/prepared.

### E2 — Evaluated route

The route/effect envelope actually examined by MKA/CWA/BTA/BRSP/other owners.

### E3 — Commit-authorised route

The route/effect envelope still valid immediately before material commit after revalidation.

### E4 — Executed/attempted route

What the execution system actually attempted/performed.

### E5 — Observed consequence

What materially occurred or can currently be established.

These can diverge.

> **Proposed Route != Evaluated Route != Commit-Authorised Route != Executed Route != Observed Consequence**

## 4. CBPR already binds execution to consequence

CBPR Action Proposal records:

- operation;
- effective target/interface;
- parameters;
- consequence class;
- relevant credential/grant;
- expiry;
- replay/idempotency information where material.

Its Action Grant binds authority to explicit operation, target, consequence, credential, resource, frequency/duration and affected-population scope.

Immediately before material commit, CBPR revalidates current:

- credential;
- action grant;
- effective target;
- output consequence;
- policy/terms;
- service relationship;
- temporal validity;
- dependency/safety;
- required approval/authority;
- composition state.

Therefore the commit boundary already provides the natural reference envelope for conformance comparison.

## 5. Decomposition is already partly solved

CBPR explicitly requires composed-effect evaluation and states that:

- sequential/distributed decomposition must not bypass a bound;
- multiple runtimes do not gain permission to circumvent limits;
- authorised parts do not imply authorised composition.

Therefore:

> **Execution Decomposition != Permission To Escape Evaluated Composition**

No new architecture is needed merely because execution is distributed.

The conformance question is whether the observed combined effect remains within the evaluated/authorised envelope.

## 6. Unknown commit state is already solved as reconciliation

CBPR states:

> **Unknown Commit State != Permission To Retry Blindly.**

Where the external side effect cannot be established, reconciliation uses consequence-proportionate evidence such as:

- operation/idempotency identifier;
- external status query;
- receipt;
- transaction record;
- authorised human/service review.

Therefore unknown execution is not equivalent to failed execution.

> **Unknown Outcome != No Outcome**

## 7. BTA already owns partial execution history

BTA states:

> **Partial Boundary Crossing != Completion Of The Intended Transition.**

and:

> **Failed Transition != No Transition History.**

A failed attempt can preserve:

`<EventRef, CrossingState, ResidualEffectRefs, RecoveryRefs, Provenance>`

Therefore a route that fails after material effect cannot be treated as never executed.

> **Execution Failure != Zero Consequence**

## 8. Proposed comparison object

A thin cross-architecture comparison may use:

`ExecutionConformanceRecord = <ConformanceID, ObjectiveRef, EvaluatedRouteRef, CommitAuthorisedRouteRef, ExecutionAttemptRefs, ObservedEffectRefs, ExpectedEffectEnvelopeRef, DeviationRefs, MaterialityState, ReconciliationState, RequiredReviewRefs, Provenance>`

This is a comparison/reconciliation record.

It does not own:

- authority validity;
- contextual permission;
- transition completion;
- legal culpability;
- substantive safety;
- remedy.

## 9. Expected effect envelope

The comparison should not require byte-for-byte identity between plan and reality.

An evaluated route may legitimately allow bounded variation.

Represent:

`ExpectedEffectEnvelope = <OperationScope, TargetScope, ContextScope, ConsequenceClass, AffectedPopulationScope, Resource/FrequencyBounds, TemporalBounds, CompositionBounds, RequiredTransitionBounds, MaterialToleranceRefs, Provenance>`

A host may use a much smaller representation for low-consequence action.

> **Conformance != Exact Mechanical Identity**

The question is material bounded equivalence.

## 10. Observed execution/effect envelope

Where proportionate and available:

`ObservedExecutionEnvelope = <ActualOperations, EffectiveTargets, EffectiveContexts, Actual/EstimatedConsequences, AffectedPopulation, Resource/FrequencyUse, TemporalState, Composition/ActorRefs, TransitionCrossings, Evidence, Uncertainty, Provenance>`

Observation can be incomplete.

> **Observed Execution != Complete Reality**

ESCP discipline remains applicable.

## 11. Deviation classes

### D0 — No material deviation identified

Observed execution is sufficiently within the evaluated/commit-authorised envelope for the declared scope.

### D1 — Non-material bounded variation

Difference exists but does not materially change authority, permission, protected boundary, consequence class, affected population, transition state or commit condition.

### D2 — Material pre-commit deviation detected

Route/effect changes before consequential commit.

Expected response: re-evaluate/re-authorise before commit where required.

### D3 — Material post-commit execution deviation

Execution after commit begins diverges materially from the authorised/evaluated envelope.

Expected response: stop/contain where legitimately possible; preserve evidence; route review.

### D4 — Material consequence deviation

Executed route may match, but actual consequence materially differs from evaluated expectation.

Expected response: preserve result; route consequence/review/recovery owners.

### D5 — Distributed composition deviation

Individual steps appear bounded but combined execution exceeds the evaluated composition.

Expected response: treat combined effect as material deviation.

### D6 — Unknown conformance

Evidence is insufficient to establish whether material execution/effect stayed within the envelope.

Expected response depends on consequence and external host rules; do not silently mark conformant.

### D7 — Disputed conformance

Legitimate sources disagree.

Preserve dispute and route externally.

## 12. Materiality test

Not every implementation variance requires architectural reopening.

A deviation is materially relevant where it may alter one or more of:

- required authority;
- permission;
- prohibition applicability;
- protected context/boundary;
- consequence class;
- affected population;
- transition completion/residual state;
- resource/frequency bound;
- dependency/safety state;
- recovery/remedy requirement;
- commit legitimacy.

> **Execution Difference != Material Conformance Failure**

but:

> **Material Boundary Change Requires Re-Evaluation Or Post-Event Review As Applicable**

## 13. Pre-commit drift

If the route changes before commit:

1. detect material difference;
2. pause/hold where required;
3. construct actual revised route/effect envelope;
4. send through BRSP/MKA/CWA/BTA/CBPR as applicable;
5. commit only if current requirements pass.

This is already strongly supported by CBPR commit-time revalidation.

> **Changed Route Before Commit != Previously Authorised Route**

## 14. Post-commit drift

Some execution cannot be atomically stopped at the commit boundary.

If material divergence appears after commit begins:

1. preserve actual execution state;
2. stop/contain further consequence where legitimate and technically possible;
3. preserve partial crossing/residual effect through BTA;
4. preserve commit/result provenance through CBPR;
5. identify changed objects/dependencies for KCS;
6. route substantive review/remedy to legitimate owners;
7. do not rewrite the original authorisation as if it covered the deviation.

> **Authorised Start != Unlimited Authority For Emergent Execution Drift**

## 15. Consequence drift without route drift

The same executed operation may produce a materially different real consequence because of environment, failure, interaction or unknown dependency.

Therefore:

> **Route Conformance != Consequence Conformance**

A system should separately compare:

- execution against route envelope;
- consequence against expected consequence envelope.

## 16. Route drift without harmful consequence

An unauthorised/materially different route may accidentally produce the intended benign consequence.

That does not retroactively make the route conformant.

> **Desired Outcome != Execution Conformance**

Likewise:

> **Beneficial Outcome != Authority**

## 17. Post-hoc authorisation

A later owner may determine that a deviation was harmless or grant future authority for the route.

That does not rewrite historical state.

> **Later Permission != Earlier Permission**

> **Later Authority != Earlier Authority**

Historical execution state and later disposition should remain distinct.

## 18. Retry and duplication

Where commit state is unknown:

- reconcile first;
- do not retry blindly;
- use idempotency/operation evidence where available;
- if retry would create another material consequence, independently validate it.

Where a retry does occur, it is a new execution attempt even if it shares an objective.

> **Retry != Proof Previous Attempt Failed**

## 19. Distributed actors

If several actors/runtimes execute parts of one material route:

- preserve actor/component references;
- evaluate the combined effect;
- prevent decomposition bypass;
- compare the observed combined effect to the authorised composition.

No actor should inherit general authority merely because another actor held authority for its own component.

> **Distributed Execution != Distributed Authority Inheritance**

## 20. Observation authority and privacy

Execution conformance does not create unlimited surveillance authority.

Evidence collection must itself respect:

- CWA/contextual permissions;
- law/rights;
- data-access authority;
- proportionality;
- protected spaces;
- purpose/retention limits.

CBPR already describes protected provenance as proportionate and purpose-bounded.

> **Need To Verify Conformance != General Surveillance Authority**

## 21. Reconciliation versus adjudication

A conformance layer may determine:

- whether observed state appears within a declared envelope;
- whether material deviation is present/unknown/disputed;
- what owner reviews are required.

It must not independently determine:

- guilt;
- legal liability;
- moral blame;
- punishment;
- authority exceptions;
- domain remedy.

> **Conformance Classification != Culpability Determination**

## 22. KCS propagation

A material deviation may change represented state of:

- runtime;
- transition;
- dependency;
- product/service;
- authority-relevant facts;
- affected downstream object.

KCS can then generate candidate downstream reviews.

> **Execution Deviation -> Candidate Dependency Review Where Material**

not:

> **Execution Deviation -> Automatic Downstream Invalidity**

## 23. BTA reconciliation

Where execution partially crosses transition boundaries:

- preserve crossing;
- preserve residual effects;
- preserve recovery attempts;
- do not mark rollback as restoration unless prior-state equivalence is established.

Thus:

> **Containment != Restoration**

and:

> **Rollback Activity != Proof Of Prior-State Recovery**

## 24. BRSP relationship

BRSP is primarily pre-commit route synthesis.

Execution conformance is primarily comparison/reconciliation across and after the commit boundary.

The relationship is:

**BRSP evaluated route/effect**
→ **CBPR commit-authorised envelope**
→ **execution attempt**
→ **observed effect**
→ **conformance comparison**
→ **BTA/KCS/owner review where deviation is material**

## 25. Candidate operating sequence

1. Preserve proposed/evaluated route reference.
2. Preserve commit-authorised route/effect envelope.
3. Record execution attempt identity.
4. Observe proportionate execution/result evidence.
5. Compare route dimensions.
6. Compare consequence dimensions.
7. Classify deviation/materiality.
8. If unknown, reconcile proportionately.
9. If material pre-commit deviation, re-evaluate before commit.
10. If material post-commit deviation, stop/contain where legitimate/possible.
11. Preserve BTA partial/residual state.
12. Trigger KCS/STRA/domain review where material.
13. Route substantive consequence/remedy/adjudication externally.
14. Preserve historical distinction between original authority and later disposition.

Compact:

> **Evaluated Route -> Commit Envelope -> Attempt -> Observed Effect -> Compare -> Reconcile -> Review/Contain/Recover**

## 26. Candidate invariants

EC-01 **Proposed Route != Evaluated Route != Commit-Authorised Route != Executed Route != Observed Consequence.**

EC-02 **Conformance != Exact Mechanical Identity.**

EC-03 **Observed Execution != Complete Reality.**

EC-04 **Execution Difference != Material Conformance Failure.**

EC-05 **Changed Route Before Commit != Previously Authorised Route.**

EC-06 **Authorised Start != Unlimited Authority For Emergent Execution Drift.**

EC-07 **Route Conformance != Consequence Conformance.**

EC-08 **Desired Outcome != Execution Conformance.**

EC-09 **Later Permission != Earlier Permission.**

EC-10 **Later Authority != Earlier Authority.**

EC-11 **Retry != Proof Previous Attempt Failed.**

EC-12 **Distributed Execution != Distributed Authority Inheritance.**

EC-13 **Need To Verify Conformance != General Surveillance Authority.**

EC-14 **Conformance Classification != Culpability Determination.**

EC-15 **Containment != Restoration.**

EC-16 **Execution Deviation -> Candidate Dependency Review Where Material.**

## 27. Failure tests

### F1 — proposal treated as execution

Prepared action is assumed to have occurred.

**FAIL.**

### F2 — authorised route treated as observed route

System assumes actual execution matched authorisation without evidence.

**FAIL.**

### F3 — successful outcome launders drift

Unauthorised material route produces desired result and is marked conformant.

**FAIL.**

### F4 — harmless implementation variation triggers full crisis

A non-material internal variation changes no protected/effect boundary but forces complete re-authorisation.

**OVERREACTION.**

### F5 — distributed bypass

Several bounded actors collectively produce an effect outside the authorised composition.

**FAIL.**

### F6 — blind retry

Commit outcome is unknown and the action is repeated.

**FAIL.**

### F7 — failed transition erased

Partial material crossing occurred but failure causes history to be recorded as no execution.

**FAIL.**

### F8 — rollback assumed restorative

Rollback command completes and prior state is assumed restored without evidence.

**FAIL.**

### F9 — conformance monitor becomes surveillance authority

Monitoring collects unrestricted participant data because conformance is useful.

**FAIL.**

### F10 — deviation classifier assigns culpability

Technical divergence is automatically treated as misconduct.

**FAIL.**

## 28. Residual gap classification

The substantive mechanisms are already present.

What is not yet explicit as a single cross-architecture pattern is the **comparison and reconciliation seam**:

> evaluated/commit-authorised envelope
> versus
> observed execution/effect envelope.

This is thinner than a new execution-control architecture.

## 29. Candidate development label

**Execution Envelope Reconciliation Pattern (EERP)**

Development definition:

> **Compare the materially relevant route and consequence envelope evaluated/authorised at commit with proportionately observed execution and effect; classify material deviation, unknown or dispute; preserve provenance and partial state; and route re-evaluation, containment, recovery or substantive review to the legitimate existing owners.**

EERP does not authorise execution and does not determine culpability.

## 30. Is a new portable module established?

**NO.**

Current classification:

**CROSS-ARCHITECTURE INTEGRATION PATTERN / PMEDG CANDIDATE / DO NOT EXTRACT YET / NON-CANONICAL**

The mechanism must first be adversarially tested against:

- bounded variation;
- pre-commit route drift;
- post-commit route drift;
- consequence-only drift;
- distributed decomposition;
- unknown commit state;
- retries/idempotency;
- partial transition;
- rollback;
- stale observations;
- incomplete observation;
- protected evidence;
- later authorisation;
- disputed execution facts;
- multi-actor execution;
- emergency execution;
- execution after revocation;
- route drift that changes affected population;
- benign outcome through unauthorised route;
- harmful outcome through conformant route;
- monitor overreach;
- false culpability inference.

## 31. Result

**SOURCE RESOLUTION: SUBSTANTIAL REDISCOVERY / NARROW RESIDUAL RECONCILIATION GAP**

Do not create a generic execution-conformance authority.

CBPR and BTA already own most of the mechanism.

Develop/test EERP only as a thin comparison/reconciliation pattern around existing owners.
