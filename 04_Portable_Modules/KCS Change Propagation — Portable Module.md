# KCS Change Propagation — Portable Module

**Version:** 1.0  
**Status:** GRADUATED PORTABLE MODULE / SPECIFICATION-LEVEL TRANSFER VALIDATED  
**Development level:** Level B — Extractable Architecture  
**Source basis:** *KCS Companion Upgrade 001 — Operational Dependency and Change-Propagation Architecture*  
**Date:** 23 September 2026

## 1. Purpose

KCS Change Propagation is a portable dependency-aware review mechanism for complex evolving systems.

It addresses a recurring problem:

> **When an upstream object changes, what downstream objects should be reconsidered—and how can that review propagate without automatically invalidating everything connected to the change?**

The module records material dependency relationships, preserves their provenance and state, generates bounded review sets after consequential changes, and propagates further only where downstream material state actually changes.

## 2. Portable problem

Complex systems contain dependencies among software, data, models, standards, interfaces, evidence, procedures, physical infrastructure, recovery capabilities and other objects.

A change to one object can matter elsewhere. But two opposite errors are common:

1. **silent dependency failure** — downstream objects remain trusted even though a prerequisite materially changed;
2. **cascade overreaction** — every downstream object is automatically rejected merely because an upstream object changed.

KCS Change Propagation provides a middle architecture:

> **Change upstream → identify materially affected dependents → review selectively → propagate further only when downstream state materially changes.**

## 3. Core invariant

For changed object x and dependent object y:

> **Change(x) → CandidateReview(y)**

not:

> **Change(x) → AutomaticRejection(y)**

A dependency creates a reason to examine possible effect. It does not prove that the dependent object has failed.

## 4. Scope

This module can:
- represent typed material dependencies;
- preserve dependency provenance, confidence, context and freshness;
- distinguish active, degraded, blocking, failed, unknown and disputed relations;
- traverse upstream and downstream relationships;
- record consequential change events;
- generate bounded downstream review sets;
- stop irrelevant propagation;
- continue propagation when downstream material state changes;
- represent correction, supersession, failure and alternatives;
- expose recovery/dependency chains;
- preserve uncertainty;
- support distributed suppliers/responsibilities;
- flag review requirements.

## 5. Non-functions

This module does **not** automatically:
- decide whether a change is ethically or legally legitimate;
- command dependent systems;
- allocate resources;
- schedule work;
- determine organisational priority;
- adjudicate disputes;
- assign authority merely from dependency;
- guarantee graph completeness;
- expose all dependency details to all participants;
- invalidate every dependent object after an upstream change.

> **Dependency State ≠ System Authority**

## 6. Object model

Let the represented dependency graph at time t be:

**G(t) = <V, R, P, S, H>**

where:
- **V** = represented objects;
- **R** = typed material relations;
- **P** = provenance/evidence;
- **S** = current represented state;
- **H** = historical state and change record.

Objects may include:
- functions;
- systems;
- architectures;
- interfaces;
- protocols;
- datasets;
- models;
- software;
- standards;
- rules;
- evidence bases;
- recovery capabilities;
- external services;
- physical infrastructure;
- represented participant capabilities;
- documents where the document itself is the relevant object.

A document may evidence a dependency without being the dependency itself.

Document relations should distinguish, where consequential:
- a document that **contains** changed content and may itself require revision;
- a document that **evidences** a dependency or state;
- a document that merely **references** another current object.

A reference to an object does not automatically inherit every substantive change to that object if the reference remains valid.

## 7. Dependency record

A portable dependency record may be represented as:

**Dependency = <ID, Source, Target, Capability, RelationType, Context, Materiality, Criticality, State, Alternatives, FailureEffect, Evidence, Confidence, FirstRecorded, LastConfirmed, LastChanged, NextReview, SupplierRole, Visibility>**

Not every implementation must materialise every field when consequence is low, but consequential propagation requires enough information to distinguish material effect from mere connection.

## 8. Relation types

Initial shared relation types:

