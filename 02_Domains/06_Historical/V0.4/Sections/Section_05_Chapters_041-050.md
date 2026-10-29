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

Migration must preserve the distinction between the original decision-time record, later corrections, and the current operational state. Reformatting or rehosting a Governance vote, Judiciary case, Continuity declaration or authority receipt cannot reissue its mandate, change its effective time or make a superseded state executable. Where the source system remains operational, Historical's migrated copy is not the current authority source. If custody, permissions or provenance cannot be verified, the affected material must remain restricted pending competent review rather than silently acquiring a more permissive state.

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

Authenticity of a document, signature or archived credential is distinct from validity of the authority it purports to describe. A genuine record can describe an expired, invalid or unauthorised act; a verified historical appointment does not establish current authority. Any actor claiming a live mandate bears the burden of proving the explicitly documented mechanism and applicable state. Historical may authenticate evidence for competent review but cannot itself validate or create the mandate.

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

Where knowledge is held by a living community, Historical custody must not be inferred from the cultural value of the knowledge alone. The lawful custodian, consent or other valid access basis, restrictions on recording and disclosure, and the ability to correct context require explicit treatment. A preserved account must distinguish community testimony, external interpretation and disputed attribution; Historical may not convert preservation into ownership or decision authority over the community. Architecture to be designed — consent and custody interfaces for living traditions and restricted cultural knowledge.

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

Self-audit is limited to Historical's actual custody, retrieval, disclosure, retention, correction and interface mechanisms. It must not repeatedly hypothesise undocumented authority pathways in other domains: where no explicit constitutional method exists, there is no authority to audit as though granted. Actual unauthorised access, coercion, forged mandates or implementation bypasses remain reviewable as concrete events. An audit may preserve evidence and refer a matter to competent oversight, but does not acquire investigative, prosecutorial or judicial authority by conducting the audit.

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

# 46. Top-Level Functional Architecture

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

A custody acknowledgement must identify the handoff mode (transfer, dual custody or reference preservation), the accepted object/version, the accountable operational and archival custodians, the effective transition and any rejected or pending obligations. An acknowledgement of receipt is not proof that live operational responsibility ended. Historical must not activate an archived decision, replace a Governance or Judiciary authority state, or initiate Continuity restoration. Architecture to be designed — authenticated handoff, retries, duplicate messages, failed acknowledgements, access restrictions and recovery after interrupted transfer.

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

