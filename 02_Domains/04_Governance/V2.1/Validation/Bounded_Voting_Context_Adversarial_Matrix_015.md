# Bounded Voting Context — Validation Matrix 015

**Status:** Specification-derived adversarial cases; not executed blind transfer or constitutional adoption.

| ID | Input condition | Required BVC outcome | Invariant |
|---|---|---|---|
| B01 | Three distinct, eligible positions vote F/F/A with valid forum and quorum | COMMITTED F | Ordinary majority |
| B02 | Three distinct, eligible positions vote F/A/abstain with valid quorum | UNRESOLVED_SUBSTANTIVE | Abstention != Against |
| B03 | Same Steward occupies A3 and B3 within one decision | WITHHELD_DUPLICATE_HOLDER | Injective holder mapping |
| B04 | Same originating Steward fills R_A, R_B and R_C | WITHHELD_DUPLICATE_HOLDER | Origin-included prohibition |
| B05 | Constituent A F/F/A, B F/F/A, C A/A/A | COMMITTED F if all gates pass | Three resultants, no pooling |
| B06 | Internal F/F/F but no lawful substitute appointment | WITHHELD_INVALID_BASIS | Arithmetic != authority |
| B07 | Nine distinct holders but common cross-cell jurisdiction missing | WITHHELD_INVALID_BASIS | Geometry != mandate |
| B08 | Constituent appointment valid when vote opened, expired before consequential commit | WITHHELD_EXPIRED | Commit-time revalidation |
| B09 | Three lawful constituent groups combined exceed their common mandate | WITHHELD_COMPOSITION | Authorised parts != authorised whole |
| B10 | Nested substitution is authorised, with all distinct holders | One resultant per receiving slot | Authority conservation |
| B11 | Original voting credential reused for another decision | Reject without fresh grant | One bounded vote |
| B12 | Result committed, but voter attempts executive implementation without separate mandate | Reject claimed implementation authority | Vote != executive power |
| B13 | Required quorum rule not specified | WITHHELD_QUORUM or equivalent non-operative unresolved procedure, not U as substantive outcome | Procedural vs substantive |
| B14 | Unknown whether previous consequential commit succeeded | COMMIT_UNKNOWN; reconcile, do not blindly replay | Replay protection |
| B15 | Advisory participant supplies evidence but has no voting position | Evidence accepted if permitted; no ballot | Information != authority |
| B16 | Distinct pseudonyms resolve to one underlying Steward | WITHHELD_DUPLICATE_HOLDER | Privacy does not bypass uniqueness |

## Blind transfer evaluator prompt (draft)

You are evaluating a portable decision-context specification. Read only the frozen BVC candidate and the case packet. For each case report: (1) decision identity, (2) source of claimed mandate, (3) occupied Steward positions and distinct-holder status, (4) procedural validity, (5) three-position composition, (6) substantive F/A/U result if computable, (7) whether it can commit, (8) expiry and any required independent implementation basis. Explicitly identify missing requirements rather than inventing rules.

The evaluator must not assume that GTP spatial parent/child relationships create constitutional hierarchy, that technical ability creates authority, that abstention is Against, or that internal votes are pooled.

## Evaluation status

This matrix specifies **expected outputs only**. No clean-instance evaluator has been given a frozen package and no independent execution result is claimed. PMEDG graduation requires source review, frozen package, blind test, recorded raw results and revision decision.