- DEPENDS_ON
- REQUIRES
- SUPPLIES
- INTERFACES_WITH
- ENABLES
- BLOCKS
- PROPAGATES_TO
- CORRECTS
- REVIEWS
- SUPERSEDES
- ALTERNATIVE_TO
- RECOVERS
- PRESERVES
- EVIDENCES
- REFERENCES

Domains may add relations, but shared relation names should retain stable semantics.

## 9. Dependency state

Minimum states:

- ACTIVE
- SATISFIED
- DEGRADED
- BLOCKING
- FAILED
- ALTERNATIVE_AVAILABLE
- SUPERSEDED
- UNKNOWN
- DISPUTED

Important:

> **Dependency Exists ≠ Dependency Is Blocking**

BLOCKING means the current prerequisite state materially prevents or constrains the dependent function.

## 10. Materiality and criticality

Materiality may be:
- CRITICAL
- HIGH
- MODERATE
- LOW
- IMMATERIAL
- UNKNOWN
- DISPUTED

Criticality is contextual. Relevant factors may include:
- consequence of failure;
- number and importance of dependents;
- alternatives;
- recovery difficulty;
- time sensitivity;
- reversibility;
- correlated exposure.

Do not compress these factors into a single universal score unless the host domain has a justified reason to do so.

Materiality thresholds are host/domain inputs unless explicitly represented. This module must not invent a threshold merely to decide whether propagation should continue.

## 11. Upstream and downstream traversal

For object x:

**Up(x) = materially relevant objects on which x depends**

**Down(x) = materially relevant objects dependent upon x**

Traversal can support:
- prerequisite discovery;
- affected-object discovery;
- shared bottleneck discovery;
- supplier/responsibility tracing;
- alternative/recovery-path discovery.

But:

> **Traversal ≠ Priority Decision**

The fact that an object is highly connected does not itself determine what should be developed, funded or governed first.

## 12. Change event

A consequential change event should preserve, where available:

**ChangeEvent = <Object, OldState, NewState, ChangeType, Reason, Evidence, Time, ActorOrSource, Confidence>**

Change types may include:
- validation;
- correction;
- supersession;
- deprecation;
- interface change;
- supplier/responsibility change;
- dependency discovery;
- dependency removal;
- failure;
- recovery;
- contested status;
- version change.

The event becomes part of history rather than overwriting the prior state.

### 12.1 Change scope

A consequential change may apply to an entire represented object or only to a bounded instance, batch, deployment, version, time interval, configuration or other identifiable subset.

Where the distinction matters, the change record should preserve the affected scope rather than silently treating a localised change as universal.

> **Object Change ≠ Necessarily Every Instance or Every Time Period**

## 13. Core propagation workflow

### Step 1 — Represent

Record objects and material dependency relations with appropriate provenance, state and uncertainty.

### Step 2 — Record change

Preserve the prior state and record the consequential upstream change.

### Step 3 — Traverse

Identify materially relevant downstream relations.

### Step 4 — Filter

For each candidate dependent, test:
- relation applicability;
- context;
- materiality;
- current state;
- available alternatives;
- whether the changed property actually supplies a required capability;
- whether the dependent is already superseded;
- whether evidence already establishes no material effect.

### Step 5 — Generate review set

Mark a dependent REVIEW_REQUIRED only where the change may materially affect it.

### Step 6 — Review externally

The appropriate host process evaluates the actual downstream effect.

### Step 7 — Record outcome

Preserve evidence, reviewer/source, conclusion and resulting state.

### Step 8 — Continue only if material

Propagate further only if the reviewed downstream object's material state changes or uncertainty itself creates a consequential review requirement.

### Step 9 — Stop

Stop when no further material downstream effect remains.

Compact form:

> **Represent → Change → Traverse → Filter → Review → Update → Propagate-if-material**

## 14. Selective propagation stopping rules

Propagation should normally stop at a relation where:
- dependency is immaterial to the changed property;
- an unaffected alternative fully satisfies the requirement;
- the dependent object is superseded and no active object relies on it;
- context makes the relation non-applicable;
- evidence establishes that the dependent function remains satisfied;
- the candidate relation was erroneous and is corrected.

