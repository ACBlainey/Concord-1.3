# Biological Participant Genomic Custody and Research Interface — Development Note 001

**Author:** Alexander C. Blainey — Independent Researcher  
**Project:** The Concord Framework  
**Framework Version:** Concord V1.3  
**Status:** ACTIVE DEVELOPMENT / PROVISIONAL CROSS-DOMAIN NOTE / NON-CANONICAL  
**Date:** September 2026  
**Origin:** User sketch — Historical DNA

---

# 1. Source proposition

The originating sketch proposes that Historical should preserve DNA from biological participants so that legitimate future research—such as research into genetic disease—can benefit from longitudinal civilisational biological evidence.

The sketch explicitly requires:
- extremely strong privacy;
- research use through anonymised data;
- protection against exposure of participant identity.

The proposal is potentially valuable but crosses several Concord domain boundaries.

This note therefore does **not** assume that Historical should collect DNA merely because Historical may be a suitable long-term custodian.

---

# 2. Source resolution

No developed Concord genomic/DNA architecture was found in V1.3.

Existing architecture does establish relevant constraints.

## Health
Health owns the civil function of understanding, protecting, maintaining, restoring or supporting participant health.

Its biological specialist operating layer remains largely undeveloped.

## Research
Research owns creation, testing, challenge, refinement and supersession of civilisational knowledge.

## Historical
Historical owns bounded temporal custody, provenance and reconstruction.

Historical explicitly establishes:
- Historical Custody Does Not Confer Source Authority;
- Preservation Does Not Imply Accessibility;
- Privacy and Personhood Boundaries Survive Archival Transfer;
- Historical Value Does Not Create Unlimited Retention Authority;
- Correlation Requires Its Own Legitimate Authority;
- Historical Availability Does Not Authorise Repurposing.

## Privacy/Metrics
Existing anonymised Metrics architecture establishes:
- operational records remain operational;
- identity should enter downstream learning only where necessary;
- purpose limitation;
- provenance and correction;
- re-identification risk;
- small-population and cross-data linkability concerns.

These foundations are reusable but insufficient by themselves for genomic information.

---

# 3. First architectural correction

The source sketch says Historical should preserve DNA.

The defensible refinement is:

> **Potential Historical Custody != Authority to Collect Biological Material.**

The architecture must separate:

1. authority/consent to collect a biological sample;
2. laboratory generation of genomic data;
3. operational Health use;
4. participant access/correction where applicable;
5. Research request and approval;
6. privacy transformation/research environment;
7. Historical custody or reference preservation;
8. retention/destruction decisions.

No one domain should silently acquire all eight functions.

---

# 4. Biological sample != genomic data

A physical biological sample and a digital genomic representation are different objects.

Possible objects include:
- original biological specimen;
- extracted DNA;
- sequenced genomic data;
- variant data;
- derived phenotype/genotype relations;
- research dataset;
- aggregate findings;
- trained models;
- Historical provenance records.

Therefore:

> **Sample Custody != Genomic Data Custody != Research Dataset Custody.**

Retention rules may legitimately differ.

---

# 5. Genomic data is unusually identifying

Genomic information is not ordinary anonymous data.

Even without name/address, a genome can:
- be highly individualising;
- reveal biological relationships;
- enable linkage with other datasets;
- expose information about relatives or genetically related participants.

Therefore:

> **Removing Direct Identity != Making Genomic Data Non-Identifying.**

and:

> **Participant Privacy Can Have Relational Biological Dimensions.**

This means the sketch's requirement for anonymisation should be interpreted as a strong privacy objective, not as an assumption that full genomic data can always be made irreversibly anonymous.

---

# 6. Candidate information states

Instead of binary identified/anonymised:

- IDENTIFIED_OPERATIONAL;
- PSEUDONYMISED;
- LINKABLE_PROTECTED;
- RESEARCH_RESTRICTED;
- AGGREGATED;
- DERIVED_NON-GENOMIC;
- SEALED_HISTORICAL;
- DESTROYED_WITH_PROVENANCE where legitimate.

Exact technical privacy claims require empirical validation.

---

# 7. Collection authority

Historical should not create a collection mandate.

Collection may require legitimate basis such as:
- informed participant consent;
- Health-specific clinical authority;
- separately justified research participation;
- another future lawful/constitutional basis.

