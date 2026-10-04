# Private Local Evaluation — Candidate Development Specification 001

**Project:** The Concord Framework
**Date:** 4 October 2026
**Status:** PMEDG CANDIDATE SPECIFICATION / CROSS-DOMAIN TRANSFER PASSED / FROZEN-TEST PREPARATION / NON-CANONICAL / NOT GRADUATED
**Working abbreviation:** PLE
**Source lineage:** Genomic Health Record and Private Local Knowledge Matching 001 -> PLE Source Resolution 001 -> PLE Cross-Domain Adversarial Transfer Test 001
**Dependencies:** Contextual Wrapper Architecture (CWA) / Concord Information Black Box (CIBB) / ESCP / KCS / MKA / consequential-action architecture

## 1. Candidate purpose

Private Local Evaluation is a privacy-preserving execution pattern for cases where a legitimate bounded question can be answered using protected information without transferring the protected source information to the question originator or evaluator.

Core rule:

> **Query To Data; Minimum Result From Data**

Expanded:

> **Where protected data can answer a legitimate bounded question locally, prefer moving the bounded question to the protected data over moving the protected data to the evaluator.**

PLE is not a database, identity system, access-control system, decision authority or substantive domain rule.

## 2. Candidate boundary

PLE begins after a legitimate question has been defined and ends when the minimum authorised evaluation result has been produced/routed.

It does not itself determine:
- whether the underlying source information is true;
- whether the question is substantively correct;
- who should possess civil/clinical/legal authority;
- whether a consequential action should occur;
- whether a Research study is ethical;
- whether an entitlement/qualification standard is justified.

> **Privacy-Preserving Evaluation != Correct Evaluation**

## 3. Required objects

A conforming PLE instance requires:

### 3.1 Protected Source Object
The governed information against which the question is evaluated.

### 3.2 Query
The bounded proposition/function.

### 3.3 Query Purpose
Why the evaluation is being requested.

### 3.4 Query Authority
Why the query may legitimately be submitted to this source/context.

### 3.5 Query Competence
Why the query is semantically fit for the substantive domain.

### 3.6 Local Evaluator
The trusted computation inside the protected context.

### 3.7 Result Policy
Which outputs are permitted.

### 3.8 Result Recipient Rule
Who may receive which output.

### 3.9 Disclosure State
The cumulative information already exposed through related queries/results where material.

### 3.10 Freshness State
Whether query and source are sufficiently current.

### 3.11 Provenance/Audit
Enough information to establish what evaluation occurred without recreating the protected source/result database unnecessarily.

## 4. Three-authority separation

PLE MUST distinguish:

**Query Authority**
→ permission to ask.

**Result Authority**
→ permission to receive a defined answer.

**Action Authority**
→ permission to act consequentially on that answer.

> **Query Authority != Result Authority != Action Authority**

No authority automatically composes into another.

## 5. Query competence separation

A legitimate actor can ask a badly designed question.

Therefore:

> **Query Competence != Query Authority**

Substantive domain owners remain responsible for:
- proposition semantics;
- thresholds;
- equivalence rules;
- uncertainty interpretation;
- appropriate use.

PLE executes the bounded proposition; it does not certify the proposition as wise.

## 6. Protected execution

The default pattern is:

**Authenticated Bounded Query**
→ protected execution boundary
→ source accessed internally
→ local evaluation
→ source remains internal
→ result classified
→ minimum permitted result generated
→ authorised route only.

> **Ability To Ask A Bounded Question != Ability To Read The Source**

## 7. Minimum-result rule

PLE SHOULD disclose no more than is reasonably required for the legitimate function.

Examples:
- AGE_REQUIREMENT_SATISFIED rather than date of birth;
- PREREQUISITE_SATISFIED rather than education transcript;
- CONTRAINDICATION_DETECTED rather than full Health record;
- ELIGIBLE_INVITATION locally rather than candidate identity to Research.

