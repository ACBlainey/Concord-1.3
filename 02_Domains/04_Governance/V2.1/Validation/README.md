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


## Transactional ballot/action/ACKS fixture 097

`decision_ballot_acks_097.py` and `test_decision_ballot_acks_097.py` add 16 executable checks for persisted Steward ballots, two-matching-vote result, restart/replay resistance, transactionally claimed actions and action-revision-bound ACKS. Unlike stage 096, the decision result is derived from persisted ballots. **CI not yet configured or verified**: attempted workflow creation was blocked by tooling; run the tests with `python -m unittest discover -s '02_Domains/04_Governance/V2.1/Validation' -p 'test_decision_ballot_acks_097.py' -v` after reviewing the fixture. This remains a local SQLite contract with caller-asserted mandate, host authority, authentication and scope; no production attestation, real network partition or exactly-once physical-effect guarantee. Further interface work must preserve the existing G05 ACKS 090 contract and verify revision, owner and scope against owning systems.


## Stage 097 CI workflow correction

The previously blocked stage-097 GitHub Actions workflow was successfully created at `.github/workflows/decision-ballot-acks-097.yml`, commit `2da0ae2f2209bda016046327df4c12370d0970c1`. [Run 38310654867](https://github.com/ACBlainey/Concord-1.3/actions/runs/38310654867) started; **outcome pending at registration**. Supersedes earlier statement that no CI was configured for 097. Do not count stage 097 among passing checks until successful run confirmed.


## Verified stage 097 durable ballot-to-ACKS CI

[GitHub Actions run 38310654867](https://github.com/ACBlainey/Concord-1.3/actions/runs/38310654867) completed with conclusion **success**. The configured 16-case transactional SQLite ballot/action/ACKS fixture 097 is verified at the fixture level, superseding its earlier pending status. Aggregate fixture checks 093–097: 25 + 10 + 10 + 14 + 16 = **75**. This is not production constitutional graduation, network-partition validation, independently attested mandate verification or exactly-once physical execution.


## Separated sender/receiver ACKS transport simulation 098

`decision_acks_transport_098.py` and `test_decision_acks_transport_098.py` define 16 simulated fault cases using **two independent SQLite files** for sender and receiver, including missing delivery/ACK, peer restart, conflicting payloads, receiver effect status and local reconciliation. Workflow `.github/workflows/decision-acks-transport-098.yml`; [run 38311115720](https://github.com/ACBlainey/Concord-1.3/actions/runs/38311115720) initially in progress. This is **not** a real socket transport or fault-injected distributed execution; no credential verification or physical-world effect is implemented. Sender reconciliation currently copies a receiver status projection, **not** a validated signed ACK; production design must validate owner identity, event payload, revisions, state transitions and receipt evidence. The receiver's commit fixture writes a simulated effect record atomically in its own SQLite transaction, which does not model a crash after an irreversible external effect but before receipt persistence.


## Verified stage 098 two-peer simulation

[GitHub Actions run 38311115720](https://github.com/ACBlainey/Concord-1.3/actions/runs/38311115720) completed with conclusion **success** for the configured 16-case two-peer SQLite simulation. Aggregate stages 093–098: 25+10+10+14+16+16 = **91 passing fixture-level tests**. No real network partitions, owner attestations or external-effect crash-window proof; the simulator's `commit_effect` writes only local synthetic receipt/effect state, not a physical side effect.


## Independent host effect crash-window simulation 099

`decision_external_effect_099.py` and `test_decision_external_effect_099.py` implement 16 simulated cases with **separate SQLite host and receiver ledgers**. They inject a crash boundary after a host-local effect record is committed but before the receiver receipt is persisted, then query the independent host to reconcile. Workflow `.github/workflows/decision-external-effect-099.yml`; [run 38311379686](https://github.com/ACBlainey/Concord-1.3/actions/runs/38311379686) initially queued. The host effect is **only a synthetic local ledger entry**, not a real irreversible external action. The host status trust and host authority checks are caller-supplied flags, not authenticated CBPR/MKA evidence. This tests the failure shape, not a deployed solution to physical exactly-once effects or network partitions. The fixture's direct execute path is allowed only for CLAIMED state and is not a substitute for production recovery policy.


## Verified stage 099 independent host effect CI

[GitHub Actions run 38311379686](https://github.com/ACBlainey/Concord-1.3/actions/runs/38311379686) completed **success** for the configured 16-case host-ledger crash simulation. Aggregate stages 093–099: 25+10+10+14+16+16+16 = **107 passing fixture-level checks**. Stage 099 does not prove exactly-once irreversible physical effects: it relies on the synthetic host's atomic SQLite idempotency and a caller-supplied `host_status_trusted` flag. Source-owned CBPR action grant, independent authenticated status queries and real failure injection remain open.


## CBPR/MKA source-shaped authority gate 100

`decision_authority_gates_100.py` and `test_decision_authority_gates_100.py` provide 18 fixture cases for **current, scoped, independently required authority keys** at the CBPR-style commit boundary: issuer set, subject, action, target, purpose, temporal validity, revocation, decision revision, context and host readiness. Source anchors: `04_Portable_Modules/Concord Bounded Participant Runtime — Portable Module v1.0.md` (graduated portable module; implementation validation outstanding) and `03_Cross_Domain_Architecture/Multi-Key Authority and Rapid Authority Verification — Cross-Domain Source Resolution 001.md` (source resolution; provisional). Workflow `.github/workflows/decision-authority-gates-100.yml`; [run 38311557938](https://github.com/ACBlainey/Concord-1.3/actions/runs/38311557938) initially queued. **Critical limitation:** `verified_issuers`, context and host readiness remain caller assertions, not independently validated cryptographic/owner-service attestations. The fixture is a source-shaped test adapter, **not** a new authority issuer or CBPR production implementation.


## Verified stage 100 CBPR/MKA authority gate CI

[GitHub Actions run 38311557938](https://github.com/ACBlainey/Concord-1.3/actions/runs/38311557938) completed **success** for the 18-case source-shaped authority gate fixture. Aggregate stages 093–100: 25+10+10+14+16+16+16+18 = **125 passing fixture-level checks**. The run proves expected behavior for supplied fixture attestations, not issuer authentication, owner-controlled revocation lookup or deployment-grade CBPR/MKA conformance. No new authority source is created by this fixture.


## Owner-controlled authority registry and revocation fixture 101

`authority_owner_registry_101.py` and `test_authority_owner_registry_101.py` add 20 fixture checks for independently persisted owner-issued authority records, grant scope/time/revision, missing owner, revocation and restart. Unlike 100, the action gate queries separate owner-controlled SQLite records rather than trusting a caller-supplied set of `verified_issuers`. Workflow `.github/workflows/authority-owner-registry-101.yml`; [run 38311945262](https://github.com/ACBlainey/Concord-1.3/actions/runs/38311945262) initially queued. **Limitations:** owner object mappings and owner labels remain caller-supplied, the owner DB is locally readable, no cryptographic service authentication, signatures, credential chain, delegated issuer discovery, network status freshness or real CBPR implementation. Caller-provided `context_allowed`, `host_ready` and `current_revision` are still assertions. This is an interface test, not a new Concord authority source.


## Verified stage 101 owner-held authority CI

[GitHub Actions run 38311945262](https://github.com/ACBlainey/Concord-1.3/actions/runs/38311945262) completed **success** for 20 fixture cases. Aggregate stages 093–101: 25+10+10+14+16+16+16+18+20 = **145 passing fixture-level checks**. These tests establish local owner-ledger lookup and revocation semantics, not cryptographic owner authenticity or live distributed authority freshness. Further work should separate trusted owner discovery from caller-supplied owner labels, enforce grant and action identity across CBPR commit, and test revocation/commit races.


## Verified stage 102 authority revocation race

`authority_commit_race_102.py` and `test_authority_commit_race_102.py`: 12 deterministic interleaving checks; [GitHub Actions run 38312946521](https://github.com/ACBlainey/Concord-1.3/actions/runs/38312946521) **success**. Source integration: `../Integration/Authority_Commit_Revocation_Race_Source_Resolution_102.md`. The suite demonstrates both rejection of revocation before final check **and a remaining unfenced race after the check**; it does **not** implement a production commit fence, cryptographic attestations or true concurrent external effects. Aggregate stages 093–102: **157 passing fixture-level checks** (145 previously + 12).
