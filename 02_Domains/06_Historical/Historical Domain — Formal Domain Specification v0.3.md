# Historical Domain — Formal Domain Specification v0.3

**Project:** The Concord  
**Domain:** Historical  
**Status:** FORMAL DOMAIN SPECIFICATION / DEVELOPMENT DRAFT  
**Version:** 0.3  
**Date:** 25 September 2026  
**Primary Basis:** Historical Source Resolutions 001–042; Historical Synthesis 001; Historical Synthesis 002; Evaluation-Space Completeness Problem (ESCP); Adversarial Boundary Test 001; Cross-Domain Interface Tests 001–004; Bounded Contextual Authority (BCA); Constitutional Emergency V2  
**Scope:** Defines the purpose, invariants, responsibilities, boundaries, information architecture, lifecycle, interfaces and minimum safeguards of the Historical Domain.

---

# 1. Domain Purpose

The Historical Domain preserves the civilisation's interpretable past.

It exists so that future participants and systems can reconstruct, within legitimate access constraints:

- what existed;
- what happened;
- what was believed or known;
- what remained unknown or disputed;
- what changed;
- why change occurred;
- what relationships and dependencies existed;
- what authority, permission and status applied;
- what evidence supported contemporary understanding;
- what alternatives, failures and unresolved questions existed;
- what evaluation architecture shaped contemporary conclusions;
- and how later evidence, correction or reinterpretation changed understanding.

Historical is not merely long-term storage.

Its primary civilisational function is **temporal interpretability**.

---

# 2. Core Domain Definition

> **The Historical Domain is the Concord's bounded temporal-custody, provenance and reconstruction layer. It preserves records, states, transitions, relationships, evidence, authority context, uncertainty, evaluation context and relevant negative space sufficiently to support accountable reconstruction across time, while neither inheriting the operational authority of the systems it remembers nor claiming that its surviving representation exhausts historical reality.**

---

# 3. Governing Principle

> **Preserve the Record; Preserve Its Provenance; Preserve Its Historical State; Preserve the Limits of Its Evaluation Space; Do Not Inherit the Authority of the System That Produced It.**

---

# 4. The Humanity Machine Constraint

Historical must operate under a permanent recognition that future value cannot always be identified from present object-level content.

Information may reside in:

- objects;
- relationships;
- sequences;
- structural position;
- dependencies;
- interfaces;
- absences;
- planned-but-unbuilt structures;
- failed attempts;
- stopping decisions;
- search paths;
- capability pathways;
- patterns between apparently unrelated records.

Therefore:

> **Present inability to identify value is not proof of future irrelevance.**

This principle does not require universal retention. It requires caution about irreversible loss and preservation of sufficient provenance, structure and diversity to permit future discovery.

---

# 5. Domain Invariants

The following are mandatory architectural invariants.

## H-I1 — Record Is Not Reality

Historical records are evidence concerning reality.

No record, archive or reconstruction may silently be treated as identical to the underlying past.

## H-I2 — Historical State Must Remain Historical

Later correction, reinterpretation or knowledge must not rewrite an earlier state so that it appears the later information was already known.

## H-I3 — Provenance Must Survive Transformation

Where a record is transformed, compressed, migrated, anonymised, summarised, translated or derived, sufficient provenance must survive to identify the transformation and its relationship to the source.

## H-I4 — Historical Custody Does Not Confer Source Authority

Archiving a judicial ruling does not make Historical judicial.

Archiving governance decisions does not give Historical governance authority.

Archiving research does not make Historical the arbiter of scientific truth.

## H-I5 — Preservation Does Not Imply Accessibility

A record may legitimately be preserved while remaining restricted, sealed, anonymised, non-searchable or inaccessible to particular actors or purposes.

## H-I6 — Retrieval Does Not Reactivate Authority

Retrieving a historical instruction, permission, credential, mandate, decision or status does not restore its former operational force.

## H-I7 — Observation Must Remain Distinguishable From Interpretation

Where materially consequential, Historical must permit later reconstruction to distinguish observation, inference, interpretation, conclusion and action.

## H-I8 — Absence Does Not Automatically Establish Non-Existence

Failure to find a record must not silently become evidence that the underlying event, state or relationship did not exist.

## H-I9 — Completeness Claims Must Be Scoped

Any claim that a historical corpus, search, reconstruction or evaluation is complete must identify the scope within which completeness has been demonstrated.

## H-I10 — Unknown States Must Be Preservable

Historical must be capable of representing uncertainty, dispute, known missing information, unresolved questions and later-recognised missing dimensions.

## H-I11 — Relational Information Is Historical Information

Relationships and structural context may be as historically significant as the individual objects they connect.

## H-I12 — Historical Must Preserve Its Own History

The domain's schemas, retention rules, migrations, access systems, failures, audits, corrections and architectural evolution are themselves historical objects.

## H-I13 — Destruction Is an Epistemically Consequential Action

Irreversible destruction can contract future evaluation space and therefore requires explicit authority, provenance and proportionality.

## H-I14 — Historical Must Remain Correctable

No Historical schema, taxonomy, interpretation or reconstruction may be treated as permanently exhaustive.

## H-I15 — Privacy and Personhood Boundaries Survive Archival Transfer

Historical custody must not become a mechanism for permanent behavioural dossiers, universal preference profiles or unrestricted correlation of participant history.

## H-I16 — Provenance Completeness Does Not Require Identity Traceability

Historical must support legitimate anonymous, pseudonymous, secret and identity-restricted processes. Provenance may establish process, custody or evidential lineage without exposing protected identity.

## H-I17 — Classification Is Not Reality

Historical taxonomies organise records but must not become the only surviving representation of them. Classification systems must be versionable and, where proportionate, source descriptors or lower-level representations should survive reclassification.

## H-I18 — Archive Change Must Remain Distinguishable From Civilisational Change

Changes in Historical collection, retention, classification, search, access or migration systems must be preserved sufficiently to prevent later users from mistaking changes in the observational apparatus for changes in the civilisation being observed.

---

# 6. Core Historical Functions

Historical shall provide the following functions.

## H1 — Temporal Custody

Preserve information across operational time boundaries.

## H2 — Provenance Preservation

Preserve relevant origin, evidence, transformation, decision, version, structural, developmental, temporal, spatial, methodological, search, traversal, contribution, access and relationship provenance.

## H3 — Historical State Preservation

Preserve what a system, object, institution or participant state was at a defined historical time.

## H4 — Transition and Version History

