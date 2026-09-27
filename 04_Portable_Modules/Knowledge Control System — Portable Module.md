# Knowledge Control System — Portable Module

**Project:** The Concord — Portable Modules  
**Source:** Concord Knowledge Control System source family  
**Development method:** PMEDG v1.0  
**Version:** 1.0  
**Status:** GRADUATED PORTABLE MODULE / SPECIFICATION-LEVEL TRANSFER VALIDATED  
**Date:** September 2026

## 1. Purpose

The Knowledge Control System (KCS) is a portable architecture for preserving accumulated knowledge, reasoning history and reusable capability outside the active context of individual participants while retaining provenance, differentiated state and bounded retrievability.

Its purpose is not to make every participant remember everything.

Its purpose is to make a larger learning system capable of remembering what matters and supplying relevant material when needed.

> **Persistent Shared Memory ≠ Individual Active Context**

KCS can be used by organisations, research programmes, engineering systems, software projects, AI-agent ecosystems, archives, long-duration projects and other complex learning systems.

---

## 2. Portable problem

Complex learning systems accumulate more information, reasoning and capability than any one participant can keep continuously active.

Simple storage does not solve the problem.

Accumulated material can become duplicated, outdated, contradictory, superseded, disputed, computationally expensive, detached from provenance, difficult to retrieve, difficult to distinguish by evidential status, or impossible to interpret after its original creator disappears.

The portable problem is:

> **How can a complex learning system preserve accumulated knowledge, reasoning history and reusable capability in a provenance-visible and state-differentiated form, while allowing participants to retrieve what they need without carrying the entire accumulated state in active context?**

---

## 3. Core principle

The portable KCS cycle is:

> **Record → preserve provenance → classify represented state → retain history → make retrievable → reuse → evaluate/update → preserve the new state without silently erasing the old one.**

A broader learning cycle is:

> **Remember → retrieve → investigate → contribute → validate → share → improve → remember again.**

The central architectural invariant is:

> **Current State Must Not Silently Erase the Path to Current State**

subject to legitimate external privacy, security, retention and deletion constraints.

---

## 4. What “control” means

“Control” means structured management of knowledge state, provenance, history and retrieval.

It does not mean authority over participants.

KCS can record, classify, preserve, version, retrieve, link, archive, mark dispute, mark supersession, preserve attribution, expose uncertainty and preserve reusable capability references.

KCS does not inherently govern participants, compel belief, allocate civil authority, decide rights, punish contributors, determine personal worth, allocate resources, establish truth by vote or execute downstream remedies.

> **Knowledge State ≠ Authority**

> **Repository Status ≠ Compulsory Belief**

---

# 5. Knowledge-object model

A KCS implementation should be able to represent a knowledge object containing, where applicable:

[
K_o = langle ID, C, T, P, E, S_e, S_r, S_i, S_a, H, S_c, L angle
]

where:

- (ID) = stable object identifier;
- (C) = content or content reference;
- (T) = object type;
- (P) = provenance;
- (E) = evidence/context/assumptions;
- (S_e) = epistemic state;
- (S_r) = retrieval/activity state;
- (S_i) = integrity state;
- (S_a) = access/visibility state;
- (H) = historical/version state;
- (S_c) = capability-operational state where applicable;
- (L) = typed relations to other represented objects.

This is a logical information model, not a mandatory database schema.

The state dimensions must not be collapsed merely for implementation convenience.

---

# 6. Object types

KCS may preserve many kinds of reusable cognitive products, including:

- findings;
- hypotheses;
- observations;
- datasets;
- models;
- methods;
- calculations;
- designs;
- procedures;
- software;
- algorithms;
- simulations;
- failed approaches;
- negative results;
- reasoning records;
- summaries;
- tools;
- validation results;
- decision records;
- bounded search-result records.

KCS does not assume every object is a factual claim.

Object type affects what its states mean.

---

# 7. Provenance

For significant objects, provenance should preserve enough information to answer questions such as:

- Who or what created this?
- When?
- From what inputs?
- Using what tools or methods?
- Under what assumptions or context?
- What modified it?
- What validated or challenged it?
- What derivatives followed?
- What is its current represented state?
- What process supplied consequential state assignments?

A useful provenance chain is:

> **Original contribution → modification → evaluation → derivative → validation → further modification**

Exact provenance depth should be proportionate to consequence, feasibility, privacy and host requirements.

KCS does not require permanent retention of every low-level interaction.

---

# 8. Independent state dimensions

BTT-001 demonstrated that a single universal status is inadequate.

A KCS object may simultaneously carry multiple independent state dimensions. Each consequential state assignment may be explicitly scope-qualified, so the same object can legitimately hold different represented states in different hardware generations, environments, times or other bounded contexts.

## 8.1 Epistemic state (S_e)

Represents current evidential/support status.

Example vocabulary:

- ESTABLISHED;
- VALIDATED;
- PROVISIONAL;
- DISPUTED;
- UNCERTAIN;
- SPECULATIVE;
- SUPERSEDED;
- REJECTED.

The vocabulary may be extended by a host if semantics remain explicit.

> **Recorded ≠ True**

> **Contributor Confidence ≠ Host Confidence**

> **Current Consensus ≠ Permanent Truth**

## 8.2 Retrieval/activity state (S_r)

Represents whether the object is currently active in ordinary retrieval/use.

Example vocabulary:

- ACTIVE;
- AVAILABLE;
- DORMANT;
- ARCHIVED;
- DEPRECATED;
- UNAVAILABLE.

This dimension does not determine truth, integrity or permission.

> **Archived ≠ False**

> **Active ≠ True**

## 8.3 Integrity state (S_i)

Represents integrity/provenance condition.

Example vocabulary:

- INTACT;
- QUESTIONED;
- UNDER-REVIEW;
- INTEGRITY-COMPROMISED;
- CORRECTED.

Integrity status is not an epistemic status.

An honest error does not automatically make an object INTEGRITY-COMPROMISED.

## 8.4 Access/visibility state (S_a)

Represents whether a particular host/user/context may see or retrieve an object.

Example vocabulary:

- OPEN;
- CONTROLLED;
- RESTRICTED;
- SEALED;
- REDACTED;
- EXPIRED;
- DELETED-BY-POLICY;
- UNAVAILABLE-BY-POLICY.

Access status is not epistemic status and is not ordinary activity status.

> **Restricted ≠ Rejected**

## 8.5 Historical/version state (H)

Represents an object's position in its development lineage.

Examples:

- ORIGINAL;
- MODIFIED;
- CORRECTED;
- SUPERSEDED-VERSION;
- CURRENT-VERSION;
- PRIOR-VERSION.

Historical/version state may also be represented through version links rather than one label.

## 8.6 Capability-operational state (S_c)

Used for reusable software, models, procedures or other executable/operational capabilities.

It should distinguish at least:

- stored-object availability;
- activation state;
- validation currency;
- compatibility/dependency state.

Example capability metadata:

- STORED;
- ACTIVE;
- DORMANT;
- ARCHIVED;
- CURRENTLY-VALIDATED;
- VALIDATION-EXPIRED;
- COMPATIBLE;
- COMPATIBILITY-UNKNOWN;
- DEPENDENCY-INCOMPLETE;
- REVALIDATION-REQUIRED.

A host may implement these as separate fields rather than one state list. To avoid vocabulary collision, stored-object availability and capability activation should be separately named/fielded in implementations; an AVAILABLE stored object must not imply an ACTIVE capability.

A procedure requires capability-operational metadata only when it is itself executable/operational or depends on a recoverable operational mechanism. A declarative rule or policy need not be treated as a capability merely because it guides action.

> **File Available ≠ Capability Executable**

> **Capability Preserved ≠ Capability Currently Validated**

---

# 9. State-assignment interface

KCS represents state assignments and their provenance.

It does not manufacture the legitimate basis for consequential state changes.

A consequential state assignment should, where applicable, identify:

[
A_s = langle object, state, basis, source/process, time, evidence, scope angle
]

For example, marking a claim REJECTED may record the evidential review that supplied that classification.

Marking material INTEGRITY-COMPROMISED may record the investigation or evidence supporting that status.

KCS may technically store the label, but:

> **Ability to Write State ≠ Legitimate Basis to Assign State**

The host must supply the appropriate evidential, legal, security, governance or other legitimate process.

---

# 10. Typed relation minimum

BTT-001 exposed the need for relation semantics.

