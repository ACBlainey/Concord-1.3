# Glass Hammer — Seventh Digit Operational Fixture 120

**Status:** test-only implementation of Stage 119; not an electronic/physical lock or deployed access-control system.

## Implemented

`SeventhDigitDecision` reads the count of distinct committed ballot positions from both the regular and late-ballot tables. Its read-only projection returns only `{status,digit}`; it does not expose the ballot choice, Steward identity, position or majority determination. Duplicate event replay and repeated Steward submissions cannot inflate the count.

`IndependentCaseLock` is an independent toy combination-lock state machine. It has no reference to the vote database or indicator. It accepts a Steward's own correct combination even after another Steward votes or an early contextual result is accepted. The indicator's outage does not block opening or voting.

A Steward may know the aggregate count 0–3; the indicator is **not** a component of the combination, an input to lock opening, or an authority source. Its state is derived from durable commitments, not caller input. Concerns do not decrement the count.

## Limitations

The lock is deliberately a toy independent state machine; the tests establish software separation of dependencies, not physical tamper resistance or hardware behaviour. The display has no trusted owner-issued projection grant; Stage 118 provides the candidate grant boundary but is not yet connected here. Real-time indicator propagation, stale-data handling, privacy of event timing, authenticated identity and true nested-triad counting remain unimplemented. Stage 110's early-acceptance input remains a fixture-level contextual assertion.
