# Private Local Evaluation — Portable Module Candidate v0.1

**Status:** PORTABLE MODULE CANDIDATE / EXTRACTION TESTING / NOT GRADUATED
**Abbreviation:** PLE
**Scope:** Substrate-neutral bounded evaluation of protected information

## Purpose

Private Local Evaluation answers a bounded question from protected information without transferring the protected source to the question originator.

> **Query To Data; Minimum Result From Data**

Move the bounded question to protected data where practical; return only the minimum authorised result.

PLE is not a database, identity system, general access-control system, decision authority, appeal process, aggregation system or substantive domain rule.

## Core separations

> **Query Authority != Result Authority != Action Authority**

> **Query Competence != Query Authority**

> **Ability To Ask A Bounded Question != Ability To Read The Source**

> **Question Originator != Automatic Result Recipient**

> **Correct Answer To A Bounded Question != Broader Conclusion**

> **Match != Authority To Act**

## Required components

A PLE instance has:
- Protected Source;
- bounded Query;
- Purpose;
- Query Authority;
- Semantic Owner;
- Local Evaluator;
- Result Policy;
- Recipient Rule;
- Disclosure State;
- Freshness State;
- Audit Rule;
- External Handoff.

## Execution

**Bounded query**
→ authenticate purpose/authority
→ classify query sensitivity
→ evaluate inside protected boundary
→ check completeness/freshness
→ check cumulative disclosure
→ form minimum sufficient result
→ verify recipient
→ release, coarsen, retain locally, refuse or require review
→ record minimum audit state.

The protected source remains inside its protected boundary.

## Uncertainty

PLE must not manufacture binary certainty.

Possible states include YES, NO, UNKNOWN, UNRESOLVED, SOURCE_INCOMPLETE, STALE, DISPUTED, REVIEW_REQUIRED and NOT_AUTHORISED_TO_EVALUATE.

> **No Match != No Relevant Fact Where Evaluation Was Incomplete**

## Minimum disclosure

Release only what the legitimate function needs. A threshold answer may replace an exact value; a prerequisite answer may replace a full history; a local invitation may replace a central identity list.

> **Result Sufficiency != Source Disclosure**

A result may remain entirely local. A non-match may require no external event.

## Cumulative disclosure

Privacy is evaluated across related queries.

> **Minimum Result Per Query != Minimum Disclosure Across Query History**

> **Individually Safe Answers Can Form An Unsafe Composite**

Where risk warrants, Disclosure State should represent requester/recipient classes, purpose, semantic query family, source sensitivity, result granularity, prior result classes, correlation, time, cumulative inference and coarsening/refusal state.

The goal is enough memory to detect reconstruction without creating another copy of the protected source.

## Semantic families

> **Different Query Text != Independent Disclosure**

Different wording, thresholds, overlapping categories or proxies may reveal the same underlying fact. If safe semantic relationship cannot be established, fail toward review, uncertainty, coarsening or refusal rather than assume independence.

## Cross-recipient composition

> **Separate Recipients != Necessarily Separate Knowledge**

Where materially foreseeable, related recipients should be considered together for disclosure risk. Universal surveillance is not required; known composition risk must not be ignored.

## Disclosure decisions

Possible decisions include RELEASE, RELEASE_COARSENED, RELEASE_LOCAL_ONLY, REVIEW_REQUIRED, REFUSE_COMPOSITION and DEFER.

A disclosure budget may constrain granularity, query frequency/range, time, purpose or recipient class. It need not be a single numeric score.

> **Disclosure Accounting != Universal Information Metric**

A reset does not automatically erase prior knowledge.

> **Time Expiry != Information Erasure**

## Query privacy

Queries can themselves be sensitive.

Query lifecycle:
**create → bind purpose/semantic owner → establish authority → classify sensitivity → authenticate/version → bounded distribution → local execution → minimum retention → expire/withdraw/supersede.**

> **Protected Source != Only Protected Information In The Evaluation**

## Audit

Audit should prove legitimate execution without becoming a result database.

Minimum audit may include evaluation/query references, purpose class, authority-check outcome, evaluator/version, time, freshness state, disclosure decision, routing class, review state and provenance.

Ordinary central audit should not retain protected source or exact participant-specific result unless separately necessary and authorised.

> **Privacy Audit != Shadow Result Database**

> **Audit Of Evaluation != Automatic Central Retention Of Result**

## Freshness and caching

Possible validity states include CURRENT, TIME_BOUNDED, EVENT_BOUNDED, STALE, UNKNOWN_VALIDITY and REVALIDATION_REQUIRED.

> **Valid When Evaluated != Permanently Valid**

> **Stale != False**

> **Past Validity != Current Sufficiency**

A cached result must not support a consequential action where required current validity cannot be established.

A protected source may invalidate a dependent result without exposing why the source changed.

> **Invalidate Result != Disclose Underlying Change**

## Result scope

Results remain bound to query, purpose, semantic scope, recipient, freshness and permitted reuse.

> **Bounded Result != General Participant Label**

## Semantic boundary

PLE can evaluate a poor proxy perfectly.

> **Private Execution Does Not Launder A Weak Proxy Into Truth**

The Semantic Owner remains responsible for whether the query represents the real substantive question.

## External handoffs

PLE ends at the bounded result.

Consequential action requires an independently legitimate decision/authority process.

Population aggregation requires a separately governed aggregation/statistical-disclosure process.

Appeal or contestability requires an external review process; protected evaluation must not make a consequential conclusion unchallengeable.

> **Local Contribution != Automatic Aggregate Collection Authority**

> **Protected Source != Unchallengeable Conclusion**

## Failure behaviour

Fail toward bounded uncertainty, refusal or review when query authority, recipient authority, completeness, freshness, disclosure composition, semantics or protected execution cannot be established.

Unknown state must not silently become permission.

## Portable execution record

**PrivateLocalEvaluation**
- EvaluationRef
- ProtectedObjectClass
- QueryRef / QueryVersion
- Purpose
- QueryAuthorityRef
- SemanticOwner
- QuerySensitivityClass
- LocalEvaluatorRef
- SourceFreshnessRequirement / SourceEvaluationTime
- PermittedResultClasses
- RecipientRule
- DisclosureStateRef / DisclosureDecision
- ResultGranularity / ResultValidityRef
- ConsequentialActionBoundaryRef
- ExternalHandoffClass
- AuditRule
- Expiry
- Provenance

The protected source itself is not part of the interface record.

## Semi-formal disclosure reasoning

An implementation may reason:

**DisclosureRisk(R) = f(Sensitivity, Granularity, PriorDisclosure, QueryFamilyCorrelation, RecipientKnowledge, Purpose, Time, PopulationRarity)**

This is a reasoning scaffold, not a universal numeric privacy formula.

## Conformance checklist

A conforming implementation must:
1. keep protected source local where the use case permits;
2. separate query/result/action authority;
3. preserve uncertainty;
4. minimise result disclosure;
5. account for materially related prior disclosure;
6. recognise or safely fail on semantic query relationships;
7. consider foreseeable recipient composition;
8. protect sensitive queries;
9. avoid audit-result centralisation;
10. preserve freshness/invalidation state;
11. bind results to scope;
12. explicitly hand off functions outside PLE.

## Non-goals

PLE does not guarantee anonymity, substantive correctness, cryptographic security, universal inference resistance, statistical privacy, consent validity, due process or decision legitimacy. Those require separate controls.

## Candidate status

This candidate intentionally depends on no particular government, legal system, profession, database product, AI substrate or software stack.

It requires standalone testing on unfamiliar applications before graduation.
