# Post-Custody Restoration and Civil-Burden Remedy — Operational Architecture 001

**Project:** The Concord
**Domain:** Civil Security / Law / Judiciary / Historical / Civil Contact
**Date:** 3 October 2026
**Status:** ACTIVE DEVELOPMENT / POST-CUSTODY REMEDY ARCHITECTURE / PROVISIONAL / NON-CANONICAL

## 1. Purpose

This document operationalises the post-custody remedy requirement developed in:

- **Custody as a Protected Context — Rights Restriction, Review and Post-Release Remedy 001**
- **Custody as a Protected Context — Scenario Stress Test 001**

It reuses existing Concord architecture for:

- participant status and record correction;
- correction propagation;
- Historical provenance;
- Civil Contact notification;
- independent review;
- automatic entitlement recalculation.

The central rule is:

> **Release should initiate restoration and review; it should not merely open the door and leave the participant to discover and repair every consequence of custody alone.**

---

## 2. Source-resolved foundations

The existing **Participant Status, Record, Notification and Correction Loop 001** establishes:

- consequential participant-state changes should be communicated;
- participants should be able to inspect and contest consequential records;
- correction must propagate to known dependent decisions;
- the participant should not need to understand Concord's institutional topology to obtain correction;
- Civil Contact should route communication rather than become the decision authority;
- Historical preserves prior/current state and correction provenance;
- a historically true adverse state must not remain operationally current merely because it remains historically preserved;
- known correction should trigger known consequence reassessment.

The existing Historical participant-record architecture establishes:

**Historical Preservation != Permanent Civil Penalty**

and:

**Historical Custody != Universal Operational Authority**

These principles apply directly to custody release and remedy.

---

## 3. Two-stage post-custody architecture

Post-custody response should distinguish:

### Stage A — Restoration

Return the participant as far as reasonably possible to the ordinary civil state that should follow release.

This should begin automatically.

### Stage B — Civil-burden remedy

Identify material harms or losses that restoration alone cannot remove.

This may lead to:

- direct correction;
- practical support;
- replacement/reinstatement;
- service restoration;
- compensation;
- independent review;
- systemic correction.

Therefore:

**Restoration != Complete Remedy**

and:

**Compensation != First Remedy Where Direct Restoration Is Possible**

---

## 4. Release event

A formal release event should be a machine-readable civil state transition where appropriate:

**CUSTODY ACTIVE**
-> **CUSTODY AUTHORITY TERMINATED**
-> **RELEASED**

The event should identify:

- release time;
- custody authority that ended;
- restrictions derived solely from custody;
- restrictions, if any, claimed to continue under separate authority;
- property/status restoration requirements;
- post-custody review route;
- responsible originating domain.

This does not make Historical or Civil Contact the release authority.

The authorised custody function creates the operational state change.

---

## 5. Automatic dependency sunset

Release should trigger examination of known custody-derived dependencies.

Examples may include:

- detention status;
- movement restrictions;
- access restrictions;
- temporary credentials;
- facility/security classifications;
- custody-only communication restrictions;
- custody-derived service holds;
- custody-derived travel restrictions;
- property holds;
- temporary administrative markers.

Candidate rule:

> **Where a restriction derives solely from custody authority, termination of custody should trigger termination of that dependent restriction unless an independently valid authority state is recorded.**

Therefore:

**Parent Authority Sunset -> Dependent Authority Reassessment**

and:

**No Independent Basis -> Dependent Restriction Sunset**

This is an application of existing correction-propagation architecture.

---

## 6. Immediate restoration bundle

On release, the system should determine which restoration operations are already known and executable.

Candidate operations:

- physical release;
- return of property where no continuing hold exists;
- restore custody-suspended credentials/access;
- restore ordinary participant status;
- remove operational custody flags;
- recalculate dependent eligibility;
- restore interrupted ordinary services where appropriate;
- identify continuing restrictions and their independent authority;
- provide release/status documentation;
- expose relevant custody record through the legitimate participant-access route;
- preserve challenge/review routes.

Where the system already possesses the necessary information:

