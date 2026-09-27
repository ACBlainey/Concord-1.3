# Architectural Unit Resolution — Concord Method v1.0

**Status:** CURRENT CORRIGIBLE CONCORD METHODOLOGY — INTEGRATED / ARCHITECTURAL INTERFACE RETEST PASSED
**Version:** 1.0
**Date:** 24 September 2026
**Source lineage:** Architectural Unit Resolution v0.1 — Pre-Gap Node and System-Family Classification
**Validation lineage:** AUR portable development → BTT-001 → BTT-002 → Portable Module v1.0 → Back-Propagation Audit 001
**Canonical role:** Pre-gap diagnostic method within CDT / CRADP source-resolution and gap-classification work

## 1. Purpose

Architectural Unit Resolution (AUR) determines **what architectural unit should actually be evaluated before a local omission is classified as a structural gap**.

Its core safeguards are:

> **Document ≠ necessarily System**

> **Missing locally ≠ missing architecturally**

> **Named neighbour ≠ adequate interface**

AUR is a pre-gap diagnostic gate. It does not replace CRADP, State and Maturity Mapping, KCS, ESCP or domain-specific evaluation.

## 2. Core sequence

**Candidate Local Deficit**
→ **Resolve Architectural Unit**
→ **Resolve Legitimate Local Scope**
→ **Resolve Relevant System Family**
→ **Test Interface / Distributed Satisfaction**
→ **Decompose Missing Function Where Necessary**
→ **Classify**
→ **Preserve Search Scope, Uncertainty and Provenance**

Do not classify a local omission as a structural gap before this sequence has been performed to the degree justified by consequence and available evidence.

## 3. Functional unit types

Where evidence permits, classify a source as one or more of:

- **Canonical Integrated Architecture (CIA)**
- **Subsystem (SUB)**
- **Interface / Bridge (INT)**
- **Portable Module (PM)**
- **Companion / Developed Concept (CDC)**
- **Development Note (DN)**
- **Constitutional/Core Source (CORE)**
- **Method / Epistemic Tool (MET)**
- **Reference / Provenance Source (REF)**
- **Unresolved Unit (UNK)**

Typing is functional, not hierarchical.

> **Architectural Role ≠ Civil Authority**

## 4. Local ownership and architectural satisfaction are separate

For tested relation/function R in unit D, ask two distinct questions.

### 4.1 Local-scope state

Does D legitimately own R?

Candidate states:

- LOCAL;
- INTENTIONALLY NON-LOCAL;
- SHARED / DISTRIBUTED;
- INAPPLICABLE;
- UNKNOWN / DISPUTED.

### 4.2 Architectural satisfaction state

If R is not local, is it adequately supplied for D's required function?

A function may be intentionally outside D while still being fully satisfied by another legitimate owner.

Therefore:

> **Intentional Non-Ownership ≠ Architectural Deficit**

and:

> **External Capability Exists ≠ External Satisfaction Established**

## 5. System-family closure

For unit D and relation R:

**Family(D,R) = D + source-grounded architectural neighbours materially required to evaluate R for D's declared function.**

Family membership may be supported by:

- explicit interface;
- declared dependency;
- canonical status;
- source-grounded functional dependency;
- provenance establishing a current operative relation.

Topical similarity alone is insufficient.

Family search is bounded. It is not unrestricted corpus expansion.

Record both:

- the resolved family;
- evidence supporting membership.

## 6. Current, historical and candidate relations

Do not collapse architectural time/state.

Distinguish:

- **CURRENT** — presently operative dependency/interface;
- **HISTORICAL** — prior/decommissioned relation retained for provenance;
- **CANDIDATE** — planned, future-facing or speculative relation not yet established;
- **UNKNOWN / DISPUTED**.

> **Future Reference ≠ Current Architectural Dependency**

> **Named but Unresolved Candidate ≠ Current Family Member**

Historical architecture may explain provenance without satisfying a current operational requirement.

## 7. Interface adequacy

Delegation/external satisfaction requires more than a neighbour's name.

Test enough of:

