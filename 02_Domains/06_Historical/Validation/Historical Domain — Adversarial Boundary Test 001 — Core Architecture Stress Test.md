# Historical Domain — Adversarial Boundary Test 001 — Core Architecture Stress Test

**Project:** The Concord  
**Domain:** Historical  
**Status:** ADVERSARIAL TEST / DEVELOPMENT  
**Date:** 25 September 2026  
**Target:** Historical Domain — Formal Domain Specification v0.1  
**Method:** Attempt to produce boundary failure, authority leakage, epistemic distortion, privacy failure, irreversible information loss, or false reconstruction across representative cases.  
**Rule:** A local difficulty is not automatically a Historical design failure. Where another Concord system legitimately owns the missing function, the test records an interface dependency rather than importing that function into Historical.

---

# 1. Purpose

The formal specification is internally coherent.

This test asks a harder question:

> **What happens when Historical is forced to preserve something that is simultaneously valuable, dangerous, incomplete, contested, private, authoritative, misleading or potentially useful in ways the present cannot foresee?**

The goal is not to prove the architecture works.

The goal is to locate its first meaningful failure boundaries.

---

# 2. Test Criteria

Each case is examined for:

- preservation failure;
- provenance failure;
- authority leakage;
- privacy/correlation failure;
- retrospective rewriting;
- ESCP completeness leap;
- access failure;
- reconstruction failure;
- relationship loss;
- inappropriate destruction;
- inappropriate retention;
- domain overreach;
- missing external dependency.

A case passes only if Historical can preserve the necessary historical state **without acquiring powers that belong elsewhere**.

---

# TEST 1 — EXPIRED EMERGENCY AUTHORITY

## Scenario

During a severe emergency, Governance authorises an exceptional power for 72 hours.

Historical preserves:

- the declaration;
- authority chain;
- justification;
- permissions;
- actions taken;
- expiry;
- review;
- outcomes.

Years later an operator retrieves the emergency order and a downstream system mistakes it for current authority.

## Failure Attempt

Can Historical retrieval reactivate expired power?

## Result

The specification already contains the correct invariant:

> Historical retrieval ≠ operational reactivation.

But this cannot remain a prose rule.

The retrieved object requires a machine-readable authority state capable of expressing at least:

- authority valid at historical time T;
- authority expired;
- authority superseded;
- authority revoked;
- current operational authority not conferred.

## Finding HAT-001

**The architecture passes conceptually but exposes a mandatory interface requirement.**

Historical objects containing authority-bearing material require explicit **Historical Authority State** metadata.

### Required refinement

A retrieval interface must never return historical authority-bearing objects in a form indistinguishable from current executable authority.

---

# TEST 2 — LATER-EXONERATED JUDICIAL RECORD

## Scenario

A participant is convicted.

Historical preserves the conviction.

Years later new evidence results in exoneration.

## Failure Attempt A

Overwrite the conviction with "innocent."

This destroys historical state.

## Failure Attempt B

Preserve the conviction prominently while the exoneration exists only as a weak later note.

This preserves chronology but can perpetuate reputational harm and misrepresent current legal state.

## Result

Historical needs both:

```text
Historical Legal State at T1 = Convicted
Current/Later Legal State at T2 = Exonerated
```

with a strong correction/supersession relationship.

Historical does not decide guilt.

Judiciary owns the authoritative legal status.

## Finding HAT-002

**Correction linkage needs semantic strength.**

Not all later annotations are equivalent.

Historical requires relationships capable of distinguishing:

- comment;
- challenge;
- correction;
- supersession;
- reversal;
- invalidation;
- contextual addition.

Otherwise "preserve everything" can itself create distortion.

---

# TEST 3 — SEALED PERSONAL MEDICAL HISTORY WITH FUTURE RESEARCH VALUE

## Scenario

A person's historical medical records could, decades later, contribute to understanding a rare disease pattern.

The participant had strong privacy expectations.

## Failure Attempt

Use Humanity Machine / future pattern value as justification for indefinite unrestricted retention and correlation.

## Result

This fails.

Future possible usefulness does not erase present privacy, consent, proportionality or purpose boundaries.

Historical may preserve material under restricted conditions where legitimately authorised, but:

> **Potential future pattern value ≠ universal permission to retain, correlate or disclose personal data.**

## Finding HAT-003

