# Bootstrap Succession Record — Pre-Schema Adversarial Evaluation 001

**Project:** The Concord  
**Date:** 1 October 2026  
**Subject:** Bootstrap Succession Record — Formal Specification 001  
**Status:** INTERNAL ADVERSARIAL EVALUATION / PRE-SCHEMA

## 1. Method

Treat BSuR Specification 001 as fixed.

Test whether the record can represent succession without silently importing authority, forcing a clean-success narrative, erasing residual control, or confusing technical continuity with institutional legitimacy.

A representational failure is distinguished from an external constitutional question.

## 2. Planned Scenario Results

### A1 — Clean planned graduation
Provisional service is tested, a successor obtains an independent legitimate basis, assets/functions move, predecessor retires.

**PASS.**

AuthorityBefore, AuthorityAfter, function/asset transitions, explicit non-transfer, retirement and provenance represent the transition.

### A2 — Partial function transfer
Only two of five functions move.

**PASS WITH REPRESENTATIONAL GAP.**

FunctionTransition can represent each function, but AuthorityNotTransferred[] is not formally bound to FunctionID/scope. In a multi-function transition, a serializer could lose which non-transferred power belongs to which function.

### A3 — One predecessor / multiple successors
Functions split among three successors.

**PASS.**

Plural parties plus per-function IntendedSuccessor represent the topology.

### A4 — Multiple predecessors / one successor
A successor consolidates functions from several provisional services.

**PARTIAL PASS / REPRESENTATIONAL GAP.**

Parties are plural, but FunctionTransition contains FunctionID without an explicit PredecessorReference. FunctionID collision or ambiguous provenance is possible across predecessor services.

### A5 — Technical handover without authority
Keys, domains and software move; successor has no valid authority basis.

**PASS.**

Technical completion and AUTHORITY_UNRESOLVED can coexist.

### A6 — Authority basis without technical handover
A legitimately authorised successor exists but predecessor still controls infrastructure.

**PASS.**

AuthorityAfter and asset/control transition are independent.

### A7 — Hostile control takeover
Successor captures infrastructure but lacks legitimate authority.

**PASS.**

Hostile trigger, effective control, disputes and authority separation represent it.

### A8 — Predecessor refuses retirement
Nominal successor exists while predecessor continues operating.

**PASS.**

FAILED_TO_RETIRE and residual state represent this.

### A9 — Hidden residual access discovered later
Predecessor retained an undeclared key.

**PASS WITH REPRESENTATIONAL CLARIFICATION.**

Residual access can be recorded, but the model should distinguish declared residual access from later-discovered residual access and its observation/effective time.

### A10 — Emergency continuation exceeds sunset
Emergency successor keeps operating after temporary authority expires.

**PASS.**

Sunset/review and residual authority state support detection; BSuR-21 blocks permanence inference.

### A11 — Participant lock-in
Participants cannot practically exit during transfer.

**PASS.**

ParticipantImpact and exit/portability consequences can represent capture.

### A12 — Identity mapping dispute
Parties disagree whether successor is same institution, fork, or new entity.

**PASS.**

Identity states include unresolved/disputed/forked/successor/reconstructed.

### A13 — Record loss and duplication
Some records transfer, some are duplicated, some lost.

**PASS WITH REPRESENTATIONAL GAP.**

The specification lists these states, but RecordTransition lacks a formal relation object binding RecordClass/Source/Destination/TransferState/ResidualCopy/ProtectionState.

### A14 — Dependency prevents independence
Successor remains operationally dependent on predecessor.

**PASS WITH REPRESENTATIONAL GAP.**

Dependency information is required, but DependencyTransition is not formally defined as a relation binding dependency, scope/function, before/after state, criticality, controller and evidence.

### A15 — Constitutional process unavailable
A Z5-like function requires constitutional basis but no constitutional process exists.

**PASS.**

CONSTITUTIONAL_PROCESS_UNAVAILABLE remains representable and does not permit self-authorisation.

### A16 — Fraudulent successor claim
An unrelated actor publishes a BSuR claiming succession.

**PASS.**

BSuR is evidentiary, not authority; competing records and disputes remain representable.

### A17 — Successor failure and rollback
Transfer completes, successor fails, some functions return to predecessor.

**REPRESENTATIONAL GAP.**

REVERSED exists, but the model does not explicitly distinguish:
- rollback to prior state;
- new reverse transition;
- partial rollback;
- authority reactivation;
- technical reactivation.

A naive implementation could treat rollback as automatic restoration of predecessor authority.

### A18 — Simultaneous competing BSuRs
Several observers publish incompatible transition records.

**PASS.**

Multiple BSuRs are explicitly allowed and publication order is not authority.

## 3. Cross-Cutting Attack Tests

### X1 — Same-institution bypass
Successor claims SAME_CONTINUING_IDENTITY and therefore copies AuthorityBefore into AuthorityAfter.

**PASS at principle level; binding repair needed.**

BSuR-08 and BSuR-14 reject the inference, but machine representation needs authority transition bound to the specific function and predecessor/successor references.

### X2 — Possession-to-power attack
Successor possesses all assets, records and keys.

