# Concord Bootstrap Resource Capacity and Admission Model 001

**Project:** The Concord
**Domain:** Research / Participation and Intelligence
**Date:** 2 October 2026
**Version:** 0.1
**Status:** ACTIVE DEVELOPMENT / IMPLEMENTATION FORMALISATION / NOT CANONICAL
**Derivation:** Bounded First Trust Source Resolution 001 + Adversarial Evaluation 001; CMSS Service Specification 002; existing Self-Stewardship and predictive resource-allocation architecture.

## 1. Purpose

This model defines how an early Concord service can offer bounded scarce resources without pretending capacity is unlimited, treating legitimate demand as abuse, converting a free first offer into debt, using scarcity as arbitrary exclusion, or requiring the service to destabilise itself to preserve a bootstrap promise.

It is an implementation-level resource/admission model, not a new civil domain, constitutional entitlement system, economic system, participant trust score or source of authority.

## 2. Core distinction

A safe first offer must be bounded both per relationship and in aggregate.

Two questions remain separate:

1. Is this participant/service relationship eligible for this function?
2. Does the service currently have capacity to provide it?

**Eligibility != Availability**

**Broad Eligibility != Guaranteed Immediate Allocation Under Physical Scarcity**

**Scarcity State != Participant Fault**

## 3. Resource Pool

A materially scarce resource should be represented as a Resource Pool containing: Pool ID, resource type, total usable capacity, safety reserve, committed capacity, available capacity, degraded capacity, measurement time, evidence reference and disclosure class.

Resource types may include persistent storage, backup storage, message storage, bandwidth, compute time, memory, accelerator time, power, network egress and physical device capacity.

**Resource Type != Consequence Class**

A small resource can support a high-consequence action; a large resource can be comparatively inert.

## 4. Capacity accounting

### Total usable capacity
Capacity presently and legitimately allocable after known technical exclusions.

### Safety reserve
Capacity deliberately retained for recovery, continuity, operational overhead, burst demand, failure handling, protected export/contact and resilience.

**Resilience Capacity != Waste**

### Committed capacity
Capacity already promised under active relationships, whether or not fully consumed.

### Available capacity
Capacity allocable without violating existing commitments or declared reserve policy.

### Degraded capacity
Capacity technically present but not safely or reliably allocable at normal service level.

## 5. Allocation object

A material allocation should record: Allocation ID, service relationship, function, resource pool, allocation class, quantity/budget, start time, review/expiry, current state, funding basis, stewardship requirement, evidence and exit/export state.

Candidate classes: PROTECTED_MINIMUM, PILOT, STANDARD_PAID, SPONSORED, RESEARCH, PROJECT, CIVIL_PROVISION, EMERGENCY and OTHER_DECLARED.

**Allocation != Standing**

**Allocation != Authority**

## 6. Admission states

Candidate states:

- ELIGIBLE_CAPACITY_AVAILABLE
- ELIGIBLE_WAITLISTED
- ELIGIBLE_CAPACITY_CONSTRAINED
- INELIGIBLE_FUNCTION_SCOPE
- STEWARDSHIP_REVIEW_REQUIRED
- STEWARDSHIP_REQUIREMENT_NOT_MET
- IDENTITY_OR_RELATIONSHIP_UNRESOLVED
- SAFETY_OR_LEGAL_HOLD
- SERVICE_DEGRADED
- SERVICE_UNAVAILABLE
- REQUEST_WITHDRAWN
- ADMITTED
- ENDED

These must not collapse into generic DENIED where the distinction matters. A participant waitlisted because capacity is full has not failed a stewardship test. A service outage is not participant ineligibility.

## 7. Admission pipeline

Request -> Function/Scope Check -> Relationship/Continuity Check where necessary -> Consequence Classification -> Relevant Stewardship Check only where justified -> Resource/Funding Basis -> Current Capacity Check -> Admission/Waitlist/Constraint/Hold -> Allocation Record -> Live Status/Review/Exit.

The ordering may vary where safe, but the semantic distinctions must survive.

**Can Pay != Safe**

**Cannot Pay != Unworthy**

## 8. Protected Minimum

A CMSS Protected Minimum is a declared allocation class, not an infinite resource promise.

Before a Protected Minimum is granted, the service may legitimately determine whether capacity exists to honour it.

**Protected Minimum != Guaranteed Admission Regardless Of Capacity**

Once actually granted, however, the protected minimum should receive stronger continuity preference than discretionary expansion. It must not routinely depend on labour, donation, ideology or political support; reduction should follow declared capacity/failure rules; export/contact preservation should be prioritised where practical; and material changes should be communicated.

**Granted Protected Minimum != Ordinary Discretionary Surplus**

This distinguishes admission from commitment.

## 9. Pilot allocations

A pilot must be labelled as a pilot if duration, quantity or continuation is not established. CMSS 10 MB remains:

