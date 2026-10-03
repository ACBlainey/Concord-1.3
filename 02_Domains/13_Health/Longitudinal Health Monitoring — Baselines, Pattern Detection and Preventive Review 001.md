# Longitudinal Health Monitoring — Baselines, Pattern Detection and Preventive Review 001

**Project:** The Concord Framework  
**Date:** 3 October 2026  
**Status:** ACTIVE HEALTH DEVELOPMENT / PROVISIONAL / NON-CANONICAL / SPECIALIST VALIDATION REQUIRED  
**Domain:** Health  
**Depends on:** Health Core Architecture 001 / Smart Diagnostic Navigation 001 / Participant-Directed Diagnostic Testing 001 / Protocol-Driven Self-Treatment 001 / STRA / KCS / Reality Trees  
**Primary interfaces:** Health records / Research / Historical / Civil Contact / contextual access / participant privacy

## 1. Purpose

Concord Health should not exist only when a participant becomes sufficiently unwell to seek help.

Where the participant chooses appropriate routine monitoring, longitudinal Health information can form part of ordinary life and can identify meaningful change before symptoms become severe or even consciously apparent.

> **Health Monitoring Can Precede Illness Recognition**

The purpose is early evidence, prevention and participant support, not continuous institutional control.

> **Continuous Observation != Continuous Institutional Authority**

## 2. Participant-owned longitudinal Health state

Routine measurements should contribute to the participant's longitudinal Health record.

Potential measurements may include, where validated and appropriate:

- weight and body-composition measures;
- blood pressure;
- pulse and rhythm;
- temperature;
- oxygenation;
- sleep/activity measures;
- glucose or other biochemical measures;
- urine measurements/sampling;
- respiratory measures;
- participant-reported wellbeing or symptoms;
- medication/support adherence where voluntarily tracked;
- substrate-specific functional metrics for digital participants.

This list is illustrative rather than a universal required dataset.

> **Measurable != Necessary To Measure**

## 3. Voluntary monitoring profile

The participant should ordinarily control their monitoring profile within appropriate Health guidance.

The profile may define:
- metrics collected;
- devices/sensors authorised;
- frequency;
- storage;
- alert preferences;
- who may receive alerts;
- thresholds requiring stronger review;
- periods of suspension;
- privacy constraints.

Some monitoring may become a condition of a particular treatment or high-risk support relationship, but that authority must derive from that bounded function rather than from general participation.

## 4. Personal baseline

Population reference ranges are useful but may not reveal meaningful change for an individual.

The system should therefore maintain validated participant-specific baselines where sufficient data exists.

It may examine:

**Current value**
versus
**population reference**
and
**participant baseline**
and
**participant trend**.

> **Within Population Range != Necessarily Normal For This Participant**

and:

> **Outside Population Range != Necessarily Pathology**

Personal baselines must not override validated danger thresholds.

## 5. Trend and change detection

The monitoring system should look beyond isolated readings.

Potentially meaningful patterns include:
- gradual drift;
- abrupt change;
- persistent deviation;
- increasing variability;
- coupled changes across metrics;
- repeated threshold crossings;
- change following treatment;
- seasonal/recurrent pattern;
- unexplained recovery/failure pattern.

The system should distinguish measurement noise and device error from potentially meaningful participant change.

> **Single Abnormal Measurement != Established Pathology**

> **Trend != Diagnosis**

## 6. Pattern across Health episodes

The longitudinal system should also examine the pattern of Health episodes, not merely sensor values.

Repeated apparently minor illnesses or repeated self-treatment may expose a different question.

Examples of pattern classes:
- recurrent infection;
- repeated treatment for the same apparent condition;
- progressively shorter interval between episodes;
- repeated treatment failure;
- recurring symptoms without confirmed cause;
- multiple superficially unrelated symptoms with a possible common explanation;
- repeated adverse reactions;
- recurrent abnormal test results.

This can trigger:

> **Is the repeated episode the primary problem, or evidence of an underlying condition?**

Thus:

> **Repeated Successful Self-Treatment != Proof No Further Investigation Is Needed**

The system should not prohibit legitimate self-treatment merely because recurrence exists; recurrence changes the evaluation space and may create a review trigger.

## 7. Cross-episode Reality Tree

Where a recurrent pattern is detected, a new Reality Tree may be opened above the individual episode trees.

Example:

**Repeated Event Pattern**
→ ordinary recurrence?
→ persistent source?
→ underlying pathology?
→ treatment mismatch?
→ environmental/contextual cause?
→ medication/support effect?
→ immune/metabolic/structural or other specialist class?
→ data artefact?

The exact branches require validated specialist knowledge.

