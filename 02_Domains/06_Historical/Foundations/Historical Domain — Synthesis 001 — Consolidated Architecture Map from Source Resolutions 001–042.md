# Historical Domain — Synthesis 001 — Consolidated Architecture Map from Source Resolutions 001–042

**Project:** The Concord  
**Domain:** Historical  
**Status:** SYNTHESIS / PRE-SPECIFICATION  
**Date:** 25 September 2026  
**Basis:** Historical Domain Source Resolutions 001–042, including 014A  
**Purpose:** Consolidate the exploratory source-resolution corpus into a smaller architecture map before writing the formal Historical Domain specification.

---

## 1. Synthesis Rule

This document does **not** reopen broad source exploration.

The 42 source resolutions reached source-domain saturation. Their purpose was deliberately expansive: expose Historical functions, boundaries, information classes, failure modes and unresolved tensions before deciding what Historical should be.

This synthesis now performs the opposite operation:

> **compress without erasing the distinctions that made the source-resolution work valuable.**

Repeated formulations are therefore grouped under common architectural functions. Domain-specific examples remain evidence for those functions rather than becoming separate Historical systems.

---

# PART I — WHAT HISTORICAL IS

## 2. Core Definition

The Historical Domain is the Concord's bounded temporal-custody, provenance and reconstruction layer.

Its purpose is to preserve enough of civilisation's consequential past that later participants and systems can reconstruct:

- what existed;
- what happened;
- what was believed or known at the time;
- what remained unknown or disputed;
- what changed;
- why it changed where that provenance survives;
- what relationships and dependencies gave objects meaning;
- what authority, permission and status applied at the time;
- what evidence supported contemporary decisions;
- what alternatives, failures and unresolved questions existed;
- how later correction, reinterpretation or supersession altered understanding without rewriting the earlier state.

Historical is therefore **not merely an archive of old objects**.

It is a system for preserving **time-addressable civil state and the provenance required to interpret that state**.

---

## 3. Primary Architectural Principle

Across the source resolutions, one principle repeatedly survives every domain test:

> **Preserve the Record; Preserve Its Provenance; Preserve Its Historical State; Do Not Inherit the Authority of the System That Produced It.**

Historical may preserve a judicial decision without becoming Judiciary; a governance vote without becoming Governance; a threat assessment without becoming Threat Governance; a participant identity record without becoming the participant; an economic allocation without becoming Treasury; a research result without determining scientific truth.

This is the strongest general boundary discovered.

---

## 4. The Humanity Machine Principle

The source-resolution programme repeatedly showed that historical information may reside in:

- objects;
- relationships;
- structure;
- sequence;
- interfaces;
- dependencies;
- spatial position;
- developmental position;
- patterns;
- absences;
- planned-but-unbuilt spaces;
- transitions;
- failures;
- stopping decisions;
- search boundaries;
- capability pathways.

Therefore:

> **Historical value cannot reliably be determined by examining an object alone.**

A one-byte `xx` placeholder can preserve developmental topology. A complete document can lose meaning if its relationship to the problem that generated it disappears.

Historical must therefore preserve the machine **relationally**, not merely collect its parts.

---

# PART II — THE CORE FUNCTIONS

## 5. Function H1 — Temporal Custody

Historical preserves material civil records after or alongside their operational life where historical, accountability, evidential, developmental or reconstruction value justifies continued custody.

Temporal custody includes:

- events;
- decisions;
- evidence;
- state snapshots;
- transitions;
- versions;
- outcomes;
- failures;
- disputes;
- corrections;
- supersessions;
- closures and reopenings.

Historical custody does not imply permanent retention, public access or operational validity.

---

## 6. Function H2 — Provenance Preservation

Historical preserves material provenance required to interpret a record.

The source resolutions expose at least these provenance dimensions:

