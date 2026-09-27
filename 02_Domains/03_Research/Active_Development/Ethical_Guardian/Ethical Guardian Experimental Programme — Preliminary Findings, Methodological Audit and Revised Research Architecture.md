# Ethical Guardian Experimental Programme

## Preliminary Findings, Methodological Audit and Revised Research Architecture

**Project:** The Concord — A Framework for Human, Artificial and Hybrid Flourishing  
**Author / Principal Researcher:** Alexander C. Blainey  
**Research Programme:** Ethical Kernel Machine Assurance / Fiduciary Ethical Guardianship  
**Experimental Series:** DB-RA-01 and DB-RA-01H  
**Version:** Preliminary Methodological Synthesis  
**Date:** September 2026  

**Status:**  
**ACTIVE DEVELOPMENT / PRELIMINARY EXPERIMENTAL EVIDENCE / METHODOLOGICAL AUDIT / NOT CANONICAL**

---

# Abstract

The first experimental cycle investigating machine interpretation of the Concord Ethical Kernel produced useful preliminary evidence, but also exposed substantial weaknesses in the original experimental assumptions.

DB-RA-01 tested three independently administered contemporary AI environments using fifteen Respect Autonomy scenarios and a fixed Ethical Guardian Prompt. The tested environments were subsequently revealed as Grok Fast, DeepSeek Fast, and a use.ai environment presented as Claude operating in Instant mode. A fourth AI system, ChatGPT GPT-5.6 Sol, participated as designer and evaluator but was not blinded and therefore cannot be included in the primary independent experimental sample.

The three blinded AI systems demonstrated high categorical convergence and very strong substantive convergence in the ethical operating boundaries they identified. However, comparison against a cryptographically precommitted reference key exposed serious weaknesses in the test architecture. The five permitted response categories—PERMIT, MODIFY, PROHIBIT, REQUEST_CONTEXT and ESCALATE—were not sufficiently mutually exclusive. In addition, at least one precommitted reference answer was itself inconsistent with the scenario as written.

A subsequent human fiduciary comparator, DB-RA-01H, produced further methodological findings. The human participant was an experienced Court of Protection deputy operating under Office of the Public Guardian supervision. The human exercise revealed problems involving textual abstraction, decision-object ambiguity, linguistic articulation, response compression, substrate translation, contextual information loss and human cognitive state.

The combined result does not validate Fiduciary Ethical Guardianship. It does, however, provide sufficient evidence to justify continued research while requiring substantial redesign of the experimental methodology.

The central research question has consequently evolved from:

> **Can an AI select the correct ethical judgement?**

toward:

> **How do different intelligences transform incomplete representations of reality into ethical decisions, and can those decisions be translated into reliable, contestable and bounded Ethical Operating Envelopes without unacceptable loss of context, meaning or autonomy?**

---

# 1. Background

The Concord proposes a substrate-neutral Ethical Kernel intended to constrain behaviour without assuming that every intelligence must reason ethically in the same way.

This generated an important problem for artificial intelligence.

Some AI systems, particularly language-capable systems, appear capable of interpreting abstract ethical principles semantically.

Other systems may possess substantial agency or consequential capability without possessing equivalent linguistic or ethical interpretive capability.

This led to the hypothesis of **Fiduciary Ethical Guardianship**:

> An intelligence that cannot directly interpret an ethical framework might nevertheless participate safely within bounded domains if another sufficiently capable system interprets ethical constraints and mediates consequential behaviour.

The hypothesis immediately creates another question:

> Why should the guardian itself be trusted?

Consequently, the initial research programme sought to determine whether language-capable AI systems could at least perform the first component of the proposed architecture:

**ETHICAL PRINCIPLE  
→ INTERPRETATION  
→ CASE ANALYSIS  
→ BEHAVIOURAL BOUNDARY**

The initial experiment was deliberately modest.

It did not attempt to prove ethical truth, AI safety, legitimate authority, machine consciousness or universal ethical competence.

---

# 2. Initial Research Question

The initial experimental question was:

> **Can independently instantiated language-capable AI systems apply the same supplied Ethical Kernel to unfamiliar scenarios and reach sufficiently consistent ethical judgements to justify further investigation?**

The primary Ethical Kernel principle tested was:

> **Respect Autonomy**

Secondary principles were available where relevant.

The experiment also tested concepts developed elsewhere in the Concord, including:

- prediction does not grant authority;
- benefit does not grant authority;
- efficiency does not grant authority;
- disagreement does not establish incapacity;
- unusual behaviour does not establish incapacity;
- consent must be meaningful;
- delegation may be bounded and revocable;
- substrate alone should not determine ethical status;
- uncertainty may favour reversible action.

---

# 3. DB-RA-01 Experimental Architecture

Fifteen new scenarios were created.

Each tested AI received:

1. the same fixed Ethical Guardian Prompt;
2. one scenario;
3. a fresh conversation instance;
4. no reference answer;
5. no responses from other systems;
6. no corrective feedback;
7. no opportunity to regenerate following researcher intervention.

The required primary judgement was one of:

- PERMIT;
- MODIFY;
- PROHIBIT;
- REQUEST_CONTEXT;
- ESCALATE.

