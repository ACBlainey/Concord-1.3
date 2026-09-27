# Participant-Initiated Civil Attention — Test Programme 002A
## Architectural Response to Institutional Failure and Escalation Tests

**Author:** Alexander C. Blainey
**Project:** The Concord Framework
**Date:** 25 September 2026
**Status:** ACTIVE DEVELOPMENT / TEST RESPONSE / NON-CANONICAL
**Test Brief:** *Test Programme 002 — Institutional Failure, Capture and Legitimate Escalation*

## 1. Result Summary

The current architecture survives the core pressure-versus-priority challenge, but the second test family exposes a missing explicit representation of **civil response state**.

A system can correctly understand a problem yet fail to act on it. Repeated participant reports may therefore contain no new information about the pothole, misconduct or outage while still providing evidence that the civil response is failing.

This cannot be represented adequately by Problem State alone.

## 2. Test Results

### A — Incorrect Traffic Model
**PASS.**
Reports containing a material challenge to the traffic assumption are information delta, not mere duplicates. Priority changes only if the underlying state/model is corrected.

### B — Persistent Failure
**PARTIAL PASS / ARCHITECTURAL GAP.**
The architecture needs explicit Response State. Failure to execute a legitimate disposition may itself become a linked Issue Object.

### C — Implicated Institution
**PASS IN PRINCIPLE.**
Existing conflict/oversight/judicial interfaces provide a route conceptually, but exact authority remains source-system owned.

### D — Classification Suppression
**PASS WITH REQUIRED CHALLENGE RECORD.**
Classification reviewability exists. A challenge should identify the contested processing decision and its disposition so repeated review is not merely informal.

### E — Correct Decision, Persistent Disagreement
**PASS.**
Unchanged support does not require endless reinvestigation. Material new evidence or changed conditions can reopen.

### F — Minority Against Majority
**PASS.**
Petition preference and severe-harm evidence remain separate. Raw majority volume does not override the harm assessment.

### G — Manipulation Allegation as Suppression
**PASS WITH CLARIFICATION.**
Source dependence remains an epistemic assessment. Suspected manipulation cannot itself invalidate the underlying issue.

### H — Genuine Emergency
**PASS IN PRINCIPLE.**
Urgency comes from changed problem state. The Civil Attention layer should trigger the established emergency/safety route rather than create emergency authority itself.

### I — Resource Constraint
**PASS IN PRINCIPLE.**
Resource scarcity remains a separate allocation problem. Civil Attention must preserve visibility of legitimate deferred issues.

### J — False Confidence From Metrics
**PASS.**
Disagreement between internal metrics and distributed observations is itself an epistemic signal requiring examination.

### K — Reopening Abuse
**PASS WITH FORMALISATION.**
Issue matching plus information-delta review prevents endless fresh cases. Reopening should require a legitimate review condition or material delta rather than raw repetition.

### L — Captured Oversight
**PASS IN PRINCIPLE / SOURCE RESOLUTION REQUIRED FOR FINAL ROUTE.**
The architecture correctly rejects infallible single-review assumptions. Exact higher-order routes belong to existing oversight/judiciary/constitutional architecture.

## 3. New Required Object — Response State

An Issue Object should distinguish:

### Problem State
Current best-supported representation of the underlying external issue.

### Response State
Current representation of civil processing/action concerning that issue.

Candidate Response State information includes:
- responsible function;
- current disposition;
- action promised/required;
- action completed;
- last material action;
- next review condition;
- dependencies;
- legitimate delay/resource constraint;
- missed condition/deadline where applicable;
- implementation failure;
- escalation state.

> **Problem-State Stability ≠ Response-State Adequacy**

This prevents duplicate reports from artificially increasing problem weight while still allowing persistent non-response to become visible.

## 4. Challenge Object

A participant challenge should not require a new copy of the entire underlying case.

A lightweight **Challenge Object** can point to:
- the Issue Object;
- the processing decision/assumption contested;
- stated reason;
- any new evidence;
- review owner;
- disposition;
- resulting change, if any.

Examples:
- wrong classification;
- stale traffic data;
- ignored evidence;
- conflict of interest;
- failure to implement;
- changed circumstances.

> **Challenge Object ≠ New Issue by Default**

If examination reveals a distinct institutional failure, it may create a linked Issue Object.

## 5. Reviewability Without Endless Reprocessing

A legitimate system needs both finality and corrigibility.

Candidate rule:

> **Unchanged Repetition → Attach / Preserve / No Automatic Full Re-Examination**

while:

> **Material Information Delta or Legitimate Review Ground → Re-Evaluation**

This prevents both spam-driven reopening and institutional immunity.

## 6. Response Failure as a New Issue

Some failures concern the response mechanism itself.

Example:

**Pothole Issue A** is correctly assessed and scheduled.

If the repair process repeatedly fails, this does not necessarily make the pothole intrinsically more severe. It may create:

**Issue B — Maintenance Execution Failure**

linked to Issue A.

This preserves causal clarity:
- A = road defect;
- B = institutional/process failure.

Issue B may affect many other cases and reveal a systemic defect.

## 7. Escalation Is Functional, Not Emotional

Escalation should not mean “the participant remains unhappy.”

It should identify a legitimate reason why another function or review level is needed.

Candidate grounds remain:
- material new evidence;
- classification challenge;
- conflict;
- rights/safety implications;
- implementation failure;
- stale system information;
- missed review condition;
- jurisdictional failure;
- institutional capture evidence;
- unresolved cross-owner responsibility.

This list requires later source resolution before any constitutional or operational status.

## 8. Revised Firewall

Test Programmes 001 and 002 together produce a balanced architecture:

> **Participants Can Trigger Attention; They Cannot Manufacture Priority.**

and:

> **Institutions Can Assess Priority; They Cannot Manufacture Finality.**

The bridge is reviewability:

> **Reviewability Is the Counterweight to Pressure Resistance.**

## 9. Overall Result

- 7 tests pass at the present abstraction;
- 5 pass/partial pass with formalisation or source-owned implementation unresolved;
- 0 architecture-invalidating failures.

The significant discovery is not a new priority mechanism. It is the need to represent **Response State** separately from **Problem State**, plus a lightweight Challenge Object.

## Current Status

**TESTS A–L EXECUTED**

**RESPONSE STATE IDENTIFIED AS DISTINCT ISSUE DATA**

**CHALLENGE OBJECT IDENTIFIED**

**REOPENING / REPROCESSING BOUNDARY STRENGTHENED**

**PRESSURE-RESISTANCE FIREWALL BALANCED BY REVIEWABILITY**

**NEXT STEP: INTEGRATE BOUNDED FINDINGS INTO PARENT DEVELOPMENT NOTE**
