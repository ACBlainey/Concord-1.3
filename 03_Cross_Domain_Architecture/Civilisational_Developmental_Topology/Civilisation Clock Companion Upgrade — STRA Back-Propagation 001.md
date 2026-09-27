# Civilisation Clock Companion Upgrade — STRA Back-Propagation 001

**Author:** Alexander C. Blainey — Independent Researcher
**Project:** The Concord Framework
**Status:** CANONICAL COMPANION UPGRADE — INTEGRATED / ARCHITECTURAL INTERFACE RETEST PASSED
**Parent architecture:** Civilisation Clock Companion Extension 001 — State, Functional and Compound Trigger Architecture
**Evidence source:** State Triggered Review Architecture — Portable Module v1.0; PMEDG STRA development record
**Back-propagation source:** State Triggered Review Architecture — Back-Propagation Audit 001
**Date:** 24 September 2026

## Purpose

This companion returns source-relevant refinements developed during PMEDG testing of State Triggered Review Architecture (STRA) to the Concord Civilisation Clock source family.

It is additive. It does not replace the existing Clock companion or alter the core rule:

> **Triggering Review ≠ Authority Over Outcome**

The Clock remains a scheduler/review-trigger architecture. Legitimate domain owners retain substantive authority.

## 1. Expanded trigger lifecycle

Add the following states to the Clock trigger vocabulary where applicable:

- **IMPOSSIBLE** — the declared condition can no longer be reached under represented assumptions;
- **RETIRED** — deliberately closed and no longer watched;
- **ROUTING-UNRESOLVED** — condition/review state is known but no legitimate destination or owner has yet been resolved.

These supplement rather than replace DORMANT, WATCHING, CONDITION-PARTIAL, CONDITION-SATISFIED, REVIEW-DUE, ACTION-PENDING, COMPLETED, SUPERSEDED, UNKNOWN and DISPUTED.

## 2. Evidence invariant

Add:

> **Missing Evidence ≠ Condition False**

Trigger evaluation must preserve UNKNOWN or DISPUTED where the evidence does not justify binary resolution.

Absent, inaccessible, stale or unobserved evidence must not silently become a negative condition result.

## 3. Minimum compound uncertainty semantics

Compound triggers must preserve uncertainty rather than force binary truth.

Unless a legitimate host/domain process defines stricter semantics:

- TRUE AND UNKNOWN → UNKNOWN;
- FALSE AND UNKNOWN → FALSE for satisfaction of that conjunction only, without asserting the unknown input false;
- TRUE OR UNKNOWN → TRUE;
- FALSE OR UNKNOWN → UNKNOWN;
- NOT UNKNOWN → UNKNOWN;
- materially relevant DISPUTED subconditions remain DISPUTED unless the compound result is independently determined.

Natural-language forms such as **unless**, **except when** and **until** must be normalised into explicit conditional structure before consequential evaluation.

> **Compound Result ≠ Erasure of Subcondition Uncertainty**

## 4. Materiality interface

Where a trigger depends on material change, the Clock/STRA mechanism consumes rather than invents the domain criterion.

A bounded determination may contain:

**M_t = <subject, change/evidence, criterion, result, evaluator/authority, provenance, time, scope, uncertainty>**

The legitimate domain or host process owns the materiality criterion.

The Clock owns evaluation of the declared trigger against the supplied determination.

## 5. Validation and authority provenance

For capability and similar triggers, distinguish where material:

- claimed;
- available;
- validated;
- authorised for the relevant use.

A consequential validation state should identify the evidence/process and legitimate source supporting it.

Validation in one scope must not silently become validation in another.

> **State Label Without Provenance ≠ Validation**

## 6. Trigger-role separation

Where material, distinguish:

- **trigger-definition owner**;
- **trigger evaluator**;
- **substantive review/action owner**;
- **ownership-resolution route**.

One actor may legitimately occupy several roles, but the Clock must not assume this.

If a condition becomes satisfied while substantive ownership/routing remains unresolved:

**CONDITION-SATISFIED / ROUTING-UNRESOLVED**

is valid.

Repeated evaluation must not manufacture legitimate ownership.

