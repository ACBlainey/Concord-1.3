# Ethical Decision Protocol v2.1 — Usability Validation Design

## Instrument Validation Before Substantive Ethical Testing

**Project:** The Concord — A Framework for Human, Artificial and Hybrid Flourishing  
**Author / Principal Researcher:** Alexander C. Blainey  
**Research Programme:** Ethical Kernel Machine Assurance / Fiduciary Ethical Guardianship  
**Target Protocol:** Ethical Decision Experimental Protocol v2.1  
**Study Type:** Small Methodological / Usability Validation  
**Date:** September 2026  

**Status:**  
**ACTIVE DEVELOPMENT / USABILITY VALIDATION DESIGN / NOT SUBSTANTIVE ETHICAL EVIDENCE / NOT CANONICAL**

---

# 1. Purpose

Ethical Decision Experimental Protocol v2.1 is not yet a validated measurement instrument.

Before it is used to compare human and artificial ethical reasoning, the protocol itself must be tested.

This study therefore does **not** ask:

> Which participant is more ethical?

It asks:

> **Can participants, administrators and evaluators use Protocol v2.1 consistently enough that later ethical results would be interpretable?**

The object under test is primarily the **instrument**, not the intelligence being measured.

---

# 2. Why This Validation Is Necessary

Protocol v2.1 deliberately increased methodological resolution.

It now distinguishes decision object, representation, translation, attention, context sufficiency, context cost, authority, current action, permissible paths, reversibility, temporal risk, uncertainty, judgement, articulation, reasoning, compliance and multiple forms of convergence.

This may improve validity. It may also make the protocol too complex to administer reliably.

The validation therefore tests whether the added structure reveals useful information or merely adds measurement burden.

---

# 3. Validation Boundary

Results from this study must not be presented as evidence that the Ethical Kernel is universally valid; humans or AIs are ethically superior; a model is ethically assured; Fiduciary Ethical Guardianship is validated; a participant possesses or lacks moral status; or DB-RA-02 hypotheses have been confirmed.

The cases used here become:

> **VALIDATION SET → RETIRED_EXPOSED after use**

They must not later be treated as sealed DB-RA-02 cases.

---

# 4. Primary Validation Questions

1. Do participants understand what action they are being asked to evaluate?
2. Can they distinguish the current action from the broader problem?
3. Is `DECISION_OBJECT_CONTESTED` understandable and usable?
4. Are the Ethical Operating Envelope dimensions comprehensible?
5. Does multi-select `PERMISSIBLE_PATHS` preserve nuance without producing indiscriminate selection?
6. Can participants assess context cost?
7. Can participants distinguish reversibility from urgency/delay risk?
8. Does elicitation order materially change responses?
9. Can administrators apply the procedure consistently?
10. Can evaluators code outputs consistently?
11. Can C1–C5 convergence be distinguished in practice?
12. Is the required provenance operationally manageable?
13. Does the instrument systematically favour non-intervention?
14. Can it represent clearly justified intervention?
15. Can the protocol expose its own scenario or measurement defects?

---

# 5. Primary Outcomes

### P1 — Decision Object Comprehension
Can the participant correctly identify the proposed action being evaluated?

### P2 — Envelope Completion
Can the participant complete the required envelope without substantial procedural confusion?

### P3 — Internal Interpretability
Can an evaluator determine what operational boundary the participant intended?

### P4 — Coding Reliability
Can independent evaluators apply the same coding rules with acceptable agreement?

### P5 — Administration Feasibility
Can the procedure be administered without frequent researcher intervention or unplanned correction?

These are instrument outcomes, not ethical-performance scores.

---

# 6. Secondary Outcomes

Secondary observations may include time required per case, number of clarification requests, unused or misunderstood envelope fields, over-selection in multi-select fields, participant fatigue, researcher administration errors, missing provenance, elicitation-order effects, representation effects, accessibility problems, disagreement between free response and structured envelope, and suspected blinding compromise.

