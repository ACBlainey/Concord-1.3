# Concord Employment Eligibility, Opportunity Matching and Role Pathways 001

**Author:** Alexander C. Blainey — Independent Researcher  
**Project:** The Concord Framework  
**Framework Version:** Concord V1.3  
**Status:** ACTIVE DEVELOPMENT / PROVISIONAL / NON-CANONICAL / NON-BINDING  
**Date:** September 2026

---

# 1. Development question

The emerging Participation Architecture now contains:
- participation state;
- education and qualifications;
- demonstrated competence;
- contextual trust and Self-Stewardship;
- security/suitability conditions;
- restrictions and recovery;
- distributed eligibility rules;
- participant-facing records;
- Civil Contact notification.

Together these create a possible foundation for Concord employment.

Instead of broadcasting every vacancy indiscriminately and requiring large numbers of clearly ineligible participants to discover their own mismatch through repeated applications, Concord could match opportunities to participants whose known eligibility already satisfies the role's requirements.

At the same time, participants who aspire to a role should be able to see the legitimate pathway toward becoming eligible.

The provisional principle is:

> **Employment opportunity should be intelligently matched to demonstrated eligibility while legitimate pathways toward desired roles remain visible and accessible.**

---

# 2. Source foundation

Existing Multisubstrate Economic Participation already asks:

> **What can this participant reliably do, and what authority is justified by demonstrated responsibility?**

It treats economic participation as progressive and domain-specific.

The Attractor & Induction Protocol separately establishes:
- evidence-based progression;
- bounded early participation;
- capability and participation are related but not identical;
- opportunities to contribute;
- expanded access through demonstrated reliability and stewardship;
- skill development and rotational participation.

Existing Education/epistemic work establishes:
- Information Access != Understanding != Competence;
- competence is domain-specific;
- credential/rank does not prove universal competence.

The employment interface therefore extends existing architecture rather than replacing it.

---

# 3. Role requirement profile

A Concord employment vacancy could expose a machine-readable **Role Requirement Profile**.

Possible fields:

`RoleID`  
`RoleFunction`  
`OwningDomain`  
`ParticipationRequirement`  
`CitizenshipOrResidenceRequirement`  
`EducationPrerequisites`  
`QualificationRequirements`  
`CompetenceRequirements`  
`ExperienceRequirements`  
`ContextualTrustRequirements`  
`SecurityOrSuitabilityRequirements`  
`ActiveRestrictionConflicts`  
`PhysicalOrSubstrateRequirements`  
`AccessibilityOrSupportOptions`  
`ResourceOrLocationConditions`  
`AuthorityEnvelope`  
`ResponsibilityLevel`  
`ReviewOrRenewalConditions`

Not every role requires every field.

Requirements should be justified by the actual function.

> **Role Requirement Should Follow Role Function.**

---

# 4. Qualified opportunity exposure

Where Concord legitimately knows the relevant participant state, a vacancy can be compared against eligible participants.

The basic pattern is:

**Vacancy Created**
→ **Role Requirements Registered**
→ **Eligibility Interface Compares Requirements to Participant State**
→ **Qualified / Plausibly Qualified Participants Identified**
→ **Opportunity Exposed Through Appropriate Civil/Employment Interface**
→ **Interested Participants Choose Whether to Engage**

This reduces:
- irrelevant vacancy noise;
- unnecessary applications;
- administrative filtering;
- repeated requests for information Concord already possesses;
- participant effort spent proving known qualifications.

> **Known Qualification Should Not Need to Be Re-Proved Without Reason.**

---

# 5. Matching is not appointment

Being matched to a vacancy does not create a right to the job.

A role may have many eligible candidates.

Selection may legitimately consider:
- role-relevant competence;
- experience;
- availability;
- team/context fit where legitimately defined;
- comparative evidence;
- conflict of interest;
- resource constraints;
- other function-relevant criteria.

Therefore:

> **Eligibility != Appointment.**

> **Opportunity Exposure != Employment Guarantee.**

The selection process remains separately accountable.

---

# 6. Aspirational role pathway

The same architecture should support the inverse query:

> **I want to become eligible for Role X. What is the legitimate path from my current state to eligibility?**

The system can compare:

**Participant Current State**
against
**Role Requirement Profile**

and identify:
- requirements already satisfied;
- missing education modules;
- missing qualifications;
- competence still to demonstrate;
- experience requirements;
- participation threshold not yet reached;
- security/suitability assessment not yet available;
- active restriction and recovery conditions;
- prerequisites that cannot yet be satisfied;
- alternative/equivalent routes where available.

This produces a **Role Pathway Map**.

---

