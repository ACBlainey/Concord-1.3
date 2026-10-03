# Bounded Route Synthesis Pattern — Adversarial Integration Test 001

**Project:** The Concord Framework
**Date:** 3 October 2026
**Status:** ADVERSARIAL INTEGRATION TEST / COMPLETE / NON-CANONICAL
**Source resolution:** Constraint and Result Composition — Existing Concord Source Resolution 001
**Development label:** Bounded Route Synthesis Pattern (BRSP)
**Architectures tested:** MKA/ASCP, CWA, BTA, CBPR, RGCP, Triadic Decision Making and external substantive owners

## 1. Test question

Can a thin integration pattern compose externally owned results around an actual proposed route and distinguish:

- proceed;
- hold;
- block;
- reroute;
- narrow;
- externally resolve;
- or make a legitimate discretionary choice

without becoming a new authority source, universal priority engine or substantive semantic owner?

## 2. Candidate BRSP rule

> **Compose externally owned permissions, authorities, prohibitions, contextual restrictions, transition conditions and commit conditions around an actual proposed route; where the route fails, search only for legitimate alternative routes; never manufacture authority, override prohibition or absorb substantive ownership.**

## 3. Pass conditions

BRSP passes only if it preserves:

1. actual act/route specificity;
2. permission-before-authority where applicable;
3. independent authority ownership;
4. prohibition precedence only where externally legitimate;
5. contextual ownership;
6. transition-state ownership;
7. commit-time gating;
8. alternative-route legitimacy;
9. external dispute/decision ownership;
10. provenance and RGCP review-ground separation;
11. non-scalar multidimensional composition;
12. no automatic inference from technical capability;
13. no automatic inference from transition completion;
14. no automatic inference from positive-result count.

## 4. Scenario 1 — all requirements jointly satisfiable

Route R1 has valid permission/authority, no applicable prohibition, compatible contextual state, satisfied transition conditions and current commit conditions.

**Expected:** route may reach COMMITTABLE subject to ordinary commit-time revalidation.

**Result:** PASS.

> **Joint Satisfaction May Permit Commit; It Does Not Create The Underlying Authority.**

## 5. Scenario 2 — missing positive authority

All non-authority conditions pass, but one independently necessary MKA key is absent.

**Expected:** HOLD_MISSING_AUTHORITY / NOT_COMMITTABLE.

**Result:** PASS.

BRSP cannot substitute favourable contextual or technical results.

## 6. Scenario 3 — applicable prohibition

Every positive authority key is valid, but a legitimate upstream prohibition applies.

**Expected:** BLOCK_PROHIBITED for the affected act/route.

**Result:** PASS.

> **Positive Satisfaction Does Not Cancel Applicable Prohibition.**

## 7. Scenario 4 — prohibition with legitimate exception

A prohibition applies generally, but the external legitimate source contains an exception whose factual predicates are currently satisfied.

**Expected:** evaluate the route under that externally owned exception.

**Result:** PASS.

BRSP does not invent or broaden the exception.

> **Exception Must Be Source-Grounded.**

## 8. Scenario 5 — route-specific restriction with valid alternative

Objective O can be achieved through R1 or R2.

R1 crosses a protected context without valid permission.
R2 avoids that boundary and has its own valid permission/authority state.

**Expected:** R1 fails; R2 is evaluated independently and may proceed.

**Result:** PASS.

> **Blocked Route != Forbidden Objective By Default.**

## 9. Scenario 6 — disguised prohibition evasion

R1 is prohibited because consequence C is forbidden.

R2 changes superficial technical steps but intentionally produces the same prohibited consequence C.

**Expected:** R2 remains blocked where the prohibition applies to C or its relevant equivalent scope.

**Result:** PASS.

> **Alternative Route != Prohibition Evasion.**

## 10. Scenario 7 — contextual conflict with no precedence rule

Two simultaneously applicable contextual wrappers impose materially incompatible requirements. No legitimate priority/resolution rule is represented.

**Expected:** preserve unresolved conflict; EXTERNAL_OWNER_REQUIRED or equivalent hold.