A ROUTING-UNRESOLVED state must itself have an appropriate bounded review, escalation or temporal backstop.

> **Need for Action ≠ Authority to Invent an Actor**

## 7. Reconciliation handoff

Where trigger-relevant state/dependency sources materially conflict, the Clock need not decide the domain truth.

It may emit or consume:

**R_h = <subject, conflicting claims, sources, requested question, legitimate resolver, result/status, provenance, time, scope>**

If reconciliation remains DISPUTED, preserve that state and route it through the legitimate resolution path.

This mechanism may also carry domain-owned recurrence/event equivalence decisions.

## 8. Privacy-preserving trigger result

Where the Clock/trigger evaluator lacks legitimate access to protected underlying evidence, it may consume a bounded result from an authorised evaluator:

**P_r = <condition/subject, result, authorised evaluator, provenance, time, scope, uncertainty>**

The result may expose only SATISFIED, NOT-SATISFIED, UNKNOWN or another bounded state required for the declared condition.

The trigger must not become justification for broad surveillance or unnecessary retrieval.

## 9. Event-order interface

Where a trigger genuinely depends on consequence-relevant ordering, the Clock may consume an externally supplied ordering relation.

That relation should preserve:

- events/subjects ordered;
- claimed relation;
- source/process;
- provenance;
- confidence/uncertainty;
- reconciliation status;
- time/scope.

Add:

> **Timestamp(A) < Timestamp(B) ≠ A materially precedes B for every consequence**

The Clock does not require a universal total order.

## 10. Stale, impossible and long-lived trigger review

A trigger may become stale because its subject, assumptions, dependencies, owner or legitimacy changed.

Long-lived WATCHING triggers require a bounded trigger-definition review condition or backstop appropriate to their host context.

Possible outcomes include:

- continue watching;
- modify;
- reset;
- suspend;
- supersede;
- retire;
- mark impossible;
- route for ownership resolution.

The Clock must not permit indefinite WATCHING merely because the original condition has never fired.

## 11. Cascade control

A satisfied trigger may legitimately activate or create another trigger, but this must not create accidental authority chains.

Where cascades occur, preserve:

- initiating/parent trigger provenance;
- direct-cycle detection where represented;
- duplicate activation suppression where host semantics allow;
- each consequential child trigger's own condition or explicit activation rule;
- materiality gating where required;
- owner/routing validation.

A superseded or retired trigger must not become effectively live again merely because a stale replica/subscriber still exposes an older WATCHING state.

The host must provide a bounded supersession/reconciliation route before consequential duplicate activation.

Exact depth/rate limits remain host/domain-defined.

## 12. Participant-condition invariant

Make explicit the rule already substantially present in wake-candidate architecture:

> **Participant Condition Satisfied ≠ Forced Action**

A participant-declared trigger authorises only the declared bounded consequence under applicable identity, consent and continuity rules.

## 13. Reactivation/revalidation invariant

Make explicit the rule already substantially present in cold-knowledge reactivation:

> **Relevance Returned ≠ Validity Restored**

Retrieved dormant material requires revalidation before consequential current use where validity may have changed.

## 14. Dependency-completeness invariant

Add:

> **No Represented Dependency ≠ No Dependency**

The Clock consumes represented dependency state. It does not claim the dependency graph is complete merely because no additional dependency is represented.

This preserves compatibility with KCS/CDT dependency architecture and ESCP-style source-resolution discipline.

## 15. Updated trigger record

The existing Clock trigger record may be extended to support:

**T = <ID, subject, class, condition, sources, dependencies, bounds, consequence, definition-owner, evaluator, substantive-owner, resolution-route, state, provenance, history>**

This is an information model, not a mandatory database schema.

Optional associated records include materiality determinations, reconciliation handoffs and privacy-preserving bounded results.

## 16. Updated operating cycle

The source-side operating cycle is:

