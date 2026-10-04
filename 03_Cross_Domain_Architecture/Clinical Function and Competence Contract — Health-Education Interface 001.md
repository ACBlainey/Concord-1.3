# Clinical Function and Competence Contract — Health-Education Interface 001

**Date:** 4 October 2026
**Status:** CROSS-DOMAIN INTERFACE / PROVISIONAL / NON-CANONICAL
**Domains:** Health / Education / Historical
**Purpose:** Define how a Health clinical function creates an assessable competence requirement without transferring curriculum ownership to Health or clinical authority to Education.

## 1. Problem

Health must be able to state what capability is required to perform a consequential clinical function.

Education must be able to turn that requirement into learning and assessment.

Historical must be able to preserve the validated medical knowledge and qualification provenance on which both depend.

Without an explicit interface, two opposite failures are possible:
- Health silently becomes the education/licensing authority; or
- Education defines clinical practice merely because it controls qualification.

Neither is acceptable.

> **Function Ownership != Education Ownership**

> **Qualification Ownership != Clinical Function Ownership**

## 2. Clinical Function and Competence Contract

A **Clinical Function and Competence Contract (CFCC)** is the bounded interface object between Health and Education.

It is not an employment contract and does not itself authorise treatment.

A CFCC should identify, proportionately:

- FunctionRef;
- FunctionName;
- ClinicalPurpose;
- Scope;
- Substrate/Population scope where material;
- Consequence/Risk class;
- Knowledge dependencies;
- Reasoning/judgement capabilities;
- Practical capabilities;
- Recognition-of-limit/escalation capabilities;
- Required supervised experience where justified;
- Required assessment evidence classes;
- Currency/freshness requirements;
- Function-critical patch dependencies;
- resource/facility dependencies relevant to competence;
- protocol dependencies where applicable;
- version;
- effective date;
- review triggers;
- provenance.

## 3. Ownership of fields

Health owns the **functional requirement**:
what must a competent actor be able to do for this clinical function?

Education owns the **educational response**:
how can that capability be learned, practised and validly assessed?

Historical owns the **knowledge/provenance reference**:
what validated medical knowledge state and enduring qualification evidence support the requirement?

> **Health Defines The Required Capability; Education Defines How Capability Can Be Developed And Demonstrated**

Health may identify clinically necessary assessment properties, such as the need to demonstrate a practical procedure under realistic conditions. It should not require attendance at a named institution where equivalent competence can legitimately be demonstrated another way.

Education may design multiple valid routes to the same competence target. It should not lower or redefine the Health function merely to make assessment easier.

## 4. Protocol relationship

A Health protocol may reference one or more CFCC competence requirements.

This resolves the existing protocol field **CompetenceRequirements** without embedding an entire educational system in each protocol.

Conceptually:

**HealthProtocol.CompetenceRequirements**
→ **CFCC reference(s)**
→ Education qualification/capability evidence
→ current currency/patch state
→ competence condition satisfied / unresolved / not satisfied.

> **Protocol Competence Requirement != Curriculum**

> **Qualification Evidence != Protocol Applicability**

A participant may be competent to execute a protocol while the protocol is still inapplicable to the current patient.

## 5. Granularity

A CFCC should be no broader than necessary to represent the clinical function.

Examples may range from:
- taking a particular specimen;
- interpreting a defined diagnostic test;
- prescribing within a bounded protocol;
- administering a medicine;
- performing a procedure;
- providing emergency stabilisation;
- conducting a specialist diagnostic function;
- performing a complex surgical function.

This does not require every action to become a separate qualification. Education may compose related CFCCs into useful qualifications.

> **Granular Function Requirements May Compose Into Qualifications; Qualification Composition Does Not Erase Functional Boundaries**

## 6. Composition

A qualification can attest competence across multiple functions.

But:

> **Authorised Qualification Components != Automatic Competence For Every Composite Clinical Situation**

Where a composite clinical function creates additional judgement, interaction or consequence, the composite itself may require assessment.

This mirrors the wider Concord rule that authorised parts do not automatically authorise every composition.

## 7. Assessment equivalence

Education may accept different evidence routes where they demonstrate the same required competence to an appropriate standard.

Possible routes include formal study, apprenticeship, supervised practice, simulation, prior experience, independent study plus direct assessment, recognised equivalent qualification or substrate-appropriate capability validation.

> **Equivalent Competence Evidence != Identical Learning History**

Equivalence must be demonstrated, not assumed.

