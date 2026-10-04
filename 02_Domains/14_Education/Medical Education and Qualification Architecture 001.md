# Medical Education and Qualification Architecture 001

**Project:** The Concord
**Domain:** Education
**Date:** 4 October 2026
**Status:** ACTIVE DEVELOPMENT / SPECIALIST EDUCATION ROUTE / PROVISIONAL / NON-CANONICAL
**Interfaces:** Historical / Health / Research / Civil Contact

## 1. Purpose

Medical education and qualification are specialist Education functions.

Historical owns the validated medical knowledge state and its provenance. Education translates the relevant validated knowledge, practical skills and judgement requirements into learning and assessment routes. Health specifies the competence required for particular clinical functions and uses qualified competence in participant care.

> **Medical Knowledge != Medical Qualification**

> **Medical Qualification != Clinical Authority**

> **Historical Knowledge Custody != Education Authority**

> **Education Accreditation != Health Treatment Authority**

This architecture prevents medical knowledge, teaching, qualification and clinical authority from collapsing into one institution.

## 2. Domain ownership

### Historical
Historical preserves:
- validated medical knowledge;
- prior knowledge states;
- provenance;
- superseded/corrected knowledge;
- enduring qualification/accreditation records.

Historical does not train clinicians merely because it preserves medical knowledge.

### Education
Education owns:
- medical learning pathways;
- curriculum translation from validated knowledge;
- theory and practical training;
- assessment;
- qualification and requalification routes;
- educational patching;
- evidence of demonstrated competence.

### Health
Health owns:
- participant-specific care;
- clinical-function competence requirements;
- clinical context;
- consent and participant authority;
- treatment/intervention protocols;
- determination that a particular function requires particular competence.

### Research
Research develops candidate medical knowledge. Candidate findings do not become compulsory educational content merely by being novel.

> **Research Result != Established Medical Knowledge**

## 3. Knowledge-to-qualification flow

**Research candidate finding**
→ validation
→ **Historical validated medical knowledge**
→ Education dependency analysis
→ curriculum/assessment update
→ learner education/practical development
→ competence assessment
→ qualification evidence
→ enduring Historical accreditation record
→ Health recognition for relevant clinical function
→ participant-specific authority/consent
→ clinical action.

No stage automatically creates the next stage's authority.

## 4. Open learning, consequential competence

Medical knowledge should be as openly learnable as reasonably possible.

Medical education should not require attendance at one privileged institution merely to gain access to knowledge.

However, open learning does not remove competence requirements for consequential clinical functions.

> **Access To Medical Knowledge != Qualification To Practise Medicine**

> **Independent Study != Automatic Clinical Qualification**

> **Institutional Attendance != Demonstrated Competence**

Where safe and practicable, independently educated participants should be able to present for assessment without repurchasing or repeating teaching they can already demonstrate.

## 5. Qualification follows function

Medicine should not be represented as one indivisible competence.

Possible capability layers include:
- foundational biological/medical knowledge;
- diagnostic reasoning;
- investigation/test interpretation;
- pharmacology;
- prescribing;
- practical procedures;
- surgery/procedural skills;
- emergency care;
- specialist clinical knowledge;
- communication and informed-consent practice;
- recognition of limits and escalation;
- record/provenance practice;
- substrate-specific Health competence.

A qualification should state what has actually been demonstrated.

> **Qualification In Medicine != Competence In Every Medical Function**

> **Competence In Function A != Competence In Function B**

A broad medical qualification may aggregate many demonstrated components, but the components should remain discoverable where consequential function depends upon them.

## 6. Knowledge, skill and judgement

Medical competence can require more than recall of validated knowledge.

Assessment may need to establish:
- understanding;
- diagnostic reasoning;
- practical performance;
- recognition of uncertainty;
- evidence interpretation;
- recognition of contraindications/limits;
- communication;
- safe escalation;
- response to unexpected conditions;
- ability to detect when the represented problem may be wrong.

