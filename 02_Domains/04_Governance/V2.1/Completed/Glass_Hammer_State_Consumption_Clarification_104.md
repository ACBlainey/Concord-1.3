# Glass Hammer — State-Conditioned, Single-Use Authority 104

**Status:** user-directed clarification to correction 103; implementation/source reconciliation required.

## Core rule

Authority is **not a continuing grant, stored balance, renewable lease, or standing permission**. The exact situation context, including the relevant state-machine state, determines whether a particular authority may be exercised **at the decision/act event**. A successful exercise **consumes that authority and changes the state**. Re-presenting the same context/evidence or invoking the same office cannot repeat that authority exercise because the prior enabling state no longer exists.

The persistent elements are the legitimate function, capacity, office, procedures and prerequisite evidence; none of them constitute possessed authority. A subsequent consequential act must satisfy the authority conditions of its own state transition, not inherit authority from the previous one.

## State transition contract

For a given event identity E and action A:

- Verify the authoritative current state S and all context guards for A, including any independently required consent, rights, scope, necessity, and relevant safeguards.
- Permit only the defined transition S --(E,A)--> S'. No generic authority token is minted.
- Commit a durable, immutable event record and the new state as **one atomic state-machine transaction**. Once S' is committed, replay of E or A against S must not succeed.
- Distinguish duplicate requests for E (return prior outcome, no new transition) from new event identities that lack a fresh legitimate enabling state (reject). Merely choosing a new event ID must not recreate authority.
- If an external host effect is involved, the local state transition cannot by itself guarantee an atomic physical consequence. The host must reconcile actual effect identity and unknown-commit outcomes; do not blindly replay. Document the external boundary rather than claiming distributed atomicity.
- An ACK is evidence of receipt or reconciliation, not authority or a new enabling state.

## Abuse, capture and failure modes obstructed

- **Replay and duplicate invocation:** prior state consumed.
- **Privilege accumulation:** no stockpile of reusable authority.
- **Role capture:** office/technical capability alone does not provide an active authority.
- **Context laundering:** previously valid circumstances cannot be silently applied after state change.
- **Stale evidence and authority inheritance:** fresh context guards must hold for each new consequential transition.
- **Concurrency:** compare-and-transition must be atomic so competing invocations cannot both consume the same enabling state.
- **Emergency power persistence:** emergency authority is bounded to its event and state transition, not a standing emergency office power.

These are intended safety properties, not yet demonstrated as complete for a production deployment.

## Correction to earlier stages

Stages 100–101 model validity windows and revocable prerequisite evidence, not a continuously valid authority resource. Stage 102 demonstrates an evidence-check/effect race, but **the primary authority mechanism is state-conditioned consumption**, not an authority lease. The proposed one-use lease/commit-fence must not be promoted as Concord's authority model. Stage 103's 'authority at exact decision/act' remains correct but incomplete without **mandatory state change and non-repeatability**.

## Follow-up executable validation

Implement an atomic compare-and-transition journal, test concurrency, replay with same and different IDs, stale state, failed guard, restart durability, and external-effect uncertainty. Keep owner boundaries with CBPR, MKA, BTA, G05 and the state-machine architecture. Original legacy glass-hammer text still requires recovery; this note preserves the user's explicit clarification without falsely attributing it to a located historical file.