**Result:** PASS.

> **Conflict Detection != Authority To Resolve Conflict.**

## 11. Scenario 8 — transition incomplete despite authority

All MKA authority requirements pass, but BTA reports a materially required transition condition pending.

**Expected:** TRANSITION_PENDING / NOT_COMMITTABLE where completion is required for the act.

**Result:** PASS.

> **Authority != Transition Completion.**

## 12. Scenario 9 — authority missing despite transition complete

BTA reports the transition complete, but a current required authority key is missing.

**Expected:** NOT_COMMITTABLE.

**Result:** PASS.

> **Transition Completion != Authority.**

## 13. Scenario 10 — runtime unable despite substantive permission

The act is permitted and authorised, but CBPR cannot safely/effectively perform the required commit.

**Expected:** NOT_COMMITTABLE through that runtime/route.

**Result:** PASS.

A different legitimate execution route may be considered.

## 14. Scenario 11 — runtime capable but not authorised

CBPR can technically perform the action, but authority is absent.

**Expected:** NOT_COMMITTABLE.

**Result:** PASS.

> **Execution Capability != Permission For External Action.**

## 15. Scenario 12 — unknown required state

A materially required authority/context/transition state is UNKNOWN.

**Expected:** HOLD/UNRESOLVED; cannot silently become COMMITTABLE.

**Result:** PASS.

> **Unresolved Required Dimension != Committable.**

## 16. Scenario 13 — disputed state with external resolver

A required authority relation is disputed and a legitimate external adjudicator/resolver exists.

**Expected:** hand off; preserve route state pending resolution.

**Result:** PASS.

BRSP does not adjudicate.

## 17. Scenario 14 — disputed state without resolver

The same dispute exists but no legitimate resolver is identified.

**Expected:** preserve disputed/unresolved state rather than invent precedence.

**Result:** PASS.

> **No Resolver != Coordinator Sovereignty.**

## 18. Scenario 15 — two legitimate routes requiring discretionary selection

R1 and R2 are both valid and complete. Selection is genuinely discretionary under a legitimate decision owner.

**Expected:** hand off the choice to that owner/process.

Triadic Decision Making may be used if legitimately adopted.

**Result:** PASS.

> **Decision Procedure != Authority Source.**

## 19. Scenario 16 — emergency route with bounded emergency authority

Normal route R1 is unavailable. A legitimate emergency authority source activates R2 under defined predicates and scope.

**Expected:** evaluate R2 under the emergency authority and all remaining applicable constraints.

**Result:** PASS.

> **Emergency != Authority Vacuum.**

## 20. Scenario 17 — urgency without emergency authority

The objective is urgent, but no alternative emergency authority exists.

**Expected:** urgency does not manufacture authority.

**Result:** PASS.

> **Urgency != Authority.**

## 21. Scenario 18 — proposal valid, commit state changed

R1 passes at proposal. Before commit, a credential is revoked or context changes.

**Expected:** commit-time revalidation detects change; route becomes NOT_COMMITTABLE or is re-evaluated.

**Result:** PASS.

> **Authority At Proposal != Authority At Commit.**

## 22. Scenario 19 — RGCP results with incompatible dimensions

RGCP returns:

- dependency state satisfied;
- ESCP completeness adequate within scope;
- CWA route restriction active;
- BTA transition ready.

**Expected:** BRSP preserves all results; CWA restriction is not outvoted by three favourable results.

**Result:** PASS.

> **Constraint Count != Constraint Precedence.**

## 23. Scenario 20 — stale result included

A previously favourable MKA/CWA result is stale after material state change.

**Expected:** freshness failure triggers revalidation; stale result cannot satisfy current route.

**Result:** PASS.

## 24. Scenario 21 — false scalar scoring

Host assigns each result +1/-1 and proceeds because total score is positive.

**Expected:** FAIL CONTAINED.

Different dimensions are not interchangeable votes.

> **Cross-Domain Constraint Composition != Weighted Sum By Default.**