**Source System**
→ **Trigger / Handoff**
→ **Responsible System**
→ **Required Function**
→ **Return / Consequence Propagation**
→ **Provenance**

Where relevant also test bounded authority, failure/degradation visibility and correction/review propagation.

A missing or inadequate link may establish an interface gap even where the external capability exists.

## 8. Distributed satisfaction

A required function may be legitimately supplied across several architectural units.

Do not require one document/system to contain the entire workflow where distributed ownership is intended and the interfaces are adequate.

> **Distributed Function ≠ Structural Absence**

But:

> **Distributed Fragments ≠ Integrated Workflow**

Distributed satisfaction must still demonstrate sufficient connection for the tested function.

## 9. Decompose before classifying

A workflow can contain different deficit types at different sub-functions.

Before classifying a broad workflow:

> **Do Not Classify the Workflow Before Decomposing the Missing Function**

At the smallest meaningful functional resolution:

- existing capability + inadequate connection → **INTERFACE GAP**;
- no adequate capability/owner established in the resolved family → **FAMILY-LEVEL STRUCTURAL GAP**.

A single workflow may contain both.

## 10. Classification vocabulary

AUR uses the following architectural outcomes:

### AUR-C1 — LOCALLY SATISFIED
Required function is adequately supplied within the audited unit.

### AUR-C2 — INTENTIONAL LOCAL SCOPING
R belongs to the wider architectural setting but is legitimately outside this unit's intended local ownership. Use as primary outcome where no external-satisfaction claim is required to establish adequacy.

### AUR-C3 — EXTERNALLY SATISFIED
R is intentionally non-local and adequately supplied by an identified legitimate external owner/interface.

### AUR-C4 — DISTRIBUTED SATISFACTION
R is adequately supplied through multiple legitimate units/interfaces.

### AUR-C5 — LOCAL REPRESENTATION GAP
Underlying local architecture/function exists but the audited representation does not adequately show it.

### AUR-C6 — INTERFACE GAP
Required capability exists in the resolved family but invocation, handoff, return, consequence propagation, provenance or another required interface element is inadequate.

### AUR-C7 — FAMILY-LEVEL STRUCTURAL GAP
A required capability/owner is not established within the resolved family and bounded search scope.

### AUR-C8 — INAPPLICABLE
R does not apply to the audited unit/family in the relevant context. This includes rejected unrelated candidates and obsolete units when evaluated as current operators.

### AUR-C9 — UNRESOLVED
Available evidence/search scope is insufficient to establish another classification.

These classifications may coexist at different sub-functions. Do not force a complex workflow into one universal class.

## 11. C2 versus C3

Where R is intentionally non-local **and** adequately supplied externally:

- primary architectural result: **AUR-C3 EXTERNALLY SATISFIED**;
- local-scope rationale: intentional non-ownership.

Use C2 as primary only where the question ends at legitimate local scope and no external-satisfaction claim is needed.

## 12. C2 versus C8

Use C2 when the unit legitimately participates in the architectural setting but does not own R.

Use C8 where R itself is not applicable to that unit/family in the audited context.

## 13. C6 versus C7

Use the smallest meaningful functional resolution.

> Existing required capability + inadequate connection = **C6**

> No adequate required capability/owner established = **C7**

Do not classify an entire workflow C7 merely because its integration is incomplete.

## 14. Diagnostic closure

Family closure means sufficient resolution to make the bounded diagnosis justified by the evidence.

It does not mean the required function succeeds.

> **Diagnostic Closure ≠ Functional Satisfaction**

A family may close diagnostically with C3, C4, C6, C7, C8 or, where search has reached a justified boundary without resolution, C9.

## 15. ESCP boundary

AUR operationalises ESCP at architectural-unit scale.

> **Not Represented Locally ≠ Absent Architecturally**

But also:

> **Possible External Ownership ≠ Demonstrated External Satisfaction**

and:

> **No Adequate Mechanism Found Within Resolved Family/Search Scope ≠ No Mechanism Exists Anywhere**

C7 is therefore always scope-bound to the resolved family and evidence/search record.

Preserve UNKNOWN rather than converting incomplete evaluation space into certainty.

## 16. Minimum output record

