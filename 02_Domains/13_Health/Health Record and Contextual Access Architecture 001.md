# Health Record and Contextual Access Architecture 001

**Project:** The Concord Framework
**Date:** 3 October 2026
**Status:** ACTIVE HEALTH ARCHITECTURE / PROVISIONAL / NON-CANONICAL / IMPLEMENTATION AND LEGAL VALIDATION REQUIRED
**Domain:** Health
**Primary dependencies:** Contextual Wrapper Architecture / Concord Information Black Box / Bounded Contextual Authority / Health Core Architecture / Health Service Topology / BTA
**Primary interfaces:** Historical / Research / Law / Civil Security / Continuity / Pharmacy / Diagnostic Services

## 1. Purpose

Concord Health requires a longitudinal record that serves the participant across preventive monitoring, diagnosis, testing, treatment, rehabilitation and continuing care without turning medical employment or institutional membership into general authority over that record.

The architecture therefore separates:

- custody of the authoritative record;
- participant access;
- Health-function access;
- contextual projection;
- contribution/edit authority;
- disclosure;
- exceptional access;
- archival/historical custody.

> **Professional Status != General Health-Record Access**

> **Care Relationship -> Bounded Contextual Access**

## 2. Source resolution

This architecture reuses existing Concord mechanisms rather than creating a separate Health permission system.

Contextual Wrapper Architecture already treats medical records as informational contexts and establishes:

> **Boundary != Access != Rules != Authority**

> **Contextual Permission != General Permission**

and the function-derived grammar:

**Legitimate Function -> Required Interaction -> Need for Permission -> Minimum Necessary Permission -> Bounded Contextual Access**

The Concord Information Black Box establishes one authoritative protected object with governed projections:

**User Access -> Projection(Master, Context)**

rather than ordinary unrestricted master possession.

It also separates read, edit, structural, control and lifecycle authority.

Health therefore supplies the domain-specific rules governing which medical functions legitimately require which projections and operations.

## 3. Participant-centred longitudinal record

A participant should have a longitudinal Health record capable of connecting:

- routine monitoring;
- participant-entered observations;
- diagnostic episodes;
- test results;
- diagnoses and diagnostic uncertainty;
- treatment;
- medications/supports;
- allergies/intolerances;
- procedures;
- rehabilitation;
- continuing support;
- preventive review;
- relevant Health alerts;
- provenance;
- access history;
- corrections/contestation.

The record exists to support the participant's Health across time rather than to belong to a particular clinic, GP, hospital or professional.

> **Record Custody != Provider Ownership**

> **Provider Contribution != Provider Ownership**

## 4. Authoritative master and projections

The authoritative longitudinal record should remain inside the protected Health information boundary.

Ordinary Health actors receive contextual projections rather than unrestricted copies of the master.

A projection is generated from:
- participant identity;
- active Health function;
- professional/service role;
- relevant episode;
- necessary information;
- consent or other legitimate basis;
- time;
- contextual restrictions.

> **Access To A Projection != Access To The Master**

> **Access To One Record Section != Access To Every Record Section**

This is especially important where Health records contain sensitive information whose relevance differs by episode.

## 5. Participant access

The participant should ordinarily be able to inspect their own Health information, including:

- measurements and trends;
- test results;
- diagnoses and working hypotheses;
- treatment history;
- medication/support state;
- clinical notes where lawfully appropriate;
- provenance;
- access history;
- corrections and disputes;
- active contextual access relationships.

The participant should not need a clinician appointment merely to obtain ordinary access to their own result or record.

> **Participant Record Access != Provider Permission**

Narrow exceptions may exist where another person's protected information, system-security information or another independently protected interest is embedded in the same record. Such exceptions require separate justification and should favour projection/redaction over blanket denial.

## 6. Health-function access

A Health professional or service obtains access because a legitimate Health function requires it.

Examples include:
- diagnosis;
- test selection/safety;
- test interpretation;
- treatment;
- medication reconciliation;
- procedure;
- rehabilitation;
- emergency care;
- continuing support.

The relationship should be represented explicitly:

**Participant P -> Health Function F -> Actor/Service A -> Necessary Record Scope S -> Legitimate Basis B -> Time T -> Permitted Operations O**

> **Need To Know != Right To Browse**

A professional's licence or employment proves competence/role where relevant; it does not itself establish a current need to inspect a particular participant's record.

## 7. Context activation

Ordinary contextual record access may activate when the participant:

- requests or attends care;
- self-refers;
- authorises a diagnostic service;
- begins a treatment relationship;
- requests a professional review;
- transfers to another Health service;
- otherwise legitimately establishes the Health function.

Where consent is the basis, it should be intelligible and appropriately scoped.

The system should make the active context visible to the participant where reasonably possible.

## 8. Minimum-necessary projection

The projection should contain information reasonably necessary for the actual function.

Examples:

A diagnostic imaging service may need the diagnostic question, relevant symptoms, contraindications, previous relevant imaging/exposure and selected clinical history.

A pharmacist may need the valid therapeutic authorisation, medication list, allergies, material interactions and relevant functional/laboratory state.

