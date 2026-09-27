# Civil Attention, Reporting, Petition and Resolution Module v1.0

**Author:** Alexander C. Blainey
**Project:** The Concord Framework
**Method:** PMEDG v1.2
**Release:** v1.0
**Date:** 25 September 2026
**Status:** GRADUATED PORTABLE MODULE / SUPPORTED / CORRIGIBLE

## Purpose

A portable, domain-neutral method by which a participant can cause a legitimate system to notice, preserve, classify, route, examine and respond to a suggestion, problem report, petition or related attention input. The participant need not understand the host system's internal topology. The method creates legitimate attention and accountable processing; it does not give the participant unilateral authority over truth, priority, remedy, resources or outcome.

## Core Architecture

**Participant Trigger → Common Intake → Receipt → Original Preservation → Provisional Classification → Existing-Issue Match → Information-Sufficiency Assessment → Issue Creation / Attachment / Split / Merge → Evidence and Epistemic State → Functional Routing → Domain Action Object(s) → Domain Examination / Action → Mandatory Return → Central Resolution Record → Participant Feedback → Challenge / Escalation / Reopening where legitimate**

## Core Invariants

1. Right to Trigger Attention ≠ Right to Dictate Outcome.
2. Submission ≠ Evidence ≠ Verification ≠ Finding ≠ Authority to Act.
3. Received ≠ Verified ≠ Accepted ≠ Authorised.
4. Popularity ≠ Truth.
5. Unverified ≠ False.
6. Reported ≠ True.
7. Central Visibility ≠ Central Control.
8. Domain Completion ≠ Issue Resolution.
9. Routing Creates Responsibility; It Must Not Break Traceability.
10. Participant Knowledge of the Problem ≠ Participant Knowledge of the Host System.
11. Auditable Status ≠ Universal Data Access.
12. Failure to Identify an Owner Must Not Become Failure to Recognise an Issue.
13. Responsibility Resolution ≠ Substantive Case Resolution.
14. Participants Can Trigger Attention; They Cannot Manufacture Priority.
15. Institutions Can Assess Priority; They Cannot Manufacture Finality.
16. Reviewability Is the Counterweight to Pressure Resistance.
17. Repeated Confirmation of a Known State ≠ Increased Problem Weight.
18. New Information About the State → Reassessment of Problem Weight.
19. Group for Processing; Preserve Individually for Evidence and Provenance.
20. No Actionable Issue Should Become Inert Merely Because It Is Waiting.
21. Triggering Review ≠ Authority Over Outcome.
22. Individual Resolution ≠ Systemic Resolution.
23. Urgent Enough to Examine or Protect Against ≠ Proven True.

## Input Classes

**Suggestion:** a proposed improvement, solution or opportunity. Merit does not depend on popularity.

**Problem Report:** a report of a possible defect, harm, failure or undesirable condition. Problem Report ≠ Established Problem.

**Petition:** a collective expression of concern, preference or requested action. Petition Support ≠ Problem Weight. Support is an attention signal, not proof of truth, severity or entitlement to resources.

## Object Model

**Submission Object ≠ Issue Object ≠ Investigation/Examination Object ≠ Finding/Decision Object ≠ Implementation/Remedy Object**

The Submission Object preserves what was actually received. An Issue Object represents a concern requiring processing. One submission may create several Issues; several submissions may attach to one Issue. Later processing must not rewrite original provenance.

## Classification and Information Sufficiency

Submitter classification is advisory context. System classification is a provisional, reviewable routing decision. Classification ≠ Information Sufficiency. Insufficient information is not a finding of falsity. Anonymity does not itself make a submission non-actionable, and identity does not establish evidentiary sufficiency.

## Split, Merge and Information Delta

Issue Objects are created when needed rather than automatically for every submission. Common Topic ≠ Common Issue. Merge for Processing ≠ Erase Individual Provenance.

The method separates submission volume, source independence where legitimately knowable, materially distinct information, corroborating evidence and contradictory evidence. Raw Count ≠ Independent Participants. Independent Participants ≠ Independent Evidence. Duplicate Processing ≠ Duplicate Information.

**Case State(t+1) = Case State(t) + Evaluated Information Delta**

## Attention / Truth / Priority Firewall

The module separates intake, attention/epistemic assessment, and problem/priority/resource assessment.

**Intake Pressure May Trigger Re-Evaluation; It Must Not Directly Command Problem Priority or Resource Allocation.**

## Domain Routing and Domain Action Objects

One Issue may route to one or several legitimate functional owners. Each route creates or binds a Domain Action Object (DAO) linking the parent Issue to domain processing. A DAO should preserve parent reference, routing reason, responsible function, processing state, significant action, dependencies, disposition, review condition where applicable, bounded return information and provenance.

**One Front Door; Many Legitimate Functional Owners.**

## Mandatory Return

Every outbound route requires a return path. The parent/common layer must receive enough bounded information to know processing state and legitimate disposition. Protected evidence need not be returned centrally.

## Problem State and Response State

Problem State represents the current best-supported understanding of the underlying Issue. Response State represents what legitimate functions have done, are doing, failed to do or are waiting upon.

