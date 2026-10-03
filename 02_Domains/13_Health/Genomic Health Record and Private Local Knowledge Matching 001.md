# Genomic Health Record and Private Local Knowledge Matching 001

**Project:** The Concord Framework
**Date:** 3 October 2026
**Status:** ACTIVE HEALTH/HISTORICAL/RESEARCH ARCHITECTURE / PROVISIONAL / NON-CANONICAL / SECURITY, GENETIC AND LEGAL VALIDATION REQUIRED
**Domains:** Health / Historical / Research
**Primary dependencies:** Health Record and Contextual Access Architecture / Medical Knowledge Stewardship / Contextual Wrapper Architecture / Concord Information Black Box / KCS Change Propagation / Historical participant-record architecture

## 1. Purpose

A participant genome can be medically valuable across an entire lifetime, but genomic information creates an unusually difficult privacy problem.

A genome is not ordinary anonymous medical data. It is deeply identifying, persistent, biologically relational and capable of acquiring new meaning as medical knowledge advances.

The Concord should therefore avoid architectures that depend on repeatedly searching a central population genomic dataset to discover which participants match each newly identified genetic risk.

The preferred relation is:

> **Move The Medical Question To The Protected Genome; Do Not Move The Genome To The Question**

## 2. Domain ownership

The genome has overlapping functions that must remain separated.

### Historical
Historical provides protected long-term custody and provenance for the participant's durable genomic record as part of the participant lifecycle record architecture.

### Health
The genome is available to the participant's Health record as a protected longitudinal Health information component for participant-specific diagnosis, prevention, treatment and risk interpretation.

### Research
Research develops candidate and validated knowledge about relationships between genetic features and Health outcomes.

Research does not gain general access to participant genomes merely because its discoveries are relevant to them.

> **Genomic Custody != General Genomic Access**

> **Research Knowledge About A Variant != Authority To Search Participants For That Variant**

## 3. Genome as a protected participant record component

The participant's genomic data should be treated as a specially protected component of the longitudinal Health record, with Historical continuity/provenance custody.

This does not require multiple unrestricted copies.

A protected authoritative genomic object may support bounded Health projections and local computation while remaining inside the participant's protected record wrapper.

> **Health Use Of Genome != Public Genomic Database**

> **Historical Custody Of Genome != Historical Permission To Inspect Genome For Arbitrary Purposes**

## 4. Genomic data cannot be assumed anonymous

Genomic information should not be treated as safely anonymous merely because obvious civil identifiers have been removed.

Its sequence itself can be identifying, and it may reveal information about biologically related participants.

Therefore:

> **Removal Of Name != Genomic Anonymisation**

> **Pseudonymised Genome != Non-Identifying Genome**

Any Research architecture that uses participant genomic material must treat re-identification and relational disclosure as material risks rather than assuming conventional anonymisation solves them.

## 5. Local private knowledge matching

When validated medical knowledge identifies a new genomic risk relation, the default Health route should be local matching inside each participant's protected record environment.

Conceptually:

**Research identifies candidate gene/variant relation**
→ validation
→ Historical validated medical knowledge state updated
→ KCS identifies genomic Health matching rule as relevant downstream knowledge
→ signed/versioned bounded genomic query distributed
→ participant protected Health record receives query
→ query executes locally against protected genome
→ MATCH or NO_MATCH evaluated internally
→ if NO_MATCH: query result discarded/closed as non-relevant
→ if MATCH: participant-facing Health system creates a private Health relevance event
→ participant is informed and offered appropriate Health interpretation/action.

The originating Research function does not need to receive the identity of matching participants.

> **Query Distribution != Genome Disclosure**

> **Local Match != External Match Disclosure**

## 6. Minimum-disclosure principle

The ordinary output of the distributed query should remain inside the participant record.

For a non-match, no external participant-specific result is required.

For a match, the result becomes relevant to that participant's Health system and participant.

External reporting should occur only where another independently legitimate purpose exists.

This yields:

> **No Match -> No Participant-Specific External Disclosure**

> **Match -> Participant Health Relevance, Not Automatic Research Disclosure**

## 7. Query object

A distributed genomic Health query should be bounded and auditable.

Conceptually:

**GenomicHealthQuery**
- QueryRef
- KnowledgeStateRef
- VariantOrPatternDefinition
- HealthAssociation
- EvidenceState
- RiskDirection
- Effect/Confidence Information
- ApplicablePopulation/Context
- InterpretationLimits
- ParticipantNotificationRule
- RecommendedHealthReviewRule
- Version
- EffectiveFrom
- Review/Expiry
- Provenance
- Signature/Integrity Evidence

The query should contain only what is needed to evaluate the Health relation.

## 8. Query authority and authenticity

The ability to distribute executable queries into protected participant records is consequential.

Only a legitimately governed Health knowledge-update route should be able to do so.