Preserve transitions between meaningful states and the reasons, authorities or evidence associated with them.

## H5 — Relational and Structural Memory

Preserve materially relevant relationships, dependencies, topology and contextual position.

## H6 — Evidential Context

Preserve distinctions necessary to interpret evidence without collapsing evidence into conclusion.

## H7 — Reconstruction

Support bounded reconstruction of past states, events, decisions and evaluation environments.

## H8 — Accountability Memory

Preserve sufficient lawful records for later audit, accountability and institutional learning.

## H9 — Developmental Memory

Preserve the development of systems, ideas, experiments, failures, alternatives and unresolved paths.

## H10 — Unknown and Dispute Memory

Preserve uncertainty, disagreement, open questions, unresolved states and recognised limitations.

## H11 — Pattern and Trajectory Preservation

Support legitimate study of patterns and trajectories without automatically treating correlation as causation.

## H12 — Recoverability and Legacy Context

Preserve enough context to understand former capabilities and dependencies without assuming that documentary preservation equals practical recoverability.

---

# 7. Historical Information Classes

Historical must be able to represent at least the following information classes.

- **HIC-1:** Event and Action
- **HIC-2:** Decision and Authority
- **HIC-3:** Evidence and Observation
- **HIC-4:** State and Snapshot
- **HIC-5:** Transition and Version
- **HIC-6:** Relationship and Dependency
- **HIC-7:** Research and Development
- **HIC-8:** Issue, Case and Resolution
- **HIC-9:** Participant and Contribution
- **HIC-10:** Public Knowledge and Communication
- **HIC-11:** Cultural and Living Knowledge
- **HIC-12:** Capability and Infrastructure Lineage
- **HIC-13:** Spatial and Environmental
- **HIC-14:** Intercivilisational and Jurisdictional
- **HIC-15:** Unknown, Open Question and Negative Space
- **HIC-16:** Pattern and Derived Historical Object
- **HIC-17:** Search, Traversal and Reconstruction Provenance

These classes are not required to map one-to-one to storage tables or folders.

They define representational obligations.

---

# 8. Historical Epistemic Model

Where material to interpretation, Historical must be capable of representing the following layers separately:

```text
Underlying Reality
        ↓
Potential Evidence
        ↓
Accessible Evidence
        ↓
Observed Evidence
        ↓
Represented Evaluation Space
        ↓
Interpretation
        ↓
Conclusion
        ↓
Scope Claim
        ↓
Decision / Action
        ↓
Outcome
        ↓
Later Reinterpretation
```

The architecture must not require every ordinary record to explicitly populate every layer.

It must, however, be capable of preserving these distinctions when their collapse would materially distort history.

---

# 9. Unknown-State Model

Historical shall support at least three epistemic absence states.

## HU-1 — Known Unknown

A relevant dimension is represented, but its value is unknown or uncertain.

## HU-2 — Known-Missing Dimension

A relevant information class is recognised but unavailable, inaccessible, unmeasured or inadequately represented.

## HU-3 — Later-Recognised Unrepresented Dimension

Later analysis identifies a dimension that materially affected the historical problem but was not represented as relevant within the earlier evaluation architecture.

Historical must not rewrite HU-3 as though historical actors consciously ignored a question they did not possess.

---

# 10. Historical Object Envelope

A Historical implementation should be capable of associating a record with fields or linked objects equivalent to:

- Historical Object ID;
- Source System;
- Source Object ID;
- Information Class;
- Event / State Time;
- Record Creation Time;
- Historical Custody Time;
- Version / State;
- Epistemic Status;
- Authority Status;
- Privacy / Classification State;
- Provenance References;
- Relationship References;
- Transformation History;
- Supersession Relations;
- Correction Relations;
- Access State;
- Retention State;
- Review Condition;
- Known Uncertainty / Dispute;
- Evaluation Context Reference where material;
- Search / Sampling Boundary where material;
- Completeness Scope where claimed.

The formal specification defines semantic requirements rather than implementation syntax.

---

# 11. Historical Evaluation Context

Where consequential, Historical should support a linked **Historical Evaluation Context** describing:

- evidence available;
- evidence known to have been inaccessible;
- evidence actually examined;
- method or model used;
- model version;
- categories or variables represented;
- known missing dimensions;
- interface or sensor limitations;
- search or sampling boundary;
- uncertainty;
- contemporary scope claim;
- decision context;
- later-discovered dimensions.

This object exists to preserve the evaluation environment without requiring every source record to duplicate it.

---

# 12. Custody Lifecycle

The default conceptual lifecycle is:

```text
Operational Creation
        ↓
Operational Custody
        ↓
Historical Qualification / Handoff
        ↓
Historical Custody State
        ↓
Access / Derivation / Reconstruction
        ↓
Review / Reclassification
        ↓
Cold Storage / Continued Archive / Authorised Destruction
```

Historical does not automatically become the original custodian at creation.

Operational systems retain operational responsibility until a defined handoff, dual-custody state or other authorised transition occurs.

---

# 13. Candidate Custody States

Historical shall be capable of representing states equivalent to:

- OPERATIONAL
- DUAL_OPERATIONAL_HISTORICAL
- ARCHIVAL_ACTIVE
- ARCHIVAL_RESTRICTED
- COLD_STORAGE
- RETRIEVED_FOR_BOUNDED_PURPOSE
- SUPERSEDED_BUT_PRESERVED
- PENDING_RETENTION_REVIEW
- AUTHORISED_FOR_DESTRUCTION
- DESTROYED_WITH_PROVENANCE_MARKER

These are semantic states. Implementations may use different labels provided the distinctions survive.

---

# 14. Historical Qualification and Handoff

A record may qualify for Historical custody because of:

- legal or constitutional requirement;
- accountability significance;
- civilisational significance;
- system-state significance;
- developmental significance;
- evidential significance;
- cultural significance;
- capability lineage;
- unresolved dispute;
- future reconstruction need;
- retention policy;
- explicit source-domain handoff.

Qualification does not automatically imply indefinite retention.

The precise handoff threshold remains a design question requiring domain-specific companion rules.

---

# 15. Access Architecture

Historical access must be evaluated as a relation:

```text
Record
+
Actor
+
Action
+
Purpose
+
Context
+
Time
+
Permission State
```

Historical shall not collapse the following properties:

```text
Preserved
Discoverable
Searchable
Accessible
Retrievable
Disclosable
Publishable
Correlatable
```

A record may legitimately occupy different states across these dimensions.

---

# 16. Purpose-Bounded Retrieval

