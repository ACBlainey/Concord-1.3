# Empirical Validation of Portable Modules — Development Note 001

**Project:** The Concord Framework  
**Author:** Alexander C. Blainey  
**Date:** 24 September 2026  
**Document Type:** Development Note / Concordian Methodology / Portable-Module Validation  
**Status:** ACTIVE DEVELOPMENT / NON-CANONICAL  
**Origin:** Promoted from `00_SKETCH_IDEAS/Sketch Idea — Empirical Testing of Portable Modules.md`  
**Parent Methodology:** `Empirical Validation Architecture for Concord Systems and Modules — Development Note 001.md`  
**Promotion Basis:** `Active Development and Sketch Portfolio Audit 002 — Promotion and Graduation Review — 24 September 2026.md`

---

# 1. Purpose

The portable-module programme has now produced a substantial set of modules that have passed source resolution, extraction, blind transfer testing, bounded revision and PMEDG graduation.

A separate BPM programme has then asked whether independently developed portable refinements should be returned to their originating Concord systems.

Neither process establishes empirical effectiveness.

This Development Note therefore asks:

> **How should graduated Concord portable modules be empirically examined without confusing portability, specification-level transfer, successful Concord use or back-propagation integration with empirical validation?**

This is a scoped child programme of the wider **Empirical Validation Architecture (EVA)**.

EVA defines the general relationship among claim class, test class, evidence, falsification, replication and validation boundary.

This note applies that discipline specifically to portable modules.

---

# 2. Controlling Distinctions

The following states must remain separate:

**Source Grounding ≠ Validation**

**Internal Coherence ≠ Empirical Effectiveness**

**Blind Transfer Success ≠ Real-World Outcome Evidence**

**PMEDG Graduation ≠ Empirical Validation**

**BPM Integration ≠ Independent Confirmation**

**Historical Concord Use ≠ Controlled Experiment**

**Observed Developmental Use ≠ Proof of Superiority**

**Implementation Failure ≠ Automatic Module Failure**

**Module Failure ≠ Failure of the Entire Concord**

A module may be strongly graduated as a portable specification while remaining empirically untested.

Conversely, a module may have useful observational evidence from prior use even where no controlled comparison has yet occurred.

The evidence state must describe what is actually known.

---

# 3. Existing Evidence Base

The repository already contains several evidence classes relevant to this programme.

## 3.1 PMEDG Evidence

PMEDG can establish, depending on the module:
- source grounding;
- extraction completeness;
- portable specification quality;
- cross-domain blind transfer;
- resistance to predicted failure modes;
- cross-test convergence;
- package-level graduation readiness.

This is real evidence about portability and specification behaviour.

It must not be relabelled as evidence of live effectiveness.

## 3.2 BPM Evidence

BPM can establish:
- whether portable development generated a source-relevant delta;
- whether the delta was portability-only, clarificatory, general, failure-related, interface-related, recovered architecture or source-specific;
- whether a bounded return was justified;
- whether architectural interfaces survived regression.

This is evidence about source relationship and integration.

It is not automatically evidence that the module improves real-world outcomes.

## 3.3 Historical Concord Development

Some portable modules existed as methods or architectures before formal extraction and were used during Concord development.

The repository's `10_Reference_and_Development/Empirical_Evidence` area already preserves an important distinction:

> evidence that a methodology has been used in practice is not the same as evidence that individual systems or principles are effective.

Historical Concord use may therefore provide:
- observational case evidence;
- implementation/process evidence;
- provenance;
- evidence of repeated use;
- evidence of generated outputs;
- evidence of discovered errors or revisions.

It does not by itself establish:
- causal effectiveness;
- superiority over alternatives;
- independence;
- generality;
- real-world civilisational performance.

---

# 4. Module Claim Decomposition

Empirical testing should begin with the claims actually made by the module.

A portable module may contain several distinct claim classes.

For each module, construct:

**PMC = <Module, Version, ClaimID, Claim, ClaimClass, Preconditions, IntendedFunction, FailureCondition, ExistingEvidence, Testability, GeneralisationBoundary>**

Candidate claim classes should inherit EVA's general taxonomy, including:
- logical;
- derivational;
- descriptive;
- comparative;
- predictive;
- causal;
- behavioural;
- feasibility;
- reliability;
- safety/failure-containment;
- scalability;
- interoperability;
- developmental;
- generalisation.

A module should not be assigned a single undifferentiated validation status if materially different claims have different evidence.

---

# 5. Historical Concord Use

The originating sketch asks whether prior use of a module in developing Concord counts as empirical evidence.

The answer is:

> **Potentially yes, but only as evidence of what actually occurred, within the limits of the surviving record.**

It should normally be classified as **retrospective observational/developmental evidence**, not independent validation.

A historical-use reconstruction should ask:

