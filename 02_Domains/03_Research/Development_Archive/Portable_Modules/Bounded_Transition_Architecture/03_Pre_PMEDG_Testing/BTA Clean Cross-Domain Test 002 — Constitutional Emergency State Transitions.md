# BTA Clean Cross-Domain Test 002 — Constitutional Emergency State Transitions

**Author:** Alexander C. Blainey — Independent Researcher  
**Project:** The Concord Framework  
**Framework Version:** Concord V1.3  
**Status:** ACTIVE DEVELOPMENT / CLEAN CROSS-DOMAIN TEST / NON-CANONICAL  
**Date:** September 2026

# 1. Test purpose

This test applies Bounded Transition Architecture 002 to a developed Concord architecture that was not used to derive BTA 002:

`03_Cross_Domain_Architecture/Constitutional_Emergency/Constitutional Emergency V2.md`

The test does not modify Emergency V2 to make it fit BTA.

The question is:

> Can BTA 002 represent consequential emergency transitions coherently while leaving emergency legitimacy, necessity, proportionality, authority, review and recovery semantics with Constitutional Emergency?

# 2. Why Constitutional Emergency is a strong clean test

Emergency architecture contains multiple consequential transitions:

- ordinary condition → emergency recognition;
- recognition → classification;
- classification → individual power activation;
- lower → higher emergency level;
- higher → lower emergency level;
- emergency authority → expiry/renewal;
- emergency operation → recovery;
- temporary restriction → rights restoration;
- emergency governance → ordinary governance;
- temporary secrecy → review/disclosure;
- degraded institution → restoration.

These transitions are high-consequence, authority-sensitive, time-sensitive and often asynchronous.

They therefore provide a demanding test of BTA without reusing Infrastructure, Enterprise, Genomics or CSHP as the test domain.

# 3. Source-domain rules BTA must not replace

Emergency V2 already establishes:

- emergencies change operational priorities, not constitutional principles;
- emergency authority does not create sovereignty;
- crisis does not manufacture authority;
- minimum constitutional deviation;
- necessity and proportionality;
- automatic expiry unless continuation is justified;
- modular rather than general emergency authority;
- each consequential emergency power requires separate justification;
- escalation requires justification;
- de-escalation is obligatory when justification weakens;
- review remains active;
- recovery/restoration is a constitutional phase;
- ordinary governance is the default.

BTA must preserve references to these rules without becoming their owner.

# 4. Test A — declaration must not propagate into power activation

Emergency V2 explicitly distinguishes:

**Emergency Recognition**
from
**Emergency Classification**
from
**Emergency Power Activation**.

It also states that emergency classification does not activate a package of powers; each consequential authority requires separate justification.

This maps directly to BTA non-propagation.

Candidate transition sequence:

`T1: OrdinaryCondition → EmergencyRecognised`

`T2: EmergencyRecognised → EmergencyClassified(Level)`

`T3a: PowerA(INACTIVE) → PowerA(ACTIVE)`

`T3b: PowerB(INACTIVE) → PowerB(ACTIVE)`

`T3c: PowerC(INACTIVE) → remains INACTIVE`

All may relate to the same emergency event, but completion of T1 or T2 does not complete T3a–c.

Required BTA rule:

> **Emergency Classification != Emergency Power Activation.**

This is an instance of:

> **Transition of One State Dimension != Transition of Every Attached Authority State.**

**RESULT: PASS.**

BTA represents the relationship without inventing emergency authority.

# 5. Test B — asynchronous emergency-power states

Suppose a Level III emergency exists.

At time t:

- evacuation authority = ACTIVE;
- temporary hazardous-zone access restriction = ACTIVE;
- emergency procurement authority = ACTIVE;
- extraordinary data-access authority = EXPIRED;
- temporary secrecy = ACTIVE_PENDING_REVIEW;
- ordinary judiciary = DEGRADED_BUT_ACTIVE;
- one regional emergency declaration = UNDER_REVIEW.

A scalar state such as `EMERGENCY_ACTIVE` loses important constitutional information.

BTA 002 can bind these scoped states to the emergency transition without flattening them.

> **Emergency State != Uniform State of Every Emergency Function.**

**RESULT: PASS.**