Temporary or exceptional access must carry effective-time, expiry or review, authority, purpose and reversion semantics where applicable. Historical self-audit should detect permissions surviving their authorising condition.


Access permission should be capable of depending upon purpose.

Examples include:

- personal access;
- academic research;
- institutional audit;
- legal review;
- safety investigation;
- statistical analysis;
- public historical inquiry;
- restoration or recovery;
- authorised governance review.

Permission for one purpose does not imply unrestricted permission for another.

---

# 17. Privacy and Participant Rights

Historical custody must not automatically terminate legitimate participant rights.

Depending upon constitutional and domain-specific rules, these may include:

- access rights;
- correction rights;
- contextualisation rights;
- privacy rights;
- restriction rights;
- anonymisation rights;
- legitimate forgetting mechanisms.

Historical must distinguish correction from erasure.

Where an original record must remain for legitimate reasons, correction may be represented through linked state rather than silent mutation.

---

# 18. Forgetting

Historical should support intermediate information states rather than forcing a binary choice between unrestricted retention and destruction. Depending on authority and purpose, these may include de-identification, aggregation, protected linkage, restricted research environments, sealed custody and reduced discoverability.


Forgetting is not limited to physical byte deletion.

It may include authorised transitions such as:

- removal from ordinary discovery;
- removal from participant correlation;
- anonymisation;
- pseudonymisation;
- aggregation;
- sealed custody;
- cold storage;
- cryptographic inaccessibility;
- destruction.

Different mechanisms have different reversibility and epistemic consequences.

The least irreversible mechanism adequate to the legitimate purpose should be preferred where other constraints permit.

---

# 19. Destruction

A destruction claim must state its scope. Source destruction does not establish that summaries, aggregates, trained models, derived representations or other derivatives have also been destroyed.


Authorised destruction must record, where lawful and safe:

- what class of material was destroyed;
- authority for destruction;
- retention rule applied;
- date/time;
- method or process;
- whether derivatives remain;
- whether relationship information was affected;
- whether a provenance marker may legitimately survive.

A destruction marker must not preserve the sensitive substance whose destruction was required.

---

# 20. Reconstruction Services

Historical shall support at least two logically distinct reconstruction modes.

## HR-1 — Contemporary Reconstruction

Question:

> What could a participant or system at time T reasonably have known or represented through the information and evaluation architecture available at time T?

Later knowledge must be excluded or explicitly separated.

## HR-2 — Present-Best Reconstruction

Question:

> Given preserved records and subsequent discoveries, what is the present best reconstruction of the historical state at time T?

Later evidence may be used but must be identified as retrospective.

Therefore:

```text
Contemporary Reconstruction(T)
≠
Present-Best Reconstruction(T)
```

Neither should overwrite the other.

---

# 21. Reconstruction Epistemic Envelope

Where material, reconstruction outputs should expose or make retrievable:

- source corpus;
- temporal boundary;
- source-system coverage;
- known missing sources;
- accessibility constraints;
- search/traversal method;
- evidential strength;
- disputes;
- transformations;
- inferred relationships;
- unresolved questions;
- known evaluation-space limitations;
- retrospective evidence;
- scope of any completeness claim;
- confidence appropriate to demonstrated coverage.

User interfaces may summarise this information, but the underlying provenance should remain available to authorised inspection.

---

# 22. Search and Traversal Provenance

Where a negative search result materially supports a conclusion, the result must remain scoped to the evaluated search space. "No record found" must not silently become "the event did not occur."


For consequential historical research, audits or reconstruction, Historical should be capable of recording:

- corpus/version searched;
- search method;
- search terms where relevant;
- traversal path;
- depth;
- exclusions;
- inaccessible areas;
- stopping rule;
- saturation basis;
- later reopening.

This is especially important where absence of evidence affects a conclusion.

---

# 23. Pattern and Trajectory Layer

Derived pattern objects should be epistemically typed so that statistical relationship, causal hypothesis, causal evidence, interpretation and competing explanation remain distinguishable.


Historical may support derived pattern objects across:

```text
Facts
→ Sequences
→ Patterns
→ Relationships Between Patterns
→ Trajectories
→ Provenance of Interpretation
```

Derived pattern objects must preserve provenance to their supporting evidence.

Pattern detection must not silently become causal attribution.

> **Pattern ≠ Causation.**

---

# 24. Cross-Domain Pattern Value

Historical may preserve generalised trends that become useful to other domains, including:

- consumption;
- movement;
- resource demand;
- food supply;
- health;
- environmental change;
- infrastructure;
- economic behaviour;
- demographic patterns.

Historical preserves temporal evidence and derived historical patterns.

It does not thereby become the operational owner of food, health, economics, infrastructure or other domains.

---

# 25. Relational Preservation

Historical must preserve materially important edges as well as nodes.

Relationship types may include:

- dependency;
- supersession;
- correction;
- derivation;
- authority;
- contribution;
- causally claimed relationship;
- temporal sequence;
- membership;
- spatial relation;
- interface relation;
- capability dependency;
- dispute;
- alternative;
- shared provenance.

Shared provenance must not automatically be treated as shared identity.

---

# 26. Negative Space

Historical should preserve materially relevant negative space, including:

- unanswered questions;
- planned but unimplemented structures;
- abandoned alternatives;
- known missing records;
- failed searches;
- inaccessible sources;
- untested hypotheses;
- unresolved interfaces;
- known capability gaps;
- stopping decisions.

Negative space must not be transformed into positive factual claims without evidence.

---

# 27. Capability and Legacy Records

Capability lineage should support recoverability status, including documented-and-demonstrated recoverability, preserved-but-untested recovery, known tacit dependencies, known missing dependencies and currently unrecoverable historical capability.


Historical may preserve:

- technical specifications;
- dependency maps;
- procedures;
- source material;
- interfaces;
- toolchains;
- training context;
- tacit-knowledge indicators;
- known restoration barriers.

However:

> **Record Completeness ≠ Capability Recoverability.**

A preserved description of a capability does not establish that the capability can actually be reconstructed.

---

# 28. Authority Boundaries

Historical is not:

- Judiciary;
- Governance;
- Threat Governance;
- Treasury or Economic Authority;
- Research Truth Authority;
- Civil State Map;
- Continuity;
- Library;
- Knowledge Control System;
- surveillance operator;
- Civil Attention resolution authority;
- recognition or jurisdiction authority;
- constitutional amendment authority.

Historical may preserve outputs from these systems.

