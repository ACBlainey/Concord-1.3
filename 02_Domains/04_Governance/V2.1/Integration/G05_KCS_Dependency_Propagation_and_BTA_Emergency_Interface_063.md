# G-05 — Existing KCS Dependency Propagation for Emergency/Clock Transitions 063

**Status:** source-recovery integration candidate. No new state machine or governance authority proposed.

## Additional recovered existing architecture

The Concord Knowledge Control System (KCS) already has an **Operational Dependency and Change-Propagation Architecture** at:
`03_Cross_Domain_Architecture/Knowledge_Control_System/KCS Companion Upgrade 001 — Operational Dependency and Change-Propagation Architecture.md`.

Its function is to preserve material relationships between upstream changes and downstream assumptions requiring reconsideration. It is an appropriate existing interface for the stale-decision concern exposed by paused-clock emergency scenario 061 and adversarial audit 062.

Other established owners:
- Constitutional Emergency V2: legitimacy, activation, sunset and restoration.
- Civilisation Clock companion/transition extensions: state, event, dependency and risk-triggered scheduling; consequence-relevant transition relations.
- BTA Portable Module v1.0: independently owned, asynchronous consequential state changes, pending/failed transitions and non-propagation.
- SMM Portable Module v1.0: represented developmental state, maturity, sufficiency and uncertainty; self-model is not reality.
- Governance GTP: overlapping spatial coordination, not a hierarchy.

## Interface crosswalk

1. **Emergency owner transition:** independent operational-time emergency action changes a specific owner-system state; BTA records transition identity, authority reference, scope and affected dimensions.
2. **Material dependency identification:** KCS change-propagation interface identifies downstream assumptions, queued decisions and procedures that materially depend on changed upstream states. Mere adjacency or shared clock membership does not imply dependency.
3. **Pending work:** Civilisation Clock may remain paused. Its queued tasks preserve dependencies and do not become automatically effective merely because an unrelated event occurred.
4. **Reassessment:** on resumption or relevant event trigger, affected downstream prerequisites are rechecked with the competent owner. SMM can describe uncertain capability/maturity but cannot itself authorise an action.
5. **Execution:** valid existing authority and current prerequisites permit lawful implementation. A material unresolved conflict is routed to the proper owner-system review/remedy path, not decided by KCS or BTA.
6. **History:** previous decisions, emergency action, supersession and remedy remain traceable; neither an expired emergency power nor a stale state is silently revived.

## Separation of responsibilities

**KCS identifies what may need reconsideration; BTA represents how consequential state dimensions changed; the Civilisation Clock schedules or wakes relevant work; the owning domains decide what is lawful and true.** No one interface becomes sovereign over the others.

## Adversarial implications

- **Stale feedback:** require material dependency/version evidence before treating delayed feedback as satisfying a current prerequisite.
- **Expiry under isolation:** independent emergency timing and authority remain owner concerns, not KCS clock triggers.
- **Cross-area conflict:** KCS may identify linked resources; it cannot create a GTP shared mandate.
- **Duplicate execution:** BTA identity and dependency provenance support detection, but implementation-level idempotency remains unverified.
- **Missing dependency:** KCS representation is fallible; an omitted dependency may still cause harm. Maintain ESCP and domain-owner review boundaries.

## Validation status

**Source-grounded interface identification, not implementation validation.** No claim that KCS automatically propagates emergency events today, or that all dependency links are complete. Next targeted test: inject an emergency owner-state change while the Clock is paused; verify KCS flags an actually dependent queued decision without flagging an unrelated one, and that BTA preserves independent expiry and recovery state.

Sources: KCS Companion Upgrade 001; BTA v1.0; SMM v1.0; Civilisation Clock extensions; Constitutional Emergency V2; Governance G-05 059–062.