A Research paper, company, clinician or external actor should not be able to inject arbitrary genomic queries directly.

> **Knowledge Publication != Authority To Execute Population-Wide Private Queries**

The query should be authenticated, versioned and traceable to the validated Historical knowledge state and applicable Health protocol.

## 9. Local execution boundary

The query engine should be designed so that the protected genome need not leave its wrapper for ordinary matching.

The external query should not gain general read access to the genome.

The computation should expose only the minimum output required by the participant's own Health system.

> **Ability To Ask A Bounded Genomic Question != Ability To Read The Genome**

This is a Contextual Wrapper / Information Black Box application.

## 10. Participant notification

A positive local match should not be treated as a diagnosis.

Depending on the validated knowledge, it may indicate:
- increased risk;
- decreased risk;
- carrier status;
- altered treatment response;
- altered monitoring need;
- diagnostic relevance;
- uncertain but material association.

> **Genetic Association != Diagnosis**

The participant-facing Health system should communicate:
- what was found;
- what the association means;
- strength/limits of evidence;
- absolute as well as relative risk where known and relevant;
- whether confirmatory testing is needed;
- available preventive/diagnostic/treatment options;
- whether professional interpretation is recommended.

## 11. Right not to receive some genomic information

Genomic knowledge can include serious, uncertain or non-actionable findings.

A participant may reasonably have preferences about whether particular categories of future genomic findings should be surfaced.

The architecture should therefore support prospective notification preferences where ethically and legally appropriate.

Possible categories might include:
- actionable preventable risk;
- actionable treatment-response information;
- serious non-actionable risk;
- carrier/reproductive information;
- uncertain findings.

Exact rules require further development.

> **Ability To Discover != Automatic Duty To Reveal Every Possible Finding**

Emergency or other exceptional boundaries require separate justification.

## 12. Participant-directed genomic interrogation

The same local architecture can permit the participant or their authorised Health function to ask bounded questions of their genome without exporting the whole genomic object.

Examples:
- does this known pharmacogenomic marker apply?
- does this validated inherited-risk rule apply?
- is this variant relevant to the current diagnostic Reality Tree?

> **Participant Health Question != Requirement To Expose Complete Genome**

## 13. Familial information

Genomic information differs from many other records because one participant's genome can reveal probabilistic information about relatives.

A participant owns their own record and Health relationship, but their genome can carry implications beyond themselves.

This creates a genuine unresolved rights/interface problem.

A positive finding affecting relatives does not automatically authorise disclosure of the participant's genome or diagnosis to those relatives.

Where possible, the preferred architecture should communicate independently useful knowledge without exposing the source participant.

For example, a validated variant-risk rule can be distributed to every participant's protected record, allowing relatives to discover their own status locally.

> **Shared Biological Relevance != Shared Record Access**

> **Familial Relevance != Automatic Familial Disclosure Authority**

## 14. Research use

Research may require genomic datasets for discovering new associations.

That is a separate function from the private local matching architecture.

Research access must have its own legitimate basis, consent/governance and privacy/security model.

Because genomes cannot be assumed truly anonymous:

> **Genomic Research Requires More Than Ordinary Anonymisation Assumptions**

Where possible, privacy-preserving methods should reduce unnecessary central exposure, but no technical method should be labelled anonymous unless its actual re-identification properties justify that claim.

## 15. Aggregate learning

The local-matching architecture does not inherently need to report aggregate match counts.

If Research needs prevalence, penetrance or outcome information, that is a separate Research question requiring an appropriate governed aggregation mechanism.

> **Need For Population Statistics != Authority For Participant-Level Disclosure**

Aggregate computation should minimise exposure and preserve the distinction between:
- asking whether a participant's Health is affected;
- studying a population.

## 16. Outcome feedback

A participant who matches a variant may later generate clinically valuable outcome information.

With appropriate governance, Research may study such outcomes.

The route remains:

**participant Health outcome**
→ separately governed Research interface
→ Research analysis
→ validation
→ Historical knowledge update
→ revised bounded Health query/protocol.

The local matcher does not silently become a Research collection agent.

## 17. Knowledge change and re-evaluation

Genetic interpretation changes over time.

A variant may move from uncertain to significant, significant to benign, or acquire a different treatment implication.

KCS should therefore support bounded re-evaluation when Historical's validated genomic knowledge state changes.

> **Genome May Be Stable While Meaning Changes**

A participant does not need to be resequenced merely because interpretation changes if the relevant genomic information is already available and sufficiently reliable.

## 18. Query withdrawal and correction

If a genomic association is later corrected or withdrawn:
- Historical preserves the change;
- KCS identifies affected Health rules;
- the prior query is retired/superseded;
- participant Health records that generated a relevant event can be re-evaluated;
- prior clinical consequences remain historically traceable.

> **Knowledge Correction != Silent Erasure Of Prior Clinical State**

## 19. Data minimisation