**Known Restoration Need -> Proactive Restoration**

The participant should not need to file separate applications for consequences Concord itself knows were created by custody.

---

## 7. Civil Contact notification

Civil Contact should provide a coherent post-release notice.

Candidate contents:

- confirmation that custody ended;
- effective release time;
- which custody-derived restrictions ended;
- which property/status/access has been restored;
- any restriction that continues and its separate stated basis;
- known restoration still in progress;
- post-custody review status;
- known automatic remedy/support;
- route to report additional loss or incomplete restoration;
- route to challenge custody/restriction legality;
- route to inspect relevant civil record.

Civil Contact communicates and routes.

**Civil Contact != Remedy Decision Authority**

The participant should be able to report simply:

> **Custody caused a loss or a restriction is still affecting me.**

The Concord should route the issue internally.

---

## 8. Automatic post-custody review trigger

A post-custody civil-burden review should be automatically opened for defined cases rather than depending entirely on participant application.

Candidate triggers include:

- release without charge/prosecution after custody;
- custody beyond a defined material duration;
- significant internal restriction;
- medical event;
- property loss/damage;
- authority defect;
- delayed release after authority sunset;
- repeated custody involving the same participant/system signal;
- known dependency-restoration failure;
- participant request.

Thresholds remain for Law.

A trivial custody/contact event need not generate disproportionate bureaucracy.

---

## 9. Review object

The post-custody review should distinguish four axes:

### Axis 1 — Custody legality

Was initial and continuing custody authorised?

### Axis 2 — Restriction legality

Were additional restrictions within custody independently justified?

### Axis 3 — Civil burden / harm

What actual loss or harm resulted from custody or its consequences?

### Axis 4 — System performance

Does the event reveal a recurring or structural problem?

The axes are related but independent.

**Lawful Authority != No Harm**

**Harm != Proof Of Unlawful Authority**

**No Individual Fault != No System Defect**

---

## 10. Baseline no-fault remedy

Where a participant is released without charge/prosecution after a materially significant custody event, a baseline remedy may be appropriate even where:

- custody was lawful;
- staff acted reasonably;
- no system defect is identified.

The rationale is burden allocation:

> **The participant bore a coercive civil burden for a wider protective function that did not progress to prosecution.**

The precise baseline may vary with:

- duration;
- severity of restriction;
- substrate-specific consequences;
- direct known disruption.

This document does not set monetary values.

Candidate principle:

**Material No-Prosecution Custody -> Presumptive Civil-Burden Review**

not:

**No Prosecution -> Automatic Finding Of Wrongdoing**

---

## 11. Consequential-loss layer

A baseline cannot represent all harms.

Additional review may consider evidenced consequential loss such as:

- lost income;
- replacement caregiving;
- missed education/training;
- cancelled travel;
- business interruption;
- property loss/damage;
- healthcare disruption;
- costs directly required to restore ordinary civil state;
- dependent-participant effects;
- service/credential disruption;
- other materially attributable loss.

Equal duration may create unequal consequence.

**Equal Custody Duration != Equal Consequential Harm**

The participant should be able to provide context without having to prove official misconduct.

---

## 12. Causation

Remedy should distinguish:

- loss directly caused by custody;
- loss caused by excessive/unlawful restriction;
- loss caused by delayed restoration;
- loss caused by independent events;
- loss materially increased by separate participant conduct;
- mixed causation.

Causation should not be used to relabel protected conduct as fault.

Specifically:

**Exercise Of Right To Silence != Participant-Caused Loss**

Where separate unlawful participant conduct materially causes additional loss, Law may recognise that causal contribution without extinguishing unrelated rights/remedies.

---

## 13. Restoration before monetisation

Where possible, repair the state rather than merely price the damage.

Examples:

**Incorrect operational marker**
-> correct marker + propagate correction

**Credential still suspended**
-> restore credential

**Property improperly retained**
-> return property

**Missed essential service**
-> restore/rebook/support access

**Incorrect external civil notification**
-> issue correction through appropriate authorised route

**Continuing dependent restriction**
-> terminate/reassess restriction

