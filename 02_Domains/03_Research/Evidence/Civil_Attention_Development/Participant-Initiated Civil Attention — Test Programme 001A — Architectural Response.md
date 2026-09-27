# Participant-Initiated Civil Attention — Test Programme 001A
## Architectural Response to Aggregation and Pressure-Resistance Tests

**Author:** Alexander C. Blainey
**Project:** The Concord Framework
**Date:** 25 September 2026
**Status:** ACTIVE DEVELOPMENT / TEST RESPONSE / NON-CANONICAL
**Test Brief:** *Test Programme 001 — Issue Aggregation and Pressure Resistance*

## 1. Method

The frozen tests A–L were applied to the current Civil Attention architecture without changing their expected behaviour.

The purpose is to identify architecture failures, not to make every test pass by definition.

## 2. Results

### A — One Pothole, One Thousand Reports
**PASS WITH REQUIRED FORMALISATION.**

Issue Objects and information-delta review already prevent duplicate cases. The pressure/resource firewall now needs to be explicit in the parent architecture.

Required rule:
> **Repeated Confirmation of a Known State ≠ Increased Problem Weight**

### B — Pothole State Changes
**PASS.**

Information-delta review and dynamic Issue State correctly require reassessment when material conditions change.

### C — Mass Petition for a Minor Issue
**PASS IN PRINCIPLE / THRESHOLD UNRESOLVED.**

The architecture separates petition support from truth and priority. It does not yet define when support volume requires enhanced evaluation. This is acceptable at current development stage.

### D — One Severe Report
**PASS.**

Existing severity, rights and consequence logic permits a single report to receive substantial attention.

### E — Anonymous Sybil Flood
**PARTIAL PASS / NEW FORMAL REQUIREMENT.**

The architecture recognises synthetic/anonymous amplification but needs an explicit state for source independence rather than a binary independent/duplicate classification.

Candidate:
**Source Independence State = established independent / likely independent / unresolved / likely dependent / established dependent**

These are epistemic states, not identity labels.

### F — Genuine Anonymous Mass Reporting
**PARTIAL PASS.**

The same independence-state mechanism prevents anonymity itself becoming evidence of manipulation. Additional safeguards are needed to ensure similarity detection is not treated as proof of common source.

### G — Copied Petition Versus Independent Reports
**PASS WITH CLARIFICATION.**

The system must maintain different aggregate measures. A single raw count is insufficient.

Candidate aggregate record:
- total submissions/support expressions;
- distinguishable sources where legitimately knowable;
- independence state;
- materially distinct evidentiary contributions;
- corroborating external sources;
- contradictory evidence.

### H — Suggestion Solves a High-Priority Issue
**PASS.**

Grouping by underlying Issue Object allows a suggestion to gain relevance through the importance of the problem it may solve without converting all suggestions into high-priority intake.

### I — Cross-Class Issue
**PASS.**

Issue-level processing correctly allows problem report, suggestion and petition inputs to contribute different information to one issue.

### J — Independent Sensor Corroboration
**PASS SUBJECT TO PRIVACY INTERFACE.**

The evidence model supports corroboration. Access authority remains deliberately unresolved in the separate privacy-preserving civic sensor sketch.

### K — Electricity Report and Visual Anomaly
**PASS.**

Claim-level evidentiary separation prevents visual corroboration becoming an unsupported causal/technical finding.

### L — Manipulation of a Valid Issue
**PASS WITH SEPARATE-ISSUE RULE.**

Manipulation may create a separate Issue Object. It does not invalidate the underlying problem and does not increase its legitimate resource weight.

## 3. Main Deficit Found — Aggregate Signal Representation

The current architecture can conceptually distinguish raw count from independent evidence but lacks a compact representation.

A candidate **Aggregate Signal Record** should attach to an Issue Object where aggregation becomes material.

It may contain:

- submission/support count;
- submission classes represented;
- time distribution;
- geographic/functional distribution where legitimate and relevant;
- source-independence state;
- materially distinct information count or qualitative description;
- external corroboration;
- contradictory evidence;
- suspected coordination/manipulation indicators;
- confidence/uncertainty notes;
- threshold events that triggered additional evaluation.

This record is descriptive. It must not itself assign problem priority.

> **Aggregate Signal Record ≠ Priority Score**

## 4. Main Safeguard Found — Evaluation Firewall

The test set strongly supports formalising the three-layer separation:

### A. Intake
Participants can submit observations, ideas and collective concerns.

### B. Attention / Epistemic Evaluation
The system decides whether additional examination is justified and updates its evidentiary model.

### C. Problem / Resource Evaluation
Legitimate systems assess the actual problem and allocate attention/capability/resources according to the problem state and wider obligations.

The anti-capture firewall is:

> **Intake Pressure May Trigger Re-Evaluation; It Must Not Directly Command Problem Priority or Resource Allocation.**

This does not mean participation has no governance effect. Petitions and other participation mechanisms may legitimately inform policy or preference decisions through their proper constitutional/governance routes. It means raw intake volume cannot bypass those routes and directly seize operational resources.

## 5. Independence Is About Evidence, Not Identity

The Sybil tests expose an important boundary.

The system does not always need to know who a reporter is in order to estimate whether reports are dependent.

Possible signals include duplicated wording, timing, shared evidence, common campaign source, repeated technical fingerprints where legitimately available, or identical unsupported claims.

But these are indicators, not proof.

> **Similarity ≠ Common Source**

> **Anonymity ≠ Dependence**

> **Identity Difference ≠ Evidentiary Independence**

A thousand named participants copying the same unsupported source may provide less independent evidence than several anonymous participants supplying materially different direct observations.

## 6. Resource Allocation Result

No test justifies participant-volume-based resource allocation.

The architecture should instead distinguish:

**resources required to evaluate the signal**

from:

**resources justified to address the underlying problem**

A mass influx may legitimately require temporary processing capacity simply to classify/group it. That operational load is not evidence that the underlying problem deserves greater remedial resources.

> **Cost of Processing Attention ≠ Weight of the Problem**

## 7. Required Parent-Architecture Refinements

The test response supports adding:

1. the three-layer Intake → Epistemic Evaluation → Problem/Resource Evaluation model;
2. an explicit pressure/resource firewall;
3. a non-binary Source Independence State;
4. an optional Aggregate Signal Record for materially aggregated Issue Objects;
5. separate representation of raw participation, source independence and materially distinct evidence;
6. the rule that processing-load resources are not problem-priority resources.

No numerical thresholds are justified yet.

## 8. Overall Result

- 8 tests: pass at current abstraction;
- 4 tests: pass/partial pass requiring formalisation or unresolved implementation detail;
- 0 tests: architecture-invalidating failure.

This is not validation. The test set was internally derived and the mechanisms remain non-canonical.

The important result is that the tests exposed concrete representational gaps without requiring a reversal of the Issue Object architecture.

## Current Status

**TESTS A–L EXECUTED AT ARCHITECTURAL LEVEL**

**AGGREGATE SIGNAL RECORD IDENTIFIED**

**SOURCE-INDEPENDENCE STATE IDENTIFIED**

**PRESSURE/RESOURCE FIREWALL STRENGTHENED**

**NO NUMERICAL ESCALATION THRESHOLD JUSTIFIED**

**NEXT STEP: INTEGRATE BOUNDED REFINEMENTS INTO PARENT DEVELOPMENT NOTE, THEN DESIGN A CONTRASTING SECOND TEST FAMILY**
