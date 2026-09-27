# State Map 001B — Concord Current-State Synthesis Layer — Candidate Architecture

**Status:** V1.2a CANDIDATE ARCHITECTURE  
**Date:** September 2026  
**External knowledge state:** INTERNAL ONLY  
**Canonical effect:** NONE  
**Parent:** State Map 001A — Frozen Minimum Schema and Boundary Requirements

# 1. Purpose

The **Concord Current-State Synthesis Layer (CCSSL)** is the minimum candidate architecture for the previously defined Concord State Map.

It does not create the underlying facts it represents.

It synthesises bounded, provenance-aware state claims from legitimate upstream systems into a reusable current architectural view.

Its central function is:

> provide a corrigible representation of what civil architecture currently exists, what it can presently do, what remains unresolved, what it depends upon, what depends upon it, how confidently that state is known, and what materially changed since an earlier state.

# 2. Architectural Position

Inputs may include:

KCS/KMDI knowledge and dependency state
+ Clock/CRSTL temporal state
+ maturity/readiness observations
+ system/interface inventories
+ validation/confidence state
+ domain-owned open questions and review states

→ **CCSSL**

→ bounded current-state views for:

- Civilisation Clock;
- Priority / Dependency Architecture;
- Induction;
- Developmental Topology;
- Temporal Review / Development Health;
- other legitimate consumers.

CCSSL is therefore a synthesis layer between state-producing systems and state-consuming systems.

# 3. Core Object — Civil Architecture State Record (CASR)

Each represented architectural unit may have a CASR.

Minimum fields:

- CASR ID;
- architectural unit ID/name;
- unit type;
- legitimate owner/domain where known;
- purpose/function;
- maturity vector/state;
- established capabilities;
- unresolved capabilities/questions;
- upstream dependencies/blockers;
- downstream dependents;
- interface state;
- validation/evidence state;
- provenance references;
- uncertainty/dispute state;
- last material review;
- Clock/transition reference;
- correction/supersession history;
- disclosure/access class.

The CASR is a representation of state, not the state itself.

# 4. State Claim Separation

A CASR must separate different kinds of claim.

Examples:

**Existence claim:** system/document/capability exists.

**Capability claim:** a specified function is architecturally established.

**Maturity claim:** applicable relations have reached a specified developmental state.

**Validation claim:** specified testing/evidence exists.

**Dependency claim:** material dependency is recorded.

**Open-state claim:** a question, residual or capability remains unresolved.

**Temporal claim:** this was the represented state at Clock/state reference T.

These claims must not collapse into one scalar “completion” value.

# 5. Maturity Representation

CCSSL reuses the multidimensional maturity principle already supported by V1.2a.

Maturity should be represented as a vector or structured profile where applicable.

A unit can therefore be:

- functionally developed;
- weakly integrated;
- strongly corrigible;
- empirically unvalidated;
- mature in rights safeguards;
- immature in implementation.

This prevents:

LargeDocument = MatureSystem

or:

OldSystem = ImmatureSystem.

# 6. Capability State

Capabilities may be represented as:

- ESTABLISHED;
- PARTIAL;
- CANDIDATE;
- UNRESOLVED;
- NOT APPLICABLE;
- UNKNOWN.

Where useful, each state should point to supporting provenance.

“Unknown” and “not found” remain distinct.

# 7. Dependency State

CCSSL does not independently invent dependency edges.

It consumes KMDI/domain dependency claims and can expose:

- satisfied prerequisite;
- unsatisfied prerequisite;
- developmental dependency;
- interface dependency;
- uncertain/disputed dependency;
- known downstream exposure.

The State Map may display a blocker.

It does not decide that the blocker is true merely because an edge exists.

# 8. Interface State

Internal maturity and interface maturity are represented separately.

Example:

System A: internally mature.
A↔B interface: partial.

This prevents a mature system from being misclassified because another system has not yet integrated with it.

Possible interface states:

- ESTABLISHED;
- PARTIAL;
- PROPOSED;
- BROKEN;
- STALE;
- UNKNOWN;
- NOT APPLICABLE.

# 9. Validation State

A capability may exist architecturally without empirical validation.

CASR therefore distinguishes:

ArchitectureState
from
ValidationState.

Candidate validation states may include:

- source-grounded;
- internally audited;
- adversarially audited;
- simulation tested;
- experimentally tested;
- externally evaluated;
- operationally observed;
- unresolved.

These labels are descriptive and may coexist.

# 10. Temporal State and Snapshots

CCSSL interfaces with the Clock.

At meaningful transitions:

StateMap(T0)
→ civil/development activity
→ Clock transition
→ StateMap(T1).

The system need not duplicate every unchanged record.

A snapshot may consist of:

- prior state reference;
- changed CASRs;
- newly created units;
- retired/superseded units;
- changed dependencies;
- changed unresolved questions;
- changed validation state.

Historical state remains reconstructable through provenance.