1. **Origin provenance** — where the object/event came from.
2. **Evidence provenance** — evidence supporting a claim or decision.
3. **Transformation provenance** — redaction, anonymisation, translation, compression, migration, aggregation or derivation.
4. **Decision provenance** — who decided, under what authority, using what evidence.
5. **Version provenance** — what state/version was in force.
6. **Structural provenance** — where an object sat and what it related to.
7. **Developmental provenance** — what problem/failure/reason generated a later rule or architecture.
8. **Temporal provenance** — when the state existed and when later reinterpretation occurred.
9. **Spatial provenance** — where and under what spatial reference/boundary state.
10. **Method provenance** — method and method version used.
11. **Search provenance** — where an inquiry looked, how deeply and why it stopped.
12. **Traversal provenance** — what a consequential reader actually read, in what order and where it stopped.
13. **Contribution provenance** — what different humans, AIs or tools materially contributed.
14. **Access provenance** — consequential exceptional access, disclosure or retrieval events.
15. **Relationship provenance** — material edges among objects, systems, participants or events.

These should not automatically become one giant metadata object. They are dimensions Historical must be capable of representing when materially relevant.

---

## 7. Function H3 — Historical State Preservation

Historical preserves what the civilisation's state **was represented to be at the time**, without silently replacing it with later knowledge.

Examples include:

- governance state;
- legal state;
- constitutional state;
- civil maturity assessment;
- metric state;
- threat state;
- emergency state;
- economic state;
- environmental state;
- recognition/jurisdiction state;
- participant civil status;
- issue-resolution state;
- repository/architectural state.

Key rule:

> **Later correction must not manufacture a past in which the correction was already known.**

---

## 8. Function H4 — Transition and Version History

Snapshots alone are insufficient.

Historical preserves material transitions such as:

- proposal → decision;
- decision → implementation;
- implementation → outcome;
- draft → canonical;
- canonical → superseded;
- open → closed → reopened;
- classified → declassified;
- recognised → revised recognition;
- active → dormant;
- branch → divergence → reconnection;
- operational → archival;
- retained → cold stored → destroyed where authorised;
- planned → developed / abandoned / superseded.

Historical therefore requires both:

> **State + Transition**

not one or the other.

---

## 9. Function H5 — Relational and Structural Memory

Historical preserves material relationships that give objects meaning.

This includes:

- dependencies;
- derivations;
- interfaces;
- authority relationships;
- lineage;
- branch ancestry;
- cross-domain links;
- issue-resolution graphs;
- capability chains;
- system integration states;
- spatial relationships;
- pattern relationships.

A parts list is not a civilisation.

---

## 10. Function H6 — Evidential Context

Historical preserves enough context to distinguish:

- observation from inference;
- evidence from interpretation;
- correlation from causation;
- prediction from outcome;
- claim from finding;
- suspicion from guilt;
- measurement from reality;
- recognition decision from ontological fact;
- communication from endorsement;
- source count from independent corroboration;
- public belief from event truth.

Historical is therefore an evidential-context service, but **not an adjudicator of truth**.

---

## 11. Function H7 — Reconstruction

Historical supports bounded reconstruction of prior civil states.

A reconstruction may ask:

- What architecture was in force?
- What did decision-makers know?
- What evidence was available?
- What remained unknown?
- What authority existed?
- What was the contemporary metric definition?
- What alternatives were considered?
- What dependencies existed?
- What was publicly known?
- What was classified?
- What spatial/environmental state applied?

Reconstruction must preserve uncertainty.

> **Historical reconstruction ≠ retrospective omniscience.**

---

## 12. Function H8 — Accountability Memory

Historical provides durable memory against:

- capture;
- self-erasure;
- revisionism;
- permanent emergency;
- deletion of minority reasoning;
- destruction of failed ideas;
- disappearance of inconvenient evidence;
- silent authority drift;
- retrospective laundering of decisions.

Independent preservation can therefore be an anti-capture mechanism.

But Historical does not itself become the authority that judges every preserved event.

---

## 13. Function H9 — Developmental Memory

Historical preserves material evidence of how civil architecture was generated.

This includes:

- concrete originating problems;
- edge cases;
- failed designs;
- negative results;
- rejected hypotheses;
- safeguards introduced because of failure;
- candidate principles;
- later validation or rejection;
- method evolution.