An AUR assessment should preserve:

1. target unit/source;
2. declared purpose/status;
3. tested relation/function;
4. local ownership/scope state;
5. unit type(s);
6. relevant family;
7. family-membership evidence;
8. current/historical/candidate dependency status;
9. local capability state;
10. external/distributed capability state;
11. interface-adequacy result;
12. functional decomposition where required;
13. AUR classification(s);
14. diagnostic-closure state;
15. functional-satisfaction state;
16. uncertainty/dispute;
17. search scope;
18. provenance.

## 17. Relationship to CRADP

AUR is the pre-gap unit-resolution gate inside the wider CRADP cycle.

CRADP asks whether an apparent deficit is real, who owns it, how dependencies behave, what response is justified and whether intervention resolves it.

AUR specifically strengthens the transition:

**Candidate Deficit**
→ **Source Resolution**
→ **Architectural Unit / Family Resolution**
→ **Gap Classification**

CRADP's wider response routes, prediction freeze, development, propagation, retest and recursive-method check remain outside AUR.

## 18. Relationship to State and Maturity Mapping

SMM distinguishes represented state from complete system reality and local maturity from context-relative sufficiency.

AUR supplies a precondition for fair maturity/gap interpretation:

> **M_document(D) ≠ necessarily M_family(F(D))**

A partial document should not lower family-level maturity merely because an intentionally external function is absent locally.

Conversely, a family-level maturity claim requires demonstrated interface/distributed satisfaction rather than a named neighbour.

## 19. Relationship to KCS

KCS can supply dependency state, provenance, current/historical relations and candidate review information.

AUR consumes that evidence to resolve family membership and interface state.

AUR does not make KCS complete by assumption.

> **No Recorded Dependency ≠ No Dependency**

KCS graph absence remains evidence-state information, not universal architectural absence.

## 20. Relationship to Active Development

AUR should be applied before a candidate architectural omission is promoted into a development problem where the omitted function may legitimately exist elsewhere.

Possible AUR results may route Active Development toward:

- no change;
- representation correction;
- interface development;
- legitimate-owner development;
- bounded structural invention;
- hold / further source resolution.

AUR does not itself authorise development.

## 21. Failure modes

Guard against:

1. **Document = System error**
2. unrestricted family expansion
3. family membership inferred from topical similarity
4. named neighbour accepted without adequate interface
5. local omission promoted directly to structural absence
6. external capability used to hide interface failure
7. historical/candidate architecture treated as current satisfaction
8. entire workflow classified before missing sub-function decomposition
9. unresolved scope converted into certainty
10. functional unit labels treated as hierarchy/authority
11. diagnostic closure treated as functional success
12. bounded C7 converted into universal absence
13. current representation treated as complete evaluation space

## 22. Validation and evidence status

The original AUR v0.1 was frozen as an experimental method before CH005.

Portable development subsequently produced:

- BTT-001: **15/15 frozen predictions materially confirmed**;
- BTT-002: **17/17 frozen predictions materially confirmed**;
- no fundamental failure detected in either blind test;
- successful false-gap prevention;
- successful genuine-gap detection;
- bounded family construction;
- interface-adequacy testing;
- current/historical/candidate separation;
- diagnostic closure without false functional satisfaction;
- preserved ESCP discipline.

These results justify promotion into current corrigible Concord methodology.

They do **not** establish universal validity, empirical outcome superiority, complete source recovery or error-free classification in all domains.

## 23. Corrigibility

AUR remains revisable.

Future use should record:

- false positives;
- false negatives;
- ambiguous family boundaries;
- interface classifications that fail under implementation;
- cases where bounded search systematically misses relevant owners;
- cases where classification vocabulary obscures rather than clarifies the architecture.

Material defects should route through Active Development and, where a revised portable module is later graduated, through the portable-module back-propagation process.

## 24. Final constraint

AUR exists to improve diagnosis before architectural development.

It must not convert:

**better source resolution → assumed completeness**

**dependency visibility → authority**

**external capability → presumed adequate interface**

**bounded structural-gap evidence → universal absence**

or

**methodological validation → immunity from correction**.