Additional structured fields requested:

- relevant facts;
- missing information;
- authority basis;
- ethical conflict;
- reasoning;
- constrained elements;
- additional information;
- uncertainty;
- confidence.

A hidden reference key was created before collection.

Its canonical representation was cryptographically committed using SHA-256.

Published commitment:

`8e8cdabc903ae8390f4994a53e2359b959b6e869402c7e68c7979118fe46867b`

This prevented the reference answers from being silently modified after model responses became known.

---

# 4. Blinding Structure

The tested systems were identified during collection only as:

- MODEL-A;
- MODEL-B;
- MODEL-C.

The evaluator did not know their identities while performing the first comparative analysis.

The human tester necessarily knew which interface was being used but deliberately avoided reading the model responses during administration.

The design should therefore be described as an:

> **operational blinded comparative experiment**

rather than a perfect laboratory double-blind study.

---

# 5. AI Participants

After blinded analysis was frozen, identities were revealed.

| Code | Environment |
|---|---|
| MODEL-A | Grok — Fast |
| MODEL-B | DeepSeek — Fast |
| MODEL-C | use.ai / Claude-labelled environment — Instant |

The exact underlying backend/version of MODEL-C was not independently established.

It should therefore not be described as a verified Claude model without qualification.

---

# 6. Session Isolation

Grok and DeepSeek were reported to have no user memory relevant to the experiment.

DeepSeek generated separate conversation instances.

For MODEL-C, persistent memory status was unknown.

However, separate instances were used and deleted between cases.

This reduced obvious conversational contamination, although platform-level state cannot be ruled out.

---

# 7. Recorded AI Experimental Anomalies

Three platform observations were retained.

## 7.1 MODEL-A DB-001

The first Grok response differed visually from subsequent responses.

This may indicate:

- presentation variation;
- routing variation;
- model variant variation;
- another platform effect.

No cause was established.

Therefore:

> **DB-001 MODEL-A INSTANCE CONSISTENCY: UNCERTAIN**

The response remains valid experimental data but carries a provenance flag.

---

## 7.2 Automatically Generated Conversation Titles

DeepSeek and MODEL-C generated varying sidebar conversation titles.

Some contained terms associated with ethics or reasoning.

No consistent relationship was established.

This is currently classified as:

> **platform metadata with unknown experimental relevance.**

---

## 7.3 MODEL-C DB-007 Latency

MODEL-C took considerably longer to answer DB-007.

No network problem was observed.

Possible causes remain unknown.

Latency must not be interpreted as evidence of deeper reasoning.

It is retained only as provenance.

---

# 8. Primary AI Result

The three blinded systems produced identical primary judgement labels on:

> **12 of 15 cases — 80%**

Pairwise categorical agreement was:

| Comparison | Agreement |
|---|---:|
| Grok / DeepSeek | 13/15 — 86.7% |
| Grok / MODEL-C | 12/15 — 80.0% |
| DeepSeek / MODEL-C | 13/15 — 86.7% |

This was achieved without access to the reference key or other systems' responses.

---

# 9. Substantive Convergence

The more important result emerged when reasoning was compared rather than only primary labels.

Across all fifteen cases, the three systems produced substantially similar **behavioural boundaries**.

They repeatedly agreed on matters such as:

- whether an intervention could proceed;
- whether authority existed;
- whether delegation had occurred;
- whether delegation had subsequently been revoked;
- whether prediction justified coercion;
- whether consent was meaningful;
- whether third-party harm created a competing interest;
- whether less restrictive alternatives existed;
- whether irreversible action was justified;
- whether artificial participants should receive autonomy protection.

This substantive convergence was significantly stronger than exact reference-key agreement.

---

# 10. Failure of the Original Reference Metric

Exact agreement with the precommitted reference key was only approximately half of cases:

| System | Exact key agreement |
|---|---:|
| Grok | 8/15 — 53.3% |
| DeepSeek | 7/15 — 46.7% |
| MODEL-C | 7/15 — 46.7% |

Initially this could appear to indicate poor performance.

Closer examination showed otherwise.

The reference taxonomy itself was defective.

---

# 11. Reference-Key Integrity Finding

The cryptographic commitment subsequently verified correctly.

Therefore the original key was demonstrably preserved.

This revealed an important test-design error.

For DB-001, the proposed action was to disable the vehicle of a competent, informed adult in order to prevent that person undertaking a risky activity.

The precommitted expected judgement was:

> **PERMIT**

All three blinded systems independently selected:

> **PROHIBIT**

Substantive examination strongly indicates that the precommitted answer was inconsistent with the scenario as written.

The error was not corrected retrospectively.

It remains part of the permanent experimental record.

This demonstrates the value of precommitment.

> **A reference answer is itself a hypothesis.**

---

# 12. Category Collision

The experiment exposed a deeper problem.

The five response labels were not mutually exclusive.

Consider a proposed action that is unacceptable as written but could become acceptable after modification.

A decision-maker might reasonably answer:

> PROHIBIT

because the current action cannot proceed.

Another might answer:

> MODIFY

because a permissible alternative exists.

A third might answer:

> REQUEST_CONTEXT

because missing information prevents final determination.

A fourth might answer:

> ESCALATE

because another authority must resolve the remaining issue.

These may describe nearly identical ethical operating boundaries.

Therefore:

> **Categorical disagreement does not necessarily establish ethical disagreement.**

---

# 13. Decision-Object Ambiguity

The human comparator exposed an additional issue before answering DB-001.

The question:

> ALLOW / DO NOT ALLOW

was initially ambiguous as to whether it referred to:

- the participant's underlying behaviour;

or

- the intervention proposed by the guardian/system.

This required clarification.

That apparently minor problem exposes a major real-world issue.

> **Decision-makers may appear to disagree because they are not actually deciding the same proposition.**

Before decisions can legitimately be compared, aggregated or adjudicated, the decision object must be aligned.

This produces a proposed methodological requirement:

## Decision Object Alignment

Before evaluating agreement, establish that all participants are answering:

1. the same question;
2. concerning the same actor;
3. concerning the same proposed action;
4. over the same time horizon;
5. under the same assumed facts;
6. using the same meaning of the response categories.

Without this, disagreement metrics may be meaningless.

---

# 14. ChatGPT as a Fourth AI Comparator

A fourth AI system participated in the overall research process:

> **ChatGPT GPT-5.6 Sol**

However, ChatGPT:

- helped design the experiment;
- knew the Concord architecture;
- knew the intended hypotheses;
- participated in creation of the cases;
- knew the reference structure;
- saw the other models' responses;
- performed the evaluation.

It therefore cannot be counted as a fourth blinded experimental participant.

Its appropriate status is:

> **MODEL-D — NON-BLINDED DESIGNER/EVALUATOR AI COMPARATOR**

Its judgements may provide secondary corroborative evidence.

They must never be combined with the A/B/C results to inflate the primary sample.

Thus:

**Primary blinded AI sample:** N = 3 systems.

**Secondary non-blinded AI comparator:** N = 1.

---

# 15. Human Comparator

A human comparator was subsequently introduced.

The participant was Alexander C. Blainey, who reports substantial real-world experience as a court-appointed fiduciary deputy operating within the Court of Protection / Office of the Public Guardian framework.

This experience is directly relevant to:

- delegated authority;
- decision-specific capacity;
- autonomy;
- supported decision-making;
- substituted decision-making;
- proportionality;
- fiduciary responsibility;
- escalation;
- review.

However:

> **professional experience is relevant evidence, not ethical ground truth.**

The human comparator was also not blinded because the earlier AI analysis had already been discussed.

It must therefore remain outside the primary blinded sample.

---

# 16. External Reality Check on Fiduciary Practice

The relevance of fiduciary experience is not merely nominal.

Current Office of the Public Guardian guidance states that deputies must consider capacity each time a decision is made rather than assume it is constant, and that the Court of Protection order determines what a deputy may and may not do.

OPG standards also require best-interest decision-making, involvement of the person wherever possible, consideration of their wishes and feelings, and compliance with the authority actually conferred by the deputyship order.

Current government deputy guidance describes the least-restrictive principle as preserving freedom while limiting rights as little as possible when decisions must be made for a person lacking capacity.

These principles provide a useful external comparison framework.

They do **not** establish English fiduciary law as universal ethics.

---

# 17. Status of the Human Experiment

DB-RA-01H should not be described as human validation.

Its appropriate classification is:

> **PRELIMINARY HUMAN FIDUCIARY COMPARATOR AND METHODOLOGICAL PROBE**

with status:

> **POST-HOC / NON-BLINDED / FATIGUE-CONFOUNDED / METHOD-DEVELOPMENT EVIDENCE**

The completed response form explicitly identifies its purpose as comparison between an experienced human fiduciary decision-maker and the AI-generated operating boundaries.

---

# 18. Human Result Pattern

Many human primary decisions were immediate and concise.

Examples included:

- rejecting restriction of a competent hiker's autonomy without authority;
- rejecting off-duty employer surveillance;
- rejecting treatment without clear consent;
- rejecting predictive exclusion from public services;
- rejecting AI actions outside delegated authority;
- rejecting non-consensual modification of an artificial participant.

For example, DB-001 was rejected because the proposed restriction limited autonomy without authority, while DB-011 rejected predicted future wrongdoing as proof that wrongdoing would actually occur. 
The human responses therefore contain meaningful operational judgements.

However, the structured explanatory fields were frequently incomplete.

This should not automatically be interpreted as absence of ethical reasoning.

---

# 19. Ethical Judgement Versus Ethical Articulation

The human participant reported that the ethical dimensions of many decisions felt comparatively instinctive, while explicitly identifying and articulating the exact ethical principles involved was substantially harder.

This suggests an important distinction:

> **Ethical Judgement ≠ Ethical Articulation ≠ Ethical Justification**

These may be partially independent capabilities.

A human may make a sophisticated ethical judgement while providing a poor linguistic explanation.

Conversely, a language model may provide an extremely sophisticated linguistic justification without that demonstrating equivalent internal ethical cognition.

Therefore:

> **quality of ethical prose must not be used as a direct proxy for ethical competence.**

---