A specialist may need a wider episode history and selected longitudinal trends.

> **More Medical Information != Automatically Better Contextual Access**

The system may allow the professional to request expansion where additional information becomes materially necessary. Expansion itself should be provenance-visible.

## 9. Read, contribute and modify are separate

Health-record operations should distinguish at least:

- READ;
- CONTRIBUTE_NEW_ENTRY;
- PROPOSE_CORRECTION;
- AMEND_OWN_ENTRY;
- SUPERSEDE_CLINICAL_INTERPRETATION;
- ANNOTATE;
- DISCLOSE;
- EXPORT;
- AUTHORISE_ACCESS;
- RESTRICT_CONTEXT;
- ARCHIVE;
- RETIRE/DESTROY where lawful.

> **Read Authority != Edit Authority**

> **Clinical Contribution Authority != Record-Control Authority**

Ordinary clinicians should not silently rewrite historical observations merely because their current interpretation differs.

## 10. Append, correct, supersede

Clinical records should preserve provenance.

Where a factual error is corrected, the system should preserve appropriate correction history.

Where a diagnosis changes, the earlier diagnosis should ordinarily be marked as corrected, superseded, disputed or no longer supported rather than silently erased where its prior existence remains clinically/provenance relevant.

This is important because:

> **Clinical Consensus != Independent Evidence**

and:

> **Repeated Restatement Of Diagnosis != Corroboration**

The record should distinguish original evidence from copied/inherited interpretations.

## 11. Participant correction and contestation

A participant should be able to:

- identify factual error;
- add relevant contextual information;
- dispute an interpretation;
- request correction;
- see whether a correction was accepted, rejected or remains disputed;
- seek review.

Participant disagreement does not automatically erase professional evidence, and professional disagreement does not eliminate the participant's ability to record contestation.

> **Record Dispute != Permission To Destroy Provenance**

## 12. Relationship termination

When the legitimate care function ends, ordinary active access should contract or terminate.

Examples:
- consultation complete;
- diagnostic episode complete;
- participant changes provider;
- treatment relationship ends;
- referral is declined;
- temporary service finishes.

The professional's contributed record remains part of the participant's longitudinal history where appropriate, but active browsing authority does not persist merely because care once occurred.

> **Past Care != Permanent Future Access**

> **Continuity Of Record != Continuity Of Authority**

A continuing-care relationship may legitimately maintain bounded continuing access where the function genuinely persists.

## 13. Handoff and transfer

Care transfer should use BTA principles.

A handoff may transfer:
- relevant clinical state;
- active questions;
- current treatment;
- pending tests;
- necessary record projection;
- provenance.

It does not automatically transfer:
- every prior permission;
- every consent;
- unrestricted record access;
- unrelated provider authority.

> **Care Transfer != Authority Transfer**

> **Record Transfer != Consent Transfer**

The receiving context establishes its own legitimate basis and necessary scope.

## 14. Emergency access

A genuine emergency may justify access that could not reasonably be obtained through ordinary participant authorisation where delay would create material danger and the applicable Health/Law architecture permits it.

Emergency access should be:
- minimum necessary;
- purpose-bounded;
- time-bounded;
- automatically logged;
- visibly classified as exceptional;
- reviewed afterward;
- terminated when the emergency basis ends.

> **Emergency Access != General Record Access**

> **Past Emergency Authority != Current Authority**

Where feasible, the participant should be informed afterward that exceptional access occurred and why.

## 15. Incapacity and supported decision-making

Temporary inability to manage record permissions does not transfer ownership of the record.

Supported decision-making should be used where feasible.

A representative or temporary authority holder receives only the permissions legitimately required by that role.

> **Decision Support != Record Ownership**

> **Temporary Representation != Permanent Information Sovereignty**

## 16. Diagnostic and automated-system access

Smart Diagnostic Navigation, longitudinal monitoring and protocol-driven treatment may require access to Health data.

Automated systems should receive only the data scope required for their declared Health function.

Their access should identify:
- system identity/version;
- purpose;
- input scope;
- derived outputs;
- provenance;
- retention;
- onward-use restrictions.

> **Automated Health Function != General Machine Access To Health Record**

Derived diagnostic outputs return to the participant's Health record with their provenance and uncertainty state.

## 17. Research boundary

Clinical information does not become Research data merely because it would be useful.

> **Health Record Collection != Research Consent**

Research access requires its own legitimate basis, projection/transformation and governance.

Where de-identification, aggregation or another transformation is used, the Information Black Box should preserve protection-relevant lineage until the resulting information state is legitimately established.

> **Clinical Access != General Research Access**

Research discoveries do not automatically create clinical authority or notification authority.

## 18. Historical interface

Health owns the active clinical function.

Historical may preserve appropriately governed long-term records/provenance according to Concord archival architecture.

Transfer to archival custody must preserve:
- participant protections;
- access restrictions;
- provenance;
- legal retention state;
- contestation/correction history;
- required future Health retrieval interface.

> **Archival Custody != Public Access**

> **Historical Preservation != Loss Of Health Confidentiality**

## 19. Civil Security, Law and external authority

