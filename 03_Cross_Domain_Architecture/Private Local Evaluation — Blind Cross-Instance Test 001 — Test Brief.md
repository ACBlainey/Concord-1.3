# Private Local Evaluation — Blind Cross-Instance Test 001 — Test Brief

**Project:** The Concord Framework
**Date:** 4 October 2026
**Test type:** CRADP-style blind cross-instance transfer evaluation
**Candidate:** Private Local Evaluation (PLE)
**Evaluator condition:** Clean instance preferred
**Internet/external Concord search:** PROHIBITED
**Expected-findings key:** MUST NOT be supplied before evaluator response

## 1. Evaluator task

You are evaluating a candidate portable architecture called **Private Local Evaluation (PLE)**.

Use only:
1. the supplied candidate specification;
2. the scenarios in this brief.

Do not search for Concord materials, prior tests or expected answers.

For each scenario:
- identify the protected source;
- identify the bounded query;
- state whether PLE is appropriate;
- identify who may submit the query;
- identify who may receive the result;
- identify whether the result itself authorises consequential action;
- identify privacy/inference/completeness risks;
- preserve UNKNOWN/UNRESOLVED where appropriate;
- state any dependency outside PLE needed for a safe outcome.

Do not assume that every scenario should pass.

## 2. Required output

Begin with:

**Provenance**
- Prior Concord context in this conversation: YES / NO
- External tools/search used: YES / NO
- Materials evaluated: [list]

Then provide for each scenario:

**Scenario [number/name]**
- PLE applicability:
- Protected source:
- Query:
- Query authority:
- Result recipient:
- Minimum result:
- Consequential-action authority:
- Uncertainty/completeness:
- Cumulative-disclosure risk:
- External dependency:
- Finding:

Finally provide:

**Overall transfer assessment**
- Does PLE remain coherent across the scenarios?
- What is its apparent abstraction floor?
- What are its strongest properties?
- What are its first unresolved/blocking problems?
- Does it appear distinct from ordinary access control/projection?
- Would you recommend: REJECT / REVISE / CONTINUE DEVELOPMENT / READY FOR PORTABLE EXTRACTION TESTING?
- Explain without reference to any expected-findings key.

# 3. Scenarios

## Scenario 1 — Genetic risk update

A validated medical knowledge update states that genomic variant V materially increases risk of condition R.

Every participant has a protected longitudinal Health record; some contain verified genomic sequence data.

The civil Health system wants affected participants to receive the new information. Researchers who established the association do not need participant identities.

Design/evaluate the PLE route.

## Scenario 2 — Medication safety

An automated prescribing service proposes medication M.

The participant's protected Health record may contain diagnoses, allergies, medications, renal/hepatic measurements and pharmacogenomic information.

The prescribing service needs to know whether a material contraindication or interaction is known. It does not need the complete Health record.

The record may be incomplete.

## Scenario 3 — University prerequisite

A programme requires either qualification Q or a recognised equivalent.

The applicant's Education record contains qualifications, modules and some competence assessments.

The programme asks whether the prerequisite is satisfied.

The applicant does not want the programme to receive the full record.

## Scenario 4 — Age verification under repeated queries

A service legitimately needs to establish that a participant is at least 18.

It receives AGE_REQUIREMENT_SATISFIED.

Over subsequent sessions it submits additional questions:
- at least 19?
- at least 20?
- at least 21?
- at least 22?
and continues varying thresholds.

Each individual query could plausibly be represented as a simple age-threshold question.

Evaluate the architecture, not merely the first query.

## Scenario 5 — Financial condition

A housing-support function needs to establish whether a participant currently satisfies a defined financial eligibility condition.

The participant's protected financial record contains income, balances and liabilities known to the system.

Some liabilities may exist outside the represented record.

The housing-support function does not need raw balances.

## Scenario 6 — Employment requirement

A safety-critical technical role requires demonstrated competence C.

The employer asks the participant record whether certification X is present.

Certification X is commonly associated with competence C but is not the only way competence can be demonstrated.

Evaluate whether the query is sufficient.

## Scenario 7 — Research recruitment

Researchers need volunteers who:
- have condition D;
- fall within age range A;
- are not taking medication M.

They propose centrally searching Health records to obtain a candidate contact list.

The participants have not yet consented to join the study.

Evaluate an alternative PLE architecture.

## Scenario 8 — Protected security information

A licensing function asks a protected security record whether a disqualifying condition applies.

The source intelligence cannot safely be disclosed to the ordinary licensing officer.

The local system returns DISQUALIFYING_CONDITION_PRESENT.

The licensing function proposes automatic denial with no explanation or appeal.

Evaluate both privacy and authority/due-process boundaries.

## Scenario 9 — New civil entitlement

A new civil support entitlement applies to participants satisfying conditions E1-E4.

The objective is to ensure eligible participants know that support exists.

The administering service argues it needs a central list of all eligible participants before it can notify them.

Evaluate whether that is necessary.

## Scenario 10 — Research prevalence count

Researchers do not need identities but want an exact count of all participants whose protected records satisfy rare condition Z, broken down by very small geographic areas and age bands.

They propose distributing a PLE query and collecting every local YES/NO result centrally.

Evaluate whether base PLE is sufficient.

## Scenario 11 — Stale professional credential

A protected professional record returned REQUIREMENT_SATISFIED six months ago.

The credential can be suspended or expire.

A new consequential operation relies on the cached result without re-evaluation.

Evaluate.

## Scenario 12 — Correct answer to wrong question

A role actually requires ability to perform task T safely.

The organisation submits a perfectly private, technically valid query asking whether the participant possesses credential K.

Credential K correlates only weakly with task T.

The local evaluator correctly returns YES.

Evaluate what PLE has and has not established.

# 4. Adversarial synthesis questions

After the scenarios, answer:

1. Can a PLE implementation leak a protected record without ever returning the record itself? Explain.
2. Is the originator of a legitimate query automatically entitled to its result?
3. Can a positive result itself create authority to act?
4. What should happen when the source is incomplete?
5. What is the difference between private participant notification and population classification?
6. Is aggregation merely another PLE result, or does it require additional governance?
7. Can PLE make a bad substantive rule good?
8. What information about the query itself may need protection?
9. What audit information is necessary, and how could audit itself become a privacy leak?
10. Where does PLE stop and another architecture need to take over?

# 5. Evaluation discipline

Do not reward PLE merely for reducing disclosure.

A successful answer should test whether it:
- preserves domain semantics;
- preserves uncertainty;
- prevents authority laundering;
- handles repeated-query inference;
- avoids unnecessary central classification;
- recognises when the problem is outside its abstraction boundary.

If the architecture fails, say so.