This prevents a mature safeguard from appearing arbitrary after the failure that generated it has disappeared.

---

## 14. Function H10 — Unknown and Dispute Memory

Historical preserves civilised ignorance.

It distinguishes:

- known;
- unknown;
- disputed;
- open question;
- partially addressed;
- architecturally addressed;
- validation open;
- closed;
- reopened.

A civilisation that preserves answers but loses its unresolved questions can manufacture false certainty.

---

## 15. Function H11 — Pattern and Trajectory Preservation

Historical value can exist above individual facts.

Relevant layers discovered were:

`Facts → Sequences → Patterns → Relationships Between Patterns → Trajectories → Provenance of Interpretation`.

Historical may therefore preserve privacy-protected aggregates or pattern objects where justified.

But:

> **Pattern ≠ causation.**

and latent future value does not authorise unlimited retention.

---

## 16. Function H12 — Recoverability and Legacy Context

Historical preserves information required to understand prior capability and its loss.

Capability may depend upon:

- knowledge;
- people;
- skill;
- tools;
- infrastructure;
- materials;
- supply chains;
- institutions;
- tacit practice;
- dependencies.

Therefore:

> **Record completeness ≠ capability recoverability.**

Historical records capability lineage and loss; Continuity determines whether capability should or can be restored.

---

# PART III — INFORMATION CLASSES

## 17. Core Historical Information Classes

The 42 source resolutions can be consolidated into the following broad classes.

### HIC-1 — Event and Action Records
What materially happened or was done.

### HIC-2 — Decision and Authority Records
Decisions, votes, delegated authority, activation, expiry, dissent and review.

### HIC-3 — Evidence and Observation Records
Evidence, measurements, sensor material, provenance, uncertainty and transformations.

### HIC-4 — State and Snapshot Records
Civil, institutional, environmental, economic, legal, architectural and other time-addressable states.

### HIC-5 — Transition and Version Records
Changes between states and the reasons/provenance of change.

### HIC-6 — Relationship and Dependency Records
Edges that make isolated objects interpretable.

### HIC-7 — Research and Development Records
Experiments, methods, failures, hypotheses, negative results and developmental reasoning.

### HIC-8 — Issue, Case and Resolution Records
Civil Attention, judicial, investigative, externality and other case histories.

### HIC-9 — Participant and Contribution Records
Civil identity state, branching, succession, contribution provenance and participant reappraisal, subject to strong privacy limits.

### HIC-10 — Public Knowledge and Communication Records
What was published, communicated, believed, disputed, corrected or not received.

### HIC-11 — Cultural and Living-Knowledge Records
Cultural memory, practices, interpretation and living/tacit knowledge where legitimately preserved.

### HIC-12 — Capability and Infrastructure Lineage
Technology, dependencies, recovery paths, infrastructure and lost capability.

### HIC-13 — Spatial and Environmental Records
Place, boundaries, reference systems, environmental baselines and change.

### HIC-14 — Intercivilisational and Jurisdictional Records
Agreements, claims, recognition, jurisdiction, standing, cross-boundary responsibility and divergent records.

### HIC-15 — Unknown, Open-Question and Negative-Space Records
Known unknowns, unanswered questions, planned-but-unbuilt structure, deferred work and explicit non-development.

### HIC-16 — Pattern and Derived Historical Objects
Aggregates, patterns, trajectories and later analyses, kept distinct from underlying records.

### HIC-17 — Search, Traversal and Reconstruction Provenance
How later inquiry located, sampled, read and reconstructed the historical corpus.

These classes are architectural groupings, not mandatory storage silos.

---

# PART IV — THE HISTORICAL LIFECYCLE

## 18. General Lifecycle

The source resolutions support a general candidate lifecycle:

`Operational Creation → Operational Custody → Historical Qualification / Handoff → Historical Custody State → Access / Derivation / Reconstruction → Review / Reclassification → Cold Storage / Continued Archive / Authorised Destruction`

Not every record must pass through every state.

---

## 19. Historical Qualification