Compensation may address residual loss that cannot be directly restored.

Therefore:

**Correctable State Error -> Correct State**

not merely:

**Correctable State Error -> Payment While Error Persists**

---

## 14. Historical record handling

Historical should preserve:

- that custody occurred;
- authority/provenance;
- duration;
- restrictions;
- release;
- review;
- correction/remedy relationships;
- later findings.

It should distinguish:

- historically true custody event;
- current custody state;
- disputed authority;
- corrected record;
- superseded restriction;
- remedy completed;
- systemic finding where appropriately linked.

The custody event need not be erased merely because no prosecution followed.

But it must not remain operationally inculpatory merely because it is historically preserved.

**Historically True Custody != Current Adverse Status**

**Preserve Event != Preserve Penalty**

Where public/ordinary operational exposure would create unjustified stigma, access/display should follow the legitimate purpose and record class rather than treating historical existence as universal visibility.

---

## 15. Correction propagation

A custody correction or release update is incomplete until known dependent consequences are addressed.

Candidate loop:

**Release / Correction**
-> **Identify Known Dependencies**
-> **Recalculate Dependent States**
-> **Withdraw Stale Restrictions**
-> **Restore Eligibility / Access**
-> **Notify Participant**
-> **Historical Preserves Prior + Corrected State**

Existing Concord rule applies directly:

**Correction Without Propagation != Complete Correction**

This is especially important for automated civil systems.

---

## 16. Participant-facing simplicity

The participant should not need to determine whether a loss belongs to:

- Civil Security;
- Law;
- Judiciary;
- Historical;
- Economy;
- Health;
- Education;
- Social Support;
- another domain.

The existing rule should apply:

> **The Participant Identifies the Problem; Concord Routes the Correction.**

A single Civil Contact report should be capable of routing multiple linked consequences.

Example:

> I was released yesterday. My work credential is still disabled, my property has not been returned and I lost a paid shift.

The civilisation should decompose and route the issues internally.

---

## 17. Remedy states

Candidate operational states:

**RESTORATION PENDING**

Known custody-derived state has not yet been restored.

**RESTORATION COMPLETE**

Known directly restorable consequences have been addressed.

**CIVIL-BURDEN REVIEW OPEN**

Material residual harm is being assessed.

**BASELINE REMEDY ELIGIBLE**

Defined no-fault criteria are met.

**CONSEQUENTIAL LOSS REVIEW**

Additional participant-specific loss is being assessed.

**REMEDY OFFERED**

A remedy has been proposed but not necessarily accepted/completed.

**REMEDY COMPLETE**

Required/accepted remedy has been delivered.

**CONTESTED**

Participant disputes restoration, causation, remedy or authority.

**INDEPENDENT REVIEW**

Matter is before the relevant independent review/Judiciary route.

These are operational states, not moral labels.

---

## 18. Participant challenge

The participant should be able to challenge:

- release time/status;
- incomplete restoration;
- continuing restriction;
- custody record accuracy;
- causal assessment;
- remedy eligibility;
- consequential-loss assessment;
- remedy adequacy;
- denial;
- delay.

Administrative correction should be available where sufficient.

Independent/Judicial review should remain available where rights, authority or unresolved consequential disputes require it.

---

## 19. Remedy must not become coercive settlement

A remedy offer should not automatically require the participant to surrender:

- challenge to custody legality;
- complaint about treatment;
- systemic reporting;
- unrelated rights;
- access to independent review.

Any settlement/closure mechanism would require separate Law.

Candidate safeguard:

**Routine Civil-Burden Remedy != Purchase Of Silence Or Waiver Of Review**

---

## 20. Repeated-event escalation

Repeated custody/remedy involving:

- the same participant;
- same alert system;
- same location;
- same procedural delay;
- same evidence failure;
- same custodial restriction;
- same restoration failure,

should generate an appropriate system signal.

The signal should not itself establish wrongdoing.

It should trigger examination.

**Repeated Remedy Pattern -> System Reliability Signal**

This interfaces with Research, Metrics and relevant oversight.

---

