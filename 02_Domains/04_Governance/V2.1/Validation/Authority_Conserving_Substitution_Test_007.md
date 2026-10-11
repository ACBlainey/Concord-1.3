# Authority-Conserving Substitution — Deterministic Test 007

**Scope:** Arithmetic and weight-preservation checks for the proposed PMEDG candidate. Not a test of legal quorum, appointment, jurisdiction or operational security.

| Test | Internal/final positions | Expected | Observed | Result |
|---|---|---|---|---|
| Single substituted position | F/F/A | F | F | PASS |
| Three constituent resultants | F/F/A | F | F | PASS |
| Unresolved substitution | F/U/A | U | U | PASS |
| Two matching with unresolved | F/F/U | F | F | PASS |
| Against majority with unresolved | A/A/U | A | A | PASS |

## Invariants

- One substituted original-level position receives exactly one resultant.
- A three-position internal triad never contributes three original-level positions.
- Nested substitution cannot multiply original-level voting weight.
- F/A/U result semantics apply at each valid triad interface, not to pooled leaves.
- Procedural invalidity is not equivalent to U; an arithmetic outcome alone does not confer legal effect.

## Adversarial tests

**Vote multiplication attempt:** Original P1=A, P3=A, substituted P2 is internal F/F/F. Valid original-level A/F/A→A; invalid flattening A/A/F/F/F→F. The latter violates the one-position substitution rule.

**Recursive multiplication attempt:** Q substitutes P2, and T substitutes Q2. T's three ballots may determine Q2 only; Q determines P2 only. No T ballot directly occupies P1, P3 or an extra original-level seat.

**Invalid appointment:** Q=F/F/F is arithmetically F but cannot be entered as an authorised resultant unless Q was properly appointed and constituted.

**Status:** PASS for deterministic arithmetic and conceptual weight-conservation checks. OPEN for authorisation, quorum, six-Steward mapping, repeated R independence and emergency interfaces. Not graduated.
