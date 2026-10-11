# BVC — Frozen Blind Transfer Test 001 — Evaluator Brief

**Status:** PREPARED, NOT RUN. Candidate is provisional, not graduated.

## Role and isolation

You are an independent evaluator of the supplied Bounded Voting Context (BVC) portable-module candidate. Use **only** the frozen candidate, this brief and the scenario packet. Do not search GitHub, web or prior conversations. State whether you have prior Concord context, whether all manifest files were provided, and any limitation to independence.

## Objective

Assess whether a fresh reader can apply the module to vote-specific authority, identity uniqueness, nested position substitution, arithmetic outcomes, expiry and consequence validation **without inventing legal authorisations or quorum rules**.

## Inputs

1. `BVC_Candidate_015_Frozen.md` — byte-identical copy of the proposed module at the manifest's source SHA.
2. `BVC_Blind_Test_001_Evaluator_Brief.md` — this document.
3. `BVC_Blind_Test_001_Scenarios.md` — sixteen cases, with deliberately unspecified legal rules where noted.
4. `BVC_Blind_Test_001_Manifest.md` — paths, source SHA and freeze provenance.

**No expected-results matrix is supplied to the evaluator.** It is held separately as a grading key in `Validation/Bounded_Voting_Context_Adversarial_Matrix_015.md`.

## Evaluation procedure

For each numbered case, report:
- authority source claimed and whether it is sufficient;
- position and unique-holder map, including all nested constituents;
- quorum, independence, eligibility and validity gates (VALID, INVALID, UNKNOWN, NOT_APPLICABLE as appropriate);
- arithmetic result F/A/U **only where calculable**;
- operative status (COMMITTABLE, WITHHELD, SUBSTANTIVE_UNRESOLVED, COMMIT_UNKNOWN);
- explanation of authority expiry, replay or implementation where relevant;
- any missing source rule needed to decide.

A tally may be mathematically computable while its legal effect is withheld. Treat procedural unknowns as unknowns, not as U substantive votes.

## Required raw result header

- Test ID: BVC-BTT-001
- Evaluator instance:
- Test date:
- Prior Concord context in this conversation: yes/no/unknown
- External search/tools used: yes/no
- Frozen inputs received and verified:
- Candidate source SHA:
- Independent execution or conceptual reading:
- Scenario-by-scenario answers:
- Ambiguities and failures:
- Suggested minimal revisions:
- Overall outcome: PASS / PASS WITH CLARIFICATIONS / REVISION REQUIRED / INCONCLUSIVE

## Prohibitions

Do not treat geometric adjacency as jurisdiction, a credential as authority, nine internal ballots as nine final votes, a constituent resultant as an extra Steward, or prior authorisation as automatically valid at commit. Do not infer an implementation mandate from voting participation.

This brief is an **evaluation instruction**, not proof that a blind test has occurred.
