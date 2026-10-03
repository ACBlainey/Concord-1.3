# Protocol-Driven Self-Treatment and Automated Therapeutic Authorisation 001

**Project:** The Concord Framework  
**Date:** 3 October 2026  
**Status:** ACTIVE HEALTH DEVELOPMENT / PROVISIONAL / NON-CANONICAL / REQUIRES SPECIALIST CLINICAL AND LEGAL VALIDATION  
**Domain:** Health  
**Depends on:** Health Core Architecture 001 / Health Service Topology and Participant-Directed Access 001 / Smart Diagnostic Navigation and Reality-Tree Health Specification 001 / Participant-Directed Diagnostic Testing 001  
**Primary interfaces:** Pharmacy / professional competence / Health records / Law / Research / antimicrobial stewardship / emergency care

## 1. Purpose

Professional involvement should occur where professional judgement, competence or intervention is materially necessary.

The mere presence of a pathology does not establish that a clinician must personally mediate treatment.

Where a participant's condition is sufficiently established and a validated treatment protocol applies without material unresolved complexity, Concord Health may support protocol-driven self-treatment.

> **Confirmed Pathology != Automatic Requirement For Doctor Encounter**

and:

> **Treatment Need != Automatic Requirement For Human Gatekeeper**

This architecture does not establish which real diseases or medicines qualify. Those classifications require validated specialist Health and legal architecture.

## 2. General pathway

A participant-directed episode may proceed:

**Symptoms/Concern**
→ Smart Diagnostic Navigation
→ candidate pathology
→ appropriate participant-accessible diagnostic testing
→ evidence/result
→ Reality Tree update
→ pathology sufficiently established for bounded treatment decision
→ validated treatment protocol identified
→ participant-specific safety/eligibility checks
→ treatment authorised/supplied where all required conditions are satisfied
→ participant self-treatment
→ monitoring
→ resolution/closure

or, if the expected course does not occur:

→ reassessment
→ additional diagnostics
→ generalist/specialist self-referral
→ urgent/emergency escalation where indicated.

Thus professional care becomes an available escalation and support layer rather than an automatic administrative stage.

## 3. Protocol suitability

Automated or protocol-driven treatment should be possible only where a validated specialist protocol establishes sufficiently bounded conditions for its use.

A protocol may require:

- sufficiently established diagnosis or indication;
- defined participant population;
- defined severity range;
- defined exclusions;
- contraindication screening;
- interaction screening;
- allergy/intolerance screening;
- relevant organ/system function or substrate equivalent;
- pregnancy/reproductive considerations where applicable;
- prior treatment history where relevant;
- dose/regimen rules;
- monitoring requirements;
- treatment duration;
- expected response window;
- failure criteria;
- adverse-effect triggers;
- escalation conditions;
- repeat-treatment limits.

> **Known Treatment Exists != Protocol Applies To This Participant**

## 4. Evidence threshold

The required evidence should depend on the consequence of treatment and the risk of treating the wrong condition.

A low-consequence self-care protocol may tolerate more diagnostic uncertainty than a consequential prescription intervention.

Therefore:

> **Diagnostic Sufficiency Is Consequence-Sensitive**

The system should not collapse:
- possible diagnosis;
- probable working diagnosis;
- test-supported diagnosis;
- confirmed causal agent;
- treatment indication.

These may require different evidential states.

## 5. Example class — suspected infection

A generic pathway could be:

**Symptoms suggest possible infection**
→ diagnostic Reality Tree
→ appropriate tests
→ evidence supports infection
→ where relevant, testing identifies organism/cause and treatment susceptibility
→ validated protocol checks whether antimicrobial treatment is indicated
→ participant-specific contraindication/interaction/allergy checks
→ appropriate treatment route.

This is an architectural example only.

A positive test does not automatically imply that antibiotics or another antimicrobial are required.

> **Pathogen Detected != Automatic Antimicrobial Indication**

The validated protocol must determine whether treatment is appropriate.

## 6. Automated therapeutic authorisation

Where all required conditions are represented and satisfied, an automated Health system may potentially issue the bounded therapeutic authorisation necessary for treatment or dispensing.

That action must be distinguished from merely generating text that resembles a prescription.

A legitimate automated authorisation requires:

- lawful authority for the system to perform that function;
- validated treatment protocol;
- current participant evidence;
- verified participant identity where necessary;
- contraindication/interactions review;
- required diagnostic threshold;
- current protocol/version;
- dose/regimen derivation;
- scope and expiry;
- provenance;
- pharmacy/dispensing validation where applicable;
- monitoring and escalation instructions.