A portable KCS should support at least the following relation types where applicable:

- **DERIVED_FROM** — object was materially produced from another;
- **SUPPORTS** — provides evidence supporting another represented claim;
- **CONTRADICTS** — provides evidence materially inconsistent with another;
- **CORRECTS** — explicitly repairs an error in another object/version;
- **SUPERSEDES** — becomes the current replacement for another representation;
- **NARROWS** — asserts a more limited scope than another claim;
- **QUALIFIES** — adds conditions or limitations without necessarily replacing the original;
- **REPLICATES** — records a materially comparable successful reproduction;
- **FAILED_TO_REPLICATE** — records a materially comparable unsuccessful reproduction;
- **SUMMARISES** — compressed representation of other material;
- **RELATED_TO** — generic relation when a stronger semantic relation is not justified.

Relation assignment should itself preserve provenance where consequential. Relations may also carry explicit scope/context qualifiers; for example, SUPERSEDES may mean “supersedes for generation 4+” rather than universal replacement.

This vocabulary is not a dependency-propagation ontology.

> **Typed Relation ≠ Material Dependency**

Where change-impact review is required, use an external dependency/change-propagation mechanism.

---

# 11. Historical preservation

KCS should preserve change as history rather than silently replacing it.

A correction should normally form:

> **Old State → Correction/Supersession Record → New State**

The previous state remains reconstructable where legitimate retention permits.

This allows later questions such as:

> Why did the system believe or do this at time T?

Historical preservation supports audit, learning, reproducibility and interpretation.

---

# 12. Knowledge is not truth

A KCS repository must not present itself as an oracle.

It can contain correct claims, incorrect claims, uncertain claims, competing interpretations, historical beliefs, failed hypotheses, deliberately corrupted material preserved as evidence and unresolved questions.

The system must distinguish:

> **What is recorded**

from:

> **What is currently supported**

and, where relevant:

> **What a particular contributor believed.**

These can differ without contradiction.

---

# 13. Honest failure as knowledge

An incorrect result can still contain useful information.

A useful negative-knowledge chain is:

> **Hypothesis → investigation → falsification → residual knowledge → new hypothesis**

A failed investigation may establish a pathway that does not work, an incorrect assumption, a boundary condition, a method-specific failure, an unexpected relationship or a reason another line deserves attention.

Therefore:

> **Incorrect Result ≠ Useless Contribution**

KCS should preserve useful negative results without misclassifying them as validated positive claims.

---

# 14. Epistemic failure and integrity failure

### Epistemic failure

A participant acts in good faith but reaches an incorrect or unsupported conclusion.

### Integrity failure

Material provenance, evidence, uncertainty or representation is deliberately falsified or corrupted, or a legitimate external process has otherwise established an integrity defect.

Therefore:

> **Epistemic Failure ≠ Integrity Failure**

KCS can record the resulting integrity state and its provenance.

It does not itself determine punishment, legal liability or civil standing.

---

# 15. Reasoning pathways

Where proportionate and available, KCS should preserve more than final conclusions.

Useful reasoning-path information can include:

- initial assumptions;
- hypotheses;
- alternatives considered;
- evidence;
- calculations;
- experiments;
- failed branches;
- revisions;
- criticism;
- conclusions.

This allows later users to ask:

> **Why was this conclusion reached?**

rather than only:

> **What was the conclusion?**

The architecture does not require storage of every intermediate token or private thought process. It requires enough legitimate reconstructable reasoning/provenance to meet the host's purpose.

---

# 16. Persistent memory and active context

KCS separates:

> **Persistent Shared Memory**

from:

> **Current Working Context**

A participant should be able to retrieve a bounded package relevant to the current task rather than loading the entire repository.

---

# 17. Bounded retrieval contract

A retrieval request should identify, where applicable:

- task/query scope;
- requesting context;
- access scope;
- time/version scope;
- desired evidence depth;
- relevant status filters;
- provenance depth.

Conceptually:

[
R(q,c) ightarrow {K_1, K_2, ..., K_n}
]

A minimum retrieval package should provide:

1. **scope and limits** — what was requested and what search/access boundaries apply;
2. **current orientation** — current summary/state where available;
3. **directly material objects** — the objects most relevant to the stated task;
4. **uncertainty/dispute** — material unresolved disagreement or confidence limitations;
5. **provenance pointers** — routes to underlying source/evidence;
6. **history pointers** — corrections, supersession and relevant prior states;
7. **known search limits** — unavailable indexes, access restrictions, incomplete source spaces or unresolved absence;
8. **on-demand deep material** — relevant underlying records not automatically injected into active context.

The exact ranking algorithm remains host/domain dependent.

KCS requires boundedness and transparency of retrieval scope, not one universal relevance function.

> **Not Retrieved ≠ Does Not Exist**

> **Not Recorded ≠ Does Not Exist**

> **Successful Retrieval ≠ Complete Evaluation Space**

---

# 18. Bounded search-result / absence record

Where absence itself becomes decision-relevant, KCS may preserve a bounded search-result object:

[
S_q = langle query, scope, time, sources, result, limitations, alternatives angle
]

It may record:

- query/search terms;
- time;
- repositories/indexes/sources searched;
- access boundary;
- result such as NO MATCH FOUND;
- known search limitations;
- unresolved plausible explanations.

A negative search result is evidence about a search, not proof about reality. If a later search locates the object, preserve the earlier search result as historically accurate for its original scope/time and link the later result through CORRECTS, SUPERSEDES or an equivalent host relation; do not rewrite the earlier search as though it never occurred.

> **No Match Found ≠ Object Does Not Exist**

This is an explicit ESCP safeguard.

---

# 19. Reusable capability

KCS may preserve software, models, algorithms, procedures, datasets and other reusable capabilities.

A capability object may include:

- purpose;
- provenance;
- version;
- dependencies;
- compatibility information;
- validation state;
- documentation;
- activation/retrieval requirements;
- integrity state;
- stored-object availability;
- current capability-operational state.

The principle is:

> **Preserve capability without necessarily maintaining constant activation.**

A preserved tool is not automatically safe, compatible, licensed, authorised or executable.

---

# 20. Capability revalidation

A capability represented as dormant or archived should not automatically become operational merely because its files can be retrieved.

Reactivation may require external verification of:

- dependencies;
- runtime environment;
- data formats;
- interfaces;
- licences;
- security;
- safety;
- documentation;
- validation currency.

KCS records the resulting state.

It does not itself perform or authorise every revalidation.

---

# 21. Stewardship

Knowledge preservation consumes resources.

KCS may support:

- deduplication;
- compression;
- summarisation;
- archival;
- deprecation;
- resource-aware replication;
- relevance classification;
- retrieval optimisation;
- periodic review.

The objective is not maximum accumulation.

It is useful persistent memory at acceptable resource cost.

---

# 22. Compression without provenance destruction

A current summary may replace repeated active retrieval of a large historical corpus.

But:

> **Compression ≠ Provenance Destruction**

A compressed representation should, where legitimate and available, retain a route to source material, evidence, prior versions, assumptions and unresolved disputes.

A user should be able to ask:

> **Why does the current summary say this?**

and obtain the supporting path to the degree allowed by access and retention constraints.

---

# 23. Attribution

Shared use does not require contribution history to disappear.

KCS can preserve creator, modifier, validator, derivative contributor, source systems and contribution history.

This supports attribution without deciding ownership law, payment, authority or civil standing.

> **Shared Availability ≠ Anonymous Origin**

---

# 24. Contextual contribution evidence

A host may record domain-specific evidence such as:

- accuracy;
- reproducibility;
- utility;
- provenance integrity;
- epistemic honesty;
- stewardship;
- collaboration;
- improvement.

Where consequential or person-linked, contribution evidence should retain:

- domain;
- relevant time/context;
- evidential basis;
- uncertainty;
- disputes/corrections;
- provenance;
- legitimate purpose/access interface.

It must not be collapsed into:

> **How good is this participant?**

The relevant question is narrower:

> **What does the recorded evidence say about these contributions in this domain and context?**

Therefore:

> **Contribution Evidence ≠ Personal Worth**

> **Reliability Evidence ≠ Authority**

> **Recorded Utility ≠ Entitlement**

Permanent or universal aggregation of contextual contribution evidence into a person-level index is outside the KCS kernel and creates a predictable contribution-to-worth/authority-laundering risk.

