# Glass Hammer — Seventh Digit: Anonymous Committed-Vote Indicator 119

**Status:** authorial clarification of the three-room glass-hammer mechanism. This is a governance integration specification, not a replacement lock or vote-authority system.

## Display semantics

The seventh digit starts at **0** and increases to **1**, **2**, then **3** as each of the three independent Steward positions commits its one-time ballot. It reports **only the aggregate number of committed positions**.

The seventh digit does not reveal the Steward identity, position, ballot choice, reasoning, timing details, or any subsequent concern. In particular, For, Against and Abstain each count as one committed ballot. No display value indicates the arithmetic majority or whether a result has been accepted.

Once committed, a vote remains part of the record. Subsequent concern, challenge or review does not decrement the count or rewrite the vote. A genuine invalidity finding is a separate adjudicated status and historical event; it does not silently erase the original commitment.

## Critical separation: display is not a lock input

**Participation state != Lock state != Voting authority.**

The seventh digit is an informational output only. It is **not part of the combination**, lock validation, lock state machine, case-opening prerequisite, eligibility condition, voting permission, or authority-consumption rule.

If Steward A commits first, the display seen by B and C can advance from 0 to 1. B and C must still be able to open their cases with their original independently valid combinations, even if they have not yet opened them. A vote must not change another Steward's combination, lock state, or ability to exercise their own authority.

The indicator must not form a dependency that delays opening, voting, emergency progression, or bounded acceptance. If the display is unavailable or stale, independent lock operation must continue. An unavailable indicator is not evidence that no one has voted.

## Interface contract

- Vote commit emits a protected, anonymous *count-only* projection for the three Steward rooms.
- The projection reads durable, distinct committed positions; it must not accept an untrusted caller-supplied count.
- A Steward's lock/open/vote authority is checked against its own legitimate owner state, never against the displayed count.
- A Steward may know only how many positions have committed, not who or how they voted.
- Count publication is an information operation governed by existing CWA/CIBB projection controls. Avoid leaking identity or choice through messages, ordering, detailed timestamps, or side channels.
- Third-position eligibility and early contextual acceptance remain separate from this indicator.

## Required adversarial checks

1. A commits while B and C have unopened cases: both combinations still work.
2. Indicator moves 0 -> 1 -> 2 -> 3; a repeated event never increments twice.
3. For, Against and Abstain produce indistinguishable count-only outputs.
4. Concern or review does not decrement the count.
5. Display outage, delay or stale reading never blocks independent case opening or voting.
6. No count-derived decision or authority grant.
7. No inference of *which* Steward committed from the aggregate display itself. Note that a Steward who knows their own vote may infer how many **other** positions have committed, which is the intended minimal awareness.

## Source relationships

- `02_Domains/04_Governance/V2.1/Integration/Glass_Hammer_Immutable_Vote_Concern_and_Independent_Review_115.md`
- `02_Domains/04_Governance/V2.1/Integration/Glass_Hammer_Contextual_Wrapper_Information_Isolation_117.md`
- `02_Domains/04_Governance/V2.1/Integration/Glass_Hammer_CIBB_Owner_Checked_Projection_118.md`
- `04_Portable_Modules/Contextual Wrapper Architecture — Portable Module.md`
- `04_Portable_Modules/Concord Information Black Box Portable Module v1.0.md`

**Non-graduation warning:** A specification does not demonstrate physical lock independence or eliminate traffic-analysis side channels; implementation and adversarial testing remain required.
