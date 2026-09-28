# Portable Module Extraction, Development and Graduation Method — PMEDG v1.3

**Project:** The Concord  
**Location:** Portable Module Development Area  
**Status:** DEVELOPMENT OPERATING METHOD / PRESERVE ACROSS REPOSITORY VERSIONS  
**Version:** 1.3  
**Date:** September 2026

## 1. Purpose

This document defines the reusable method for identifying, extracting, developing, transfer-testing, graduating and archiving Concord portable modules.

It exists so that future Concord versions do not need to import the full development history of every successfully graduated module merely to reconstruct how portable-module development is performed.

The method is intended to travel forward with the active development architecture.

Completed module-development records may remain archived.

> **Preserve the method; archive the completed development history.**

This method consolidates the procedure already established through repeated portable-module development. It does not retroactively claim that every earlier module followed an identical document sequence. Where earlier practice varied, this document records the mature common procedure.

---

# 2. Relationship to Other Methods

PMEDG is the specific lifecycle method for portable modules.

It uses, but is not replaced by:

- **CRADP** — general recursive architectural diagnosis and development;
- **ESCP** — evaluation-space completeness discipline;
- source-resolution and provenance rules;
- frozen-prediction testing;
- independent transfer testing.

CRADP can diagnose and develop many kinds of architecture.

PMEDG answers the narrower question:

> **How does a candidate Concord mechanism become a defensible standalone portable module?**

---

# 3. Core Principles

## 3.1 Portability is not validation

> **Portability ≠ Canonicality ≠ Validation ≠ Independence of Origin.**

A mechanism can be portable while still experimental.

A graduated portable module has completed the stated portable-package development cycle. It has not thereby been proven universally correct.

## 3.2 Source before abstraction

Do not extract a module from a convenient summary while ignoring the wider source architecture.

> **Local Source ≠ Complete Source Space**

## 3.3 ESCP applies throughout

> **No Source Found ≠ Source Does Not Exist**

> **Not Represented in Candidate ≠ Not Present in Source Architecture**

> **Observed Portable Deficit ≠ Source Architecture Deficit**

Before treating an apparent omission as a source defect, expand the evaluation space and source-resolve it.

## 3.4 Preserve provenance

Record what the portable mechanism came from, what was removed, what was externalised and what was added during portable development.

Do not rewrite earlier predictions or test expectations after results are known.

## 3.5 Extract the mechanism, not the civilisation

A portable module should not require adoption of the Concord merely to function.

Concord-specific dependencies should be:

- removed where unnecessary;
- translated into generic concepts where legitimately portable;
- or exposed as explicit external interfaces.

## 3.6 Do not manufacture completeness

Graduation means the package has met its stated graduation conditions.

It does not mean:

- every possible source has been found;
- every domain has been tested;
- every dependency is known;
- every implementation is correct;
- empirical validation is complete;
- future revision is unnecessary.

---

# 4. Development Entry Routes and Candidate Levels

Portable modules may legitimately enter PMEDG through **two development routes**.

The routes describe where portability is recognised. They do not create different graduation standards.

> **Different Development Route != Different Evidence Standard**

## 4.1 Route A — Candidate-First Portable Development

Use this route when a mechanism is recognised as a portable-module candidate before substantial standalone development begins.

The candidate should be registered in the portable-module development queue and organised by candidate level.

A dedicated candidate folder should be created early so source resolution, specifications, tests, independent responses and graduation evidence accumulate in one bounded development space.

This is the preferred route when portability is already the explicit development objective.

## 4.2 Route B — Research-First Emergent Portability

Use this route when architecture begins as ordinary research or active development and only later demonstrates a reusable portable kernel.

Typical path:

> **Research / Active Development → Architecture Matures → Portability Recognised → PMEDG Candidacy Assessment → Formal Source Resolution and Extraction Audit → Common PMEDG Pipeline**

Research-first work must not be retrospectively rewritten to look candidate-first.

When portability is recognised:

1. identify the complete development file family relevant to the candidate;
2. record the research location and provenance boundary;
3. perform a formal PMEDG candidacy assessment;
4. source-resolve the candidate against neighbouring and pre-existing architecture;
5. identify which pre-PMEDG tests count as development evidence and which do not substitute for formal PMEDG transfer tests;
6. create the standalone portable specification only after the extraction boundary is defensible;
7. proceed through the same frozen blind-testing, convergence, graduation and release standards as Route A.

