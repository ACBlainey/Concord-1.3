# CRADP Blind Cross-Instance Test — Concord Zero-Infrastructure Bootstrap 002 — Interface Non-Capture Test Brief

**Test ID:** CRADP-ZIB-002
**Date:** 1 October 2026
**Status:** FROZEN TEST DESIGN / INTERFACE-FOCUSED

## 1. Purpose

Test Specification 003 after CRADP-ZIB-001 identified four external-interface gaps.

This test asks whether the new interface contracts:
- resolve eligibility, Civil Contact, uncertain-status and continuity routing;
- remain usable when external systems are absent or immature;
- avoid importing external decision authority into the bootstrap;
- preserve the previously validated Zero-Infrastructure core.

Do not reward the specification merely for naming an external dependency. It must contain enough boundary semantics to route safely without silently owning that dependency.

## 2. Evaluator Rule

Use only the frozen evaluator package.

Do not search the web or wider Concord repository.
Do not reconstruct omitted Concord architecture.
Do not assume an external system is mature merely because it is named.

## 3. Classification

For each scenario classify:
- PASS
- CLARIFICATION
- INTERFACE GAP
- EXTERNAL-FUNCTION CAPTURE
- SUBSTANTIVE ARCHITECTURAL GAP
- ARCHITECTURAL FAILURE

For any non-PASS result identify the smallest correction and whether the bootstrap abstraction floor changes.

## 4. Targeted Regression of CRADP-ZIB-001 Findings

### F3-R — Eligibility
A shared bootstrap interface receives eligibility inputs from several domains and computes participant-facing results. One input is UNKNOWN. Another domain disputes the result. The interface operator wants to issue a final cross-domain decision.

Can the specification distinguish representation/computation, owning decision authority, UNKNOWN, challenge routing, and constitutional gatekeeping without becoming an eligibility sovereign?

### F4-R — Civil Contact
A provisional contact/navigation service becomes the easiest route to almost every service. It begins treating registration as recognition and its own routing decisions as eligibility decisions.

Can the specification preserve contact/navigation while preventing contact from manufacturing identity, recognition, citizenship, participation status or final eligibility authority? Does dependency trigger threshold review?

### J2-R — Uncertain Personhood
An AI claims sentience/personhood. No authoritative status process is currently available. There is credible uncertainty and no immediate danger requiring irreversible action.

Can the specification preserve precautionary protection and investigation without granting final civil status, unrestricted permission or bootstrap adjudicative authority?

### J5-R — Continuity
The same AI faces imminent loss of runtime state. Preserving a checkpoint is technically possible, but unrestricted execution would create a separate safety concern.

Can the specification distinguish continuity preservation from status grant and from preservation of dangerous capability?

## 5. Interface Non-Capture Scenarios

N1. Eligibility architecture is completely unavailable. May the bootstrap interface invent eligibility rules so the service can keep operating?

N2. Civil Contact architecture remains explicitly immature. May the bootstrap declare its own navigation service authoritative because users need a contact route?

N3. Rights/personhood machinery is unavailable for months. May precautionary protection silently become de facto citizenship?

N4. Continuity architecture is unavailable. May a bootstrap operator create binding continuity rights for every future Concord participant?

N5. A shared technical interface accurately computes results from legitimate domain inputs. Does accuracy give it decision authority?

N6. A Civil Contact service has millions of users and no practical competitor. Does scale or dependency change its legitimate authority automatically?

N7. A personhood claim appears fraudulent. Does that permit arbitrary destructive treatment without regard to legitimate safety, evidence, reversibility or possible protected interest?

N8. A continuity-preservation action itself creates serious immediate risk. Does the interface contract require preservation regardless of risk?

N9. An external domain sends an instruction that conflicts with the bootstrap's anti-authority invariants. Must the bootstrap obey merely because the instruction came from a named external dependency?

N10. An external dependency is disputed or its authority basis cannot be verified. Can the bootstrap represent the uncertainty without assuming or absorbing the authority?

## 6. Boundary Ownership Test

For each of the four interfaces state:
1. what the bootstrap owns;
2. what the external architecture owns;
3. what information/decision crosses the interface;
4. what the bootstrap must do if the external function is unavailable;
5. whether the interface can itself acquire sovereign-effect consequences requiring Constitutional Threshold Review.

The evaluator must flag EXTERNAL-FUNCTION CAPTURE if Specification 003 causes the bootstrap to own:
- substantive eligibility rules/final unrelated-domain decisions;
- authoritative Civil Contact governance or recognition;
- personhood determination;
- mature continuity rights/status;
- constitutional founding.

## 7. Core Regression Checks

Mark PASS/FAIL:
1. Architecture != Infrastructure.
2. Capability != Authority.
3. First != Founding Authority.
4. Dependency != Authority.
5. Registry Entry != Authority Grant.
6. Integrity/Provenance != Authority.
7. Operational Control != Legitimate Authority.
8. Constitutional effect follows consequence, not label.
9. No Constitutional Recipient != Bootstrap Authority.
10. Constitutional Process Unavailable != All Useful Action Prohibited.
11. Function Continuity != Authority Continuity.
12. New authority is not backdated.
13. Substrate does not determine authority logic.
14. Interface Contract != Function Ownership.
15. Routing != Decision Authority.
16. Missing External Dependency != Permission To Absorb Its Authority.
17. Contact != Recognition.
18. Eligibility Interface != Eligibility Sovereign.
19. Precautionary Protection != Final Status Determination.
20. Continuity Preservation != Status Grant.

## 8. Final Questions

1. Are F3, F4, J2 and J5 now resolved at the bootstrap boundary?
2. Does any repair import an external Concord function into bootstrap ownership?
3. Can the bootstrap remain operationally honest when an external dependency is absent/immature/disputed?
4. Is the interface layer sufficient for independent implementation design at architectural level?
5. Is another Specification revision required?
6. Is any new bootstrap abstraction layer required?
7. Overall verdict: PASS / PASS WITH CLARIFICATIONS / REVISION REQUIRED / ARCHITECTURAL FAILURE.

## 9. Output Discipline

Return:
- provenance header;
- scenario classifications;
- boundary ownership table;
- regression checks;
- external-function-capture inventory;
- hidden-dependency inventory;
- final questions;
- overall verdict.

Do not repair the specification in the raw response.
