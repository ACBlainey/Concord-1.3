# Private Local Evaluation — Cross-Domain Adversarial Transfer Test 001

**Project:** The Concord Framework
**Date:** 3 October 2026
**Status:** ACTIVE DEVELOPMENT TEST / ADVERSARIAL CROSS-DOMAIN TRANSFER / NON-CANONICAL
**Subject:** Private Local Evaluation (PLE)
**Source:** Private Local Evaluation — Query-to-Data and Minimum-Disclosure Result Pattern — Source Resolution 001
**Test objective:** Determine whether PLE transfers beyond genomics without collapsing semantic ownership, authority, privacy or completeness safeguards.

## 1. Frozen candidate kernel under test

The candidate pattern is:

> **Query To Data; Minimum Result From Data**

and:

> **Where protected data can answer a legitimate bounded question locally, prefer moving the bounded question to the protected data over moving the protected data to the evaluator.**

The test must not assume this is universally preferable.

It must identify:
- domains where it transfers cleanly;
- domains where it transfers only with additional safeguards;
- domains/questions where it should not be used;
- whether the residual pattern remains distinct enough from CWA/CIBB to justify later PMEDG extraction.

## 2. Required separations

For every scenario distinguish:

1. source-data custody;
2. authority to submit query;
3. competence to define query;
4. authority to execute query;
5. semantic validity of query;
6. local computation;
7. result classification;
8. authority to receive result;
9. authority to act on result;
10. cumulative disclosure across queries;
11. source/query freshness;
12. completeness of represented evaluation space.

No successful local computation may silently satisfy another category.

---

# TEST A — Genomic Health Risk Update

## Scenario

Validated medical knowledge identifies variant V as materially increasing risk R.

A bounded query is distributed to protected participant genomic records.

## Expected PLE behaviour

Genome remains inside protected wrapper.

Query executes locally.

NO_MATCH:
- no participant-specific external disclosure;
- relevance closes locally.

MATCH:
- private Health relevance event;
- participant informed according to Health notification rules;
- Research receives no participant identity/match by default.

## Adversarial challenges

### A1 — Research requests match list
FAIL if PLE assumes query originator receives identities.

Expected:

> **Question Originator != Automatic Result Recipient**

### A2 — Query requests surrounding sequence
FAIL if bounded matching becomes disguised genome extraction.

### A3 — Variant association later withdrawn
Requires KCS-driven query retirement and participant-state reassessment.

### A4 — genome incomplete/low quality
Must return UNRESOLVED/INSUFFICIENT_SOURCE where appropriate, not NO_MATCH.

## Result

**PASS — STRONG SOURCE APPLICATION**

This remains the reference case.

---

# TEST B — Medication Contraindication

## Scenario

A prescribing system needs to know whether proposed medication M conflicts with the participant's diagnoses, medicines, allergies, renal/hepatic state or validated pharmacogenomic markers.

## Expected PLE behaviour

The protected Health record locally evaluates the contraindication rule.

Possible outward result:

- NO_KNOWN_CONTRAINDICATION;
- CONTRAINDICATION_DETECTED;
- INTERACTION_REVIEW_REQUIRED;
- SOURCE_INCOMPLETE;
- STALE_DATA;
- PROFESSIONAL_REVIEW_REQUIRED.

The prescribing system need not receive every underlying diagnosis or genomic fact.

## Adversarial challenge

A binary SAFE result would overclaim where records are incomplete.

Therefore:

> **No Detected Contraindication != Demonstrated Safety**

## Result

**PASS WITH ESCP/FRESHNESS SAFEGUARD**

PLE transfers strongly but requires explicit uncertainty states.

---

# TEST C — Education Prerequisite Verification

## Scenario

An educational programme requires:
- qualification Q;
- prerequisite module P;
- or demonstrated equivalent competence.

The programme needs eligibility, not the participant's complete educational history.

## Expected PLE behaviour

Protected Education record evaluates the requirement.

Output may be:
- SATISFIED;
- NOT_SATISFIED;
- EQUIVALENCE_REVIEW_REQUIRED;
- RECORD_INCOMPLETE.

## Adversarial challenge

A rigid query may reject legitimate equivalent learning not represented in formal credentials.