This independently validates asynchronous multidimensional completion.

# 6. Test C — sunset and renewal

Emergency V2 establishes automatic expiry and requires renewed justification for continuation.

Consider:

`Power P = ACTIVE`

`Sunset reached`

`Renewal review = PENDING`

The unsafe inference would be:

`Emergency still exists → P remains active`.

BTA non-propagation and protected unresolved consequence prevent this.

Correct state can be:

`P = EXPIRED / INACTIVE_PENDING_NEW_AUTHORITY`

while:

`Emergency classification = ACTIVE`.

Renewal, if legitimate, is a new authority-bearing transition rather than silent continuation.

> **Persistence of Emergency Condition != Persistence of Every Emergency Authority.**

**RESULT: PASS.**

# 7. Test D — escalation

Emergency V2 states that higher emergency level does not equal higher sovereignty and that escalation should trigger review of relevant powers.

Consider:

`Level II → Level III`

The unsafe transition would propagate:

`Level increased → all Level III-associated powers active`.

BTA requires separate TransitionBasisRefs/authority references and completion conditions for each consequential activation.

Therefore the level transition can complete while several power-activation transitions remain inactive or pending.

> **Emergency-Level Escalation != Automatic Authority Expansion.**

**RESULT: PASS.**

# 8. Test E — de-escalation

Suppose:

`Emergency Level III → Level II`

At the same time:

- one movement restriction should terminate;
- a remediation function remains active;
- judicial review of prior emergency actions continues;
- emergency-collected data enters post-crisis review;
- one secrecy restriction remains temporarily justified;
- recovery assistance remains active.

BTA represents the level transition separately from surviving duties and other state transitions.

> **De-Escalation != Instantaneous Termination of Every Emergency-Related Function.**

But equally:

> **Surviving Recovery or Review Function != Surviving Emergency Sovereignty.**

**RESULT: PASS.**

This validates the distinction between surviving duty/function and surviving authority.

# 9. Test F — transition to recovery

Emergency V2 treats recovery as a constitutional phase and states that recovery begins during response.

Therefore:

`Emergency Response → Recovery`

is not necessarily an instantaneous replacement.

Response and recovery may overlap.

Some emergency powers may terminate while:

- rights restoration is incomplete;
- judiciary restoration is active;
- infrastructure restoration is active;
- emergency-data review is pending;
- compensation/remedy processes remain active;
- Historical preservation/review continues.

BTA 002 represents this as partially ordered/scoped transition rather than forcing:

`EMERGENCY → RECOVERY → NORMAL`

as one universal linear state machine.

**RESULT: PASS.**

This independently supports BTA's decision not to universalise CSHP's linear Transition Epoch.

# 10. Test G — return to ordinary governance

Emergency V2 makes ordinary governance the constitutional default.

Suppose formal emergency authority terminates.

That does not prove:

- all rights are practically restored;
- all institutions have recovered;
- all emergency data has been dispositioned;
- all secrecy has been reviewed;
- all emergency cases have received remedy;
- all infrastructure has recovered.

BTA therefore must distinguish:

`FormalEmergencyAuthority = TERMINATED`

from

`RecoveryCompletion = PENDING`.

> **Termination of Emergency Authority != Completion of Recovery.**

**RESULT: PASS.**

# 11. Test H — failed emergency transition

Consider an attempted emergency power activation where:

- operational instructions are issued;
- some actors begin compliance;
- judicial review then finds activation invalid or insufficiently justified;
- authority is withdrawn.

Representing the activation merely as `FAILED` would lose consequences already created.

BTA preserves:

- attempted activation;
- partial execution;
- affected actions;
- authority withdrawal;
- review decision reference;
- remedy/recovery references;
- provenance.

> **Invalidated or Withdrawn Emergency Action != No Emergency Transition History.**

**RESULT: PASS.**

# 12. Test I — rollback/restoration

Emergency restrictions are lifted.

That does not automatically restore the exact pre-emergency state.

Examples:

- business/activity losses already occurred;
- data was collected;
- detention occurred;
- institutional procedures were delayed;
- infrastructure was damaged;
- trust may have changed;
- secrecy records remain;
- precedents require review.