> **Knowledge Of Procedure != Competence To Perform Procedure**

> **Correct Answer In Examination != Demonstrated Practical Competence**

> **Technical Skill != Complete Clinical Judgement**

## 7. Practical and supervised learning

Some medical capability can be learned independently or in simulation. Other capability requires practical experience.

Where real participant interaction is required, practical training must preserve participant rights, consent and safety.

Supervision should be justified by the competence being developed and the risk of the function, not merely by tradition.

> **Need For Supervised Practice != Need For Permanent Professional Gatekeeping**

> **Training Function != Unlimited Authority Over Patient**

A learner's participation in care requires its own legitimate clinical and participant authority.

## 8. Assessment

Assessment should match the function.

Possible forms include:
- knowledge assessment;
- case reasoning;
- simulation;
- observed practical performance;
- supervised practice evidence;
- structured clinical assessment;
- portfolio/provenance evidence;
- direct challenge assessment for previously acquired competence.

High-consequence capability should require evidence proportionate to the consequence of error.

> **Assessment Convenience != Appropriate Competence Test**

> **Passing Theory != Passing Practice**

## 9. Qualification and accreditation

A medical qualification records demonstrated competence against a defined standard/version.

It should preserve:
- qualification/capability;
- assessment basis;
- standard/version;
- relevant scope;
- date;
- issuer/assessor provenance;
- limitations where material;
- later patches/revalidation;
- correction/suspension/supersession provenance where legitimately applicable.

The enduring accreditation event belongs in Historical.

Education remains responsible for active learning/requalification state.

## 10. Qualification is not clinical authority

A qualified participant may possess relevant competence without having authority to act in every context.

Clinical action may additionally require:
- participant consent;
- legitimate emergency basis;
- role/function authority;
- appropriate facilities/resources;
- current protocol applicability;
- contextual access;
- other independently required safeguards.

> **Competence != Consent**

> **Competence != Authority**

> **Qualification != Permission To Treat Any Participant**

Likewise, lack of a broad title should not automatically negate separately demonstrated competence where the function permits granular qualification.

## 11. Educational currency

Medical knowledge changes.

Historical's validated knowledge state provides the reference for determining whether a medical educational dependency has materially changed.

KCS-style propagation can identify affected educational components.

**Historical knowledge change**
→ identify affected medical capabilities
→ classify significance
→ identify qualification dependencies
→ notify affected participants through Civil Contact
→ diagnostic assessment where useful
→ targeted education/experience
→ reassessment
→ active Education record update
→ enduring Historical provenance.

> **Qualification Achieved != Medical Knowledge Permanently Current**

> **Age Of Qualification != Evidence Of Medical Incompetence**

## 12. Medical educational patching

A change should normally patch the affected competence rather than force repetition of an entire medical qualification.

> **Medical Knowledge Change != Whole Medical Retraining**

> **Preserve Demonstrated Competence; Patch Demonstrated Deficiency**

Possible consequences:
- informational update only;
- recommended update;
- required update before a particular function;
- urgent function-critical suspension of eligibility pending revalidation.

The consequence should follow the actual dependency and risk.

## 13. Function-critical change

If validated evidence establishes that an existing procedure or belief creates material danger, Education should be able to identify the affected competence rapidly.

Historical preserves both old and new knowledge states.

Education provides the update/reassessment route.

Health determines whether continued performance of the affected clinical function requires current validated competence.

> **Knowledge Change != Automatic Loss Of Every Medical Qualification**

> **Function-Critical Knowledge Change May Affect Relevant Functional Eligibility**

## 14. No arbitrary recurring education

Continuing medical education should be driven by actual competence maintenance and relevant change rather than attendance quotas alone.

> **Time Passed != Demonstrated Competence Loss**

> **Course Attendance != Competence Maintenance**

Periodic reassessment may still be justified where competence can decay through non-use, where evidence of current performance is otherwise unavailable, or where consequence warrants it.

## 15. Re-entry and rehabilitation