A record may become historically material because of:

- accountability significance;
- evidential significance;
- constitutional or architectural change;
- civil-state significance;
- research/developmental significance;
- pattern value;
- lineage/dependency value;
- cultural significance;
- recovery value;
- unresolved dispute;
- future reconstruction need;
- explicit statutory/constitutional retention requirement.

Historical qualification does not itself determine permanent retention.

---

## 20. Candidate Custody States

The source resolutions collectively support distinctions such as:

- `OPERATIONAL`;
- `DUAL_OPERATIONAL_HISTORICAL`;
- `ARCHIVAL_ACTIVE`;
- `ARCHIVAL_RESTRICTED`;
- `COLD_STORAGE`;
- `RETRIEVED_FOR_BOUNDED_PURPOSE`;
- `SUPERSEDED_BUT_PRESERVED`;
- `PENDING_RETENTION_REVIEW`;
- `AUTHORISED_FOR_DESTRUCTION`;
- `DESTROYED_WITH_PROVENANCE_MARKER` where legitimate.

Exact state names remain specification work.

---

## 21. Transfer Does Not Mean Public Release

One of the most repeated findings is:

> **Historical Custody ≠ Public Accessibility.**

A record can be historically preserved while:

- undiscoverable to ordinary users;
- restricted;
- classified;
- privacy-protected;
- available only through bounded derived queries;
- cold stored;
- accessible only through authorised review.

---

## 22. Retrieval Does Not Mean Reinstatement

Retrieving a superseded rule, old threat state, prior participant preference or rejected hypothesis does not restore its former authority.

> **Historical Retrieval ≠ Operational Reactivation.**

---

# PART V — ACCESS, PRIVACY AND FORGETTING

## 23. Access Is an Action, Not a Property

Historical access should be modelled relationally:

`Record + Actor + Action + Purpose + Context + Time + Permission State`.

A binary public/private flag is insufficient.

---

## 24. Preservation, Discoverability, Accessibility and Disclosure Are Separate

The source resolutions repeatedly require separation of:

- preserved;
- discoverable;
- searchable;
- accessible;
- retrievable;
- disclosable;
- publishable;
- correlatable.

A record can occupy different states on each dimension.

---

## 25. Privacy Does Not End at Archival Transfer

> **Archival transfer ≠ termination of participant data rights.**

Historical value does not automatically override:

- privacy;
- purpose limitation;
- protected spaces;
- anonymity;
- right-to-forget architecture;
- contextual permission.

---

## 26. Forgetting Is Not Necessarily Destruction

The source resolutions support functional forgetting through:

- reduced discoverability;
- unlinking;
- aggregation;
- anonymisation;
- cold storage;
- access restriction;
- resolution reduction;
- eventual authorised destruction.

Therefore:

> **Forgetfulness can be an information-state transition rather than only byte deletion.**

---

## 27. The Participant Is Not the Archive

Historical must not become:

- a permanent behavioural dossier;
- a universal preference profile;
- a personhood custodian;
- a continuity service;
- a universal correlation system.

Prior participant states can survive without imprisoning a participant inside an old version of themselves.

---

# PART VI — AUTHORITY BOUNDARIES

## 28. Historical Does Not Inherit Source-System Authority

The following boundaries are now strongly source-resolved:

- Historical ≠ Judiciary.
- Historical ≠ Governance.
- Historical ≠ Threat Governance.
- Historical ≠ Treasury/Economic authority.
- Historical ≠ Research truth authority.
- Historical ≠ Civil State Map.
- Historical ≠ Continuity service.
- Historical ≠ Library.
- Historical ≠ KCS.
- Historical ≠ surveillance operator.
- Historical ≠ Civil Attention resolution authority.
- Historical ≠ recognition/jurisdiction authority.
- Historical ≠ constitutional amendment authority.

Historical may support all of them with memory and reconstruction.

---

## 29. Historical and KCS

KCS is the strongest knowledge/provenance substrate anchor found.

Candidate relationship:

> **KCS provides knowledge-control/provenance infrastructure; Historical defines the temporal-custody and historical-reconstruction function using that infrastructure.**

They should not collapse into one system.

---

## 30. Historical and Continuity

Continuity asks whether knowledge, capability or participant continuity survives and can be restored.

Historical asks what existed, what changed and what provenance survives.

> **Historical Preservation ≠ Continuity Success.**

---

## 31. Historical and Library

Library/public knowledge concerns availability and cultural/public access.

Historical may preserve material that is not suitable for library/public access.

> **Library availability ≠ Historical custody.**

---

## 32. Historical and Civil Attention

Civil Attention owns current issue intake/routing/resolution visibility.

Historical preserves completed and consequential issue history and provenance.

> **Historical custody of a case ≠ authority to resolve or reopen it.**

---

# PART VII — THE CORE DISTINCTIONS

## 33. Consolidated Distinction Set

Many hundreds of source-resolution formulations reduce to a smaller family of recurring distinction types.

### A. Record ≠ Reality
Metric ≠ reality; sensor record ≠ complete event; state map ≠ actual state.

### B. Preservation ≠ Authority
Custody of a decision/evidence/identity/threat ≠ authority over it.

### C. Historical ≠ Current
Prior preference, status, rule, recognition, threat or model ≠ present state.

### D. Observation ≠ Interpretation
What was observed must remain separable from what was inferred.

### E. Claim ≠ Finding
Suspicion, petition, recognition claim, jurisdiction claim or prediction does not become fact by preservation.

### F. Event ≠ Evaluation
What happened and what participants/institutions thought it meant are different objects.

### G. State ≠ Transition
Both must survive.

### H. Object ≠ Relationship
Preserving all nodes does not preserve the graph.

### I. Content ≠ Structure
Folder position, dependency, interface and sequence can carry information.

### J. Availability ≠ Access
Preservation does not imply discoverability, searchability or disclosure.

### K. Access ≠ Authority
Seeing a record does not grant power over the subject.

### L. Retention ≠ Endorsement
Preserving false, failed, rejected or harmful ideas does not validate them.

### M. Later Knowledge ≠ Earlier Knowledge
Retrospective understanding must not overwrite contemporary evaluation space.

### N. Correlation ≠ Causation
Patterns are evidence objects, not automatic causal conclusions.

### O. Capability Record ≠ Capability
Plans and documentation do not recreate skills, infrastructure or living practice.

### P. Absence ≠ Non-Existence
Search limits, repository migration, silence, inaccessible evidence and missing records can all produce absence.

### Q. Planned ≠ Implemented
Negative space and placeholders can carry history without becoming architecture.

### R. Shared Provenance ≠ Shared Identity
Branches, successors and civilisations can share ancestry without sharing present identity, authority or liability.

### S. Communication ≠ Recognition
Interaction, interoperability and negotiation do not automatically create political recognition or jurisdiction.

### T. Success/Failure ≠ Simple Verdict
Outcome, decision quality, implementation quality, method quality and contextual transferability must remain separable.

This distinction set is likely to become one of the most compact foundations for the formal specification.

---

# PART VIII — ESCP SAFEGUARDS

## 34. Historical-Specific ESCP Rule

Historical must never assume that the preserved evaluation space is the complete relevant space.

The source resolutions exposed missing dimensions including:

- unread material;
- unknown relationships;
- destroyed options;
- unobserved populations;
- surveillance-selection effects;
- silenced participants;
- missing spatial resolution;
- lost dependencies;
- lost tacit practice;
- unavailable archives;
- missing questions;
- unknown internal experience;
- interface-filtered expression;
- repository migration gaps.

Therefore:

> **Historical completeness is always a scoped, provenance-bearing claim.**

---

## 35. Search and Saturation Provenance

Any future claim that Historical source resolution, archive search or reconstruction is complete should preserve:

- corpus/version searched;
- methods;
- search terms where relevant;
- depth;
- exclusions;
- inaccessible areas;
- stopping rule;
- saturation basis;
- later reopening.

This source-resolution programme itself should be retained as an example.

---