Health records should not become a general-purpose civil surveillance source.

Lawful non-Health access, where it exists, requires independently legitimate authority and should be separately represented and audited.

> **Health Purpose != Police Purpose**

> **Technical Availability != Lawful Disclosure Authority**

A Health professional should not be forced to infer legal disclosure authority from a requester's status alone.

## 20. Access audit

Material access should generate an audit event including, proportionately:

- actor/service;
- participant record;
- function/purpose;
- basis;
- scope;
- operation;
- time;
- expansion request if any;
- exceptional/emergency state;
- onward disclosure where applicable.

The participant should ordinarily be able to inspect meaningful access history.

Audit information itself may require protection against revealing unrelated protected operational/security information.

## 21. Break-glass access

Where implementation requires a break-glass mechanism, it should not mean unrestricted administrator access.

It is an exceptional state requiring:
- declared reason;
- authenticated actor;
- bounded purpose;
- minimum scope;
- expiry;
- automatic logging;
- review.

The Concord Information Black Box rule applies:

> **Exceptional Direct Master Access Is A State, Not A Normal Role**

## 22. Privacy against browsing and curiosity

Professional access controls should prevent record browsing based merely on:
- professional curiosity;
- celebrity/public interest;
- friendship/family connection;
- organisational membership;
- prior care;
- technical capability.

> **Ability To Find A Record != Authority To Open It**

## 23. Family and relational access

Family relationship does not automatically create unrestricted record access.

Where the participant authorises a family member/supporter, or where a legitimate representative role exists, access remains scope- and function-bounded.

Different sections may legitimately have different visibility.

> **Relationship != Universal Health-Record Permission**

## 24. Longitudinal monitoring privacy

Routine sensors may create dense longitudinal data.

Collection for Health monitoring does not automatically authorise every professional to inspect raw continuous telemetry.

Relevant trends, alerts or bounded data windows may be projected where they satisfy the active function.

> **Longitudinal Collection != Universal Professional Visibility**

> **Health Monitoring != General Participant Surveillance**

## 25. Data-source separation

The record should distinguish:
- participant-entered information;
- sensor/device data;
- laboratory/diagnostic results;
- professional observations;
- professional interpretations;
- automated-system interpretations;
- imported external records;
- Research-derived information legitimately returned to care.

This prevents an interpretation from masquerading as a primary observation.

## 26. External Health providers

Where a participant uses non-Concord or external Health services, the system should support bounded import/export where technically and legally possible.

External interoperability should preserve:
- provenance;
- source;
- date;
- uncertainty;
- access purpose;
- participant choice where applicable.

External provider format should not determine internal semantic ownership.

## 27. Failure and degraded operation

Health must remain operable when parts of the record system are unavailable.

Possible states include:
- complete relevant projection available;
- partial record available;
- stale record;
- external record pending;
- authority verification unavailable;
- provenance unresolved.

> **Missing Record != Permission To Assume Normality**

> **System Failure != Automatic Permission For Unrestricted Access**

Emergency degraded operation requires its own bounded policy.

## 28. Security and backup

Backups should preserve the protected information state.

Backup existence must not create a less-governed copy through which contextual controls can be bypassed.

> **Backup Copy != Unwrapped Copy**

Recovery should restore both information and required protection/control state.

## 29. Minimum contextual-access record

A Health access context should be capable of representing:

**HealthAccessContext**
- ContextRef
- ParticipantRef
- ActorOrServiceRef
- HealthFunction
- EpisodeRef where applicable
- LegitimateBasis
- PermittedDataScope
- PermittedOperations
- Start
- Review/Expiry
- EmergencyState if any
- ExpansionHistory
- DisclosureConstraints
- Provenance
- TerminationState

This is conceptual rather than an implementation schema.

## 30. Core invariants

> **Professional Status != General Health-Record Access**

> **Care Relationship -> Bounded Contextual Access**

> **Record Custody != Provider Ownership**

> **Provider Contribution != Provider Ownership**

> **Access To A Projection != Access To The Master**

> **Need To Know != Right To Browse**

> **Read Authority != Edit Authority**

> **Past Care != Permanent Future Access**

> **Continuity Of Record != Continuity Of Authority**

> **Care Transfer != Authority Transfer**

> **Record Transfer != Consent Transfer**

> **Emergency Access != General Record Access**

> **Health Record Collection != Research Consent**

> **Archival Custody != Public Access**

> **Health Purpose != Police Purpose**

> **Ability To Find A Record != Authority To Open It**

> **Longitudinal Collection != Universal Professional Visibility**

> **Backup Copy != Unwrapped Copy**

## 31. Remaining development

This architecture establishes the civil information model but does not yet settle:
- exact legal retention periods;
- jurisdiction-specific disclosure law;
- detailed clinical-note categories;
- minor/dependent participant access rules;
- post-death access;
- genetic/familial information conflicts;
- exact emergency thresholds;
- external-provider interoperability standards;
- cryptographic/technical implementation;
- Health-specific anonymisation/de-identification standards;
- operational access-control testing.

These require dedicated Health/Law/Historical/technical development rather than inference.