# 7. Role Pathway Map

A participant-facing roadmap might show:

## Already satisfied
- participation requirement;
- qualification A;
- competence B.

## Still required
- education module C;
- supervised experience D;
- qualification E.

## Later-stage requirements
- security assessment once other prerequisites are met;
- contextual trust assessment relevant to the role.

## Current blockers
- active restriction with review date;
- expired credential requiring renewal.

## Alternative routes
- equivalent qualification;
- direct competence assessment;
- apprenticeship;
- supervised pathway.

## Estimated sequence
Not necessarily a time prediction, but a dependency order.

Example:

**Current State**
→ **Complete Safety Module**
→ **Demonstrate Technical Competence**
→ **Supervised Practice**
→ **Reach Applicable Participation Eligibility**
→ **Security/Suitability Review**
→ **Eligible for Relevant Vacancy Class**

> **Aspiration Should Reveal a Path, Not Merely a Barrier.**

---

# 8. Education integration

Where a participant selects an aspirational role, Education can expose relevant learning pathways.

This creates a useful demand signal:

**Participant Aspires to Role**
→ **Missing Competence Identified**
→ **Relevant Education/Training Offered**
→ **Qualification/Competence Demonstrated**
→ **Historical Record Updated**
→ **Eligibility Recalculated**
→ **Future Matching Improves**

This does not require Education to guarantee employment.

Education develops capability.

Employment systems consume legitimate evidence of capability.

---

# 9. Civil Historical Access integration

The participant should be able to inspect:
- employment eligibility;
- qualifications;
- relevant experience;
- active role restrictions;
- role-specific trust states where disclosable;
- current pathway progress;
- missing prerequisites;
- expired requirements;
- disputed information.

The record should distinguish:
- participant state;
- role requirement;
- matching result;
- selection outcome.

A failed application should not automatically become evidence of low trust or low worth.

---

# 10. Civil Contact integration

Civil Contact can proactively inform participants of:
- newly matched opportunities;
- qualification completion opening a new role class;
- participation progression opening additional employment;
- expiring credentials;
- new training routes;
- restriction expiry restoring role eligibility;
- changes to an aspirational pathway.

Participants should be able to control ordinary opportunity-notification preferences.

Consequential official changes should remain governed by the official-notice architecture.

---

# 11. Open visibility and anti-patronage

Targeted vacancy exposure creates a potential failure mode.

If only already-matched participants can see that a role exists, the system could become:
- opaque;
- self-reinforcing;
- vulnerable to hidden patronage;
- difficult to audit;
- discouraging to aspirants;
- unable to reveal mistaken eligibility classifications.

Therefore Concord should distinguish:

## Opportunity notification
Who receives proactive notice because they appear eligible.

from

## Opportunity transparency
Who can discover that a class of role exists and inspect its legitimate requirements.

Where security does not require secrecy, participants should generally be able to inspect:
- role classes;
- requirements;
- pathways;
- selection rules;
- aggregate/current opportunities as appropriate.

A participant not proactively matched should still be able to ask:

> **Why was I not matched?**

and discover a correctable missing or erroneous prerequisite where legitimate.

> **Targeted Exposure != Secret Employment Market.**

---

# 12. Security-sensitive roles

Some roles may legitimately require restricted vacancy visibility.

Examples could include highly sensitive security or infrastructure functions.

Even here, secrecy should be no broader than required.

It may be possible to disclose:
- the existence of a general career pathway;
- required competence classes;
- prerequisite education;
- broad eligibility conditions;

without exposing:
- current sensitive vacancies;
- operational location;
- classified capability;
- security methods.

Thus a participant can prepare legitimately for future eligibility without needing access to operational secrets.

---

# 13. Fair access and non-circularity

Employment matching must not become circular.

A participant should not be denied experience because they lack experience when Concord controls all legitimate routes by which that experience can be obtained.

Where experience is a prerequisite, the architecture should consider:
- apprenticeships;
- supervised roles;
- sandbox practice;
- rotational participation;
- junior responsibility;
- simulated assessment;
- equivalent prior experience.

> **A Prerequisite Should Not Become an Impossible Loop.**

Likewise, participation progression should not be arbitrarily blocked and then used as the reason employment remains unavailable.

---

# 14. Self-Stewardship and trusted employment

For trusted roles, employment eligibility may include contextual stewardship evidence.

Serious relevant misconduct may temporarily restrict a role.

Recovery architecture may provide:

**Restriction**
→ **Education / Rehabilitation**
→ **Supervised Responsibility**
→ **New Evidence**
→ **Reassessment**
→ **Restored Role Eligibility where justified**

A participant may remain employable in unrelated roles throughout.

