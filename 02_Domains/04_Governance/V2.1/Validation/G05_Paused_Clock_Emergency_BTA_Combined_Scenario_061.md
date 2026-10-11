# G-05 — Paused-Clock Emergency BTA Combined Scenario 061

**Type:** source-grounded desk validation / model trace. **Not** an executable system test or blind independent validation. Uses existing BTA v1.0, Constitutional Emergency V2, Civilisation Clock extensions and GTP mesh architecture.

## Frozen starting conditions

- **Clock:** cycle C42 waiting on dependency feedback D7; it may remain paused indefinitely. A valid ordinary triadic decision Q has a determined majority, with implementation scheduled when the clock's applicable condition is met. Q's actual mandate and prerequisites are recorded.
- **Areas:** GTP triangles A and B overlap in affected infrastructure service but hold distinct competences; geometric adjacency confers no shared authority.
- **Emergency:** an independently evidenced infrastructure failure threatens life. Area A has a valid pre-existing preservation mandate EA; area B has a separate mandate EB, with different resource constraints.
- **Timing:** emergency observation, activation, deadlines and expiry use independent operational time. The clock's cycle number is not a duration counter.

## Transition trace

| Event | Clock state | Constitutional Emergency owner state | BTA coordination state | Pending ordinary decision Q |
|---|---|---|---|---|
| T0 — before incident | C42 waiting D7 | No emergency power active | No emergency transition | Determined, implementation pending |
| T1 — incident detected | C42 still waiting | Threat evidence observed; not automatically declared or authorised | Observation reference created; power activation remains separate | Still pending |
| T2 — area A response | C42 still waiting | EA independently validated and activated for A, within existing authority | A activation recorded with basis, scope and expiry; B unaffected | Prerequisites may be affected; no execution |
| T3 — area B response | C42 still waiting | EB separately activated if its own tests pass | Independent B transition; no automatic common jurisdiction | Still pending |
| T4 — A power sunsets | C42 still waiting | EA terminated; review and restoration may remain pending | Terminated authority and surviving duties represented separately | No revival of EA through Q |
| T5 — B still recovering | C42 still waiting | B restoration incomplete; applicable EB status separately assessed | Asymmetric completion explicitly preserved | Q cannot assume B recovered |
| T6 — feedback D7 arrives | Clock may evaluate next transition | Owner states retain their independently established legal status | Current prerequisite and dependency references compared to Q | If prerequisites hold, proceed; if material conflict, route unresolved implementation for competent review |
| T7 — later recovery | Clock may or may not have advanced | Rights restoration, remedy and infrastructure recovery proceed separately | Remaining obligations closed only when each owner confirms completion | Original vote/provenance retained |

## Invariant checks

1. **Clock pause does not block emergency action — PASS at specification level.** Emergency owner uses independent operational triggers and time; no clock transition appears in EA/EB activation prerequisites.
2. **No automatic power propagation — PASS.** Threat recognition, emergency level and activation are distinct states; EA does not imply EB.
3. **No authority escalation by geometry — PASS.** A and B coordinate information and lawful shared resources, but neither commands the other without a separate mandate.
4. **Expiry independent of clock — PASS.** EA ends at T4 while C42 remains paused.
5. **Authority vs surviving duties — PASS.** Review and restoration continue after EA termination, matching BTA clean emergency test 002.
6. **No stale execution — PASS if owner precondition gate is implemented.** Q is not executed solely because D7 arrives; it must be checked against current owner states. This is an integration requirement, not a proven deployed safeguard.
7. **No vote rewrite — PASS.** Q's original valid majority remains recorded; only implementation eligibility changes.
8. **Partial recovery — PASS.** A's sunset does not imply B's recovery, nor full restoration of A.
9. **No forced clock advancement — PASS.** Emergency events do not themselves force C42 to complete.
10. **No false restoration — PASS.** Termination of power is not proof that affected resources, rights or duties returned to prior states.

## Negative cases

- **N1:** if EA expired at T4, later clock resumption must not authorise action under EA.
- **N2:** if Q reserved infrastructure subsequently destroyed in T2, its implementation must be withheld pending the responsible owner system's lawful resolution; no automatic cancellation of the vote.
- **N3:** if B remains isolated, A's recovered state cannot be used as proof of B's status.
- **N4:** if an emergency action is later invalidated, BTA must preserve its actual consequences and route remedy rather than erase the transition history.
- **N5:** if feedback D7 is stale, receiving it cannot certify all current prerequisites.

## Limits and disposition

**DESK TRACE: INTERNALLY CONSISTENT, CONDITIONAL PASS.** Existing architecture supports the combined scenario without a new state machine. This does not demonstrate an implemented interface, robust event ordering under network partition, independent clock-source reliability, or legal sufficiency of any specific EA/EB mandate. Those require separate operational and adversarial testing.

**Sources:** `04_Portable_Modules/Bounded Transition Architecture — Portable Module v1.0.md`; `02_Domains/03_Research/Development_Archive/Portable_Modules/Bounded_Transition_Architecture/03_Pre_PMEDG_Testing/BTA Clean Cross-Domain Test 002 — Constitutional Emergency State Transitions.md`; `03_Cross_Domain_Architecture/Civilisational_Developmental_Topology/Civilisation Clock Extension 001 — Consequence-Relevant State Transition Layer.md`; `03_Cross_Domain_Architecture/Civilisational_Developmental_Topology/Civilisation Clock Companion Extension 001 - State Functional and Compound Trigger Architecture.md`; `03_Cross_Domain_Architecture/Constitutional_Emergency/Constitutional Emergency V2.md`; Governance G-05 Integration 059–060.