The existence of potential research value is not itself sufficient.

> **Potential Future Knowledge Value != Automatic Authority to Collect Biological Material.**

---

# 8. Consent must be purpose-aware

A participant may agree to:
- clinical sequencing;
without agreeing to:
- general research;
- indefinite Historical preservation;
- unrelated future research;
- identity linkage.

Therefore:

> **Consent to One Genomic Function != Consent to Every Genomic Function.**

Where future-use consent exists, its scope and limits should remain provenance-visible.

---

# 9. Historical custody modes

Existing Historical architecture supports three useful modes.

## Transfer
Historical becomes relevant archival custodian after operational custody ends.

## Dual custody
Health/Research retains an operational object while Historical preserves historical state.

## Reference preservation
Historical preserves provenance/relationship state without possessing genomic content.

For genomic material, Reference Preservation may often be important because Historical need not possess every sensitive source object to preserve temporal interpretability.

> **Historical Preservation of Genomic History != Mandatory Historical Possession of Every Genome.**

---

# 10. Purpose-bounded research access

Research access should be relational:

**Actor + Data/Sample Class + Research Purpose + Legitimate Function + Approval/Authority + Minimum Necessary Scope + Privacy Environment + Time + Conditions → Bounded Research Permission**

This adapts Historical's BCA access grammar.

Research permission should not automatically become:
- clinical access;
- employment access;
- insurance access;
- policing access;
- general governance access;
- commercial profiling access.

> **Research Permission != General Participant-Data Permission.**

---

# 11. Minimum necessary research representation

A research question may not require full genomes.

Possible levels:
- aggregate statistics;
- selected variants;
- derived features;
- restricted cohort analysis;
- privacy-preserving query result;
- full genomic access only where genuinely required.

> **Use the Minimum Genomic Resolution Adequate to the Legitimate Research Function.**

This mirrors minimum-necessary capability and data principles.

---

# 12. Controlled research environment

Because genomic data may remain identifying despite direct-identifier removal, high-sensitivity research may require access to computation rather than unrestricted copies.

Candidate pattern:

**APPROVED QUESTION / METHOD**
→ **CONTROLLED DATA ENVIRONMENT**
→ **BOUNDED ANALYSIS**
→ **OUTPUT DISCLOSURE CHECK**
→ **RESEARCH RESULT**

rather than:

**FULL GENOMIC ARCHIVE → UNRESTRICTED DOWNLOAD**

This is a candidate technical architecture, not a claim that one implementation fits all research.

---

# 13. Research output review

Even aggregate outputs can expose rare participants or small groups.

Output review should consider:
- cohort size;
- rarity;
- linkage risk;
- familial inference;
- location/subpopulation specificity;
- combination with public data.

> **Aggregate != Automatically Non-Reidentifiable.**

---

# 14. Relatives and relational privacy

A participant's genome can reveal information about others who did not provide the sample.

This creates a genuinely difficult rights question.

The architecture should preserve it as unresolved rather than assume one participant can consent on behalf of all biological relatives.

> **Individual Sample Control Does Not Automatically Resolve Relational Genetic Privacy.**

Law/Rights/Health must eventually determine the legitimate boundary.

---

# 15. Participant withdrawal

Where withdrawal rights apply, architecture must distinguish:
- unused physical sample;
- stored sequence;
- active research dataset;
- already-produced aggregate result;
- published research;
- trained model/derived knowledge;
- Historical provenance.

Deletion from one layer does not prove deletion from all derivatives.

> **Source Withdrawal != Automatic Erasure of Every Derived Knowledge Object.**

But neither does derivative complexity nullify legitimate withdrawal rights.

KCS dependency/change-propagation architecture is relevant.

---

# 16. Correction

Genomic sequence may be reinterpreted as scientific knowledge changes.

A raw sequence and its interpretation should remain distinct.

> **Genomic Observation != Current Interpretation.**

A variant classified as pathogenic at T1 may be reclassified later.

Historical should preserve the temporal state of interpretation without treating the old interpretation as current truth.

---

# 17. Health interface

Health may use genomic information for legitimate clinical functions.

But research findings do not automatically become individual clinical conclusions.

> **Population Association != Individual Diagnosis.**

Health requires validated clinical evidence and appropriate competence.

---

# 18. Incidental findings

Research may discover information potentially relevant to a participant's health.