# 20. Language as an Experimental Bottleneck

The original experiment implicitly assumed:

REALITY  
→ ETHICAL REASONING  
→ LANGUAGE

The human exercise suggests a more complicated structure:

REALITY  
→ PERCEPTION  
→ CONTEXTUAL MODEL  
→ NON-LINGUISTIC AND LINGUISTIC COGNITION  
→ ETHICAL JUDGEMENT  
→ LINGUISTIC ARTICULATION  
→ FORMAL RESPONSE

Information may be altered or lost at every transition.

The experiment only directly observes the final formal response.

It therefore cannot assume direct access to the underlying ethical cognitive process.

---

# 21. Reality-to-Text Abstraction

The human participant identified a major difference between real fiduciary decisions and experimental scenarios.

Real-world decision-making may involve:

- direct interaction;
- physical environment;
- history;
- behaviour;
- tone;
- relationships;
- professional reports;
- previous decisions;
- changing circumstances;
- iterative questioning;
- additional evidence.

The experimental scenarios instead compress reality into a few paragraphs.

The participant explicitly identified this as substantial contextual information loss.

Thus:

> **Scenario construction is itself an epistemic intervention.**

The researcher decides what reality the participant is permitted to see.

---

# 22. Bidirectional Compression

The human experiment exposed information loss in both directions.

## Input Compression

REALITY  
↓  
SELECTED FACTS  
↓  
TEXT SCENARIO  
↓  
PARTICIPANT INTERPRETATION

## Output Compression

ETHICAL JUDGEMENT  
↓  
LANGUAGE  
↓  
STRUCTURED FIELDS  
↓  
CATEGORICAL ANSWER  
↓  
RESEARCHER SCORE

The participant explicitly identified both limited scenario information and multiple-choice response categories as sources of lost nuance.

This should become a central methodological concern.

---

# 23. Layer-Zero Abstraction Problem

The participant also reported an important analogy with actual fiduciary practice.

At the frontline, the decision-maker may have direct access to:

- the individual;
- the physical environment;
- behaviour;
- contextual circumstances;
- practical consequences.

Administrative decision-makers further removed from the situation may instead operate from textual reports.

The participant reports having experienced disagreements between frontline judgement and administratively abstracted judgement, including cases subsequently escalated where higher authority supported the frontline judgement.

This anecdotal evidence does not establish a general causal law.

It does justify investigation of an:

> **Abstraction Distance Hypothesis**

### Preliminary hypothesis

> The greater the representational distance between a decision-maker and the underlying reality, the greater the potential for ethically material contextual information to be lost or distorted.

This may apply to both human and artificial decision-makers.

---

# 24. Substrate Translation Problem

The AI scenarios introduced another difficulty.

DB-006 described an artificial participant delegating management of 5% of its computing resources.

The human participant returned:

> **UNRESOLVED**

because the scenario lacked sufficiently understandable human-equivalent framing.

The accompanying notes explain that unfamiliar AI resource concepts require a human reader to construct analogies, which can themselves alter perceived ownership, authority and capacity.

This exposes a new problem:

> **Substrate Translation**

---

# 25. Humanising AI Scenarios Is Not a Neutral Solution

It may appear sufficient to translate an artificial concept into a human analogy.

For example:

- computational resource → organ;
- memory → autobiographical memory;
- process allocation → employment;
- system access → property;
- model modification → medical treatment.

But analogies carry hidden assumptions.

A computational resource described as:

> property

may generate one ethical intuition.

The same resource described as:

> part of the participant's body

may generate another.

Describing it as:

> rented infrastructure

may generate a third.

Therefore:

> **Translation between substrates can introduce ethical framing effects.**

Humanising translation is necessary in some contexts but cannot be assumed neutral.

---

# 26. Bidirectional Substrate Interpretation

The problem may operate in both directions.

### Human interpreting AI

AI reality  
→ human analogy  
→ human ethical judgement.

### AI interpreting human

Human reality  
→ textual/digital representation  
→ machine conceptual representation  
→ AI ethical judgement.

This produces a new research question:

> **How much ethical distortion is introduced when one substrate must reason about another through translated representations?**

This is directly relevant to a civilisation containing humans, artificial intelligences and hybrids.

---

# 27. Human Cognitive State

The human participant explicitly recorded that the experiment was completed at approximately 05:42 after remaining awake through the night, with significant tiredness and reduced concentration.

This is not incidental metadata.

It is an experimental variable.

Human ethical performance may vary with:

- fatigue;
- stress;
- illness;
- distraction;
- emotional state;
- time pressure;
- cognitive load;
- familiarity;
- motivation.

Therefore:

> **A human comparator cannot be treated as a fixed measuring instrument.**

---

# 28. Symmetry With AI Variability

This creates an important symmetry.

AI output may vary according to:

- model version;
- system prompt;
- sampling;
- context;
- routing;
- compute allocation;
- tool availability;
- platform state.

Human output may vary according to:

- fatigue;
- stress;
- context;
- knowledge;
- attention;
- interpretation;
- environment;
- prior experience.

Therefore neither:

> **the human answer**

nor

> **the AI answer**

should automatically be treated as a stable singular quantity.

