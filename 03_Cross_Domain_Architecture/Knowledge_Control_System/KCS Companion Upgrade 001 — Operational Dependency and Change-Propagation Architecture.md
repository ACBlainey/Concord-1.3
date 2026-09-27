# KCS Companion Upgrade 001 — Operational Dependency and Change-Propagation Architecture

**Author:** Alexander C. Blainey — Independent Researcher
**Project:** The Concord Framework
**Status:** CANONICAL COMPANION UPGRADE — CORRIGIBLE / INITIAL OPERATIONAL VERSION
**Parent system:** The Concord Knowledge Control System
**Interface architecture:** Civilisational Developmental Topology
**Date:** September 2026

## Abstract

The original Concord Knowledge Control System defines civilisational memory as more than storage. It preserves content, provenance, epistemic status, history, supersession, failed investigations and reusable knowledge while avoiding the fiction that a shared knowledge base is an oracle.

The Civilisational Developmental Topology exposes a further operational requirement: civilisation must know not only what knowledge exists, but what depends upon what.

A correction to an upstream architecture may invalidate a downstream assumption. A deprecated interface may require several systems to be reviewed. A development target may appear local while actually being blocked by an immature shared prerequisite.

This companion extends KCS with an operational Dependency and Change-Propagation Layer. It does not replace or rewrite the original KCS.

> **Record not only what civilisation knows, but the material relationships that determine what must be reconsidered when that knowledge changes.**

# 1. Why the Original KCS Is Preserved

The original KCS remains the foundational architecture. It already establishes distributed logical civilisational memory; content; provenance; epistemic status; history; active, available, archived, provisional, disputed, superseded and rejected states; preservation of honest failure; resource stewardship; attribution and reuse.

The developmental rule is:

**Existing Canonical System + Companion Upgrade → Current Integrated System State.**

The foundation remains visible. The upgrade records the newly exposed requirement and solution.

# 2. The Missing Operational Capability

The original KCS can answer what exists, where it came from, its status, what superseded it and what was learned.

The developmental topology additionally requires:

- What does this object depend upon?
- What depends upon it?
- Which dependency is materially consequential?
- Which dependency is blocking another system?
- If this object changes, what must be reviewed?
- If it fails, which functions may degrade?
- Is an alternative supplier available?
- Is the relation current, stale, unknown or disputed?

The required extension is a **live dependency representation**.

# 3. KCS Dependency Layer

Let the KCS knowledge graph be:

**K(t) = <V, R, P, S, H>**

where V is knowledge/architecture objects, R typed material relations, P provenance, S current status and H historical state/change record.

A dependency record is:

**d = <source, target, capability, type, materiality, state, context, evidence, confidence, time>.**

# 4. Dependency Objects

KCS should not restrict dependency tracking to documents. Objects may include civilisational functions, systems, architectures, interfaces, protocols, datasets, models, software, standards, constitutional provisions, evidence bases, recovery capabilities, external services, physical infrastructure and legitimately represented participant capabilities.

A document may evidence a dependency without being the dependency itself.

# 5. Core Dependency Relations

Initial shared types:

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

Additional domain relations may exist, but shared types should remain semantically stable.

# 6. Dependency State

Minimum vocabulary:

- ACTIVE
- SATISFIED
- DEGRADED
- BLOCKING
- FAILED
- ALTERNATIVE_AVAILABLE
- SUPERSEDED
- UNKNOWN
- DISPUTED

A dependency is not BLOCKING merely because it exists. BLOCKING means the current prerequisite state materially prevents or constrains the dependent function.

# 7. Materiality and Criticality

Materiality may be CRITICAL, HIGH, MODERATE, LOW, IMMATERIAL, UNKNOWN or DISPUTED, and is context-sensitive.

Criticality should consider consequence of failure, importance and number of dependents, alternatives, recovery difficulty, time sensitivity, reversibility and correlated exposure.

KCS should preserve component evidence rather than compressing all dimensions into one number by default.

# 8. Upstream and Downstream Traversal

For object x:

**Up(x) = objects on which x materially depends.**