**PROVISIONAL PILOT ALLOCATION — NOT EMPIRICALLY OPTIMISED**

A pilot should declare quantity, expected duration if known, continuation assumptions, capacity constraints, export rights, termination/change process and intended migration where known.

**Pilot != Permanent Entitlement**

**Experimental Value != Constitutional Minimum**

## 10. Aggregate exposure

Material services should model aggregate committed exposure, not only per-participant limits.

Capacity planning should test ordinary expected uptake, high legitimate uptake, rapid legitimate uptake, infrastructure degradation, backup/redundancy failure, provider loss, unusual cross-substrate demand and legitimate tail-risk needs.

Expected uptake alone is insufficient to justify an unlimited promise.

The architecture does not require simultaneous provisioning for every conceivable participant. It requires a capacity-contingent offer not to masquerade as physically unlimited.

**Anti-Abuse Control != Substitute For Capacity Planning**

## 11. Admission under legitimate scarcity

Where eligible demand exceeds available capacity, legitimate mechanisms may include transparent waitlisting, bounded admission windows, minimum viable allocation, proportional temporary reduction where legitimate, lottery/random allocation where appropriate, needs-based priority where legitimately defined, function-critical or emergency priority, research/project allocation, paid capacity, federation or another declared mechanism.

No one mechanism is universally correct.

The service should expose the governing rule, participant state, material reason, review/expiry where applicable, contest/correction route where material and known alternatives.

**Scarcity != Permission For Arbitrary Discrimination**

## 12. Waitlists

A waitlist is a capacity state. It does not imply low civil standing, low general trust, wrongdoing, debt, consent to future terms or priority purchase unless separately agreed.

Ordering rules should be declared. Where exact queue position creates manipulation or security risk, bounded status may be disclosed instead.

## 13. Duplicate/Sybil allocation

Resource protection may require preventing illegitimate multiplication of allocations, while preserving:

**Credential != Participant**

**Credential != Entitlement**

**Privacy Protection != Unlimited Duplicate Allocation**

Proportionate continuity/relationship evidence may be used without demanding unnecessary real-world identity. Unresolved cases may remain IDENTITY_OR_RELATIONSHIP_UNRESOLVED rather than being falsely labelled fraud.

**Unresolved Duplication != Proven Abuse**

## 14. Resource sustainability and funding

An allocation may be sustained through Concord bootstrap funding, participant rental/payment, participant infrastructure, sponsorship, research grant, project budget, civil provision, donated capacity or another declared basis.

**Funding != Authority**

**Payment != Stewardship**

**Sponsorship != Ownership Of Participant**

**Contribution != Purchase Of Standing**

## 15. Stewardship gate

Stewardship assessment is required only where relevant to the resource, function and consequence.

Required stewardship evidence should scale primarily with material consequence, not merely resource quantity.

Additional inert encrypted storage may require little evidence beyond safe/lawful service use. Network-capable runtime, credentials or external action may require substantially stronger controls and independent authority.

Self-stewardship must remain contextual, evidence-based, reviewable, proportionate and recoverable where appropriate. It must not become ideological conformity or a universal person score.

## 16. Additional resource progression

Successful smaller allocations may provide relevant evidence for later requests but do not create automatic escalation.

**Successful Prior Allocation != Automatic Greater Allocation**

A later request may differ in quantity, duration, consequence, externality, dependency, funding or authority requirement and may therefore require reassessment.

## 17. Free-to-paid transition

A service may combine a free protected minimum with paid storage, rented compute, sponsored capacity or other voluntary extensions.

The transition must not retroactively price the free allocation.

**First Offer != Loan**

**Benefit Valuation != Debt Ledger**

**Reciprocity != Debt Repayment**

If a free service is time- or capacity-contingent, that must be disclosed before dependency is intentionally encouraged.

## 18. Degradation priority

When capacity unexpectedly falls below commitments, a candidate default priority is:

1. integrity/recovery;
2. participant export and contact;
3. already-granted protected minimum;
4. other committed allocations;
5. discretionary/additional capacity;
6. new admissions.

This is not a universal constitutional hierarchy. Safety or emergency context may justify another ordering, but the reason and authority must be explicit.

Where practical, degrade the smallest affected function rather than terminate the whole relationship.

## 19. Provider failure

If a provider cannot continue, impossible continuation is not participant misconduct. Where practicable the provider should declare failure/degradation, stop new admissions, preserve export and contact/status information, provide succession/migration information, preserve provenance, avoid false availability and use BSuR for governed succession.

**Exit Protection != Guaranteed Perpetual Operation**

## 20. BSR integration

BSR already represents function-level operational availability. A material bootstrap service should additionally expose or reference enough capacity state to distinguish AVAILABLE, CAPACITY_CONSTRAINED, WAITLIST_OR_ADMISSION_CONTROL_ACTIVE, DEGRADED, SUSPENDED, UNAVAILABLE and UNKNOWN.