Any consequential employment, authority, access or resource decision requires an external legitimate process.

---

# 25. Privacy, security, retention and forgetting

Provenance and historical preservation do not justify unlimited retention or universal visibility.

> **Preserve Provenance ≠ Preserve Everything Forever**

> **Preserve History ≠ Expose History to Everyone**

A host supplies legitimate policies/processes for access, privacy, security, retention, expiry, deletion, legal obligations and protected information.

KCS can represent:

- RESTRICTED;
- SEALED;
- REDACTED;
- EXPIRED;
- DELETED-BY-POLICY;
- UNAVAILABLE-BY-POLICY.

A redacted derivative may preserve a DERIVED_FROM relation to a restricted/sealed source while exposing only the minimum permitted source identity/provenance metadata. The relation must not leak protected content.

Where lawful and appropriate, a removed object may leave a tombstone or minimal provenance trace indicating that an object existed and was removed/restricted.

Where legitimate policy or law forbids even that trace, KCS must not manufacture one.

> **Historical Preservation Is Bounded by Legitimate Retention**

---

# 26. External interface contracts

KCS is a memory/provenance layer, not an all-purpose control system.

## 26.1 Host evidential/review process

**KCS supplies:** objects, provenance, evidence links, history and current represented states.

**Host process supplies:** legitimate basis for consequential epistemic/integrity classifications.

KCS records the resulting assignment and provenance.

## 26.2 Access/retention process

**KCS supplies:** object identity, provenance and represented access/retention metadata.

**Host process supplies:** legitimate access, privacy, expiry, redaction, sealing and deletion decisions.

## 26.3 KCS Change Propagation

**KCS supplies:** object identities, typed relations and represented dependency records where available. A minimum dependency handoff should identify source object/version, dependent object/version, relation/dependency type if known, scope/context and provenance.

**Change-propagation process supplies:** material downstream review decisions when a source object changes.

KCS does not duplicate the propagation algorithm.

## 26.4 Continuity/recovery

**KCS supplies:** preserved knowledge/capability objects and their represented operational metadata.

**Continuity process supplies:** assessment of whether sufficient function and enabling dependencies survive or can be recovered.

> **Preserved Knowledge ≠ Recoverable Function**

## 26.5 Governance/allocation

**KCS supplies:** relevant contextual evidence where legitimately requested.

**Host process supplies:** authority, due process, allocation, employment or other consequential decisions.

---

# 27. Minimal operating cycle

1. **INGEST** — receive object and provenance.
2. **CLASSIFY** — assign explicit object type and represented states from legitimate inputs/processes.
3. **PRESERVE** — retain content/reference, provenance and required history.
4. **INDEX/LINK** — assign justified typed relations and make legitimate relationships discoverable.
5. **RETRIEVE** — supply a bounded task-relevant package.
6. **USE/INVESTIGATE** — external participant/process acts on the material.
7. **REVIEW** — receive validation, criticism, correction or new evidence.
8. **UPDATE** — create new state/version without silently erasing old state.
9. **STEWARD** — adjust active/archive/compression state subject to host constraints.
10. **REPEAT**.

---

# 28. Example — research history

A research group records a promising hypothesis as PROVISIONAL.

A later laboratory fails to reproduce it.

The failed replication is stored as its own object and linked FAILED_TO_REPLICATE.

Further contrary evidence leads a legitimate evidential process to classify the broad hypothesis REJECTED.

The original hypothesis remains historically reconstructable.

A methodological artefact discovered during the failed replication is preserved separately as reusable negative knowledge.

Years later a narrower claim receives new evidence.

It is represented as a new object linked NARROWS or QUALIFIES rather than rewriting the old broad rejected claim.

---

# 29. Example — dormant software capability

An organisation preserves a specialist conversion tool after a migration project.

Its source and documentation remain AVAILABLE as stored objects.

The capability itself is DORMANT.

Years later its validation currency is EXPIRED and compatibility is UNKNOWN because the old runtime has disappeared.

Retrieval does not automatically change the capability to operational.

External revalidation is required before use.

---

# 30. Failure modes

### KCS-F1 — Oracle failure
Repository state is treated as truth.

### KCS-F2 — Historical erasure
Rejected or superseded material disappears as though it never existed.

### KCS-F3 — Provenance loss
Content survives while origin, assumptions or modification history disappear.

