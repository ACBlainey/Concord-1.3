# KCS Companion Upgrade 002 — KCS Change-Propagation Back-Propagation 001

**Author:** Alexander C. Blainey — Independent Researcher
**Project:** The Concord Framework
**Status:** CANONICAL COMPANION UPGRADE — INTEGRATED / ARCHITECTURAL INTERFACE RETEST PASSED
**Parent architecture:** KCS Companion Upgrade 001 — Operational Dependency and Change-Propagation Architecture
**Evidence source:** KCS Change Propagation — Portable Module v1.0
**Back-propagation source:** KCS Change Propagation — Back-Propagation Audit 001
**Date:** 24 September 2026

## Purpose

This is a deliberately bounded companion upgrade.

KCS Companion Upgrade 001 already contains the substantive dependency and change-propagation architecture. PMEDG development of the portable KCS Change Propagation module did not expose a need to replace that kernel.

Instead, this companion returns twelve source-relevant refinements concerned primarily with scope, provenance, cascade control, representation and epistemic boundaries.

> **Change(x) → CandidateReview(y)**

remains the governing propagation rule.

> **Dependency State ≠ System Authority**

remains the governing authority boundary.

## 1. REFERENCES relation

Add **REFERENCES** to the shared relation vocabulary.

**EVIDENCES** and **REFERENCES** are not interchangeable.

- **EVIDENCES** means the object materially supports a claim, state or dependency.
- **REFERENCES** means the object points to another object without necessarily carrying substantive evidential dependence upon its current contents.

This distinction helps prevent unnecessary propagation through reference-only links.

## 2. Document-role distinction

Where consequential, distinguish whether a document:

1. **contains** changed content and may itself require revision;
2. **evidences** a dependency or state;
3. merely **references** another current object.

A document that merely references an object does not automatically inherit every substantive change to that object if the reference remains valid.

> **Reference ≠ Substantive Dependency**

## 3. Purpose-bounded visibility in the dependency record

KCS Companion Upgrade 001 already requires purpose-bounded access.

Dependency records should therefore be capable of carrying a visibility/access-handling attribute where needed.

A practical dependency record may be extended to include:

**Visibility**

This does not make KCS the access-control authority. It allows the dependency layer to preserve that a relation has bounded exposure requirements.

> **Dependency Legibility ≠ Universal Visibility**

## 4. Change type, confidence and bounded scope

A consequential change event should preserve, where available:

**ChangeEvent = <Object, OldState, NewState, ChangeType, Reason, Evidence, Time, ActorOrSource, Confidence, Scope>**

Scope may identify an entire object or a bounded:

- instance;
- version;
- configuration;
- batch;
- deployment;
- time interval;
- jurisdiction/context;
- other identifiable subset.

> **Object Change ≠ Necessarily Every Instance or Every Time Period**

Propagation must not silently universalise a localised change.

## 5. Changed-property filtering

When evaluating a candidate dependent, KCS should ask whether the changed property actually supplies or affects the capability required by that dependent.

A relation can be genuine while the particular change remains immaterial to the dependent.

This is an explicit refinement of selective propagation.

> **Dependency Exists ≠ This Change Affects the Dependency**

## 6. No-transformation safeguard

A downstream object may be materially implicated even if it does not transform the affected payload.

Storage, transmission, publication, display, caching or preservation of materially affected output can justify review where the changed content passes through that object.

> **No Transformation ≠ No Material Effect**

This prevents selective-propagation stopping rules from being interpreted too narrowly.

## 7. Alternative-verification boundary

KCS may represent alternatives and consume their verification state.

It does not automatically determine domain equivalence.

Where equivalence matters, the legitimate host/domain process supplies the verification result.

KCS may then preserve states such as:

- FULL;
- PARTIAL;
- EMERGENCY_ONLY;
- DEGRADED;
- UNVERIFIED.

> **Alternative Label ≠ Proven Equivalence**

## 8. Evaluation-space completeness escalation boundary

Retain the existing rule:

> **No Recorded Dependency ≠ No Dependency**

Add the following operational boundary:

UNKNOWN does not automatically mean REVIEW_REQUIRED.

Where a consequential decision depends upon assumed dependency completeness, high-consequence uncertainty may justify source-grounded dependency discovery or external escalation before that decision proceeds.

The consequence/escalation threshold is supplied by the legitimate host/domain architecture.

Where no justified threshold exists, preserve UNKNOWN and surface the unresolved uncertainty rather than inventing a universal threshold.

## 9. Freshness boundary

Retain REVIEW_OVERDUE and existing freshness fields.

Add:

> **Age Alone ≠ Universal Staleness Threshold**

Review intervals and freshness thresholds remain host/domain inputs unless explicitly represented.

A stale relation is not automatically false and must not be silently deleted.

## 10. Coexistent output semantics

KCS change-propagation outcomes may be multidimensional and coexist.

For example, one bounded object state may legitimately be both:

- REVIEW_REQUIRED;
- ALTERNATIVE_AVAILABLE;
- UNKNOWN_EFFECT.