**Problem-State Stability ≠ Response-State Adequacy**

## Responsibility Resolution

When ordinary routing cannot establish legitimate ownership, the Issue remains recognised. A Responsibility Resolution Object (RRO) may record candidate owners, routing reasons, acceptance/refusal/transfer history, disputed responsibility, unresolved functional need, current resolver, escalation and disposition. Responsibility Resolution ≠ Substantive Case Resolution. The core does not manufacture an authority merely because one is missing.

## Dependencies and External Dependencies

Dependencies may be independent, sequential, mutually dependent, conditionally dependent, blocked or jointly required.

**Waiting For + Dependency Owner + Required State/Information + Review Condition + Backstop + Next Responsible Function**

Waiting Without a Represented Condition Is a Staleness Risk.

**External Dependency ≠ Transfer of Local Responsibility**

## Queue Vitality and Deferral

A host may bind the module to a scheduler or state-trigger architecture. Deferral Requires a State, Reason and Review Condition. Significant deferrals should remain auditable. Replacing a Review Date Must Not Erase the History of Deferral. Blocked Is a Claim About State, Not an Exemption From Accountability. Review Performed ≠ Review Resolved. Timestamp Refresh ≠ Meaningful State Update.

## Urgency and Protected Information

Urgency can justify rapid examination, protective routing or host-authorised protective action. Urgency does not establish truth. The Civil Attention core does not acquire emergency authority.

Protected evidence may remain within the legitimate domain that owns it. The common layer receives only information necessary for routing, coordination, status, review and feedback.

## Individual and Systemic Resolution

An individual case may reveal a systemic defect. The two may be linked but processed independently. Systemic Investigation ≠ Reason to Delay an Available Individual Remedy. An individual workaround or remedy does not automatically resolve the systemic Issue.

## Challenge, Review and Reopening

Legitimate grounds may include classification error, missed evidence, material information delta, stale processing, conflict of interest, implementation failure, changed conditions or overlooked rights/safety implications. Right to Challenge Processing ≠ Right to Dictate Outcome. Unchanged repetition may attach without full re-examination. Closure preserves provenance and remains subject to legitimate reopening.

## Feedback

Where legitimately possible, participant-facing feedback should communicate:

**Current State + Reason + Responsible Function(s) + Last Material Action + Next Review Condition**

Protected information may limit detail but must not become a pretext for concealing absence of processing.

## Core / Domain Companion Contract

The portable core is versioned independently.

**Core Method Version N + Domain Companion + Bound Host Services → Domain Implementation**

A Domain Companion may specify domain terminology, local evidence requirements, authority/jurisdiction boundaries, confidentiality rules, local processing states, escalation routes, scheduler conditions, permitted dispositions, specialist-system interfaces and domain-specific feedback constraints.

A Domain Companion may not redefine a core invariant, convert attention into command authority, remove provenance or mandatory return, turn popularity into truth/priority, centralise substantive control, erase reviewability for convenience or silently modify the core version.

**Domain Requirement ≠ Core Method Amendment**

**Companion Extension ≠ Core Override**

**Local Adaptation Must Preserve Core Invariants**

**Domain Variation Belongs at the Companion Boundary Unless a General Core Defect Is Demonstrated.**

## Core Revision Rule

**Domain Finding → Candidate Back-Propagation → Core Review → Bounded Core Revision if Justified → Core Version Change → Companion Regression Review**

**Domain-Specific Need Is Evidence for Review, Not Permission for Drift.**

## Host Interface Requirements

The host supplies or binds legitimate mechanisms where needed for durable receipt/persistence, identity/standing/anonymity, substantive domain authority, evidence/verification, privacy/protected information, escalation/review authority, scheduler/review triggers, resource allocation, emergency authority and external-system communication. The module does not invent missing authority.

## Minimum Auditability

A host implementation should preserve enough provenance to reconstruct the original submission, associated Issues, classification/routing changes, responsible owners, significant information/evidence changes, dispositions, significant deferrals, challenge/review outcomes, overall resolution and feedback state.

## Non-Goals

The module does not prescribe a universal database schema, UI, priority algorithm, numerical thresholds, identity system, substantive domain law/policy, domain-specific evidence standards, resource-allocation formula, emergency powers or surveillance authority.

## Validation Record

**BTT-001 — Multi-Site Facilities:** 16/16 cases handled without core amendment.

**BTT-002 — Distributed Open-Source Software Ecosystem:** 16/16 cases handled without core amendment.

**Cross-Test Convergence:** 32/32 blind-transfer cases handled without core amendment.

No core defect was identified. No material core ambiguity required revision. Domain variation was absorbed by Domain Companions and Host Interfaces.

This validation does not establish population-scale empirical performance, legal sufficiency, security robustness or real-world deployment performance.

## Provenance

Developed from the Concord Participant-Initiated Civil Attention programme under `08_Active_Development`, extracted and tested under PMEDG v1.2, and graduated after Portable-Package Graduation Review. The complete development and test record is retained in the PMEDG completed archive.