### KCS-F4 — Context overload
Retrieval indiscriminately returns the repository rather than task-relevant material.

### KCS-F5 — Runaway accumulation
Everything remains active or equally prominent.

### KCS-F6 — Compression loss
Summary replaces underlying evidence without a reconstructable route.

### KCS-F7 — False certainty
Dispute or uncertainty is collapsed into one authoritative state.

### KCS-F8 — Integrity conflation
Honest error and deliberate integrity failure are treated as equivalent.

### KCS-F9 — Contribution-to-worth collapse
Contextual evidence becomes a universal participant score.

### KCS-F10 — Authority laundering
Reliability, utility or repository centrality becomes authority.

### KCS-F11 — Surveillance creep
Provenance becomes justification for indefinite unnecessary monitoring.

### KCS-F12 — Suppression by status
Current rejection becomes automatic illegibility or historical deletion.

### KCS-F13 — Dormant-capability decay
A preserved tool is represented as operationally available despite unusable dependencies, expired validation or incompatible formats.

### KCS-F14 — Access leakage
Sensitive content or provenance is exposed beyond legitimate scope.

### KCS-F15 — Completeness illusion
Repository/search absence is treated as reality absence.

### KCS-F16 — Module absorption
KCS absorbs dependency propagation, continuity, governance or other external functions and becomes an unbounded central system.

---

# 31. Falsification / revision conditions

The specification requires revision if transfer testing shows that:

1. users cannot distinguish represented state from truth;
2. provenance cannot survive correction/supersession;
3. rejected or superseded material must be erased for the mechanism to function;
4. useful retrieval requires loading the whole repository;
5. independent state dimensions necessarily collapse;
6. useful negative results cannot be represented;
7. contribution evidence necessarily becomes a universal personal score;
8. basic memory/provenance functions require Concord-specific governance;
9. KCS must internally duplicate change propagation to function;
10. legitimate privacy/security/retention constraints cannot coexist with history/provenance;
11. a clean evaluator cannot apply the architecture outside civilisation-scale use;
12. the architecture inherently centralises authority rather than knowledge representation;
13. file availability cannot be separated from operational capability;
14. bounded negative search results necessarily become claims of nonexistence.

---

# 32. Minimum implementation requirements

A system claiming to implement the portable KCS kernel should minimally provide:

1. identifiable knowledge objects;
2. provenance;
3. explicit epistemic state;
4. explicit retrieval/activity state;
5. explicit integrity state where applicable;
6. explicit access/visibility interface;
7. version/correction/supersession history;
8. bounded retrieval with scope/limit representation;
9. preservation of uncertainty/dispute;
10. ability to preserve useful negative knowledge;
11. attribution;
12. external access/retention constraints;
13. distinction between knowledge state and authority;
14. explicit completeness limitation;
15. capability-operational distinction where reusable capability is represented;
16. typed relations sufficient to distinguish correction, supersession, qualification and derivation.

---

# 33. Non-requirements

KCS does **not** require:

- a single central database;
- one universal ontology;
- one universal truth authority;
- one participant rating;
- permanent storage of every interaction;
- universal visibility;
- all capabilities to remain active;
- Concord governance;
- a particular software stack;
- a particular AI architecture;
- one universal retrieval-ranking algorithm;
- KCS itself to decide legitimate access, authority or retention.

The logical system may be physically distributed.

---

# 34. Validation record

KCS completed two independent blind transfer tests in materially different non-Concord domains.

- BTT-001 — pharmaceutical R&D: KCS-T3; 46/46 frozen predictions materially confirmed; 0/10 fundamental failures.
- BTT-002 — long-lived aerospace engineering and mission operations: KCS-T3; 50/50 frozen predictions materially confirmed; 0/12 fundamental failures.

> **CROSS-TEST CONVERGENCE OBSERVED**

The formal PMEDG Graduation Review passed and authorised v1.0 release.

> **GRADUATED PORTABLE MODULE / SPECIFICATION-LEVEL TRANSFER VALIDATED**

This status does not claim universal empirical validation.

# 35. Release status

**Version:** 1.0

KCS is released as a standalone portable module.

Future changes should follow explicit version control and should preserve the validated kernel unless new evidence justifies revision.