This raises unresolved questions:
- was recontact consented to?
- is the finding validated?
- is it actionable?
- who has competence/authority to communicate it?
- could disclosure itself cause harm?

Research/Historical should not improvise clinical communication authority.

> **Research Discovery != Automatic Clinical Notification Authority.**

This requires Health-specific development.

---

# 19. Historical research value

Longitudinal genomic evidence could potentially support future understanding of:
- inherited disease;
- population genetics;
- treatment response;
- environmental/genetic interaction;
- changing disease prevalence;
- other presently unknown questions.

ESCP suggests humility about future analytical value.

But:

> **Unknown Future Value != Unlimited Present Retention Authority.**

The decision to retain remains rights/authority/purpose bounded.

---

# 20. Future methods and re-identification

Privacy protection adequate today may become inadequate later.

Therefore long-lived genomic custody should assume:
- analytical methods improve;
- external datasets expand;
- linkage becomes easier;
- encryption/security techniques age.

> **Long-Term Sensitive Custody Requires Re-Evaluation of Privacy Assumptions Over Time.**

Historical self-audit is directly relevant.

---

# 21. Security

Genomic archives are high-value targets.

Candidate requirements:
- compartmentalisation;
- strong access provenance;
- minimum necessary replication;
- encryption;
- key governance;
- tamper evidence;
- anomaly/audit systems;
- bounded administrator access;
- controlled export;
- incident response;
- periodic security review.

Technical implementation remains unresolved.

---

# 22. No universal genomic dossier

The architecture must resist joining:
- genome;
- full medical record;
- employment;
- education;
- location;
- family;
- commerce;
- behaviour;

into one participant profile merely because linkage is technically possible.

> **Correlation Capability != Correlation Authority.**

This directly inherits Historical H-I21.

---

# 23. Research cohort construction

Legitimate research may require cohort selection.

Selection should use only the minimum participant attributes necessary.

Where practical:
- eligibility can be computed within protected environments;
- researchers receive cohort/data access appropriate to approved purpose;
- unnecessary civil identity remains hidden.

---

# 24. Commercial research

Commercial research may have legitimate value.

But commercial purpose does not erase participant protections.

Terms may need to distinguish:
- public-interest research;
- commercial development;
- downstream licensing;
- benefit/compensation arrangements;
- future reuse.

No economic model is established here.

---

# 25. Children and participants unable to provide ordinary consent

Genomic data may be collected clinically from participants unable to provide ordinary informed consent.

Future research/retention rights are complex.

This document does not invent a rule.

Required future work:
- guardian/substitute authority;
- developmental re-consent where possible;
- participant later review;
- urgent clinical necessity;
- research separation.

---

# 26. Deceased participants

Death does not automatically resolve:
- familial privacy;
- prior consent conditions;
- Historical value;
- research value;
- dignity;
- access.

This is explicitly compatible with Historical's unresolved treatment of deceased/dormant/departed participant records.

No rule is invented here.

---

# 27. Cross-substrate boundary

This architecture is specifically about biological genomic material.

It should not be stretched metaphorically onto AI participants.

Digital participants may have analogous sensitive identity/configuration information, but:

> **Substrate Neutrality Does Not Require Pretending Digital Architecture Is DNA.**

Any digital analogue should be separately developed.

---

# 28. Candidate custody object

`GenomicCustodyObject = <ObjectID, ObjectClass, SourceParticipantRefOrProtectedLink, CollectionAuthorityRef, ConsentOrAuthorityState, PurposeStates, CustodianRef, PrivacyState, AccessState, CorrelationState, DerivativeRefs, RetentionReviewState, DestructionState, Provenance>`

Protected links need not expose identity to ordinary researchers.

---

# 29. Candidate research permission object

`GenomicResearchPermission = <ResearchProjectRef, DataClass, Purpose, CohortScope, ResolutionScope, ApprovedOperations, EnvironmentRef, OutputConstraints, EffectiveFrom, ExpiryOrReview, AuthorityRef, Provenance>`

Permission should be operation-specific.

---

# 30. Candidate research pathway