It may expose provenance to them.

It may support authorised reconstruction for them.

It must not silently inherit their powers.

---

# 29. Knowledge Control System Interface

The Knowledge Control System may provide general infrastructure for:

- provenance;
- versioning;
- knowledge state;
- transformation tracking;
- evidence linkage.

Historical applies such capabilities specifically to temporal custody and reconstruction.

Candidate separation:

> **KCS governs how knowledge objects are controlled and related; Historical governs how civilisational state remains interpretable across time.**

Further interface specification remains required.

---

# 30. Library Interface

Library and Historical may contain overlapping material but serve different functions.

A Library primarily enables knowledge access and use.

Historical preserves temporal state, provenance, transitions and reconstruction context.

A document can legitimately exist in both contexts with different metadata, permissions and lifecycle rules.

---

# 31. Continuity Interface

Historical can support continuity by preserving evidence of prior systems and capabilities.

It must not become the Continuity system itself.

Historical retrieval of a previous system state does not authorise restoration.

Any reactivation must pass through the relevant current authority and safety architecture.

---

# 32. Civil Attention Interface

Historical should receive appropriate records concerning:

- problem reports;
- petitions;
- responses;
- status transitions;
- resolutions;
- unresolved cases;
- feedback loops.

Historical preserves the civil attention trail.

It does not determine the operational resolution.

The Historical Domain should eventually receive its own domain-specific Civil Attention companion methodology.

---

# 33. Jurisdiction and Recognition

Historical may preserve records of:

- recognition;
- diplomatic status;
- jurisdiction;
- membership;
- authority boundaries;
- contested standing.

These records describe historical states.

They do not themselves confer present recognition, membership or jurisdiction.

---

# 34. ESCP Requirements

Historical must apply the Evaluation-Space Completeness Problem throughout its lifecycle.

At minimum:

1. do not infer global completeness from local evaluation accuracy;
2. preserve known evaluation boundaries where consequential;
3. distinguish unknown, known-missing and later-recognised unrepresented dimensions;
4. scope completeness claims;
5. preserve search and sampling boundaries where absence affects conclusions;
6. preserve representational diversity where proportional;
7. recognise interface and sensor limitations;
8. preserve enough relational and negative-space information to permit later dimensional discovery;
9. apply stronger completeness scrutiny to consequential irreversible actions;
10. preserve Historical's own architectural blind spots and revisions.

---

# 35. ESCP and Destruction

Before consequential irreversible destruction, the responsible authority should ask:

- What future uses have been represented?
- What participant harms have been represented?
- What privacy/safety requirements apply?
- What relationships would be lost?
- Could a less irreversible state satisfy the requirement?
- What dimensions are known to be missing from the decision?
- Is the decision being treated as globally justified when only locally evaluated?

Historical itself does not necessarily possess final destruction authority.

It must support the evaluation and preserve the authorised provenance.

---

# 36. Minimum Anti-Surveillance Constraint

Historical must not become a universal retrospective surveillance system merely because records exist.

The architecture must support separation between:

- retention;
- identity;
- correlation;
- search;
- access;
- disclosure.

Pattern analysis involving participants should be purpose-bounded and subject to the relevant privacy, authority and oversight architecture.

---

# 37. Minimum Anti-Dossier Constraint

Historical must not automatically aggregate every participant's records into a permanent unified profile.

Where longitudinal linkage is legitimate, it should be:

- authorised;
- purpose-bounded;
- proportionate;
- auditable;
- subject to applicable participant protections.

---

# 38. Historical Integrity

Migration integrity must include relational and semantic preservation where those properties are historically material. Object counts and checksums alone do not demonstrate historical preservation.


Historical integrity requires protection against:

- unauthorised alteration;
- silent deletion;
- provenance stripping;
- timestamp corruption;
- version collapse;
- relationship corruption;
- unauthorised reclassification;
- access-control drift;
- misleading reconstruction;
- unauthorised reactivation.

Integrity mechanisms may be technical, procedural, institutional or cryptographic.

The specification does not mandate a single implementation.

---

# 39. Correction Model

Correction relationships must be semantically typed where material. Historical should distinguish at least:

- comment;
- challenge;
- contextual addition;
- correction;
- supersession;
- reversal;
- invalidation.

A later state must not be reduced to an undifferentiated annotation.



Historical correction should ordinarily preserve:

```text
Original Historical State
        +
Correction / Challenge
        +
Evidence
        +
Authority / Method
        +
Effective Time
        +
Relationship Between States
```

The corrected interpretation becomes available without manufacturing a false earlier state.

---

# 40. Compression and Summarisation

Compression can destroy future-relevant structure.

Where compression is used, Historical should consider preserving:

- source reference;
- method;
- model/tool version where material;
- date;
- purpose;
- information intentionally removed;
- known limitations;
- relationship to uncompressed source where retained.

A summary must not silently replace its source where the source remains required.

---

# 41. Migration

Historical systems will outlive individual technical formats.

Migration procedures should preserve, as applicable:

- content;
- metadata;
- provenance;
- relationships;
- permissions;
- classification;
- timestamps;
- signatures/authenticity evidence;
- correction chains;
- retention state.

Migration loss must be recorded where detected.

---

# 42. Authenticity

Historical must support graded provenance where identity disclosure is inappropriate or impossible, including verified-but-restricted identity, intermediary-verified identity, pseudonymous, anonymous, identity unknown and authenticity disputed states.


Historical should support reasonable means to determine:

- source identity where legitimately knowable;
- whether content changed;
- when transformations occurred;
- who or what performed them;
- whether authenticity is verified, disputed or unknown.

Historical must not convert absence of authenticity evidence into automatic falsity.

---

# 43. Cultural and Living Knowledge

Not all historically important information is adequately represented as static documents.

Historical architecture should permit representation of:

- oral tradition;
- embodied practice;
- cultural context;
- procedural knowledge;
- community-held interpretation;
- living traditions.

Preservation must respect legitimate cultural, privacy and access boundaries.

---

# 44. Historical Self-Audit

Historical must preserve the history of its own observational apparatus, including collection rules, schema and taxonomy changes, retention policy, search capability, access policy, migration events and known blind spots.


Historical requires periodic self-audit covering at least:

- provenance integrity;
- access drift;
- retention-rule performance;
- destruction compliance;
- migration loss;
- classification drift;
- search bias;
- reconstruction quality;
- relationship preservation;
- privacy/correlation risk;
- ESCP blind spots;
- architectural overreach.

