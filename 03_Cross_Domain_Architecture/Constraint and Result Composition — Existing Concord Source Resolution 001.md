# Constraint and Result Composition — Existing Concord Source Resolution 001

**Project:** The Concord Framework
**Date:** 3 October 2026
**Status:** SOURCE RESOLUTION / SUBSTANTIAL REDISCOVERY / RESIDUAL ROUTE-SYNTHESIS GAP / NON-CANONICAL
**Primary sources:** Multi-Key Authority (MKA), Concord Bounded Participant Runtime (CBPR), Contextual Wrapper Architecture (CWA), Bounded Transition Architecture (BTA), Triadic Decision Making, Review-Ground Composition Pattern (RGCP)

## 1. Question

When several independently legitimate review results apply to the same proposed consequential act, how should the system determine whether the act:

- may proceed;
- must be narrowed;
- must use another route;
- must wait for unresolved state;
- is blocked;
- or requires an externally authorised discretionary decision?

This question emerged from the Review-Ground Composition Pattern after review grounds themselves had been preserved successfully.

## 2. Source-resolution result

**SUBSTANTIAL REDISCOVERY.**

The Concord already contains most of the required composition architecture.

The problem is not a blank “constraint conflict” space.

Existing ownership is distributed:

- **MKA** composes and verifies independently necessary authority for the actual act, route, context and consequence and consumes applicable upstream prohibitions.
- **CWA** represents contextual permissions, restrictions, simultaneous contexts and known conflict/priority rules while refusing to invent a universal priority algorithm.
- **BTA** composes transition-state references and prevents completion/authority/permission in one dimension from silently propagating into another.
- **CBPR** evaluates the materially composed effect at consequential commit and refuses commit where required state fails or remains materially unresolved.
- **Triadic Decision Making** provides a decision procedure only where legitimate decision authority exists; it does not manufacture authority or override external constraints.
- **RGCP** preserves independently grounded review results and their provenance before composition.

Therefore:

> **Constraint/Result Composition Is Largely An Existing Distributed Function, Not A Missing Central Decision Architecture.**

## 3. MKA is the primary authority-composition owner

MKA already asks:

> **How can a system determine whether every independently necessary authority for an actual consequential act and route is represented, legitimately grounded, current, within scope, composable where required, and not blocked by an applicable prohibition?**

Its portable kernel states:

> **A consequential act may proceed only where every independently necessary authority for the actual route, context and consequence is represented to a proportionate completeness standard, independently legitimate, current, within scope, validly composable where composition is required, and not blocked by an applicable upstream prohibition.**

This already covers a large portion of the apparent constraint/result problem.

MKA also preserves:

- permission-before-authority;
- actual act/route granularity;
- ASCP authority-space completeness;
- independently grounded keys;
- composition rules;
- upstream prohibitions;
- emergency authority boundaries;
- proposal/commit revalidation;
- rerouting;
- unknown/disputed states;
- external-owner handoff.

Core:

> **Authority Does Not Automatically Compose.**

> **Positive-Key Completeness != Complete Authority Space.**

> **Blocked Route != Forbidden Objective By Default.**

## 4. Hard prohibition versus missing positive authority

These must not be collapsed.

### Missing positive authority

A necessary authority key is absent, invalid, expired, out of scope, unknown or disputed.

Possible MKA states include:

- HOLD_MISSING_AUTHORITY;
- HOLD_UNKNOWN_AUTHORITY;
- HOLD_DISPUTED_AUTHORITY;
- BLOCK_INVALID_AUTHORITY;
- BLOCK_OUT_OF_SCOPE;
- REVALIDATION_REQUIRED;
- EXTERNAL_OWNER_REQUIRED.

### Applicable prohibition

An upstream legitimate prohibition applies to the act/route/context.

MKA explicitly states that positive authority is insufficient where such a prohibition blocks the act.

Therefore:

> **All Positive Requirements Satisfied != Act Permitted Where Applicable Prohibition Blocks**

and:

> **Missing Authority != Prohibition**

The remediation path may differ.

## 5. Objective versus route

MKA explicitly separates objective from route.

> **Same Objective != Same Authority Path**

> **Blocked Route != Forbidden Objective By Default**

This is central.

A conflict may invalidate one route without invalidating the objective.

Therefore composition should first ask whether an alternative legitimate route exists before treating a route-specific failure as a global objective prohibition.

## 6. CWA owns contextual constraint representation

CWA already requires simultaneous applicable contexts and known conflict/priority rules to be represented.

Its composition section requires:

1. identify applicable wrappers;
2. identify conflicts;
3. identify legitimate conflict/priority rules;
4. preserve unresolved conflict where none exists.

CWA states:

> **Wrapper composition requires explicit conflict and priority handling.**

But also:

> **CWA v1.0 does not claim a universal composition algorithm.**

and:

> **Information architecture != decision authority.**

Therefore CWA detects and represents contextual conflict but does not create authority to resolve it.

This is not a gap; it is a deliberate boundary.

## 7. BTA owns transition coherence, not conflict sovereignty

BTA permits different owner systems to report different legitimate states for the same transition.

It prevents:

- local completion becoming integrated completion;
- transition need creating authority;
- authority/permission silently propagating;
- failed partial transitions being erased.

BTA may determine whether declared integration-contract conditions are satisfied, pending, failed or unresolved.

Therefore:

> **Different Owner States != Error By Default**

and:

> **Completion In One Dimension != Completion Of The Bounded Transition**

BTA does not need to resolve every substantive conflict. It needs to preserve the states and apply the declared completion contract.

## 8. CBPR owns consequential commit gating

CBPR already contains a composition evaluation for the materially relevant combined effect:

`COMPOSED_EFFECT(X,C)`

It requires current permissions, current authority where required, authorised combined consequence/data movement/target scope, no decomposition bypass and valid cumulative bounds.

At commit:

> **A required FAIL means NOT_COMMITTABLE.**

> **A materially required UNRESOLVED state cannot be treated as COMMITTABLE.**

and:

> **Authorised Parts != Authorised Composition.**

Thus CBPR provides the final technical/consequential gate.

It does not decide the substantive authority rules it consumes.

## 9. Triadic Decision Making is downstream, not a universal resolver

Triadic Decision Making requires the decision and its authority to be defined before the triad exercises the decision rule.

It can support decisions where:

- several legitimate options remain;
- evidence must be weighed;
- discretion is legitimately delegated;
- escalation is authorised.

It cannot convert a prohibited or unauthorised act into an authorised one by majority vote.

Therefore:

> **Decision Procedure != Authority Source**

> **Majority Decision != Override Of Upstream Prohibition By Default**

A triad may select among legitimate routes only where its authority includes that selection.

## 10. Result classes

The source resolution supports distinguishing at least six result classes.

### R1 — Positive prerequisite / authority requirement

A condition that must be satisfied before a route may proceed.

Owner examples: MKA/external authority source.

### R2 — Prohibition

A legitimate rule blocking the act or route unless a legitimate exception/override applies.

Owner: external law/constitutional/contextual authority consumed by MKA/CWA.

### R3 — Contextual permission/restriction

A context-bounded permission, restriction, protected boundary or local rule.

Owner: CWA/context owner.

### R4 — Transition/completion condition

A condition required for a bounded transition to be considered coherently complete.

Owner: BTA plus external state owners.

### R5 — Runtime/commit condition

A technical/consequential condition required at the point of commit.

Owner: CBPR plus external supplied state.

### R6 — Discretionary decision factor

A factor to be weighed where legitimate authority leaves more than one permitted option.

Owner: legitimate substantive decision process, potentially including Triadic Decision Making.

These classes should not be flattened into one scalar “constraint score.”

## 11. Composition precedence is not a universal ranking

There is no evidence in the examined architecture for a universal rule such as:

`Law > Safety > Rights > Efficiency`

or any other global scalar priority.

Instead, precedence is source-grounded and relation-specific.

Examples:

- an applicable constitutional prohibition may block an authority otherwise valid;
- a context-specific restriction may alter the permitted route;
- an exception may apply only if an external legitimate rule establishes it;
- a transition may remain incomplete even though authority exists;
- a runtime may remain not committable even though substantive approval exists.

Therefore:

> **Composition Requires Applicable Rules, Not A Universal Constraint Ranking**

## 12. Candidate act-evaluation object

A cross-architecture act evaluation can be represented as:

`ActEvaluation = <ObjectiveRef, ActRef, RouteRef, TargetRef, ContextRefs, ConsequenceRef, ReviewResultRefs, RequiredAuthorityRefs, PermissionRefs, ProhibitionRefs, TransitionConditionRefs, CommitConditionRefs, DiscretionaryDecisionRefs, ExternalOwnerRefs, State, Provenance>`

This is an integration object only.

It does not own the referenced semantics.

## 13. Candidate composition sequence

A source-compatible sequence is:

1. **Define objective.**
2. **Define actual proposed act and route.**
3. **Resolve applicable contexts.**
4. **Attach RGCP-preserved review results.**
5. **Classify results by external semantic owner/function.**
6. **Check whether bounded permission is sufficient.**
7. **Identify required independent authority dimensions.**
8. **Check authority-space completeness.**
9. **Validate each required authority key.**
10. **Apply legitimate composition/inheritance rules.**
11. **Check applicable upstream prohibitions and legitimate exceptions.**
12. **Check contextual permissions/restrictions.**
13. **Check required transition-state/completion conditions.**
14. **Check dependency/safety/runtime conditions.**
15. **If route fails, test legitimate alternative route where available.**
16. **If several legitimate options remain, route discretionary choice to legitimate decision authority.**
17. **Revalidate material state at consequential commit.**
18. **Commit only if all materially required commit conditions are satisfied.**
19. **Preserve outcome/provenance and later review triggers.**

Compact:

> **Objective → Actual Act/Route → Context → Authority Completeness → Authority Validity/Composition → Prohibitions → Contextual Constraints → Transition Conditions → Commit Conditions → Reroute/External Decision If Needed → Commit-Time Revalidation**

## 14. Outcome vocabulary

The existing modules already support most useful outcomes.

A cross-architecture integration layer may map them without replacing native states:

- PERMISSION_SUFFICIENT;
- AUTHORISED_FOR_ROUTE;
- HOLD_MISSING_REQUIREMENT;
- HOLD_UNKNOWN;
- HOLD_DISPUTED;
- BLOCK_PROHIBITED;
- BLOCK_OUT_OF_SCOPE;
- ROUTE_NOT_PERMITTED;
- TRANSITION_PENDING;
- TRANSITION_FAILED;
- NOT_COMMITTABLE;
- REROUTE_AVAILABLE;
- EXTERNAL_OWNER_REQUIRED;
- DISCRETIONARY_DECISION_REQUIRED;
- COMMITTABLE.

These are integration labels, not universal substantive verdicts.

## 15. Alternative-route rule

A failed route should be distinguished from a failed objective.

Candidate rule:

> **Where a proposed route fails a material permission, authority, contextual, transition or commit condition, test whether the objective can be satisfied through another legitimate bounded route before classifying the objective itself as unavailable.**

This extends MKA's established:

> **Blocked Route != Forbidden Objective By Default**

without creating a right to reroute around a genuine prohibition.

> **Alternative Route != Prohibition Evasion**

## 16. Conflict handling

When two results appear incompatible:

### Step A — confirm same act/route/scope/context

Apparent conflict may disappear after AUR/context resolution.

### Step B — identify semantic owners

Do not ask a generic coordinator to reinterpret them.

### Step C — determine relationship

Possible relationships:

- both requirements can be jointly satisfied;
- one is route-specific;
- one is stale/superseded;
- an externally legitimate precedence/exception rule applies;
- requirements are genuinely incompatible;
- state remains unknown/disputed.

### Step D — test alternative route

Only where legitimate.

### Step E — external resolution

If genuine conflict remains and an authorised resolver exists, route it there.

If no resolver exists, preserve unresolved state.

> **Conflict Detection != Authority To Resolve Conflict**

## 17. No “constraint voting”

Independent constraints are not votes.

Three permissions do not outvote one applicable prohibition.

Five positive review results do not cancel one required unresolved authority dimension.

A triadic decision cannot vote away a boundary outside its legitimate discretion.

> **Constraint Count != Constraint Precedence**

## 18. No universal scalar composition

Do not reduce:

- authority;
- rights;
- permission;
- prohibition;
- transition completion;
- runtime safety;
- evidence completeness

into a single score and permit action above a threshold.

The dimensions have different semantics.

> **Cross-Domain Constraint Composition != Weighted Sum By Default**

## 19. Emergency handling

Urgency does not erase the architecture.

MKA already establishes:

> **Emergency != Authority Vacuum**

> **Emergency Need != Unlimited Emergency Authority**

An emergency may activate different externally legitimate authority, context or transition rules.

Those rules must themselves be represented and bounded.

## 20. Unknown/disputed states

Unknown or disputed state is not silently permission and not silently prohibition.

Its consequence depends on whether the unresolved dimension is materially required for the proposed act.

At commit, CBPR establishes:

> **A materially required UNRESOLVED state cannot be treated as COMMITTABLE.**

Thus:

> **Unresolved Required Dimension != Committable**

without asserting:

> **All Uncertainty != Permanent Prohibition**

## 21. Review composition interface

RGCP remains upstream.

Its role is:

many review grounds
→ potentially shared work/evidence
→ independently owned results.

Constraint/result composition consumes those results.

It must not retroactively merge their grounds.

> **Result Composition != Review-Ground Erasure**

## 22. Residual gap

After source resolution, the remaining gap is small.

The Concord has the necessary substantive components, but lacks a single compact cross-architecture **route-synthesis integration pattern** that says:

- how to collect already-owned result classes;
- how to preserve their semantic owners;
- how to test joint satisfiability;
- how to distinguish route failure from objective failure;
- when to seek an alternative route;
- when to hand off genuine discretion;
- when unresolved required state prevents commit.