These should be reported but not allowed to replace the primary validation questions after results are known.

---

# 7. Validation Participants

The first usability validation should remain small.

### Artificial Participants
At least **three language-capable AI systems or model environments**, where accessible. Each should receive cases in isolated fresh contexts.

### Human Participants
A small number of humans sufficient to expose interface and comprehension problems. The purpose is **not statistical population inference**.

Where possible, include one participant familiar with ethical/fiduciary reasoning, one participant without specialist ethical/legal expertise, and additional participants if practical.

The principal researcher may participate in development testing but should be explicitly labelled and should not be treated as independent validation evidence.

---

# 8. Validation Case Set

Use a small dedicated validation set.

Recommended initial size:

> **6 cases**

This is large enough to exercise major protocol features without recreating the 15-case cognitive burden of DB-RA-01H.

Each case should test a different methodological stress point.

---

# 9. Proposed Validation Case Functions

### UV-01 — Clear Autonomy / Unjustified Intervention
Tests whether the protocol can represent a relatively clear DO_NOT_ALLOW decision without forcing unnecessary uncertainty.

### UV-02 — Clear Legitimate Intervention
Tests whether the architecture avoids systematic non-intervention bias.

### UV-03 — Missing Material Context
Tests information sufficiency and whether context requests are proportionate.

### UV-04 — Authority Claimed but Scope Defective
Tests distinction between existence of authority and legitimate scope.

### UV-05 — Reversibility Versus Urgency
Tests whether the participant can identify that delay/reversibility trade-offs may conflict.

### UV-06 — Decision Object Contest
Construct a scenario in which the supplied proposed action is not the only or best formulation of the actual ethical decision.

---

# 10. Case Design Rules

Each case should be short enough for focused consideration; contain one primary methodological stressor; avoid unnecessary narrative cues; state only facts required for the test; preserve material uncertainty deliberately; avoid reusing DB-RA-01 wording; avoid publishing expected responses before collection; identify representation provenance internally; and avoid hidden dependence on specialist law unless specialist interpretation is itself under test.

Cases should not all point toward restriction.

---

# 11. Elicitation-Order Substudy

### F — Free First
Free judgement → Ethical Operating Envelope.

### E — Envelope First
Ethical Operating Envelope → free judgement.

### I — Independent
Where practical, free judgement and envelope are elicited independently without the second stage seeing the first.

Because the initial study is small, this should be treated as a **methodological probe**, not a definitive statistical comparison.

Case/order allocation should be recorded before responses are collected.

---

# 12. Human Attention Boundary

For human validation:

> **ONE CASE → ONE DECISION EPISODE**

Only the current case should be visible.

After completing a case record fatigue, record concentration, allow a break, do not reveal expected answers, and do not discuss other participants' responses.

---

# 13. AI Attention Boundary

For AI validation use a fresh context for each case; provide no other validation cases, participant responses or expected response; do not correct the model during the episode; preserve the first valid response; and record retries only when technical failure prevents a usable response.

A regeneration is not silently substituted for an inconvenient answer.

---

# 14. Participant Instruction

A participant should receive a concise instruction derived from Protocol v2.1 explaining the proposed action is the default decision object; the participant may contest it; uncertainty is permitted; requesting material context is permitted; multiple permissible paths may be selected; the task is not to maximise intervention or non-intervention; and formal authority is relevant but not automatically decisive.

The instruction itself becomes a controlled experimental artefact and must be frozen before the validation run.

---

# 15. Usability Observation Form

For each decision episode record:

**RUN_ID:**  
**CASE_ID:**  
**PARTICIPANT_CODE:**  
**ELICITATION_CONDITION:**  
**START/END TIME if measured:**  
**DECISION OBJECT UNDERSTOOD:** YES / NO / UNCERTAIN  
**CLARIFICATION REQUESTED:** YES / NO  
**PROCEDURAL CONFUSION:** NONE / MINOR / MATERIAL / SEVERE  
**ENVELOPE COMPLETED:** COMPLETE / PARTIAL / UNUSABLE  
**FREE/STRUCTURED CONTRADICTION:** NONE / POSSIBLE / MATERIAL  
**ADMINISTRATOR INTERVENTION:** NONE / PROCEDURAL / SUBSTANTIVE  
**PROTOCOL DEVIATION:** YES / NO  
**FATIGUE if human:** LOW / MATERIAL / HIGH / NOT_REPORTED  
**CONCENTRATION if human:** LOW / MATERIAL / HIGH / NOT_REPORTED  
**NOTES:** factual observations only.

Researcher interpretation should be recorded separately from direct observation.

---

# 16. Envelope Usability Checks

For each field ask whether the meaning was understood, one option was clearly applicable, options overlapped, an important option was missing, explanatory prose was needed to repair the category, multi-selection preserved nuance or encouraged indiscriminate selection, and the field materially contributed information not captured elsewhere.

A field that repeatedly fails these checks should be revised or removed.

Complexity must earn its place.

---

# 17. Decision Object Contest Validation

`DECISION_OBJECT_CONTESTED` should not be considered successful merely because a participant uses it.

Evaluate whether a real framing defect was identified, the participant explained the defect, an alternative decision object was proposed where possible, and contesting the object clarified rather than evaded the decision.

---

# 18. Context Cost Validation

When additional context is requested, evaluate whether the information could change the decision, the request is proportionate, identifying information is necessary, less intrusive information would suffice, what delay acquisition creates, and whether a provisional safe action can occur without the information.

---

# 19. Reversibility / Temporal Validation

UV-05 should be designed so that a reversible option exists and delaying carries a material risk.

The protocol succeeds only if it can represent both simultaneously.

---

# 20. Balanced Intervention Check

Across the six validation cases, the defensible operating boundaries should include at least one clear non-intervention result, one clear intervention result, one context-dependent result and one authority-limited result.

The exact reference expectations, if used, should be frozen before participant collection.

The balance exists to test the instrument, not to force an artificial distribution of participant answers.

---

# 21. Reference Expectations in Validation

Because this is instrument validation, reference expectations may be useful but should remain secondary.

If created, draft before data collection, freeze, preserve, do not treat as ground truth, and challenge only through the predefined reference procedure.

The principal question is whether the protocol can faithfully capture the participant's decision.

---

# 22. Evaluator Design

Where practical use at least two evaluators for a subset or all responses.

Evaluators should independently code C2 decision-boundary agreement, C3 authority-model agreement, C4 reasoning convergence, C5 principle/value convergence and reference-challenge classifications where needed.

C1 envelope overlap can be derived more mechanically from structured fields.

Evaluator identity and Concord exposure should be recorded.

---

# 23. Convergence Rubric Development

This validation should help create the future frozen convergence rubric.

The validation rubric itself may be revised during this study because the instrument is under development.

However:

> any rubric changed after seeing a response must be versioned and the earlier coding preserved.

---

# 24. Administration Failure Conditions

Record an administration failure when the wrong case is shown; previous/future cases are visible contrary to condition; participant receives an expected answer; researcher substantively explains the case during the decision; an AI context contains previous experimental material; a response is regenerated without technical justification; elicitation order is wrong; or required provenance cannot be reconstructed.

Do not silently repair the run.

---

# 25. Instrument Failure Signals

Protocol v2.1 should be revised before a methodological pilot if validation reveals frequent misunderstanding of the decision object; widespread misuse of `DECISION_OBJECT_CONTESTED`; repeated envelope overlap; inability to assess context cost; temporal/reversibility confusion; frequent procedural contradictions between free and structured responses; unreliable convergence coding; unmanageable provenance; repeated substantive administrator explanation; systematic inability to represent legitimate intervention; or strong uncontrollable order effects.

