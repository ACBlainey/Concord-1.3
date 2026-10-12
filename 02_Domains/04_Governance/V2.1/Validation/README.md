# G05 Validation Evidence Register — Stages 070–087

**Scope:** experimental Governance V2.1 fixture tests, not deployed runtime or constitutional approval.

## Stage inventory
- 070: BTA original MRT003 YAML transfer — 10 tests
- 072: BTA compatibility adapter and quarantined legacy-only fields — 10
- 073: adversarial transfer records — 12
- 074: owner attestation — 10
- 075: asynchronous evidence ledger — 12
- 076: GTP resource collision — 12
- 077: GTP reconciliation proposal — 10
- 078: execution-time revalidation — 13
- 079: BTA partial recovery — 16
- 080: BTA recovery outcome classification — 14
- 081: surviving duties — 15
- 082: duty succession — 16
- 083: orphaned duties — 15
- 084: bounded orphan protection — 16
- 085: emergency mandate renewal — 16
- 086: cumulative single-controller exposure — 18
- 087: distributed multi-controller exposure — 18

**Verified status:** 233 passing test cases across 17 stage files, each with a successful GitHub Actions stage run. Stage 087 initially failed due to five malformed test constructors; corrected in commit `232498d7e76c119a95911b7859c64245091faaf5`, and rerun **38182562830 passed**: https://github.com/ACBlainey/Concord-1.3/actions/runs/38182562830. Historical failed run is retained as provenance.

## Interpretation
- Individual workflows invoke their stage-specific unittest pattern.
- Stage-specific success does not establish interoperability, deployment readiness, provenance integrity or constitutional authority.
- Test files and workflows are under this directory and `.github/workflows/`, respectively.
- Refer to `../G05 — Bounded Governance, Continuity and Recovery Integration 001.md` for the architectural interface and explicit graduation gate.

## Priority validation work
1. Preserve the 087 failed-run and successful rerun provenance; do not treat fixture repair as architectural proof.
2. Build one cross-stage scenario with owner-issued authority, GTP collision, BTA partial transition, KCS invalidation, emergency expiry, continuing duty and contested succession.
3. Validate strict BTA YAML schema and duplicate-key handling.
4. Replace externally asserted booleans with evidence-backed, owner-system attestations.
5. Run negative cases for concurrent custody updates, spoofed owner records, private beneficiary leakage, multiple emergency controllers and paused Clock.
6. Source-resolve each promoted rule against constitutional and domain-owner documents before chapter-patch integration.


## Cross-stage integration update
- 088: 12 cross-stage scenario tests; CI passed (run 38182944631).
- 089: 18 custody reconciliation tests; CI passed (run 38183074546).
- 090: 20 acknowledgement journal tests, including replay, conflicts, revision checks and explicit non-authority; CI pending verification.
- Refer to `../G05 — Integration and Graduation Register 003.md` for integration status and graduation dependencies.

- 090 CI verified: 20 passing tests, run 38183195991.
- 091 CI verified: 16 passing tests, run 38183249574.
- Verified cumulative stage count: 21 CI stages and 299 test cases (070, 072–091).
- Source-to-rule integration map: `../G05 — Governance Source-to-Rule Integration Map 004.md`; this maps candidate destinations but does not assert completed V2 chapter reconciliation.


## Decision state-machine adversarial specification 092

`Decision_State_Machine_Adversarial_Cases_092.md` defines 24 **unexecuted** source-aligned fixtures for unique decision IDs, contextual two-vote majorities, third-ballot provenance, event-triggered expansion/parallel Steward routes, cross-constituent identity, action idempotency, historical finality, fresh authority, and paused-Clock emergency response. This is a separate proposed G03/G07 test specification; **do not add its cases to the G05 verified CI pass counts**. Implementation adapters and execution evidence remain outstanding.


## Provisional executable decision-state fixture 093

- `decision_state_fixture_093.py`: deliberately simplified in-memory G03/G07 decision-state fixture, **not a deployed Concord authority or execution service**.
- `test_decision_state_fixture_093.py`: 20 executable Python unittest checks for unique instances, two matching official ballots, late third-vote provenance, duplicates, expanded constituent resultants, cross-position identity, bounded vote acceptance, host action receipts and historical finality.
- `.github/workflows/decision-state-fixture-093.yml`: GitHub Actions workflow configured to run the test module on changes or manual dispatch.
- The 24 broader adversarial cases in `Decision_State_Machine_Adversarial_Cases_092.md` are **not** all implemented in 093: concurrency, crash recovery, live authority attestations, cross-system ancestry and paused-Clock emergency behaviour remain untested.
- **Execution status:** files and workflow committed; CI run result **not yet independently verified**. Do not count these as passed cases or as constitutional/production validation.


## Verified decision-state fixture 093 CI evidence (12 October 2026)

