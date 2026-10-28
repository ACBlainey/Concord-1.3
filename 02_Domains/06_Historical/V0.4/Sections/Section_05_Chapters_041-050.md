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