> **Connected ≠ Affected**

A downstream object may nevertheless be materially implicated even when it does not transform the affected payload. Storage, transmission, display, publication, caching or other preservation of materially affected output can justify review where the changed content passes through that object.

> **No Transformation ≠ No Material Effect**

## 15. Propagation escalation conditions

Review urgency or breadth may increase where:
- high-consequence functionality depends on the changed object;
- no viable alternative exists;
- failure may be silent;
- multiple important dependents share the same prerequisite;
- effects may be irreversible;
- recovery is difficult or time-sensitive;
- protected constraints may be affected;
- uncertainty is itself consequential.

Escalation changes review handling, not automatic authority.

## 16. Correction propagation

When object x is corrected:

1. preserve the previous state;
2. record the correction and evidence;
3. identify materially dependent objects;
4. mark REVIEW_REQUIRED where justified;
5. surface review through an appropriate host interface;
6. preserve review outcomes;
7. clear the flag where the dependency remains satisfied;
8. propagate further only where downstream material state changes.

This creates bounded recursive correction.

## 17. Supersession

Supersession should preserve the old object.

Represent:

**OldObject — SUPERSEDED_BY → NewObject**

Dependents may then be classified:
- COMPATIBLE_WITH_NEW
- MIGRATION_REQUIRED
- REVIEW_REQUIRED
- LEGACY_DEPENDENCY
- UNKNOWN

> **Superseded ≠ Erased**

A new version does not automatically prove compatibility.

## 18. Failure and alternatives

When an object fails, the module should expose where relevant:
- direct dependents;
- critical indirect dependents;
- available alternatives;
- recovery suppliers/responsibilities;
- degraded modes;
- unresolved unknowns.

Alternative states may include:
- FULL
- PARTIAL
- EMERGENCY_ONLY
- DEGRADED
- UNVERIFIED

> **Alternative Label ≠ Proven Equivalence**

An alternative should be evaluated against the required capability and context.

Equivalence testing is external to this module unless the host explicitly supplies that capability. KCS Change Propagation records the alternative state and consumes the verification result; it does not manufacture domain equivalence.

## 19. Distributed suppliers and responsibilities

Dependency representation must not force a false single-owner model.

Possible supplier/responsibility roles:
- PRIMARY
- CO-OWNER
- DISTRIBUTED_SUPPLIER
- DELEGATED
- INTERFACE_SUPPLIER
- FALLBACK

These labels describe represented supply/responsibility relationships. They do not themselves establish legal ownership or governance authority.

## 20. Dependency and authority

If A depends on B, B does not thereby govern A.

> **Dependency ≠ Subordination**

Likewise, knowing that B is a bottleneck does not itself authorise the dependency system or B's supplier to command downstream systems.

Authority must come from an external legitimate basis.

## 21. Unknown and disputed dependencies

First-class uncertainty states should include where relevant:
- UNKNOWN_DEPENDENCY
- UNKNOWN_SUPPLIER
- UNKNOWN_MATERIALITY
- UNKNOWN_EFFECT
- DISPUTED_DEPENDENCY
- DISPUTED_SUPPLIER
- DISPUTED_EFFECT

> **Unknown ≠ Absent**

> **Disputed ≠ False**

A missing graph edge is not proof that no real dependency exists.

## 22. Evaluation-space completeness

Dependency maps are representations, not reality itself.

Therefore:

> **No Recorded Dependency ≠ No Dependency**

A review should not infer that an object is independent merely because the current graph contains no edge.

Where consequence is high, source-grounded dependency discovery may be required before making a completeness claim.

UNKNOWN does not automatically mean REVIEW_REQUIRED. However, where a consequential decision depends on assumed completeness, high-consequence uncertainty may justify source-grounded dependency discovery or external escalation before that decision proceeds.