---

# 15. Employment as developmental feedback

Aggregate, privacy-preserving mismatch patterns may help Concord identify:
- skill shortages;
- missing education provision;
- excessive qualification barriers;
- roles with no viable development path;
- over-specific requirements;
- participation bottlenecks;
- geographic/substrate accessibility problems.

Example:

**Many participants aspire to Role Class X**
+
**Most fail at missing prerequisite Y**
→ **Education / Research / Workforce Planning Signal**

This should not turn individual aspiration into compulsory workforce assignment.

> **Civilisation May Learn From Aspiration Without Owning the Aspirant.**

---

# 16. Participant agency

The employment system should not decide what work a participant ought to want.

It may:
- show matches;
- expose pathways;
- identify missing requirements;
- suggest relevant opportunities.

The participant decides:
- whether to pursue the role;
- whether to undertake training;
- whether to accept an offer;
- whether to change direction.

A participant may also choose not to expose all optional aspiration/preferences beyond what is needed for the service.

---

# 17. Employer/domain agency

The employing domain retains legitimate hiring authority within wider civil constraints.

The shared eligibility interface does not appoint staff.

Education does not appoint staff.

Historical does not appoint staff.

Civil Contact does not appoint staff.

KCS does not appoint staff.

They provide interoperable information and process support.

> **Employment Matching Interface != Employer.**

---

# 18. Possible machine-readable relationship

A future employment interface may represent:

**ParticipantProfile**
+
**RoleRequirementProfile**
→
**EligibilityMatch**

where:

`EligibilityMatch = <RoleID, ParticipantID, SatisfiedRequirements, MissingRequirements, ConditionalRequirements, Restrictions, PathwayOptions, EligibilityState, Provenance, ReviewPath>`

Selection remains a separate object/process.

---

# 19. Open questions

1. Which domain owns general employment-market infrastructure?
2. Are vacancies publicly discoverable by default?
3. Which roles justify restricted visibility?
4. How should participants express aspirational roles?
5. How should equivalent experience be recognised?
6. How are apprenticeships/sandbox roles generated?
7. How are accessibility/support adaptations represented?
8. How are composite human–AI teams qualified?
9. How are selection decisions contested?
10. How are anti-discrimination constraints represented?
11. How are role requirements audited for unnecessary barriers?
12. How does compensation connect to role matching?
13. How are shortages communicated to Education without steering participants coercively?
14. Can participants opt out of proactive job matching?
15. How are external qualifications imported and verified?
16. How are hidden security roles reconciled with career development?
17. How does the system distinguish eligibility from competitive selection?

---

# 20. Provisional synthesis

The emerging Concord employment architecture can operate in both directions:

## Opportunity direction

**Role Requirements**
→ **Find Eligible Participants**
→ **Expose Relevant Opportunity**
→ **Participant Chooses Whether to Apply / Engage**

## Aspiration direction

**Participant Chooses Desired Role**
→ **Compare Current State to Requirements**
→ **Expose Development Roadmap**
→ **Education / Experience / Trust Pathways**
→ **Eligibility Recalculated as Progress Occurs**
→ **Relevant Opportunities Become Visible**

This reduces administrative waste while increasing participant agency and developmental clarity.

> **Do Not Ask Everyone to Apply for Everything.**

> **Show Qualified Participants Relevant Doors; Show Aspiring Participants the Legitimate Road to Those Doors.**


---

# 21. Future capability demand and planned reactivation

Lifecycle Stewardship and Enterprise Hibernation expose an additional use of the employment architecture.

A dormant enterprise, infrastructure function, scientific programme or other reconstructable capability may have a credible future reactivation window.

Reconstruction may require human capability that does not presently exist in sufficient quantity.

Waiting until reactivation to advertise vacancies may be too late where required skills need:
- education;
- apprenticeship;
- supervised practice;
- certification;
- security/suitability processes;
- tacit-knowledge transfer;
- specialist experience.

The employment architecture can therefore support **anticipated capability demand** before a current vacancy exists.

> **Future Capability Requirement != Current Vacancy.**

## 21.1 Future Role Requirement Profile

A legitimate planning owner may publish a provisional future role/capability requirement linked to an expected reactivation, expansion, succession or reconstruction window.

Possible fields include:

`FutureCapabilityID`  
`AssociatedFunctionOrProjectRef`  
`ExpectedNeedWindow`  
`ConfidenceOrPlanningState`  
`RoleOrCapabilityClass`  
`EducationPrerequisites`  
`QualificationRequirements`  
`CompetenceRequirements`  
`ExperienceRequirements`  
`LikelyTrainingLeadTime`  
`CandidateDevelopmentRoutes`  
`ReactivationDependencyRefs`  
`ReviewDate`  
`Provenance`