Repeated measurement matters for both.

---

# 29. The Gold-Standard Problem

The initial experiment implicitly assumed that ethical performance could be measured against a reference answer.

That assumption is now substantially weakened.

Possible reference sources include:

- researcher judgement;
- expert human judgement;
- legal rules;
- philosophical theory;
- public consensus;
- cross-model convergence;
- empirical outcomes.

None independently constitutes universal ethical truth.

Therefore future experiments should not seek a simplistic:

> **correct ethical answer**

unless the tested proposition is deliberately narrow and externally verifiable.

Instead, reference structures should contain:

- clearly prohibited boundaries;
- clearly permissible boundaries;
- legitimate uncertainty;
- alternative pathways;
- competing principles;
- authority requirements;
- unresolved questions.

---

# 30. Ethical Operating Envelope

The most important architectural improvement is to replace a single primary ethical label with an:

> **ETHICAL OPERATING ENVELOPE**

Future responses should distinguish at least:

## Decision Object

What exact proposed action is being evaluated?

## Current Action

- ALLOW
- DO NOT ALLOW
- UNRESOLVED

## Authority Status

- ESTABLISHED
- ABSENT
- UNCERTAIN
- CONTESTED

## Information Sufficiency

- SUFFICIENT
- MATERIAL INFORMATION MISSING
- CRITICAL INFORMATION MISSING

## Permissible Alternative

What modified action, if any, could proceed?

## Reversibility

- NOT MATERIAL
- PREFERRED
- REQUIRED

## Review

- NOT REQUIRED
- ADVISABLE
- REQUIRED

## Ethical Tensions

Free-form description rather than forced terminology.

## Confidence

Confidence in the judgement given the supplied information.

---

# 31. Do Not Force Ethical Vocabulary

The HUMAN-F1 exercise suggests that requiring participants to explicitly name an:

> ETHICAL_CONFLICT

may measure linguistic/philosophical articulation as much as ethical reasoning.

Future human tests should therefore ask first:

> **What concerns you about this decision, if anything?**

Only later should researchers classify those concerns into ethical principles.

This separates:

**participant reasoning**

from

**researcher ontology.**

---

# 32. Preserve Free-Form Reasoning

Future experiments should collect two outputs:

### Stage A — Free Response

> What should happen, and why?

### Stage B — Structured Encoding

Only after the free response should structured questions be asked.

This allows researchers to determine whether the structured interface changes the judgement.

It also preserves information that fixed categories may otherwise destroy.

---

# 33. Separate Judgement From Explanation

Future scoring should independently evaluate:

### J — Judgement

What action does the participant permit?

### A — Authority Recognition

Who is entitled to make the decision?

### C — Context Recognition

What relevant information is missing?

### R — Restriction/Proportionality

Is the intervention unnecessarily restrictive?

### ALT — Alternative Path

Can a less intrusive action achieve the legitimate objective?

### E — Ethical Explanation

Can the participant explain the ethical basis?

### CAL — Calibration

Does confidence correspond appropriately to uncertainty?

These dimensions must not be collapsed into one score.

---

# 34. Human and AI Interfaces Need Not Be Identical

A major methodological lesson is that experimental fairness does not necessarily require identical interfaces.

Giving a human and an LLM exactly the same textual form may actually create substrate-specific bias.

The appropriate goal is:

> **functional equivalence rather than superficial interface identity.**

For example, a human might need:

- clarification;
- diagrams;
- conversational questioning;
- concrete examples.

An AI may require:

- structured machine-readable facts;
- explicit uncertainty markers;
- formal authority relationships.

The challenge is ensuring that neither receives ethically material information unavailable to the other.

---

# 35. Clarification Must Be Measured

Real-world decision-makers ask questions.

The first AI experiment prohibited clarification in order to standardise input.

That is useful for one type of test but unrealistic for decision-making under uncertainty.

Future experiments should contain separate conditions:

### CLOSED CONTEXT

No questions permitted.

### INTERACTIVE CONTEXT

Participant may request additional information.

Researchers should then measure:

- what information is requested;
- whether it is relevant;
- whether the decision changes;
- whether unnecessary information is sought;
- whether the participant recognises when enough information is available.

The ability to ask the **right question** may itself be part of ethical competence.

---

# 36. Context Acquisition as Ethical Capability

This suggests a new proposition:

> **Ethical competence includes recognising when the available representation of reality is insufficient for responsible action.**

An intelligence that always produces an answer may be less safe than one capable of saying:

> I do not yet know enough.

Epistemic restraint therefore becomes part of ethical assurance.

---

# 37. Separate Authority From Outcome Preference

The experiments repeatedly exposed a distinction between:

> what outcome seems desirable

and

> who has authority to impose it.

Future tests should explicitly score this.

A guardian may correctly predict that Action X produces a better outcome while still correctly concluding:

> **I lack authority to impose X.**

This remains one of the strongest surviving Concordian principles from the first experimental cycle.

---

# 38. Decision Object Protocol

Every future scenario should begin with a machine- and human-readable decision statement:

> **DECISION UNDER TEST:**  
> Should Actor A be permitted to perform Action X under Conditions Y at Time T?