BTA correctly treats lifting a measure as another transition and does not infer prior-state equivalence.

> **Removal of an Emergency Restriction != Restoration of the Pre-Emergency World State.**

**RESULT: PASS.**

# 13. Test J — BTA ownership boundary

Does applying BTA require BTA to decide:

- whether an emergency exists? **NO**;
- what level applies? **NO**;
- whether a power is necessary? **NO**;
- whether it is proportionate? **NO**;
- who possesses constitutional authority? **NO**;
- whether renewal is justified? **NO**;
- whether rights restriction is lawful? **NO**;
- whether recovery is substantively complete? **NO**.

BTA only binds and preserves the scoped transition states and their references.

**RESULT: PASS.**

This is important evidence that the reduced BTA kernel can transfer without absorbing the clean-test domain.

# 14. Example BTA record

Illustrative only:

`TransitionID = EMERGENCY-DEESCALATION-001`

`ObjectOrFunctionRefs = <EmergencyClassification, PowerSetRefs, RecoveryFunctions>`

`Scope = affected jurisdiction/context`

`ParticipatingStateSystemRefs = <ConstitutionalEmergency, Judiciary, Governance, Rights, Historical, relevant domains>`

`PriorValidStateRefs = <LevelIII, active scoped powers>`

`TransitionBasisRefs = <evidence review, de-escalation authority>`

`TransitionStateRefs = <LevelIII→LevelII=COMPLETED, PowerA→EXPIRED=COMPLETED, PowerB→TERMINATING=PENDING, RecoveryFunction=ACTIVE>`

`PendingStateRefs = <rights restoration, case review, data review, recovery>`

`NonPropagationRules = <LevelChange !→ automatic power state, AuthorityExpiry !→ DutyExpiry>`

`CompletionConditionRefs = domain-owned`

`ProtectedUnresolvedStateRefs = domain-owned`

`SurvivingDutyRefs = <review, remedy, recovery, provenance>`

`TerminatedAuthorityRefs = <expired emergency powers>`

`NextStateRefs = scoped states`

`Provenance = emergency decision/review records`

BTA does not determine any of the substantive emergency decisions represented above.

# 15. New finding — authority contraction is itself multidimensional

The clean test exposes a useful refinement.

During de-escalation, authority can contract faster than responsibility, recovery or review functions.

Therefore:

> **Authority Contraction != Responsibility Contraction.**

This is consistent with the existing BTA invariant:

> **End of Authority != Automatic End of Responsibility.**

but Emergency V2 demonstrates it dynamically across a transition rather than only at an endpoint.

No new BTA field is required.

# 16. New finding — transition completion can be intentionally asymmetric

Emergency architecture also shows that asymmetry is not always a defect.

For example:

- emergency power termination may be immediate;
- rights restoration may require active remediation;
- accountability review may continue much longer;
- Historical preservation may be indefinite;
- ordinary governance authority may already be restored.

Therefore BTA must not assume that coherent completion means all state systems converge to the same status at the same time.

> **Transition Coherence != Synchronous Completion.**

This should be added as a BTA invariant.

# 17. ESCP observation

A clean emergency record could populate every BTA field correctly while still omit a materially relevant emergency consequence not represented by participating systems.

Therefore the test does not weaken the ESCP boundary.

> **Correct BTA Integration != Proof That Every Emergency-Relevant Dimension Was Represented.**

No additional BTA subsystem is required.

# 18. Test outcome

**PASS — BTA 002 TRANSFERS TO A CLEAN HIGH-CONSEQUENCE DOMAIN.**

No new BTA-owned subsystem was required.

The clean test independently supports:

- scoped multidimensional state;
- asynchronous completion;
- non-propagation;
- protected unresolved consequence;
- surviving duties after authority termination;
- failed/partial transition provenance;
- rollback/restoration distinction;
- domain ownership boundaries.

The principal refinement is an additional invariant:

> **Transition Coherence != Synchronous Completion.**

# 19. Development implication

BTA 002 does not need structural expansion as a result of this clean test.

The next appropriate step is:

1. add the new invariant to BTA 002;
2. run the machine-readable transfer test;
3. then perform the interface-boundary audit and materiality test;
4. only after those tests consider PMEDG candidacy.