> **Result Sufficiency != Source Disclosure**

## 8. Participant-local result route

A valid PLE result may remain entirely inside the protected participant context.

This is a primary architecture mode.

Example:

**Research eligibility query**
→ local MATCH
→ participant receives study invitation
→ Research receives nothing unless participant responds.

> **Question Originator != Automatic Result Recipient**

> **Cohort Discovery != Candidate Identity Disclosure**

## 9. Silent non-result route

Where the legitimate purpose is notification of affected participants, a non-match may require no external event.

> **No Relevant Result May Require No Participant-Specific Disclosure**

This avoids creating unnecessary central classification lists.

## 10. Non-binary state requirement

PLE MUST NOT force YES/NO where evaluation state does not justify it.

Supported states SHOULD include where applicable:
- YES;
- NO;
- UNKNOWN;
- UNRESOLVED;
- SOURCE_INCOMPLETE;
- STALE;
- DISPUTED;
- REVIEW_REQUIRED;
- NOT_AUTHORISED_TO_EVALUATE.

> **No Match != No Relevant Fact Where Evaluation Was Incomplete**

## 11. ESCP boundary

A local evaluator may correctly process every represented fact and still lack a relevant dimension.

Therefore:

> **Correct Local Computation != Complete Real-World Evaluation**

PLE MUST preserve uncertainty where source completeness cannot be established.

## 12. Freshness

The query and source may have different validity periods.

A result SHOULD carry sufficient validity/freshness state for its legitimate use.

> **Valid When Evaluated != Permanently Valid**

A rapidly changing financial condition and a stable civil-age threshold require different treatment.

## 13. Cumulative disclosure

PLE MUST NOT assess privacy only one query at a time where repeated queries can reconstruct protected information.

> **Minimum Result Per Query != Minimum Disclosure Across Query History**

High-risk implementations SHOULD support:
- query-history/disclosure state;
- semantic query budgets;
- rate limits;
- purpose binding;
- result coarsening;
- adaptive refusal;
- recipient-specific disclosure accounting;
- expiry/reset rules where legitimate.

## 14. Query composition

Several individually authorised queries may form an unauthorised composite inference.

> **Authorised Queries != Automatically Authorised Query Composition**

CIBB disclosure-state architecture is the primary dependency for this problem.

## 15. Query privacy

Queries themselves may be sensitive.

A query can reveal:
- a suspected diagnosis;
- an investigation;
- a new Research finding;
- a security concern;
- an institutional intention.

Query visibility MUST therefore be bounded where appropriate.

> **Protected Source != Only Protected Information In The Evaluation**

## 16. Result semantics

PLE results MUST be scoped to the proposition actually evaluated.

Examples:

**PREREQUISITE_SATISFIED**
does not mean
**FULLY COMPETENT FOR ROLE**.

**NO_KNOWN_CONTRAINDICATION**
does not mean
**TREATMENT PROVEN SAFE**.

**AGE_THRESHOLD_SATISFIED**
does not disclose exact age.

> **Correct Answer To A Bounded Question != Broader Conclusion**

## 17. Consequential-action boundary

A PLE result does not itself authorise consequential action.

**PLE Result**
→ substantive interpretation
→ authority/context/transition checks
→ commitment
→ execution.

> **Match != Authority To Act**

## 18. Protected-source due process

PLE may be used with protected intelligence or other non-disclosable sources only where the surrounding legal/governance architecture preserves appropriate contestability.

> **Protected Source != Unchallengeable Conclusion**

> **PLE Must Not Become Secret Evidence Laundering**

PLE itself does not solve due process.

## 19. Aggregation boundary

Participant-level local evaluation is distinct from population aggregation.

A request for:
- prevalence;
- match counts;
- demographic distribution;
- cohort statistics;

requires a separately governed aggregation mechanism.

> **Local Contribution != Automatic Aggregate Collection Authority**

The minimum PLE kernel does not grant aggregation authority.

