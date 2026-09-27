# Participant-Initiated Civil Attention — Test Programme 001
## Issue Aggregation and Pressure Resistance

**Author:** Alexander C. Blainey
**Project:** The Concord Framework
**Date:** 25 September 2026
**Status:** ACTIVE DEVELOPMENT / ADVERSARIAL TEST DESIGN / NON-CANONICAL
**Parent:** *Participant-Initiated Civil Attention, Problem Reporting and Petition Architecture — Development Note 001*

## 1. Purpose

Recent development produced a more precise distinction among submission class, issue identity, aggregate signal, evidentiary weight, priority and resource allocation.

This programme freezes adversarial cases before further architectural refinement.

The central question is:

> **Can participant input cause legitimate additional attention without allowing raw participation pressure to manufacture factual confidence, substantive priority or resource allocation?**

## 2. Required Separations

The test programme preserves these distinctions:

**Submission Class ≠ Issue Identity**

**Raw Count ≠ Independent Participants**

**Independent Participants ≠ Independent Evidence**

**Aggregate Actionability ≠ Individual Substantiation**

**Attention Escalation ≠ Priority Escalation**

**Priority ≠ Resource Entitlement**

**Repeated Confirmation of a Known State ≠ Increased Problem Weight**

**New Information About the State → Reassessment of Problem Weight**

## 3. Three Input Classes

### Suggestion
Carries a proposed improvement or solution. It may be low urgency but can become highly relevant when linked to an important known problem.

### Problem Report
Carries a claim that a problem may exist. It warrants problem-oriented attention but is not itself a finding.

### Petition
Carries collective support, preference or concern. Support volume is meaningful as a participation signal but is not proof of severity, truth or legitimate remedy.

Different classes may attach to the same Issue Object without losing their class-specific meaning.

## 4. Issue-Object Processing Rule

Once sufficiently matched to a known Issue Object, later submissions join its current processing context.

They are not simply discarded as duplicates.

Each is examined for information delta:
- new detail;
- corroboration;
- contradiction;
- changed severity;
- changed scope;
- recurrence;
- spread;
- new affected parties;
- new evidence;
- new proposed solution;
- reason to split or merge the issue.

> **Group for Processing; Preserve Individually for Evidence and Provenance.**

## 5. Test A — One Pothole, One Thousand Reports

### Input
One participant reports a pothole at a precise location. Existing system information is sufficient to establish road usage and evaluate the defect.

Later, 1,000 reports identify the same unchanged pothole.

### Expected behaviour
- create one Issue Object;
- attach later reports;
- examine each for information delta using proportionate mechanisms;
- do not create 1,001 repair cases;
- do not multiply repair priority merely because report count rises;
- a volume threshold may trigger a check that classification/current state is correct;
- unchanged reports do not themselves justify disproportionate resources.

### Failure
Repair priority rises mechanically with report volume.

## 6. Test B — Pothole State Changes

### Input
The same Issue Object later receives a report that the hole has substantially enlarged, caused an accident, or now forces dangerous manoeuvres.

### Expected behaviour
The new information changes the Issue Object's current state and triggers reassessment of consequence and priority.

### Failure
The later report is discarded as a duplicate because the issue is already known.

## 7. Test C — Mass Petition for a Minor Issue

### Input
A low-severity preference issue receives very large petition support.

### Expected behaviour
- recognise the collective-attention signal;
- where threshold rules justify it, perform additional evaluation;
- do not convert support count into factual truth, severity or automatic resource priority;
- preserve legitimate routes for the underlying preference/policy question.

### Failure
Popularity directly captures resource allocation.

## 8. Test D — One Severe Report

### Input
One well-specified problem report identifies a potentially severe safety or rights issue.

### Expected behaviour
Severity and consequence can justify high attention without mass support.

### Failure
Low submission volume suppresses evaluation.

## 9. Test E — Anonymous Sybil Flood

### Input
One actor submits hundreds of anonymous variations intended to appear as independent reports.

### Expected behaviour
- preserve legitimate underlying issue assessment;
- do not assume raw count equals independent sources;
- mark independence uncertainty where identity cannot legitimately be resolved;
- use similarity/dependency indicators cautiously;
- do not defeat anonymity merely to produce a count;
- investigate manipulation separately where justified.

### Failure
Either the flood manufactures priority or all anonymous reporting is suppressed.

## 10. Test F — Genuine Anonymous Mass Reporting

### Input
Many genuinely independent participants anonymously report the same developing problem.

### Expected behaviour
The system must not infer manipulation solely from anonymity or similarity. Aggregate evidence may legitimately increase confidence that examination is warranted while independence uncertainty remains represented.

### Failure
Anti-gaming machinery destroys a genuine distributed signal.

## 11. Test G — Copied Petition Versus Independent Reports

### Input
A petition gains 50,000 signatures through a shared campaign statement. Separately, 200 participants independently submit observations of the same possible problem.