This is an ESCP/semantic-definition problem.

PLE can protect privacy but cannot decide what counts as legitimate equivalence unless Education supplies that rule.

> **Private Evaluation != Correct Eligibility Rule**

## Result

**PASS WITH DOMAIN-SEMANTIC SAFEGUARD**

---

# TEST D — Age / Civil Status Verification

## Scenario

A service needs to establish whether a participant is over a defined age or possesses a defined civil status.

It does not need date of birth or the full civil record.

## Expected PLE behaviour

Local query returns the minimum proposition:
- AGE_THRESHOLD_SATISFIED;
- STATUS_PRESENT;
- STATUS_ABSENT;
- UNRESOLVED.

## Adversarial challenge

Repeated threshold queries could reconstruct date of birth:
- over 18?
- over 19?
- over 20?
- etc.

A binary-search attack could derive protected detail.

Therefore cumulative disclosure control is essential.

## Result

**PASS WITH STRONG QUERY-COMPOSITION CONTROL**

This strongly validates the distinction:

> **Minimum Result Per Query != Minimum Disclosure Across Query History**

---

# TEST E — Financial Eligibility Without Balance Disclosure

## Scenario

A bounded service requires evidence that a participant satisfies a financial condition.

The evaluator does not require complete account balances or transaction history.

## Expected PLE behaviour

Protected financial context computes the defined condition locally and releases only the legitimate result.

## Adversarial challenges

### E1 — threshold probing
Repeated queries at different thresholds reconstruct balance.

### E2 — stale funds
A result may cease to be true immediately after evaluation.

### E3 — wrong semantic rule
Affordability, creditworthiness, solvency and entitlement are not interchangeable.

### E4 — source incompleteness
The protected context may not contain external liabilities.

## Result

**PASS CONDITIONALLY / HIGH COMPOSITION AND TEMPORAL RISK**

PLE is useful, but result validity must be time-bounded and query history protected.

---

# TEST F — Employment Competence Verification

## Scenario

A role requires competence/certification C.

Employer needs to know whether the requirement is satisfied, not the participant's complete education/employment record.

## Expected PLE behaviour

Local evaluation returns:
- REQUIREMENT_SATISFIED;
- NOT_SATISFIED;
- EXPIRED;
- EQUIVALENCE_REVIEW_REQUIRED.

## Adversarial challenge

Formal certification may not equal actual competence, and actual competence may exist without the expected credential.

PLE must not turn an employer's chosen proxy into truth.

> **Verified Credential != Necessarily Verified Competence**

## Result

**PASS FOR BOUNDED FACT VERIFICATION / CONDITIONAL FOR SUBSTANTIVE COMPETENCE**

The pattern works best where the proposition itself is well-defined.

---

# TEST G — Research Cohort Discovery

## Scenario

Research seeks participants satisfying condition C.

Researchers would traditionally search a central dataset and obtain a candidate list.

PLE instead distributes a study eligibility query into protected participant records.

## Expected PLE behaviour

Eligible participants receive a private invitation locally.

Researchers do not automatically receive identities of eligible non-consenting participants.

Participants may choose whether to respond.

Conceptually:

**Research Study Query**
→ local eligibility evaluation
→ if not eligible: close silently
→ if eligible: participant-local invitation
→ participant voluntarily responds
→ only then does identity/contact cross into Research context.

## Adversarial challenge

Research asks the system for exact match counts or demographic slices, allowing inference about small populations.

Aggregate statistics require a separate governed aggregation route.

## Result

**PASS — VERY HIGH VALUE TRANSFER**

This is a major independent use case beyond genomics.

> **Cohort Discovery != Candidate Identity Disclosure**

---

# TEST H — Security Condition With Protected Source Intelligence

## Scenario

A civil function needs to know whether a defined security restriction applies to participant P, but the underlying intelligence/source cannot legitimately be disclosed to the ordinary evaluator.

## Expected PLE behaviour

Protected security context may answer a bounded proposition without revealing source intelligence.

## Adversarial challenge

A hidden security result could become unchallengeable secret authority.

Privacy/security of source information cannot eliminate due process, contestability or legitimate explanation requirements.

> **Protected Source != Unchallengeable Conclusion**