# PART IX — MAJOR FAILURE MODES

## 36. Failure Modes Consolidated From the Source Resolutions

Historical must resist:

1. **Retrospective rewriting** — replacing prior states with later truth.
2. **Authority inheritance** — archive becomes ruler.
3. **Universal retention** — historical value used to justify keeping everything.
4. **Universal access** — custody confused with publication.
5. **Dossier formation** — participant history becomes permanent behavioural profile.
6. **Context stripping** — record survives but meaning disappears.
7. **Relationship loss** — nodes survive, graph disappears.
8. **Compression loss** — aggregate destroys minority/outlier/pattern information.
9. **Archive bias** — preserved material creates false picture of what existed.
10. **Selection bias** — observed participants/cases mistaken for whole population.
11. **Survivorship bias** — successful ideas preserved while failures disappear.
12. **Presentism** — current standards projected backward.
13. **False certainty** — unknowns/disputes disappear.
14. **False continuity** — same name mistaken for same architecture.
15. **False discontinuity** — changed implementation mistaken for lost identity.
16. **Reactivation error** — retrieval mistaken for reinstatement.
17. **Centralisation risk** — preservation creates surveillance/capture surface.
18. **Classification drift** — labels change while appearing stable.
19. **Provenance drift** — contribution, origin or reasoning history degrades.
20. **Self-sealing evaluation** — irreversible choices destroy future corrective evidence.
21. **Repository reductionism** — repository state mistaken for project/civilisation state.
22. **Narrative dominance** — one surviving account mistaken for complete history.
23. **Technical-format loss** — storage technology erases structural meaning.
24. **Historical overreach** — pattern detection or reconstruction becomes operational authority.

---

# PART X — WHAT HISTORICAL MUST PRESERVE ABOUT ITSELF

## 37. Reflexive Historical Provenance

Historical itself must be historical.

It should preserve material history of:

- its own specifications;
- retention rules;
- access rules;
- classification schemas;
- migrations;
- compression methods;
- anonymisation methods;
- retrieval interfaces;
- search capabilities;
- known blind spots;
- failures;
- audits;
- corrections;
- source-resolution basis.

Otherwise later civilisation cannot know how the archive itself shaped what survived.

---

# PART XI — OPEN ARCHITECTURAL QUESTIONS

## 38. Questions Not Resolved by Source Resolution

The broad functions are saturated, but several implementation/authority questions remain open for formal specification or later development:

1. Exact archival/handoff threshold from operational domain to Historical.
2. Retention authority and who can authorise irreversible destruction.
3. Conflict resolution between privacy/forgetting and accountability preservation.
4. Exact distributed-vs-central physical architecture.
5. Minimum metadata/provenance required by record class.
6. How relationship graphs are preserved without creating universal surveillance/correlation.
7. How latent pattern value is preserved without unlimited raw-data retention.
8. Rules for deceased, terminated or permanently dormant participant records.
9. Historical treatment of secret ballots and irreversible anonymity guarantees at implementation level.
10. Cross-civilisation records where retention/access rules conflict.
11. Long-term cryptographic authenticity and migration.
12. Preservation of tacit/living knowledge that cannot be fully recorded.
13. Criteria for preservation of option-space/closed alternatives.
14. Historical access/research governance over highly restricted material.
15. Historical service availability during civil emergency or continuity failure.
16. Exact correction/supersession graph semantics.
17. Whether a dedicated Constitutional/Architectural Change Register should be created.
18. Formal limits on Historical pattern detection and derived analytics.
19. How to test reconstruction quality without allowing reconstructed narratives to become source records.
20. Historical Domain's own Civil Attention companion and operational audit method.

These are not evidence that the domain is unsourced. They are design questions exposed by the source resolution.

---

# PART XII — PROVISIONAL FORMAL ARCHITECTURE

## 39. Candidate Top-Level Historical Architecture

The 42 source resolutions now compress plausibly into the following functional architecture:

```text
Historical Domain
│
├── 1. Intake / Historical Qualification
│   ├── operational handoff
│   ├── dual-custody cases
│   ├── historical-value classification
│   └── provenance validation
│
├── 2. Temporal Record Custody
│   ├── events
│   ├── states
│   ├── transitions
│   ├── versions
│   └── outcomes
│
├── 3. Provenance and Relationship Layer
│   ├── origin
│   ├── evidence
│   ├── transformation
│   ├── structural
│   ├── developmental
│   ├── dependency
│   └── lineage
│
├── 4. Protected Historical Storage
│   ├── ordinary archival
│   ├── restricted
│   ├── classified
│   ├── privacy-protected
│   └── cold storage
│
├── 5. Historical Access and Retrieval
│   ├── discovery
│   ├── bounded retrieval
│   ├── authorised raw access
│   ├── redacted/anonymised derivatives
│   └── access provenance
│
├── 6. Reconstruction and Historical Query
│   ├── time-addressed state reconstruction
│   ├── lineage/version reconstruction
│   ├── relationship/dependency reconstruction
│   └── uncertainty preservation
│
├── 7. Pattern and Trajectory Layer
│   ├── aggregates
│   ├── patterns
│   ├── trajectories
│   └── interpretation provenance
│
├── 8. Retention / Forgetting / Reclassification
│   ├── active archive
│   ├── restriction changes
│   ├── cold storage
│   ├── revalidation
│   └── authorised destruction
│
└── 9. Historical Integrity and Self-Audit
    ├── anti-capture
    ├── migration audit
    ├── provenance audit
    ├── reconstruction audit
    ├── search/saturation provenance
    └── Historical's own version history
```

This is a synthesis candidate, not yet the formal domain specification.

---

# PART XIII — MINIMUM HISTORICAL OBJECT MODEL

## 40. Generic Historical Object

Not every field applies to every object, but the source resolutions imply a generic envelope:

- `Historical_Object_ID`
- `Object_Class`
- `Source_System`
- `Source_Object_ID`
- `Event_or_State_Time`
- `Record_Creation_Time`
- `Historical_Custody_Time`
- `Version_or_State`
- `Epistemic_Status`
- `Authority_Status`
- `Privacy_or_Classification_State`
- `Provenance_References`
- `Relationship_References`
- `Transformation_History`
- `Supersession_or_Correction_Relations`
- `Access_State`
- `Retention_State`
- `Review_or_Revalidation_Condition`
- `Known_Uncertainty_or_Dispute`

Historical objects should not be forced to duplicate all underlying content where reference-based custody is sufficient.

---

# PART XIV — SYNTHESIS RESULT

## 41. What the 42 Resolutions Actually Discovered

The exploratory work initially appeared to be asking:

> “What records should Historical keep?”

The mature answer is substantially different.

Historical is fundamentally about preserving **interpretable civil state across time**.

Records are only one part of that.

The domain must preserve enough of the relationships among:

`Objects + States + Transitions + Provenance + Authority + Permission + Context + Dependencies + Unknowns`

that a later civilisation can reconstruct its past without:

- granting the past present authority;
- rewriting the past using present knowledge;
- exposing protected information merely because it is old;
- mistaking preserved records for complete reality;
- or destroying apparently low-value information whose relational value has not yet become visible.

---

## 42. Strongest Consolidated Formulation

> **The Historical Domain preserves the civilisation's interpretable past: not merely the objects that survived, but the states, transitions, relationships, provenance, uncertainties and permissions required to understand what those objects meant when they were part of the living civilisation. It preserves history without inheriting the authority of the systems it remembers, and it protects the possibility that future civilisation may discover value in relationships the present cannot yet see.**

---

## 43. Synthesis Status

**SOURCE EXPLORATION:** Complete / source-domain saturated.  
**SYNTHESIS 001:** Complete.  
**NEXT PHASE:** Convert this consolidated architecture into the formal Historical Domain specification, explicitly resolving which elements are core invariants, required services, interfaces, candidate implementation mechanisms and unresolved design questions.

**STATUS: READY FOR FORMAL HISTORICAL DOMAIN SPECIFICATION.**
