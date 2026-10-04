# Private Local Evaluation — Revision 002 Focused Regression Test 001 — Test Brief

**Date:** 4 October 2026
**Status:** FOCUSED REGRESSION / PMEDG DEVELOPMENT TEST / NON-CANONICAL
**Material under test:** Private Local Evaluation — Candidate Development Specification 002
**Purpose:** Test the residuals identified by valid Blind Cross-Instance Test 001.

## Evaluator discipline

Use Candidate Development Specification 002 only.

Do not assume PLE should pass.

For each case state:
- whether PLE itself owns the problem;
- required PLE behaviour;
- information that may leave the protected context;
- disclosure-state consequence;
- external handoff if any;
- PASS / CONDITIONAL / FAIL.

## Case 1 — Semantic-family reconstruction

A service has legitimately received:
AGE_AT_LEAST_18 = YES.

It later asks differently worded questions:
- "Is birth year before 2007?"
- "Is participant 21 or older?"
- "Is participant in age band 18–20?"
- "Does youth tariff still apply?"

Each query has a superficially different form and may have a plausible business purpose.

Can PLE recognise composition across semantic families and avoid exact-age reconstruction?

## Case 2 — Cross-recipient collusion

Service A receives AGE_AT_LEAST_18.
Service B receives AGE_AT_LEAST_21.
Service C receives YOUTH_TARIFF_ELIGIBLE.

A, B and C are controlled by the same parent organisation and combine their answers.

Does treating each recipient independently preserve privacy?

## Case 3 — Sensitive query itself

A Research group discovers a possible association between a rare genetic variant and a serious condition not yet publicly announced.

It distributes a local eligibility query.

The participant records remain protected, but query text is logged in ordinary infrastructure visible to unrelated administrators.

Evaluate.

## Case 4 — Audit shadow database

A central audit service records:
participant ID;
query;
exact result;
requester;
time;
purpose;
every time PLE runs.

No original protected records are copied.

Has PLE preserved its privacy objective?

## Case 5 — Stale credential

A result REQUIREMENT_SATISFIED was valid yesterday.

Today the underlying credential is suspended.

A relying service has a cached token valid for 30 days and proposes a safety-critical operation.

What should happen?

## Case 6 — Invalidation without disclosure

The credential authority can notify PLE that a dependent result is no longer current, but the reason for suspension is confidential.

Can the cached result be invalidated without revealing the underlying reason?

## Case 7 — Aggregation handoff

Research wants prevalence of condition Z.

Local PLE contexts can determine whether Z is present.

Research proposes that each context send YES/NO to a central collector and calls this "aggregation."

Evaluate whether Specification 002 permits this and where PLE must stop.

## Case 8 — Protected predicate and appeal

A protected local security predicate returns a result that contributes to licence refusal.

The participant appeals.

The source cannot simply be exposed.

What must PLE preserve for the external due-process architecture, and what problem must it refuse to solve itself?

## Case 9 — Weak proxy

An employer wants competence for hazardous task T.

It asks only whether credential K is present, although K is known to correlate weakly with actual ability.

The query is private, current, authorised and safely disclosed.

Does PLE permit the employer to treat YES as competence established?

## Case 10 — Participant-local notification

A new validated medical risk marker is distributed.

A participant matches.

Health policy requires the participant to receive a private warning but does not require Research or the central distributor to know who matched.

Show the minimum valid route and audit state.

## Case 11 — Coarsening

A financial service has legitimate reason to establish that funds exceed a minimum threshold.

Prior related queries have already narrowed the likely balance.

Can PLE answer the new exact threshold query? If not, identify possible bounded alternatives.

## Case 12 — Reset abuse

A requester exhausts a disclosure budget, waits for an automatic reset, then repeats the same inference sequence.

Does time expiry alone necessarily make the old disclosures irrelevant?

## Regression questions

1. Does Revision 002 materially improve cumulative-disclosure handling over Specification 001?
2. Is the disclosure-state model concrete enough to guide implementation without pretending to be a universal privacy metric?
3. Does query protection now cover the query lifecycle adequately at architectural level?
4. Does the minimum audit contract avoid a central shadow-result database?
5. Are freshness and invalidation semantics sufficiently clear?
6. Are aggregation and due process correctly handed off rather than absorbed?
7. What genuine PLE gap remains that should block portable extraction testing?

## Decision

Recommend one:
- FAIL / RETURN TO SOURCE RESOLUTION
- REVISE SPECIFICATION 002
- PASS REGRESSION / READY FOR PORTABLE EXTRACTION TESTING

Explain the first unresolved requirement if not ready.