Do not force such dimensions into a universal precedence ladder.

The portable KCP-C1 through KCP-C16 identifiers remain an optional implementation vocabulary rather than mandatory Concord serialization.

The required source semantic is:

> **Multiple Scoped Classifications May Coexist**

## 11. Scope-bound classifications

Where scope matters, each material classification should bind to the relevant:

- instance;
- version;
- configuration;
- batch;
- deployment;
- time interval;
- context;
- or other bounded subset.

Different scoped states must not be collapsed into one undifferentiated object status.

This is the downstream counterpart to bounded ChangeEvent scope.

## 12. Consequential review record

A consequential downstream review should preserve enough information to explain why propagation stopped or continued.

A practical semantic record is:

**ReviewRecord = <ChangedObject, DependentObject, Relation, ChangedProperty, Materiality, ApplicableContext, Alternatives, Evidence, Confidence, ReviewOutcome, ResultingState, FurtherPropagation, ReviewerOrSource, Time, Scope>**

Exact implementation schema remains flexible.

The record should make it possible to determine:

- why review was triggered;
- what property/change was evaluated;
- what dependency/context applied;
- what evidence supported the result;
- what state resulted;
- why propagation stopped or continued;
- what bounded scope the result applies to.

## 13. Updated selective-propagation cycle

The existing propagation architecture may now be expressed:

1. **RECORD** — preserve prior state and bounded change event.
2. **TRAVERSE** — identify materially relevant downstream relations.
3. **FILTER** — test relation applicability, changed property, context, scope, alternatives and current state.
4. **CLASSIFY** — preserve coexistent scoped candidate states.
5. **REVIEW** — route substantive effect evaluation to the legitimate host process.
6. **RECORD OUTCOME** — preserve evidence, result, scope and provenance.
7. **PROPAGATE IF MATERIAL** — continue only where downstream material state or consequential uncertainty changes.
8. **STOP** — terminate where no further material effect remains.

## 14. Authority boundary

Nothing in this companion authorises KCS to:

- decide substantive domain equivalence;
- invent consequence/materiality thresholds;
- treat graph completeness as reality completeness;
- convert dependency into governance authority;
- expose protected dependency details universally;
- impose a single object status across materially different scopes;
- automatically invalidate downstream objects.

KCS remains civilisational memory and dependency-state infrastructure.

## 15. Relationship to Companion Upgrade 001

This companion does not supersede Companion Upgrade 001.

Current KCS dependency/change-propagation architecture is:

**KCS foundation + Companion Upgrade 001 + applicable Companion Upgrade 002 refinements**

Companion Upgrade 001 remains the substantive source architecture.

This document closes bounded operational gaps exposed during portable-module testing.

## 16. Required interface regression

Before this companion is treated as integrated canonical capability, check:

### Civil State Map / SMM

Confirm that scoped dependency states, UNKNOWN completeness and coexistent classifications can be consumed without the State Map collapsing them into one universal state.

### Civilisation Clock / STRA

Confirm that KCS review requirements and dependency changes can trigger bounded review without KCS becoming scheduler or Clock becoming dependency adjudicator.

### Continuity

Confirm that reconstruction/recovery chains can use bounded dependency scope and alternatives without KCS deciding identity/continuity legitimacy.

### Privacy / protected context

Confirm that Visibility semantics preserve minimum necessary access and do not imply that the dependency graph owns access-control decisions.

### Active Development

Confirm that candidate changes, corrections and supersession can produce review records and bounded downstream propagation without automatically rewriting canonical dependents.

## 17. Evidence boundary

These refinements derive from graduated KCS Change Propagation v1.0 after PMEDG development.

The back-propagation audit found:

- 12 material source/portable deltas;
- 8 operational/failure-mode improvements;
- 3 clarifications/formalisations;
- 1 partial semantic incorporation;
- 0 kernel replacements;
- 0 authority expansions.

The result is therefore intentionally smaller than the SMM and STRA back-propagation upgrades.

## 18. Current status

> **CANONICAL COMPANION UPGRADE — INTEGRATED / ARCHITECTURAL INTERFACE RETEST PASSED**

The required regression has been completed in **KCS Companion Upgrade 002 — KCS Change-Propagation Back-Propagation 001 — Interface Regression Review**.

Results: Civil State Map/SMM PASS; Civilisation Clock/STRA PASS; Continuity/recovery PASS; privacy/protected-context PASS with bounded vocabulary follow-up; Active Development PASS with proportional-record follow-up; no epistemic, authority or cascade/propagation regression observed.

The bounded follow-ups do not block architectural integration.

## Conclusion

Portable-module development did not reveal a missing KCS dependency architecture.

It refined an already mature source.

The returned improvements sharpen the distinction between references and evidence, preserve bounded change scope, improve selective propagation, prevent false stopping conditions, clarify alternative verification, strengthen ESCP handling, preserve scoped/coexistent outputs and improve review provenance.

The result is a small source upgrade rather than a redesign.
