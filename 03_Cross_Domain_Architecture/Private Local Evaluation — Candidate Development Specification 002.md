# Private Local Evaluation — Candidate Development Specification 002

**Project:** The Concord Framework
**Date:** 4 October 2026
**Status:** PMEDG CANDIDATE / POST-BLIND-TEST REVISION / NON-CANONICAL / NOT GRADUATED
**Predecessor:** Candidate Development Specification 001
**Validation basis:** Blind Cross-Instance Test 001 — valid clean-instance run
**Working abbreviation:** PLE

## 1. Purpose and retained kernel

Private Local Evaluation is a privacy-preserving execution pattern for answering a legitimate bounded question from protected information without transferring the protected source information to the question originator.

> **Query To Data; Minimum Result From Data**

Where protected data can answer a legitimate bounded question locally, prefer moving the bounded question to the protected data over moving the protected data to the evaluator.

PLE remains bounded. It is not a database, identity system, general access-control system, decision authority, judiciary, statistical aggregation system or substantive domain rule.

## 2. Core authority and semantic separations

PLE MUST preserve:

> **Query Authority != Result Authority != Action Authority**

> **Query Competence != Query Authority**

> **Ability To Ask A Bounded Question != Ability To Read The Source**

> **Question Originator != Automatic Result Recipient**

> **Correct Answer To A Bounded Question != Broader Conclusion**

> **Match != Authority To Act**

The substantive domain owns the meaning of the question. PLE owns neither the domain rule nor the downstream decision.

## 3. Protected execution

Default flow:

**Authorised bounded query**
→ protected execution boundary
→ source evaluated locally
→ source remains protected
→ uncertainty/completeness checked
→ disclosure state checked
→ minimum permitted result formed
→ recipient authority checked
→ result routed or retained locally
→ bounded audit state recorded.

A valid result may remain entirely participant-local.

A non-match may produce no participant-specific external event where no external result is needed.

## 4. Non-binary evaluation state

PLE MUST preserve uncertainty rather than manufacture a binary answer.

Applicable states include:
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

> **Correct Local Computation != Complete Real-World Evaluation**

## 5. Disclosure State Model

Specification 002 adds an explicit disclosure-state object.

A protected context SHOULD maintain, where risk warrants:

**PLEDisclosureState**
- ProtectedContextRef
- RequesterRef or RequesterClass
- ResultRecipientRef or RecipientClass
- PurposeClass
- QueryFamily
- QuerySemanticScope
- SourceSensitivityClass
- ResultGranularity
- PriorResultClasses
- CorrelationLinks
- TimeWindow
- CumulativeInferenceState
- DisclosureBudgetState
- CoarseningState
- RefusalState
- ResetOrExpiryRule
- Provenance

The objective is not to reconstruct every substantive result centrally. The disclosure state records enough about what has been revealed to judge whether another answer would materially increase inference risk.

> **Minimum Result Per Query != Minimum Disclosure Across Query History**

> **Authorised Queries != Automatically Authorised Query Composition**

## 6. Cumulative-inference decision

Before releasing a result, high-risk PLE SHOULD evaluate:

1. Is this query legitimate in isolation?
2. What has this requester/recipient already learned?
3. Is this query semantically related to prior queries?
4. Would the new result materially narrow a protected fact?
5. Does combination across time, purposes or recipient identities create a new inference?
6. Can the function be satisfied with a coarser result?
7. Should the query be delayed, refused, rerouted or require independent review?

Possible responses:
- RELEASE;
- RELEASE_COARSENED;
- RELEASE_PARTICIPANT_LOCAL_ONLY;
- REVIEW_REQUIRED;
- REFUSE_COMPOSITION;
- DEFER;
- UNKNOWN where source state prevents answer.

> **Individually Safe Answers Can Form An Unsafe Composite**

## 7. Query-family control

Queries SHOULD be classified by semantic family where repeated variation can reconstruct source information.

