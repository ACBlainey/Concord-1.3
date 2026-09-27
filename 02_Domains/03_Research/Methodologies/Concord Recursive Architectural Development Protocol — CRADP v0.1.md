# Concord Recursive Architectural Development Protocol — CRADP v0.1

**Status:** V1.2a PORTABLE EXPERIMENTAL OPERATING PROTOCOL  
**Date:** September 2026  
**Canonical effect:** NONE  
**Purpose:** permit a fresh AI/human research instance to perform architectural gap detection, upstream-bottleneck identification, bounded development and retest without reconstructing the entire V1.2a research trail first.

# 1. What This Protocol Does

CRADP is a portable procedure for asking:

1. What is the current architecture?
2. Where does an applicable architectural requirement first fail?
3. Is the apparent gap real?
4. If real, who legitimately owns the missing capability?
5. Is the problem structural, integrative, developmental or contextual?
6. Should the response be reuse, interface, upstream development, hold or invention?
7. Did the intervention actually resolve the original gap?
8. What changed elsewhere as a consequence?
9. Did use of the development method expose a defect in the method itself?

The protocol is diagnostic and developmental.

It is not a governance authority.

# 2. Required Inputs

A new instance should have access to:

- the target Concord corpus/version;
- the current frozen ethical/constitutional constraints;
- the frozen Abstraction Layer Ladder;
- the AL interface/context rules;
- the Relational Grammar;
- ESCP;
- available State Map/CCSSL data;
- available KCS/KMDI dependency data;
- relevant provenance/history.

If some inputs are unavailable, record UNKNOWN rather than silently reconstructing them.

# 3. Core Safeguards

## 3.1 ESCP

Being right about everything measured does not prove everything relevant was measured.

Therefore:

NoSourceFound
NOT=> SourceDoesNotExist.

NoRecordedDependency
NOT=> NoDependency.

NoRecordedGap
NOT=> CompleteArchitecture.

## 3.2 No Local-Invention Presumption

MissingLocalCapability(A,x)
NOT=> Invent(A,x).

## 3.3 No Authority From Analysis

DevelopmentLeverage
NOT=> CivilAuthority.

DependencyCentrality
NOT=> Authority.

Measurement
NOT=> Governance.

## 3.4 Provenance

Do not rewrite earlier predictions, requirements or failed hypotheses after results are known.

Add corrections/supersession records.

# 4. Operating Cycle

Use the following cycle:

Current Architecture
→ Context
→ AL Audit
→ Candidate Deficit
→ Source Resolution
→ Ownership Resolution
→ Dependency Trace
→ Gap Classification
→ Response Selection
→ Prediction Freeze
→ Development/Integration
→ Downstream Propagation
→ Retest
→ State/Dependency Update
→ Recursive Method Check
→ Repeat or Stop.

# 5. Step 1 — Define Audit Object and Context

Record:

- system/unit ID;
- document/version;
- owner/domain;
- intended function;
- deployment context;
- consequence class;
- participant exposure;
- authority exercised;
- known interfaces.

Use:

A(S|c)

where S is system and c is audited context.

Do not assume one context-free AL if deployment changes applicable requirements.

# 6. Step 2 — Establish Current State

Retrieve or construct the minimum current state:

- purpose/function;
- capabilities;
- unresolved questions;
- maturity dimensions;
- validation/evidence;
- provenance;
- upstream dependencies;
- downstream dependents;
- interface state;
- recent material transitions;
- stale/unknown information.

Treat State Map/CCSSL as synthesis over source-owned claims, not sovereign truth.

# 7. Step 3 — Run Cumulative AL Audit

For each layer from AL0 upward, test every applicable requirement.

Requirement state:

R(S,r,c) ∈ {
SATISFIED-INTERNAL,
SATISFIED-INTERFACE,
NOT-APPLICABLE,
UNSATISFIED,
UNKNOWN,
DISPUTED
}.

Stop contiguous completeness at the first layer containing an unresolved applicable requirement.

Record higher-layer feature exposure separately.

Never allow an AL7-like feature to conceal an AL2 deficit.

# 8. Step 4 — Test Applicability

Before calling a requirement missing, ask whether its trigger exists in context c.

N/A requires rationale.

N/A(r,S,c1)
NOT=> N/A(r,S,c2).

If applicability cannot be established:

UNKNOWN.

# 9. Step 5 — Test Interface Satisfaction

A capability may be legitimately external.

SATISFIED-INTERFACE requires:

1. identifiable legitimate owner;
2. owner actually has sufficient capability;
3. sufficient interface;
4. bounded authority;
5. visible dependency;
6. failure/degradation representable;
7. correction/review propagation where material;
8. no hidden sovereignty/unreviewable monopoly.