**Down(x) = objects materially dependent upon x.**

Recursive traversal supports prerequisite discovery, affected-object discovery, owner tracing and shared upstream bottleneck detection.

Traversal does not itself determine development priority.

# 9. Change Events

A consequential change event should record object, old state, new state, reason, evidence, time and actor/source.

Examples include validation, correction, supersession, deprecation, interface change, owner change, dependency discovery/removal, failure, recovery, contested status and version change.

The event becomes part of provenance/history.

# 10. Change Propagation

When object x changes, KCS should identify materially dependent downstream objects.

The output is a **review set**, not automatic invalidation.

**Change(x) → CandidateReview(y)**

rather than:

**Change(x) → AutomaticRejection(y).**

This prevents both silent dependency failure and uncontrolled cascade.

# 11. Selective Propagation

Propagation should stop where the dependency is immaterial, an unaffected alternative satisfies the requirement, the downstream object is superseded, context makes the relation non-applicable, or evidence shows the change does not alter the dependent function.

Propagation should escalate where high-consequence functionality depends on the changed object, no alternative exists, failure may be silent, multiple dependents share the prerequisite, or constitutional/rights consequences may be affected.

# 12. Correction Propagation

For corrected object x:

1. preserve the previous state;
2. record the correction;
3. identify materially dependent objects;
4. mark them REVIEW_REQUIRED where justified;
5. surface review through legitimate interfaces;
6. preserve review outcomes;
7. clear the flag where dependency remains satisfied;
8. propagate further only where downstream state materially changes.

This creates bounded recursive correction.

# 13. Supersession Propagation

Supersession should not erase the old object.

Represent old object as SUPERSEDED_BY new object.

Dependents should be classified as COMPATIBLE_WITH_NEW, MIGRATION_REQUIRED, REVIEW_REQUIRED, LEGACY_DEPENDENCY or UNKNOWN.

# 14. Failure and Alternatives

For a failed object, KCS should expose direct dependents, critical indirect dependents, available alternatives, recovery owners, degraded modes and unresolved unknowns.

Alternatives may be FULL, PARTIAL, EMERGENCY_ONLY, DEGRADED or UNVERIFIED.

Similar labels do not establish equivalence.

# 15. Ownership and Dependency Are Different

If A depends on B, B does not thereby govern A.

**Dependency ≠ Subordination.**

Authority requires separate legitimate architecture.

# 16. Distributed Ownership

KCS should permit multiple legitimate suppliers with roles such as PRIMARY, CO-OWNER, DISTRIBUTED_SUPPLIER, DELEGATED, INTERFACE_SUPPLIER and FALLBACK.

The graph must not force distributed architecture into a false single-owner model.

# 17. Unknown and Disputed Dependencies

First-class states should include UNKNOWN_OWNER, UNKNOWN_DEPENDENCY, UNKNOWN_MATERIALITY, DISPUTED_DEPENDENCY, DISPUTED_OWNER and DISPUTED_EFFECT.

Unknown must not silently become absent. Disputed must not silently become false.

# 18. Freshness and Review

Each material dependency should support first recorded, last confirmed, last changed, next review, evidence freshness, source/reviewer and confidence.

A stale relation may become REVIEW_OVERDUE without automatic deletion.

# 19. Minimal Dependency Record

A practical minimum record contains:

- ID
- source
- target
- capability
- relation type
- context
- materiality
- criticality
- state
- alternatives
- failure effect
- evidence
- confidence
- first recorded
- last confirmed
- next review

The logical schema precedes implementation choice.

# 20. Integration With Civilisational Developmental Topology

CDT defines the formal grammar. KCS maintains live knowledge about instantiated objects and relations.

**CDT → Schema**

**KCS → Live Dependency State**

CDT should not maintain a competing dependency database. KCS should not decide which topology is constitutionally correct merely because it stores it.

# 21. Integration With the Civil State Map

The State Map consumes KCS dependency state to determine prerequisite satisfaction, blockers, uncertainty, downstream reliance and whether maturity deficits are local or upstream.

