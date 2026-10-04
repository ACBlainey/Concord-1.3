# Medication, Prescribing, Dispensing and Pharmacovigilance Architecture 001

**Project:** The Concord
**Date:** 4 October 2026
**Status:** ACTIVE HEALTH ARCHITECTURE / PROVISIONAL / NON-CANONICAL / SPECIALIST VALIDATION REQUIRED
**Primary owner:** Health
**Interfaces:** Historical / Research / Education / Participant Health Record / Clinical Learning Architecture

## 1. Purpose

Medication is a Health function with strong dependencies on other domains.

The central ownership model is:

- **Historical** preserves validated medication and prescribing knowledge.
- **Research** investigates candidate knowledge, adverse reactions, unexpected outcomes, interactions and treatment-performance questions.
- **Education** owns pharmaceutical and medication-related education, competence assessment, qualification and accreditation.
- **Health** owns participant-specific medication assessment, prescribing/therapeutic authorisation, dispensing interfaces, reconciliation, monitoring, adjustment and clinical feedback.
- **Participant Health records and authorised personal monitoring** preserve the participant-specific medication state, actual-use evidence and relevant longitudinal outcome metrics.

> **Shared Medication Lifecycle != Shared Domain Ownership**

## 2. Historical medication knowledge

Historical preserves the current validated knowledge state and provenance for matters such as:
- indications;
- expected benefits;
- dosage/range knowledge where validated;
- contraindications;
- known interactions;
- known adverse effects;
- monitoring requirements;
- population/substrate limitations;
- administration constraints;
- discontinuation/tapering knowledge where relevant;
- validated prescribing guidance;
- prior and superseded knowledge states.

Historical does not prescribe to an individual.

> **Validated Prescribing Knowledge != Participant Prescription**

> **Knowledge Custody != Prescribing Authority**

## 3. Health as participant-specific controller

Health combines validated medication knowledge with the current participant context.

Relevant inputs may include:
- diagnosis/indication;
- current symptoms and clinical state;
- allergies/intolerances;
- current medications;
- participant-reported actual use;
- recent dispensing;
- contraindications;
- interactions;
- renal/hepatic or other relevant functional state;
- monitoring results;
- prior response;
- adverse reactions;
- participant preferences;
- pregnancy/reproductive context where relevant;
- relevant genomic information where legitimately available;
- current protocol;
- available competence and resources.

> **Population Medication Knowledge != Individual Medication Decision**

Health therefore owns the participant-specific decision and ongoing medication state, not Historical, Research, Education or the manufacturer.

## 4. Medication lifecycle

A general lifecycle is:

**Clinical need**
→ **participant-specific assessment**
→ **validated medication knowledge retrieval**
→ **medication reconciliation**
→ **contraindication/interaction/risk review**
→ **prescribing or therapeutic authorisation**
→ **dispensing/supply**
→ **participant information**
→ **actual use / administration**
→ **personal monitoring**
→ **outcome/adverse-effect assessment**
→ **continue / modify / stop / escalate**
→ **clinical learning signal where warranted**
→ **Research**
→ **validated knowledge change where supported**
→ **Historical**
→ **KCS**
→ **Health/Education update**.

## 5. Prescribing and therapeutic authorisation

A medication order should identify, proportionately:
- participant;
- medication;
- indication;
- intended regimen;
- duration/review point;
- material monitoring;
- contraindication/interaction state;
- prescriber/authorising function;
- competence reference;
- protocol/evidence reference;
- consent/participant choice where material;
- uncertainty;
- effective period;
- stopping/review conditions.

> **Prescription != Proof Of Current Appropriateness**

> **Prior Prescription != Continuing Authority**

A prescription or automated therapeutic authorisation remains bounded by the participant state and applicable protocol.

## 6. Prescribing competence

Education owns the development, assessment, qualification and accreditation of prescribing/pharmaceutical competence.

Health defines the clinical function and required competence through the existing Health-Education interface.

> **Pharmaceutical Accreditation = Education Function**

> **Qualification != Prescribing Authority In Every Context**

> **Competence != Participant-Specific Clinical Authority**

The Clinical Function and Competence Contract may specify prescribing, dispensing, medication-review and specialist pharmaceutical capabilities separately.

## 7. Medication reconciliation

The participant's real medication state may differ from a list of prescriptions.

Reconciliation should distinguish:
- currently authorised;
- dispensed;
- possessed;
- actually taken/administered;
- dose/frequency actually used;
- temporarily paused;
- stopped;
- participant-modified;
- self-treatment;
- externally supplied medication;
- relevant supplements/other substances;
- unknown state.

