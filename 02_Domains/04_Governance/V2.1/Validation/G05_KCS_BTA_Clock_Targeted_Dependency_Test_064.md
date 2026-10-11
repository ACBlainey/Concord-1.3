# G-05 — KCS/BTA/Clock Targeted Dependency Test 064

**Method:** transparent specification-level thought test against existing source contracts. Not a live system run or independent blind validation.

## Frozen setup

Civilisation Clock is paused at state C42 awaiting feedback D7.

- **Q1:** pending ordinary decision to allocate Pump P to Water Network A, contingent on P remaining available and fit for purpose.
- **Q2:** pending ordinary decision to publish an unrelated education glossary, with no dependency on Pump P or the water network.
- **E1:** independently authorised emergency action reallocates Pump P to critical Water Network B, with bounded authority and operational-time expiry.
- **R1:** emergency authority subsequently expires, while equipment inspection and review obligations remain.

KCS dependency graph includes Q1 -> Pump P availability. Q2 has no Pump P link. BTA represents E1 and R1 separately, preserving authority, resource and surviving-duty dimensions.

## Expected state trace

| Stage | Emergency owner | BTA | KCS dependency effect | Clock/queued decisions |
|---|---|---|---|---|
| T0 | No active emergency | Baseline owner states | Q1 depends on Pump P; Q2 independent | Clock waiting; Q1 and Q2 pending |
| T1 | E1 activated lawfully | Record reallocation and bounded authority | Mark Q1's Pump P assumption for reassessment; do not flag Q2 solely for adjacency | Clock still waiting |
| T2 | E1 expires | Terminate authority; keep inspection/review pending | Q1 remains subject to current availability verification; expiry alone does not prove Pump P returned | Clock still waiting |
| T3 | D7 feedback arrives | No implied renewed emergency authority | Verify Q1 current dependency; Q2 unchanged | Q1 held if Pump P unavailable; Q2 eligible under its own ordinary conditions |
| T4 | Owner restores Pump P availability, if verified | Recovery owner confirms state | Update dependency state, clear Q1 only after actual prerequisite satisfaction | Q1 may proceed via existing mandate/timing; no vote rewriting |

## Assertions

- **A1, relevant propagation:** KCS identifies Q1 as materially affected by E1. Supported by KCS dependency/change-propagation architecture.
- **A2, proportionality:** KCS does not infer Q2 is affected solely because both decisions share the Clock. Supported by material-dependency design; requires a complete enough dependency graph.
- **A3, non-propagation:** expiry of E1 does not automatically restore Pump P availability. Supported by BTA v1.0 and its Constitutional Emergency clean test.
- **A4, temporal independence:** E1 and R1 proceed while Clock C42 is paused. Supported by Constitutional Emergency owner rules and authorial clarification 059.
- **A5, no authority transfer:** neither KCS dependency flag nor BTA state record grants emergency power, voting authority or jurisdiction. Supported by owner-boundary principles.
- **A6, no stale execution:** Q1 is not implemented until its resource prerequisite is currently satisfied. This is a necessary interface gate, not demonstrated software behaviour.

## Negative-control and falsification criteria

The interface fails if Q1 executes with Pump P unavailable, Q2 is blocked solely by the shared Clock, expiry of E1 automatically marks Pump P restored, or a KCS flag itself changes constitutional authority.

**Disposition:** EXPECTED SPECIFICATION-LEVEL PASS for A1–A5; A6 is a required execution integration, not validated implementation. No simulation or software was run. A real test should use owner-state event records, versioned KCS dependencies and a clock queue executor; capture actual outputs against these assertions.

## Sources

KCS Companion Upgrade 001 — Operational Dependency and Change-Propagation Architecture; BTA Portable Module v1.0; BTA Clean Cross-Domain Test 002 — Constitutional Emergency State Transitions; Civilisation Clock Companion Extension 001; Constitutional Emergency V2; Governance G-05 059–063.