Audit findings themselves enter Historical custody according to applicable rules.

---

# 45. Failure Modes

Historical architecture must explicitly guard against:

1. retrospective rewriting;
2. authority inheritance;
3. universal retention;
4. universal accessibility;
5. permanent dossier formation;
6. context stripping;
7. relationship loss;
8. compression loss;
9. archive bias;
10. selection bias;
11. survivorship bias;
12. presentism;
13. false certainty;
14. false continuity;
15. false discontinuity;
16. historical reactivation error;
17. dangerous centralisation;
18. classification drift;
19. provenance drift;
20. self-sealing evaluation;
21. repository reductionism;
22. narrative dominance;
23. technical-format loss;
24. domain overreach;
25. retrospective omniscience;
26. archive-absence fallacy;
27. completeness leap;
28. evaluation-space collapse;
29. destructive loss of future discovery capacity;
30. interface-filtered history mistaken for complete history.

---

# 46. Candidate Top-Level Architecture

The Historical Domain should contain services or components corresponding to:

## HA-1 — Intake and Historical Qualification

Determines whether and how material enters Historical custody.

## HA-2 — Temporal Record Custody

Maintains historical objects and custody states.

## HA-3 — Provenance and Relationship Layer

Maintains provenance, transformations, dependencies and graph relationships.

## HA-4 — Protected Historical Storage

Provides storage appropriate to retention, classification and privacy requirements.

## HA-5 — Historical Access and Retrieval

Applies actor/action/purpose/context/time/permission rules.

## HA-6 — Reconstruction and Historical Query

Supports contemporary-state and present-best reconstruction.

## HA-7 — Pattern and Trajectory Layer

Supports bounded derived historical analysis.

## HA-8 — Retention, Forgetting and Reclassification

Manages information-state transitions and authorised destruction.

## HA-9 — Historical Integrity and Self-Audit

Monitors provenance, drift, reconstruction quality, access and ESCP-related risks.

These components may be distributed rather than implemented as one central service.

---

# 47. Centralisation Constraint

The existence of one Historical domain does not imply one physical archive.

A distributed architecture may be preferable for:

- resilience;
- privacy;
- jurisdiction;
- cultural autonomy;
- security;
- local custody;
- scale.

The domain specification standardises required semantics and interfaces, not mandatory physical centralisation.

---

# 48. Minimum Interface Contract

A system handing material to Historical should, where applicable, communicate:

- object identity;
- source domain;
- relevant timestamps;
- current state;
- authority context;
- privacy/classification requirements;
- retention requirements;
- provenance;
- relationship references;
- correction/supersession state;
- known uncertainty;
- destruction constraints;
- required future review conditions.

Historical should return a custody acknowledgement or equivalent provenance-bearing state.

Detailed interface schemas remain implementation work.

---

# 49. Historical Query Contract

A consequential query should be capable of specifying:

- requested time or interval;
- subject/domain;
- reconstruction mode;
- permitted sources;
- actor;
- purpose;
- access context;
- required epistemic detail;
- whether derived patterns are permitted.

Returned results should carry sufficient provenance to prevent them from being mistaken for unsupported historical fact.

---

# 50. What Historical Must Not Promise

Historical must not promise:

- perfect preservation;
- perfect reconstruction;
- complete truth;
- universal accessibility;
- permanent recoverability;
- absence of archival bias;
- absence of future reinterpretation;
- that all important future questions are presently representable.

Its promise is narrower and stronger:

> **to preserve and expose enough bounded, provenance-bearing historical state that legitimate future reconstruction remains possible without silently converting the surviving archive into the whole of reality.**

---

# 51. Unresolved Architecture Questions

The following remain deliberately open for subsequent development and testing:

1. Exact historical handoff thresholds by domain.
2. Final retention and destruction authority.
3. Privacy/accountability conflict resolution.
4. Distributed versus central physical architecture.
5. Mandatory versus optional metadata fields.
6. How to preserve useful relationship graphs without creating surveillance infrastructure.
7. How to preserve latent pattern value without universal raw-data retention.
8. Treatment of deceased, dormant or departed participant records.
9. Secret ballot and anonymous participation history.
10. Cross-civilisation and cross-jurisdiction retention conflicts.
11. Long-term cryptographic authenticity and migration.
12. Preservation of tacit and embodied knowledge.
13. Minimum viable preservation of option-space and negative-space information.
14. Governance of restricted historical research.
15. Emergency access and continuity availability.
16. Formal correction-graph semantics.
17. Whether a dedicated constitutional/architectural change register is required.
18. Limits and oversight of pattern analytics.
19. Formal reconstruction-quality testing.
20. Historical's Civil Attention companion methodology.
21. Formal schema for Historical Evaluation Context.
22. Criteria for determining when evaluation-space preservation is materially required.
23. Proportionality rules for irreversible contraction of future evaluation space.
24. Cross-substrate representation of historical experience without false equivalence.

Open questions are part of the specification state and must not be silently treated as resolved.

---

# 52. Development and Validation Requirements

Before graduation, this specification should be tested against representative cases including:

- ordinary public records;
- private participant records;
- judicial history;
- governance decisions;
- scientific/research development;
- failed projects;
- emergency records;
- cultural knowledge;
- economic/consumer trend data;
- health-related historical pattern data;
- classified or restricted records;
- destroyed/forgotten records;
- system migrations;
- contested historical narratives;
- a case where later evidence reveals an unrepresented contemporary dimension;
- a case where archive absence could be mistaken for non-existence;
- a case where retrieval could accidentally reactivate expired authority.

Testing should focus on boundary failures rather than merely demonstrating happy-path storage.

---

# 53. Specification Self-Scope

This specification is itself subject to ESCP.

Its source basis is the Historical source-resolution programme, Synthesis 001, Synthesis 002 and the Concord architecture available during this development phase.

It does not claim to represent every future Historical requirement.

Later evidence may reveal missing dimensions.

Such discoveries should extend or supersede this specification through preserved version history rather than retrospectively rewriting v0.2.

---

# 54. Consolidated Formal Definition

The Historical Domain preserves civilisational state across time through:

```text
Objects
+
States
+
Transitions
+
Evidence
+
Provenance
+
Relationships
+
Authority Context
+
Permission Context
+
Evaluation Context
+
Unknowns
+
Negative Space
```

so that later civilisation can reconstruct not merely **what records survived**, but what those records meant within the living systems that produced them.

---

# 55. Final Architectural Principle