**PASS.**

No tested possession state creates authority.

### X3 — Emergency permanence attack
Emergency service becomes indispensable and argues dependency/popularity renews its authority.

**PASS.**

BSuR-11, BSuR-12, BSuR-21 and BSuR-25 block the inference.

### X4 — Paper retirement / practical control
Predecessor is marked RETIRED but retains root credentials and a critical dependency.

**PASS WITH REPRESENTATIONAL CLARIFICATION.**

The contradiction is representable, but RetirementResidual should bind declared retirement state to observed residual controls/dependencies and verification state.

### X5 — Successor-by-registry-consensus
Several registries agree that one claimant is the successor.

**PASS.**

Registry observation is not adjudication.

### X6 — Authority laundering through merger
Two services with different bounded authorities merge and claim the union of both authorities for all functions.

**SUBSTANTIVE REPRESENTATIONAL GAP.**

AuthorityBefore/After are described per function, but the formal object does not yet define an AuthorityTransition relation that binds:
- predecessor service;
- predecessor function;
- successor service;
- successor function;
- before claim/basis/scope;
- after claim/independent basis/scope;
- non-transferred authority;
- threshold state;
- evidence.

Without that relation, a serializer could permit scope union/laundering during merge/split.

### X7 — Asset bundle ambiguity
A database, domain and key transfer to different successors.

**REPRESENTATIONAL GAP.**

Asset transition requirements are prose fields but no formal AssetTransition relation binds asset, source, destination, controller before/after, transfer state and residual control.

### X8 — Participant impact differs by function/population
One population is unaffected; another loses access and exit.

**REPRESENTATIONAL GAP.**

ParticipantImpact is not formally scoped to function/population/consequence.

## 4. Findings

### P1 — Transition Relations Need Explicit Source/Destination Binding

**Classification:** SUBSTANTIVE REPRESENTATIONAL GAP / NOT NEW BOOTSTRAP ABSTRACTION.

The top-level architecture is sound, but several transition dimensions remain prose lists rather than formal relations.

Required relation objects:
- FunctionTransition;
- AssetTransition;
- RecordTransition;
- DependencyTransition;
- AuthorityTransition;
- ParticipantImpact.

Each must identify relevant predecessor/source, successor/destination, scope/function and state.

### P2 — Authority Non-Transfer Must Be Function/Scope Bound

**Classification:** SUBSTANTIVE REPRESENTATIONAL GAP.

AuthorityNotTransferred[] cannot remain an unbound list in a multi-party/multi-function succession.

It should live inside or reference AuthorityTransition and identify:
- authority/power;
- function;
- scope;
- predecessor holder;
- proposed/actual successor;
- reason/state;
- evidence.

### P3 — Rollback Is a New Transition, Not Automatic Restoration

**Classification:** SUBSTANTIVE SEMANTIC CLARIFICATION.

A rollback must not reactivate predecessor authority merely because predecessor infrastructure still exists.

Required rule:

> **Rollback Of Function != Automatic Restoration Of Prior Authority**

A reverse/rollback event must independently represent current authority basis, technical control and participant consequence.

### P4 — Residual State Needs Observation Semantics

**Classification:** REPRESENTATIONAL CLARIFICATION.

Residual access/control should distinguish:
- declared at transfer;
- observed later;
- effective interval;
- verification state;
- disputed/unknown.

This allows hidden residual control to be discovered without rewriting history.

### P5 — Identity Mapping Needs Object-to-Object Binding

**Classification:** REPRESENTATIONAL GAP.

IdentityMapping lists identity classes and states but does not formally bind:
- source identity/reference;
- destination identity/reference;
- mapping state;
- scope;
- evidence;
- verification/dispute state.

### P6 — Transition-Level State Is Not Enough

**Classification:** REPRESENTATIONAL GAP.

One overall transition may be COMPLETED while:
- a function is PARTIALLY_COMPLETED;
- authority is UNRESOLVED;
- records are FAILED;
- retirement is DISPUTED.

Each transition relation needs its own state. Top-level state should be summary/derived or explicitly non-authoritative.

## 5. Architecture Check

No finding requires:
- reopening Zero-Infrastructure Bootstrap;
- a new succession authority;
- a new constitutional mechanism;
- a central identity authority;
- a new civilisational abstraction layer.

The failures arise from converting the sound succession architecture into a multi-party relational record.

## 6. Disposition

**Specification 001 pre-schema result:** REVISION REQUIRED.

**Architectural discovery reopened:** NO.

**New bootstrap abstraction required:** NO.

**Reason:** relational completeness and prevention of authority laundering during split/merge/rollback.

Create BSuR Formal Specification 002 before serialization.

Specification 002 should:
1. formalise source/destination relation objects;
2. introduce AuthorityTransition;
3. bind AuthorityNotTransferred to function/scope/parties;
4. formalise identity mapping;
5. make rollback a new transition requiring current authority trace;
6. formalise residual observations;
7. scope participant impact;
8. make top-level transition state summary/non-authoritative where component states differ.

No JSON Schema should be produced from Specification 001.