A genomic record should not be routinely projected in full where a bounded derived answer is sufficient.

For example, a medication system may need:

**marker indicates altered metabolism: YES/NO/UNRESOLVED**

rather than the participant's complete sequence.

> **Derived Clinical Answer May Be Sufficient Where Raw Genome Is Not Needed**

## 20. Professional access

Even an active clinician should not automatically receive unrestricted genome access.

The active Health function should determine whether the clinician needs:
- a specific derived result;
- selected loci;
- a bounded genomic interpretation;
- broader genomic information.

> **Clinical Relationship != Automatic Whole-Genome Access**

## 21. Civil Security and identity use

The existence of a genomic record for Health/Historical continuity must not silently turn it into a general forensic identification database.

Any Civil Security or legal access would require independently established authority and must not be inferred from technical availability.

> **Health Genome != General Forensic Database**

> **Technical Match Capability != Forensic Authority**

## 22. Backup and continuity

Because the genome is durable and potentially irreplaceable as a record, continuity protection may be strong.

Backups must retain the same wrapper/protection semantics.

> **Genomic Backup != Unrestricted Genomic Copy**

Recovery must restore both data and protection state.

## 23. Security assumptions

The architecture should assume that compromise of raw genomic information may be effectively irreversible: unlike a password, the underlying genome cannot simply be changed.

Therefore security design should prioritise:
- minimising copies;
- local computation;
- bounded projections;
- authenticated queries;
- strong audit;
- least privilege;
- separation of Health and Research functions;
- durable provenance;
- prevention of bulk export.

> **Persistent Biological Identifier -> Persistent Protection Duty**

## 24. Failure modes

### Central population trawl
A new gene-risk relation causes a central service to search every participant genome and produce a list of identities.

**Safeguard:** distribute bounded query to protected records; keep match local.

### False anonymisation
Names are removed and the genomic dataset is declared anonymous.

**Safeguard:** treat genome as intrinsically re-identifiable unless demonstrated otherwise.

### Query exfiltration
A distributed query is designed to reveal more genomic information than its declared Health purpose.

**Safeguard:** bounded query grammar, sandboxed execution, output restriction, audit and validation.

### Research backflow
Positive matches are automatically reported to the researchers who identified the association.

**Safeguard:** Health relevance remains participant-local unless separate Research authority exists.

### Clinician overreach
A clinician with one legitimate Health function downloads the whole genome.

**Safeguard:** minimum-necessary contextual projection.

### Familial disclosure
A participant's finding is disclosed to relatives merely because it may matter to them.

**Safeguard:** distribute the medical question to relatives' own protected records where possible.

### Meaning drift
An old interpretation remains active after the evidence changes.

**Safeguard:** Historical versioning + KCS re-evaluation.

## 25. Compact architecture

**Genome**
→ protected participant Health/Historical record object.

**Research**
→ discovers candidate genomic relation.

**Validation**
→ determines whether relation enters validated medical knowledge.

**Historical**
→ preserves validated relation and provenance.

**Health**
→ creates bounded genomic Health query.

**KCS**
→ distributes relevant knowledge-change review/query.

**Participant protected record**
→ executes query locally.

**NO MATCH**
→ no participant-specific external disclosure; close/discard relevance result.

**MATCH**
→ private participant Health event
→ participant informed
→ appropriate prevention/diagnosis/treatment route.

**Research receives no identity/match by default.**

## 26. Core invariants

> **Move The Medical Question To The Protected Genome; Do Not Move The Genome To The Question**

> **Genomic Custody != General Genomic Access**

> **Research Knowledge About A Variant != Authority To Search Participants For That Variant**

> **Removal Of Name != Genomic Anonymisation**

> **Query Distribution != Genome Disclosure**

> **Local Match != External Match Disclosure**

> **Match -> Participant Health Relevance, Not Automatic Research Disclosure**

> **Ability To Ask A Bounded Genomic Question != Ability To Read The Genome**

> **Genetic Association != Diagnosis**

> **Shared Biological Relevance != Shared Record Access**

> **Familial Relevance != Automatic Familial Disclosure Authority**

> **Genome May Be Stable While Meaning Changes**

> **Clinical Relationship != Automatic Whole-Genome Access**

> **Health Genome != General Forensic Database**

> **Persistent Biological Identifier -> Persistent Protection Duty**

## 27. Remaining development

Further work is required for:
- exact genome custody topology between Health and Historical;
- sequencing/verification quality standards;
- consent for initial sequencing;
- minors/dependent participants;
- familial disclosure conflicts;
- reproductive/heritable information;
- right-not-to-know boundaries;
- forensic/legal access;
- genomic Research governance;
- secure local-query implementation;
- malicious-query resistance;
- cryptographic integrity;
- external genomic-service imports;
- post-death genomic rights;
- deletion/retention conflicts where familial relevance exists.

These should be resolved without abandoning the default architecture of protected local matching.