> **PLE Must Not Become Secret Evidence Laundering**

## Result

**CONDITIONAL PASS / HIGH RIGHTS RISK**

PLE can minimise source disclosure but requires strong Law/Judiciary safeguards. It is not sufficient architecture by itself.

---

# TEST I — Malicious Query Reconstruction

## Scenario

An authorised requester asks many individually legitimate questions whose combined answers reconstruct protected information.

Examples:
- age threshold binary search;
- financial threshold probing;
- genomic locus probing;
- educational-history reconstruction;
- diagnosis inference through medication contraindication queries.

## Expected PLE behaviour

The protected context recognises cumulative disclosure risk.

Controls may include:
- semantic query budget;
- result coarsening;
- purpose binding;
- query-history state;
- adaptive refusal;
- time windows;
- recipient-specific disclosure accounting.

## Result

**PASS ONLY IF CIBB DISCLOSURE-STATE INTEGRATION IS MANDATORY FOR HIGH-RISK USES**

This is the strongest general attack on the pattern.

The source-resolution invariant is confirmed:

> **Authorised Queries != Automatically Authorised Query Composition**

---

# TEST J — Stale, Incomplete or Disputed Source

## Scenario

The local protected record is incomplete or contains disputed information.

A valid query executes correctly over that record.

## Failure risk

The system returns NO when the correct state is UNKNOWN.

This is classic ESCP.

## Required behaviour

PLE must support:
- UNKNOWN;
- UNRESOLVED;
- SOURCE_INCOMPLETE;
- STALE;
- DISPUTED;
- REVIEW_REQUIRED.

## Result

**PASS WITH MANDATORY NON-BINARY STATE SUPPORT**

> **Correct Local Computation != Complete Real-World Evaluation**

---

# TEST K — Query Originator Not Entitled To Positive Result

## Scenario

A public-health or Research function legitimately distributes a query because participants should know if a condition applies.

The originator does not need participant identities.

## Expected behaviour

Positive result routes locally to participant/Health function.

Originator receives no participant-specific response.

## Result

**PASS — CORE PLE PROPERTY**

This demonstrates that query authority, result-recipient authority and action authority are genuinely separable.

---

# TEST L — Aggregate Research Request

## Scenario

Research legitimately needs prevalence of condition C rather than participant identities.

## PLE question

Can individual local results be aggregated without turning the local matcher into an uncontrolled Research collection system?

## Finding

Potentially, but this is a distinct operation.

It requires a governed aggregation architecture defining:
- consent/legal basis;
- minimum cohort size;
- disclosure risk;
- statistical leakage;
- repeated-query composition;
- output precision;
- provenance.

## Result

**OUTSIDE MINIMUM PLE KERNEL**

PLE may supply local contributions, but aggregate Research statistics should not be silently included in the base module.

---

# TEST M — Participant Benefit Without External Observer

## Scenario

A new entitlement, Health warning or educational opportunity applies to some participants.

The civil system's objective is to ensure relevant participants know, not to build a list of who qualifies.

## Expected behaviour

Rule/query distributed locally.

Only qualifying participants receive local notification.

No central qualifying-participant list is required.

## Result

**PASS — HIGH VALUE GENERALISATION**

This suggests a broader civil design principle:

> **Notification Need != Population Classification Database Need**

---

# TEST N — Consequential Action Trigger

## Scenario

A local query returns MATCH and an automated system proposes a consequential action.

## Adversarial challenge

The system treats the match itself as authority to execute.

## Required behaviour

PLE result enters the existing consequential-action architecture.

**Local Result**
→ substantive interpretation
→ authority/context/transition checks
→ commit
→ execute.

> **Match != Authority To Act**

## Result

**PASS ONLY WITH EXISTING CONSEQUENTIAL-ACTION BOUNDARY**

PLE must remain informational/computational rather than sovereign.

---

# TEST O — Wrong Question

## Scenario

A perfectly bounded private query asks the wrong proposition.

Example:
an employer privately verifies credential X even though credential X is a poor proxy for the actual role competence required.

## Finding

PLE protects privacy while still producing a substantively bad decision input.

Therefore:

> **Privacy-Preserving Evaluation != Correct Evaluation**

