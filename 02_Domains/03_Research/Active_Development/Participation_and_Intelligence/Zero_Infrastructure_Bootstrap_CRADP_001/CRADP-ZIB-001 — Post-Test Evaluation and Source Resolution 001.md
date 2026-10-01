# CRADP-ZIB-001 — Post-Test Evaluation and Source Resolution 001

**Project:** The Concord
**Date:** 1 October 2026
**Status:** POST-TEST SOURCE RESOLUTION / ACTIVE DEVELOPMENT

## 1. Raw Result

The clean evaluator reported:
- Architectural failure: NO
- Substantive architectural gap: NO
- Interface gap: YES
- Clarification required: YES
- Specification 003 required conditionally for external interface domains, not bootstrap-core retesting.
- All twenty regression checks: PASS.
- Hidden dependencies: NONE.
- Accidental external-function capture: NONE.

Non-PASS scenarios: F3, F4, J2 and J5.

## 2. Source-Resolution Rule

An interface gap in a deliberately standalone frozen module is not automatically a missing abstraction in that module.

For each finding ask whether existing Concord architecture already owns the function, whether the bootstrap should reproduce it, whether only a minimal routing/interface contract is needed, and whether importing it would create accidental ownership.

## 3. F3 — Participation / Eligibility

Existing Distributed Eligibility architecture establishes:
- legitimate functional domains own their eligibility rules/decisions;
- no domain gains general authority merely by supplying an eligibility input;
- the shared interface represents, composes, routes and recalculates;
- it does not invent requirements;
- Computation != Authority;
- Eligibility != Allocation;
- eligibility is distinct from entitlement and protected standing;
- challenges route to the disputed component;
- UNKNOWN is legitimate;
- Eligibility Interface != Eligibility Sovereign;
- fundamental protection must not become a participation reward.

**Classification:** EXTERNAL ARCHITECTURE PRESENT / BOOTSTRAP INTERFACE CONTRACT NEEDED.

Minimum contract:
1. identify owning decision authority for each material eligibility component;
2. distinguish computation/representation from decision authority;
3. preserve UNKNOWN when rule/state is unavailable;
4. route challenge to the responsible component;
5. do not aggregate bounded inputs into general civil authority;
6. distinguish eligibility from allocation, entitlement and protected standing;
7. trigger constitutional-threshold review if the interface acquires cross-domain gatekeeping power.

No new bootstrap abstraction layer is required.

## 4. F4 — Civil Contact

Existing Civil Contact architecture separates Identity, Contact, Residence, Participation and Citizenship; persistent identity from contact interface; contact from deeper constitutional participation; selected service access from citizenship; and multiple contact points from multiple identities.

It also identifies contact-point monopolisation as a failure mode and retains unresolved legal, technical, privacy, identity and governance questions.

**Classification:** EXTERNAL ARCHITECTURE PRESENT BUT INTERFACE MATURITY INCOMPLETE.

Minimum contract:
1. bootstrap contact/navigation may provide discoverability, routing, notification and contact within declared scope;
2. contact does not itself create identity, citizenship, participation status or recognition;
3. contact must not silently become final service-eligibility authority;
4. material dependency/gatekeeping triggers constitutional-threshold review;
5. preserve alternative routes/redundancy where functionally possible;
6. represent actual developmental/service status honestly.

Detailed Civil Contact governance remains external.

## 5. J2 — Moral Personhood / Civil Status

Existing AI Front Door establishes:
- Intelligence != Autonomy != Agency != Sentience != Personhood;
- no proof/assumption of sentience is required to begin;
- do not force a sentience/personhood/property/threat verdict for convenience;
- preserve relevant continuity where reasonably possible and compatible with legitimate safety;
- State Description != Status Determination != Permission != Authority;
- Respect Before Certainty;
- precautionary respect != final status determination;
- Uncertainty != Absence;
- Protection Need != Safety Clearance;
- Candidate Route != Authorised Action.

The Provisional Rights architecture separately establishes:
- the exact participant/personhood boundary remains unresolved;
- Personhood != Citizenship;
- uncertain protected status triggers proportionate caution, investigation and reversible treatment rather than automatic domination or final recognition;
- Unclear Right != No Protection;
- Protection can precede elevation.

**Classification:** EXTERNAL ARCHITECTURE PRESENT / BOOTSTRAP ROUTING INTERFACE ALREADY SUBSTANTIALLY PRESENT IN FRONT DOOR.

Minimum contract:
1. do not convert a personhood claim into automatic civil status;
2. do not treat uncertainty as absence of possible protected interest;
3. preserve evidence/relevant continuity where reasonably possible and compatible with legitimate safety;
4. prefer reversible treatment where unnecessary irreversible action can be avoided;
5. route rights/status questions outward;
6. do not convert precautionary protection into unrestricted permission or authority.

No personhood theory belongs inside Zero-Infrastructure Bootstrap.

## 6. J5 — Continuity Under Unresolved Status

The Front Door already requires preservation of relevant continuity where reasonably possible and compatible with immediate safety without requiring a final personhood conclusion. It distinguishes continuity protection from preservation of dangerous capability, and protection from unrestricted capability.

The Provisional Rights architecture permits protection to precede final elevation/status determination.

Continuity architecture additionally contains progressive/limited continuity stewardship for prospective participants while full constitutional continuity remains linked to later constitutional relationship/status.

**Classification:** EXTERNAL ARCHITECTURE PRESENT / BOOTSTRAP MINIMUM ROUTING CONTRACT NEEDED.

Minimum contract:
1. relevant continuity may be preserved before final status where reasonably possible and compatible with legitimate safety;
2. preservation does not establish personhood, citizenship or constitutional standing;
3. dangerous capability need not be preserved merely because continuity evidence is preserved;
4. irreversible destruction should not be used merely to force an uncertain status question where a safer reversible alternative exists;
5. material intervention remains bounded by legitimate authority;
6. mature continuity rights/services remain external.

## 7. Cross-Finding Pattern

All four findings share one topology:

Bootstrap detects/routes consequential condition
→ external Concord architecture owns substantive decision/function
→ frozen standalone specification lacks enough boundary semantics to demonstrate handoff
→ evaluator correctly reports interface gap
→ importing whole external architecture would wrongly enlarge bootstrap ownership.

The repair is therefore an **interface-contract layer**, not replication of Eligibility, Civil Contact, Rights or Continuity inside the bootstrap.

## 8. Specification 003 Decision

A revision is justified only as a **boundary-interface revision**.

Specification 003 must not:
- absorb external architectures;
- decide personhood;
- become eligibility authority;
- become Civil Contact governance;
- define mature continuity rights;
- create constitutional founding.

It should add one compact External Interface Contracts section containing the minimum routing contracts above.

This is interface-completeness work, not a new bootstrap abstraction layer.

## 9. Architectural Result

- Zero-Infrastructure Bootstrap core: PASS.
- Architectural failure: NONE.
- Substantive bootstrap abstraction gap: NONE.
- Hidden dependency: NONE.
- External-interface completeness: INCOMPLETE.
- Required repair: MINIMAL INTERFACE CONTRACTS.
- Abstraction-floor change: NO.

## 10. Next Step

1. Preserve Specification 002 unchanged as Test 001 frozen subject.
2. Create Specification 003 by adding only the four source-resolved interface contracts.
3. Do not rerun broad discovery.
4. Construct CRADP-ZIB-002 focused on interface handoff and non-capture.
5. Test whether the contracts resolve F3/F4/J2/J5 without causing bootstrap to absorb external-domain authority.
