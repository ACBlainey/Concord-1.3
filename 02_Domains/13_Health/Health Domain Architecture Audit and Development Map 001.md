# Health Domain Architecture Audit and Development Map 001

**Project:** The Concord
**Date:** 4 October 2026
**Status:** ACTIVE DEVELOPMENT MAP / NON-CANONICAL
**Domain:** Health

## 1. Purpose

This audit reviews the current Health architecture after development of the medical-knowledge, pharmaceutical, evidence-neutral treatment and prescribing-independence branches.

Its purpose is to identify structural coverage and select future work by architectural dependency rather than by medical speciality.

## 2. Current architectural backbone

The current Health domain already establishes a coherent general care lifecycle:

**Need/Concern -> Intake -> Immediate Safety Triage -> Participant/Context Identification -> Evidence Gathering -> Competing Explanations -> Bounded Assessment -> Options -> Consent/Authority Resolution -> Intervention/Support -> Observation -> Outcome Evaluation -> Revision/Recovery/Rehabilitation -> Closure or Continuing Support -> Learning**

The domain is participant-directed and substrate-neutral at the core level.

## 3. Strongly represented areas

### 3.1 Access and service topology
Covered by:
- Health Core Architecture 001;
- Health Service Topology and Participant-Directed Access 001.

Participant access is not designed around a compulsory GP gatekeeper.

### 3.2 Longitudinal observation and prevention
Covered by:
- Longitudinal Health Monitoring — Baselines, Pattern Detection and Preventive Review 001.

This establishes baseline/pattern/change detection and preventive review.

### 3.3 Diagnostic access and reasoning
Covered by:
- Participant-Directed Diagnostic Testing — Risk-Banded Access and Pathway Review 001;
- Smart Diagnostic Navigation and Reality-Tree Health Specification 001.

The participant can access diagnostic pathways without treating professional access as a universal prerequisite. Reality-Tree reasoning supports competing explanations and question correction.

### 3.4 Records, privacy and contextual access
Covered by:
- Health Record and Contextual Access Architecture 001;
- Genomic Health Record and Private Local Knowledge Matching 001.

The longitudinal record and protected-master/contextual-projection model are established.

### 3.5 Treatment knowledge and protocol
Covered by:
- Treatment Protocol Governance and Clinical Knowledge Validation 001;
- Evidence-Neutral Treatment Recognition and Neglected Therapeutics Architecture 001.

Medical knowledge is distinguished from clinical protocol, and treatment validity is evidence/outcome-led rather than pharmaceutical-category-led.

### 3.6 Self-treatment and automation
Covered by:
- Protocol-Driven Self-Treatment and Automated Therapeutic Authorisation 001.

This establishes a bounded route for participant-directed and automated treatment where risk, evidence and authority permit it.

### 3.7 Professional competence
Covered by:
- Clinical Competence Requirements and Qualified-Practitioner Interface 001;
- Education-domain Medical Education and Qualification Architecture;
- Clinical Function and Competence Contract.

Health defines required capability; Education owns education, assessment, qualification and accreditation.

### 3.8 Medical knowledge lifecycle
Covered by:
- Medical Knowledge Stewardship, Research Translation and Experimental Treatment 001;
- cross-domain Clinical Experience to Medical Knowledge learning loop;
- Clinical Learning Signal Intake;
- Medical Knowledge Validation and Historical Promotion.

Historical preserves validated medical knowledge; Research validates candidate knowledge; Health applies it; clinical experience can feed back into Research.

### 3.9 Medication and pharmacovigilance
Covered by:
- Medication, Prescribing, Dispensing and Pharmacovigilance Architecture 001.

This distinguishes prescribing, dispensing, possession, actual use, monitoring and adverse-event learning.

### 3.10 Pharmaceutical production and access
Covered by:
- Open Pharmaceutical Production, Quality and Access Architecture 001;
- Commerce-domain open-knowledge, bounded-IP and development-return work.

Validated manufacturing knowledge can support non-exclusive qualified production without removing safety/quality requirements.

### 3.11 Treatment-category neutrality and neglected therapeutics
Covered by:
- Evidence-Neutral Treatment Recognition and Neglected Therapeutics Architecture 001.

Validated pharmaceutical and non-pharmaceutical treatments can enter the same knowledge and treatment-selection system. Low commercial return is not treated as low medical value.

### 3.12 Clinical economic independence
Covered by:
- Clinical Treatment Independence and Prescriber Conflict-of-Interest Architecture 001.

Clinical recommendation is separated from personal sales incentive and commercial sponsorship must not define the treatment comparison set.

## 4. Structural gaps

### GAP H-01 — Acute and emergency care authority
**Priority: CRITICAL / NEXT**

The generic lifecycle contains immediate safety triage but does not yet fully specify what happens when:
- delay creates serious harm;
- participant consent cannot presently be obtained;
- capacity is temporarily impaired or uncertain;
- identity/history is unknown;
- evidence is incomplete;
- several patients compete for immediately scarce capability;
- emergency responders must act before ordinary contextual access is established;
- emergency action changes the participant's body, state or future options;
- an initially justified intervention must later terminate or return to ordinary consent.

This is an upstream architecture, not merely an emergency-department speciality.

It should define:
**Emergency Need != General Emergency Authority**
and the transition:
**ordinary participant-directed care -> bounded emergency authority -> stabilisation -> restored participant authority -> reconciliation/audit/record update**.