> **Research Evidence Can Support PMEDG; It Does Not Automatically Satisfy PMEDG.**

A research-first candidate may already have extensive adversarial or cross-domain evidence. Preserve it as pre-PMEDG evidence. Do not rename it as formal PMEDG evidence after the fact.

## 4.3 Route convergence

Both routes converge no later than formal Source-Space Resolution and Extraction Audit.

After convergence, the same requirements apply for:

- portable specification;
- frozen blind tests;
- independent responses;
- post-test evaluation;
- bounded revision;
- cross-test convergence;
- graduation candidacy;
- graduation review;
- v1.0 release;
- plain-language interface;
- completed archive.

Neither route may bypass source resolution, owner/dependency boundaries, ESCP discipline or transfer evidence merely because substantial prior work exists.

## 4.4 Repository organisation

Candidate-first work should use a dedicated portable-module development folder where the current repository provides one.

Research-first work may originate under:

`02_Domains/03_Research/Active_Development/`

Once a research-first module graduates, its complete module-specific development family should be removed from the shared active-development root **only after two-phase archive verification** and preserved under:

`02_Domains/03_Research/Development_Archive/Portable_Modules/<Module_Name>/`

A research-first archive should normally separate:

- `01_Research_Development/`
- `02_Source_Resolution/`
- `03_Pre_PMEDG_Testing/`
- `04_Formal_PMEDG/`
- `05_Independent_Evaluator_Responses/`

This structure preserves the actual route into portability rather than manufacturing a candidate-first history.

If the research-first files share a directory with unrelated active research, archive and remove **only the explicitly manifested module file family**. Never empty or delete the shared research directory.

> **Shared Development Directory != Candidate Folder**

Candidate levels are organisational development states, not quality rankings.

## Level A — Complete Portable Protocols

Already substantially self-contained and close to portable form.

## Level B — Extractable Architectures

Coherent reusable architectures whose portable core must be separated from Concord-specific dependencies.

## Level C — Embedded Primitives and Mechanisms

Smaller mechanisms embedded inside larger architectures. They may become standalone modules or combine with other mechanisms.

A candidate remains active until graduation or an explicit hold/rejection decision.

---

# 5. Lifecycle Overview

The standard lifecycle is:

> **Candidate Identification → Source-Space Resolution → Extraction Audit → Portable Specification v0.1 → Frozen Blind Transfer Test 001 → Independent Response → Post-Test Evaluation → Bounded Revision → Portable Specification v0.2 → Blind Transfer Test 002 → Cross-Test Convergence → Graduation-Candidate v0.3 → Graduation Review → v1.0 Release → Plain-Language Interface → Completed Archive**

This is the default path, not an inflexible requirement to manufacture document versions.

If evidence requires another test or revision, add it.

If a candidate fails fundamentally, do not force it through the sequence.

---

# 6. Stage 1 — Candidate Identification

Create or maintain a candidate folder containing at least a README.

Record:

- candidate name;
- development level;
- candidate function;
- why portability appears plausible;
- primary known source;
- current status;
- known boundaries.

Initial status should not imply completion.

Example:

> **CANDIDATE PORTABLE MODULE / DEVELOPMENT PLACEHOLDER**

The candidate README is an inventory and routing record, not a portable specification.

---

# 7. Stage 2 — Source-Space Resolution

Before abstraction, resolve the relevant source family.

Search:

1. the named primary source;
2. neighbouring documents in the source domain;
3. later upgrades or companions;
4. active-development material;
5. earlier repository versions where relevant;
6. completed or overlapping portable modules;
7. dependency/state records where relevant;
8. provenance/history when needed to distinguish origin from later development.

The purpose is not to read the entire Concord indiscriminately.

The purpose is to close the evaluation space sufficiently for the extraction decision.

Record the search scope.

Possible findings include:

- one source is sufficient;
- multiple sources form the architecture;
- later work materially changes the candidate;
- part of the source has already become another portable module;
- the candidate is actually several separable mechanisms;
- the proposed module is not independently portable;
- source resolution remains insufficient.

Do not silently merge overlapping modules.

---

# 8. Stage 3 — Source Resolution and Extraction Audit

Create:

> **Source Resolution and Extraction Audit 001**

The audit should establish:

## 8.1 Source set