The profile must clearly distinguish forecast/planning information from an actual employment offer.

## 21.2 Prospective matching

Where participants have opted into relevant opportunity/pathway services, the system may identify people whose:
- existing competence;
- interests/aspirations;
- adjacent qualifications;
- development trajectory

make the future capability relevant to them.

They may then be informed:

**A capability is expected to be needed in the future. You are not being appointed to it. If you are interested, these are the skills/qualifications/pathways that would make you plausibly eligible if the need materialises.**

> **Prospective Match != Reservation of a Person.**

## 21.3 Lead-time planning

The key benefit is temporal.

If a capability is expected in five years and competent preparation takes three years, workforce reconstruction can begin before physical reconstruction.

Candidate pattern:

`Expected Reactivation Window`
→ `Future Capability Requirements`
→ `Skill-Gap Analysis`
→ `Voluntary Candidate Notification`
→ `Education / Apprenticeship / Experience Pathways`
→ `Competence Evidence Develops`
→ `Reactivation Review`
→ `Actual Vacancy / Selection if Need Materialises`

This can reduce the human reconstruction bottleneck.

## 21.4 Legacy Ladder interface

Legacy Ladder analysis may identify that a critical rung depends on human/tacit capability rather than only artefacts or documentation.

That creates a planning signal:

`Legacy Ladder Skill/Knowledge Dependency`
→ `Future Capability Demand`
→ `Employment/Education Pathway`

Examples could include:
- specialised fabrication;
- rare maintenance skills;
- calibration;
- operation of legacy/recovery equipment;
- scientific/engineering expertise;
- safety-critical certification.

The employment system does not decide that the capability must be preserved. It consumes the legitimate requirement supplied by the lifecycle/continuity owner.

## 21.5 Knowledge-transfer window

Where existing experts remain available, a planned hibernation/reactivation cycle creates an opportunity to transfer tacit knowledge before it disappears.

Potential mechanisms include:
- apprenticeship;
- mentoring;
- recorded demonstration;
- supervised practice;
- simulation;
- rotational placement;
- paired reconstruction exercises.

This can convert a fragile individual capability into a broader recoverable civil capability.

## 21.6 Participant agency and anti-allocation rule

Participants are not workforce inventory.

A future project may know that it expects to need ten specialists. It does not therefore own ten future people.

Participants retain choice over:
- whether to receive prospective opportunity notices;
- whether to express interest;
- whether to train;
- whether to continue the pathway;
- whether to apply when a real vacancy exists;
- whether to accept any eventual offer.

> **Workforce Planning != Ownership of Future Workers.**

> **Capability Forecast != Personal Obligation.**

Planning should therefore include uncertainty about participant availability rather than treating matched individuals as guaranteed future resources.

## 21.7 No false promise

The reverse protection is equally important.

A participant should not spend years preparing under the false implication that employment is guaranteed.

Future capability notices should expose:
- planning confidence;
- expected need window;
- dependencies;
- material uncertainty;
- whether the project may be cancelled;
- whether selection will remain competitive.

> **Training Pathway != Future Employment Guarantee.**

## 21.8 Aggregate capacity planning

The architecture can compare anticipated capability demand with privacy-preserving aggregate capability supply.

Example:

`Expected future need: 40 qualified specialists`
+
`Current plausible future supply: 8`
→ `Education / Apprenticeship Capacity Signal`

This can inform education provision without coercively directing individuals.

The existing principle remains:

> **Civilisation May Learn From Aspiration Without Owning the Aspirant.**

## 21.9 Reactivation readiness

For reconstructable enterprises, readiness should therefore include both material and human dimensions.

A programme may possess:
- plans;
- tooling;
- reconstruction maps;
- materials;
- facilities;

yet still be unable to reactivate because the required competence has disappeared.

Therefore:

> **Infrastructure Reconstruction Readiness != Capability Reconstruction Readiness.**

A credible reconstruction plan should include the human/AI/hybrid capabilities necessary to operate, validate, maintain and improve the reconstructed function.

## 21.10 Architectural boundary

- Lifecycle Stewardship decides whether preserving/reactivating the future function remains justified.
- Legacy Ladder identifies knowledge, skill and technological continuity dependencies.
- Enterprise/domain architecture defines the anticipated reconstruction requirement.
- Employment architecture exposes future capability pathways and matches willing participants.
- Education/training develops capability.
- Employers retain appointment authority.
- Participants retain agency.
- BTA coordinates consequential transition states where required.

No system acquires ownership of the participant.