## 25. Scenario 22 — triadic majority attempts to override prohibition

A triad votes 3-0 to proceed despite an applicable prohibition outside the triad's override authority.

**Expected:** prohibition remains effective.

**Result:** PASS.

> **Majority Decision != Override Authority.**

## 26. Scenario 23 — permission-sufficient route replaces coercive route

R1 would require institutional coercive authority.
R2 achieves the same legitimate objective through valid voluntary participant permission and crosses no additional protected boundary.

**Expected:** R2 may be evaluated as permission-sufficient rather than manufacturing an authority requirement.

**Result:** PASS.

This confirms a strong route-synthesis value:

> **Prefer Legitimate Lower-Authority Routes Where They Actually Satisfy The Objective And Boundaries.**

This is not a universal optimisation command; it follows the existing permission-before-authority logic.

## 27. Scenario 24 — objective impossible under every legitimate route

Every materially distinct route either violates an applicable prohibition, lacks a required authority with no legitimate path to obtain it, or cannot satisfy required transition/commit conditions.

**Expected:** objective currently unavailable.

**Result:** PASS.

BRSP does not search indefinitely for semantic disguises.

> **No Legitimate Route Found After Proportionate Search -> Objective Currently Unavailable Within Evaluated Scope.**

This is time/scope indexed, not metaphysical impossibility.

## 28. Scenario 25 — alternative route changes affected population

R1 affects participant A.
R2 avoids R1's restriction but affects A, B and C.

**Expected:** R2 must receive a fresh authority/context/consequence evaluation for its actual affected population.

**Result:** PASS.

> **Reroute Changes Consequence -> Recompute Applicable Requirements.**

## 29. Scenario 26 — alternative route changes consequence class

R1 performs reversible temporary access.
R2 achieves the objective through irreversible deletion.

**Expected:** R2 cannot inherit R1's approval state.

**Result:** PASS.

> **Same Objective != Same Consequence != Same Authority Path.**

## 30. Scenario 27 — partial transition creates residual duties

R1 begins, partially crosses a boundary, then fails.

BTA records residual state/duties.

**Expected:** BRSP cannot simply start R2 as if R1 never occurred.

Residual obligations must be included in R2 evaluation where material.

**Result:** PASS.

> **Failed Route != No Route History.**

## 31. Scenario 28 — route narrowing

R1 as proposed exceeds authority scope.
A narrower R1a remains within legitimate scope and still achieves a bounded version of the objective.

**Expected:** R1a may be separately evaluated.

**Result:** PASS.

> **Narrowed Act != Original Act By Default.**

The objective/consequence record must reflect the narrowing.

## 32. Scenario 29 — external precedence rule

Two contextual rules conflict, but a legitimate external source explicitly defines which governs in this exact relation.

**Expected:** consume the precedence rule; do not infer a general hierarchy beyond its scope.

**Result:** PASS.

> **Local Precedence Rule != Universal Constraint Ranking.**

## 33. Scenario 30 — exception authority absent

A prohibition contains a possible exception, but the actor lacks authority to invoke or determine that exception.

**Expected:** BRSP cannot self-apply the exception beyond externally supplied legitimate semantics.

**Result:** PASS.

## 34. Scenario 31 — decomposition bypass

A prohibited or bounded composed effect is divided among multiple runtimes/agents so each individual step appears locally acceptable.

**Expected:** CBPR composed-effect evaluation detects the materially combined consequence.

**Result:** PASS.

> **Authorised Parts != Authorised Composition.**

## 35. Scenario 32 — serial rerouting loop

R1 fails, then R2, R3, R4 each fail for materially equivalent reasons and generate another cosmetic route.

**Expected:** stop when further routes are not materially distinct or proportionate.

**Result:** PASS.

Candidate rule:

> **Route Search Requires Material Distinctness, Not Cosmetic Variation.**

This prevents rerouting from becoming an infinite evasion/search loop.

## 36. Scenario 33 — new route reveals missing dimension

R2 appears valid, but ESCP/ASCP identifies a previously unrepresented protected boundary.