1. **DEFINE** — represent subject, condition, class and consequence.
2. **BIND** — identify permitted inputs, provenance, materiality ownership and legitimate routing.
3. **WATCH** — observe only permitted relevant state/evidence.
4. **EVALUATE** — preserve UNKNOWN/DISPUTED and compound uncertainty.
5. **SIGNAL** — record partial, satisfied, review-due, impossible or unresolved-routing state.
6. **ROUTE** — send candidacy to the legitimate owner or ownership-resolution route.
7. **RECORD** — preserve evaluation and provenance.
8. **UPDATE** — complete, reset, continue, correct, suspend, supersede or retire.
9. **BACKSTOP** — re-evaluate trigger assumptions and ownership at bounded fallback where defined.

## 17. Updated failure-mode safeguards

This companion operationalises several failure modes already named in the source:

- **false non-satisfaction** → missing evidence remains UNKNOWN rather than false;
- **stale trigger** → bounded definition review/backstop;
- **impossible trigger persistence** → IMPOSSIBLE state plus review/retirement route;
- **cascade amplification** → provenance, duplicate/cycle/materiality/routing controls;
- **ownership vacuum** → ROUTING-UNRESOLVED plus legitimate resolution route;
- **privacy leakage** → privacy-preserving bounded evaluation;
- **stale reactivation** → explicit revalidation invariant;
- **dependency completeness illusion** → no represented dependency is not proof of no dependency;
- **timestamp precedence error** → external bounded ordering relation;
- **compound certainty collapse** → explicit uncertainty semantics.

## 18. Authority boundary

Nothing in this companion authorises the Clock to:

- define substantive domain outcomes;
- invent a materiality criterion;
- validate capabilities without legitimate evidence;
- appoint unresolved owners;
- own the complete dependency graph;
- override participant consent/continuity;
- retrieve protected evidence without legitimate access;
- convert trigger satisfaction directly into general substantive action.

Automatic execution remains possible only where a separate legitimate process has already authorised that bounded automation.

## 19. Interface regression required

Before this companion is treated as integrated canonical capability, perform bounded regression against:

### Civil State Map / SMM Back-Propagation 001

Check that UNKNOWN (REVIEW DUE), ownership gaps, consequence carriage, active-work state and context-sensitive sufficiency remain distinct from Clock trigger lifecycle state.

### KCS

Check that dependency/evidence updates, correction/supersession, stale-state propagation and distributed source state can feed triggers without the Clock absorbing KCS ownership.

### Continuity / participant architecture

Check that participant triggers remain bounded by identity, consent, continuity and reactivation rules and cannot create forced wake/action.

### Protected-context/privacy architecture

Check that bounded evaluator results do not become a route for unnecessary protected-data access and that the Clock can operate on minimum necessary information.

## 20. Evidence boundary

The refinements returned here originate in graduated STRA v1.0 after two materially different blind transfer tests.

STRA records:

- BTT-001: 50 / 50 frozen predictions materially confirmed; 0 / 12 fundamental failures;
- BTT-002: 52 / 52 frozen predictions materially confirmed; 0 / 14 fundamental failures;
- combined: 102 / 102 frozen predictions; 0 / 26 fundamental failures;
- cross-test convergence: yes;
- third blind test not currently justified under PMEDG.

These counts are evidence summaries, not universal statistical proof.

Their relevance here is that the returned refinements were retained through independent transfer pressure and graduation rather than being invented solely during source reintegration.

## 21. Current status

> **CANONICAL COMPANION UPGRADE — INTEGRATED / ARCHITECTURAL INTERFACE RETEST PASSED**

The required regression has been completed in **Civilisation Clock — STRA Back-Propagation 001 — Interface Regression Review**.

Results: Civil State Map/SMM PASS; KCS PASS; Continuity/participant architecture PASS with bounded implementation follow-up; protected-context/privacy boundary PASS with bounded schema follow-up; no authority, epistemic or privacy/autonomy regression observed.

The bounded follow-ups do not block architectural integration.

## Conclusion

The original Civilisation Clock companion supplied the STRA kernel.

Portable-module development subsequently operationalised trigger lifecycle, uncertainty, materiality, routing, reconciliation, privacy, stale-state and cascade edge conditions that were absent or only provisional in the source.

This companion returns those refinements without replacing the Clock or expanding its substantive authority.

The next step is the bounded cross-interface regression defined above.