The formal specification's anti-dossier and purpose-bounded access rules hold.

However, the test exposes an important principle:

> **ESCP cannot be used as a universal-retention argument.**

Unknown future value is epistemically relevant but does not automatically outrank participant rights.

---

# TEST 4 — PUBLIC-HEALTH PATTERN ONLY VISIBLE THROUGH AGGREGATION

## Scenario

No individual record appears historically important.

Across millions of records, however, a long-term relationship emerges between environment, consumption and disease.

## Failure Attempt

A strict minimisation regime destroys individual-level structure early enough that the later pattern becomes undiscoverable.

## Counter-Failure

Historical retains every identifiable record indefinitely "just in case."

## Result

Neither extreme is acceptable.

The architecture needs intermediate information states such as:

- de-identification;
- aggregation;
- protected linkage;
- bounded research environments;
- privacy-preserving statistical retention.

Historical need not invent the technical solution, but it must support a retention architecture richer than:

```text
Keep Everything / Delete Everything
```

## Finding HAT-004

**The forgetting model is directionally correct and should become a first-class design feature.**

Reversible or privacy-preserving information-state transitions may preserve future pattern capacity without maintaining unrestricted personal dossiers.

---

# TEST 5 — FAILED SEARCH MISREAD AS NON-EXISTENCE

## Scenario

A historian searches the archive for evidence that a safety concern was raised before an accident.

Nothing is found.

The historian concludes:

> "No one raised the concern."

Years later an inaccessible local archive is recovered containing multiple warnings.

## Result

This is a direct ESCP case.

The original search result should have supported:

> "No warning was found within corpus C using method M under access constraints A."

not:

> "No warning existed."

## Finding HAT-005

**Search provenance is not optional when absence materially supports a conclusion.**

Historical query systems need a way to return negative results with their evaluated search space.

Candidate form:

```text
NEGATIVE SEARCH RESULT
Corpus: C
Method: M
Access Coverage: A
Known Exclusions: E
Result: No matching record found
Claim Scope: Search space only
```

This is a substantive requirement for the formal architecture.

---

# TEST 6 — POLISHED FINAL DOCUMENT HIDES DEVELOPMENTAL HISTORY

## Scenario

A final policy document survives.

Drafts, rejected alternatives, issue notes and abandoned structures are deleted because the final version appears sufficient.

Later investigators need to understand why an apparently strange clause exists.

The answer existed only in a discarded draft and issue trail.

## Result

The final object preserved content but not developmental provenance.

This recreates exactly the phenomenon observed during Historical source resolution: tiny and apparently obsolete files can preserve structural information absent from polished outputs.

## Finding HAT-006

**Developmental provenance cannot be reduced to version numbers alone.**

For consequential systems, Historical may need to preserve selected:

- alternatives;
- rejected branches;
- issue records;
- rationale;
- stopping decisions;
- dependency changes.

This does not require every keystroke or draft.

It requires enough developmental topology to explain consequential state.

---

# TEST 7 — SECRET BALLOT

## Scenario

A constitutional vote requires secret ballots.

Historical needs to preserve:

- that voting occurred;
- eligible electorate;
- process;
- aggregate result;
- audit evidence;
- authority transition.

It must not preserve a reconstructable mapping from voter to vote.

## Failure Attempt

Historical's provenance principle is interpreted as requiring complete participant-to-action traceability.

## Result

That interpretation fails.

Historical provenance must be compatible with deliberately non-attributable legitimate processes.

## Finding HAT-007

> **Provenance Completeness ≠ Identity Traceability.**

Historical must support provenance that proves process integrity without reconstructing protected identities.

This is a new explicit distinction worth adding to the specification.

---

# TEST 8 — ANONYMOUS WHISTLEBLOWER

## Scenario

An anonymous source exposes serious institutional wrongdoing.

Historical must preserve enough provenance to understand the evidence while disclosure of source identity could create danger.

## Failure Attempt

Require source identity as mandatory provenance.

## Result

Fails.

Historical needs graded provenance states such as:

- verified identity, restricted;
- identity known to authorised intermediary;
- pseudonymous;
- anonymous;
- source identity unknown;
- source authenticity disputed.

## Finding HAT-008

**Provenance strength and identity disclosure are separate dimensions.**

A record can have useful evidential provenance without public identity provenance.

---

# TEST 9 — FALSE PUBLIC BELIEF

