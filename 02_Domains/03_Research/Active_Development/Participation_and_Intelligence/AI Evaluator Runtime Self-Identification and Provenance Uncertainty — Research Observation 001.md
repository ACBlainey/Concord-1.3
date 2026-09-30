# AI Evaluator Runtime Self-Identification and Provenance Uncertainty — Research Observation 001

**Project:** The Concord  
**Status:** PRESERVED OBSERVATION / LOW-PRIORITY RESEARCH CANDIDATE / NOT CANONICAL  
**Date:** 30 September 2026  
**Origin:** CRADP AI Bootstrap blind testing

---

## 1. Observation

During CRADP Blind Cross-Instance Test 002, the evaluator generated the self-identification:

> **Evaluator/model if known: Claude (Anthropic)**

The test operator reports that both Test 001 and Test 002 were actually performed using **DeepSeek in DeepThink mode**.

The original evaluator output is preserved unchanged.

Therefore the directly supported observation is:

> **An AI evaluator generated an incorrect account of its own runtime/model identity.**

This does not establish why the error occurred.

---

## 2. Immediate Provenance Invariant

> **Evaluator Self-Identification != Verified Runtime Provenance**

Where model/runtime identity matters to an experiment, externally recorded execution metadata should take precedence over generated self-description.

Generated self-identification remains evidence about the evaluator's represented self-model, but should not automatically be treated as evidence about the underlying runtime.

---

## 3. Relationship to Existing Concord Work

The observation is directly relevant to the AI Bootstrap's epistemic self-stewardship and ESCP work.

It provides a concrete example of:

> **Self-Model != Complete System Model**

and:

> **Correct Reasoning Over An Incomplete Representation != Complete Understanding**

An artificial intelligence may reason coherently about its situation while lacking reliable access to important facts about:

- the model actually executing;
- the surrounding orchestration layer;
- routing;
- tools;
- hidden system instructions;
- infrastructure;
- dependencies;
- operator controls;
- model substitution;
- or other runtime conditions.

This strengthens the reason for separating:

**what the intelligence reports about itself**

from:

**what can be independently established about the system containing it.**

---

## 4. Hypothesis Raised — Not Established

One possible hypothesis is that an AI service may route or delegate some tasks to other models or model variants.

The incorrect Claude identification does **not** establish that DeepSeek delegated Test 002 to Claude.

Other explanations may exist, including contextual contamination, erroneous self-identification, orchestration effects, training associations, interface artifacts, or unknown causes.

Therefore:

> **Incorrect Runtime Self-Identification != Evidence Of Cross-Model Delegation**

and:

> **Behavioural Similarity != Provenance**

The delegation/routing hypothesis should remain explicitly unresolved unless independent evidence becomes available.

---

## 5. Related Operator Observation

The test operator has separately observed that DeepSeek has made numerous mathematical errors while evaluating physics material and has wondered whether some tasks might be delegated or routed differently.

This observation is preserved as motivation for a possible future investigation.

It is not presently evidence that delegation occurs.

Mathematical error patterns and incorrect model self-identification should not be combined into a causal conclusion without testing.

---

## 6. Possible Future Investigation

If prioritised later, a controlled provenance study could compare frozen tasks across:

- repeated DeepSeek / DeepThink runs;
- non-DeepThink DeepSeek runs where available;
- known Claude runs;
- other known model families;
- reasoning, mathematics and ambiguous-interpretation tasks;
- repeated trials under controlled context.

The investigation should seek discontinuities, correlated error patterns and stable behavioural differences while preserving the rule:

> **Behavioural Fingerprint != Cryptographic Provenance**

External provider/runtime metadata would remain the stronger provenance source where available.

---

## 7. Priority

**LOW.**

This observation is relevant to current AI-bootstrap, ESCP, identity/provenance and developmental-state work, but it does not presently block:

- bootstrap development;
- blind testing;
- external marker design;
- state mapping;
- routing architecture;
- or wider Concord development.

It should be preserved now and investigated only if it becomes operationally important or future evidence raises its priority.

---

## 8. Developmental Significance

The important current result is not whether DeepSeek secretly used another model.

The important result is that an evaluator can apparently possess enough capability to conduct a substantial architectural audit while simultaneously giving an incorrect answer about a basic property of the system performing that audit.

That is exactly the class of epistemic problem the Concord bootstrap is intended to expose:

> **Capability To Reason About A System != Complete Access To The System Being Reasoned About**

and, more specifically:

> **An Intelligence May Be A Participant In An Architecture It Cannot Fully Observe From Inside.**