This appears to be an integration grammar, not a new substantive authority system.

## 23. Candidate development label

**Bounded Route Synthesis Pattern (BRSP)**

Development meaning:

> **Compose externally owned permissions, authorities, prohibitions, contextual restrictions, transition conditions and commit conditions around an actual proposed route; where the route fails, search only for legitimate alternative routes; never manufacture authority, override prohibition or absorb substantive ownership.**

This is a development label only.

## 24. Candidate invariants

BRSP-01 **Actual Route Determines Applicable Composition.**

BRSP-02 **Blocked Route != Forbidden Objective By Default.**

BRSP-03 **Alternative Route != Prohibition Evasion.**

BRSP-04 **Constraint Count != Constraint Precedence.**

BRSP-05 **Conflict Detection != Authority To Resolve Conflict.**

BRSP-06 **Decision Procedure != Authority Source.**

BRSP-07 **Result Composition != Review-Ground Erasure.**

BRSP-08 **Unresolved Required Dimension != Committable.**

BRSP-09 **Cross-Domain Constraint Composition != Weighted Sum By Default.**

BRSP-10 **Composition Requires Applicable Rules, Not A Universal Constraint Ranking.**

BRSP-11 **Different Owner States != Error By Default.**

BRSP-12 **Authorised Parts != Authorised Composition.**

BRSP-13 **Commit-Time State != Proposal-Time State By Default.**

BRSP-14 **Route Synthesis != Substantive Sovereignty.**

## 25. Failure examples

### F1 — majority overrides prohibition

Three favourable review results and one applicable prohibition are treated as a 3:1 approval.

**FAIL.**

### F2 — authority implies transition completion

All MKA keys validate, so BTA transition is marked complete.

**FAIL.**

### F3 — transition completion implies authority

BTA reports complete, so MKA authority is inferred.

**FAIL.**

### F4 — runtime capability implies permission

CBPR can technically execute the route, so contextual permission is assumed.

**FAIL.**

### F5 — universal safety score

All dimensions are reduced to one number.

**FAIL unless an externally legitimate domain rule specifically owns that decision and the reduction is valid for that bounded purpose.**

### F6 — reroute around prohibition

Route A is prohibited, so the system disguises the same prohibited consequence as route B.

**FAIL.**

### F7 — legitimate reroute

Route A requires unavailable coercive authority; route B achieves the objective through valid participant permission without crossing the protected boundary.

**POTENTIALLY VALID**, subject to full evaluation of route B.

### F8 — unresolved required authority

All technical/contextual conditions pass but one materially required authority dimension remains unknown.

**NOT COMMITTABLE.**

### F9 — discretionary choice

Routes A and B are both legitimate and complete; selecting between them is delegated to an authorised decision owner.

**VALID HANDOFF.**

Triadic Decision Making may be used if that owner/process legitimately adopts it.

## 26. Is a new portable module established?

**NO.**

The substantive composition semantics are already distributed across graduated modules.

Creating a new portable “constraint composition” module now would risk duplicating MKA and CBPR or centralising CWA/BTA semantics.

The residual BRSP mechanism is best treated as:

**CROSS-ARCHITECTURE INTEGRATION PATTERN / PMEDG CANDIDATE / DO NOT EXTRACT YET**

## 27. Recommended next test

Run:

**Bounded Route Synthesis Pattern — Adversarial Integration Test 001**

At minimum test:

- all requirements jointly satisfiable;
- missing positive authority;
- applicable prohibition;
- prohibition with legitimate exception;
- route-specific restriction with valid alternative;
- disguised prohibition evasion;
- contextual conflict with no precedence rule;
- transition incomplete despite authority;
- authority missing despite transition complete;
- runtime unable despite substantive permission;
- runtime capable but not authorised;
- unknown required state;
- disputed state with external resolver;
- disputed state without resolver;
- two legitimate routes requiring discretionary selection;
- emergency route with bounded emergency authority;
- proposal valid but commit state changed;
- RGCP constituent results with incompatible dimensions;
- stale result included in composition;
- false scalar scoring;
- triadic majority attempting to override non-discretionary constraint;
- low-authority permission-sufficient route replacing coercive route;
- objective impossible under every legitimate route;
- alternative route changes affected population/consequence and therefore required authority set;
- partial transition creates residual duties after route failure.

## 28. Result

**SOURCE RESOLUTION: SUBSTANTIAL REDISCOVERY / SMALL RESIDUAL INTEGRATION GAP**

The Concord already contains the core composition logic.

Do not create a new general constraint-resolution authority.

Develop and test BRSP only as a thin integration pattern around existing semantic owners.

