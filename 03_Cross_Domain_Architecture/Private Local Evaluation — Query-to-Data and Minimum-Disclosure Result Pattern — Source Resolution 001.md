# Private Local Evaluation — Query-to-Data and Minimum-Disclosure Result Pattern — Source Resolution 001

**Project:** The Concord Framework
**Date:** 3 October 2026
**Status:** SOURCE-RESOLVED RESIDUAL PATTERN / CROSS-ARCHITECTURE INTEGRATION PATTERN / PMEDG CANDIDATE / NON-CANONICAL / DO NOT EXTRACT YET
**Origin:** Genomic Health Record and Private Local Knowledge Matching 001
**Primary dependencies:** Contextual Wrapper Architecture / Concord Information Black Box / Bounded Contextual Authority / KCS Change Propagation
**Working name:** Private Local Evaluation (PLE)

## 1. Question

The genomic Health architecture introduced a useful privacy mechanism:

> **Move The Medical Question To The Protected Genome; Do Not Move The Genome To The Question**

Does this represent a genuinely reusable Concord mechanism, or is it already completely contained by existing CWA/CIBB architecture?

## 2. Source-resolution result

The pattern is substantially enabled by existing Concord architecture but is not merely a restatement of it.

### Already present in CWA
CWA provides:
- protected informational/computational contexts;
- function-derived permission;
- minimum-necessary permission;
- bounded contextual access;
- non-inheritance of unrelated access;
- information-flow boundaries.

### Already present in CIBB
CIBB provides:
- authoritative master retained inside protected boundary;
- governed information objects;
- contextual projections;
- transformations before disclosure;
- minimum-necessary selection before egress;
- protected transfer;
- disclosure-state governance;
- exceptional master-access discipline.

### Residual pattern

The genomic case adds a distinct operational relation:

**external bounded question**
→ **execute inside protected information boundary**
→ **evaluate against protected source data**
→ **retain source data inside boundary**
→ **release only minimum authorised result, or no result**
→ **do not disclose participant-specific match state to the question originator unless separately authorised**.

CIBB primarily describes governed information operations and projections. PLE makes **protected local computation initiated by a bounded external question** the central reusable operation.

Therefore:

> **PLE is not a replacement for CWA or CIBB. It is a candidate execution pattern built on them.**

## 3. Core principle

> **Where protected data can answer a legitimate bounded question locally, prefer moving the bounded question to the protected data over moving the protected data to the evaluator.**

Compactly:

> **Query To Data; Minimum Result From Data.**

## 4. Why it matters

Traditional information systems commonly solve a question by:
1. gathering relevant records into an evaluator's environment;
2. searching or correlating them centrally;
3. producing an answer;
4. attempting to control the resulting copies and disclosures.

PLE reverses the default:

1. keep protected source information in its governed context;
2. authenticate and bound the question;
3. execute the question locally;
4. expose only the minimum legitimate result;
5. preserve non-result privacy where possible.

This reduces the amount of protected information that must cross boundaries.

## 5. Distinct objects

PLE should distinguish:

### Protected source object
The information that should ordinarily remain inside its wrapper.

### Query
The bounded proposition/function to evaluate.

### Query authority
Why this question may legitimately be asked of this protected object/class.

### Local evaluator
The trusted execution function inside the protected boundary.

### Result policy
What output, if any, may leave the boundary.

### Result recipient
Who is authorised to receive that output.

### Provenance
Which query/version/basis produced the result.

> **Authority To Submit Query != Authority To Receive Every Possible Result**

## 6. Basic lifecycle

**Legitimate objective**
→ bounded query defined
→ query authority validated
→ query authenticated/versioned
→ delivered to protected context
→ local execution
→ source data remains internal
→ result classified
→ minimum authorised output generated
→ output delivered only to legitimate recipient
→ provenance/audit retained
→ query expires/retires/re-evaluates as appropriate.

## 7. Result classes

A query need not always return a binary answer externally.

Possible result policies include:

### Silent negative
If condition is absent, no participant-specific external result leaves the boundary.

### Participant-local positive
A match creates a private event for the protected-data owner/participant but not for the query originator.

### Bounded external answer
A YES/NO/UNRESOLVED or categorical result may be released where legitimate.

### Derived value
Only a minimum derived measure is released.

### Action trigger
The local system triggers a legitimate downstream function without revealing the underlying protected data.

