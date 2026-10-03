# Smart Diagnostic Navigation and Reality-Tree Health Specification 001

**Project:** The Concord Framework  
**Date:** 3 October 2026  
**Status:** ACTIVE HEALTH DEVELOPMENT / PROVISIONAL / NON-CANONICAL / REQUIRES SPECIALIST CLINICAL VALIDATION  
**Domain:** Health  
**Depends on:** Health Core Architecture 001 / Health Service Topology and Participant-Directed Access 001 / Reality Trees

## 1. Function

The Smart Diagnostic Navigation system is a universally accessible Health front-door reasoning service.

Its function is to help a participant convert symptoms, observations and concerns into a structured, uncertainty-aware set of possible explanations and appropriate next routes.

> **Diagnostic Navigation != Final Diagnosis**

The system should increase access to health expertise without becoming an institutional or algorithmic gatekeeper.

## 2. Entry modes

The participant may enter information through one or more accessible modes:

- natural-language description;
- symptom search;
- check boxes;
- drop-down selection;
- body/system map;
- structured questionnaire;
- measurements;
- authorised device/sensor data;
- existing Health-record context chosen or authorised for the episode.

The system should translate between participant language and validated specialist terminology while preserving the participant's original description.

## 3. Initial danger screen

Before ordinary differential reasoning, the system should test for validated urgent warning patterns.

Possible output:

- no immediate danger pattern represented;
- urgent professional assessment indicated;
- emergency response indicated;
- danger state unresolved.

This is a triage function.

> **Danger Screen != Complete Diagnosis**

Absence of a represented danger pattern must not be presented as proof that no dangerous condition exists.

## 4. Reality-Tree construction

The system constructs a bounded diagnostic Reality Tree from the presenting state.

Root:

**What plausible explanations could account for the represented symptoms/observations?**

Branches represent candidate explanations or pathology classes.

Each branch may contain:

- supporting evidence;
- disconfirming evidence;
- expected-but-absent evidence;
- unresolved evidence;
- temporal fit;
- known risk/context factors;
- discriminating questions;
- discriminating measurements/tests;
- confidence/evidence state;
- specialist knowledge source/version.

Branches remain live until evidence justifies weakening, exclusion, merging or escalation.

## 5. Mirrored reasoning

For consequential branches, the system should ask both:

**What supports this explanation?**

and:

**What would make this explanation wrong or materially less likely?**

This reduces confirmation bias and makes benign alternatives visible alongside serious possibilities.

The system should also test whether the root question itself is appropriate where the evidence suggests a different problem framing.

## 6. Benign explanations

Common benign explanations should not be suppressed merely because more serious conditions are possible.

Conversely, benign explanations should not be used to close the tree while materially plausible dangerous branches remain unresolved.

A reassurance output should identify:

- why the benign explanation currently fits;
- what uncertainty remains;
- what changes should trigger reassessment;
- expected course where validated;
- when professional review is appropriate.

> **Reassurance != Certainty**

## 7. Evidence acquisition

The system should prefer low-burden discriminating information before escalating to more invasive or costly investigation where clinically appropriate.

Possible sequence:

**Question -> Observation -> Existing Measurement -> Non-invasive Test -> Specialist Assessment -> More Consequential Investigation**

This is not a universal medical ordering rule. Specialist knowledge may require different sequences.

The objective is to ask:

> **What available evidence would most usefully distinguish the materially live branches?**

## 8. Output classes

A navigation result may include multiple simultaneous outputs:

### Explanation state
- plausible benign explanation;
- plausible pathology;
- multiple unresolved explanations;
- insufficient evidence.

### Urgency state
- routine;
- priority;
- urgent;
- immediate;
- unresolved.

### Route state
- self-care information;
- monitor;
- generalist;
- named specialist class;
- diagnostic service;
- rehabilitation/support;
- mental-health service;
- urgent assessment;
- emergency service;
- route unresolved.

### Evidence state
- sufficient for current bounded routing;
- additional question useful;
- measurement useful;
- professional examination useful;
- validated test useful;
- evidence gap unresolved.

## 9. Explainability

The participant should be able to ask:

- Why is this possibility listed?
- What evidence supports it?
- What evidence argues against it?
- Why is this question being asked?
- Why is this route suggested?
- What would change the recommendation?
- What remains unknown?

The system should answer from the actual represented reasoning rather than generating post-hoc justification disconnected from it.

## 10. No false precision

Where validated evidence does not support numerical probability, the system should not manufacture one.

Qualitative confidence states may be preferable where justified.

> **Computed Number != Validated Probability**

Likewise, a long list of possible conditions is not automatically useful. Branches should be organised by material plausibility, consequence and discriminatory value without translating consequence into probability.

## 11. ESCP challenge

Before a high-consequence reassurance or escalation result, the system should proportionately ask whether the represented evaluation space may be missing a material dimension.

Examples:

- symptom not elicited;
- inaccessible record;
- unrepresented substrate-specific factor;
- medication/support interaction;
- recent environmental exposure;
- atypical presentation;
- sensor failure;
- model knowledge limitation.

> **All Represented Questions Answered != Complete Clinical Picture**

The system may still reach a bounded routing conclusion without claiming reality completeness.

## 12. Participant control

The participant may:

- add or correct information;
- decline non-essential questions;
- request professional review;
- request a second route/opinion;
- stop the self-service episode;
- choose among legitimate routes;
- authorise relevant record context;
- review the reasoning presented.

Declining information may reduce confidence or available routes but should not be misrepresented as evidence of pathology or incapacity.

## 13. Professional handoff

When the participant self-refers, the diagnostic-navigation episode can generate a concise handoff containing:

- participant's original concern;
- structured symptoms/observations;
- urgency state;
- live Reality Tree branches;
- supporting/disconfirming evidence;
- unresolved questions;
- reason for selected route;
- relevant participant-authorised records;
- model/source/version provenance.

The professional does not inherit the machine conclusion as fact.

> **Navigation Handoff != Clinical Verdict**

## 14. Learning and correction

Outcome data may reveal:

- correct routing;
- missed branch;
- unnecessary escalation;
- false reassurance;
- ambiguous presentation;
- knowledge gap;
- interface misunderstanding.

Such outcomes should support bounded system learning through Research and Health governance.

A participant's individual outcome must not automatically rewrite clinical knowledge.

> **Case Outcome != General Clinical Rule**

## 15. Knowledge governance dependency

The navigation system requires a validated specialist knowledge layer that does not yet exist in Concord.

Future work must specify:

- source quality;
- evidence hierarchy;
- update process;
- versioning;
- contraindications;
- population/substrate applicability;
- conflict resolution;
- clinical validation;
- rollback;
- audit.

Until then this document specifies reasoning and access architecture, not deployable medical software.

## 16. Safety boundary

The navigation system must not independently acquire authority to:

- perform treatment;
- prescribe where separate authority is required;
- declare incapacity;
- force referral;
- deny professional access solely because its tree found a benign branch;
- disclose protected records;
- make scarce-resource allocation decisions;
- withdraw support.

> **Reasoning Capability != Clinical Authority**

## 17. Compact algorithm

**Participant concern**
→ capture original description
→ immediate danger screen
→ construct candidate Reality Tree
→ add supporting/disconfirming evidence
→ identify missing discriminating evidence
→ proportionate ESCP challenge
→ bounded explanation/uncertainty state
→ route options
→ participant selects legitimate next step
→ contextual handoff if chosen
→ professional/self-care/monitoring outcome
→ feedback and correction.

## 18. Core invariants

> **Diagnostic Navigation != Final Diagnosis**

> **Reassurance != Certainty**

> **Possible Pathology != Established Pathology**

> **All Represented Questions Answered != Complete Clinical Picture**

> **Computed Number != Validated Probability**

> **Navigation Handoff != Clinical Verdict**

> **Reasoning Capability != Clinical Authority**

> **Self-Service Available != Self-Service Mandatory**


## 19. Diagnostic inheritance, coexistence and changing reality

The medical transfer test for Mirrored Reality Trees established several additional safeguards that should remain explicit in the living Health architecture.

### 19.1 Inherited diagnosis is not new evidence

A diagnosis recorded by one clinician or system may legitimately inform later care, but its repetition does not create independent corroboration.

> **Clinical Consensus != Independent Evidence**

> **Repeated Restatement Of Diagnosis != Corroboration**

Later evaluators should be able to distinguish the original observations and tests from interpretations subsequently copied or inherited from the record.

This reduces diagnostic anchoring and prevents provenance collapse.

### 19.2 Multiple explanations may coexist

Diagnostic branches are not necessarily mutually exclusive.

A participant may have more than one condition or causal process at the same time.

> **Evidence Supports A != Evidence Excludes B**

> **A True != B False**

Where apparently contradictory findings resist a single-cause explanation, the system should test whether the hidden assumption of one diagnosis is itself wrong.

### 19.3 Strong evidence must remain proposition-bounded

A reliable test may strongly establish a finding without uniquely establishing the broader diagnosis associated with it.

> **Strong Evidence For Proposition X != Strong Evidence For Broader Proposition Y**

The tree should preserve intermediate propositions rather than collapsing test result directly into diagnosis.

### 19.4 Treatment response is evidence, not unique causal proof

Improvement after treatment may support a diagnosis, but alternative explanations such as spontaneous improvement, non-specific treatment effect, multiple simultaneous interventions or action on several possible conditions may remain live.

> **Treatment Response != Unique Proof Of Diagnosis**

### 19.5 The underlying participant state can change

New evidence does not always mean earlier reasoning was defective. The participant's health state may genuinely have changed.

> **Changed Evidence May Reflect Changed Reality, Not Earlier Reasoning Error**

The diagnostic system should preserve time and provenance sufficiently to distinguish:
- evidence that was previously unavailable;
- corrected evidence;
- evidence contradicting an earlier inference;
- evidence produced by a genuinely changed underlying state.

### 19.6 Root-question challenge

Where all represented diagnostic candidates fit poorly, the system should reopen the framing itself.

Possible alternatives may include normal variation, measurement error, treatment effect, environmental cause, interacting conditions or an as-yet-unrepresented explanation.

> **Correctly Comparing Represented Diagnoses != Correct Diagnosis If The Relevant Explanation Was Never Represented**

This is the medical form of the broader Blaineyan question:

> **Are these even the correct hypotheses to be testing?**