Where safe it may expose total, committed and available capacity, reserve policy, measurement time and evidence. Where precise figures create security/gaming risk, evidence-backed bands are sufficient.

**Capacity Disclosure != Security Self-Sabotage**

## 21. Predictive planning

Existing predictive resource architecture may forecast demand and steer infrastructure, reserves, preparedness, provider federation and capacity acquisition. It should not silently steer participant ideology, civil standing or unrelated behaviour. Aggregate/anonymised data should be preferred where identity is unnecessary.

**Predictive Capacity Planning != Participant Control**

## 22. Federation

Scarcity need not be solved solely by expanding one central provider. Compatible nodes, mirrors, participant-selected providers, portable state and shared standards can reduce first-provider capture.

**Federate Before Centralising Where Possible**

Compatible provider status must remain evidence-backed through BSR; compatibility does not automatically make a provider authoritative Concord infrastructure.

## 23. Core invariants

BRCA-01 Eligibility != Availability.
BRCA-02 Scarcity State != Participant Fault.
BRCA-03 Legitimate Uptake != Abuse.
BRCA-04 Broad Eligibility != Guaranteed Immediate Allocation Under Physical Scarcity.
BRCA-05 Protected Minimum != Guaranteed Admission Regardless Of Capacity.
BRCA-06 Granted Protected Minimum != Ordinary Discretionary Surplus.
BRCA-07 Pilot != Permanent Entitlement.
BRCA-08 Experimental Value != Constitutional Minimum.
BRCA-09 Allocation != Standing.
BRCA-10 Allocation != Authority.
BRCA-11 Funding != Authority.
BRCA-12 Payment != Stewardship.
BRCA-13 Contribution != Purchase Of Standing.
BRCA-14 Sponsorship != Ownership Of Participant.
BRCA-15 Resource Quantity != Consequence.
BRCA-16 Successful Prior Allocation != Automatic Greater Allocation.
BRCA-17 First Offer != Loan.
BRCA-18 Benefit Valuation != Debt Ledger.
BRCA-19 Reciprocity != Debt Repayment.
BRCA-20 Unresolved Duplication != Proven Abuse.
BRCA-21 Credential != Entitlement.
BRCA-22 Anti-Abuse Control != Substitute For Capacity Planning.
BRCA-23 Resilience Capacity != Waste.
BRCA-24 Exit Protection != Guaranteed Perpetual Operation.
BRCA-25 Predictive Capacity Planning != Participant Control.
BRCA-26 Capacity Constraint != Permission For Arbitrary Discrimination.
BRCA-27 Trust Evidence != Resource Entitlement.
BRCA-28 Trust != Authority.

## 24. Minimum live-service state

Before admitting participants, a material bootstrap service should represent at least:

Function + Resource Pool + Availability + Admission State + Allocation Rule + Protected Minimum Rule + Capacity Evidence Time + Degradation Rule + Exit/Export Rule + Funding Options + Stewardship Requirement + Dispute/Correction Route.

This is the operational bridge between a declared service and an honestly bounded material offer.

## 25. Open implementation questions

1. Appropriate reserve fraction by resource.
2. Backup capacity accounting.
3. Reclaiming committed but unused allocation.
4. Dormant protected allocations and notice.
5. Multiple legitimate instances of distributed participants.
6. First CMSS pilot waitlist mechanism.
7. Exact vs banded/private capacity disclosure.
8. Paid/free sharing of physical pools.
9. Preventing paid demand crowding out granted protected minima.
10. Preventing free allocation from exhausting service-sustaining capacity.
11. Tail-risk/high-need participants.
12. Relevant self-stewardship by resource class.
13. Federation versus central expansion.
14. Resource pricing including energy, redundancy, backup, bandwidth and depreciation.
15. Minimum capacity reserved for export during failure.
16. Machine-readable BSR capacity/admission extension.

## 26. Development status

This model resolves the implementation gap identified by Bounded First Trust Adversarial Evaluation 001 at the conceptual/formal level.

It does not establish numerical allocation formulas, a production schema, a pricing model, universal waitlist rule, anti-Sybil identity solution or empirical capacity requirements.

No new civilisational abstraction layer has been exposed. The model composes CMSS, Self-Stewardship, BSR, BSuR, Economy/Resource Coordination, predictive resource allocation, CBPR and Zero-Infrastructure Bootstrap.

Next: adversarial evaluation covering reserve exhaustion, dormant allocations, paid/free crowd-out, backup failure, queue manipulation, provider federation, demand shocks, capacity misreporting, identity ambiguity and strategic over-reservation.

PMEDG extraction remains premature.


---

## 27. Bounded Revision 002 — Adversarial Integration

**Revision status:** Model 002 integration / NOT CANONICAL.