# 11. Material State Change Event

A material State Map change occurs when a represented property changes sufficiently to matter to a legitimate consumer.

Examples:

- capability becomes established;
- dependency becomes unsatisfied;
- interface fails;
- validation result changes;
- open question closes;
- correction invalidates a prior assumption;
- system ownership changes;
- a new downstream dependency is verified.

A spelling edit is not automatically a civil state transition.

# 12. Staleness

Every consequential state record must permit staleness to be visible.

A record may be:

- CURRENT WITHIN REVIEW WINDOW;
- REVIEW DUE;
- STALE;
- UNKNOWN FRESHNESS.

No stale record should silently present itself as current fact.

Review windows may be domain-specific.

# 13. Contestation and Correction

CASR state claims are contestable.

Challenge
→ provenance review
→ domain/independent review as appropriate
→ confirm / amend / dispute / supersede.

Correction creates a new state transition.

It does not erase the prior represented state.

# 14. Bounded Views

CCSSL should support task-specific views rather than universal disclosure.

Examples:

## Clock View
Current unresolved blockers, development transitions, dependencies, review-due states.

## Induction View
Current architecture, capabilities, known uncertainties, relevant dependencies and active questions appropriate to the participant/task.

## Topology View
Maturity vectors, interfaces, dependency edges, residuals and validation state.

## Continuity View
Capabilities and prerequisites necessary to restore a function.

## Public View
Only information legitimately public and necessary for broad civil understanding.

A view is a projection of the State Map, not a separate truth.

# 15. Missing-State Humility

The State Map must be capable of saying:

- represented and established;
- represented and unresolved;
- represented but disputed;
- not represented;
- search/review incomplete;
- unknown.

Therefore:

NoCASR(X) != XDoesNotExist.

NoRecordedGap(X) != NoGap(X).

NoRecordedDependency(A,B) != NoDependency(A,B).

# 16. Healthy Recursive Cycles

CCSSL permits cycles such as:

StateMap(T)
→ Clock decision/cycle
→ development
→ new knowledge
→ KMDI update
→ StateMap(T+1).

A cycle is classified as problematic only when it creates illegitimate authority, logical impossibility, unresolvable dependence, or uncontrolled failure propagation.

Feedback itself is not a defect.

# 17. State Map Self-Representation

CCSSL must contain a CASR for itself.

That record includes:

- schema/version;
- upstream data dependencies;
- review method;
- known blind spots;
- unresolved coverage;
- last review;
- correction history.

Thus the map cannot exempt itself from the rules it applies to other systems.

# 18. Minimal Machine-Readable Form

Conceptually:

{
  unit_id,
  unit_type,
  owner,
  purpose,
  maturity,
  capabilities,
  unresolved,
  upstream_dependencies,
  downstream_dependents,
  interfaces,
  validation,
  provenance,
  uncertainty,
  last_review,
  clock_state,
  history,
  disclosure
}

This is a conceptual schema, not a frozen technical encoding.

# 19. SM1–SM22 Check

SM1 unit identity — SATISFIED.
SM2 owner/domain — SATISFIED.
SM3 multidimensional maturity — SATISFIED.
SM4 capabilities — SATISFIED.
SM5 unresolved state — SATISFIED.
SM6 upstream blockers — SATISFIED.
SM7 downstream dependents — SATISFIED.
SM8 interface state — SATISFIED.
SM9 validation/evidence — SATISFIED.
SM10 provenance — SATISFIED.
SM11 uncertainty/dispute — SATISFIED.
SM12 last review — SATISFIED.
SM13 Clock interface — SATISFIED.
SM14 KCS/KMDI interface — SATISFIED.
SM15 historical comparison — SATISFIED.
SM16 staleness — SATISFIED.
SM17 bounded retrieval — SATISFIED.
SM18 missing vs negative — SATISFIED.
SM19 healthy recursion — SATISFIED.
SM20 human/machine representation — SATISFIED architecturally.
SM21 correction/contestation — SATISFIED.
SM22 partial-map humility — SATISFIED.

# 20. Boundary Check

B1–B10 are preserved.

In particular:

State Map != Governance.

State Map != KCS.

State Map != Clock.

State Map != Priority Authority.

State Map != Complete Reality.

# 21. Residual Questions

CCSSL-R1 — How are domain-specific maturity dimensions registered without uncontrolled schema growth?

CCSSL-R2 — What determines review windows/staleness by domain?

CCSSL-R3 — How should conflicting owner/domain state claims be displayed and reconciled?

CCSSL-R4 — What is the minimum useful snapshot frequency for different functions?

CCSSL-R5 — How should sensitive dependency topology be represented in public versus restricted views?

CCSSL-R6 — How should automated state extraction be validated against source reality?

These remain development questions, not new system claims.

# 22. Candidate Status

The minimum architecture satisfies the frozen State Map requirements at conceptual level.

It should now be tested against P-SM1–P-SM6 without altering those predictions.
