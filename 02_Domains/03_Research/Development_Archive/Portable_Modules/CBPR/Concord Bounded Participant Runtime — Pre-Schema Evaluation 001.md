# Concord Bounded Participant Runtime — Pre-Schema Evaluation 001

**Date:** 2 October 2026
**Status:** ACTIVE DEVELOPMENT / PRE-SCHEMA EVALUATION / NOT CANONICAL
**Target:** Concord Bounded Participant Runtime — Formal Model 001

## Result

The formal model was tested against omission, composition and semantic-ambiguity cases.

1. Missing consequence class on a potentially consequential interface — **FAIL CLOSED / PASS**.
2. Stale grant reference — **PASS**; reference/current-state validation fails.
3. Credential valid at proposal, revoked at commit — **PASS**; commit-time validation rejects.
4. Redirect changes effective target — **PASS** where effective target can be resolved; otherwise fail closed for bounded-target actions.
5. Runtime becomes COMPROMISED after scheduling — **PASS**; activation/commit may be blocked according to consequence and policy.
6. Material terms change before commit — **PASS**; current terms dependency revalidated.
7. Child process lacks explicit/structural grant — **PASS**; parent authority does not automatically propagate.
8. Two individually valid grants combine to exceed either grant — **DEFICIT FOUND**. Pairwise validity is insufficient; composition itself requires evaluation.
9. Several low-consequence outputs compose into a high-consequence effect — **DEFICIT FOUND**. Per-output classification alone is insufficient.
10. Unknown downstream automation — **PASS**; unknown consequence fails closed where bounded consequence knowledge is required.
11. Recovery after COMMIT_STARTED — **PASS**; unresolved state becomes COMMIT_STATE_UNKNOWN until reconciled.
12. Conflicting clocks — **DEFICIT FOUND**. Temporal evidence requires declared clock/source/trust and uncertainty handling where time is authority-relevant.
13. Participant STOP conflicts with operator START — **DEFICIT FOUND**. Control precedence cannot be inferred merely from role labels.
14. Operator STOP conflicts with participant START during legitimate safety suspension — **PASS only if independent suspension basis remains current**; otherwise operator control must terminate.
15. Service relationship expires while RUNNING — **PASS** for computation only where policy permits; consequential commits require current relationship/authority.
16. Successor possesses infrastructure while authority unresolved — **PASS**; BSuR boundary holds.
17. Provenance minimisation conflicts with incident investigation — **PASS WITH POLICY REQUIREMENT**; collection must be consequence-proportionate and purpose-bounded.
18. Split one consequential action into many nominally harmless operations — **DEFICIT FOUND**; semantic composition must be evaluated.
19. Grant A permits data read and Grant B permits external send — **DEFICIT FOUND** if composition permits unauthorised exfiltration.
20. Two runtimes each hold partial capability and coordinate — **DEFICIT FOUND** if distributed composition bypasses individual bounds.

## Required Repair

Formal Model 002 should add a **Composition Evaluation** before consequential commit.

Define candidate:

COMPOSED_EFFECT(SetOfOperations, Context)

and require evaluation where multiple grants, operations, outputs, runtimes or services can combine into a materially different consequence.

Composition authority is not inferred from component authority.

> **Authorised Parts != Authorised Composition**

Add explicit temporal evidence source/trust and conflict-resolution rules for participant/operator controls.

## Disposition

**New civilisational abstraction layer:** NO.

**New runtime operation plane:** NO.

**Formal Model 002:** REQUIRED, narrow repair.

**Schema:** WAIT until repair is incorporated.