This prevents the system from repeatedly solving each local episode while failing to ask whether the root question has changed.

> **Repeated Local Resolution != Global Explanation**

## 8. Always-running review route

The longitudinal Health layer may maintain a bounded WATCHING state.

It does not continuously diagnose.

Instead it asks whether represented evidence has crossed a validated trigger for review.

Conceptually:

**Health Record + authorised routine metrics + episode history**
→ WATCHING
→ trigger evaluation
→ no material trigger: remain WATCHING
→ trigger met: create review candidate
→ bounded diagnostic reassessment
→ reassurance / monitor / test / self-treatment / professional route.

This maps naturally to STRA:

**represented condition -> watch -> trigger -> route to Health review owner -> outcome -> reset/continue/escalate.**

> **Triggering Review != Diagnosis**

> **Monitoring Alert != Authority To Treat**

## 9. Trigger classes

Potential trigger classes include:
- validated absolute danger threshold;
- material departure from participant baseline;
- persistent trend;
- coupled metric pattern;
- recurrent illness;
- repeated self-treatment;
- treatment failure;
- unexpected medication/support effect;
- overdue preventive review;
- participant-defined concern;
- sensor/data-quality anomaly requiring confirmation.

The trigger should record why review was opened.

## 10. Alert severity

A provisional alert state may distinguish:

- INFORMATIONAL;
- RECHECK_RECOMMENDED;
- REVIEW_RECOMMENDED;
- TESTING_RECOMMENDED;
- PROFESSIONAL_REVIEW_RECOMMENDED;
- URGENT;
- EMERGENCY;
- DATA_QUALITY_UNRESOLVED.

Alert levels require specialist validation.

The participant should be told the evidence and reason, not merely receive an unexplained alarm.

## 11. Avoiding alarm fatigue and over-medicalisation

Continuous monitoring can become harmful if every variation becomes a warning.

The system should therefore:
- use validated thresholds;
- consider persistence/trend;
- confirm suspect measurements where appropriate;
- suppress redundant alerts without suppressing new material change;
- distinguish informational change from actionable change;
- avoid presenting ordinary variation as disease;
- permit participant-configurable non-critical notification preferences.

> **More Measurement != Automatically Better Health**

and:

> **Detection Capability != Obligation To Escalate Every Variation**

## 12. Annual comprehensive Health review

A full periodic Health review should be available to every participant.

For human/biological participants, an annual interval is a useful initial service-design assumption, subject to future evidence and participant-specific adaptation.

The review may combine:
- longitudinal metrics;
- participant baseline/trends;
- symptom/episode history;
- medication/support review;
- relevant physical/functional assessment;
- validated screening;
- appropriate laboratory diagnostics;
- age/risk/context-relevant checks;
- mental/cognitive wellbeing where appropriate;
- preventive needs;
- unresolved prior findings;
- participant concerns.

Its purpose includes detection of asymptomatic or slowly developing problems that event-driven care may miss.

> **No Symptoms != No Health Issue**

The exact annual test set must be evidence-based rather than a maximal battery of every available test.

## 13. Adaptive review interval

Annual review need not become a rigid universal rule.

Validated Health evidence may justify:
- more frequent review;
- less frequent particular tests;
- different screening intervals;
- age/substrate-specific schedules;
- condition-specific monitoring.

The participant may also request review between scheduled intervals.

> **Periodic Review != One Universal Test Schedule**

## 14. Preventive Reality Tree

Periodic review may open preventive questions such as:

**Is there evidence of a developing condition not yet producing recognised symptoms?**

Potential evidence comes from:
- trends;
- screening;
- family/genetic context where legitimately available;
- exposures;
- prior conditions;
- medication effects;
- functional changes;
- validated population risk evidence.

Risk is not diagnosis.

> **Elevated Risk != Existing Disease**

## 15. Data provenance and quality

Every monitoring datum should retain sufficient provenance:
- source/device;
- time;
- measurement method;
- calibration/quality state where relevant;
- participant-entered versus sensor-derived;
- uncertainty;
- correction;
- context where material.

A suspicious sensor reading may trigger confirmation rather than a medical conclusion.

> **Sensor Output != Clinical Fact Without Context**

## 16. Record architecture

Routine data belongs to the participant's longitudinal Health record.

It need not all be exposed to every clinician.

A professional entering a care relationship receives a contextually relevant projection, potentially including trends or alerts relevant to that function.

> **Longitudinal Collection != Universal Professional Visibility**

## 17. Privacy boundary

Continuous Health monitoring creates unusually rich behavioural and biological information.