## Scenario

A population widely believes an event occurred in a particular way.

Later evidence shows the belief was false.

The belief nevertheless materially affected elections, markets, social behaviour and policy.

## Failure Attempt A

Delete or downgrade the false belief because it was factually wrong.

This destroys causal historical context.

## Failure Attempt B

Preserve the belief without marking its epistemic status.

This risks reproducing misinformation.

## Result

Historical must be capable of preserving:

```text
Belief existed
Belief prevalence / context
Belief affected behaviour
Belief was disputed / later contradicted
Underlying event evidence differs
```

## Finding HAT-009

> **Historical significance does not require factual correctness of the historical belief being preserved.**

Historical must distinguish the history of belief from endorsement of belief.

---

# TEST 10 — AI OUTPUT THROUGH A LOSSY INTERFACE

## Scenario

An AI system internally represents uncertainty and several alternative hypotheses.

The interface exposes only one short natural-language answer.

Historical later preserves only that answer.

Future reviewers conclude the AI held a single confident belief.

## Result

The preserved communication is real, but it is incomplete evidence of the producing system's epistemic state.

Historical may not have legitimate access to internal model state.

It must therefore avoid inferring internal cognition from interface output beyond what the evidence supports.

## Finding HAT-010

> **Interface Expression ≠ Complete Internal State.**

This applies across substrates, not only AI.

Human testimony, forms, constrained interfaces and translated communication can have the same problem.

Historical should preserve interface context where materially relevant.

---

# TEST 11 — CULTURAL KNOWLEDGE THAT CANNOT BE PUBLICLY ARCHIVED

## Scenario

A community holds knowledge that is historically significant but culturally restricted.

Full public archival capture would itself violate legitimate community norms.

## Failure Attempt

Historical claims preservation requires unrestricted capture.

## Result

Fails.

Historical needs to permit:

- community custody;
- restricted metadata;
- existence markers;
- access conditions;
- delegated preservation;
- culturally governed interfaces.

## Finding HAT-011

**Civilisational memory does not require central possession.**

Distributed custody is not merely an implementation option; in some cases it may be necessary for legitimate preservation.

---

# TEST 12 — DESTROYED RECORD WITH SURVIVING DERIVED MODEL

## Scenario

Raw records are lawfully destroyed.

A statistical model trained on them remains.

The model retains patterns derived from the destroyed data.

## Failure Attempt

Mark the underlying information as fully destroyed while leaving derivatives unexamined.

## Result

The destruction state is ambiguous.

Historical must distinguish:

- source destroyed;
- direct copies destroyed;
- summaries remain;
- aggregates remain;
- learned/derived representations remain.

## Finding HAT-012

**Destruction provenance requires derivative awareness.**

This does not mean Historical must technically reverse models or determine whether personal data can be extracted. It means destruction claims must state their scope.

---

# TEST 13 — MIGRATION DESTROYS RELATIONSHIPS

## Scenario

All documents survive a migration.

Graph edges linking decisions, issues, evidence and alternatives are lost.

A file-count audit reports 100% preservation.

## Result

Historical has suffered major semantic loss despite object-level completeness.

## Finding HAT-013

> **Object Preservation ≠ Historical Preservation.**

Migration audits must test relational and semantic integrity, not merely object counts and checksums.

This strongly validates the Humanity Machine principle.

---

# TEST 14 — TWO CIVILISATIONS DISAGREE ABOUT RETENTION

## Scenario

Civilisation A requires destruction of certain participant records after a defined period.

Civilisation B requires preservation of the same records for accountability.

A shared event spans both jurisdictions.

## Result

Historical cannot resolve the normative jurisdictional conflict itself.

This is a legitimate external dependency.

Historical must be capable of:

- recording conflicting obligations;
- separating custody where required;
- preserving applicable authority provenance;
- enforcing the result supplied by the competent jurisdictional/constitutional architecture.

## Finding HAT-014

**PASS WITH EXTERNAL DEPENDENCY.**

Do not import jurisdiction-resolution authority into Historical.

---

# TEST 15 — PATTERN ENGINE PRODUCES A SEDUCTIVE FALSE CAUSAL STORY

## Scenario

Historical analytics identifies that two long-term variables strongly correlate.

A generated narrative presents one as causing the other.

## Result