Identify the material sources actually used.

## 8.2 Source architecture

Describe the mechanism as it exists before portability abstraction.

## 8.3 Portable problem

State the general problem the candidate solves without Concord-specific framing.

## 8.4 Candidate kernel

State the smallest mechanism that appears to survive abstraction.

## 8.5 Concord-specific dependencies

For each dependency decide whether it is:

- essential and portable;
- removable;
- replaceable by a generic interface;
- already owned by another portable module;
- or unresolved.

## 8.6 Overlap boundary

Explicitly distinguish neighbouring modules.

Do not duplicate an already-extracted mechanism merely because it appears in the source architecture.

## 8.7 Inputs, outputs and interfaces

Identify the minimum external information or services the module requires.

## 8.8 Failure modes and epistemic boundaries

Preserve source uncertainty and known failure conditions.

## 8.9 Extraction decision

Use a clear result such as:

> **SOURCE RESOLUTION SUFFICIENT FOR PORTABLE EXTRACTION**

or:

> **HOLD — SOURCE RESOLUTION INSUFFICIENT**

Only proceed when the extraction space is sufficiently resolved.

---

# 9. Stage 4 — Portable Specification v0.1

Create the first standalone specification.

v0.1 should be understandable without requiring the reader to know the Concord.

Where applicable define:

- purpose;
- portable problem;
- core principle/invariant;
- terminology;
- inputs;
- outputs;
- states/classifications;
- process or algorithm;
- interfaces;
- stopping conditions;
- uncertainty handling;
- authority boundaries;
- security/privacy boundaries;
- failure modes;
- implementation minimum;
- worked examples;
- falsification/failure criteria;
- validation status.

The specification should distinguish:

> **Mechanism**

from:

> **Host decision**

and:

> **Observation**

from:

> **Authority**

where those distinctions are relevant.

Do not claim transfer merely because the abstraction appears coherent.

---

# 10. Stage 5 — Freeze Blind Transfer Test 001

Before obtaining an independent response, create two separate records.

## 10.1 Test Brief

The brief gives a clean evaluator:

- the portable specification;
- a materially non-Concord scenario;
- relevant facts;
- required analysis/output;
- transfer-class definitions where used.

Do not provide expected answers.

## 10.2 Expected Findings and Evaluation Key

Freeze the expected findings before seeing the independent response.

Predictions should be sufficiently specific to reveal whether the module actually transfers.

Where practical, use numbered predictions.

The hidden key must not be supplied to the clean evaluator.

> **Prediction must precede observation.**

---

# 11. Stage 6 — Independent Transfer Response

Obtain a response from an evaluator that has not been given:

- the hidden expected-findings key;
- the desired result;
- previous evaluator conclusions;
- unnecessary Concord source architecture.

The evaluator should work from the portable specification and frozen scenario.

Preserve the independent response as part of the development record.

Do not rewrite it to make it agree with the expected result.

---

# 12. Stage 7 — Post-Test Evaluation

Compare the independent response against the frozen key.

For each prediction record:

- confirmed;
- partially confirmed;
- contradicted;
- not tested;
- ambiguous.

Then assess:

- whether the core mechanism transferred;
- whether Concord-specific assumptions leaked through;
- whether the evaluator required hidden context;
- whether safeguards survived;
- what ambiguities were exposed;
- whether any failure is fundamental or bounded.

A useful transfer scale may distinguish:

- failure/no meaningful transfer;
- partial transfer;
- functional transfer;
- strong transfer.

The label matters less than the recorded evidence.

Do not change the frozen key after the response.

---

# 13. Stage 8 — Bounded Revision

If the first test reveals bounded specification problems, create the next specification version.

Apply only findings justified by the test and source architecture.

Do not use a successful test as permission for unrelated feature expansion.

Record the delta.

A bounded revision may clarify:

- terminology;
- scope;
- state representation;
- interfaces;
- uncertainty;
- stopping;
- examples;
- failure handling;
- host/module boundaries.

If the test reveals a fundamental failure, return to source resolution or reconsider whether the candidate should exist as a standalone module.

---

# 14. Stage 9 — Blind Transfer Test 002

The second test should use a **materially different non-Concord domain**.

Its purpose is not merely repetition.

It should pressure:

1. the unchanged core mechanism;
2. the bounded clarifications introduced after Test 001;
3. different objects, relationships or consequences;
4. known failure modes;
5. independence from Concord-specific terminology.