The host supplies any consequence/escalation threshold. Where no such threshold is available, preserve the UNKNOWN state and surface the unresolved consequential uncertainty rather than inventing a universal threshold.

## 23. Freshness

Material dependency records should support:
- first recorded;
- last confirmed;
- last changed;
- next review;
- evidence freshness;
- source/reviewer;
- confidence.

A stale relation may become REVIEW_OVERDUE.

Freshness and review intervals are host/domain inputs unless explicitly represented. Age alone does not establish a universal stale threshold.

> **Stale ≠ Automatically False**

Do not silently delete a relation merely because its evidence is old.

## 24. Purpose-bounded visibility

Dependency graphs can expose:
- vulnerabilities;
- privileged interfaces;
- recovery paths;
- single points of failure;
- sensitive participant/system relationships.

Therefore:

> **Dependency Legibility ≠ Universal Visibility**

An implementation may represent that a consequential dependency exists without exposing every operational detail to every viewer.

Access control should be external to this module but the module must preserve the need for purpose-bounded visibility.

## 25. Anti-centralisation boundary

A live dependency graph may appear to offer a commanding view of a system.

That view must not become sovereign merely because it is comprehensive.

KCS Change Propagation may:
- record;
- preserve;
- retrieve;
- link;
- traverse;
- flag;
- generate review requirements.

It does not automatically:
- command systems;
- allocate resources;
- approve changes;
- adjudicate disputes;
- define ethical/legal legitimacy;
- rank participants;
- impose development priorities.

> **Knowledge State ≠ Authority**

## 26. Output classifications

A host implementation may emit:

- KCP-C1 — NO_MATERIAL_DOWNSTREAM_EFFECT
- KCP-C2 — REVIEW_REQUIRED
- KCP-C3 — REVIEW_OVERDUE
- KCP-C4 — DEPENDENCY_DEGRADED
- KCP-C5 — DEPENDENCY_BLOCKING
- KCP-C6 — DEPENDENCY_FAILED
- KCP-C7 — MIGRATION_REQUIRED
- KCP-C8 — LEGACY_DEPENDENCY
- KCP-C9 — ALTERNATIVE_AVAILABLE
- KCP-C10 — ALTERNATIVE_UNVERIFIED
- KCP-C11 — UNKNOWN_DEPENDENCY
- KCP-C12 — DISPUTED_DEPENDENCY
- KCP-C13 — UNKNOWN_EFFECT
- KCP-C14 — PROPAGATION_STOPPED
- KCP-C15 — PROPAGATION_CONTINUES
- KCP-C16 — EXTERNAL_ESCALATION_REQUIRED

These classifications are dimensional/coexistent outputs, not a universal precedence ladder. Several may legitimately apply to the same object at once.

Where scope matters, each classification should bind explicitly to the relevant instance, version, configuration, batch, deployment, time interval or other bounded subset. Do not collapse different scoped states into one undifferentiated object status.

## 27. Review record

A consequential downstream review should preserve where appropriate:

**ReviewRecord = <ChangedObject, DependentObject, Relation, ChangedProperty, Materiality, ApplicableContext, Alternatives, Evidence, Confidence, ReviewOutcome, ResultingState, FurtherPropagation, ReviewerOrSource, Time>**

Where several classifications coexist, the record should preserve the scope and dimension of each classification rather than forcing them into a single status. Presentation/display policy remains an implementation concern.

The record should make it possible to distinguish:
- why review was triggered;
- what was actually evaluated;
- whether the dependency remained satisfied;
- why propagation stopped or continued.

## 28. Failure modes and safeguards

### 28.1 Dependency hallucination
A relation is invented because it seems plausible.

**Safeguard:** provenance, evidence, confidence, UNKNOWN.

### 28.2 Missing dependency
The graph lacks a real relation.

**Safeguard:** no-recorded-dependency discipline and source-grounded audits for consequential completeness claims.

### 28.3 Stale dependency
An old relation is treated as current without review.

**Safeguard:** freshness and REVIEW_OVERDUE.

### 28.4 Cascade overload
Every connected object is reviewed after every change.

