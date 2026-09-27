# KMDI-001B — KCS Material Dependency Index — Candidate Extension

**Status:** V1.2a CANDIDATE KCS EXTENSION  
**Date:** September 2026  
**Canonical effect:** NONE  
**External knowledge state:** INTERNAL ONLY  
**Parent:** KMDI-001A Frozen Requirements

# 1. Architecture Statement

The **KCS Material Dependency Index (KMDI)** is a bounded relational layer within the Knowledge Control System.

Its purpose is:

> to make materially relevant dependencies among civil knowledge, capabilities and architectures discoverable, provenance-visible, contestable and updateable without turning the KCS into an authority over the systems it describes.

KMDI does not replace domain reasoning.

It answers:

- what is recorded as depending on what;
- for which function;
- according to what evidence/provenance;
- at what knowledge/version state;
- and what may need review when that relation changes.

# 2. Basic Object — Material Dependency Record (MDR)

A dependency is represented as an MDR:

**Dependent**
→ **Dependency Relation**
→ **Prerequisite / Upstream Object**

with fields sufficient to express:

- MDR ID;
- dependent object/capability/system;
- upstream object/capability/system;
- dependency type;
- functional scope;
- applicability/version;
- epistemic status;
- evidence/provenance reference;
- criticality if legitimately established;
- uncertainty;
- owning/reviewing domain;
- review trigger;
- Clock/state reference where relevant;
- correction/supersession links;
- last review state.

# 3. Dependency Types

KMDI reuses the Concord's existing dependency-analysis logic and permits typed relations such as:

## Existential Dependency
The dependent function cannot operate meaningfully without the upstream capability.

## Enabling Dependency
The upstream capability enables a function that otherwise remains unavailable.

## Quality / Reliability Dependency
The dependent can operate, but its reliability materially depends upon the upstream object.

## Evidence Dependency
A conclusion/model/decision materially relies upon specified evidence or knowledge.

## Interface Dependency
Two systems require a defined relation/interface for a function.

## Developmental Dependency
A system's further development is blocked or constrained by an upstream capability/maturity state.

## Continuity Dependency
Restoration/preservation of a function requires the upstream object/capability.

## Constraint Dependency
The dependent is bounded by a constitutional, ethical, legal or architectural constraint.

These are not necessarily exhaustive.

New types may be added with provenance rather than forcing false classification.

# 4. Dependency State

Each MDR can carry a state:

- VERIFIED;
- PROVISIONAL;
- DISPUTED;
- SUPERSEDED;
- BROKEN / UNSATISFIED;
- UNKNOWN / INCOMPLETE.

The status concerns the recorded relation, not metaphysical truth.

# 5. Material Change Event

When an indexed upstream object changes materially:

Upstream Change
→ identify relevant MDRs
→ identify recorded dependents
→ generate bounded review candidates.

Not:

Upstream Change
→ automatically rewrite all downstream systems.

The KMDI routes attention.

It does not decide the result.

# 6. Review Trigger

A review trigger should minimally state:

- changed object;
- nature/version of change;
- dependency relation;
- affected scope;
- downstream object;
- why review may be material;
- provenance;
- uncertainty;
- responsible/legitimate reviewing domain.

The downstream owner can then determine:

NO EFFECT
 / UPDATE
 / HOLD
 / INVESTIGATE
 / PROPAGATE FURTHER.

# 7. Bounded Propagation

Correction propagation follows material dependency edges only as far as justified.

Conceptually:

Correction(B)
→ Dependents(B)
→ Materiality Review
→ affected A
→ Dependents(A)
→ ...

Propagation terminates where:

- dependency is not material to the changed property;
- downstream state remains valid;
- relation is superseded;
- uncertainty requires HOLD rather than assumed effect;
- domain review determines no further consequence.

This prevents indiscriminate repository-wide rollback.

# 8. Provenance and Historical State

MDR corrections are additive/versioned.

Old relation
→ correction/supersession
→ new relation.

The historical dependency state remains recoverable.

This allows later questions such as:

> Why was system A developed this way at time T?

to be answered using the dependency knowledge actually available then.

# 9. Missing-Edge Rule

KMDI adopts an explicit ESCP safeguard:

**No MDR(A,B) != NoDependency(A,B).**

Search completeness must be represented separately from dependency status.

A query may return:

- recorded dependency found;
- recorded dependency not found;
- search scope incomplete;
- relationship unknown.

# 10. Contestability

A consequential MDR should support:

Claim
→ provenance
→ challenge
→ independent/domain review
→ confirm / amend / dispute / supersede.

KCS classification authority therefore remains bounded and correctable.