> **Automated Recommendation != Therapeutic Authorisation**

and:

> **Automation Capability != Prescribing Authority**

The authority must be prospectively established by Health/Law rather than inferred from technical capability.

## 7. Human review state

If all required protocol conditions cannot be resolved, the system should not improvise.

Possible states:

- PROTOCOL_ELIGIBLE;
- PROTOCOL_ELIGIBLE_WITH_MONITORING;
- ADDITIONAL_EVIDENCE_REQUIRED;
- PROFESSIONAL_REVIEW_REQUIRED;
- SPECIALIST_REVIEW_REQUIRED;
- URGENT_REVIEW_REQUIRED;
- EMERGENCY;
- TREATMENT_NOT_INDICATED;
- PROTOCOL_UNRESOLVED.

> **Protocol Unresolved != Permission To Guess**

A professional review can resolve actual uncertainty without becoming a permanent gate for future protocol-complete episodes.

## 8. Participant choice

Even where automated treatment is available, the participant may request professional consultation.

> **Automated Route Available != Human Consultation Prohibited**

The participant may prefer explanation, reassurance, a second opinion, alternative treatment discussion or continuing clinician relationship.

Likewise, declining an automatically suggested treatment does not terminate Health access.

## 9. Self-treatment information

A protocol-authorised self-treatment package should provide understandable information including:

- what condition/indication is being treated;
- evidential basis;
- treatment and intended effect;
- how to use/administer it;
- duration;
- common expected effects;
- material adverse effects;
- interactions/activities to avoid where applicable;
- expected improvement window;
- what to monitor;
- when to stop;
- when to repeat testing;
- when to seek generalist/specialist review;
- urgent/emergency warning signs.

The participant should be able to ask for clarification.

## 10. Monitoring and expected course

Every protocol should define a bounded expected course where clinically meaningful.

Example states:

**IMPROVING_AS_EXPECTED**
→ continue protocol.

**RESOLVED**
→ close episode / routine follow-up if applicable.

**NOT_IMPROVING_BY_TRIGGER**
→ reopen Reality Tree / professional or further diagnostic route.

**WORSENING**
→ severity-based reassessment/escalation.

**ADVERSE_EFFECT**
→ treatment-specific response/escalation.

**NEW_SYMPTOMS**
→ reopen diagnostic space.

> **Treatment Started != Diagnosis Permanently Fixed**

Failure to respond is evidence that may challenge the diagnosis, treatment selection, resistance/susceptibility assumption, adherence, severity model or completeness of the original evaluation.

## 11. Escalation by exception

Professional involvement can therefore be triggered by material reasons such as:

- diagnostic ambiguity;
- protocol exclusion;
- treatment failure;
- worsening condition;
- severe presentation;
- unexpected result;
- adverse effect;
- contraindication;
- complex interaction;
- recurrent disease;
- unusual organism/pathology;
- participant request;
- inability to safely self-administer;
- need for consequential procedure;
- unresolved ESCP challenge.

> **Professional Escalation Should Be Triggered By Clinical Need, Not Routine Administrative Sequence**

## 12. Medication safety

Medication authorisation requires a current medication/support reconciliation where interactions are material.

The system should check:
- active medications;
- recent relevant medications;
- allergies/intolerances;
- duplicate therapy;
- interactions;
- participant-specific contraindications;
- relevant laboratory/functional state;
- protocol-defined prior failures;
- maximum duration/repetition.

The participant record should update automatically when treatment is supplied, while preserving provenance.

## 13. Antimicrobial stewardship

Antimicrobials illustrate why removing a doctor gate does not mean removing stewardship.

A protocol-driven system may potentially improve stewardship if it:
- requires evidence appropriate to the indication;
- distinguishes bacterial/viral/other causes where possible;
- incorporates susceptibility/resistance information where relevant;
- avoids treatment where evidence does not support benefit;
- selects validated agent/dose/duration;
- tracks recent antimicrobial exposure;
- monitors outcome;
- updates population resistance evidence through appropriately governed Research/public-health channels.

> **No Doctor Gate != No Stewardship**

Stewardship should be embedded in the treatment protocol rather than implemented solely through professional scarcity.

## 14. Repeat treatment

A prior successful automated treatment does not automatically authorise indefinite repetition.