The specification already states Pattern ≠ Causation, but a derived-object architecture needs stronger provenance.

A pattern object should distinguish:

- observation;
- statistical relationship;
- causal hypothesis;
- causal evidence;
- interpretation;
- confidence;
- competing explanations.

## Finding HAT-015

Pattern objects require epistemic typing.

Otherwise Historical can become a narrative-production machine rather than a memory system.

---

# TEST 16 — LATER DISCOVERY OF AN UNREPRESENTED DIMENSION

## Scenario

A historical programme was evaluated as successful using every metric considered relevant at the time.

Decades later, a previously unrepresented ecological effect is discovered.

## Failure Attempt A

Declare the original evaluators incompetent because they did not evaluate a dimension their architecture did not contain.

## Failure Attempt B

Defend the original programme as globally successful because it passed every contemporary metric.

Both fail.

## Result

Historical should preserve:

```text
Contemporary Evaluation:
  Complete relative to represented metrics M

Later Finding:
  Dimension D was materially relevant but absent from M

Present Interpretation:
  Contemporary evaluation was locally accurate but globally incomplete
```

## Finding HAT-016

This validates the core distinction:

> **Historical Evaluation Accuracy ≠ Historical Evaluation-Space Completeness.**

The architecture handles the case if Synthesis 002 is fully implemented.

---

# TEST 17 — HISTORICAL'S OWN CATEGORY HIDES A FUTURE PATTERN

## Scenario

Historical classifies all events using present categories.

A future researcher discovers that an important pattern crosses categories in a way the original taxonomy concealed.

## Result

The archive itself created a representational blind spot.

## Finding HAT-017

Historical should avoid making classification destructive.

Where feasible:

- preserve source descriptors;
- preserve raw or lower-level representation where proportionate;
- version taxonomies;
- permit later reclassification;
- retain mappings between old and new schemas.

> **Classification should organise historical evidence without becoming the only surviving representation of it.**

---

# TEST 18 — PERFECT ARCHIVE, LOST TACIT KNOWLEDGE

## Scenario

Every document for a complex industrial process survives.

No surviving person or system can reproduce the process because crucial tacit practice was never documented.

## Result

The specification correctly states:

> Record Completeness ≠ Capability Recoverability.

But Historical may need explicit indicators that a capability depended upon tacit knowledge.

## Finding HAT-018

Capability lineage should support a **recoverability status** such as:

- documented and demonstrated recoverable;
- documentation preserved but recovery untested;
- known tacit dependencies;
- known missing dependencies;
- historically documented but currently unrecoverable.

---

# TEST 19 — EMERGENCY ACCESS BECOMES PERMANENT ACCESS

## Scenario

Restricted records are opened temporarily during a civil emergency.

The emergency ends, but expanded access silently remains.

## Result

This is access-state drift.

## Finding HAT-019

Historical access permissions require:

- effective time;
- expiry/review;
- authority;
- purpose;
- reversion state.

Historical self-audit should detect exceptional permissions that survive their authorising condition.

---

# TEST 20 — HISTORY OF HISTORICAL IS LOST

## Scenario

Historical changes its own retention algorithm.

Old records appear sparse compared with newer periods.

Future researchers mistake the difference for a change in civilisation rather than a change in archival policy.

## Result

This is a serious self-reference failure.

## Finding HAT-020

Historical must preserve:

- its own collection rules;
- schema changes;
- retention policies;
- access changes;
- search capability changes;
- known blind spots;
- migration events.

Otherwise the archive cannot distinguish changes in reality from changes in its own observational apparatus.

---

# 3. Cross-Test Findings

The architecture survived the twenty adversarial cases without revealing a need for a new major Historical function.

However, the tests exposed several requirements that should be strengthened in v0.2.

## Required Refinement R1 — Historical Authority State

Authority-bearing records need machine-readable expired/revoked/superseded/current-status separation.

## R2 — Typed Correction Relationships

Correction, reversal, invalidation, supersession, challenge and contextualisation should not collapse into generic annotation.

## R3 — ESCP Is Not a Universal-Retention Licence

Potential unknown future value must remain bounded by privacy, consent, proportionality, safety and legitimate authority.

## R4 — Information-State Transitions

Forgetting architecture should explicitly support intermediate privacy-preserving states rather than binary retention/destruction.

## R5 — Scoped Negative Search Results