> **Historical preserves the civilisation's interpretable past without claiming ownership of that past, inheriting its expired authority, or assuming that the archive's present evaluation space contains every dimension future civilisation may need. It therefore preserves not only records, but enough provenance, relationships, uncertainty, evaluation context and negative space to keep the past open to legitimate future understanding.**

---

## Specification Status

**Source Resolution:** Complete / source-domain saturated.  
**Synthesis 001:** Complete.  
**Synthesis 002:** Complete.  
**Formal Domain Specification v0.2:** Revised after Adversarial Boundary Test 001.  
**Next Development Stage:** Targeted cross-domain interface testing against systems that own Historical's unresolved external decisions, followed by resolution of high-priority open architecture questions.


---

# 56. v0.2 Adversarial-Test Integration

Formal Domain Specification v0.2 incorporates the findings of **Historical Domain — Adversarial Boundary Test 001 — Core Architecture Stress Test**.

The following refinements are now explicit requirements or architectural distinctions:

1. authority-bearing historical records require current/expired/revoked/superseded separation;
2. correction relationships require semantic typing;
3. ESCP must not be used as a universal-retention licence;
4. forgetting must support intermediate information-state transitions;
5. consequential negative search results require scoped search provenance;
6. developmental topology may require preservation beyond final versions;
7. provenance completeness does not require identity traceability;
8. source provenance may be graded and identity-protected;
9. historically consequential belief is distinct from factual endorsement;
10. interface expression must not be assumed to expose complete internal state;
11. legitimate historical custody may be distributed;
12. destruction claims must be derivative-aware;
13. migration integrity includes relationships and semantics;
14. pattern objects require epistemic typing;
15. classification must remain non-destructive where proportionate;
16. capability records require recoverability semantics;
17. temporary exceptional access requires reversion/review state;
18. Historical must preserve changes in its own observational apparatus.

These refinements do not create a new major Historical function. They operationalise requirements already latent in the v0.1 architecture.

## New Consolidated Distinctions

> **Provenance Completeness ≠ Identity Traceability**

> **Historical Significance ≠ Factual Correctness of a Preserved Belief**

> **Interface Expression ≠ Complete Internal State**

> **Object Preservation ≠ Historical Preservation**

> **Source Destruction ≠ Derivative Destruction**

> **Classification ≠ Reality**

> **Documentary Completeness ≠ Capability Recoverability**

> **Temporary Access ≠ Permanent Permission**

> **Archive Change ≠ Civilisational Change**

## v0.2 Development State

The architecture has now survived one broad adversarial boundary pass. The next evaluation should cross the Historical boundary deliberately and test whether its proposed interfaces remain coherent when resolved against the actual Concord systems that own authority, privacy, adjudication, civil attention, knowledge control, continuity and related functions.


---

# 57. v0.3 Cross-Domain Integration

Formal Domain Specification v0.3 integrates the findings of Cross-Domain Interface Tests 001–004 and the Concord's Bounded Contextual Authority architecture.

This version does not replace the source systems that resolve live authority, knowledge state, privacy entitlement, adjudication, emergency response, civil attention or continuity. It formalises how Historical preserves their temporal states and relationships.

## 57.1 Historical Handoff Modes

Historical handoff does not always mean ownership transfer.

Three modes are required:

1. **Transfer** — operational custody ends and Historical becomes the relevant archival custodian.
2. **Dual Custody** — the operational domain retains a live object while Historical preserves historical state.
3. **Reference Preservation** — Historical preserves sufficient provenance and relationship state without possessing the source content.

Therefore:

> **Historical Handoff ≠ Mandatory Ownership Transfer.**

The appropriate mode depends on source-domain function, privacy, retention, continuity, jurisdiction and access requirements.

## 57.2 Operational Current State and Historical State Sequence

Where consequential, the architecture should maintain a reconstructable relationship between:

**Operational Current State ↔ Historical State Sequence**

Historical must not create a competing live source of truth.

KCS or the appropriate operational domain remains authoritative for current represented state.

Historical preserves what that represented state was at earlier times, how it changed and what evidence/evaluation architecture bounded it.

> **Historical Reconstruction of Current-Looking Data ≠ Current Operational State.**

## 57.3 Historical Event Spine

The Historical Event Spine is retained as a semantic and temporal reconstruction view:

**Source Event → Domain Transition → Knowledge Change → Dependency Effect → Authority/Decision → Operational Outcome → Later Correction**

It should normally be constructed over provenance-bearing relationships already maintained by source domains, KCS or shared infrastructure.

Historical does not presently require an independent civilisation-wide Event Spine database.

> **Historical Event Spine = Temporal Reconstruction View, Not Automatic New Graph Authority.**

Domain-level completeness does not establish cross-domain historical completeness.

> **Domain-Level Completeness ≠ Cross-Domain Historical Completeness.**

## 57.4 BCA-Aligned Authority Representation

Authority is not modelled as a permanent property of a record, actor, office or credential.

The governing sequence is:

**Standing Eligibility → Contextual Conditions Satisfied → Bounded Authority Activated → Bounded Exercise → Exercise Terminates → Context Changes → Fresh Justification for Further Authority**

The locked-case/glass-hammer metaphor from BCA applies.

Historical therefore preserves an **Authority Activation and Exercise Record** rather than treating authority as a durable possession.

Where material, this record should preserve:

- pre-exercise context;
- standing eligibility;
- authority source;
- legitimate function;
- functional need;
- conditions;
- actor/institution;
- action;
- object;
- scope;
- space/jurisdiction;
- affected rights;
- activation time;
- bounded authority envelope;
- exercise;
- immediate consequences;
- termination/sunset;
- post-exercise context;
- later challenge/adjudication/correction;
- provenance.

A previous exercise may materially alter the next context without authorising the next exercise.

> **Past Legitimate Authority ≠ Reusable Authority.**

> **Previous Authority May Alter Future Context ≠ Previous Authority Grants Future Authority.**

> **Historical Evidence of Authority ≠ Preserved Authority.**

Historical retrieval reconstructs the authority event. It does not recreate the context that generated it.

## 57.5 Claimed, Exercised and Adjudicated Authority

Historical should preserve distinctions between:

- claimed authority;
- activated authority;
- exercised authority;
- contemporaneously recognised authority;
- contested authority;
- later-adjudicated authority;
- revoked/superseded/invalidated authority;
- current authoritative interpretation where separately resolved by the current system.

An invalid or unlawful authority claim may still correspond to a real historical event.

> **Invalid Authority Does Not Imply Non-Event.**

