# Glass Hammer — Extended Steward Decision Visualisation 107

**Status:** illustrative explanatory analogy supplied by the author; **not** a literal runtime, hardware, voting protocol, cryptographic design, or replacement for source-owned architecture.

## Author's scenario

A Steward sits in a room with an incoming and outgoing conveyor and a display showing a six-digit state-machine code. An incoming locked briefcase holds a uniquely identified binary decision question, a marked Yes / No / Abstain board, a nail bearing the decision identifier and a glass hammer. The eligible Steward's unique key opens the identity lock; the code corresponding to the **current** state opens the contextual lock. The Steward drives the nail into the chosen response; the hammer breaks. The completed case leaves, and the state changes to prevent the same decision being exercised again.

Three independently identified Stewards undertake equivalent decisions, distinguished by a/b/c suffixes, and the three records are later brought together for tallying. Abstention may reflect conflict of interest or insufficient information.

## Architectural interpretation, not literal translation

- Steward key: **eligibility and actor-specific competence/identity**, not permanently held authority.
- Current state code: **context and state precondition**, not an actual six-digit password requirement or a substitute for all rights/consent/necessity guards.
- Two locks: independent prerequisites; neither eligibility nor state alone is sufficient.
- Unique decision ID and Steward suffix: distinct per-Steward ballots associated with one decision; do not confuse three ballot IDs with three independent underlying decision questions.
- Nail and shattered hammer: an **irreversible recorded exercise**; that specific exercise is spent and must not be replayed.
- Outgoing case: durable evidence/provenance, **not transferable authority**.
- State change: a material enabling state is consumed; a new request identifier alone cannot recreate the old circumstances.
- Three rooms: independently produced Steward votes; aggregation is a separate process and must follow the already-established triadic outcome rules, not infer a new majority or abstention rule from the analogy.

## Existing triadic decision boundary

Earlier Governance validation defines three Steward positions P1/P2/P3 and two matching affirmative or negative votes sufficient for a resolved outcome. F/A split or cases without the required matching pair remain unresolved under the applicable rules. **Abstention must not be silently counted as For or Against**. A resolved ballot result is not itself permission to execute an external effect.

## Continuous functions and atomicity

The original BCA section 30A.4 allows bounded continuous functions, without requiring bureaucratic re-authorisation for every trivial movement. The metaphor explains **particular consequential decisions**; it does not mean every physical movement needs a new glass hammer. For executable software, the anti-replay guarantee requires a genuinely guarded state transition and durable event identity, with an atomic decision-state boundary where feasible. This implementation requirement is an inference, not an instruction to build literal briefcases, keys, glass objects or six-digit state codes.

## Source relationship

- User-provided `Extended glass hammer visualisation.txt`, 12 October 2026, explanatory analogy.
- V1.2 original `08_Active_Development/01_DEVELOPMENT_NOTES/04_GOVERNANCE_AND_STEWARDSHIP/Bounded Contextual Authority — Functional Authority, Inherent Sunset and General Operational Design.md`, section 30A.
- V1.2a `V1.2a/06_Topology_and_Formalisation/Civilisation Clock Extension 001 — Consequence-Relevant State Transition Layer.md`: transition history/relations only, not authority issuer.
- V1.3 `02_Domains/04_Governance/V2.1/Integration/Glass_Hammer_V12a_Crosscheck_106.md`.

**Scope guard:** preserve the analogy as a teaching aid and source of validation scenarios; do not promote its props, vote enumeration or operational sequencing as a canonical technical specification.