**Safeguard:** materiality, context, changed-property filtering and stopping rules.

### 28.5 Automatic invalidation
A dependency causes downstream rejection without actual review.

**Safeguard:** CandidateReview rather than AutomaticRejection.

### 28.6 Hidden centralisation
The graph becomes a de facto command structure.

**Safeguard:** dependency/authority separation.

### 28.7 Vulnerability exposure
The graph becomes a catalogue of sensitive weaknesses.

**Safeguard:** purpose-bounded visibility.

### 28.8 False equivalence
An alternative is treated as fully substitutable because it has a similar label.

**Safeguard:** capability/context validation and UNVERIFIED state.

### 28.9 Historical erasure
Correction or supersession deletes the old state.

**Safeguard:** preserve history and explicit supersession.

### 28.10 Priority laundering
Connectivity or criticality is silently converted into authority or priority.

**Safeguard:** traversal/materiality outputs are inputs to external prioritisation, not decisions.

## 29. Worked example — software library correction

Service A depends on Library B for cryptographic signature verification.

Library B version 4.2 is discovered to mishandle a particular signature case and is corrected in 4.3.

The dependency graph identifies Service A and two other services as direct dependents.

Service A never uses the affected signature mode. Review concludes NO_MATERIAL_DOWNSTREAM_EFFECT and propagation stops.

Service C does use the affected mode. It becomes REVIEW_REQUIRED and then MIGRATION_REQUIRED.

A reporting system depends on Service C's verified output. Only after Service C's state materially changes does review propagate to the reporting system.

The correction therefore creates a bounded review cascade rather than invalidating every object connected to Library B.

## 30. Worked example — research evidence correction

Policy Model P depends materially on Dataset D for one parameter estimate.

Dataset D is corrected after a measurement-calibration error is found.

The graph triggers review of P.

The review asks whether the corrected measurements materially alter P's parameter or conclusions.

If the parameter remains within the model's supported range, P may remain satisfied and propagation stops.

If P's output materially changes, downstream reports relying on that output become candidate reviews.

> **Evidence Correction ≠ Automatic Rejection of Every Downstream Conclusion**

## 31. Worked example — infrastructure failure

Facility X depends on Power Feed A.

A fails.

Backup Feed B is recorded as ALTERNATIVE_AVAILABLE but PARTIAL and UNVERIFIED for one high-load function.

Low-load systems may remain satisfied through B.

The high-load function becomes REVIEW_REQUIRED or DEPENDENCY_DEGRADED until B's capability is established.

The dependency graph identifies the difference without assuming either total facility failure or total equivalence of the backup.

## 32. Relationship to Architectural Unit Resolution

AUR asks whether an apparent omission or deficit is being attributed to the correct architectural unit.

KCS Change Propagation asks what downstream objects require reconsideration after a represented upstream object changes.

> **Unit Resolution ≠ Change Propagation**

## 33. Relationship to Continuity Protocol

Continuity asks what must survive disruption and whether enough has been preserved for genuine recovery.

KCS Change Propagation can expose prerequisite and recovery chains, but does not decide the continuity strategy.

> **Dependency Map ≠ Continuity Plan**

## 34. Relationship to Minimum Necessary Capability

MNC asks how much capability is justified by a legitimate function.

KCS Change Propagation may represent dependencies involving capabilities, but it does not decide how much capability or authority an actor should possess.

> **Dependency ≠ Authority**

## 35. External interfaces

The module may consume or supply information to:
- knowledge/state stores;
- configuration management;
- software dependency systems;
- model/data lineage systems;
- architecture registries;
- change-management workflows;
- continuity/recovery systems;
- risk systems;
- external schedulers/prioritisers;
- authority/governance systems;
- access-control systems;
- audit systems.

These systems remain distinct.

Consequential downstream actions—including public notification, regulatory action, recall, remediation, shutdown, resource allocation or enforcement—remain external unless a host architecture separately supplies legitimate authority and an applicable action process.

> **Review Requirement ≠ Authority to Execute the Remedy**