Judicial procedural finality must not become historical infallibility.

> **Procedural Finality ≠ Historical Infallibility.**

## 57.6 Information-State Architecture

Historical shall treat retention and access as multidimensional information states.

The following remain independently governable:

**Preserved ≠ Discoverable ≠ Searchable ≠ Accessible ≠ Retrievable ≠ Disclosable ≠ Publishable ≠ Correlatable**

Forgetting may therefore operate through reduced discoverability, access restriction, correlation restriction, pseudonymisation, anonymisation, aggregation, sealed custody, cryptographic inaccessibility or authorised destruction.

Where several mechanisms satisfy the legitimate purpose, the least irreversible adequate mechanism should normally be preferred, subject to rights and applicable authority.

This preference must not become a refusal to execute legitimately authorised destruction.

## 57.7 Information-State Transition Record

Consequential forgetting, sealing, anonymisation, disclosure-state change or destruction should support an **Information-State Transition Record** containing, where legitimate:

- affected record/reference class;
- previous information state;
- new information state;
- authorising process/reference;
- effective time;
- scope;
- affected derivatives/relationships;
- execution status;
- review/appeal state;
- minimum surviving provenance;
- access classification.

Historical preserves the transition without inventing the entitlement that authorised it.

> **Custody ≠ Adjudication.**

## 57.8 Correlation Boundary

Possession or legitimate access to separate records does not automatically authorise joining them.

> **Record A Accessible + Record B Accessible ≠ Authority to Correlate A and B.**

Cross-domain correlation is itself a bounded contextual action.

This is required because relational metadata can reconstruct identity even after direct identifiers are removed.

> **Identity Removal ≠ Relationship Removal ≠ Non-Reidentifiability.**

Historical and KCS must therefore avoid turning provenance infrastructure into universal retrospective surveillance.

## 57.9 Historical Value and Retention Authority

The Humanity Machine principle and ESCP require caution around irreversible information loss.

They do not create unlimited retention authority.

> **Historical Value ≠ Unlimited Retention Authority.**

> **Future Possible Value ≠ Sufficient Retention Justification.**

> **ESCP Is Not a Universal-Retention Licence.**

ESCP exposes both destruction-side and retention-side completeness errors.

Historical should therefore treat ESCP as a decision-quality and epistemic-humility constraint rather than as an automatic preservation rule.

> **ESCP Creates Epistemic Humility, Not Automatic Preservation.**

## 57.10 Minimum Necessary Historical Residue

Where legitimate destruction occurs, a bounded provenance marker may survive only where independently justified.

The marker should preserve no more than required to establish the authorised transition and its auditability.

It must not recreate the destroyed substance.

> **Destruction Provenance ≠ Reconstruction of Destroyed Content.**

A candidate Minimum Necessary Historical Residue may record:

- existence of a record/class where legitimate;
- transition category;
- authorising process;
- effective time;
- affected derivative classes;
- necessary audit reference;
- destruction scope.

## 57.11 Derivative-Aware Information-State Propagation

Source deletion does not establish derivative deletion.

Aggregates, summaries, trained models, cached copies, embeddings, exported datasets, dependency edges and other derived objects require explicit evaluation.

> **Source Deletion ≠ Automatic Derivative Deletion.**

Equally:

> **Derivative Status ≠ Automatic Right to Survive.**

Authorised information-state changes should propagate across known material dependencies through source-domain/KCS/shared relationship infrastructure, followed by domain-specific execution and reconciliation.

Any claim of complete deletion must remain scoped to the evaluated systems and known copies.

> **Deletion Completeness Must Be Scoped.**

## 57.12 Public Authority Accountability and Personal Privacy

Exercises of consequential public or institutional authority can create stronger provenance requirements than ordinary private activity.

This is an accountability gradient, not a general loss of privacy.

Historical should preserve the minimum information necessary to reconstruct the authority event while excluding irrelevant private detail.

> **Public Authority Accountability ≠ Permanent Private Dossier.**

> **Accountability ≠ Universal Exposure.**

## 57.13 Emergency Records

Constitutional Emergency V2 provides the governing emergency semantics.

Historical does not require a separate emergency authority system.

Emergency records preserve past authority relationships; they do not preserve emergency powers.

> **Emergency Historical Record ≠ Continuing Emergency Authority.**

> **Authentic Emergency Record ≠ Active Emergency Instrument.**

> **Integrity ≠ Current Authority.**

Emergency Decision Records are native Historical inputs and should be preserved or referenced rather than duplicated into a competing decision architecture.

## 57.14 Versioned Secrecy

Secrecy is an information state requiring justification, scope, review and termination semantics.

A Historical secrecy envelope should be capable of preserving:

- protected record/reference;
- secrecy justification;
- authority source;
- scope;
- start time;
- review time;
- expiry condition;
- disclosure condition;
- permitted actors/actions;
- later review outcomes;
- partial disclosure state;
- residual protected elements;
- provenance.

> **Operational Secrecy ≠ Constitutional Invisibility.**

> **Secrecy Persistence ⇒ Current Justification.**

> **Secrecy Is a Time-Bounded Information State, Not an Eternal Property of a Record.**

## 57.15 Emergency Surveillance and Data

Emergency collection does not create Historical retention entitlement.

Post-emergency review should determine whether emergency-collected information is destroyed, anonymised, aggregated, sealed, restricted or preserved for independently justified accountability purposes.

> **Emergency Collection ≠ Historical Retention Entitlement.**

Purpose-specific emergency access does not authorise later repurposing.

> **Historical Availability ≠ Repurposing Authority.**

## 57.16 Contemporary and Retrospective Emergency Records

Historical should distinguish contemporaneous records from retrospective reconstruction.

Urgency may legitimately delay documentation, but later documentation must not be backdated epistemically.

> **Later Documentation ≠ Contemporaneous Evidence.**

Repeated emergency renewal should be represented as a sequence of new justification events.

> **Repeated Renewal ≠ One Original Justification.**

## 57.17 Emergency Recovery Sequence

The end of an emergency is not necessarily a single state transition.

Historical should be able to reconstruct:

**Threat Reduction → De-escalation → Authority Sunset → Access Reversion → Data Review → Secrecy Review → Institutional Dissolution/Reversion → Rights Restoration → Dependency Cleanup → Post-Emergency Audit**

> **Emergency End ≠ Instantaneous Restoration of Normal State.**

## 57.18 Controlled Redundancy

Distributed Historical storage may be required for resilience.

Replication must preserve privacy, access, secrecy and destruction semantics.