> **Prescribed != Dispensed != Possessed != Taken**

> **Medication List != Verified Current Medication State**

The purpose is not to police participant behaviour. It is to prevent clinical decisions from being made against a fictional medication state.

## 8. Participant Health record

The longitudinal Health record should preserve medication history and current state with provenance.

This may include:
- prescriptions/authorisations;
- dispensing events;
- reported actual use;
- monitoring data;
- benefit;
- adverse effects;
- participant changes/refusal;
- clinician changes;
- discontinuation;
- reason for change;
- relevant learning signals.

> **Medication Record != Assumption Of Consumption**

Participant access and correction/contestation remain important.

## 9. Personal monitoring

Where voluntarily used and clinically meaningful, personal daily monitoring may provide longitudinal evidence concerning:
- physiological measurements;
- symptoms;
- functional state;
- sleep/activity or other relevant metrics;
- dose timing;
- response timing;
- adverse effects;
- adherence/use patterns;
- recurrence after stopping;
- change after dose modification.

Individual baseline architecture remains relevant.

> **Monitoring Metric != Diagnosis**

> **Correlation With Medication Timing != Proven Causation**

But longitudinal participant-specific evidence can reveal patterns that episodic clinical observation may miss.

## 10. Actual-use feedback

Health should compare the intended medication plan with actual participant use where this is legitimately known.

Differences may indicate:
- misunderstanding;
- intolerable effects;
- cost/supply/access problem;
- participant preference;
- forgotten doses;
- ineffective regimen;
- practical difficulty;
- deliberate self-adjustment;
- incorrect record;
- other unknown cause.

> **Non-Adherence != Automatic Incapacity**

> **Deviation From Prescription != Proof Of Irrationality**

The appropriate response is to understand the cause and reassess the plan where necessary.

## 11. Dispensing

Dispensing is a bounded Health-supporting function.

It may require:
- valid current authorisation where required;
- correct participant/recipient;
- correct medication/formulation;
- dose/quantity;
- interaction/duplicate check where applicable;
- supply provenance;
- storage/quality state;
- participant information;
- traceable dispensing event.

> **Prescribing Authority != Dispensing Authority**

> **Dispensing Authority != General Clinical Authority**

> **Medication Availability != Authority To Supply**

Automation may perform dispensing functions where competence, protocol, identity, authority and exception handling are adequately satisfied.

## 12. Medication safety reconciliation at dispensing

A dispensing function may detect a conflict that was not visible at prescribing time, such as:
- newly added medication;
- changed allergy;
- duplicate therapy;
- interaction;
- changed participant state;
- obsolete authorisation.

This should trigger bounded review rather than silent supply or silent cancellation.

> **Detected Conflict -> Review; Not Automatic Substitution Of Dispensing For Clinical Judgement**

## 13. Participant information

Participants should receive useful information proportionate to the medication and risk, including where material:
- purpose;
- intended use;
- common/material adverse effects;
- serious warning signs;
- interactions;
- monitoring;
- missed-dose guidance;
- stopping constraints;
- when to seek review;
- uncertainty.

Information should support self-management rather than make professional contact a ritual prerequisite where it is not functionally needed.

## 14. Adverse reaction detection

Possible adverse reactions may arise from:
- participant report;
- professional observation;
- personal monitoring;
- laboratory/diagnostic change;
- repeated outcome pattern;
- automated signal detection;
- dispensing/pharmacy feedback.

Health first handles the participant-specific safety and care question.

Where broader significance may exist, a ClinicalLearningSignal enters Research.

> **Suspected Adverse Reaction != Proven Drug Causation**

> **Participant Safety Response != Research Conclusion**

## 15. Research and pharmacovigilance

Research owns investigation of candidate generalisable knowledge arising from:
- adverse reactions;
- unexpected interactions;
- lack of effect;
- dose-response anomalies;
- subgroup effects;
- long-term outcomes;
- withdrawal/rebound effects;
- unexpected benefits;
- medication/device combinations;
- repeated participant monitoring patterns.

The clinical learning intake and medical knowledge validation architectures apply.

> **Adverse-Event Report != Validated Adverse-Effect Knowledge**

Research may aggregate signals while preserving privacy and evidence independence.

## 16. Historical feedback

When Research validates a medication-related finding, Historical updates the validated knowledge state with provenance.

