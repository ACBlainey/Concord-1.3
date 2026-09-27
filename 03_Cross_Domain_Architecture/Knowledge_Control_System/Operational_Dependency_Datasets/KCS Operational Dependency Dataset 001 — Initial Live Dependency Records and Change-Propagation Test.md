# KCS Operational Dependency Dataset 001 — Initial Live Dependency Records and Change-Propagation Test

**Author:** Alexander C. Blainey — Independent Researcher
**Project:** The Concord Framework
**Status:** CANONICAL OPERATIONAL DATASET / TEST — PROVISIONAL / CORRIGIBLE
**Parent system:** Knowledge Control System + Companion Upgrade 001
**Source register:** Canonical Topology Register 001
**Date:** September 2026

## Purpose

This document instantiates the first operational dependency records defined by KCS Companion Upgrade 001.

It converts the 20 high-confidence material edges in Canonical Topology Register 001 into KCS-style records with context, materiality, state, failure effect, evidence, confidence and review state.

It then performs the first bounded change-propagation test.

This is intentionally a small dataset. Its purpose is to test whether dependency representation produces useful bounded review consequences before the graph is expanded.

# 1. Record Schema

Each record uses:

**KDR = {ID, Source, Relation, Target, Capability, Context, Materiality, State, Failure Effect, Evidence, Confidence, Freshness}.**

Materiality:

- CRITICAL
- HIGH
- MODERATE
- LOW
- UNKNOWN
- DISPUTED

State:

- ACTIVE
- SATISFIED
- DEGRADED
- BLOCKING
- FAILED
- ALTERNATIVE_AVAILABLE
- SUPERSEDED
- UNKNOWN
- DISPUTED

Confidence:

- HIGH
- MODERATE
- LOW
- UNKNOWN

Freshness for this initial dataset:

**CURRENT-INITIAL-POPULATION — September 2026**

# 2. Initial Dependency Records