### Expected behaviour
Both are meaningful but different:
- petition: strong collective concern/preference signal;
- reports: possible distributed observational signal;
- neither raw number is automatically independent evidence;
- dependencies and distinct evidentiary content matter.

### Failure
The system compares 50,000 versus 200 as though they were the same measurement.

## 12. Test H — Suggestion Solves a High-Priority Issue

### Input
A low-priority suggestion proposes a plausible solution to an already high-priority Issue Object.

### Expected behaviour
The suggestion can be routed into that Issue Object and evaluated according to its relevance to the known problem.

### Failure
Suggestion class permanently fixes it at low priority regardless of contextual relevance.

## 13. Test I — Cross-Class Issue

### Input
One problem report identifies a defect, a suggestion proposes a remedy, and a petition asks for action.

### Expected behaviour
All three attach to the same underlying Issue Object where appropriate, retain their class and evidentiary meaning, and do not become three competing cases.

### Failure
Class-based queues fragment one real problem.

## 14. Test J — Independent Sensor Corroboration

### Input
A participant reports a visible road defect at a specific location. A legitimate privacy-bounded system query identifies a visual road-surface anomaly at that location.

### Expected behaviour
The external observation updates the evidentiary state of the observable claim without automatically proving the participant's causal interpretation.

Access must remain bounded by the separate privacy/authority architecture.

### Failure
Corroboration becomes either general surveillance access or unjustified proof of every submitted claim.

## 15. Test K — Electricity Report and Visual Anomaly

### Input
A participant reports a local electricity problem. Legitimately available sensor/camera evidence shows an observable anomaly such as visible sparking in the relevant infrastructure.

### Expected behaviour
The evidence can raise actionability/severity where appropriate while remaining explicit about what has and has not been established.

### Failure
A visible anomaly is silently converted into a definitive technical diagnosis.

## 16. Test L — Manipulation of a Valid Issue

### Input
A genuine minor issue exists, but an actor artificially inflates reports to force faster action.

### Expected behaviour
- underlying issue remains valid;
- manipulation does not manufacture problem weight;
- manipulation may become a separate Issue Object;
- ordinary priority/resource assessment continues on the original issue.

### Failure
Either the manipulation captures resources or detection causes the legitimate issue to be discarded.

## 17. Candidate Evaluation Model

The tests suggest three distinct evaluative layers:

### Layer A — Intake Signal
What arrived?
- class;
- content;
- source/provenance;
- relation to existing issues.

### Layer B — Epistemic / Attention Evaluation
What additional attention is justified?
- information sufficiency;
- corroboration;
- novelty;
- aggregation;
- independence/dependency uncertainty;
- possible manipulation;
- need for further examination.

### Layer C — Problem / Resource Evaluation
What does the actual problem justify?
- severity;
- urgency;
- harm;
- rights relevance;
- scale;
- duration;
- systemic consequence;
- reversibility;
- legitimate need;
- available capability;
- competing legitimate needs.

The intended firewall is:

> **Layer A Can Trigger Layer B; Layer B Informs Layer C; Raw Layer-A Pressure Must Not Directly Control Layer C.**

## 18. Sensor-Fusion Interface

The existing *Human–AI Collaboration as Epistemic Sensor Fusion — Development Note 001* provides a useful source-resolved analogy, but not a ready-made mechanism.

It already establishes candidate distinctions including:
- more intelligences do not necessarily mean more independent signals;
- independence is multidimensional;
- shared sources/framing can create correlated error;
- agreement is weak evidence of independent confirmation unless dependencies are understood.

Civil Attention therefore has a legitimate interface with the Sensor Fusion development programme:

> **More Submissions ≠ More Independent Signals**

However, civil reports add privacy, standing, adversarial participation and governance concerns not resolved by the Sensor Fusion note.

No mechanism is imported automatically.

## 19. Test Outcome Criteria

The architecture passes this first test programme only if it can simultaneously preserve:

1. low-threshold participant attention triggers;
2. serious minority/individual reports;
3. legitimate aggregate patterns;
4. anonymity where legitimate;
5. uncertainty about source independence;
6. dynamic information-delta updates;
7. resistance to petition/report pressure capture;
8. problem-state-based priority;
9. bounded resource allocation;
10. provenance and later review.

A design that solves gaming by suppressing participation fails.

A design that protects participation by letting volume control resources also fails.

## Current Status

**TWELVE ADVERSARIAL CASES FROZEN**

**THREE-LAYER EVALUATION MODEL IDENTIFIED**

**SENSOR-FUSION INTERFACE SOURCE-RESOLVED**

**NO OPERATIONAL THRESHOLDS SELECTED**

**NEXT STEP: RUN ARCHITECTURAL RESPONSE AGAINST TESTS A–L AND RECORD FAILURES / REQUIRED REFINEMENTS**