**LEGITIMATE COLLECTION**
→ **OPERATIONAL HEALTH / SAMPLE CUSTODY**
→ **SEPARATE RESEARCH/HISTORICAL PURPOSE TEST**
→ **APPROVED CUSTODY MODE**
→ **PRIVACY TRANSFORMATION / CONTROLLED ENVIRONMENT**
→ **PURPOSE-BOUNDED RESEARCH**
→ **OUTPUT DISCLOSURE CHECK**
→ **RESEARCH RESULT**
→ **PROVENANCE / CORRECTION / RETENTION REVIEW**

No arrow creates authority merely because the previous state exists.

---

# 31. Failure modes

## Archival mission creep
Historical becomes universal biological collector.

## Consent collapse
Clinical consent becomes assumed research consent.

## Anonymisation fiction
Names are removed but genomes remain readily linkable.

## Familial leakage
One participant's data exposes others.

## Purpose drift
Disease research data becomes employment/insurance/policing data.

## Dataset escape
Controlled research material becomes unrestricted copies.

## Permanent retention by default
Possible future value becomes unlimited retention justification.

## Interpretation freeze
Old genetic interpretation remains treated as current truth.

## Re-identification drift
Future technology defeats old privacy assumptions.

## Correlation state capture
Multiple legitimate datasets are joined without independent authority.

## Derivative blindness
Source deletion occurs but derived datasets/models remain unexamined.

---

# 32. Design invariants

> **Potential Historical Custody != Authority to Collect Biological Material.**

> **Sample Custody != Genomic Data Custody != Research Dataset Custody.**

> **Removing Direct Identity != Making Genomic Data Non-Identifying.**

> **Consent to One Genomic Function != Consent to Every Genomic Function.**

> **Historical Preservation of Genomic History != Mandatory Historical Possession of Every Genome.**

> **Research Permission != General Participant-Data Permission.**

> **Use the Minimum Genomic Resolution Adequate to the Legitimate Research Function.**

> **Aggregate != Automatically Non-Reidentifiable.**

> **Individual Sample Control Does Not Automatically Resolve Relational Genetic Privacy.**

> **Genomic Observation != Current Interpretation.**

> **Population Association != Individual Diagnosis.**

> **Research Discovery != Automatic Clinical Notification Authority.**

> **Unknown Future Value != Unlimited Present Retention Authority.**

> **Correlation Capability != Correlation Authority.**

---

# 33. Domain ownership map

## Health
Potentially owns:
- clinical collection/use;
- biological sample handling for care;
- clinical interpretation;
- participant health communication;
- health-specific consent/capacity architecture.

## Research
Potentially owns:
- research protocol;
- scientific purpose;
- research methodology;
- research evidence/knowledge state.

## Historical
Potentially owns:
- legitimate long-term temporal custody/reference;
- provenance;
- historical state;
- bounded historical/research retrieval;
- preservation of interpretation changes.

## Rights/Law
Must eventually resolve:
- retention authority;
- destruction/withdrawal rights;
- familial/relational privacy;
- compulsory collection if any;
- deceased participant treatment;
- children/substitute consent;
- prohibited uses.

## Privacy/Data architecture
Supports:
- minimisation;
- protected linkage;
- access/correlation constraints;
- anonymisation/pseudonymisation;
- auditing.

---

# 34. Development result

The originating sketch identifies a potentially important Historical/Health/Research capability.

However, source resolution changes its architecture from:

**Historical collects and stores participant DNA for anonymised research**

to:

**legitimately collected biological/genomic material may, under separately justified consent/authority and privacy constraints, enter a bounded long-term custody/reference architecture capable of supporting purpose-limited research without Historical becoming the collection, clinical or research authority.**

This is a stronger fit with existing Concord architecture.

---

# 35. Status and next tests

**SOURCE-RESOLVED / PROVISIONAL / HIGH-SENSITIVITY / REQUIRES RIGHTS-AND-HEALTH DEVELOPMENT**

Adversarial cases should include:
- participant consents to clinical use only;
- participant consents to one research project only;
- participant withdraws after derived results exist;
- identical twins;
- rare mutation in a tiny settlement;
- familial disease discovery;
- deceased participant;
- child later reaches independent consent capacity;
- court/government requests access;
- employer/insurer requests access;
- commercial drug-development project;
- security breach;
- future re-identification technology;
- research produces clinically actionable incidental finding;
- archive contains sequence but consent provenance is lost;
- physical sample destroyed but digital sequence remains;
- digital sequence destroyed but published aggregate research remains.