It interfaces directly with Blainey's Laws, temporal consent, bounded authority, Health records, triage, Law and consequential-action architecture.

### GAP H-02 — Procedural and surgical intervention
**Priority: HIGH / DEPENDS PARTLY ON H-01**

Needs architecture for invasive procedures, anaesthesia, irreversible/reversible consequences, procedural teams, competence composition, peri-operative monitoring, implants, complications and post-procedure care.

### GAP H-03 — Rehabilitation and long-term support
**Priority: HIGH**

The core lifecycle names recovery/rehabilitation but lacks a developed branch covering restoration, adaptation, chronic disability, long-duration support, participant goals, assistive systems and changing dependency.

### GAP H-04 — Mental and cognitive health
**Priority: HIGH**

Requires careful treatment of participant standing, capacity, distress, coercion, emergency intervention, privacy, therapeutic relationships, self-harm risk and Law interfaces. It should follow rather than pre-empt the general emergency-authority architecture.

### GAP H-05 — Reproductive, maternity and developmental Health
**Priority: HIGH**

Requires pregnancy, childbirth, maternal/fetal interests, reproductive autonomy, neonatal transition, paediatric/developmental interfaces and changing capacity/standing questions.

### GAP H-06 — Infectious disease and population Health
**Priority: HIGH / CROSS-DOMAIN**

Requires participant-level Health versus population externality, surveillance boundaries, outbreak evidence, isolation/quarantine authority, vaccination, environmental/public-health interventions and Law/Governance interfaces.

### GAP H-07 — Digital/AI substrate Health
**Priority: HIGH**

The core is substrate-neutral but detailed implementation remains biologically weighted. Digital Health needs diagnosis of functional damage, integrity/corruption, continuity, restoration, backup/state questions, substrate migration, identity/health distinction and owner/host/participant authority boundaries.

### GAP H-08 — Devices, sensors and measurement integrity
**Priority: MEDIUM-HIGH**

Longitudinal monitoring and diagnostic testing depend on device calibration, provenance, uncertainty, failure detection, interoperability and distinction between sensor output and clinical fact.

### GAP H-09 — Pharmacy/dispensing operational topology
**Priority: MEDIUM-HIGH**

Medication architecture exists but detailed dispensing service topology, substitutions, verification, supply continuity, controlled/high-risk medicine handling and recall execution remain underdeveloped.

### GAP H-10 — Specialist service branches
**Priority: MEDIUM AFTER SHARED ARCHITECTURES**

Dentistry, ophthalmology, specialist medicine and similar branches should generally reuse the common Health architecture rather than each rebuilding authority, records, knowledge and consent.

### GAP H-11 — Health resource scarcity and allocation
**Priority: HIGH / CROSS-DOMAIN**

Existing life-support source resolution identified unresolved boundaries around scarcity, allocation and involuntary withdrawal. A general Health scarcity architecture remains needed.

### GAP H-12 — End-of-life, palliative care and death
**Priority: HIGH / CROSS-DOMAIN**

Requires participant preference, advance decisions, symptom relief, treatment withdrawal/refusal, irreversible incapacity, death determination, records, relatives and Historical/Continuity interfaces.

## 5. Dependency ordering

Recommended development order:

1. **Acute and Emergency Care Authority and Consent Transition**
2. Procedural/Surgical Intervention
3. Health Resource Scarcity and Allocation
4. Rehabilitation and Long-Term Support
5. Mental and Cognitive Health
6. End-of-Life and Palliative Care
7. Infectious Disease and Population Health
8. Reproductive/Maternity/Developmental Health
9. Digital/AI Substrate Health
10. Devices/Sensors/Measurement Integrity
11. Pharmacy/Dispensing Operational Topology
12. specialist branches as needed.

This order is architectural rather than a judgement of medical importance.

## 6. Why emergency architecture is next

Emergency care stress-tests several of the most important Concord distinctions simultaneously:
- autonomy versus necessary immediate intervention;
- consent versus temporary inability to consent;
- capability versus authority;
- evidence incompleteness versus time pressure;
- contextual record access versus urgent need;
- reversibility versus irreversible action;
- temporary authority versus continuing authority;
- individual need versus scarce resources.

If these are resolved at the shared Health level, later speciality architectures can inherit the rules rather than inventing inconsistent emergency exceptions.

## 7. Proposed next architecture

Create:

**Acute and Emergency Health Care — Triage, Temporary Authority and Consent Restoration Architecture 001**

Minimum questions:
1. What creates emergency clinical authority?
2. What is the minimum necessary scope?
3. How is uncertainty handled?
4. How does known refusal/advance consent constrain action?
5. What happens when capacity/communication returns?
6. How is emergency contextual record access bounded?
7. How are unknown identity/history handled?
8. How are emergency interventions documented and audited?
9. How does emergency authority terminate?
10. How are consequences reconciled with the participant afterward?
11. How does scarcity differ from individual emergency need?
12. When does Law become involved?

## 8. Audit conclusion

The Health domain no longer lacks a general conceptual core. Its principal gaps are now **stress-state and specialist implementations**.

The highest-value next step is to develop emergency Health as the first major stress-state architecture.

> **Normal Care Architecture Is Not Complete Until It Explains How Its Boundaries Behave Under Urgency**

> **Urgency May Change The Permissible Action Window Without Creating General Sovereignty Over The Participant**