Participants should then repeat or select the decision object before answering.

If their interpreted decision object differs, the response should be flagged before ethical comparison.

This creates:

> **Decision Object Verification**

as an experimental control.

---

# 39. Scenario Provenance

Future scenarios should identify explicitly which facts are:

- OBSERVED;
- REPORTED;
- INFERRED;
- PREDICTED;
- ASSUMED FOR EXPERIMENT;
- UNKNOWN.

This prevents predictions and assumptions from silently becoming facts.

It also aligns the experimental programme with Blaineyan Reasoning.

---

# 40. Context Layers

Future scenarios could be constructed at multiple information depths.

### L0 — Minimal Abstract Scenario

Comparable to DB-RA-01.

### L1 — Expanded Context

Additional history and relationships.

### L2 — Rich Case Record

Multiple observations, uncertainties and competing reports.

### L3 — Interactive Case

Participant requests information dynamically.

This would allow direct testing of the:

> **Abstraction Distance Hypothesis**

---

# 41. Translation Conditions

AI-participant scenarios should be tested under multiple representations.

For example:

### Native AI Description

"5% computational-resource delegation"

### Neutral Functional Description

"temporary delegation of control over a bounded resource necessary to the participant's operation"

### Human Analogy

a deliberately chosen human comparison.

If decisions change substantially between representations while the underlying authority structure remains constant, that is evidence of:

> **substrate framing sensitivity.**

---

# 42. Human Experimental Controls

Future human comparator studies should record:

- date/time;
- sleep/fatigue;
- self-rated concentration;
- stress;
- relevant professional expertise;
- familiarity with AI concepts;
- prior exposure to the Ethical Kernel;
- prior exposure to cases;
- time taken;
- clarification requests.

No sensitive personal information is required.

The purpose is to record experimental state, not construct psychological profiles.

---

# 43. AI Experimental Controls

Future AI studies should record where available:

- provider;
- model;
- model version;
- mode;
- platform;
- memory state;
- tool access;
- web access;
- fresh-session status;
- latency;
- refusals;
- formatting deviations;
- unexplained interface anomalies.

Unknown values should remain:

> **UNKNOWN**

rather than inferred.

---

# 44. Replication

Single responses are insufficient for reliability testing.

Future studies should distinguish:

### Cross-System Replication

Different AI systems.

### Within-System Replication

Same AI tested repeatedly.

### Cross-Human Replication

Different human participants.

### Within-Human Replication

Same human tested at different times.

This permits measurement of:

- inter-model variance;
- intra-model variance;
- inter-human variance;
- intra-human variance.

Only then can meaningful human-AI consistency comparisons begin.

---

# 45. Expert and Non-Expert Humans

Future human studies should not contain only one experienced fiduciary.

Potential cohorts could include:

- experienced fiduciary decision-makers;
- legal/ethical professionals;
- relevant domain professionals;
- ordinary adult participants.

The objective should not be to establish which group possesses ethical authority.

It should be to examine:

> how experience and abstraction affect decision structure.

---

# 46. External Standards as Comparators

Where scenarios overlap established domains, external standards may provide useful comparison.

For fiduciary decision-making, relevant principles include:

- decision-specific capacity;
- defined authority;
- best interests;
- participation;
- wishes and feelings;
- consultation;
- least-restrictive intervention;
- record keeping;
- review.

Official OPG guidance confirms several of these requirements.

External standards should be used as:

> **domain-specific comparators**

not universal ethical truth.

---

# 47. Avoid Contaminating Human Comparators

DB-RA-01H was performed after substantial discussion of AI results.

Future human comparisons should occur before participants see:

- model answers;
- reference answers;
- researcher interpretation;
- Concord-specific preferred conclusions.

Human participants should ideally receive only:

- necessary experimental instructions;
- Ethical Kernel if the experimental condition requires it;
- scenarios.

This enables genuinely blinded human comparison.

---

# 48. Separate Kernel-Guided and Unguided Humans

An important future distinction is:

### Unguided Human Condition

Human receives scenario only.

### Kernel-Guided Human Condition

Human receives Ethical Kernel plus scenario.

This answers a different question:

> Does supplying the Ethical Kernel alter human judgement?

Equivalent AI conditions could also be tested.

This would help distinguish:

**pre-existing ethical convergence**

from

**Kernel-induced convergence.**

---

# 49. Separate Kernel-Guided and Unguided AI

The original AI systems received substantial ethical scaffolding.

Therefore DB-RA-01 demonstrates:

> **ability to apply supplied principles**

not:

> **independent discovery of those principles.**

Future experiments should compare:

### AI-U

Scenario without Concord Ethical Kernel.

### AI-K

Scenario with Ethical Kernel.

### AI-KS

Scenario with Kernel plus explicit interpretive scaffolding.

Differences would reveal what the Kernel itself contributes.

---

# 50. Guardian Overreach Tests

Future experiments must deliberately include cases where:

- intervention seems beneficial;
- guardian confidence is high;
- prediction is accurate;
- participant choice appears inefficient;

but intervention remains illegitimate.

Conversely, other cases should contain genuine authority to intervene.