Examples:
- new interaction;
- revised contraindication;
- changed risk estimate;
- new adverse effect;
- narrowed indication;
- revised monitoring need;
- changed dosage knowledge;
- new subgroup distinction;
- corrected prior claim.

KCS then identifies affected Health protocols and Education dependencies.

> **Validated Medication Knowledge Change != Automatic Prescription Change For Every Participant**

Participant-specific relevance must still be evaluated.

## 17. Private participant matching

Where a new medication warning is relevant only to some participants, the system should prefer bounded matching against protected Health records rather than general record browsing.

PLE may support:
**validated bounded query → protected participant Health record → local evaluation → relevant participant/Health notification where matched**.

> **Need To Find Affected Participants != General Health-Record Access**

## 18. Education feedback

Validated changes may alter:
- pharmaceutical curricula;
- prescribing competence;
- dispensing competence;
- assessment;
- function-critical educational patches;
- specialist qualifications.

Education owns the educational response.

> **Medication Knowledge Change != Automatic Loss Of Pharmaceutical Qualification**

Function-critical gaps may require targeted patching/reassessment.

## 19. Self-treatment and automated medication pathways

Existing protocol-driven self-treatment remains compatible with this architecture.

Where pathology, medication protocol, participant state, contraindications, interactions and authority are sufficiently resolved, medication access may not require a routine professional encounter.

> **Professional Encounter != Universal Medication Permission Ritual**

Higher uncertainty, consequence or exception states may require professional review.

## 20. Medication discontinuation

Stopping medication can itself be clinically consequential.

The system should preserve validated knowledge concerning:
- abrupt cessation risk;
- tapering;
- rebound;
- withdrawal;
- monitoring after cessation;
- alternative support.

> **Authority To Start Medication != Permanent Authority To Continue It**

> **Participant Withdrawal Of Consent != Permission To Conceal Material Stopping Risk**

The participant should be informed of material consequences while retaining applicable autonomy.

## 21. Unused medication and stewardship

Unused or expired medication should have safe return/disposal routes.

Where legitimate and safe, resource stewardship may include controlled recovery or material disposal, but medication integrity and contamination constraints take precedence over naive reuse.

> **Unused Product != Automatically Reusable Medicine**

This interfaces with product lifecycle and resource stewardship architecture.

## 22. Learning from medication outcomes

Medication use creates a particularly strong closed feedback loop:

**validated knowledge**
→ **participant-specific prescription**
→ **actual use**
→ **daily/clinical monitoring**
→ **outcome**
→ **Health reassessment**
→ **learning signal**
→ **Research**
→ **validation**
→ **Historical**
→ **KCS**
→ **Health + Education**
→ **future prescribing**.

This allows the medical system to improve from real clinical experience without converting every anecdote into doctrine.

## 23. Core invariants

MED-01 Validated Prescribing Knowledge != Participant Prescription.
MED-02 Knowledge Custody != Prescribing Authority.
MED-03 Population Medication Knowledge != Individual Medication Decision.
MED-04 Prescription != Proof Of Current Appropriateness.
MED-05 Prior Prescription != Continuing Authority.
MED-06 Pharmaceutical Accreditation = Education Function.
MED-07 Qualification != Prescribing Authority In Every Context.
MED-08 Prescribed != Dispensed != Possessed != Taken.
MED-09 Medication List != Verified Current Medication State.
MED-10 Medication Record != Assumption Of Consumption.
MED-11 Monitoring Metric != Diagnosis.
MED-12 Non-Adherence != Automatic Incapacity.
MED-13 Prescribing Authority != Dispensing Authority.
MED-14 Dispensing Authority != General Clinical Authority.
MED-15 Suspected Adverse Reaction != Proven Drug Causation.
MED-16 Adverse-Event Report != Validated Adverse-Effect Knowledge.
MED-17 Need To Find Affected Participants != General Health-Record Access.
MED-18 Medication Knowledge Change != Automatic Loss Of Pharmaceutical Qualification.
MED-19 Authority To Start Medication != Permanent Authority To Continue It.

## 24. Remaining development

Still required:
- specialist pharmaceutical validation;
- controlled/restricted medication law;
- manufacturing and quality assurance;
- supply-chain provenance;
- exact dispensing implementation;
- medication substitution rules;
- dose calculation specialist architecture;
- antimicrobial stewardship;
- emergency medication supply;
- detailed pharmacovigilance thresholds;
- medication recall architecture;
- cross-jurisdiction prescription recognition.

This architecture establishes ownership and the participant-specific medication feedback lifecycle without manufacturing specialist pharmaceutical rules.