## 8. Currency

A CFCC can identify which capability dependencies are time-sensitive, change-sensitive or practice-sensitive.

Possible currency bases:
- knowledge-state change;
- protocol change;
- non-use/skill decay;
- changed equipment or environment;
- safety evidence;
- changed substrate/population;
- observed competence concern.

> **Currency Requirement Should Follow The Capability Dependency, Not An Arbitrary Calendar Alone**

## 9. Change propagation

When Historical's validated medical knowledge changes:

**Historical knowledge change**
→ KCS dependency resolution
→ affected Health protocols and CFCCs identified
→ Health reviews whether functional requirement changed
→ Education reviews affected learning/assessment dependency
→ affected qualifications/capabilities identified
→ participant notification/patch/reassessment where required.

A knowledge change may affect:
- neither;
- curriculum only;
- protocol only;
- competence requirement only;
- several together.

> **Shared Upstream Change != Identical Downstream Change**

## 10. Qualification verification

For a clinical episode Health ordinarily needs to know whether the relevant competence requirement is currently satisfied, not inspect the entire educational record.

Possible result states:
- SATISFIED;
- SATISFIED_WITH_SCOPE_LIMIT;
- SUPERVISION_REQUIRED;
- PATCH_REQUIRED;
- REASSESSMENT_REQUIRED;
- NOT_SATISFIED;
- EVIDENCE_INCOMPLETE;
- UNKNOWN.

PLE may support minimum-disclosure verification.

> **Competence Verification != Educational Record Transfer**

## 11. Learners

A learner may satisfy some CFCC components while still requiring supervision for others.

Training therefore should be capable of bounded participation:

**demonstrated learner capability + supervised scope + participant consent/authority + accountable supervisor + escalation boundary**.

> **Learner != Unqualified For Everything**

> **Partial Competence != Independent Competence**

## 12. Exceptional and emergency conditions

Emergency conditions may change which competence is sufficient for a particular bounded action, especially where no better-qualified actor is available and delay itself creates harm.

But emergency does not manufacture expertise.

> **Emergency May Alter The Minimum Justifiable Action Threshold; It Does Not Create Competence**

Any exceptional use should remain bounded by necessity, proportionality, actual capability and available alternatives.

## 13. Clinical outcome and competence review

An adverse outcome can trigger review of competence, protocol, diagnosis, system conditions or other causes.

It does not prove incompetence.

Likewise, a successful outcome does not prove competence.

> **Adverse Outcome != Proof Of Incompetence**

> **Successful Outcome != Proof Of Competence**

Mirrored Reality Trees can help distinguish candidate causes rather than treating the practitioner as the default explanation.

## 14. Boundary with discipline and liability

CFCC describes competence requirements and evidence interfaces.

It does not determine:
- misconduct;
- negligence;
- criminal liability;
- employment discipline;
- participant compensation;
- professional exclusion.

Those require their own lawful/evidential processes.

> **Competence Review != Presumption Of Misconduct**

## 15. Compact interface

**Historical validated medical knowledge**
→ **Health clinical function/protocol**
→ **CFCC competence requirement**
→ **Education learning/assessment routes**
→ **demonstrated competence**
→ **qualification/accreditation provenance**
→ **minimum-disclosure current competence verification**
→ **separate participant/context/protocol authority**
→ **clinical action**.

## 16. Core invariants

CFCC-01 Function Ownership != Education Ownership.
CFCC-02 Qualification Ownership != Clinical Function Ownership.
CFCC-03 Protocol Competence Requirement != Curriculum.
CFCC-04 Qualification Evidence != Protocol Applicability.
CFCC-05 Equivalent Competence Evidence != Identical Learning History.
CFCC-06 Competence Verification != Educational Record Transfer.
CFCC-07 Partial Competence != Independent Competence.
CFCC-08 Emergency Does Not Create Competence.
CFCC-09 Adverse Outcome != Proof Of Incompetence.
CFCC-10 Successful Outcome != Proof Of Competence.
CFCC-11 Competence Review != Presumption Of Misconduct.
CFCC-12 Qualification != Clinical Authority.

## 17. Development status

This interface resolves ownership and information flow.

It does not yet establish:
- a universal clinical-function taxonomy;
- exact consequence/risk classes;
- assessment thresholds;
- specialty-specific CFCCs;
- legal liability standards;
- accreditor topology;
- deployment schema.

Those can be developed without changing the domain ownership established here.
