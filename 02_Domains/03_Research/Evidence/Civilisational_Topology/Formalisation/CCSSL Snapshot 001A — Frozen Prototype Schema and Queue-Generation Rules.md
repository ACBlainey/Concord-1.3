# CCSSL Snapshot 001A — Frozen Prototype Schema and Queue-Generation Rules

**Status:** V1.2a OPERATIONAL PROTOTYPE PRE-REGISTRATION  
**Date:** September 2026  
**Canonical effect:** NONE  
**External knowledge state:** INTERNAL ONLY

# 1. Purpose

Before populating the first operational State Map snapshot, freeze how the snapshot may generate a development queue.

This prevents the queue from being retrofitted to whichever candidate later appears interesting.

# 2. Prototype Scope

The first snapshot will represent a bounded set of civil systems already reviewed in the dependency experiments.

It is not a whole-Concord map.

Absence from the snapshot has no negative implication.

# 3. Required Fields Per Unit

- Unit ID;
- unit name/type;
- broad maturity state;
- established capabilities;
- unresolved capabilities;
- upstream dependencies;
- downstream dependents;
- interface state;
- validation state;
- provenance/source basis;
- freshness/review state;
- uncertainty.

# 4. Queue Candidate Conditions

A unit may enter the development queue when at least one of these holds:

Q1 — a downstream system is blocked by an unresolved capability legitimately owned by the unit;

Q2 — multiple downstream consumers require the same immature capability;

Q3 — an interface deficit prevents an otherwise available capability from propagating;

Q4 — state synthesis is missing between existing producers and consumers;

Q5 — a material dependency is stale/unknown enough that downstream development cannot be responsibly resolved;

Q6 — a previously developed upstream capability creates a newly visible unresolved requirement.

# 5. Queue Exclusions

Do not queue merely because:

- a document is old;
- a document is short;
- a system has few recorded capabilities;
- a system has many dependencies;
- a system is highly central;
- a maturity dimension is legitimately N/A;
- an interesting speculative extension is possible.

# 6. Ordering Rules

No universal numerical score is used.

Queue ordering should consider:

1. hard blocking before enhancement where other factors are comparable;
2. shared upstream bottlenecks before repeated local patches;
3. rights/safety/continuity criticality;
4. number and materiality of affected downstream functions;
5. reversibility of delay;
6. confidence that ownership is correct;
7. whether an existing solution can be reused;
8. feasibility and boundedness of the next development step.

Centrality alone must not determine order.

# 7. Mandatory Source-Resolution Gate

Every queued candidate must undergo source resolution before development.

Allowed outcomes:

- REUSE EXISTING;
- INTERFACE/INTEGRATION;
- DEVELOP EXISTING OWNER;
- HOLD / INSUFFICIENT EVIDENCE;
- INVENTION FRONTIER CANDIDATE;
- FALSE POSITIVE.

# 8. Queue Freeze

Once Snapshot 001B generates its ordered candidate set, that queue must be committed before focused source inspection of those candidates.

Subsequent changes require explicit provenance.

# 9. Evaluation

After source resolution, record:

- number of candidates;
- confirmed developmental bottlenecks;
- reuse/integration cases;
- false positives;
- holds;
- invention candidates;
- newly discovered dependencies;
- predicted downstream effects.

# 10. Success Criterion

The prototype is useful if the frozen snapshot/queue produces non-trivial, source-resolvable development guidance without simply selecting the largest, oldest or most connected system.

The prototype is weakened if queue candidates mostly collapse as artefacts of incomplete mapping or arbitrary maturity judgement.
