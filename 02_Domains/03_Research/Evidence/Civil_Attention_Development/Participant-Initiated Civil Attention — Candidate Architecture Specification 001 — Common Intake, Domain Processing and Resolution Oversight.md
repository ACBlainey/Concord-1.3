# Participant-Initiated Civil Attention — Candidate Architecture Specification 001
## Common Intake, Domain Processing and Resolution Oversight

**Author:** Alexander C. Blainey
**Project:** The Concord Framework
**Date:** 25 September 2026
**Status:** CANDIDATE ARCHITECTURE / ACTIVE DEVELOPMENT / NON-CANONICAL
**Parent:** *Participant-Initiated Civil Attention, Problem Reporting and Petition Architecture — Development Note 001*

## 1. Purpose

The preceding development and test cycles support freezing a candidate system architecture for cross-domain testing.

The intended civil interface is a **single participant-facing intake system** capable of routing one submission to one or several relevant Concord domains while preserving one coherent civil record of what happened.

Participants should not need to understand Concord's internal organisational topology in order to report a problem, offer a suggestion or initiate a petition.

> **One Civil Front Door; Many Legitimate Functional Owners.**

The front door is not itself the universal investigator, decision-maker or remedy provider.

Its role is to preserve the civil attention chain across domain boundaries.

## 2. Core Architecture

**Participant**
→ **Common Civil Attention Intake**
→ **Receipt / Original Submission Preservation**
→ **Provisional Classification**
→ **Issue Matching / Issue Object**
→ **Multi-Domain Resolution**
→ **Domain Action Object(s)**
→ **Domain-Specific Examination / Action**
→ **Domain Status / Disposition Return**
→ **Central Resolution Record**
→ **Participant Feedback / Reviewability**

One Issue Object may produce:

**Issue A**
→ **Governance Action A1**
→ **Judiciary Action A2**
→ **Safeguarding Action A3**
→ **Infrastructure Action A4**

without requiring the participant to make four separate submissions.

## 3. Common Architecture, Domain-Specific Action

Each receiving domain should use the same minimum civil-attention interface even where its internal substantive processes differ.

The common interface should preserve at least:
- source Issue Object;
- reason for routing;
- domain responsibility;
- receipt/acceptance state;
- current processing state;
- last material action;
- disposition where reached;
- next review condition where unresolved;
- return/status communication;
- provenance of material changes.

The domain remains responsible for its own legitimate expertise, evidence standards, procedures, authority and remedies.

> **Standardise the Civil-Attention Interface; Preserve Legitimate Domain-Specific Process.**

This resembles the broader Concord principle of standardised interfaces with contextual variation, but this specification does not import another module's authority or validation status.

## 4. Domain Action Objects

Routing should create linked **Domain Action Objects** rather than copying the original submission into disconnected systems.

Conceptually:

**Issue Object I-001**
→ **DAO-GOV-001**
→ **DAO-JUD-001**
→ **DAO-OVS-001**

Each Domain Action Object retains a link to the parent Issue Object and returns status/disposition information to it.

A Domain Action Object may itself create legitimate internal investigative, decision or implementation objects according to that domain's architecture.

> **Routing Creates Responsibility; It Must Not Break Traceability.**

## 5. Multi-Domain Routing

One issue may legitimately require multiple domains.

Routing therefore cannot assume:

**One Submission → One Department**

Instead:

**One Submission → One Issue or Several Issues → One or Several Functional Owners**

Each route should record why it exists.

Where ownership is uncertain, the system should resolve responsibility rather than requiring the participant to identify the correct destination.

> **Participant Knowledge of the Problem ≠ Participant Knowledge of the Civil Machine.**

## 6. Central Resolution Record

The Common Civil Attention system should maintain a resolution view of the Issue Object.

This does not duplicate every domain's complete case file.

It records enough information to answer:
- Was the issue received?
- Where was it routed?
- Which domains accepted responsibility?
- What is each route's current status?
- Has any route reached a disposition?
- Is action pending?
- Is a review condition outstanding?
- Has responsibility been transferred?
- Is a route stalled?
- Has the overall issue been resolved, partially resolved, rejected, deferred, escalated or left unresolved for a stated reason?

> **Central Visibility ≠ Central Control.**

The intake/oversight layer can know that Governance has not resolved a routed action without acquiring Governance's substantive decision authority.

## 7. Mandatory Return Path

A routed action must not disappear into a domain.