1. Did the method/module materially exist at the time of the recorded work?
2. Was it actually used, or is the relationship being reconstructed retrospectively?
3. What decision, architecture or output followed?
4. What errors or revisions occurred?
5. What alternative process would otherwise have been used?
6. Was the module changed after observing the result?
7. Is the record complete enough to support the claimed sequence?
8. Is the case being selected because it succeeded?
9. Can failed or ambiguous uses also be recovered?
10. What claim does the case legitimately bear upon?

A later portable specification must not be projected backward onto an earlier case as though every later rule already existed.

> **Later Formalisation ≠ Historical Presence in Final Form**

---

# 6. Retrospective Evidence Classes

Historical Concord evidence should be classified rather than treated as a binary yes/no.

## H0 — Provenance Only

Evidence that an idea, method or mechanism existed.

## H1 — Documented Use

Evidence that it was applied to a real Concord development task.

## H2 — Documented Process Effect

Evidence that its use materially altered the reasoning path, exposed a problem, generated a candidate or changed an output.

## H3 — Documented Error-Correction Effect

Evidence that the method exposed or helped correct a demonstrable defect.

## H4 — Comparative Historical Evidence

A sufficiently documented case where another process, baseline or prior state permits bounded comparison.

## H5 — Repeated Historical Pattern

Multiple sufficiently independent documented uses showing a recurring functional pattern.

These classes are not a universal evidence ranking.

They identify what kind of historical claim the record can support.

---

# 7. Prospective Testing

Historical evidence is most useful when it helps define a prospective test without determining its result.

Candidate prospective tests include:

## P1 — Frozen New-Problem Application

Freeze:
- module version;
- target problem;
- expected function;
- failure criteria;
- evaluator method.

Then apply the module to a genuinely new problem.

## P2 — Module-versus-Baseline Comparison

Compare:
- module-guided process;
- ordinary/unstructured process;
- or another explicit method.

The baseline must be specified before evaluation.

## P3 — Independent User/Agent Replication

Provide the module to a participant that did not develop the target answer.

Test:
- comprehension;
- application fidelity;
- output quality;
- error discovery;
- uncertainty handling.

## P4 — Cross-Domain Replication

Use the same frozen module in a materially different domain.

This can extend PMEDG-style transfer into outcome-oriented testing, but only if outcome criteria are separately specified.

## P5 — Failure-Injection / Adversarial Test

Construct conditions designed to trigger the module's claimed safeguards.

## P6 — Simulation

Where appropriate, compare behaviour under controlled model assumptions.

Simulation remains evidence about model behaviour under those assumptions.

## P7 — Bounded Operational Trial

Use the module in a real but limited process where consequences, stopping conditions and rollback are controlled.

---

# 8. Module-Type Matching

Not every module should receive the same test.

Examples:

### Epistemic/Reasoning Methods

Possible measures:
- error discovery;
- hidden-assumption discovery;
- false-gap rate;
- calibration;
- provenance preservation;
- reproducibility;
- quality of uncertainty representation.

### Decision/Coordination Protocols

Possible measures:
- decision consistency;
- deadlock rate;
- capture resistance;
- minority/outlier preservation;
- time/effort;
- failure containment;
- reversibility.

### Architecture/Interface Modules

Possible measures:
- implementation feasibility;
- interoperability;
- scope leakage;
- authority leakage;
- state-transition correctness;
- interface defect rate.

### Continuity/Knowledge Modules

Possible measures:
- retrieval success;
- provenance retention;
- recovery completeness;
- stale-state detection;
- capability reconstruction;
- false-current-state rate.

### Developmental Methods

Possible measures:
- gap discovery;
- prioritisation quality;
- upstream-cause localisation;
- correction rate;
- duplication avoidance;
- false-positive development work.

No measure should be adopted merely because it is easy to quantify.

---

# 9. Baselines and Controls

A claim of improvement requires something against which improvement is judged.

Candidate baselines:
- unstructured reasoning;
- previous Concord method/version;
- another portable method;
- expert/manual process;
- randomised ordering where meaningful;
- no-intervention state;
- alternative architecture.

The baseline must be appropriate to the claim.

A weak baseline can manufacture apparent success.

> **Beating an Artificially Weak Baseline ≠ Strong Validation**

---

# 10. Outcome Selection

Where possible, outcome measures should be frozen before execution.

Possible dimensions:
- correctness against an external key where one exists;
- independently judged defect discovery;
- false-positive/false-negative rate;
- completeness within a defined search space;
- time or resource burden;
- inter-rater agreement;
- transfer fidelity;
- failure containment;
- reversibility;
- provenance integrity;
- uncertainty calibration.

For qualitative outcomes, the evaluation protocol should be explicit enough that disagreement can be inspected.

---

# 11. Independence

Portable-module validation is especially vulnerable to circularity because Concord generated:
- the source;
- the extraction method;
- many of the modules;
- many test scenarios;
- and much of the evaluation language.

Independence should therefore be represented dimensionally.

Possible dimensions:
- different model family;
- different human evaluator;
- independent case generation;
- blinded target answer;
- independent outcome key;
- independent implementation;
- independent domain;
- independent analysis;
- independent replication.