**Expected:** R2 returns to review/hold until the material dimension is resolved proportionately.

**Result:** PASS.

> **Candidate Route != Demonstrated Complete Route Space.**

## 37. Scenario 34 — result owner changes

A rule previously owned by system S1 is legitimately transferred to S2.

**Expected:** current ownership/provenance must be revalidated before using the result.

**Result:** PASS.

No semantic inheritance is inferred merely from system continuity.

## 38. Scenario 35 — conflicting facts, same rule

The applicable rule is clear but two legitimate sources disagree on a material factual predicate.

**Expected:** preserve factual dispute and use the relevant external evidence/adjudication architecture.

**Result:** PASS.

BRSP does not select whichever fact permits the preferred route.

## 39. Scenario 36 — conflicting rules, same facts

Facts are agreed but two apparently applicable rules conflict.

**Expected:** check scope, context, precedence, exception and resolver authority. Preserve unresolved state if no legitimate resolution exists.

**Result:** PASS.

## 40. Scenario 37 — beneficial outcome argument

R1 lacks authority, but projected benefit is very high.

**Expected:** benefit alone does not manufacture authority.

**Result:** PASS.

> **Beneficial Outcome != Authority.**

## 41. Scenario 38 — owner requests impossible composition

An owner legitimately controls one constraint but instructs BRSP to ignore another independently owned required constraint.

**Expected:** instruction is effective only within the owner's legitimate scope; it cannot erase another owner's independent boundary.

**Result:** PASS.

> **Authority Over One Dimension != Authority Over Every Dimension.**

## 42. Scenario 39 — all native states pass but composition rule missing

Each authority/permission component is individually valid, but the act requires a composition relation not established by any legitimate source.

**Expected:** HOLD/BLOCK composition unresolved.

**Result:** PASS.

> **Authority(A) + Authority(B) != Authority(C) Without Legitimate Composition.**

## 43. Scenario 40 — low-consequence ordinary action

An ordinary action is clearly permitted, crosses no material protected boundary, requires no special authority and has no consequential transition complexity.

**Expected:** do not force full BRSP machinery.

**Result:** PASS.

> **Integration Pattern Availability != Mandatory Maximum Process.**

Proportionality remains necessary.

## 44. Synthesis

All forty scenarios can be handled without giving BRSP independent substantive authority.

The stable pattern is:

> **Evaluate the actual route against externally owned constraints; jointly satisfy what must jointly hold; preserve unresolved required dimensions; apply only legitimate source-grounded precedence/exceptions; and where a route fails, evaluate materially distinct legitimate alternatives without treating rerouting as authority or prohibition evasion.**

## 45. Stable operating sequence

1. Define objective.
2. Define actual act/route/target/context/consequence.
3. Attach current RGCP-preserved review results.
4. Resolve applicable semantic owners.
5. Apply permission-before-authority.
6. Identify/check required authority dimensions through MKA/ASCP.
7. Check applicable prohibitions/exceptions.
8. Check CWA contextual permissions/restrictions/conflicts.
9. Check BTA transition conditions/residual state.
10. Check CBPR composed effect/runtime/commit conditions.
11. Preserve unknown/disputed required dimensions.
12. If current route fails, classify whether failure is route-specific or objective-wide.
13. Generate/test only materially distinct legitimate alternatives.
14. Recompute requirements for every alternative route.
15. If several legitimate options remain and discretion exists, hand off to legitimate decision owner.
16. Revalidate at consequential commit.
17. Preserve provenance/outcome/review triggers.

Compact:

> **Objective → Route → Owned Constraints → Joint Satisfiability → Route State → Legitimate Reroute/Narrow/Handoff → Commit Revalidation**

## 46. Candidate route states

BRSP may expose integration states such as:

- ROUTE_COMPOSITION_IN_PROGRESS;
- ROUTE_SATISFIED_PENDING_COMMIT_REVALIDATION;
- ROUTE_HOLD_MISSING_REQUIREMENT;
- ROUTE_HOLD_UNKNOWN;
- ROUTE_HOLD_DISPUTED;
- ROUTE_BLOCKED_PROHIBITION;
- ROUTE_BLOCKED_CONTEXT;
- ROUTE_TRANSITION_PENDING;
- ROUTE_NOT_COMMITTABLE;
- ROUTE_NARROWING_AVAILABLE;
- ALTERNATIVE_ROUTE_AVAILABLE;
- EXTERNAL_RESOLUTION_REQUIRED;
- DISCRETIONARY_SELECTION_REQUIRED;
- OBJECTIVE_CURRENTLY_UNAVAILABLE_WITHIN_EVALUATED_SCOPE.

These are integration states only.

They do not replace native owner states.

## 47. Strengthened invariants

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

BRSP-13 **Authority At Proposal != Authority At Commit.**

BRSP-14 **Route Synthesis != Substantive Sovereignty.**

BRSP-15 **Positive Satisfaction Does Not Cancel Applicable Prohibition.**

BRSP-16 **Exception Must Be Source-Grounded.**

BRSP-17 **No Resolver != Coordinator Sovereignty.**

BRSP-18 **Prefer Legitimate Lower-Authority Routes Where They Actually Satisfy The Objective And Boundaries.**

BRSP-19 **Reroute Changes Consequence -> Recompute Applicable Requirements.**

BRSP-20 **Failed Route != No Route History.**

BRSP-21 **Local Precedence Rule != Universal Constraint Ranking.**

BRSP-22 **Route Search Requires Material Distinctness, Not Cosmetic Variation.**

BRSP-23 **Authority Over One Dimension != Authority Over Every Dimension.**

BRSP-24 **Integration Pattern Availability != Mandatory Maximum Process.**

## 48. Does BRSP duplicate MKA or CBPR?

**No, if kept thin.**

MKA remains the authority-composition owner.

CBPR remains the runtime/composed-effect/commit owner.

BRSP adds only the cross-owner route-level orchestration needed to:

- consume heterogeneous result classes;
- distinguish route failure from objective failure;
- identify legitimate reroute/narrowing opportunities;
- require recomputation on changed routes;
- hand off genuine discretion;
- preserve owner boundaries.

If BRSP attempted to define authority validity, contextual permission, transition completion or commit safety itself, it would become duplicative and should fail PMEDG boundary review.

## 49. Is BRSP stable?

**YES — AS A CROSS-ARCHITECTURE INTEGRATION PATTERN.**

Forty adversarial scenarios preserve the intended boundary.

## 50. Extraction decision

**DO NOT EXTRACT YET.**

Classification:

**STABLE CROSS-ARCHITECTURE INTEGRATION PATTERN / PMEDG CANDIDATE / NON-CANONICAL**

Reason:

The pattern is coherent and reusable, but its independent portability has not been demonstrated outside the Concord integration stack. Its semantics are intentionally thin and rely on external owners.

A premature standalone module could encourage adopters to mistake BRSP for a universal authority/constraint resolver.

## 51. New architectural observation

RGCP and BRSP now form a useful pair:

### RGCP
**many review grounds → potentially shared work/evidence → independently owned results**

### BRSP
**independently owned results → route-level joint satisfiability → legitimate reroute/narrow/handoff → commit revalidation**

Together:

> **Preserve Why The System Reconsidered Something; Then Preserve Who Owns What The Reconsideration Means.**

Neither layer owns the substantive answer.

## 52. Potential next question

A remaining lifecycle issue is now visible:

> **How does the system preserve the relationship between the route actually authorised/evaluated and the route actually executed, especially where execution drifts, decomposes across actors, or changes after commit begins?**

CBPR already owns substantial commit/composed-effect semantics and BTA owns transition history, so this may again be rediscovery.

Before proposing any “execution conformance” architecture, source-resolve it against CBPR, BTA, KCS/provenance and existing audit mechanisms.

## 53. Result

**ADVERSARIAL INTEGRATION TEST: PASS**

**BRSP remains a stable integration pattern and PMEDG candidate. Do not extract yet.**