### Aggregate contribution
A separately governed mechanism may contribute a privacy-preserving aggregate result.

> **Local Evaluation != Mandatory External Result**

## 8. Candidate applications

### Health
A drug-interaction or genetic-risk query executes against a participant's protected Health record and exposes only the clinically necessary answer.

### Education
An opportunity may ask whether prerequisites are satisfied without receiving the participant's complete educational history.

### Employment
A role may ask whether a participant satisfies a defined competence/certification condition without receiving unrelated employment or education records.

### Economy
A transaction may ask whether a bounded affordability/eligibility condition is satisfied without disclosing complete financial history.

### Civil services
A service may ask whether a participant meets a defined entitlement condition without receiving the full civil record.

### Identity
A system may ask whether a required identity/age/status proposition is satisfied without receiving the underlying identity record.

### Research
A distributed study may ask protected records to evaluate a condition locally, with participant-specific results remaining local unless separately consented.

### Security-sensitive systems
A protected system may answer whether a bounded safety/clearance condition is satisfied without exposing the source intelligence or complete security record.

These are candidate applications only; each domain retains authority over its own semantics and disclosure rules.

## 9. No semantic ownership transfer

PLE is an execution/privacy pattern.

It does not decide:
- whether the question is legitimate;
- whether the source fact is correct;
- what substantive meaning the result has;
- whether an action should follow;
- whether the result may be disclosed.

Those remain with legitimate domain owners.

> **Local Computation != Substantive Authority**

> **Query Engine != Decision Sovereign**

## 10. Query minimisation

The query itself can be privacy-sensitive.

A query may reveal:
- what an organisation suspects;
- what Research has discovered;
- what condition is being screened;
- what investigation is underway.

Therefore query visibility should also be bounded.

> **Protected Data != Only Protected Information In The Interaction**

## 11. Query exfiltration risk

A malicious or overly broad query could reconstruct protected source information through repeated questions.

Examples:
- asking one bit at a time;
- adaptive narrowing;
- overlapping queries;
- repeated threshold probes;
- correlated queries across contexts.

Therefore:

> **Minimum Result Per Query != Minimum Disclosure Across Query History**

CIBB disclosure-state mechanisms are relevant here.

The local context may need to consider cumulative disclosure rather than each query independently.

## 12. Query-budget and composition controls

Depending on risk, PLE may require:
- query-rate limits;
- semantic query restrictions;
- result coarsening;
- cumulative disclosure state;
- purpose binding;
- query expiry;
- anti-correlation rules;
- recipient restrictions;
- review/escalation for unusual query sequences.

A legitimate individual query can become illegitimate when composed with prior results.

> **Authorised Queries != Automatically Authorised Query Composition**

## 13. Negative-result privacy

One of the strongest properties of the genomic case is that a non-match does not need to be externally observable.

This can generalise.

If the legitimate objective is to alert a participant when a condition applies, the originator may not need a list of everyone for whom it does not apply.

> **No Relevant Result May Require No Participant-Specific Disclosure**

This can dramatically reduce population-level surveillance.

## 14. Positive-result privacy

Even a positive match need not return to the query originator.

The result may instead be routed to:
- the participant;
- a participant-authorised function;
- a domain-specific service;
- another legitimate owner.

> **Question Originator != Automatic Result Recipient**

## 15. Result semantics

A derived answer should state its scope.

For example:

**Prerequisite satisfied: YES**

does not imply disclosure of:
- which qualification satisfied it;
- where it was obtained;
- grades;
- unrelated qualifications.

Similarly:

**Medication contraindication detected**

does not necessarily disclose the diagnosis or genomic marker that caused it.

> **Result Sufficiency != Source Disclosure**

## 16. Unknown and disputed states

PLE must not force protected data into binary answers where the source state is incomplete, stale, disputed or ambiguous.

Possible results include:
- YES;
- NO;
- UNRESOLVED;
- STALE;
- SOURCE_INCOMPLETE;
- REVIEW_REQUIRED;
- NOT_AUTHORISED_TO_EVALUATE.

> **No Match != No Relevant Fact Where Evaluation Was Incomplete**

This interfaces with ESCP.

## 17. Data freshness

The query may be current while the protected source is stale, or vice versa.

A local result should preserve relevant freshness/version information without necessarily disclosing source details.

> **Current Query + Stale Source != Current Answer**

