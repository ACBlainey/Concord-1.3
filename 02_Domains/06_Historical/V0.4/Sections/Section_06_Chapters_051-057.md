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

Further implementation and validation should test this operational specification against representative cases including:

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

The standing functional mandate of Historical is separate from each authority event it records. That mandate permits lawful custody, protection, preservation, indexing and authorised reconstruction without a fresh triadic decision for every routine action. The recorded event's authority is never imported into Historical through possession, authenticity, custody or retrieval. A purported mandate must be proven by the actor claiming it; the archive need not prove the absence of an undocumented power.

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
**Historical V0.4:** Current operational sectional edition, retaining the v0.3 source and its development provenance.  
**Further work:** Formal schema extraction, targeted implementation and interface validation, and resolution of identified design questions; no separate graduation condition applies.