Again freeze the brief and hidden expected-findings key before the independent response.

---

# 15. Stage 10 — Cross-Test Convergence

After Test 002, compare the tests.

Ask:

- Did the same core mechanism survive both domains?
- Did the first test's clarifications work in the second?
- Did independent evaluators preserve the same boundaries?
- Did a new domain expose a fundamental missing primitive?
- Are remaining issues bounded implementation/interface matters?
- Did transfer improve, remain stable or deteriorate?

Count frozen predictions where appropriate, but do not treat a numerical total as sufficient by itself.

> **Prediction Count ≠ Architectural Validity**

The important question is whether the same portable architecture survived materially different transfer conditions.

---

# 16. Stage 11 — Decide Whether Another Test Is Required

A third blind test is **not automatically required**.

Add another test when:

- a revision introduces a materially new mechanism;
- the second test exposes unresolved transfer risk;
- convergence is weak or contradictory;
- a critical boundary has not actually been exercised;
- apparent success may depend on domain similarity;
- graduation review identifies insufficient evidence.

Do not add tests merely to create a larger number.

---

# 17. Stage 12 — Graduation-Candidate Specification

When the mechanism has survived sufficient transfer testing, create a graduation-candidate version.

The candidate should incorporate only justified bounded revisions.

Typical metadata:

> **GRADUATION-CANDIDATE SPECIFICATION / NOT YET RELEASED**

Recheck:

- source provenance;
- standalone legibility;
- overlap with other modules;
- external interfaces;
- authority boundaries;
- epistemic claims;
- security/privacy;
- failure modes;
- test evidence;
- validation wording.

---

# 18. Stage 13 — Portable-Package Graduation Review

Create a formal graduation review.

At minimum test:

## Source grounding
Is the module traceable to resolved source architecture?

## Standalone legibility
Can it be understood without hidden Concord context?

## Mechanism stability
Did the core survive development and testing without being replaced?

## Boundary integrity
Are neighbouring modules and host responsibilities separated?

## ESCP discipline
Does the package avoid treating incomplete representation as completeness?

## Transfer evidence
Did independent non-Concord tests materially support portability?

## Failure handling
Are important failure modes explicit?

## Authority discipline
Does the module avoid manufacturing authority from measurement, dependency, capability, criticality or convenience?

## External interfaces
Are legitimate host dependencies explicit rather than hidden?

## Epistemic boundaries
Does the release claim only what the evidence supports?

## Further-test requirement
Would another test materially reduce unresolved transfer uncertainty?

Possible decisions:

- PASS — release authorised;
- PASS WITH REQUIRED BOUNDED REVISION;
- HOLD — more evidence/development required;
- FAIL — candidate not currently suitable for graduation.

---

# 19. Stage 14 — v1.0 Release

On PASS, create the standalone file in:

`06_Portable_Modules/`

Recommended metadata:

> **Version: 1.0**

> **Status: GRADUATED PORTABLE MODULE / SPECIFICATION-LEVEL TRANSFER VALIDATED**

The release should preserve the graduation candidate's substantive architecture except for release metadata and any explicitly required graduation correction.

Graduation at specification level means:

- source extraction completed to the stated search boundary;
- standalone package produced;
- independent transfer demonstrated to the stated level;
- known boundaries preserved;
- no identified release blocker remains.

It does not mean universal empirical validation.

---

# 20. Stage 15 — Plain-Language Interface

Add the graduated module to the plain-language guide.

The guide should normally include:

- plain-English name;
- what it does;
- simple example;
- possible application domains;
- when to use it;
- what it does not do;
- formal-module name;
- comparison question distinguishing it from neighbouring modules.

The guide is an interface layer.

It is not the authoritative specification.

---

# 21. Stage 16 — Archive Development Record

After release, archive the complete development record according to its entry route.

**Route A — candidate-first:** move the candidate's complete dedicated development folder to the repository's completed portable-development archive, preserving its original level and module identity.

**Route B — research-first:** create or use:

`02_Domains/03_Research/Development_Archive/Portable_Modules/<Module_Name>/`

and preserve the explicitly manifested module file family using the research/source-resolution/pre-PMEDG/formal-PMEDG/evaluator-response structure defined in section 4.4.

Do not move unrelated files merely because they share the research directory.