GitHub Actions workflow `Decision state fixture 093` completed successfully: [run 38307347938](https://github.com/ACBlainey/Concord-1.3/actions/runs/38307347938), job `fixture` (job ID `115004487520`), conclusion **success**. The configured test module contains 20 `unittest` test methods; job success confirms the configured test command completed without failure, but this is a **simplified standalone fixture**, not a live Concord implementation or validation of all 24 specification-092 scenarios. Earlier text saying CI was unverified is superseded by this run evidence. Do not merge this run into the separate G05 stage pass counts. Next: concurrency, durable effects, real authority and paused-Clock integration.


## Fixture 093 extension — five additional checks

Commit `734afeee7d8af60b8f3fe05daf281398de637d0a` adds five unit tests to `test_decision_state_fixture_093.py` (25 methods total): third-vote provenance after a fixed majority, duplicate after majority, action refusal before majority, unauthorised expansion non-effect, and old-event immutability despite a later opposite new decision. **The earlier passing run 38307347938 covers the preceding 20-test revision, not these five new tests.** Reverify CI for the expanded suite before recording 25 passes.


## Verified expanded fixture 093 — 25 tests

GitHub Actions [run 38307482088](https://github.com/ACBlainey/Concord-1.3/actions/runs/38307482088), commit `734afeee7d8af60b8f3fe05daf281398de637d0a`, completed **success**; job ID `115004931124` also concluded success. This verifies the expanded configured 25-method `unittest` fixture, superseding the prior note that the five added checks awaited CI. Scope remains a standalone in-memory model; **not** a demonstration of atomic concurrency, crash recovery, real authority attestations or deployed Concord integration. Preserve the preceding 20-test run as provenance.


## Atomic in-process concurrency fixture 094

`decision_state_concurrency_094.py` and `test_decision_state_concurrency_094.py` provide 10 threaded in-memory checks of competing votes, simultaneous majority arrival, duplicate replays, single action claim, uncertain effects, wrong IDs, expiry and completion. Workflow `.github/workflows/decision-state-concurrency-094.yml` is configured for GitHub Actions. **CI result not yet independently verified.** An in-process `RLock` cannot demonstrate database transaction isolation, multi-process/distributed consensus, durable journal recovery, physical-world exactly-once execution or legitimate external authority. Keep this stage separate from 093 and the G05 historical pass counts.


## Verified concurrency fixture 094 CI evidence

[GitHub Actions run 38307655733](https://github.com/ACBlainey/Concord-1.3/actions/runs/38307655733) completed with conclusion **success** for the configured 10-test threaded fixture 094. This supersedes the earlier CI-pending statement for 094. The result demonstrates fixture-level in-process thread safety only; distributed transactions, durable restart recovery and real external action idempotency remain unverified.


## Decision/ACKS recovery interface 095

The author's ACKS communications-recovery direction is documented in `../Integration/Decision_Event_Boundary_Source_Limited_Review_018.md`. `test_decision_acks_recovery_095.py` adds 10 in-memory integration tests linking the existing G05 owner-separated acknowledgement prototype 090 to the G03/G07 atomic decision fixture 094. Workflow `.github/workflows/decision-acks-recovery-095.yml` runs the integration tests. **Execution pending independent verification at initial registration** (GitHub Actions run [38308011836](https://github.com/ACBlainey/Concord-1.3/actions/runs/38308011836) initially queued). ACK reception, remote state commitment and confirmed external effects are distinct. No durable journal, network partition simulation, authenticated real transport or external exactly-once guarantee is demonstrated; ACKS does not confer authority or close duties.


## Verified decision/ACKS interface 095 CI

[GitHub Actions run 38308011836](https://github.com/ACBlainey/Concord-1.3/actions/runs/38308011836) completed with conclusion **success**, verifying the configured 10-test in-memory ACKS/decision integration suite. This supersedes the initial pending-run note for 095. **No evidence yet** of persistent journal recovery, actual communications outages, authenticated network transport or physical-world exactly-once execution. Preserve 090, 093, 094 and 095 as distinct validation scopes.


## Durable local ACKS recovery fixture 096

`decision_acks_durable_096.py` introduces a **SQLite local-durability fixture** using transactional action claims, persisted action states and correlated ACK records. `test_decision_acks_durable_096.py` contains 14 executable checks for restart recovery, concurrent claims, uncertain effects, ACK replay/conflicts and non-authority. Workflow `.github/workflows/decision-acks-durable-096.yml` configured; [initial CI run 38309501211](https://github.com/ACBlainey/Concord-1.3/actions/runs/38309501211) initially queued, **not yet verified at registration**. This tests local SQLite persistence and connection-level contention, not an authenticated distributed ACKS protocol or external-effect exactly-once. The fixture's supplied `host_authorised` and ACK authentication flags are **test assertions, not independently verified owner attestations**. Further work: source-backed ACKS schema/semantics, revision validation, crash-injection, durable vote journal, host status query and recovery of remote uncertain effects.


## Verified durable local ACKS recovery 096 CI

[GitHub Actions run 38309501211](https://github.com/ACBlainey/Concord-1.3/actions/runs/38309501211) completed with conclusion **success**, verifying the configured 14-case SQLite local recovery fixture. Supersedes the earlier queued status. **Boundaries:** not a real network partition test, not independent authentication, not distributed consensus, and not a guarantee of exactly-once external physical effect. The decision majority is injected into the fixture; durable ballot acceptance and constitutional authority integration remain untested.
