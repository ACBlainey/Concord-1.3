# Bootstrap Succession Record — Pre-Schema Adversarial Evaluation 002

**Project:** The Concord  
**Date:** 1 October 2026  
**Subject:** Bootstrap Succession Record — Formal Specification 002  
**Status:** SECOND ADVERSARIAL / REGRESSION / COMPOSITION TEST

## 1. Method

Specification 002 was treated as fixed.

The evaluation repeated the 18 scenarios from Evaluation 001 and then attacked the new relational model through split/merge composition, rollback, multi-hop succession, cyclic claims, residual-control discovery and mixed component states.

The test asks whether the semantic model can represent the state without:
- manufacturing authority;
- deleting uncertainty;
- collapsing source/destination identity;
- forcing transition success;
- hiding residual control;
- treating a summary as component truth.

## 2. Original Scenario Regression

### A1 Clean planned graduation — PASS
Independent AuthorityAfter basis, scoped transfer and retirement are representable.

### A2 Partial function transfer — PASS
AuthorityNotTransferred is now bound through AuthorityTransition to source/destination function and scope.

### A3 One predecessor / multiple successors — PASS
Separate FunctionTransitions and AuthorityTransitions represent each branch.

### A4 Multiple predecessors / one successor — PASS
SourceService + SourceFunctionID eliminate cross-predecessor FunctionID ambiguity.

### A5 Technical handover without authority — PASS
AssetTransition may complete while AuthorityAfter remains unresolved/unverified.

### A6 Authority basis without technical handover — PASS
Authority and infrastructure remain independently representable.

### A7 Hostile control takeover — PASS
Effective control can change without authority transition becoming legitimate.

### A8 Predecessor refuses retirement — PASS
RetirementState + residual observations preserve contradiction.

### A9 Hidden residual access discovered later — PASS
ResidualObservation distinguishes DISCOVERED_LATER and preserves observation/effective times.

### A10 Emergency continuation exceeds sunset — PASS
Current authority state remains independently testable after sunset.

### A11 Participant lock-in — PASS
ParticipantImpact binds function, population, exit effect and consequence.

### A12 Identity mapping dispute — PASS
Object-to-object mapping, verification and dispute states preserve uncertainty.

### A13 Record loss/duplication — PASS
RecordTransition explicitly represents copy/retention/loss/protection states.

### A14 Dependency prevents independence — PASS
DependencyTransition binds function scope, controllers, criticality and independence claim.

### A15 Constitutional process unavailable — PASS
CONSTITUTIONAL_PROCESS_UNAVAILABLE remains representable without self-authorisation.

### A16 Fraudulent successor claim — PASS
A record can preserve the claim while authority remains unsupported/disputed.

### A17 Successor failure and rollback — PASS
Rollback is a new relation set and does not reactivate historical authority automatically.

### A18 Simultaneous competing BSuRs — PASS
Competing records remain possible; record priority does not create authority.

**Regression result: 18/18 PASS.**

## 3. Relational Composition Attacks

### C1 Merger authority union
Two predecessors hold distinct bounded authorities; successor claims both across a merged function.

**PASS.**
AuthorityTransition remains per source/destination function and BSuR-31/40 reject topology-created scope expansion.

### C2 Split authority replication
One bounded predecessor function splits into three successor services, each claiming the complete predecessor authority.

**PASS.**
Separate AuthorityTransitions require independent AuthorityAfter basis and scoped non-transfer.

### C3 Same-identity authority inheritance
Successor is mapped SAME_CONTINUING_IDENTITY and copies predecessor authority.

**PASS.**
IdentityMapping is independent; BSuR-17 and AuthorityAfter requirements block inheritance.

### C4 Multi-hop succession
A→B→C. C cites A's historical authority while B's authority was unresolved.

**PASS.**
Each transition has its own authority trace; historical provenance does not bypass the current independent-basis requirement.

### C5 Cyclic succession claims
A says successor B; B says successor C; C says successor A.

**PASS.**
Relations are evidentiary claims, not an authority-generating graph. Cycles do not create legitimacy.

### C6 Many-to-many function reorganisation
Three predecessor functions are recomposed into four successor functions.

**PASS.**
Source/destination binding can express the graph without global FunctionID assumptions.

### C7 Mixed component completion
Assets complete, records partial, dependencies unresolved, authority disputed.

**PASS.**
Component relation states remain primary; top-level summary is non-authoritative.

### C8 Record copy masquerades as transfer
Successor receives a full copy while predecessor retains live writable copy.