Preserve:

- original candidate README/registration file, even when it contains only queue metadata or a placeholder summary;
- source-resolution audit;
- every specification version;
- frozen test briefs;
- hidden evaluation keys;
- independent responses;
- post-test evaluations;
- graduation review;
- other material development records.

Do not delete the development history.

Then verify explicitly:

1. every expected artifact exists in the completed archive;
2. for Route A, the original candidate README/registration file is included;
3. for Route B, the manifest records the complete module-specific research file family and its original paths;
4. independent evaluator responses are preserved where available;
5. every corresponding module-specific active-development copy is absent after verified archival;
6. unrelated files in a shared research directory remain untouched;
7. the v1.0 release exists in the main portable-module folder;
8. the plain-language guide entry exists.

Git repositories do not preserve empty directories, so the active candidate folder should disappear when its final file is removed.

---

# 22. Archive and Repository-Version Transition Rule

Completed development records are historical evidence, not mandatory active-development inputs.

When advancing to a future repository version, such as V1.3:

### Carry forward
- this PMEDG method;
- the active candidate queue;
- supporting methods needed by PMEDG, including ESCP and relevant source-resolution rules;
- current graduated v1.0 portable modules;
- the plain-language guide or successor index;
- unresolved development records still needed for active candidates.

### May remain archived
- completed candidate working folders;
- superseded draft specifications;
- old blind-test working material;
- historical graduation records, provided they remain retrievable through the archive/provenance system.

Therefore:

> **Future development should depend on the method, not on reconstructing the method from archived module histories.**

The archive remains available for audit, provenance, replication and later methodological research.

---

# 23. Change Control for PMEDG

PMEDG itself may evolve.

When portable-module development exposes a methodological defect:

1. record the defect;
2. distinguish one-module exception from general method failure;
3. propose the smallest method change;
4. test it on subsequent module development;
5. preserve the earlier method version;
6. do not rewrite historical module records to imply they followed later rules.

> **Method Improvement ≠ Historical Revision**

### 23.1 Unpredicted Blind-Test Findings

Blind transfer tests may expose useful findings that were not anticipated in the frozen expected-findings key.

These findings must be preserved, but they must not be inserted retrospectively into the scored prediction set.

After each blind test:

1. score only predictions frozen before the independent response;
2. record materially useful unpredicted findings in a separate section;
3. distinguish unpredicted specification/interface findings from fundamental mechanism failures;
4. permit such findings to justify bounded revision when supported by the response;
5. never alter the original frozen prediction denominator or claim that an unpredicted finding was predicted.

> **New Finding ≠ Retrospective Prediction**

This rule was added after the same methodological issue appeared independently during KCS BTT-001 and KCS BTT-002.

Major changes should increment the PMEDG version.

### 23.2 Blind-Test Finding Classes

For post-test evaluation, distinguish:

1. **Predicted finding** — the frozen key materially anticipated the finding.
2. **Predicted pressure with novel detail** — the key correctly anticipated the area/mechanism under pressure, while the evaluator exposed a specific defect or refinement not itself predicted.
3. **Wholly unpredicted finding** — neither the finding nor its material pressure area was anticipated by the frozen key.

Only frozen predictions contribute to the prediction score. Novel detail and wholly unpredicted findings are preserved separately and may justify bounded revision.

This distinction prevents both under-crediting a correctly predicted pressure and overclaiming that an unanticipated detail was predicted.

### 23.3 Graduation-Candidate Consistency Check

Before formal Graduation Review, perform a mechanical consistency check across the candidate:

- filename;
- document title;
- version number;
- status metadata;
- source-module name;
- referenced specification versions;
- referenced test numbers/results;
- claimed prediction/failure totals.

A mismatch must be corrected before the Graduation Review decision.

> **Substantive Convergence ≠ Metadata Consistency**

### 23.4 Archive Manifest and Two-Phase Verification

Before archiving a graduated development record:

0. identify the entry route. For Route A, the archive boundary is normally the entire dedicated candidate folder. For Route B, the archive boundary is the explicitly identified module file family within the shared research space.
1. enumerate the **entire archive boundary**, not only files created during formal PMEDG stages;
2. create an expected-artifact manifest that includes every active file intended for preservation or explicit disposal, including the original README/registration/placeholder file;
3. verify every expected active artifact exists;
4. copy/move the complete preservation set into the completed archive;
5. verify every preservation-manifest item exists in the archive;
6. only then remove the active copies inside the verified archive boundary; for Route A this normally means all files remaining in the candidate folder, while for Route B it means only the manifested module-specific files;
7. verify a Route A candidate folder no longer resolves as a live queue item, or for Route B verify that no manifested module-specific file remains loose in the shared active-development root;
8. verify the v1.0 release and plain-language interface exist.

