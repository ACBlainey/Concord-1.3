# Glass Hammer — Instantaneous Authority Correction 103

**Status:** user-directed architectural correction / source-reconciliation required / not a new canonical definition.

## Correction to stages 100–102

The Concord glass-hammer interpretation states that **authority is not an ongoing resource**. It is available only at the exact time of the particular legitimate decision or authorised act. An office may retain its function, competence, capacity, procedures and eligibility to request authority; these are **not** authority held in reserve. A completed authority exercise does not leave a reusable grant.

The previous stage 100–102 test fixtures used grants with validity windows and revocation semantics. Those may model **eligibility, evidence availability, contextual permission or prerequisite conditions**, but **must not be called continuously held authority**. Stage 102's framing of a 'revocation/commit race' is therefore not a faithful model of the original glass-hammer principle.

## Required distinction

1. **Persistent:** legitimate function, institutional role, competence, technical capability, standing procedures, evidence of prerequisites, and any separately defined obligations.
2. **Event-local:** the determination that a specific decision/act is legitimate **at the instant it is made**. Authority is exercised at that bounded event and is not retained afterward.
3. **Persistent after event:** immutable decision/effect/provenance records, consequences, accountability and any independently legitimate follow-up duties. These are **not** retained authority.
4. **New consequential act:** requires its own authority determination at its own relevant instant; no inheritance from a previous authorised act.

## Implications for ACKS and CBPR

- A delayed ACK, status query or receipt reconciles **what happened**, not whether a previously consumed authority still exists.
- A communication retry must not re-exercise authority. It must query the event/host's actual outcome and preserve uncertain states.
- An action that entails a later independent consequential decision must be authorised at that later decision instant; it cannot borrow authority from the original vote or action.
- If the decision event and material execution event are separate, their authority semantics must be explicitly resolved by the competent owner. Do not silently extend authority between them using a lease.
- A one-use token can represent a **technical replay guard / provenance reference**, not a reservoir of authority.
- Emergency decisions remain event-triggered and independent of a paused Civilisation Clock.

## Required corrections to prior work

- Reclassify 100's temporal evidence as prerequisite/evidence validity, not duration of authority.
- Reclassify 101's owner registry as prerequisite and revocation evidence, not an authority store.
- Reclassify 102's check-then-act demonstration as an **implementation race in evidence/commit sequencing**, not proof that constitutional authority persists between checks.
- Do **not** graduate 100–102 as models of glass-hammer authority until original primary text has been located and source-resolved.
- Do not rewrite CBPR/MKA/BCA canonical or graduated source on the basis of this note alone. Preserve provenance and identify the exact original glass-hammer source.

## Source status

Reviewed in V1.3: `02_Domains/04_Governance/Governance Operating Boundary and Authority Lifecycle — Source Resolution 001.md` and `02_Domains/03_Research/Active_Development/Governance_and_Stewardship/Legitimate Function and the Authority Justification Chain.md`. Both discuss legitimate function, bounded authority and termination, but the precise original glass-hammer wording has **not yet been verified** in those files. This correction records the user's explicit architectural clarification, not a claim that the source was recovered.
