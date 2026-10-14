# Glass Hammer — Architectural Consolidation and Analogy Boundary 121

**Status:** source-based governance integration and scope correction. No new authority or portable module. This document takes precedence over the *illustrative lock-testing interpretation* of Stage 120, not over historical sources or valid existing governance architecture.

## Authorial correction: do not operationalise the room analogy

The three rooms, cases, combinations, hammers and seventh digit are an explanatory analogy. They do **not** prescribe physical hardware, a seven-digit electronic controller, or separate lock state machines. Stage 120's `IndependentCaseLock` and its tests are illustrative only; they are not requirements for Concord implementation or graduation.

The actual architectural implementation concerns independently bounded voting authority, transactional vote commitment, information disclosure, decision acceptance, and separate review/host-execution authority. Future validation should test those real boundaries rather than simulate rooms and locks.

## Reconciled invariants

1. **Three independent positions:** Each eligible Steward has distinct, bounded authority to commit a ballot in their own decision context. No Steward can inherit another's authority or learn another's vote merely by occupying a Steward position.
2. **Authority consumed once:** A valid committed For, Against or Abstain ballot is immutable. A repeated submission, changed event ID, later regret, peer pressure or concern cannot amend it. Challenge to validity requires separate adjudication with retained provenance.
3. **Minimal participation projection:** The seventh digit means only the number (0–3) of distinct positions that have committed. It reveals neither position/identity nor vote choice, reasoning, result, review status or acceptance status. A count is an information projection, not an authority token.
4. **Noninterference:** One Steward's commitment, the participation count and its availability must not alter the remaining Steward's independently valid vote authority or ability to submit. The third vote may be recorded after independently justified early acceptance while its own contextual authority remains valid.
5. **Determination vs acceptance vs execution:** Two matching votes can arithmetically determine an outcome. Early acceptance needs a separate valid contextual basis; normal progression allows the third Steward. Neither determination nor acceptance automatically grants downstream host execution authority.
6. **Concern and review:** A post-vote concern is append-only and does not change the tally. Review and any replacement decision need fresh, independently legitimate authority; an original Steward may be excluded from a replacement panel where independence requires. The review router does not become a judge.
7. **Information protection:** CWA/CIBB projection controls separate private ballots, concern evidence, review evidence and permissible aggregate participation data. The count-only projection must be authenticated and bounded in a real implementation; raw ballot storage must not be exposed as a side effect.
8. **Operational time:** A paused or variable Civilisation Clock cannot stall an independently authorised emergency path. CRSTL records relevant state changes but grants no authority.
9. **Historical continuity:** The original vote and any later concern, validity finding, review or replacement decision are distinct attributable records. Historical preservation does not confer operational decision authority.

## Actual implementation boundaries and current gaps

| Boundary | Existing fixture | What remains |
| --- | --- | --- |
| Atomic one-use vote and independent positions | Stage 108 and corrected Stage 110 | Genuine authenticated Steward identity, owner-controlled eligibility/authority, cross-substrate integration |
| Contextual early acceptance | Stages 110–112 | Genuine owner state, commit-time context proof, no distributed TOCTOU |
| Concern/review referral | Stage 116 | Genuine Judiciary/STRA routing authority, replacement panel exclusion with alias checks |
| Protected projections | Stages 117–118 | Authenticated CIBB enforcement, owner-mediated revocation-safe projection |
| Anonymous participation count | Stage 119 specification; Stage 120 count-only method | Connect to owner-authorised projection and preserve noninterference without toy locks |
| Host effect | Stage 109 and owner transition plan 113 | Separate legitimate execution grant, reconciliation of uncertain external effects |

## Important source conflict / correction

Stage 108's standalone `BallotMachine.submit` closes a decision when two matching ballots determine a majority. That **must not** be treated as the current policy for the third Steward: Stage 110 explicitly separates determination from acceptance and preserves the third Steward's independent remaining ballot. Do not integrate the Stage 108 closure shortcut as the operative rule.

Stage 117's direct `view(...authority_verified=True)` and Stage 120's direct `seventh_digit()` are **untrusted internal fixture interfaces**; they are not safe external access endpoints. Stage 118 is the more appropriate owner-check pattern, but still lacks genuine authentication and atomic owner/projection enforcement.

Stage 120's physical-lock independence tests do not establish an architectural guarantee. The architectural requirement is that vote submission checks its own legitimate authority, not another Steward's vote count or the indicator's availability.

## Validation discipline

Before adding another fixture, identify a genuine architectural boundary not already exercised by an existing test. Prefer one concise integration test across vote commitment, remaining-Steward eligibility, count-only owner-authorised projection, and separate acceptance/review paths. Do not multiply analogy tests or imply fixture passes equal deployment assurance.

## Sources

- `02_Domains/04_Governance/V2.1/Integration/Glass_Hammer_Immutable_Vote_Concern_and_Independent_Review_115.md`
- `02_Domains/04_Governance/V2.1/Integration/Glass_Hammer_Seventh_Digit_Anonymous_Commit_Count_119.md`
- `02_Domains/04_Governance/V2.1/Integration/Glass_Hammer_Operational_Cross_Boundary_109.md`
- `02_Domains/04_Governance/V2.1/Integration/Glass_Hammer_Contextual_Early_Acceptance_110.md`
- `02_Domains/04_Governance/V2.1/Integration/Glass_Hammer_CIBB_Owner_Checked_Projection_118.md`
- `04_Portable_Modules/Contextual Wrapper Architecture — Portable Module.md`
- `04_Portable_Modules/Concord Information Black Box Portable Module v1.0.md`


Integrated into Chapter 12.0d, commit 3aaca6d6d9a52e17a8fda0997904393a69c19f04.