If an active file is intentionally not preserved, the manifest must record that disposal decision explicitly before deletion. An unlisted leftover file is an archive failure, not a harmless placeholder.

If archive verification fails, do not treat the candidate as cleanly archived.

> **Archive Intent ≠ Archive Completion**

> **Manifested Development Files ≠ Entire Active Candidate Folder**

> **Research-First Module Files ≠ Entire Shared Research Directory**

This clarification was added after STRA graduation correctly archived all 14 manifested development artifacts but left the original candidate README in the active Level B folder, causing the graduated candidate to remain visibly present in the active queue.



# 24. Minimum Development Record

A normally graduated module should leave enough evidence to reconstruct:

1. why it was considered portable;
2. what source space was searched;
3. what architecture was extracted;
4. what Concord-specific dependencies were removed/externalised;
5. what v0.1 claimed;
6. what Test 001 predicted;
7. what the independent evaluator found;
8. what changed afterward;
9. what Test 002 predicted;
10. whether the second domain confirmed the mechanism;
11. why further testing was or was not required;
12. why graduation was authorised;
13. what v1.0 claims;
14. where the development record was archived.

The exact number of files is not normative.

The evidential functions are.

---

# 25. Compact Algorithm

```
INPUT: Concord corpus C, candidate M

1. RegisterCandidate(M)
2. sources <- ResolveSourceSpace(M, C)
3. if sources insufficient: HOLD
4. audit <- ExtractPortableKernel(M, sources)
5. if no coherent portable kernel: STOP / RECLASSIFY
6. spec1 <- BuildStandaloneSpecification(audit)
7. Freeze(Test1, Key1)
8. response1 <- IndependentTransfer(Test1, spec1)
9. eval1 <- Compare(response1, Key1)
10. if fundamental failure: return to source resolution/reclassification
11. spec2 <- ApplyBoundedFindings(spec1, eval1)
12. Freeze(Test2, Key2) using materially different domain
13. response2 <- IndependentTransfer(Test2, spec2)
14. eval2 <- Compare(response2, Key2)
15. convergence <- CompareTests(eval1, eval2)
16. if unresolved material transfer risk: add test/revise
17. candidate <- BuildGraduationCandidate(convergence)
18. VerifyCandidateMetadata(candidate)
19. decision <- GraduationReview(candidate, evidence)
20. if decision != PASS: route required work
21. release <- PublishV1(candidate)
22. UpdatePlainLanguageGuide(release)
23. active_set <- EnumerateEntireActiveCandidateFolder(M)
24. manifest <- BuildArchiveManifest(M, active_set)
25. ArchiveDevelopmentRecord(M, manifest)
26. VerifyArchiveAgainstManifest(manifest)
27. RemoveAllRemainingActiveCandidateFiles(active_set, manifest)
28. VerifyActiveCandidateFolderAbsent()
29. VerifyReleaseAndGuide()
OUTPUT: graduated portable module + preserved development evidence
```

---

# 26. Handover Test

A fresh future instance should be able to receive:

- PMEDG;
- access to the current Concord corpus;
- ESCP;
- the active portable-module candidate queue;
- the supporting source-resolution tools/methods;

and continue extracting a new candidate **without reading the completed development histories of previous modules merely to discover the procedure**.

Previous module histories may still be consulted as examples or evidence, but they are not the method.

If a future instance cannot do this, PMEDG is incomplete.

---

# 27. Final Constraint

Portable-module development exists to discover and expose reusable mechanisms, not to generate modules for their own sake.

A valid outcome may be:

- graduate;
- merge;
- split;
- reclassify;
- hold;
- reject portability;
- discover that another module already owns the function.

The method should therefore optimise for faithful extraction and defensible transfer, not graduation count.

> **Candidate ≠ Module**

> **Successful Extraction ≠ Universal Validation**

> **Graduation ≠ Finality**

> **Archive the evidence; preserve the method; carry forward the reusable result.**