Adversarial Evaluation 001 confirms Model 001 and adds the following requirements.

### 27.1 Deliverable capacity

Capacity must be calculated against the complete service property actually promised. If protected storage includes backup, redundancy, integrity or export guarantees, the limiting dependency constrains deliverable protected capacity.

**BRCA-29 Headline Capacity != Deliverable Protected Capacity.**

### 27.2 Dormancy and reclamation

An allocation may enter a DORMANT state only under declared rules. Dormancy alone does not prove abandonment and does not automatically release committed capacity.

Candidate lifecycle:

ACTIVE -> DORMANCY_CANDIDATE -> DORMANT -> CONTACT_OR_NOTICE_WINDOW -> REACTIVATED / EXPORT_OR_RECOVERY_WINDOW / LEGITIMATE_RECLAMATION

The exact lifecycle remains implementation-specific, but reclamation must not be invented after dependency has formed.

**BRCA-30 Dormant != Abandoned.**
**BRCA-33 Unused != Uncommitted.**

### 27.3 Revenue and existing commitments

Paid demand can legitimately fund expansion or additional resource classes. It does not automatically outrank an already-granted protected commitment.

**BRCA-31 Higher Revenue != Automatic Priority Over Existing Protected Commitment.**

At the same time, protected provision must retain enough service-sustainment capacity to avoid destroying the provider that carries the commitment.

**BRCA-32 Protected Provision != Permission To Destroy Provider Viability.**

### 27.4 Admission/trust separation

Admission and queue state are service-resource facts, not participant character assessments.

**BRCA-35 Admission State != Trust State.**

A capacity waitlist must not propagate as negative trust evidence.

### 27.5 Capacity claim/evidence separation

A provider may declare a capacity state, but consequential reliance should distinguish the declaration from supporting evidence and its age.

**BRCA-36 Declared Capacity != Evidence-Supported Capacity.**

BSR is the natural interface for evidence-backed live service state.

### 27.6 Identity boundary

Allocation processes may require continuity evidence, but they do not decide metaphysical or constitutional identity.

**BRCA-34 Resource Allocation Process != Identity Sovereign.**

### 27.7 Federation boundary

Multiple compatible providers may jointly supply a function without merging civil or constitutional authority.

**BRCA-37 Federation != Authority Union.**

### 27.8 Concentration boundary — source-resolved

Subsequent Economy / Resource Allocation development resolves the architectural dependency in:

`02_Domains/06_Economy_and_Value_Coordination/04_Resource_Allocation_and_Stewardship/Concord-Controlled Scarce Resource Concentration — Planned Allocation Principle 001.md`

Scarce Concord-controlled capacity may be subject to a **capacity-dependent maximum-use/allocation limit** sufficient to preserve meaningful population access, resilience and anti-capture objectives.

The bootstrap model must not infer either:

- Wealth -> Right To All Spare Concord Capacity; or
- Wealth -> Automatic Disqualification From Large Allocation.

Instead:

**Available Capacity != Unlimited Individual Entitlement**

**Ability To Pay != Unlimited Claim On Concord-Controlled Capacity**

**Concord Allocation Limit != Participant Consumption Limit**

**Concord Resource Scarcity != Prohibition On External Supply**

A participant who reaches a Concord allocation limit remains free, subject to ordinary applicable law and external terms, to obtain additional resources from external providers. Concord does not thereby become responsible for those independent external contracts or services unless it separately undertakes such an obligation.

Numerical limits are intentionally deferred because Concord currently has no material resource base from which responsible thresholds can be derived. They should be determined from actual deliverable capacity, commitments, reserves, demand, resilience requirements and operational evidence.

Therefore:

**Economic Capacity Concentration Policy = ARCHITECTURALLY RESOLVED / QUANTITATIVE POLICY DEFERRED**

This remains an external Economy-owned policy consumed by the bootstrap model rather than a bootstrap-created economic rule.

### 27.9 Revised minimum live-service state

A material bootstrap service should represent:

Function + ResourcePool + DeliverableCapacityBasis + Availability + AdmissionState + AllocationRule + ProtectedMinimumRule + Dormancy/ReclamationRule + CapacityClaim + CapacityEvidence + DegradationRule + Exit/ExportRule + FundingOptions + StewardshipRequirement + Dispute/CorrectionRoute + ExternalAllocationPolicyDependencies.

## 28. Model 002 disposition

With the adversarial additions above, the capacity/admission model is stable enough for integration into the next CMSS bounded revision.

It is **not** ready for PMEDG extraction because numerical allocation policy, anti-Sybil resolution and deployed evidence remain unresolved. Economic concentration is now architecturally resolved, with quantitative limits deliberately deferred until real resource capacity exists.

No further broad architectural discovery is currently indicated for this model unless new scenarios expose a missing abstraction layer.