Every receiving domain should return machine-readable status/disposition information to the parent Issue Object.

Candidate minimum return states include:
- received;
- accepted for processing;
- transferred;
- awaiting information/evidence;
- under examination;
- action authorised;
- action in progress;
- no action justified;
- outside authority/jurisdiction;
- deferred with reason;
- blocked by dependency;
- resolved;
- escalated;
- closed subject to reopening.

Exact vocabularies may later require domain mapping.

The architectural requirement is:

> **Every Outbound Route Requires a Return Path.**

## 8. Resolution Oversight

A separate oversight function is required to observe the processing state across domains.

Its purpose is not to decide every substantive case.

It should detect conditions such as:
- no domain accepted responsibility;
- contradictory ownership claims;
- silent transfer loops;
- no material status update;
- missed review condition;
- unresolved dependency;
- domain action marked complete while parent issue remains unresolved;
- partial resolution incorrectly treated as total resolution;
- issue closed without required disposition information;
- cross-domain disagreement preventing resolution.

> **Oversight of Resolution ≠ Substitution for Domain Judgment.**

## 9. Overall Issue State

Because one issue may have several Domain Action Objects, the parent Issue Object requires an overall state derived from—but not reducible to—individual domain states.

Examples:
- active;
- partially resolved;
- awaiting cross-domain action;
- blocked;
- escalated;
- resolved;
- closed with unresolved residual;
- reopened.

A domain saying “our part is complete” must not automatically close the parent Issue Object.

> **Domain Completion ≠ Issue Resolution.**

## 10. Participant Feedback

The participant-facing system should provide an intelligible status without exposing protected information or requiring knowledge of internal structures.

A useful feedback representation remains:

**Current State + Reason + Responsible Function(s) + Last Material Action + Next Review Condition**

Where several domains are involved, the system may summarise the overall state while preserving route-level detail where legitimately visible.

The participant should not need to chase each domain independently merely to discover whether the civil system has acted.

## 11. Auditability

The architecture should preserve an auditable chain:

**Submission**
→ **Receipt**
→ **Classification**
→ **Issue Object**
→ **Routing Decision(s)**
→ **Domain Acceptance/Transfer**
→ **Material Status Changes**
→ **Disposition(s)**
→ **Overall Resolution Assessment**
→ **Feedback**
→ **Challenge/Reopening Where Applicable**

This allows later examination of whether the system:
- lost a report;
- misrouted it;
- failed to act;
- concealed delay;
- transferred responsibility repeatedly;
- closed it prematurely;
- failed to communicate outcome.

## 12. Oversight Escalation Trigger

Resolution oversight may trigger review where process-state evidence indicates failure.

This does not mean that delay automatically increases the underlying problem's substantive priority.

It means the **Response State** may itself require attention.

> **Problem Priority and Resolution-Process Failure Remain Distinct.**

Where appropriate, persistent process failure may create a linked institutional Issue Object.

## 13. Common Domain Interface — Candidate Minimum Contract

Every participating domain should be capable of receiving:

**Input**
- parent Issue ID;
- relevant submission/evidence links;
- routing reason;
- requested function;
- current problem/epistemic state;
- applicable urgency/rights/safety flags;
- provenance.

and returning:

**Output**
- domain action ID;
- acceptance/transfer state;
- current status;
- last material action;
- disposition/reason where applicable;
- next review condition;
- dependencies;
- escalation/transfer information;
- completion state;
- information/evidence delta generated by the domain.

This is a candidate interface contract, not an implementation protocol.

## 14. Information Return and Epistemic Update

Domains may discover information that changes the parent Issue Object.

Therefore return traffic is not limited to administrative status.

A domain may return:
- corroboration;
- contradiction;
- changed scope;
- new affected systems;
- evidence of another issue;
- corrected classification;
- changed severity;
- implementation outcome.

The Common Civil Attention system should update the Issue Object while preserving which domain supplied the information.

> **Domain Processing Can Change the Shared Problem Model Without Erasing Domain Provenance.**

## 15. Protected Information Boundary

Central visibility does not justify central exposure of all domain data.

The parent system should receive only information legitimately required for:
- routing;
- status;
- resolution oversight;
- participant feedback;
- cross-domain coordination;
- review/reopening.

Protected investigative, personal, security, judicial or other restricted information may remain within the authorised domain while returning an appropriately bounded status.

