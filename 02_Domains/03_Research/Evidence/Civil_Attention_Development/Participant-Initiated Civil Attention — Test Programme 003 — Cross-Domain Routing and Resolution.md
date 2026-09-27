# Participant-Initiated Civil Attention — Test Programme 003
## Cross-Domain Routing and Resolution

**Author:** Alexander C. Blainey
**Project:** The Concord Framework
**Date:** 25 September 2026
**Status:** ACTIVE DEVELOPMENT / ADVERSARIAL TEST / NON-CANONICAL
**Frozen Specification:** *Candidate Architecture Specification 001 — Common Intake, Domain Processing and Resolution Oversight*

## 1. Test Rule

The frozen specification is tested without silently adding mechanisms to make individual cases pass.

The target is the structural claim:

> **Centralise Intake, Provenance, Routing Visibility, Resolution Status and Feedback; Distribute Legitimate Domain-Specific Examination, Decision and Action.**

## 2. Case Results

### T1 — Wrong Initial Domain
**PASS WITH REROUTING REQUIREMENT.**

A receiving domain must be able to return **outside authority / transfer recommended** without closing the parent Issue Object. The central record preserves the original route and subsequent transfer.

### T2 — Two Legitimate Domains
**PASS.**

Two Domain Action Objects can coexist under one Issue Object. Neither domain's completion automatically closes the parent.

### T3 — Five Legitimate Domains
**PASS WITH COORDINATION GAP.**

The model scales structurally, but five parallel owners expose the need to distinguish independent parallel actions from actions with cross-domain dependencies.

### T4 — No Domain Accepts Responsibility
**PARTIAL PASS / GAP.**

The Resolution Oversight function can detect this state, but the frozen specification does not yet define a formal **Unowned Issue** state or responsibility-resolution procedure.

### T5 — Two Domains Claim the Other Owns It
**PARTIAL PASS / GAP.**

Transfer visibility detects the dispute, but a responsibility conflict must not become an endless transfer loop. A bounded ownership-resolution/escalation mechanism is required.

### T6 — Domain Silently Stops Processing
**PASS WITH STALENESS REQUIREMENT.**

Response State plus last material action/next review condition makes silence detectable, provided the central system can identify a missed review condition or stale route.

### T7 — Domain Completes Action but Issue Persists
**PASS.**

Domain completion does not equal Issue resolution. The parent Issue Object remains open/reviewable and implementation outcome can update Problem State.

### T8 — One Domain Resolves, Another Remains Active
**PASS.**

The parent can become **partially resolved** while retaining active Domain Action Objects.

### T9 — Protected Domain Cannot Disclose Details
**PASS.**

The bounded-status model allows a protected domain to return processing/disposition state without returning restricted evidence.

### T10 — Domain Discovers a Second Issue
**PASS WITH LINEAGE REQUIREMENT.**

The new issue should become a linked Issue Object with provenance to the domain finding that exposed it. It should not silently mutate the parent into an unrelated case.

### T11 — Domain Evidence Changes Original Priority
**PASS.**

Domain-returned evidence can update the shared Problem State and cause legitimate reassessment through the normal priority architecture.

### T12 — Participant Challenges Domain Classification
**PASS.**

The Challenge Object can identify the contested domain decision without granting the participant control of the outcome.

### T13 — Repeated Transfer Loop
**PARTIAL PASS / GAP.**

Auditability reveals the loop, but detection needs an explicit route-history/loop condition and escalation.

### T14 — Central Oversight Attempts to Overrule Domain Judgment
**PASS AS A BOUNDARY TEST.**

The specification explicitly denies central Resolution Oversight substantive domain authority. Oversight may challenge process state or trigger legitimate review; it cannot silently substitute its own domain decision.

### T15 — Domain Attempts to Close Parent Issue
**PASS.**

Domain Action Object completion returns to the parent; only the parent resolution process can determine overall Issue state.

### T16 — Parent Appears Resolved but Implementation Later Fails
**PASS.**

Dynamic Problem State, Response State and reopening permit the Issue Object to reactivate. Closure does not erase provenance.

## 3. Main Gap — Responsibility Resolution

Three tests expose the same missing structure:

