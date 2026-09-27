# Dependency-Aware Civilisational Graph v0.1 — Populated Prospective Test Slice

**Status:** V1.2a MACHINE-READABLE / HUMAN-AUDITABLE TEST MODEL  
**Date:** September 2026  
**External knowledge state:** INTERNAL ONLY  
**Canonical effect:** NONE

# 1. Purpose

Populate a small source-grounded dependency graph before selecting the next bottleneck.

This graph is intentionally incomplete. It is a test slice, not a claim to represent all Concord dependencies.

**ESCP:** absence of a node or edge means only “not represented in this test slice.”

# 2. Node Schema

Each node records:

- ID;
- architectural unit;
- broad current maturity;
- capabilities represented in reviewed source;
- unresolved maturity notes.

Maturity labels are qualitative and source-relative:

- EARLY;
- DEVELOPING;
- SUBSTANTIALLY DEVELOPED;
- MATURE DOMAIN ARCHITECTURE;
- UNKNOWN/UNASSESSED.

# 3. Nodes

## N01 — Civilisation Clock
**Maturity:** DEVELOPING / experimentally extended in V1.2a.
**Owns:** cycles, developmental sequencing, temporal/developmental transitions, priority timing.
**Known deficit:** operationalisation and wider validation.

## N02 — KCS
**Maturity:** DEVELOPING.
**Owns:** civil knowledge state, provenance, retrieval, knowledge lifecycle, dependency mapping.
**V1.2a extension:** KMDI.

## N03 — Concord State Map
**Maturity:** EARLY / CONCEPTUAL.
**Source definition:** continuously updated representation of completed, incomplete, dependent and unresolved components.
**Known deficit:** no verified standalone operational state representation found in reviewed source.

## N04 — Priority / Dependency Architecture
**Maturity:** DEVELOPING.
**Owns:** priority bands, prerequisite/dependency-aware development gating, justified cross-layer bypass.

## N05 — Induction Protocol
**Maturity:** DEVELOPING.
**Owns:** progressive access to current state, principles, capabilities, uncertainty and participation.

## N06 — Metrics Reliability / Correction
**Maturity:** SUBSTANTIALLY DEVELOPED.
**Owns:** measurement provenance, uncertainty, versioning, correction propagation, meta-metrics.

## N07 — Case-Learning / Structural Knowledge
**Maturity:** SUBSTANTIALLY DEVELOPED CANDIDATE.
**Owns:** structural knowledge extraction, uncertainty, causal humility, provenance, model correction.

## N08 — Recursive Oversight
**Maturity:** SUBSTANTIALLY DEVELOPED PORTABLE MODULE.
**Owns:** reviewability, correction, escalation, provenance, anti-capture of oversight.

## N09 — Continuity Protocol
**Maturity:** SUBSTANTIALLY DEVELOPED CONSTITUTIONAL ARCHITECTURE.
**Owns:** functional/civil continuity, preservation, restoration principles, continuity declarations, resilience.

## N10 — Constitutional Emergency
**Maturity:** DEVELOPED CONSTITUTIONAL ARCHITECTURE.
**Owns:** bounded emergency action, emergency safeguards, review and recovery.

## N11 — CA-05 Predictive System-Steering / Resource Allocation
**Maturity:** DEVELOPED CANDIDATE ARCHITECTURE / EMPIRICALLY UNVALIDATED.
**Owns:** aggregate evidence-driven infrastructure/resource adaptation.

## N12 — CA-03 Civilisational Learning and Metrics
**Maturity:** DEVELOPED CANDIDATE ARCHITECTURE.
**Owns:** conversion of outcomes into corrigible structural civil knowledge.

## N13 — Developmental Topology
**Maturity:** V1.2a EXPERIMENTAL.
**Owns:** gap detection, ownership resolution, maturity/dependency analysis, development routing.

## N14 — Temporal Review / Development Health
**Maturity:** ACTIVE DEVELOPMENT.
**Owns:** periodic review, carry-forward, stale/open work detection, development-health signals.

# 4. Source-Grounded Dependency Edges

Format:

Dependent --[relation]--> Upstream Owner

## E01
N01 Clock --[requires current civilisational state representation]--> N03 State Map.

## E02
N01 Clock --[requires prerequisite/dependency knowledge]--> N02 KCS/KMDI.

## E03
N01 Clock --[uses development priority rules]--> N04 Priority Architecture.

## E04
N04 Priority Architecture --[requires dependency state]--> N02 KCS/KMDI.

## E05
N05 Induction --[requires current Concord state]--> N03 State Map.

## E06
N05 Induction --[requires bounded relevant knowledge retrieval]--> N02 KCS.

## E07
N03 State Map --[requires knowledge/status/dependency inputs]--> N02 KCS/KMDI.

## E08
N03 State Map --[requires temporal transition/state position]--> N01 Clock.

This is an intentional feedback relation, not automatically a pathological cycle.

