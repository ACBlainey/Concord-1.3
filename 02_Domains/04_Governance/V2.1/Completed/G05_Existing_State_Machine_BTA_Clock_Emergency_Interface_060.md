# G-05 — Existing State-Machine Interface: Emergency, Civilisation Clock and BTA 060

**Basis:** authorial direction to reuse Concord's existing state machines; migration-aware recovery rule 056. This document is a source crosswalk, not a new transition engine.

## Recovered sources

- `03_Cross_Domain_Architecture/Civilisational_Developmental_Topology/Civilisation Clock Companion Extension 001 - State Functional and Compound Trigger Architecture.md`: clock is state-transition scheduling and review-trigger architecture, not a periodic timer; chronological, state, dependency, event, risk and evidence triggers.
- `03_Cross_Domain_Architecture/Civilisational_Developmental_Topology/Civilisation Clock Extension 001 — Consequence-Relevant State Transition Layer.md`: clock cycles and civil transitions differ; legitimate transitions may be concurrent, divergent or partially observable.
- `04_Portable_Modules/Bounded Transition Architecture — Portable Module v1.0.md`: graduated grammar for asynchronous consequential transitions; coordination without taking ownership of state semantics.
- `02_Domains/03_Research/Development_Archive/Portable_Modules/Bounded_Transition_Architecture/03_Pre_PMEDG_Testing/BTA Clean Cross-Domain Test 002 — Constitutional Emergency State Transitions.md`: PASS across emergency activation, escalation, de-escalation, recovery, invalidated actions and restoration.
- `03_Cross_Domain_Architecture/Constitutional_Emergency/Constitutional Emergency V2.md`: owns legitimacy, power activation, expiry and restoration.
- Governance G-05 059: variable Civilisational Clock may pause; emergency operational time cannot depend on its advancement.

## Recovered architecture, not invented replacement

**Owner states:** Constitutional Emergency, Governance, Rights, Judiciary and other domain systems determine their own valid states and authorities.

**Transition coordination:** BTA preserves bounded transition identities, prerequisite references, independently changing dimensions, unresolved states, non-propagation rules and surviving duties. BTA does not decide emergency legitimacy or force synchronisation.

**Clock interface:** the Civilisation Clock represents scheduling/dependencies and compound review triggers. It may pause. Independently authorised emergency transitions proceed through their own operational timing and are represented as consequential state changes, without requiring the Clock to advance.

**Resumption:** pending clock-governed actions compare their recorded prerequisites to current owner-system states. Materially changed prerequisites are routed through existing BTA dependency, unresolved-state and review interfaces; an old vote is not rewritten and a clock transition does not validate an obsolete implementation.

## Existing tested non-propagation invariants

- Emergency classification change does not automatically activate powers.
- Emergency authority termination does not terminate continuing review, remedy or recovery duties.
- De-escalation does not instantly terminate every emergency-related function.
- Termination of a restriction does not prove restoration of the previous world state.
- Transition coherence does not require synchronous completion.
- An invalidated emergency activation still has a consequential history.
- BTA integration does not guarantee every relevant dimension was represented; retain ESCP boundary.

## Paused-clock scenario

1. A valid ordinary decision is queued on a clock dependency.
2. Clock waits for feedback; an emergency arises.
3. Constitutional Emergency independently validates and activates an authorised response; BTA records changes in each affected owner system.
4. Emergency powers sunset independently while recovery obligations may remain pending.
5. When the clock dependency becomes eligible, current prerequisites are checked. Valid actions proceed; materially inconsistent actions remain unresolved for the proper owner-system review or remedy.
6. The clock need not be forced forward, and emergency power is not invented by state coordination.

## Remaining targeted validation

Run a combined scenario with a paused Clock, emergency response, an expired emergency power, an outstanding ordinary decision and asynchronous GTP recovery. Verify owner-state independence, no authority propagation, and no stale execution. Do not duplicate BTA as a Governance-specific module.