Existence of another system alone is insufficient.

# 10. Step 6 — Candidate Gap Record

For every first unresolved applicable requirement, create a candidate record:

- target system;
- requirement;
- context;
- evidence located;
- evidence not located;
- current classification;
- possible owner;
- known dependencies;
- uncertainty;
- search scope.

Do not call it a structural gap yet.

# 11. Step 7 — Mandatory Source Resolution

Search the corpus before development.

Search:

- target system;
- likely owner systems;
- constitutional interfaces;
- portable modules;
- development notes;
- archive/provenance where relevant;
- later reconstructions;
- machine-readable/state/dependency records.

Possible outcomes:

A. capability already exists locally;
B. capability exists externally with sufficient interface;
C. capability exists externally but interface is missing/partial;
D. owner exists but capability maturity is insufficient;
E. function exists in distributed fragments;
F. no verified satisfying mechanism found within searched scope;
G. search remains insufficient/ambiguous.

Never convert F or G into universal absence.

# 12. Step 8 — Resolve Legitimate Owner

Ask:

> Which architecture should legitimately own this capability?

Use function and bounded scope, not convenience.

Possible outcomes:

- target system legitimately owns it;
- another system owns it;
- shared/interface ownership;
- owner unresolved;
- no legitimate owner exists yet.

Do not duplicate a capability locally merely because the target needs it.

# 13. Step 9 — Trace Upstream Dependencies

For target A requiring x from owner B:

A --requires x--> B.

Assess:

M(B)

against:

R(B|A,x).

If:

M(B) < R(B|A,x)

classify a Developmental Dependency Gap.

If multiple systems require the same insufficient upstream capability:

{A1,A2,...An} --require x--> B

then B is a candidate Upstream Development Bottleneck.

Test this against source evidence before development.

# 14. Step 10 — Gap Classification

Use at least:

## Structural Gap
Required function/legitimate owner absent.

## Integration Gap
Capability exists but necessary connection/interface is missing or inadequate.

## Developmental Dependency Gap
Correct owner exists but is not sufficiently developed for dependent requirement.

## Synthesis-State Gap
Required information exists across sources but is not integrated into a reusable current representation.

## Representation Gap
Underlying architecture exists but current map/document/model fails to represent it.

## Context Gap
Architecture adequate in one context but insufficient when additional triggers/consequences apply.

## False Positive
Source resolution finds adequate existing capability/interface.

## Unknown
Evidence/search insufficient.

# 15. Step 11 — Select Response

Route to exactly one primary response:

**REUSE** — adequate mechanism already exists.

**INTERFACE / INTEGRATE** — mechanism exists elsewhere/distributed; connect it.

**DEVELOP OWNER** — legitimate owner exists but capability is immature.

**HOLD** — evidence, ownership or requirement remains too uncertain.

**INVENT** — after internal source resolution, no verified satisfying mechanism/owner is available and the functional need remains.

Invention is the last route, not the default.

# 16. Step 12 — Freeze Prediction Before Intervention

Before changing architecture, write:

- identified deficit;
- proposed owner;
- proposed intervention;
- systems expected to improve;
- systems expected not to change;
- failure conditions;
- residuals expected to remain.

Example:

> If owner B is extended with capability x, local deficit d in A should collapse into an interface requirement and at least one other dependent of B should gain reusable capability.

Do not edit this prediction after results.

# 17. Step 13 — Develop Minimum Necessary Capability

Develop only enough architecture to test the hypothesis.

Avoid:

- speculative feature expansion;
- creating authority merely to solve coordination;
- duplicating legitimate owners;
- hiding uncertainty;
- treating conceptual elegance as validation.

Preserve explicit boundaries and residual questions.

# 18. Step 14 — Propagate Downstream

After upstream development:

B gains x
→ identify recorded dependents
→ test interface availability
→ route bounded review
→ update only materially affected downstream state.

Do not automatically rewrite every dependent.

# 19. Step 15 — Retest Original Deficit

Return to the exact frozen requirement.

Possible outcomes:

- RESOLVED;
- PARTIALLY RESOLVED;
- RECLASSIFIED;
- UNCHANGED;
- WORSENED;
- FALSE ORIGINAL DIAGNOSIS;
- NEW RESIDUAL EXPOSED.

A new residual is not failure if the original broad claim has genuinely narrowed.

# 20. Step 16 — Update State and Dependency Knowledge

Update, where available:

- CCSSL/State Map;
- KMDI dependency edges;
- AL requirement states;
- interface states;
- maturity dimensions;
- provenance;
- prediction result;
- unresolved residuals;
- last review.

Never silently replace the historical state.

# 21. Step 17 — Recursive Method Check

Ask whether use of CRADP exposed a defect in CRADP or its supporting models.