## E09
N14 Temporal Review --[requires temporal/developmental position]--> N01 Clock.

## E10
N14 Temporal Review --[requires open-item/dependency state]--> N02 KCS/KMDI.

## E11
N06 Metrics Reliability --[requires source/extraction provenance]--> N12/knowledge sources.

## E12
N11 Resource Steering --[requires civil metrics/structural knowledge]--> N12 CA-03.

## E13
N11 Resource Steering --[requires reliability/correction state]--> N06 Metrics Reliability.

## E14
N10 Emergency --[requires bounded review/oversight]--> N08 Recursive Oversight.

## E15
N10 Emergency --[requires dependency knowledge for resilience planning]--> N02 KCS/KMDI.

## E16
N09 Continuity --[requires preserved knowledge/provenance]--> N02 KCS.

## E17
N09 Continuity --[requires functional dependency knowledge for restoration]--> N02 KCS/KMDI.

## E18
N13 Developmental Topology --[requires dependency knowledge]--> N02 KCS/KMDI.

## E19
N13 Developmental Topology --[requires maturity/current-state representation]--> N03 State Map.

## E20
N13 Developmental Topology --[requires temporal/developmental transition state]--> N01 Clock.

## E21
N03 State Map --[requires maturity/readiness observations]--> metrics/readiness architecture.

## E22
N04 Priority Architecture --[requires current unresolved/completed state]--> N03 State Map.

## E23
N14 Development Health --[requires current state and historical state comparison]--> N03 State Map.

## E24
N11 Resource Steering --[benefits from current structural/civil state]--> N03 State Map.

This edge is enhancement rather than existential.

# 5. Edge Confidence

For this first slice:

- E01–E10, E12–E20, E22–E23 are treated as **strongly source-supported or directly implied by explicit architecture descriptions**.
- E11 and E21 compress multiple source relations and require later decomposition.
- E24 is an **enhancement dependency**, not a claim that CA-05 cannot function without the State Map.

# 6. Bottleneck Discovery Procedure

Exclude N01 Clock and N02 KCS because they were already selected/developed in earlier demonstrations.

For remaining nodes:

1. count represented downstream dependents;
2. distinguish existential/enabling dependencies from enhancement;
3. inspect maturity;
4. ask whether one missing capability is shared across dependents;
5. reject nodes that are highly connected only because they are broad constitutional constraints;
6. prefer a candidate where development produces a falsifiable downstream prediction.

No numerical priority score is imposed.

# 7. Blind Result

Among untested nodes, **N03 — Concord State Map** emerges as the strongest next bottleneck candidate.

Represented downstream consumers include:

- Civilisation Clock;
- Induction;
- Priority / Dependency Architecture;
- Developmental Topology;
- Temporal Review / Development Health;
- potentially Resource Steering as an enhancement consumer.

The State Map itself depends upstream on KCS/KMDI, Clock transition state and maturity/readiness observations.

This gives it a distinctive architectural position:

KCS/KMDI + Clock + Metrics/Readiness
→ **State Map**
→ Clock / Priority / Induction / Topology / Development Health.

# 8. Why N03 Wins This Test Slice

The State Map is highly connected **and** currently early/conceptual.

Its source definition is already clear:

> a continuously updated representation of completed, incomplete, dependent and unresolved components.

But the reviewed source does not yet establish a standalone operational representation sufficient to answer:

- What systems currently exist?
- What maturity state is each in?
- What capabilities are present?
- What is unresolved?
- What is blocked?
- By what?
- What changed since the prior state?
- What requires review?
- What evidence supports the state classification?
- What uncertainty exists in the map itself?

This is exactly the kind of maturity deficit the dependency model predicts should become visible after developing Clock and KCS.

# 9. Prospective Prediction Before State-Map Development

If the State Map is a genuine third upstream bottleneck, developing it should improve at least:

P-SM1 — Clock state assessment.
P-SM2 — Priority/dependency selection.
P-SM3 — Induction current-state navigation.
P-SM4 — Developmental topology maturity/dependency analysis.
P-SM5 — Temporal review comparison across periods.

Secondary:

P-SM6 — Resource steering should gain a clearer civil structural-state input, but this is expected to be enhancement rather than closure of a hard block.

# 10. Important Dependency Cycle

The graph exposes:

Clock → State Map
and
State Map → Clock.

This is not necessarily circular failure.

The likely relation is iterative:

StateMap(t)
→ Clock cycle/transition
→ State changes
→ StateMap(t+1).

Similarly:

KMDI
→ State Map
→ development decisions
→ new/corrected knowledge
→ KMDI update.

The graph therefore begins to expose **healthy recursive cycles** as well as blocking dependencies.

# 11. Test Status

This is the first prospective bottleneck selected from a populated graph rather than chosen directly from an observed local gap.

**Candidate third bottleneck: CONCORD STATE MAP.**

Do not develop it yet.

First freeze its required inputs/outputs and perform a source-resolution test for whether an operational State Map already exists elsewhere under another name.