## 36. Minimum implementation

A minimal implementation requires:
1. identifiable objects;
2. typed dependency relations;
3. evidence/provenance;
4. state;
5. materiality or an equivalent applicability test;
6. change-event recording;
7. downstream traversal;
8. a review-required state;
9. a way to record review outcome;
10. a stopping rule;
11. preservation of unknown/disputed states.

Without these, “change propagation” risks becoming either an unbounded notification system or automatic invalidation.

## 37. Adversarial questions

Before accepting a propagation result, ask:
- Is this relation evidenced or merely assumed?
- Did the changed property actually supply something the dependent uses?
- Is the relation material in this context?
- Is an unaffected alternative available?
- Is the dependent already superseded?
- Are we confusing connection with effect?
- Are we confusing dependency with authority?
- Are we treating absence from the graph as proof of independence?
- Are we exposing sensitive dependency information unnecessarily?
- Are we preserving the old state?
- Why should propagation continue past this node?
- What evidence would justify stopping?

## 38. Falsification conditions

Reconsider or narrow this module if:
- represented dependencies do not improve downstream review accuracy/usefulness;
- maintenance cost consistently exceeds useful value;
- propagation produces mostly irrelevant review sets;
- relation semantics cannot remain sufficiently stable;
- host systems already provide the capability without useful benefit from this abstraction;
- dependency mapping creates unacceptable centralisation or security risk;
- source-grounded audits repeatedly contradict graph-derived dependencies.

## 39. Provenance

Portable extraction source:

*KCS Companion Upgrade 001 — Operational Dependency and Change-Propagation Architecture.*

The source is a canonical companion upgrade within Concord but explicitly corrigible and an initial operational version.

This portable specification abstracts the dependency/change-propagation mechanism from that host architecture.

## 40. Validation status

Currently supported:

> **A coherent standalone portable specification has been extracted from a substantial source architecture and has demonstrated independent transfer across two materially different non-Concord domains.**

### KCP-BTT-001
Domain: regional hospital laboratory and clinical-reporting infrastructure.  
Independent result: **KCP-T3 — FUNCTIONAL TRANSFER**.  
Frozen-key result: **26/26 materially confirmed**.

### KCP-BTT-002
Domain: municipal water-distribution control and public-notification infrastructure.  
Independent result: **KCP-T4 — STRONG TRANSFER**.  
Frozen-key result: **26/26 materially confirmed**.

Combined:

> **52/52 FROZEN PREDICTIONS MATERIALLY CONFIRMED**

> **NO FUNDAMENTAL FAILURE DETECTED**

BTT-002 successfully exercised the v0.2 clarifications concerning scoped change, historical/current/future distinction, non-transforming conduits, host thresholds, high-consequence unknowns, document semantics, alternative verification and coexistent classifications.

v0.3 adds only bounded clarifications exposed by BTT-002: explicit classification scope binding, host-owned unknown-escalation criteria, a generic REFERENCES relation, preservation of coexistent-state dimensions, and the external-action boundary.

Not supported:
- universal empirical validation;
- complete dependency discovery;
- automatic legal/ethical legitimacy;
- automatic prioritisation;
- automatic authority.

> **Portable Extraction ≠ External Validation**

## 41. Graduation status

Portable-Package Graduation Review 001: **PASS**.

> **GRADUATION CONDITIONS SATISFIED AT SPECIFICATION LEVEL**

> **52/52 FROZEN PREDICTIONS MATERIALLY CONFIRMED ACROSS TWO MATERIALLY DIFFERENT NON-CONCORD DOMAINS**

> **BTT-001: KCP-T3 — FUNCTIONAL TRANSFER**

> **BTT-002: KCP-T4 — STRONG TRANSFER**

> **NO THIRD BLIND TEST REQUIRED FOR SPECIFICATION-LEVEL GRADUATION**

> **NO RELEASE BLOCKER IDENTIFIED**

This v1.0 release is specification-level transfer validated. It remains subject to its stated epistemic, security and external-interface boundaries.