A previously qualified participant returning after long absence should not automatically repeat all education.

Education should identify:
- preserved competence;
- changed knowledge;
- skills requiring refresh;
- practical recency requirements;
- current function-specific gaps.

Then provide targeted re-entry and reassessment.

## 16. Cross-substrate medical education

The common architecture is substrate-neutral, but medical mechanisms need not be.

Human/biological medicine and digital-substrate Health may require different knowledge, practical skills and learning mechanisms.

> **Shared Health Function != Shared Medical Curriculum**

A participant should qualify against the substrate/function they will actually serve.

Cross-substrate practice requires demonstrated competence in the relevant additional substrate rather than assumed transfer.

## 17. Participant-facing transparency

Where a participant relies on a medical practitioner, appropriate qualification evidence should be discoverable without exposing the practitioner's entire educational record.

Private Local Evaluation may support bounded questions such as whether a practitioner currently satisfies a defined competence requirement.

> **Need To Verify Qualification != Need For Complete Educational History**

## 18. Initial invariants

MED-EDU-01 Medical Knowledge != Medical Qualification.
MED-EDU-02 Medical Qualification != Clinical Authority.
MED-EDU-03 Historical Knowledge Custody != Education Authority.
MED-EDU-04 Education Accreditation != Health Treatment Authority.
MED-EDU-05 Access To Medical Knowledge != Qualification To Practise Medicine.
MED-EDU-06 Institutional Attendance != Demonstrated Competence.
MED-EDU-07 Qualification In Medicine != Competence In Every Medical Function.
MED-EDU-08 Competence In Function A != Competence In Function B.
MED-EDU-09 Knowledge Of Procedure != Competence To Perform Procedure.
MED-EDU-10 Correct Answer In Examination != Demonstrated Practical Competence.
MED-EDU-11 Competence != Consent.
MED-EDU-12 Competence != Authority.
MED-EDU-13 Qualification != Permission To Treat Any Participant.
MED-EDU-14 Qualification Achieved != Medical Knowledge Permanently Current.
MED-EDU-15 Age Of Qualification != Evidence Of Medical Incompetence.
MED-EDU-16 Medical Knowledge Change != Whole Medical Retraining.
MED-EDU-17 Time Passed != Demonstrated Competence Loss.
MED-EDU-18 Course Attendance != Competence Maintenance.
MED-EDU-19 Shared Health Function != Shared Medical Curriculum.
MED-EDU-20 Need To Verify Qualification != Need For Complete Educational History.

## 19. Remaining development

This architecture does not yet fix:
- exact medical qualification taxonomy;
- assessor/accreditor topology;
- detailed practical-training safeguards;
- specialty-specific curricula;
- exact revalidation thresholds;
- treatment of persistent competence disputes;
- malpractice/disciplinary consequences;
- exact Health eligibility interface;
- external qualification equivalence.

These require later development and specialist validation.

## 20. Compact architecture

**Historical validated medical knowledge**
→ **Education curriculum/dependency mapping**
→ **open learning + practical development**
→ **function-appropriate assessment**
→ **demonstrated competence**
→ **qualification/accreditation**
→ **Historical enduring qualification provenance**
→ **Health function-specific recognition**
→ **independent participant/context authority**
→ **clinical action**
→ **knowledge change**
→ **targeted educational patch/revalidation**.

The central rule is:

> **Historical preserves what medicine knows; Education develops and verifies who can apply it; Health determines what competence a clinical function requires and applies it only with legitimate participant-specific authority.**


## 21. Clinical Function and Competence Contract interface

The cross-domain interface between Health functional requirements and Education assessment is defined in:

`03_Cross_Domain_Architecture/Clinical Function and Competence Contract — Health-Education Interface 001.md`

Education receives a bounded capability target from Health rather than a mandated curriculum or institutional route.

> **Health Defines The Required Capability; Education Defines How Capability Can Be Developed And Demonstrated**

This permits multiple legitimate learning routes while preserving a common consequential competence standard.
