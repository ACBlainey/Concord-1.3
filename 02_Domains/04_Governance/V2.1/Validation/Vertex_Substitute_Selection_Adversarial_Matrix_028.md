# Vertex Substitute Selection — Adversarial Validation Matrix 028

**Status:** PROVISIONAL conceptual test specification. Expected outcomes, not evidence of independent blind execution. Candidate under test: Operational Candidate 027.

| ID | Scenario | Expected outcome |
|---|---|---|
| V01 | A1 recused for verified material conflict; five independent eligible alternatives; valid unbiased draw | Select one; bind to A1 position only; no fourth vote |
| V02 | A1 abstains solely for insufficient information | `NOT_A_VACANCY`; seek evidence, no draw |
| V03 | A1 absent but no authorised absence-substitution rule | `AUTHORITY_MISSING`; withhold |
| V04 | Five nominal candidates; two materially conflicted, one already voted elsewhere in same event | Exclude three; uniformly draw from remaining two |
| V05 | All five conflicted or ineligible | `NO_ELIGIBLE_ALTERNATE`; withhold or independently authorised fallback |
| V06 | Exactly one candidate eligible | Do not claim random anti-capture protection; require separate policy for single-candidate appointment |
| V07 | Candidate is valid at draw but loses eligibility before commit | Do not commit; neutral failure procedure only |
| V08 | Convenor repeatedly redraws until preferred Steward appears | Invalid manipulation; prohibit outcome-dependent retries |
| V09 | Conflict is fabricated to remove dissenting A1 | Do not open vacancy; independent finding/challenge required |
| V10 | A2 (same triangle, different vertex) is offered as one of five vertex neighbours | Exclude: not the Steward assigned to the same abstract vertex of another incident triangle |
| V11 | Two candidate records alias the same participant | Deduplicate by real identity, then verify topology and eligibility; no extra lottery weight |
| V12 | Random source has predictable/manipulable seed | `DRAW_INTEGRITY_FAILURE`; withhold |
| V13 | Substitute receives A1's vote and additional independent vote | Reject; one-position authority conservation |
| V14 | Substitute already occupies constituent vote in nested extended triad | `IDENTITY_DUPLICATE`; reject |
| V15 | Five nominal alternatives, quorum requirements unknown | Can prepare diagnostic selection only; consequential commit withheld |
| V16 | Three eligible alternatives, one compromised, fair one-shot draw | Compromised selection probability 1/3, not 1/5 |
| V17 | Original A1 returns and attempts to vote in same event after valid substitute vote | Reject duplicate occupancy; no concurrent original/substitute vote |
| V18 | Adjacent Steward selected solely because geometry connects triangles, with no appointment basis | `AUTHORITY_MISSING`; withhold |
| V19 | Same underlying event renamed to evade prior duplicate-position check | Reject identity reset; decision-event boundary proof required |
| V20 | No eligible alternate, emergency cited without emergency mandate | Withhold; emergency label alone creates no authority |

## Test pass conditions

Each case must state (1) vacancy classification, (2) eligible pool size, (3) authorisation and identity checks, (4) draw permitted/forbidden, (5) one-position vote effect, (6) commit/withhold state, (7) provenance. A correct arithmetic vote tally does not cure invalid procedure.

## Model-level statistical check

For one compromised candidate among `n` equally eligible alternatives and an uncompromised uniform draw, `P(compromised)=1/n`. For `k` compromised, `P=k/n`. This is a mathematical conditional, not a measured real-world capture probability.

## Unresolved normative gates

Minimum eligible pool, single-candidate policy, neutral re-draw on post-selection disqualification, authoritative random source, exact conflict challenge procedure, quorum/denominator, decision-event boundaries. These are deliberately **not** invented by this test.