- T4 no owner accepts;
- T5 ownership dispute;
- T13 transfer loop.

The architecture needs a bounded **Responsibility Resolution State**.

Candidate states:
- owner resolved;
- provisional owner;
- multi-owner;
- ownership disputed;
- unowned / owner unresolved;
- transfer pending;
- responsibility escalation required.

This state belongs to routing/resolution architecture, not to the participant.

> **Failure to Identify an Owner Must Not Become Failure to Recognise an Issue.**

## 4. Responsibility Resolution Object

Where ordinary routing fails, create a lightweight **Responsibility Resolution Object (RRO)** linked to the Issue Object.

Candidate fields:
- Issue ID;
- domains considered;
- routing reasons;
- acceptance/refusal/transfer records;
- disputed responsibility;
- unresolved functional need;
- current resolver;
- escalation route;
- resolution/disposition.

The RRO exists to resolve **who must process the issue**, not what the substantive outcome should be.

> **Responsibility Resolution ≠ Substantive Case Resolution.**

## 5. Cross-Domain Dependency Model

T3 shows that several valid Domain Action Objects may be:

- independent;
- sequential;
- mutually dependent;
- conditionally dependent;
- blocked by another domain;
- jointly required for overall resolution.

The central record therefore needs bounded dependency information.

Candidate relation:

**DAO-A → independent of DAO-B**

or

**DAO-B → requires output from DAO-A**

or

**DAO-C + DAO-D → jointly required before parent resolution**

This is coordination metadata, not authority transfer.

## 6. Staleness and Silence

A route cannot be judged stalled merely because a fixed amount of time passed. Different legitimate processes operate at different speeds.

Instead, detect staleness relative to:
- promised/required next action;
- stated review condition;
- dependency resolution;
- domain-specific legitimate timing;
- material change requiring response.

> **Elapsed Time Alone ≠ Process Failure.**

but:

> **Missed Legitimate Review Condition → Response-State Reassessment.**

This preserves the earlier principle that the system works at the speed justified by the work while still making silent disappearance auditable.

## 7. Transfer-Loop Detection

A route history should preserve transfers.

Example:

**Governance → Oversight → Governance → Oversight**

The loop itself becomes process-state evidence.

A repeated route cycle should trigger Responsibility Resolution rather than continue indefinitely.

No universal numerical loop threshold is established here; obvious repeated cycles and unresolved ownership require review.

## 8. Overall Resolution Function

The parent Issue Object should determine overall resolution from:

- current Problem State;
- current Response State;
- Domain Action Object states;
- unresolved dependencies;
- Responsibility Resolution state;
- outstanding legitimate review conditions;
- implementation outcome where relevant.

This is not a simple “all child objects closed” calculation.

A domain may close legitimately while the underlying issue remains unresolved.

## 9. New Failure Modes

43. no-owner disappearance;
44. responsibility ping-pong;
45. transfer-loop normalisation;
46. central oversight substantive capture;
47. domain unilateral parent closure;
48. hidden cross-domain dependency;
49. false resolution from child-object completion;
50. protected-information opacity used to conceal process failure;
51. central-status demand causing unnecessary protected-data exposure;
52. downstream-discovered issue silently folded into wrong parent.

## 10. Overall Result

- 12 cases pass at the current abstraction;
- 4 expose bounded structural gaps/refinements;
- 0 invalidate the candidate hub-and-domain architecture.

The most important finding is that the architecture requires a **Responsibility Resolution layer** between ordinary routing and substantive domain action.

The frozen specification therefore survives the first cross-domain adversarial test, subject to bounded revision.

## Current Status

**16 CROSS-DOMAIN CASES EXECUTED**

**HUB-AND-DOMAIN STRUCTURE SURVIVED**

**RESPONSIBILITY RESOLUTION OBJECT IDENTIFIED**

**CROSS-DOMAIN DEPENDENCY REPRESENTATION IDENTIFIED**

**STALENESS / TRANSFER-LOOP BOUNDARIES REFINED**

**NEXT STEP: BOUNDED REVISION OF CANDIDATE SPECIFICATION, THEN TEST IN A MATERIALLY DIFFERENT DOMAIN SCENARIO**