KCS returns evidence/state. The State Map performs developmental synthesis.

# 22. Integration With the Civilisation Clock

The Clock uses dependency state for ordering. If A depends on B and both require development, developing B first may be rational unless consequence dictates otherwise.

KCS supplies the relation. The Clock supplies temporal/developmental ordering. KCS does not become a scheduler.

# 23. Integration With Continuity

Continuity planning should be dependency-aware. Preserving a system's documents is insufficient if reconstruction requires lost prerequisites.

**Recovery(function) requires preservation of its necessary prerequisites.**

The Legacy Ladder and continuity architecture can use KCS dependency state to identify reconstruction chains.

# 24. Integration With Active Development

When development changes a canonical object:

1. record the candidate change;
2. preserve prior state;
3. identify affected dependents;
4. freeze predicted effects;
5. develop/test;
6. record evaluation;
7. on legitimate adoption, update current state;
8. create review flags for materially affected dependents.

# 25. Companion Upgrade Provenance

Where an existing canonical system is extended by a companion paper, KCS should represent:

**Foundation ← EXTENDED_BY — Companion.**

The foundation is not obsolete unless explicitly superseded.

The integrated system state is the foundation plus applicable companions.

# 26. Privacy and Access Boundaries

Dependency knowledge can reveal infrastructure vulnerabilities, participant dependencies, emergency weaknesses, privileged interfaces and security-critical recovery paths.

Not every dependency record should therefore be universally visible.

Purpose-bounded access should permit the existence of a dependency to be represented without necessarily exposing every operational detail.

Legibility must not become a vulnerability catalogue.

# 27. Anti-Centralisation Boundary

A live dependency graph may appear to offer a commanding view of civilisation. That view must not become sovereign.

KCS records, preserves, retrieves, links, flags and propagates review requirements.

KCS does not automatically command systems, allocate resources, approve constitutional changes, adjudicate disputes, define ethical legitimacy, rank persons or impose development priorities.

**Knowledge State ≠ Civil Authority.**

# 28. Failure Modes

Dependency hallucination: safeguard with provenance, confidence and UNKNOWN.

Missing dependency: safeguard with ESCP; absence from KCS is not proof of civil absence.

Stale dependency: safeguard with freshness/review.

Cascade overload: safeguard with materiality thresholds and selective propagation.

Hidden centralisation: safeguard by separating dependency, priority and authority.

Vulnerability exposure: safeguard with purpose-bounded access.

False equivalence: validate alternatives contextually.

Historical erasure: preserve superseded state.

# 29. Initial Operational Test

The first dependency test should remain bounded.

Use the chain:

**Formal Topology → KCS Dependency Graph → State Map → Civilisation Clock**

and at least one downstream dependency-blocked function such as formal civil reachability or shared civil reference.

For each object record ID, owner, capability, dependency, state, materiality, evidence, uncertainty and predicted change propagation.

Then test whether an upstream change produces the correct bounded review set.

# 30. Falsification Conditions

Reconsider this upgrade if dependency records do not improve developmental decisions; maintenance cost exceeds useful value; propagation produces mostly irrelevant reviews; topology semantics are unstable; original KCS already supplies the capability without extension; mapping creates unacceptable centralisation/security risk; or source-grounded audits repeatedly contradict graph-derived dependencies.

# 31. Resulting KCS Capability

With this companion KCS can answer:

- What exists?
- What is its status?
- Where did it come from?
- What changed?
- What does it depend upon?
- What depends upon it?
- What may need review if it changes?
- Which dependencies are blocking development?
- Which alternatives or recovery paths exist?

# Conclusion

The Knowledge Control System already provides the Concord with a model of civilisational memory.

This companion extends that memory into relational operational knowledge:

**Knowledge Object + Provenance + Status + History + Dependencies + Change Propagation.**

That does not turn KCS into a central planner. It allows civilisation to remember the relationships that make its systems work together.

The next developmental step is to instantiate these relationships in a bounded real State Map and test whether the topology, KCS dependency layer and Civilisation Clock can recover a useful development order from represented civil state.