## 18. Change propagation

KCS can distribute newly relevant bounded questions to protected records where a legitimate knowledge or rule change occurs.

This does not give KCS access to the protected source data.

Conceptually:

**validated upstream change**
→ identify affected query class
→ distribute bounded query/update
→ local evaluation
→ local or authorised result
→ downstream action only where material.

> **Change Propagation != Data Collection**

## 19. Audit

Proportionate audit may record:
- query identity/version;
- source-object class;
- legitimate basis;
- execution time;
- result class;
- disclosure destination;
- whether an external result was released;
- cumulative-disclosure state where required.

Audit should avoid becoming a secondary database of the protected answers.

> **Privacy Audit != Shadow Result Database**

## 20. Failure modes

### Centralisation creep
A system starts with local evaluation but later copies data centrally for convenience.

**Safeguard:** source-retention invariant and explicit exception authority.

### Query exfiltration
Repeated queries reconstruct the protected object.

**Safeguard:** cumulative disclosure control.

### Originator overreach
The question sender assumes it is entitled to every match.

**Safeguard:** separate query authority from result-recipient authority.

### Semantic laundering
A YES/NO result is treated as authority for an action it did not establish.

**Safeguard:** domain-owned result semantics and downstream authority checks.

### Silent stale evaluation
An old protected record produces a confident result to a current query.

**Safeguard:** freshness state.

### Audit leakage
Logs recreate the sensitive result dataset.

**Safeguard:** minimum-necessary audit representation.

## 21. Candidate schema

**PrivateLocalEvaluation**
- EvaluationRef
- ProtectedObjectClass
- QueryRef
- QueryVersion
- QueryPurpose
- QueryAuthorityRef
- LocalEvaluatorRef
- SourceFreshnessRequirement
- PermittedResultClasses
- ResultRecipientRule
- CumulativeDisclosureStateRef
- Expiry
- Provenance
- AuditRule

The protected source data itself is deliberately absent from this interface object.

## 22. Relationship to existing Concord architecture

### CWA
Defines the protected context, access conditions and function-derived permissions.

### CIBB
Defines governed information objects, protected master retention, transformation/projection and disclosure governance.

### PLE
Defines the specific pattern of executing an externally supplied bounded question inside the protected context and releasing only the minimum legitimate result.

### KCS
Can propagate changed questions/rules when upstream knowledge changes.

### ESCP
Prevents local query success from being mistaken for complete evaluation where the source/query representation is incomplete.

### MKA
May verify multiple necessary authorities for consequential query execution/disclosure where required.

### BTA
May govern state transitions caused by a local result without implying that the query transfers ownership of source semantics.

## 23. Source-resolution classification

PLE is currently best classified as:

**RESIDUAL CROSS-ARCHITECTURE PATTERN / PMEDG CANDIDATE / DO NOT EXTRACT YET**

It is more specific than CWA and CIBB, but currently has only one fully developed source application: genomic Health.

Before extraction, it should be adversarially tested across several unrelated protected-data domains.

## 24. Proposed validation set

At minimum test:
1. genomic Health risk update;
2. medication contraindication;
3. education prerequisite verification;
4. age/status verification;
5. financial eligibility without balance disclosure;
6. employment competence verification;
7. Research cohort discovery without participant disclosure;
8. security condition with protected source intelligence;
9. malicious repeated-query reconstruction;
10. stale/incomplete/disputed source data;
11. query-originator not authorised to receive positive result;
12. legitimate aggregate research request distinct from participant-level query.

The test should specifically look for:
- information leakage;
- authority laundering;
- semantic ownership collapse;
- query-composition attacks;
- false binary certainty;
- hidden centralisation.

## 25. Core invariants

> **Query To Data; Minimum Result From Data**

> **Where protected data can answer a legitimate bounded question locally, prefer moving the bounded question to the protected data over moving the protected data to the evaluator.**

> **Authority To Submit Query != Authority To Receive Every Possible Result**

> **Local Evaluation != Mandatory External Result**

> **Question Originator != Automatic Result Recipient**

> **Local Computation != Substantive Authority**

> **Result Sufficiency != Source Disclosure**

> **Minimum Result Per Query != Minimum Disclosure Across Query History**

> **Authorised Queries != Automatically Authorised Query Composition**

> **Change Propagation != Data Collection**

> **Privacy Audit != Shadow Result Database**

