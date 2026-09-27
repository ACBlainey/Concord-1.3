# KMDI-001C — Downstream Prediction Retest and Second Upstream-Bottleneck Replication

**Status:** V1.2a POST-DEVELOPMENT RETEST  
**Date:** September 2026  
**Canonical effect:** NONE  
**External knowledge state:** INTERNAL ONLY  
**Candidate:** KCS Material Dependency Index (KMDI)

# 1. Method

Before KMDI design, eight downstream predictions were frozen.

This document tests whether the minimum KMDI architecture actually supplies a relevant capability to each predicted dependent.

The test is architectural, not empirical implementation validation.

# 2. P1 — Civilisation Clock

Prediction: improve prerequisite/development ordering.

KMDI provides:

- recorded prerequisites;
- developmental dependencies;
- broken/unsatisfied dependency state;
- upstream blockers;
- downstream dependents;
- change/review triggers.

The Clock can use these as inputs to its existing dependency-aware priority and state-transition process.

**Result: SUPPORTED.**

Important boundary: KMDI does not choose the priority.

# 3. P2 — Bounded Correction Propagation

Prediction: identify downstream objects requiring review without indiscriminate re-audit.

KMDI explicitly supports:

Upstream Correction
→ material dependency traversal
→ downstream review candidate
→ domain materiality decision
→ bounded further propagation.

This operationalises the existing Metrics correction grammar at cross-system level.

**Result: SUPPORTED ARCHITECTURALLY.**

# 4. P3 — State Map

Prediction: add explanatory dependency state.

A system can now be represented as:

maturity/state
+ unresolved prerequisites
+ upstream blockers
+ downstream dependents
+ review state.

This distinguishes:

“System immature”

from:

“System cannot advance because capability X in system Y is unresolved.”

**Result: SUPPORTED.**

# 5. P4 — Induction

Prediction: permit bounded dependency-relevant knowledge packages.

Task
→ relevant object
→ prerequisite traversal
→ KCS retrieval.

This is directly compatible with KCS's existing retrieve-what-is-relevant principle.

**Result: SUPPORTED ARCHITECTURALLY.**

Residual: practical retrieval ranking remains undeveloped.

# 6. P5 — Continuity

Prediction: identify minimum functional restoration dependency sets.

KMDI can traverse material continuity dependencies for a function and produce a candidate prerequisite set.

Because missing edges remain possible, the result must be labelled incomplete/conditional rather than a proof of sufficiency.

**Result: SUPPORTED WITH ESCP LIMITATION.**

# 7. P6 — Emergency

Prediction: query known dependency chains and critical nodes.

Emergency architecture already requires dependency mapping.

KMDI can provide pre-existing, provenance-visible dependency knowledge and expose stale/uncertain edges.

This can reduce rediscovery during crisis.

**Result: SUPPORTED ARCHITECTURALLY.**

Boundary: emergency decisions and authority remain outside KMDI.

# 8. P7 — Resource Steering

Prediction: expose structural/evidence assumptions and route affected models for review after upstream change.

KMDI can index model dependencies and generate review triggers.

**Result: SUPPORTED ARCHITECTURALLY.**

Boundary: KMDI cannot determine allocation.

# 9. P8 — Developmental Topology

Prediction: reduce repeated manual rediscovery.

The present experiment itself repeatedly had to search the corpus to reconstruct dependencies.

A maintained KMDI would preserve validated dependency edges, their provenance and state for reuse in later topology passes.

**Result: SUPPORTED IN PRINCIPLE; EMPIRICAL EFFICIENCY NOT YET MEASURED.**

# 10. Prediction Summary

P1 Clock — SUPPORTED
P2 Correction propagation — SUPPORTED ARCHITECTURALLY
P3 State Map — SUPPORTED
P4 Induction — SUPPORTED ARCHITECTURALLY
P5 Continuity — SUPPORTED WITH ESCP LIMITATION
P6 Emergency — SUPPORTED ARCHITECTURALLY
P7 Resource steering — SUPPORTED ARCHITECTURALLY
P8 Topology reuse — SUPPORTED IN PRINCIPLE / NOT YET EMPIRICALLY MEASURED

No frozen prediction was contradicted at architectural analysis level.

# 11. Second Replication Result

The Clock demonstration showed:

Downstream gap
→ immature upstream owner
→ upstream extension
→ downstream gap closure.

The KCS demonstration shows a related but distinct pattern:

Multiple downstream information needs
→ existing upstream owner
→ distributed solution fragments already present
→ missing integration maturity
→ minimal upstream integration layer
→ multiple downstream capabilities improve.

Thus the upstream-bottleneck model has now survived a second case with a different failure mode.

# 12. Two Bottleneck Classes Now Observed

## Type A — Functional Maturity Bottleneck

Owner exists but lacks a newly required function.

Observed case:
**Civilisation Clock / CRSTL.**

## Type B — Integration Maturity Bottleneck

Owner and solution components exist, but they are not integrated into a reusable upstream capability.

Observed case:
**KCS / KMDI.**

This distinction should be preserved in the maturity map.

# 13. Development-Order Implication

A development planner should therefore ask not only:

“Which system is least mature?”

but:

1. Which downstream requirements are blocked?
2. Do several share an owner?
3. Is the owner missing a function or merely an integration?
4. Can one upstream development satisfy several dependents?
5. What rights/safety/continuity criticality modifies priority?
6. What downstream effects can be predicted before development?

# 14. Remaining Falsification Work

This is still architecture-level evidence.

Stronger validation requires:

- populate a small real KMDI slice from existing V1.2 systems;
- use it prospectively to predict a development bottleneck not chosen manually;
- perform that development;
- measure whether predicted downstream gaps actually change;
- compare against a baseline manual audit;
- adversarially test stale/missing/incorrect dependency edges.

# 15. Conclusion

**SECOND UPSTREAM-BOTTLENECK REPLICATION: SUPPORTED AT ARCHITECTURAL LEVEL.**

The evidence now supports a broader provisional proposition:

> Uneven civilisational development can be diagnosed through dependency topology, and development effort can sometimes be ordered more efficiently by maturing shared upstream capabilities before patching multiple downstream systems independently.

The proposition remains falsifiable and should now move from hand-constructed examples toward a populated dependency graph and prospective prediction.