# 11. Current-Task Retrieval

KMDI extends KCS's existing principle:

> Retrieve what is relevant to the current task.

A consumer can request:

- prerequisites for object X;
- dependents of object X;
- unresolved dependencies affecting X;
- changes since Clock state T;
- dependencies relevant to function F;
- broken developmental dependencies;
- critical continuity prerequisites;
- dependency edges requiring review.

The response should be bounded to legitimate need.

# 12. Clock Interface

KMDI and the Civilisation Clock are complementary.

KMDI:
**what depends upon what and what changed?**

Clock:
**where are we in developmental/civil state and what should be acted upon/reviewed now?**

Interface:

KMDI dependency/change state
→ Clock priority/development analysis
→ Clock transition
→ KMDI update/review.

Neither becomes sovereign over the other.

# 13. State Map Interface

A State Map entry can now contain:

System
→ maturity/state
→ unresolved dependencies
→ upstream blockers
→ downstream dependents
→ last material change
→ review state.

This converts maturity from an isolated label into relational state.

# 14. Induction Interface

For a task T:

Task T
→ relevant system/object
→ KMDI prerequisite traversal
→ bounded KCS retrieval package.

This can reduce the need for an incoming participant to rediscover the entire architectural context manually.

# 15. Continuity Interface

For civil function F:

F
→ material prerequisites
→ prerequisite dependencies
→ minimum restoration candidate set.

This is a candidate restoration map, not proof of completeness.

ESCP remains explicit.

# 16. Emergency Interface

Emergency systems may query:

Threatened capability
→ known critical dependencies
→ known downstream exposure
→ stale/uncertain dependency edges.

Emergency authority remains entirely outside KMDI.

# 17. Resource-Steering Interface

A model/output can identify:

Model M
→ evidence assumptions
→ structural assumptions
→ resource dependencies
→ model version.

If an upstream assumption changes, KMDI can route the model for review.

It cannot automatically reallocate resources.

# 18. Developmental Topology Interface

Topology can reuse KMDI edges rather than rediscovering all relationships on every pass.

But topology must still test:

- whether the edge is current;
- whether the relation is genuinely material;
- whether unrecorded relations may exist;
- whether the owning system is correctly identified.

KMDI is therefore an input to topology, not a substitute for topology.

# 19. Recursive Self-Application

KMDI must index its own important dependencies:

KMDI
→ KCS provenance
→ Clock temporal state
→ domain review
→ storage/retrieval infrastructure
→ correction architecture.

Changes to KMDI's own schema are versioned and reviewable.

# 20. Minimal Machine-Readable Relation

Conceptually:

{
 dependent,
 prerequisite,
 relation_type,
 scope,
 status,
 version_applicability,
 provenance,
 uncertainty,
 owner,
 review_trigger,
 clock_state,
 supersedes
}

This is an information model, not a frozen implementation format.

# 21. K1–K22 Check

K1 material relation — SATISFIED.
K2 typed dependency — SATISFIED.
K3 scope — SATISFIED.
K4 provenance — SATISFIED.
K5 epistemic status — SATISFIED.
K6 version applicability — SATISFIED.
K7 owner separation — SATISFIED.
K8 downstream discovery — SATISFIED.
K9 no automatic consequence — SATISFIED.
K10 correction propagation — SATISFIED.
K11 historical preservation — SATISFIED.
K12 missing-edge humility — SATISFIED.
K13 contestability — SATISFIED.
K14 current-state retrieval — SATISFIED.
K15 bounded disclosure — SATISFIED architecturally.
K16 circularity visibility — SATISFIED through graph representation.
K17 criticality without sovereignty — SATISFIED.
K18 temporal compatibility — SATISFIED.
K19 continuity compatibility — SATISFIED.
K20 domain extensibility — SATISFIED architecturally.
K21 machine/human accessibility — SATISFIED architecturally.
K22 recursive self-application — SATISFIED.

# 22. Residual Questions

KMDI-R1 — How should dependency criticality be evaluated without false numerical precision?

KMDI-R2 — How should stale dependency edges be detected efficiently?

KMDI-R3 — What minimum dependency information may cross privacy/security boundaries?

KMDI-R4 — How should contradictory dependency claims from different domains coexist and resolve?

KMDI-R5 — How should large dependency cascades be bounded operationally?

These are residual development questions, not yet new systems.

# 23. Candidate Status

The minimum architecture satisfies the frozen K1–K22 at conceptual/architectural level.

It should now be tested against the separately frozen P1–P8 downstream predictions.

Only demonstrated downstream improvement counts as evidence for the upstream-bottleneck hypothesis.