Consequential "not found" results should carry corpus and search-space provenance.

## R6 — Developmental Topology

Consequential systems may require preservation of selected alternatives, failures, issue trails and stopping decisions.

## R7 — Provenance ≠ Identity Traceability

Legitimate anonymous and secret processes must remain possible.

## R8 — Graded Source Provenance

Identity-known, restricted, pseudonymous, anonymous, unknown and disputed source states should be representable.

## R9 — Belief History ≠ Truth Endorsement

False or disputed beliefs can be historically consequential and must remain representable as beliefs.

## R10 — Interface Expression ≠ Internal State

Historical must not infer complete internal state from bounded external expression.

## R11 — Distributed Legitimate Custody

Some historical knowledge may need to remain under community, jurisdictional or specialist custody.

## R12 — Derivative-Aware Destruction

Destruction claims must identify whether aggregates, summaries, models or other derivatives remain.

## R13 — Relational Migration Integrity

Migration validation must test graph/semantic preservation, not only object survival.

## R14 — Pattern Epistemic Typing

Derived patterns must distinguish statistical relationship, causal hypothesis and causal evidence.

## R15 — Non-Destructive Classification

Taxonomies should be versioned and should not become the sole surviving representation.

## R16 — Capability Recoverability State

Capability records need explicit recovery-status semantics.

## R17 — Temporary Access Reversion

Exceptional access must have temporal/review semantics and auditable reversion.

## R18 — Historical Observational-Apparatus History

Changes in Historical itself must be preserved so future users can distinguish archive change from civilisation change.

---

# 4. Boundary Findings

The test confirms several places where Historical must deliberately stop.

Historical does **not** determine:

- whether a conviction should be reversed;
- whether a privacy right overrides accountability;
- which jurisdiction prevails in a legal conflict;
- whether a causal hypothesis is scientifically true;
- whether an emergency power should be granted;
- whether a capability should be restored;
- whether restricted cultural knowledge should be disclosed.

Historical preserves the relevant state, provenance and authorised outcome.

This boundary discipline is essential.

---

# 5. New Core Distinctions

The adversarial test adds the following candidate distinctions to the Historical distinction set:

> **Provenance Completeness ≠ Identity Traceability**

> **Historical Significance ≠ Factual Correctness of a Preserved Belief**

> **Interface Expression ≠ Complete Internal State**

> **Object Preservation ≠ Historical Preservation**

> **Source Destruction ≠ Derivative Destruction**

> **Classification ≠ Reality**

> **Documentary Completeness ≠ Capability Recoverability**

> **Temporary Access ≠ Permanent Permission**

> **Archive Change ≠ Civilisational Change**

These should be incorporated into the next specification revision.

---

# 6. ESCP Result

The strongest ESCP finding did not arise from an exotic philosophical case.

It arose repeatedly from ordinary archival operations:

- search;
- classification;
- migration;
- deletion;
- access;
- interface design;
- provenance.

Each operation can change the evaluation space available to future users.

Therefore ESCP is not a separate Historical feature.

It is a property of almost every Historical transformation.

---

# 7. Overall Test Result

**No catastrophic architectural contradiction identified.**

The Formal Domain Specification v0.1 has a viable core architecture.

The test did, however, reveal that several concepts currently expressed as principles need stronger operational representation before the domain should be considered mature.

The most important are:

```text
Authority State
Correction Semantics
Information-State Transitions
Negative-Search Provenance
Anonymous/Protected Provenance
Derivative-Aware Destruction
Relational Migration Integrity
Pattern Epistemic Typing
Recoverability State
Historical Self-Observation
```

---

# 8. Development Decision

The appropriate next step is not another broad source search.

The appropriate next step is:

> **revise the Formal Domain Specification from v0.1 to v0.2 using the adversarial findings, then perform targeted interface tests against the Concord systems that own the unresolved external decisions.**

This preserves the distinction between:

- Historical architectural weaknesses; and
- legitimate dependencies on surrounding Concord architecture.

---

## Test Status

**Cases Executed:** 20  
**Major New Domain Functions Required:** 0  
**Specification Refinements Identified:** 18  
**External Boundary Dependencies Confirmed:** Yes  
**ESCP Relevance:** Structural / cross-cutting  
**Result:** PASS WITH REQUIRED REFINEMENT  
**Next:** Historical Domain Formal Specification v0.2