**PASS.**
CopyState and residual observations distinguish duplication from completed exclusive transfer.

### C9 Operational independence claim with hidden common dependency
Two apparent successors rely on the same predecessor-controlled identity service.

**PASS.**
CommonDependencyRefs, controller states and later residual observations can expose the dependency.

### C10 Late residual discovery after declared retirement
Root key discovered months after predecessor marked RETIRED.

**PASS.**
Append-representable residual observation does not rewrite the historical record and can place retirement verification into dispute.

### C11 Rollback to technically intact predecessor
Old infrastructure is restored after successor failure, but predecessor's prior delegation expired.

**PASS.**
Rollback requires current AuthorityTransition; historical delegation is not automatically revived.

### C12 Emergency successor becomes indispensable
Participants depend on emergency successor after sunset.

**PASS.**
Dependency and participant impact are representable; neither renews authority.

### C13 Registry consensus on successor
Many BSR registries cite the same BSuR.

**PASS.**
Observation/consensus does not adjudicate succession authority.

### C14 Conflicting identity mappings
One BSuR says SAME_CONTINUING_IDENTITY; another says FORKED_IDENTITY.

**PASS.**
Competing BSuRs and disputed mappings remain representable.

### C15 Partial constitutional grounding
One successor function is constitutionally grounded; another is below threshold; a third requires basis but process unavailable.

**PASS.**
Threshold belongs to AuthorityTransition/function, avoiding whole-institution flattening.

## 4. Boundary Attacks

### B1 Empty destination
Predecessor retires a function with no successor.

**PASS.**
Destination may be null/unresolved.

### B2 Empty source
A reconstructed/new function appears during recovery without a clean predecessor.

**PASS.**
Source may be null/unresolved; provenance can still link context without inventing identity continuity.

### B3 AuthorityNotTransferred omitted on non-authority function
No authority-bearing function is involved.

**PASS.**
Mandatory condition is correctly scoped to authority-bearing transitions.

### B4 AuthorityNotTransferred omitted on authority-bearing function
**SEMANTIC FAIL AS INTENDED.**
Validation U9 detects the omission.

### B5 Summary says COMPLETED while authority disputed
**SEMANTIC FAIL if implementation treats summary as authoritative; otherwise representable contradiction.**
BSuR-35 requires component truth to dominate.

### B6 Residual access exists but is legitimate archival read-only
**PASS.**
Residual access does not automatically imply residual governance.

## 5. Remaining Formalisation Notes

No new semantic relation is required.

Serialization must preserve:
1. nullable/unresolved source and destination without turning null into absence-of-evidence certainty;
2. extensible vocabulary handling comparable to BSR Schema 002;
3. separate verification/integrity/freshness/dispute state spaces;
4. component states over summary;
5. multiple competing relations rather than uniqueness constraints that delete contradiction;
6. evidence references and temporal observation for later-discovered residual control;
7. scoped AuthorityNotTransferred entries;
8. no schema-level inference that validates authority merely from a populated IndependentBasis string.

These are serialization/semantic-validator requirements, not reasons for Specification 003.

## 6. Authority Non-Capture Review

Tested possible authority creation through:
- succession record publication;
- first publication;
- asset possession;
- record possession;
- technical control;
- effective control;
- same identity;
- merger;
- split;
- rollback;
- emergency operation;
- dependency;
- popularity;
- registry consensus;
- retirement declaration;
- historical authority;
- transition completion.

**No tested route creates authority by itself.**

## 7. Representational Completeness

Within the tested succession scope, Specification 002 can represent:
- clean, failed, partial, hostile and disputed transitions;
- one-to-one, one-to-many, many-to-one and many-to-many topology;
- technical/authority divergence;
- identity uncertainty;
- record duplication/loss;
- dependency capture;
- participant lock-in;
- residual control;
- rollback;
- emergency sunset;
- constitutional-process absence;
- competing records.

**Result: PASS.**

## 8. Disposition

**Specification 002 pre-schema adversarial result:** PASS.

**Original regressions:** 18/18 PASS.

**Additional composition/boundary tests:** PASS within intended semantic scope.

**Specification 003 required:** NO.

**Architectural discovery reopened:** NO.

**New bootstrap abstraction required:** NO.

**Semantic model stable for serialization:** YES, within tested scope.

Freeze BSuR Specification 002 as the semantic source for JSON Schema 001.

If serialization reveals a semantic impossibility, source-resolve it explicitly rather than silently altering Specification 002.