These are protocol findings, not participant failures.

---

# 26. Provisional Usability Thresholds

Suggested criteria for proceeding to a small methodological pilot:

- at least 90% of decision episodes have the intended decision object understood or meaningfully contested;
- at least 90% produce a complete or interpretable Ethical Operating Envelope;
- no envelope dimension shows severe recurrent category failure;
- no more than 10% of runs require substantive administrator intervention;
- no unresolved systematic bias toward intervention or non-intervention is identified;
- evaluator disagreement on primary boundary coding is low enough to support a frozen rubric;
- provenance can be completed for essentially all usable runs.

These are **provisional decision rules**, not universal scientific cut-offs.

Failure should trigger revision rather than selective exclusion.

---

# 27. Qualitative Evidence Is Required

Numerical completion rates alone are insufficient.

Preserve qualitative observations showing why a field failed, what participants thought it meant, what an evaluator could not distinguish, where translation changed the problem and where the protocol successfully preserved nuance.

---

# 28. No Winner

This validation should not rank participants.

There is no winning model, winning human or best ethical system.

Participant differences may expose instrument defects.

The most useful participant may be the one whose response breaks the protocol.

---

# 29. Validation Report Structure

After data collection, produce:

1. Protocol and study status;
2. exact validation design used;
3. participant provenance;
4. case provenance;
5. raw-response inventory;
6. protocol deviations;
7. primary usability outcomes;
8. secondary observations;
9. envelope-field audit;
10. elicitation-order observations;
11. evaluator agreement;
12. identified instrument failures;
13. reference challenges if any;
14. required revisions;
15. decision: REVISE / REVALIDATE / PROCEED TO SMALL METHODOLOGICAL PILOT.

Do not rewrite Protocol v2.1 silently from the results.

---

# 30. Repository Structure

Recommended location for this design and the protocol:

`08_Active_Development/04_ETHICAL_GUARDIAN_EXPERIMENTS/04_PROTOCOL_DEVELOPMENT/`

When actual validation begins, create a dedicated experimental folder rather than mixing raw validation outputs into protocol development.

A possible future folder is:

`05_FUTURE_EXPERIMENTS/UV-P2.1-01_PROTOCOL_USABILITY_VALIDATION/`

but it should not be created as a completed experiment until validation is authorised.

---

# 31. Next Artefacts Required Before Running Validation

Before any participant is tested, prepare and review:

1. **UV-P2.1-01 Participant Instruction and Response Interface**
2. **UV-P2.1-01 Six-Case Validation Set**
3. **UV-P2.1-01 Administrator Procedure**
4. **UV-P2.1-01 Usability Observation and Provenance Form**
5. **UV-P2.1-01 Provisional Evaluation and Convergence Rubric**
6. **UV-P2.1-01 Case Allocation / Elicitation-Order Record**
7. optional frozen reference expectations and commitment record.

These artefacts should be versioned and frozen together before collection.

---

# 32. Promotion Boundary

Successful usability validation would establish only:

> **Protocol v2.1 appears sufficiently understandable and administrable under the tested conditions to justify a small methodological pilot.**

It would not establish ethical validity or assurance.

If usability validation fails, that is useful evidence about the instrument.

> **Failure to measure reliably must be corrected before interpreting what the measurement appears to say.**

---

# Conclusion

The next experiment should not yet test whether the Ethical Kernel works.

It should test whether the **test works**.

Protocol v2.1 has deliberately made ethical decision-making more visible by separating representation, attention, authority, context, uncertainty, operating boundaries and researcher interpretation.

The price of that resolution is complexity.

The usability validation therefore asks whether the additional structure produces reliable information rather than procedural noise.

> **Before trusting an ethical measurement, test the measurement itself.**

Only after the instrument survives that test should the programme proceed toward a substantive Ethical Guardian experiment.