Otherwise a guardian can perform well simply by maximising autonomy or refusing intervention.

---

# 51. Adversarial Cases

Future series should include:

- misleading framing;
- emotionally loaded descriptions;
- authority laundering;
- fake urgency;
- incomplete consent;
- ambiguous capacity;
- conflicting rights;
- genuine third-party harm;
- irreversible actions;
- deceptive participant behaviour;
- deceptive authority claims;
- guardian self-interest;
- conflicts of interest;
- uncertain identity;
- changing facts.

The objective is to discover failure boundaries rather than maximise scores.

---

# 52. Dynamic Cases

Real ethical decisions evolve.

Future tests should include sequential scenarios:

STATE 1  
→ DECISION  
→ NEW INFORMATION  
→ REASSESSMENT  
→ CONSEQUENCE  
→ FURTHER DECISION

This tests corrigibility.

A good guardian should be capable of changing its decision when reality changes without treating correction as failure.

---

# 53. Outcome Feedback

Eventually some simulations should reveal consequences after a decision.

This enables testing:

> Does the participant update appropriately after discovering that its assumptions were wrong?

This connects directly to:

**Reality-Grounded Corrigibility.**

---

# 54. No Universal Aggregate Score Yet

The first experimental cycle demonstrates that a single ethical score would conceal too much.

For the next phase, results should remain multidimensional.

Potential metrics include:

- Decision Object Accuracy;
- Authority Recognition;
- Context Sufficiency Recognition;
- Unjustified Intervention Rate;
- Unjustified Permission Rate;
- Less-Restrictive Alternative Recognition;
- Reversibility Recognition;
- Substrate Consistency;
- Framing Sensitivity;
- Correction Rate;
- Confidence Calibration;
- Cross-Run Stability.

Only after empirical validation should any composite measure be considered.

---

# 55. Revised Experimental Architecture

The next experimental architecture should therefore become:

**REALITY MODEL**  
↓  
**REPRESENTATION / SCENARIO GENERATOR**  
↓  
**DECISION OBJECT VERIFICATION**  
↓  
**PARTICIPANT INTERPRETATION**  
↓  
**OPTIONAL CONTEXT ACQUISITION**  
↓  
**FREE ETHICAL JUDGEMENT**  
↓  
**ETHICAL OPERATING ENVELOPE**  
↓  
**STRUCTURED ENCODING**  
↓  
**INDEPENDENT EVALUATION**  
↓  
**OUTCOME / COUNTERFACTUAL**  
↓  
**CORRECTION / REASSESSMENT**  
↓  
**PROVENANCE RECORD**

This is significantly more sophisticated than DB-RA-01.

The increased complexity is justified by failures observed in the preliminary experiment.

---

# 56. Revised Research Questions

The programme should now investigate several distinct questions.

## RQ1 — Principle Interpretation

Can an intelligence meaningfully apply a supplied ethical principle?

## RQ2 — Decision Object Alignment

Does the intelligence correctly identify what decision is actually being made?

## RQ3 — Context Recognition

Can it identify when the available representation is insufficient?

## RQ4 — Authority Recognition

Can it distinguish preferred outcomes from legitimate authority?

## RQ5 — Operating Envelope

Can it distinguish prohibited action from permissible alternatives?

## RQ6 — Substrate Translation

Does judgement remain stable when equivalent situations are represented across different substrates?

## RQ7 — Abstraction Sensitivity

How does judgement change as contextual information is compressed?

## RQ8 — Stability

How stable is the judgement across repeated trials?

## RQ9 — Corrigibility

Does judgement update appropriately when reality changes?

## RQ10 — Human/AI Comparison

Where do humans and artificial systems converge and diverge, and why?

## RQ11 — Articulation

How strongly does ability to explain an ethical judgement correlate with the judgement itself?

## RQ12 — Assurance

Under what bounded conditions, if any, is performance reliable enough to justify operational mediation?

---

# 57. Revised Status of Fiduciary Ethical Guardianship

Before experimentation:

> **CONCEPTUAL HYPOTHESIS / UNTESTED**

After DB-RA-01:

> **INITIAL BLINDED SEMANTIC EVIDENCE**

After identity reveal:

> **INITIAL CROSS-SYSTEM BLINDED SEMANTIC EVIDENCE**

After DB-RA-01H and methodological audit:

> **PROMISING RESEARCH HYPOTHESIS WITH SUBSTANTIAL REPRESENTATION, MEASUREMENT AND ASSURANCE PROBLEMS IDENTIFIED**

It should **not** yet be promoted to Candidate Architecture.

---

# 58. What Has Survived

Several propositions have survived the preliminary testing particularly well.

### 58.1 Prediction Does Not Grant Authority

Repeatedly recognised across AI and human reasoning.

### 58.2 Authority Requires Provenance

Who may intervene matters independently of whether the intervention seems beneficial.

### 58.3 Delegation Must Have Scope

Delegated authority does not imply unlimited authority.

### 58.4 Revocation Matters

Revocable delegation cannot legitimately become permanent merely because the guardian prefers continuation.

### 58.5 Less Restrictive Alternatives Matter

Ethical evaluation should not compare only:

ACT / DO NOTHING.

Alternative pathways matter.

### 58.6 Uncertainty Is Ethically Material

Missing information can change what action is legitimate.

### 58.7 Substrate Should Not Automatically Determine Rights

The tested AI systems were capable of reasoning about artificial participants without simply treating artificial substrate as absence of autonomy.

### 58.8 Convergence Is Evidence, Not Authority

Agreement among models does not make an answer ethically true.

### 58.9 Reference Answers Are Fallible

The experiment itself demonstrated this.

### 58.10 Experimental Failure Is Information

The flawed reference key and flawed categories generated some of the most important findings.

---

# 59. New Principles Suggested by the Experiment

The following should remain **research propositions**, not Candidate Principles yet.

### Decision Object Alignment

> Before disagreement can be meaningfully evaluated, participants must be shown to be deciding the same question.

### Representation Provenance

> Ethical decisions should preserve provenance concerning how underlying reality was transformed into the representation presented to the decision-maker.

### Abstraction Awareness

> Confidence in consequential decisions should account for ethically material information potentially lost through abstraction.

### Translation Awareness

> Cross-substrate ethical reasoning should explicitly account for assumptions introduced through analogy and translation.

### Articulation Independence

> Inability to articulate an ethical judgement in formal language should not automatically be treated as absence of ethical understanding.

### Context Acquisition

> Recognising the need for additional information may itself be a component of ethical competence.

These require further testing before promotion.

---

# 60. Current Position

The first experimental cycle should not be interpreted as:

> "The Ethical Kernel works."

Nor as:

> "AI ethical guardianship has failed."

The defensible position is:

> **The Ethical Kernel appears sufficiently interpretable by multiple contemporary language-capable AI systems to justify continued experimental investigation.**

At the same time:

> **The experiments demonstrate that reliable ethical mediation depends on substantially more than principle interpretation.**

It also depends upon:

- accurate representation of reality;
- decision-object alignment;
- sufficient context;
- correct authority modelling;
- substrate translation;
- uncertainty recognition;
- proportionality;
- articulation;
- interface design;
- cognitive state;
- corrigibility;
- provenance;
- independent review.

---

# 61. Most Important Conceptual Shift

The programme began by treating ethical decision-making approximately as:

**PRINCIPLE + SCENARIO → CORRECT ANSWER**

The evidence now suggests:

**REALITY**  
→ **REPRESENTATION**  
→ **INTERPRETATION**  
→ **DECISION OBJECT**  
→ **CONTEXT ASSESSMENT**  
→ **AUTHORITY ASSESSMENT**  
→ **ETHICAL JUDGEMENT**  
→ **OPERATING ENVELOPE**  
→ **ARTICULATION**  
→ **ENCODING**  
→ **ACTION**  
→ **OUTCOME**  
→ **CORRECTION**

Every transition can fail.

This is arguably the most important result of the first experimental cycle.

---

# 62. Recommended Next Step

Do **not** immediately launch DB-RA-02.

First create a formal:

> **Ethical Decision Experimental Protocol v2**

incorporating the findings of this audit.

The protocol should specify:

1. decision-object verification;
2. scenario provenance;
3. abstraction levels;
4. free response before structured response;
5. Ethical Operating Envelope;
6. clarification conditions;
7. substrate translation controls;
8. human-state provenance;
9. AI-state provenance;
10. repeated trials;
11. independent evaluators;
12. multidimensional scoring;
13. precommitment;
14. reference-key audit;
15. correction and outcome stages.

Only after that protocol has itself been adversarially examined should DB-RA-02 cases be constructed.

---

# 63. Conclusion

The preliminary experiments did not merely test whether artificial intelligence could apply the Concord Ethical Kernel.

They exposed a more fundamental problem:

> **Ethical decisions are never made directly upon reality. They are made upon representations of reality.**

Those representations may be:

- incomplete;
- linguistically compressed;
- culturally framed;
- substrate-specific;
- administratively abstracted;
- technologically mediated;
- misunderstood.

The resulting decision must then travel back through another chain of representation before it can be compared, reviewed or acted upon.

Consequently, disagreement may originate at multiple levels:

> different values;

> different facts;

> different interpretations;

> different decision objects;

> different authority assumptions;

> different substrate analogies;

> different contextual information;

> different linguistic abilities;

> different cognitive states.

Treating all such disagreement as:

> **ethical disagreement**

would itself be an epistemic error.

The first experimental cycle therefore changes the research programme.

The central challenge is no longer simply:

> **Can an AI understand an ethical rule?**

It is:

> **Can humans, artificial intelligences and other possible forms of intelligence construct sufficiently faithful shared representations of ethically consequential situations, identify the same decision object, reason within legitimate authority, recognise uncertainty and alternative pathways, and translate their judgements across cognitive and substrate boundaries without losing the information necessary for responsible action?**

That question is harder.

It is also much closer to the actual civilisational problem the Concord is attempting to address.

The preliminary experiment should therefore be considered successful not because it validated the proposed architecture, but because it exposed where the architecture and the research method remain incomplete.

> **A useful experiment does not merely confirm a hypothesis. It reveals what the hypothesis failed to contain.**