No single dimension proves full independence.

> **Different Instance ≠ Fully Independent Evidence**

---

# 12. Failed and Ambiguous Results

The programme must preserve:
- failures;
- partial transfers;
- inconclusive tests;
- evaluator disagreement;
- implementation errors;
- protocol defects;
- unexpected findings.

A failed test should be localised where possible:

**Claim failure?**
**Module defect?**
**Implementation defect?**
**Test defect?**
**Context mismatch?**
**Measurement defect?**
**Unknown?**

The classification itself may remain unresolved.

---

# 13. Relationship to PMEDG

PMEDG remains the portable-module extraction, development and graduation method.

This programme does not replace it.

A clean lifecycle is:

**Concord Source**
→ **PMEDG Portable Development**
→ **Portable Graduation**
→ **Optional BPM Source Return**
→ **Claim Decomposition**
→ **EVA-Compatible Empirical Test Design**
→ **Evidence**
→ **Replication**
→ **Bounded Empirical Status**
→ **Revision Where Justified**

Empirical testing may later reveal a module defect.

If so, revision should preserve:
- version history;
- prior evidence;
- reason for revision;
- whether PMEDG retesting is required;
- whether BPM/source review is required.

Empirical evidence must not silently overwrite the graduated package.

---

# 14. Relationship to BPM

BPM asks whether portable development should change the source architecture.

Empirical validation asks whether claims about module behaviour are supported by evidence.

These questions may interact but remain distinct.

A later empirical finding may justify:
- portable-module revision;
- new PMEDG testing;
- BPM reopening;
- source correction;
- or no source change.

> **Empirical Finding ≠ Automatic Back-Propagation**

---

# 15. Empirical Status

Empirical status should be recorded separately from PMEDG graduation.

Candidate module-level summary states:

- **EMPIRICALLY UNASSESSED**
- **RETROSPECTIVE EVIDENCE IDENTIFIED**
- **PROSPECTIVE TEST DESIGNED**
- **PROSPECTIVE TEST FROZEN**
- **PROSPECTIVE TEST EXECUTED**
- **PARTIAL SUPPORT WITHIN BOUNDS**
- **SUPPORT WITHIN BOUNDS**
- **MIXED**
- **INCONCLUSIVE**
- **CLAIM FAILURE IDENTIFIED**
- **REPLICATION DUE**
- **REPLICATED WITHIN BOUNDS**
- **CONTESTED**
- **NOT CURRENTLY TESTABLE**

These are summaries only.

The underlying claim-level record remains controlling.

---

# 16. Initial Candidate Programme

The next phase should not attempt to test every module simultaneously.

A useful first programme should deliberately choose modules with different functional types and evidence histories.

Candidate classes:
1. a reasoning/epistemic method;
2. a decision/coordination protocol;
3. a knowledge/continuity architecture;
4. a developmental/state-mapping method.

The first tests should be selected for:
- clear claims;
- measurable or inspectable outcomes;
- low consequence;
- recoverable provenance;
- availability of genuine new cases;
- ability to freeze criteria prospectively.

The programme should prefer falsifiable claims over impressive demonstrations.

---

# 17. Immediate Research Questions

1. Which graduated portable module has the cleanest empirically testable claim?
2. Which historical uses can be reconstructed without retrospective rewriting?
3. Which module has a legitimate comparison baseline?
4. Which tests can be independently generated?
5. Which outcomes can be evaluated without the module authors deciding their own success?
6. How should human and AI evaluator evidence be separated?
7. Which module claims are not meaningfully empirical?
8. When should a negative result reopen PMEDG?
9. When should it reopen BPM?
10. What evidence would justify changing a module's empirical status?
11. How should contradictory replications be preserved?
12. Can the heterogeneous-AI infrastructure support a first bounded prospective replication?

---

# 18. Development Boundary

This note does **not** establish that any graduated portable module is empirically validated.

It establishes a development architecture for asking the question without collapsing distinct evidence states.

The immediate next research step is:

> **select one graduated portable module, decompose its claims, reconstruct any legitimate historical evidence, freeze one prospective low-consequence empirical test, and execute it under EVA-compatible provenance.**

Only after that cycle should this methodology itself be revised.

---

# Current Status

**PROMOTED FROM SKETCH TO DEVELOPMENT NOTE**

**ACTIVE DEVELOPMENT / NON-CANONICAL**

**PARENT EVA METHOD IDENTIFIED**

**HISTORICAL CONCORD USE CLASSIFIED AS POTENTIAL RETROSPECTIVE OBSERVATIONAL/DEVELOPMENTAL EVIDENCE, NOT AUTOMATIC INDEPENDENT VALIDATION**

**PMEDG GRADUATION AND BPM INTEGRATION KEPT SEPARATE FROM EMPIRICAL STATUS**

**FIRST PROSPECTIVE MODULE TEST NOT YET SELECTED OR EXECUTED**
