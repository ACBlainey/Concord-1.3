# Glass Hammer — V1.2 Primary Source Recovery 105

**Status:** historical source recovered; interpretation and migration crosswalk; preserve original source qualification.

## Exact historical source

Repository: `ACBlainey/Concord-1.2`

`08_Active_Development/01_DEVELOPMENT_NOTES/04_GOVERNANCE_AND_STEWARDSHIP/Bounded Contextual Authority — Functional Authority, Inherent Sunset and General Operational Design.md`

Original document identifies itself as Concord V1.1, 11 September 2026, review copy / active development / candidate general architectural principle / not canonical. **Section 30A, lines 2067–2320**, directly defines the locked-case / glass-hammer model.

### Recovered source statements

- Case does not open merely because of office, credentials, prior authority, or future need (lines 2069–2087).
- Context, legitimate function, functional need, conditions and minimum proportionate scope open the case (2075–2085).
- Once the act is performed, that particular hammer is consumed; past authority is not a reusable token (2091–2113).
- The act changes context C0 to C1. Any A2 requires fresh justification against C1, not inheritance from A1 (2115–2172).
- **A specific exercise can be consumed while the broader function continues** (2174–2198).
- Standing eligibility, contextual activation, bounded exercise, consumption/termination, changed context and re-justification are separate phases (2200–2223).
- **Important qualification:** section 30A.4 (2225–2250) says some legitimate functions have a *continuing bounded authority envelope* across a period and need not demand bureaucratic re-authorisation after every trivial movement. Individual actions inside that genuinely justified envelope are distinguished from new/materially different acts requiring fresh justification. This is a historical nuance; do not silently erase it while implementing the user's stronger state-consumption clarification.
- Historical records preserve **evidence of authority**, not authority itself (2252–2276).

Companion adversarial source:
`08_Active_Development/01_DEVELOPMENT_NOTES/04_GOVERNANCE_AND_STEWARDSHIP/Bounded Contextual Authority — Adversarial Attack and Falsification Audit.md`

Its early attacks identify self-declared functions, mission inflation, permanent strategic necessity and self-declared emergency as capture routes. The audit also distinguishes standing eligibility from activated authority, duties from permission, and technical capability from civil authority.

## Resolution for Governance 103–104

The recovered primary text **strongly supports** one-use *specific exercises*, context changes, non-inheritance and non-replay. Stage 104's atomic compare-and-transition is a proposed executable implementation of these principles, **not an assertion that the 2026 source itself prescribed SQLite or atomic compare-and-swap**.

The primary text is **more nuanced** than the unqualified claim that every micro-action has zero duration: a legitimate continuous function may have a bounded authority envelope. Governance must distinguish:
1. a single materially consequential exercise that consumes its enabling authority;
2. a continuous bounded function with explicit, limited permitted acts;
3. a new materially distinct exercise requiring fresh context justification.

Do not equate a continuous function/envelope with unlimited reusable authority or standing institutional power. The user's current instruction emphasises state-machine transitions and exhaustion after use. The exact mapping of continuous envelopes to state-machine transitions needs explicit source-sensitive resolution, not silent replacement.

## Source location limitation

The `ACBlainey/Concord-1.2` main tree contains `V1.2a/` but **no folder literally named `v1.21`**, based on recursive tree inspection (3414 entries, not truncated). If `v1.21` denotes a local archive folder, other branch or differently named snapshot, that exact source has not been reviewed here. Do not misrepresent `V1.2a` as `v1.21`.

## Follow-up

- Recover the precise `v1.21` folder if available.
- Examine section 30A.4 continuous-envelope qualification against the user's state-transition rule and distinguish micro-actions from material authority-consuming decisions.
- Implement and validate guarded, one-time state transitions without minting ongoing authority tokens.
- Audit existing Governance stages 100–102 for misleading labels; their passing checks prove prerequisite-evidence logic, not constitutional authority.