## 20. Change propagation

KCS may distribute changed queries/rules when upstream validated knowledge or policy changes.

KCS does not thereby receive protected source information or local results.

> **Change Propagation != Data Collection**

## 21. Audit minimisation

PLE needs enough provenance to verify legitimate execution while avoiding an audit system that reconstructs the sensitive result database.

> **Privacy Audit != Shadow Result Database**

Audit design SHOULD separate:
- query/protocol execution evidence;
- participant-specific substantive result;
- disclosure event.

## 22. Failure behaviour

PLE SHOULD fail toward bounded uncertainty rather than invented certainty.

Where source, authority, freshness, query validity or disclosure state cannot be resolved, appropriate outputs include:
- REVIEW_REQUIRED;
- UNRESOLVED;
- NOT_AUTHORISED_TO_EVALUATE;
- SOURCE_INCOMPLETE.

Unknown state must not silently become permission.

## 23. Candidate execution record

**PrivateLocalEvaluation**
- EvaluationRef
- ProtectedObjectClass
- QueryRef
- QueryVersion
- QueryPurpose
- QueryAuthorityRef
- QueryCompetenceRef
- LocalEvaluatorRef
- SourceFreshnessRequirement
- QueryFreshness
- PermittedResultClasses
- ResultRecipientRule
- CumulativeDisclosureStateRef
- ConsequentialActionBoundaryRef
- Expiry
- Provenance
- AuditRule

The protected source itself is not part of the interface record.

## 24. Reference applications

PLE has passed internal transfer analysis for:
1. genomic Health risk update;
2. medication contraindication;
3. Education prerequisite verification;
4. age/civil-status verification;
5. bounded financial eligibility;
6. employment credential/competence predicates;
7. private Research recruitment;
8. protected-source security condition;
9. participant-specific civil notification.

These examples demonstrate transfer; they do not become mandatory domain policy.

## 25. Non-goals

PLE does not:
- eliminate need for protected central custody where legitimate;
- guarantee anonymity;
- guarantee correctness;
- create entitlement;
- create clinical authority;
- create employment authority;
- create law-enforcement authority;
- create Research consent;
- eliminate human judgement;
- solve all inference attacks;
- establish substantive thresholds.

## 26. Candidate invariants

> **Query To Data; Minimum Result From Data**

> **Query Authority != Result Authority != Action Authority**

> **Query Competence != Query Authority**

> **Ability To Ask A Bounded Question != Ability To Read The Source**

> **Question Originator != Automatic Result Recipient**

> **Result Sufficiency != Source Disclosure**

> **Correct Local Computation != Complete Real-World Evaluation**

> **Valid When Evaluated != Permanently Valid**

> **Minimum Result Per Query != Minimum Disclosure Across Query History**

> **Authorised Queries != Automatically Authorised Query Composition**

> **Correct Answer To A Bounded Question != Broader Conclusion**

> **Match != Authority To Act**

> **Protected Source != Unchallengeable Conclusion**

> **Local Contribution != Automatic Aggregate Collection Authority**

> **Change Propagation != Data Collection**

> **Privacy Audit != Shadow Result Database**

## 27. PMEDG state

Internal source resolution: COMPLETE.

Internal adversarial cross-domain transfer: PASS WITH REQUIRED SAFEGUARDS.

Candidate specification: COMPLETE FOR BLIND TESTING.

Portable extraction: NOT YET AUTHORISED.

Graduation: NOT YET AUTHORISED.

## 28. Next validation

Freeze a blind cross-instance test that tests whether an evaluator, given only the candidate specification and scenarios, independently identifies:
- source retention;
- minimum-result routing;
- query/result/action authority separation;
- cumulative disclosure risk;
- non-binary uncertainty;
- participant-local notification;
- due-process boundary;
- aggregation boundary;
- semantic/non-sovereignty boundary.

The blind evaluator must not be given an expected-findings key before producing its response.