## 21. Remedy funding and institutional incentives

The function that decides whether custody is justified should not gain operational benefit from denying remedy.

Likewise, remedy cost should not create pressure to avoid legitimate custody where genuinely required.

Institutional design should avoid:

- custody function marking its own remedy performance without review;
- budget incentives to under-compensate;
- compensation availability lowering custody thresholds;
- compensation cost suppressing legitimate protective action.

Candidate principle:

**Custody Authority Decision != Remedy Financial Incentive**

Exact institutional ownership remains for Economy/Law/Governance development.

---

## 22. Substrate neutrality

The remedy architecture must not assume all participants experience custody harm identically.

For a biological human, harms may include physical confinement, employment loss, caregiving or healthcare disruption.

For a digital/AI participant, analogous restrictions may include:

- compute restriction;
- network isolation;
- process suspension;
- memory/state access restriction;
- interruption of economic/service functions;
- loss of continuity;
- replica/instance restrictions;
- resource deprivation;
- reputational/status consequences.

For hybrid participants, both may apply.

Therefore:

**Same Legal Category != Same Substrate Consequence**

Remedy should assess the actual protected functions and losses affected.

---

## 23. Initial invariants

PCR-01 Release Should Initiate Restoration, Not Merely End Physical Confinement.  
PCR-02 Restoration != Complete Remedy.  
PCR-03 Compensation != First Remedy Where Direct Restoration Is Possible.  
PCR-04 Parent Authority Sunset -> Dependent Authority Reassessment.  
PCR-05 No Independent Basis -> Dependent Restriction Sunset.  
PCR-06 Known Restoration Need -> Proactive Restoration.  
PCR-07 Civil Contact != Remedy Decision Authority.  
PCR-08 Material No-Prosecution Custody -> Presumptive Civil-Burden Review.  
PCR-09 No Prosecution != Automatic Finding Of Wrongdoing.  
PCR-10 Lawful Authority != No Harm.  
PCR-11 Harm != Proof Of Unlawful Authority.  
PCR-12 Correctable State Error -> Correct State.  
PCR-13 Historically True Custody != Current Adverse Status.  
PCR-14 Preserve Event != Preserve Penalty.  
PCR-15 Correction Without Propagation != Complete Correction.  
PCR-16 Routine Civil-Burden Remedy != Purchase Of Silence Or Waiver Of Review.  
PCR-17 Repeated Remedy Pattern -> System Reliability Signal.  
PCR-18 Custody Authority Decision != Remedy Financial Incentive.  
PCR-19 Same Legal Category != Same Substrate Consequence.  
PCR-20 Remedy Offered != Remedy Complete.

---

## 24. Compact operational lifecycle

**Custody Authority Ends**
-> **Release Event**
-> **Automatic Dependency Scan**
-> **Immediate Restorable State Corrected**
-> **Civil Contact Notification**
-> **Historical Prior/Current State Updated**
-> **Automatic Post-Custody Review Trigger Test**
-> if material: **Civil-Burden Review**
-> **Baseline Remedy Assessment**
+ **Consequential Loss Assessment Where Needed**
+ **Legality/Restriction Review If Raised**
+ **System Signal If Indicated**
-> **Restoration / Support / Compensation**
-> **Participant Confirmation / Contestability**
-> **Correction Propagates**
-> **Historical Preserves Full Provenance**
-> **Case Remedy State Closes When Actually Completed**

---

## 25. Development conclusion

The Concord already contains most of the infrastructure required for a humane post-custody remedy system.

It does not need to create a separate adversarial compensation bureaucracy as the default.

Existing participant-state, Civil Contact, Historical, correction-propagation and review architecture can support:

> **automatic restoration of known consequences, proactive review of material no-prosecution custody, and participant-specific remedy for residual harm.**

The resulting principle is:

> **If the civilisation imposes a coercive burden for a legitimate civil purpose, the participant should not be left alone to discover, navigate and repair every resulting civil consequence after the authority ends.**

This does not make custody illegitimate.

It makes the civilisation responsible for the consequences of exercising legitimate coercive power.