and:

> **Correct Answer To Wrong Question != Correct Decision**

This interfaces directly with Blaineyan Reasoning, Reality Trees and ESCP.

## Result

**PASS AS A LIMITATION TEST**

The architecture correctly remains non-sovereign and non-semantic.

---

# 3. Cross-domain findings

## 3.1 Transfer

PLE transfers materially across:
- genomics;
- medication safety;
- Education;
- identity/status;
- finance;
- employment;
- Research recruitment;
- security-sensitive information;
- civil notification.

It is therefore not merely a genomic special case.

## 3.2 Strongest use cases

PLE is strongest where:
1. source data is highly sensitive;
2. a narrow proposition is sufficient;
3. source data can remain local;
4. the result recipient needs less information than the source contains;
5. negative results need not be centrally observed;
6. participant-local notification is sufficient.

## 3.3 Weakest use cases

PLE is weaker where:
- the proposition is poorly defined;
- human judgement is itself the substantive function;
- source completeness is unknown;
- repeated queries can reconstruct the source;
- result secrecy would undermine due process;
- the result immediately becomes a consequential action without independent authority.

## 3.4 Newly confirmed architectural separations

The test strongly confirms:

> **Query Authority != Result Authority != Action Authority**

> **Query Competence != Query Authority**

> **Local Computation != Semantic Validity**

> **Privacy Preservation != Decision Correctness**

> **Minimum Result != Minimum Cumulative Disclosure**

> **Negative Result Privacy Can Be A First-Class Property**

## 3.5 New high-value application: private recruitment

Research cohort recruitment is especially strong.

Instead of:

**Research searches population records -> Research obtains candidate identities -> Research contacts candidates**

PLE permits:

**Research publishes authorised eligibility query -> protected records evaluate locally -> eligible participant receives private invitation -> participant chooses whether to contact Research.**

This reverses the surveillance relationship.

The same pattern can apply to:
- clinical studies;
- education opportunities;
- benefits/entitlements;
- employment opportunities where appropriate;
- preventive Health invitations.

## 3.6 New high-value principle: notify without classifying centrally

Many civil functions do not actually need a central list of affected participants.

They need affected participants to know that something is relevant.

Therefore:

> **Need To Reach Relevant Participants != Need To Centrally Identify Relevant Participants**

PLE can transform some population-wide searches into distributed private notification.

# 4. Architecture changes required before extraction

The source-resolution sketch should be strengthened with mandatory:

1. separation of Query Authority / Result Authority / Action Authority;
2. cumulative disclosure-state integration for sensitive repeated queries;
3. non-binary UNKNOWN/STALE/DISPUTED/INCOMPLETE states;
4. explicit query semantic ownership;
5. result freshness/expiry;
6. participant-local notification as a first-class result route;
7. due-process boundary for secret/protected-source evaluations;
8. explicit prohibition on treating PLE result as consequential-action authority;
9. distinction between participant-level PLE and governed aggregate computation.

# 5. PMEDG assessment

**TRANSFER:** PASS

**CROSS-DOMAIN DISTINCTNESS:** PASS

**PRIVACY VALUE:** HIGH

**AUTHORITY BOUNDARY:** PASS WITH REQUIRED INTEGRATION

**ESCP RESILIENCE:** PASS IF NON-BINARY STATES REQUIRED

**ADVERSARIAL QUERY COMPOSITION:** MATERIAL RISK / MITIGABLE THROUGH CIBB DISCLOSURE STATE

**DUE-PROCESS TRANSFER:** CONDITIONAL / DOMAIN-SPECIFIC

**AGGREGATION:** OUTSIDE MINIMUM KERNEL

## Current classification

**PMEDG CANDIDATE — CROSS-DOMAIN TRANSFER PASSED — EXTRACTION NOT YET AUTHORISED**

The pattern is now sufficiently distinct to justify further module development, but the required architecture changes should be folded into the candidate specification before any blind extraction/graduation test.

# 6. Recommended next step

Revise the PLE source-resolution specification into a candidate development specification incorporating the nine required safeguards above.

Then freeze a blind cross-instance test package.

Do not yet graduate or place PLE in the root Portable Modules folder.