Examples:
- age thresholds;
- financial thresholds;
- genomic loci;
- diagnostic predicates;
- credential sets;
- geographic/demographic partitions.

Syntactically different questions may belong to the same semantic family.

> **Different Query Text != Independent Disclosure**

This prevents trivial evasion through reformulation.

## 8. Disclosure budgets

A disclosure budget is a bounded governance mechanism, not necessarily a numeric counter.

It may include:
- maximum useful granularity;
- permitted number/range of related queries;
- time-bound query windows;
- permitted purpose;
- recipient class;
- required coarsening after prior disclosures;
- escalation threshold.

The architecture MUST NOT imply that every information domain can be reduced to one universal privacy score.

> **Disclosure Accounting != Universal Information Metric**

## 9. Query Protection Lifecycle

Queries themselves can reveal protected or sensitive information.

A PLE query SHOULD have a lifecycle:

**Create**
→ establish purpose and semantic owner
→ establish query authority
→ classify query sensitivity
→ authenticate/version
→ distribute only to required protected contexts
→ execute locally
→ retain only required query/audit state
→ expire/withdraw/supersede
→ preserve provenance where necessary.

Query protection may include:
- bounded visibility;
- purpose binding;
- encrypted/controlled transport;
- restricted logs;
- expiry;
- versioning;
- prohibition on unrelated reuse.

> **Protected Source != Only Protected Information In The Evaluation**

> **Authority To Receive A Result != Authority To Inspect Every Query Detail**

## 10. Query change and withdrawal

When a query is superseded because knowledge, policy or validity changes, KCS may propagate the new query/version or retirement state.

This does not grant KCS access to protected local results.

> **Change Propagation != Data Collection**

A withdrawn query SHOULD cease new execution once the withdrawal state is authoritative, subject to bounded degraded-operation rules.

## 11. Minimum Audit Contract

PLE requires auditability without creating a second sensitive database.

Minimum audit SHOULD establish:
- EvaluationRef;
- query/version reference;
- legitimate purpose class;
- authority-check outcome;
- evaluator identity/version;
- execution time;
- freshness state;
- disclosure-policy decision;
- result-routing class;
- exceptional override/review state;
- provenance.

The central or ordinary audit record SHOULD NOT contain the protected source or substantive participant-specific result unless independently necessary and authorised.

Where a participant-specific substantive result must be retained, it SHOULD remain in the protected context appropriate to that result.

> **Privacy Audit != Shadow Result Database**

> **Audit Of Evaluation != Automatic Central Retention Of Result**

Audit access itself MUST be contextual and logged.

## 12. Audit minimisation and correlation

Even metadata can reveal sensitive patterns.

Audit architecture SHOULD consider:
- requester identity;
- query frequency;
- query family;
- timing;
- recipient;
- rare event patterns.

Where possible, separate:
1. proof that legitimate evaluation occurred;
2. substantive result;
3. disclosure event;
4. security/anomaly monitoring.

No actor should gain all four merely because it operates an audit function.

## 13. Freshness and Cache Contract

Every result used beyond immediate local notification SHOULD have an explicit freshness state.

**PLEResultValidity**
- ResultRef
- QueryVersion
- SourceEvaluationTime
- ValidityClass
- ValidUntil where meaningful
- SourceChangeDependency
- RevalidationTrigger
- ConsequentialUseClass
- CachePermission
- Provenance

Possible validity classes:
- CURRENT;
- TIME_BOUNDED;
- EVENT_BOUNDED;
- STALE;
- UNKNOWN_VALIDITY;
- REVALIDATION_REQUIRED.

> **Valid When Evaluated != Permanently Valid**

## 14. Consequential reuse

A cached PLE result MUST NOT be reused for a consequential action if its required freshness cannot be established.

Possible actions:
- re-evaluate locally;
- obtain current authoritative state;
- return STALE;
- return REVALIDATION_REQUIRED;
- route to bounded review.