Candidate self-development event requires:

M_n
→ Use(M_n)
→ DetectGap(M_n)
→ Develop(M_n)
→ Retest(M_n+1)
→ ImprovedDiagnosticState.

Do not count a self-development event until the correction is retested.

# 22. Stopping Rules

Stop the cycle for a target when any of the following holds:

1. all currently applicable requirements through the target layer are satisfied;
2. remaining issue is UNKNOWN and further internal search is not justified;
3. ownership is unresolved and development would risk capture/duplication;
4. residual requires empirical/operational evidence unavailable in architecture work;
5. proposed change adds complexity without resolving a frozen deficit;
6. repeated passes generate no new material relation;
7. the issue has been routed to an external experiment/pilot/review;
8. further development would exceed the experiment's canonical boundary.

Do not continue generating architecture merely because another abstraction is imaginable.

# 23. Negative Results Are Valid

A successful CRADP run may conclude:

- no gap;
- existing architecture sufficient;
- apparent gap was representation error;
- system should not be developed;
- requirement is N/A;
- current evidence is insufficient;
- proposed invention is unnecessary.

These are positive methodological outcomes.

# 24. Minimal Output Record

Every run should produce:

1. Audit ID.
2. Target/system/context.
3. Sources searched.
4. Current AL and feature exposure.
5. First unresolved applicable requirement.
6. Source-resolution result.
7. Legitimate owner.
8. Dependency path.
9. Gap classification.
10. Selected response.
11. Frozen prediction.
12. Intervention if any.
13. Retest result.
14. Downstream effects.
15. Residuals.
16. State/KMDI/AL updates.
17. Recursive-method finding if any.

# 25. Handover Test

A fresh instance should be able to receive:

- this protocol;
- the frozen AL ladder/model;
- Relational Grammar;
- ESCP;
- access to the Concord corpus;

and then perform a bounded audit without being told which gap or bottleneck previous instances expect it to find.

For a clean test:

1. do not provide the expected answer;
2. choose a target not used to derive the protocol;
3. require explicit source citations/provenance;
4. freeze its diagnosis before revealing prior V1.2a results;
5. compare classifications and dependency paths;
6. record disagreements rather than forcing convergence.

# 26. Success Criteria for Cross-Instance Test

The protocol passes an initial portability test if an independent instance can:

- follow the steps without hidden oral context;
- avoid declaring absence before source resolution;
- distinguish local from upstream deficits;
- identify legitimate owners;
- avoid unnecessary invention;
- produce a reproducible gap classification;
- freeze a falsifiable prediction;
- identify stopping conditions;
- preserve uncertainty;
- reach materially comparable results on known calibration cases;
- discover at least one useful result on a blind case without being led to it.

# 27. Failure Criteria

The protocol requires revision if independent instances repeatedly:

- invent locally despite existing upstream owners;
- confuse feature exposure with contiguous AL;
- treat N/A as failure or Unknown as absence;
- cannot reproduce classifications from the same evidence;
- produce arbitrary AL scores;
- cannot distinguish owner maturity from interface failure;
- generate endless architecture without stopping;
- systematically converge only when given expected answers;
- cannot preserve provenance of prediction versus result.

# 28. Current Evidence Status

CRADP is assembled from multiple V1.2a prospective tests and two recorded recursive self-development events.

It has not yet passed an independent-instance portability test.

Therefore:

**PORTABLE EXPERIMENTAL PROTOCOL — READY FOR BLIND CROSS-INSTANCE TESTING.**

# 29. Compact Algorithm

INPUT: corpus C, target S, context c

1. state <- RetrieveCurrentState(S,C)
2. audit <- AuditAL(S,c)
3. r <- FirstUnresolvedApplicableRequirement(audit)
4. if no r: STOP / record no current gap
5. evidence <- SourceResolve(r,C)
6. owner <- ResolveLegitimateOwner(r,evidence)
7. deps <- TraceDependencies(S,owner,r)
8. class <- ClassifyGap(r,evidence,owner,deps)
9. action <- Route(class)
10. FreezePrediction(S,r,owner,action)
11. if action in {DEVELOP OWNER, INTERFACE}: implement minimum candidate
12. result <- Retest(S,r)
13. PropagateMaterialEffects(result,deps)
14. UpdateStateAndProvenance()
15. CheckMethodForSelfGap()
16. ApplyStoppingRules()
17. repeat only if a material unresolved requirement remains.

# 30. Final Constraint

The protocol exists to improve the Concord's ability to discover and correct its own architectural deficiencies.

It must never convert:

better mapping
→ unquestionable mapping,

better prediction
→ authority,

recursive development
→ compulsory development,

or

high abstraction level
→ greater moral or political worth.