## 26. Next step

Run a cross-domain adversarial integration test before any PMEDG extraction decision.

The purpose is not to prove that local computation is technically possible. It is to determine whether the pattern transfers cleanly across domains while preserving semantic ownership, bounded authority, privacy and cumulative-disclosure control.


# 27. Post-transfer-test candidate strengthening

**Source:** Private Local Evaluation — Cross-Domain Adversarial Transfer Test 001

The first cross-domain adversarial transfer test found that PLE transfers materially beyond genomics, but identified safeguards that must be treated as part of the candidate architecture rather than optional implementation details.

## 27.1 Three-authority separation

Every consequential deployment should distinguish:

**Query Authority**
— may this question legitimately be submitted?

**Result Authority**
— who may receive which result?

**Action Authority**
— what, if anything, may legitimately be done because of the result?

> **Query Authority != Result Authority != Action Authority**

A participant-local result can therefore exist without being disclosed to the originator and without authorising any external action.

## 27.2 Query competence

Authority to submit a query does not establish that the query is semantically well-designed.

> **Query Competence != Query Authority**

Domain owners remain responsible for the meaning and validity of the proposition being evaluated.

## 27.3 Mandatory uncertainty states

High-consequence PLE implementations must not force binary output where source state is incomplete.

At minimum, where applicable, preserve:
- UNKNOWN;
- UNRESOLVED;
- STALE;
- SOURCE_INCOMPLETE;
- DISPUTED;
- REVIEW_REQUIRED.

> **Correct Local Computation != Complete Real-World Evaluation**

## 27.4 Result freshness

A result should carry sufficient temporal validity to prevent an old local evaluation from being treated as indefinitely current.

> **Valid When Evaluated != Permanently Valid**

## 27.5 Cumulative disclosure is first-class

For sensitive data, query-history disclosure state is part of the security boundary.

A query may be refused or coarsened even when it would be acceptable in isolation if prior answers make the composition excessively revealing.

> **Minimum Result != Minimum Cumulative Disclosure**

## 27.6 Participant-local notification

PLE explicitly supports a result route in which the participant is informed while the query originator is not.

This is not an edge case. It is one of the architecture's primary privacy functions.

> **Need To Reach Relevant Participants != Need To Centrally Identify Relevant Participants**

Potential applications include:
- new Health risks;
- Research studies;
- benefits/entitlements;
- Education opportunities;
- preventive services.

## 27.7 Private Research recruitment

A high-value transfer pattern is:

**Research defines legitimate eligibility query**
→ query distributed to protected participant records
→ local eligibility evaluation
→ non-eligible closes silently
→ eligible participant receives private invitation
→ participant chooses whether to reveal themselves/respond.

> **Cohort Discovery != Candidate Identity Disclosure**

This should be developed further with Research.

## 27.8 Protected-source due process

Where PLE uses protected intelligence or other non-disclosable sources, the resulting answer must not become unchallengeable secret authority.

> **Protected Source != Unchallengeable Conclusion**

> **PLE Must Not Become Secret Evidence Laundering**

Law/Judiciary must provide the applicable contestability and explanation architecture.

## 27.9 Consequential-action boundary

PLE produces information/evaluation state.

It does not supply execution authority.

**PLE Result**
→ substantive domain interpretation
→ applicable authority/context/transition checks
→ commit
→ execute.

> **Match != Authority To Act**

## 27.10 Aggregation remains separate

Participant-level local evaluation and population aggregation are distinct operations.

Research statistics may require:
- separate basis;
- aggregation threshold;
- statistical disclosure control;
- query-composition protection;
- output-precision limits.

> **Local Contribution != Automatic Aggregate Collection Authority**

## 27.11 Revised maturity

Following adversarial transfer across genomics, medication safety, Education, civil status, finance, employment, Research recruitment, security-sensitive information and civil notification:

**TRANSFER:** PASS

**DISTINCTNESS FROM CWA/CIBB:** PASS

**GENERAL PRIVACY VALUE:** HIGH

**CUMULATIVE DISCLOSURE RISK:** MATERIAL BUT ARCHITECTURALLY ADDRESSABLE

**CURRENT STATUS:** PMEDG CANDIDATE — CROSS-DOMAIN TRANSFER PASSED — DO NOT EXTRACT YET

The next step is a frozen blind cross-instance test after preparation of a candidate development specification/test package.