A previously valid result does not become false merely because it is old; it becomes insufficiently current for uses requiring present truth.

> **Stale != False**

> **Past Validity != Current Sufficiency**

## 15. Source-change invalidation

Where the protected source system can identify a material state change, it MAY invalidate dependent cached results without exposing the changed source fact.

Example:
credential suspension can invalidate a prior REQUIREMENT_SATISFIED token without disclosing the reason for suspension.

> **Invalidate Result != Disclose Underlying Change**

## 16. Result scope

Every released result SHOULD remain tied to:
- query;
- purpose;
- semantic scope;
- recipient;
- freshness;
- permitted reuse where applicable.

A result for one purpose MUST NOT silently become a general reusable participant classification.

> **Bounded Result != General Participant Label**

## 17. External Handoff Contract — consequential action

PLE ends when the minimum authorised evaluation result is routed.

Any consequential action then enters the appropriate architecture:

**PLE Result**
→ substantive domain interpretation
→ authority/context/transition checks
→ commitment
→ execution.

PLE MUST NOT encode a positive match as self-executing authority unless an independently authorised downstream system explicitly consumes it under its own bounded rules.

## 18. External Handoff Contract — aggregation

Population aggregation is outside base PLE.

If a legitimate aggregate function exists:

**Local PLE-compatible contribution**
→ separately governed aggregation boundary
→ statistical disclosure control
→ authorised aggregate output.

PLE MUST NOT achieve aggregation by silently collecting every participant-level YES/NO result into a central result database.

> **Local Contribution != Automatic Aggregate Collection Authority**

## 19. External Handoff Contract — due process

Protected local evaluation may minimise disclosure of sensitive source material, but cannot replace contestability where a result affects rights, standing, licence, liberty, entitlement or comparable interests.

PLE SHOULD provide enough provenance/route information for the legitimate due-process architecture to know:
- which bounded proposition was evaluated;
- what result class was relied upon;
- freshness;
- whether uncertainty/dispute existed;
- which authority supplied the query/rule.

It SHOULD NOT expose protected source information merely because an appeal exists; disclosure questions remain governed by the relevant legal architecture.

> **Protected Source != Unchallengeable Conclusion**

> **PLE Must Not Become Secret Evidence Laundering**

## 20. External Handoff Contract — substantive semantics

PLE can faithfully evaluate a poor proxy.

Therefore the domain owning the question MUST remain identifiable.

Examples:
- Education owns equivalence;
- Health owns clinical semantics;
- employment/qualification architecture owns competence criteria;
- Law owns legal predicates.

> **Private Execution Does Not Launder A Weak Proxy Into Truth**

## 21. Semi-formal disclosure accounting

PLE does not claim universal information-theoretic anonymity.

For a proposed result R, the protected evaluator SHOULD conceptually assess:

**DisclosureRisk(R) = f(Sensitivity, Granularity, PriorDisclosure, QueryFamilyCorrelation, RecipientKnowledge, Purpose, Time, PopulationRarity)**

This is a reasoning structure, not a mandatory universal numeric formula.

Release is permitted only when the legitimate function remains proportionate to the resulting disclosure state under the applicable domain/privacy rules.

The purpose is to force composition-aware reasoning.

## 22. Cross-recipient composition

Colluding or related recipients may combine results.

Where materially foreseeable, disclosure accounting SHOULD support recipient groups/classes rather than assuming every requester is independent.

> **Separate Recipients != Necessarily Separate Knowledge**

This does not require universal surveillance of all recipients; it requires risk-aware grouping where justified.

## 23. Participant visibility

Where safe and appropriate, participants SHOULD be able to know:
- what classes of local queries are permitted;
- what services have requested evaluation;
- what disclosures were made;
- what participant-local notifications occurred;
- what contest/review routes exist.

Exceptions may exist under separately legitimate protected processes.