> **Redundancy ≠ Uncontrolled Replication.**

An authorised information-state transition should propagate to legitimate replicas according to their custody role.

## 57.19 Civil Attention Resolution State

Historical preservation of Civil Attention must distinguish:

- parent Issue state;
- Domain Action state;
- domain completion;
- central issue resolution;
- participant feedback/review state;
- reopening.

> **Domain Completion ≠ Issue Resolution.**

Historical records the path without becoming the resolution authority.

## 57.20 KCS Review State

KCS states such as REVIEW_REQUIRED must survive Historical reconstruction without being converted into invalidity.

> **REVIEW_REQUIRED ≠ Invalid.**

Historical should preserve what the live knowledge architecture represented at T, not substitute the current KCS reconstruction of what it now believes the dependencies were.

## 57.21 Library, Historical and Continuity Separation

The functional separation is:

> **Library preserves usable civilisational knowledge; Historical preserves interpretable civilisational past state; Continuity preserves the ability to carry necessary civilisational capability forward.**

Overlap of content does not collapse these functions.

Historical retrieval of a capability does not authorise restoration or operation.

> **Preserving an Executable Capability ≠ Authorising Its Execution.**

Technical capability is not civil authority.

## 57.22 Revised Core Access Rule

Historical access should now be interpreted through BCA:

**Actor + Record + Action + Purpose + Context + Legitimate Function + Functional Need + Scope + Time + Conditions + Authority Source → Bounded Historical Permission**

This replaces any interpretation of access as a durable generic permission.

Permission for one action or purpose does not propagate to another.

## 57.23 New v0.3 Invariants

The following invariants are added to H-I1 through H-I18:

**H-I19 — Past Legitimate Authority Is Not Reusable Authority.**

**H-I20 — Historical Value Does Not Create Unlimited Retention Authority.**

**H-I21 — Correlation Requires Its Own Legitimate Authority.**

**H-I22 — Destruction Provenance Must Not Reconstruct Destroyed Substance.**

**H-I23 — Emergency Historical Records Do Not Preserve Emergency Power.**

**H-I24 — Secrecy Is a Reviewable Information State.**

**H-I25 — Information-State Change Must Remain Propagatable Across Known Material Dependencies.**

**H-I26 — Historical Handoff Does Not Necessarily Transfer Ownership.**

**H-I27 — Operational Current State and Historical Reconstruction Must Remain Distinguishable.**

**H-I28 — Historical Redundancy Must Preserve Information-State Constraints.**

## 57.24 New v0.3 Failure Modes

The failure-mode register is extended with:

31. authority represented as durable possession rather than contextual activation;
32. past authority mistaken for reusable authority;
33. cross-domain correlation without independent justification;
34. anonymisation defeated by relational re-identification;
35. ESCP used to justify universal retention;
36. destruction marker recreating destroyed content;
37. derivative survival ignored during deletion;
38. deletion claimed complete beyond evaluated scope;
39. emergency access persisting after function termination;
40. static secrecy persisting without review;
41. emergency record treated as active instrument;
42. retrospective documentation represented as contemporaneous;
43. repeated emergency renewal collapsed into one original justification;
44. emergency collection repurposed without new authority;
45. uncontrolled archival replication;
46. operational current state confused with Historical reconstruction;
47. Event Spine duplicated as an unnecessary competing civil graph;
48. domain completion confused with Civil Attention issue resolution;
49. KCS review state mistaken for invalidity;
50. preserved executable capability mistaken for permission to execute.

## 57.25 Revised High-Priority Open Questions

Cross-domain testing resolves or substantially narrows several v0.2 questions.

Remaining high-priority questions include:

1. exact Historical handoff thresholds and preferred handoff mode by domain;
2. final constitutional/legal allocation of retention and destruction authority;
3. formal schema for Information-State Transition Records;
4. formal Correlation Permission architecture and oversight;
5. derivative-propagation and reconciliation protocol;
6. treatment of deceased, dormant or departed participant records;
7. cross-civilisation and cross-jurisdiction retention conflicts;
8. long-term cryptographic authenticity and migration;
9. preservation of tacit and embodied knowledge;
10. formal correction-graph semantics;
11. limits and oversight of pattern analytics;
12. formal reconstruction-quality testing;
13. Historical Civil Attention companion methodology;
14. formal Historical Evaluation Context schema;
15. proportionality rules for irreversible contraction of future evaluation space;
16. cross-substrate representation of historical experience without false equivalence;
17. implementation boundary between KCS relationship infrastructure and Historical temporal projections;
18. machine-readable authority-envelope and non-reactivation status schema;
19. controlled-redundancy protocol for restricted and destructible records;
20. long-duration secrecy review where disclosure itself remains dangerous.

## 57.26 v0.3 Validation State

The architecture has now been tested against:

- core internal boundary failures;
- Civil Attention;
- KCS;
- Continuity;
- Judiciary;
- Governance;
- Bounded Contextual Authority;
- privacy and participant data;
- forgetting and destruction;
- emergency authority;
- emergency secrecy;
- emergency surveillance;
- emergency recovery.

No tested interface requires Historical to acquire a new sovereign or operational authority.

The repeated pattern is instead that Historical requires richer temporal, provenance, information-state and relationship semantics while authority remains with the legitimate current system.

This is a strong architectural convergence result.

---

# 58. v0.3 Consolidated Architectural Principle

> **Historical preserves enough bounded, provenance-bearing civilisational state to reconstruct what existed, what was represented, what authority legitimately or purportedly operated, what remained unknown, how states changed, and what consequences followed — while preserving the distinction between past and present, evidence and reality, custody and authority, preservation and accessibility, relationship and identity, historical value and retention entitlement, and authentic record and executable power.**

Historical's strongest protection is therefore not maximal storage.

It is **faithful temporal context with bounded custody**.

The domain should preserve enough of the Humanity Machine that future civilisation can discover relationships the present cannot yet see, while refusing the opposite error of treating every possible future question as authority to retain every present detail forever.

---

## Specification Status — v0.3

**Source Resolution:** Complete / source-domain saturated.  
**Synthesis 001:** Complete.  
**Synthesis 002:** Complete.  
**Adversarial Boundary Test 001:** Complete.  
**Cross-Domain Interface Tests 001–004:** Complete.  
**Formal Domain Specification v0.3:** Integrated development draft.  
**Next Development Stage:** Formal schema extraction and targeted validation of the v0.3 objects/interfaces before considering domain graduation.