Repeat episodes may require:
- confirmation that presentation is materially equivalent;
- recurrence limits;
- repeat diagnostics;
- resistance or treatment-failure checks;
- professional review after defined recurrence;
- investigation of underlying causes.

> **Previous Protocol Eligibility != Permanent Future Eligibility**

## 15. Pharmacy/dispensing role

Where treatment requires controlled dispensing, the pharmacy or equivalent service performs a substantive safety and supply function.

It may validate:
- therapeutic authorisation;
- participant identity;
- medication;
- dose;
- duplicate supply;
- material interaction alerts;
- protocol expiry;
- supply provenance.

The dispenser should not silently become a second arbitrary gate where the valid authorisation and safety conditions are satisfied.

## 16. Records and contextual access

The episode should record:
- presenting concern;
- diagnostic evidence;
- protocol/version;
- eligibility determination;
- therapeutic authorisation;
- supplied treatment;
- participant instructions;
- monitoring state;
- outcome;
- escalation if any.

Any professional entering later receives a contextual projection relevant to the episode rather than general unrestricted access.

## 17. Population learning

Protocol outcomes can generate valuable Health evidence:
- response rate;
- adverse effects;
- diagnostic mismatch;
- recurrence;
- resistance;
- subgroup differences;
- unexpected failures.

Use for Research/public health requires appropriate governance, privacy and provenance.

> **Automated Care At Scale != Automatic Research Consent**

## 18. Safety against automation overreach

Protocol-driven treatment must not allow the automated system to:
- invent a treatment outside validated protocol;
- conceal unresolved contraindications;
- convert missing data into assumed normality;
- use a positive test as automatic treatment indication;
- ignore material participant change;
- continue treatment despite defined failure/adverse triggers;
- issue authority beyond its delegated scope;
- suppress access to a human professional.

> **Protocol Automation != Autonomous Clinical Sovereignty**

## 19. Relation to generalist and specialist care

Generalists and specialists remain essential where the problem requires:
- broader synthesis;
- examination;
- judgement under uncertainty;
- complex multimorbidity;
- unusual pathology;
- procedure;
- consequential intervention;
- treatment adaptation beyond validated protocol;
- management of repeated failure;
- participant preference.

Their value comes from clinical capability, not their position as mandatory entry gate.

## 20. Compact pathway

**Participant**
→ symptoms
→ Smart Diagnostic Navigation
→ participant-accessible testing
→ sufficient evidence
→ validated treatment protocol?

If NO:
→ more evidence / professional review / specialist route.

If YES:
→ participant-specific eligibility and safety checks
→ all required conditions satisfied?

If NO:
→ appropriate review/escalation.

If YES:
→ bounded automated therapeutic authorisation where lawfully enabled
→ treatment supplied
→ self-treatment
→ monitor expected course.

If resolves:
→ closure.

If persists/worsens/adverse/new evidence:
→ reopen diagnostic tree
→ additional testing and/or self-referral to professional care.

## 21. Core invariants

> **Confirmed Pathology != Automatic Requirement For Doctor Encounter**

> **Treatment Need != Automatic Requirement For Human Gatekeeper**

> **Known Treatment Exists != Protocol Applies To This Participant**

> **Diagnostic Sufficiency Is Consequence-Sensitive**

> **Pathogen Detected != Automatic Antimicrobial Indication**

> **Automated Recommendation != Therapeutic Authorisation**

> **Automation Capability != Prescribing Authority**

> **Protocol Unresolved != Permission To Guess**

> **Automated Route Available != Human Consultation Prohibited**

> **Treatment Started != Diagnosis Permanently Fixed**

> **Professional Escalation Should Be Triggered By Clinical Need, Not Routine Administrative Sequence**

> **No Doctor Gate != No Stewardship**

> **Previous Protocol Eligibility != Permanent Future Eligibility**

> **Protocol Automation != Autonomous Clinical Sovereignty**

## 22. Required next development

This architecture now exposes several concrete missing layers:

1. Health Treatment Protocol Governance and Validation;
2. automated therapeutic-authority legal model;
3. medication/support reconciliation;
4. pharmacy and dispensing architecture;
5. antimicrobial stewardship and resistance feedback;
6. treatment failure and escalation architecture;
7. professional competence/service registry;
8. participant-facing Health record and contextual wrapper;
9. biological specialist pathway catalogue;
10. digital-substrate treatment/repair equivalents.