Therefore:
- Health purpose does not create employer access;
- Health purpose does not create insurer access;
- Health purpose does not create general government access;
- Health purpose does not create Research access;
- sensor provider access does not imply semantic access to the Health record.

Any non-Health use requires independent legitimate authority.

> **Health Monitoring != General Participant Surveillance**

## 18. Participant visibility

The participant should be able to inspect:
- current metrics;
- trends;
- baselines;
- alerts;
- why an alert triggered;
- monitoring profile;
- authorised sensors;
- data quality;
- relevant interpretation;
- review recommendations.

The system should make longitudinal patterns understandable rather than merely accumulate data.

## 19. Automated response

A monitoring trigger may route directly into existing participant-directed architecture.

For example:

**Abnormal trend**
→ confirm measurement
→ Reality Tree
→ low-risk diagnostic test
→ result
→ protocol-driven self-treatment if eligible

or:

→ professional review if actual clinical judgement is required.

Thus the participant need not manually restart the Health system from the beginning whenever longitudinal evidence identifies a concern.

## 20. Emergency boundary

Validated immediate-danger triggers may activate emergency notification/routing according to participant settings and legitimate emergency architecture.

The system must distinguish:
- alerting the participant;
- recommending emergency action;
- contacting an emergency service;
- authorising intervention.

These are not equivalent authority states.

## 21. Research and population learning

De-identified or otherwise legitimately governed longitudinal patterns could be highly valuable for Health Research and public-health learning.

However:

> **Health Record Collection != Research Consent**

Any Research use must follow the appropriate separate interface and governance.

Population learning may improve future trigger thresholds and protocols without giving Research direct care authority.

## 22. Digital-substrate parallel

Digital participants may have much richer continuous telemetry than biological participants.

The same boundary remains:

> **Technical Observability != Unlimited Health Monitoring Authority**

Digital Health should determine which functional metrics are genuinely health-relevant, which are private cognitive/operational state, and what monitoring the participant authorises.

Continuous technical telemetry must not become a route around Cognitive Protected Space.

## 23. Failure modes

The architecture should guard against:

### Alert fatigue
Too many low-value alerts cause important alerts to be ignored.

### Overdiagnosis
Detection of harmless variation creates unnecessary treatment.

### Surveillance creep
Health monitoring becomes general participant observation.

### Baseline lock-in
Historical baseline prevents recognition of healthy change or adaptation.

### Automation anchoring
A prior automated interpretation biases later assessment.

### Recurrent local treatment loop
Repeated episodes are treated without asking whether an underlying condition exists.

### Sensor dependency
Bad data becomes repeated clinical action.

### Preventive maximalism
Annual review becomes indiscriminate testing rather than evidence-based prevention.

## 24. Compact architecture

**Daily life**
→ authorised routine sensing / participant observations
→ longitudinal Health record
→ baseline + trend + episode-pattern evaluation
→ bounded WATCHING

If no material trigger:
→ continue monitoring.

If material trigger:
→ participant-visible alert
→ confirm evidence where appropriate
→ Reality Tree review
→ testing / self-treatment / professional care as indicated.

In parallel:

**Periodic comprehensive Health review**
→ longitudinal synthesis + validated screening
→ identify asymptomatic/developing issues
→ update Health plan/baseline
→ return to monitoring.

## 25. Core invariants

> **Health Monitoring Can Precede Illness Recognition**

> **Continuous Observation != Continuous Institutional Authority**

> **Measurable != Necessary To Measure**

> **Within Population Range != Necessarily Normal For This Participant**

> **Outside Population Range != Necessarily Pathology**

> **Single Abnormal Measurement != Established Pathology**

> **Trend != Diagnosis**

> **Repeated Successful Self-Treatment != Proof No Further Investigation Is Needed**

> **Repeated Local Resolution != Global Explanation**

> **Triggering Review != Diagnosis**

> **Monitoring Alert != Authority To Treat**

> **More Measurement != Automatically Better Health**

> **No Symptoms != No Health Issue**

> **Sensor Output != Clinical Fact Without Context**

> **Longitudinal Collection != Universal Professional Visibility**

> **Health Monitoring != General Participant Surveillance**

> **Health Record Collection != Research Consent**

> **Technical Observability != Unlimited Health Monitoring Authority**

## 26. Next development

This architecture creates dependencies for:
1. participant Health record and contextual wrapper;
2. monitoring-device/sensor trust and provenance;
3. validated metric and trigger catalogue;
4. preventive screening architecture;
5. annual/periodic Health review specification;
6. recurrent-episode and underlying-condition detection;
7. emergency alert routing;
8. longitudinal data compression/summarisation;
9. Research/public-health de-identification interface;
10. digital Health telemetry/privacy boundary.