Participant visibility does not imply direct exposure of security-sensitive query details.

## 24. Failure modes

PLE MUST fail toward bounded uncertainty or refusal where:
- query authority cannot be established;
- result recipient is not authorised;
- source completeness is insufficient;
- freshness is insufficient;
- disclosure composition is unsafe;
- query semantics are unresolved;
- protected execution cannot be trusted.

Unknown state MUST NOT silently become permission.

## 25. Revised execution record

**PrivateLocalEvaluation**
- EvaluationRef
- ProtectedObjectClass
- QueryRef
- QueryVersion
- QueryPurpose
- QueryAuthorityRef
- QueryCompetenceOwner
- QuerySensitivityClass
- LocalEvaluatorRef
- SourceFreshnessRequirement
- SourceEvaluationTime
- PermittedResultClasses
- ResultRecipientRule
- DisclosureStateRef
- DisclosureDecision
- ResultGranularity
- ResultValidityRef
- ConsequentialActionBoundaryRef
- ExternalHandoffClass
- AuditRule
- Expiry
- Provenance

The protected source itself remains outside the interface record.

## 26. Reference transfer cases

PLE remains applicable, with domain-specific safeguards, to:
- genomic Health updates;
- medication safety;
- Education prerequisite checks;
- age/civil-status predicates;
- financial eligibility;
- credential predicates;
- private Research recruitment;
- protected security predicates;
- participant-specific civil notification.

Population prevalence/statistical aggregation remains outside the base kernel.

## 27. Retained non-goals

PLE does not:
- guarantee anonymity;
- guarantee substantive correctness;
- replace CWA/CIBB;
- replace consent architecture;
- create clinical/legal/employment authority;
- create Research consent;
- create due process;
- perform statistical disclosure governance;
- establish domain thresholds;
- eliminate inference attacks;
- require one universal privacy metric.

## 28. Revision 002 invariants

> **Query To Data; Minimum Result From Data**

> **Query Authority != Result Authority != Action Authority**

> **Query Competence != Query Authority**

> **Question Originator != Automatic Result Recipient**

> **Minimum Result Per Query != Minimum Disclosure Across Query History**

> **Different Query Text != Independent Disclosure**

> **Individually Safe Answers Can Form An Unsafe Composite**

> **Disclosure Accounting != Universal Information Metric**

> **Privacy Audit != Shadow Result Database**

> **Audit Of Evaluation != Automatic Central Retention Of Result**

> **Valid When Evaluated != Permanently Valid**

> **Stale != False**

> **Past Validity != Current Sufficiency**

> **Invalidate Result != Disclose Underlying Change**

> **Bounded Result != General Participant Label**

> **Local Contribution != Automatic Aggregate Collection Authority**

> **Protected Source != Unchallengeable Conclusion**

> **Private Execution Does Not Launder A Weak Proxy Into Truth**

> **Separate Recipients != Necessarily Separate Knowledge**

> **Match != Authority To Act**

## 29. PMEDG state

Source resolution: PASS.

Internal cross-domain adversarial transfer: PASS.

Blind Cross-Instance Test 001: PASS WITH DEVELOPMENT RESIDUALS.

Specification 001: superseded for ongoing development, preserved as frozen Test 001 material.

Specification 002: ACTIVE CANDIDATE REVISION.

Portable extraction: NOT YET AUTHORISED.

Graduation: NOT YET AUTHORISED.

## 30. Required regression

Before portable extraction, run a focused regression test covering:

1. repeated semantic-family queries;
2. colluding/cross-recipient queries;
3. query-content privacy;
4. audit metadata reconstruction;
5. stale cached results;
6. source-change invalidation without source disclosure;
7. aggregation handoff;
8. due-process handoff;
9. weak-proxy semantic laundering;
10. participant-local notification with no external match disclosure.

If Revision 002 preserves its boundaries under those cases, PMEDG may consider portable extraction testing.