> **Auditable Status ≠ Universal Data Access.**

## 16. Failure Modes for Cross-Domain Testing

The frozen candidate architecture should now be tested against at least:

1. wrong initial domain;
2. two legitimate domains;
3. five legitimate domains;
4. no domain accepts responsibility;
5. two domains each claim the other owns the issue;
6. domain silently stops processing;
7. domain completes its action but issue persists;
8. one domain resolves while another remains active;
9. protected domain cannot disclose substantive details;
10. domain discovers a second issue;
11. domain evidence changes original priority;
12. participant challenges a domain classification;
13. repeated transfer loop;
14. central oversight attempts to overrule substantive domain judgment;
15. domain attempts to close parent issue unilaterally;
16. parent issue appears resolved but implementation fails later.

## 17. Candidate Structural Principle

The current architecture can be summarised as:

> **Centralise Intake, Provenance, Routing Visibility, Resolution Status and Feedback; Distribute Legitimate Domain-Specific Examination, Decision and Action.**

This is the candidate architecture to be tested next.

## Current Status

**CANDIDATE ARCHITECTURE FROZEN FOR CROSS-DOMAIN TESTING**

**SINGLE CIVIL FRONT DOOR DEFINED**

**MULTI-DOMAIN ACTION OBJECT MODEL DEFINED**

**MANDATORY RETURN PATH DEFINED**

**CENTRAL RESOLUTION RECORD DEFINED**

**RESOLUTION OVERSIGHT BOUNDED FROM DOMAIN JUDGMENT**

**PARTICIPANT FEEDBACK LOOP PRESERVED**

**NEXT STEP: CROSS-DOMAIN ADVERSARIAL TEST OF THE FROZEN SPECIFICATION**


---

# 18. Bounded Revision After Cross-Domain Test 003

Test Programme 003 did not invalidate the frozen architecture. Four cases exposed bounded additions required for responsibility and dependency handling.

## 18.1 Responsibility Resolution State

The parent Issue Object should represent responsibility using states such as:
- owner resolved;
- provisional owner;
- multi-owner;
- ownership disputed;
- unowned / owner unresolved;
- transfer pending;
- responsibility escalation required.

> **Failure to Identify an Owner Must Not Become Failure to Recognise an Issue.**

## 18.2 Responsibility Resolution Object

Where normal routing cannot establish legitimate ownership, a **Responsibility Resolution Object (RRO)** may be created.

It should preserve:
- parent Issue ID;
- domains considered;
- routing reasons;
- acceptance/refusal/transfer records;
- disputed responsibility;
- unresolved functional need;
- current responsibility resolver;
- escalation route;
- final ownership disposition.

> **Responsibility Resolution ≠ Substantive Case Resolution.**

The RRO determines who must process the relevant function. It does not decide the underlying case.

## 18.3 Cross-Domain Dependencies

Domain Action Objects may be independent, sequential, mutually dependent, conditionally dependent, blocked by another domain, or jointly necessary.

The central Resolution Record should preserve enough dependency information to distinguish:
- genuine delay;
- blocked work;
- unresolved coordination;
- completed independent work;
- conditions preventing overall resolution.

Dependency representation coordinates visibility without transferring substantive authority.

## 18.4 Staleness

A route should not be classified as failed merely because a universal time limit has elapsed.

> **Elapsed Time Alone ≠ Process Failure.**

Staleness should instead be assessed against legitimate process information such as:
- next review condition;
- promised/required action;
- unresolved dependency;
- domain-specific timing;
- material change requiring response.

> **Missed Legitimate Review Condition → Response-State Reassessment.**

## 18.5 Transfer Loops

Transfer history must remain auditable.

Where responsibility repeatedly cycles between domains without resolution, the system should enter Responsibility Resolution rather than permit indefinite transfer.

> **Transfer Is a Routing Action, Not a Mechanism for Discharging Responsibility Into the System.**

No universal numerical loop threshold is established by this revision.

## 18.6 Overall Resolution

Overall Issue resolution should consider:
- Problem State;
- Response State;
- Domain Action Object states;
- cross-domain dependencies;
- Responsibility Resolution state;
- outstanding legitimate review conditions;
- implementation outcome where relevant.

It must not be reduced to a mechanical rule that all child actions are marked closed.

**Revision Status:** BOUNDED REVISION AFTER TEST 003 / CANDIDATE ARCHITECTURE REMAINS NON-CANONICAL