| ID | Source | Relation | Target | Capability | Materiality | State | Failure Effect | Evidence | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| KDR-001 | L1-02 | DEPENDS_ON | L1-10 | Stable topology semantics | HIGH | ACTIVE | Dependency graph becomes ambiguous/inconsistent | CDT Mathematical Model; Topology Register | HIGH |
| KDR-002 | L1-03 | DEPENDS_ON | L1-02 | Live dependency state | HIGH | ACTIVE | State synthesis cannot reliably distinguish local/upstream deficits | KCS Companion; State Map | HIGH |
| KDR-003 | L1-11 | DEPENDS_ON | L1-03 | Current developmental state | HIGH | ACTIVE | Levelling/queue inputs become stale or intuition-led | State Map; ODG-001 | HIGH |
| KDR-004 | L1-09 | DEPENDS_ON | L1-10 | Formal structural semantics | HIGH | BLOCKING | Formal/machine reachability cannot be reliably encoded | Topology Register; State Map | HIGH |
| KDR-005 | L2-03 | DEPENDS_ON | L1-10 | Shared formal reference grammar | HIGH | BLOCKING | Shared civil reference remains semantically unstable | Topology Register; State Map | HIGH |
| KDR-006 | L2-03 | DEPENDS_ON | L1-02 | Live provenance/dependency state | HIGH | ACTIVE | Shared reference lacks current relational state | KCS Companion; Topology Register | HIGH |
| KDR-007 | L3-01 | DEPENDS_ON | L2-03 | Reconciled/shared civil reference | HIGH | BLOCKING | Meta-coherence remains distributed without stable common reference | L3 baseline; Topology Register | HIGH |
| KDR-008 | L1-04 | DEPENDS_ON | L1-02 | Dependency/change propagation knowledge | HIGH | ACTIVE | Corrections may fail to reach material dependents or over-propagate | KCS Companion | HIGH |
| KDR-009 | L1-12 | DEPENDS_ON | L1-02 | Cross-system dependency/failure knowledge | HIGH | ACTIVE | Failure effects cannot be reliably traced across systems | KCS Companion; Continuity interface | HIGH |
| KDR-010 | L2-14 | DEPENDS_ON | L1-12 | Cross-system failure/resilience state | HIGH | ACTIVE | Partial-failure coordination lacks failure-chain visibility | State Map; Topology Register | HIGH |
| KDR-011 | L2-14 | DEPENDS_ON | L1-03 | Current civil state | HIGH | ACTIVE | Coordination may act on stale/partial state | State Map | HIGH |
| KDR-012 | L3-08 | DEPENDS_ON | L1-12 | Failure-domain/cross-system resilience representation | HIGH | ACTIVE | Correlated failure may remain hidden | Continuity; Topology Register | MODERATE |
| KDR-013 | L3-05 | DEPENDS_ON | L2-11 | Identity/membership continuity | HIGH | ACTIVE | Fork/succession cannot reliably preserve standing, rights or obligations | Baseline; IA/AD development domains | HIGH |
| KDR-014 | L3-05 | INTERFACES_WITH | L3-14 | Peaceful-distance/residual relationship handling | HIGH | ACTIVE | Separation architecture may lack stable post-fork relationship rules | IA/AD | MODERATE |
| KDR-015 | L3-06 | DEPENDS_ON | L3-03 | Semantic continuity | HIGH | ACTIVE | External functional recognition may compare labels rather than functions | IA; CDT | HIGH |
| KDR-016 | L3-06 | DEPENDS_ON | L3-04 | Constitutional/functional equivalence | HIGH | ACTIVE | Heterogeneous implementations cannot be reliably recognised as equivalent | IA; CDT | HIGH |
| KDR-017 | L3-03 | DEPENDS_ON | L2-03 | Shared/plural reference capability | HIGH | ACTIVE | Deep-change semantic continuity lacks reconciled reference | CDT; Continuity | HIGH |
| KDR-018 | L3-15 | DEPENDS_ON | L1-05 | Provenance/history | HIGH | ACTIVE | Forgetting/expiry may destroy reconstruction/accountability context | KCS; Continuity | HIGH |
| KDR-019 | L3-15 | INTERFACES_WITH | L0-01 | Bounded information/privacy constraints | CRITICAL | ACTIVE | Retention or forgetting may violate privacy, contestability or legitimate purpose | CC; KCS | HIGH |
| KDR-020 | L3-11 | DEPENDS_ON | L1-11 | Developmental state/sufficiency evidence | HIGH | ACTIVE | Stopping condition becomes arbitrary or premature | CDT State Map | HIGH |

All records use the current canonical civil-development context unless a narrower context is later specified.

# 3. Initial Graph Checks

## 3.1 No orphan dependency records

All source and target IDs resolve to Canonical Topology Register 001.

## 3.2 No dependency implies authority

No DEPENDS_ON edge is interpreted as delegation, governance or subordination.

## 3.3 Blocking is selective

Only KDR-004, KDR-005 and KDR-007 are initially BLOCKING.

Other dependencies are ACTIVE because they materially matter but do not presently justify a claim that the dependent function cannot operate at all.

## 3.4 Criticality is not connectivity

KDR-019 is CRITICAL despite not being part of the most connected infrastructure chain.

This preserves the consequence guard.

# 4. First Change-Propagation Test

## Test event CP-001

Assume the definition or relation semantics of **L1-10 — Civilisational Topology / Integrated Structural Representation** materially change during formal population.

This is a realistic event because L1-10 is currently PRESENT-EXPLICIT / DEVELOPING.

Change event:

**CP-001 = MATERIAL_SEMANTIC_CHANGE(L1-10).**

Question:

> Which nodes should be reviewed, and how far should propagation travel?

# 5. Direct Dependents of L1-10

From the current KCS records:

- KDR-001: L1-02 depends on L1-10.
- KDR-004: L1-09 depends on L1-10.
- KDR-005: L2-03 depends on L1-10.

Therefore the direct review set is:

**R1 = {L1-02, L1-09, L2-03}.**

All three are material.

# 6. Second-Order Dependents

If CP-001 materially changes L1-02, its dependents include:

- L1-03 through KDR-002;
- L1-04 through KDR-008;
- L1-12 through KDR-009;
- L2-03 through KDR-006.

If CP-001 materially changes L2-03, its dependents include:

- L3-01 through KDR-007;
- L3-03 through KDR-017.

Therefore candidate second-order review set:

**R2 = {L1-03, L1-04, L1-12, L3-01, L3-03}.**

However these are not automatically REVIEW_REQUIRED.

They become REVIEW_REQUIRED only if the direct dependent's own state or interface changes materially.

# 7. Third-Order Candidates

Potential downstream nodes include:

- L1-11 through L1-03;
- L2-14 through L1-03 or L1-12;
- L3-08 through L1-12;
- L3-06 through L3-03;
- L3-11 through L1-11.

These form:

**R3-candidate = {L1-11, L2-14, L3-08, L3-06, L3-11}.**

Propagation should reach these only after an actual material change is confirmed in an intermediate dependency.

# 8. Propagation Boundary

The test therefore rejects two extremes.

## Too narrow

Only reviewing L1-02, L1-09 and L2-03 risks silent downstream inconsistency.

## Too broad

Immediately flagging every reachable node would create cascade overload.

The correct bounded rule is:

**Change → direct material review → propagate only through materially changed dependents.**

This matches KCS Companion Upgrade 001.

# 9. CP-001 Frozen Prediction

If L1-10 changes materially:

### Immediate REVIEW_REQUIRED

- L1-02
- L1-09
- L2-03

### CONDITIONAL_REVIEW

- L1-03
- L1-04
- L1-12
- L3-01
- L3-03

### DOWNSTREAM_WATCH

- L1-11
- L2-14
- L3-08
- L3-06
- L3-11

### No review currently justified from this dataset

All other registered nodes.

This is the first bounded KCS change-propagation output.

# 10. Test Result

**CP-001 PASS — PROVISIONAL.**

The dependency dataset produces a finite and explainable review set.

It does not:

- invalidate all downstream systems;
- ignore indirect effects;
- confuse dependency with authority;
- propagate through immaterial relations;
- require a whole-corpus re-audit for every topology edit.

This is evidence that the KCS companion model is operationally usable at small scale.

# 11. Development-Order Consequence

The live records also reproduce the infrastructure chain:

**L1-10 → L1-02 → L1-03 → L1-11.**

Because L1-10 has now been populated by Canonical Topology Register 001, its state should be reconsidered.

The original state was:

**PE / DEV — schema exists; canonical population incomplete.**

After Register 001:

**PE / DEV — initial canonical population exists; validation and dependency population underway.**

This is progress, but not closure.

KDR-001 can now move from a purely prospective relation to an operationally exercised relation.

# 12. State Update Candidates

The following provisional state updates should be considered by the Civil State Map:

**L1-10:** remains PE / DEV, but "population absent" residual is replaced by "initial population requires validation/expansion."

**L1-02:** remains PE / DEV, but live dependency records now exist.

**L1-03:** remains PE / DEV until the State Map consumes these live records rather than relying primarily on narrative/manual dependency statements.

No other maturity state should be upgraded merely because this test passed.

# 13. Next Graph-Selected Action

ODG-001 selected:

1. populate formal topology;
2. instantiate KCS dependency records;
3. populate live State Map;
4. generate Clock queue.

Steps 1 and 2 now have initial operational implementations.

The next selected action is therefore:

> **Update the Civil State Map from the live KCS dependency dataset and produce the first structured queue input.**

This should be performed before selecting a substantive development target.

# 14. Falsification / Retest Conditions

The KCS dependency model remains provisional.

Retest if:

- new source resolution contradicts an edge;
- a direct dependency proves immaterial;
- propagation repeatedly produces irrelevant reviews;
- important downstream effects are missed;
- a new high-consequence dependency is discovered;
- topology IDs or semantics change;
- KCS storage/maintenance burden becomes disproportionate.

# Conclusion

KCS Operational Dependency Dataset 001 completes the second action selected by the first canonical dependency graph.

The Concord now has:

- a 52-node canonical topology register;
- 20 instantiated dependency/interface records;
- explicit materiality and blocking states;
- the first bounded change-propagation result.

The test supports the core KCS rule:

> **A material change should trigger direct review of material dependents and propagate further only where those dependents themselves materially change.**

The next developmental action is now the third step in the frozen chain:

**consume this live dependency state in the Civil State Map and generate the first structured Civilisation Clock queue input.**
