# Selective Context-State Transition Propagation — Cross-Domain Architecture 001

**Project:** The Concord Framework  
**Date:** 5 October 2026  
**Status:** CROSS-DOMAIN ARCHITECTURE / PROVISIONAL / NON-CANONICAL  
**Primary interfaces:** Context Composition and Evaluation-Space Completeness; Contextual Wrapper Architecture (CWA); Bounded Transition Architecture (BTA); KCS Change Propagation; State Triggered Review Architecture (STRA); State and Maturity Mapping (SMM); Decision Authorship and Contextual Participation; Evaluation-Space Completeness Problem (ESCP)

## 1. Purpose

A participant, object or function may occupy several contexts simultaneously.

When a material state changes in one context, other contexts may need:
- no response;
- review only;
- revalidation;
- suspension pending review;
- a separately authorised state transition;
- termination/reversion;
- or, in narrowly pre-authorised cases, an automatic bounded transition.

The central problem is:

> **When should a material state change in Context A cause anything to happen in Context B, and what exactly is permitted to propagate?**

The architecture must avoid two opposite failures:

1. **state isolation failure** — a materially dependent context continues unchanged even though a prerequisite changed;
2. **state bleed failure** — a state change in one context silently changes unrelated contexts.

This architecture applies the existing KCS Change Propagation grammar to contextual participant/system state without transferring ownership of those states to the propagation mechanism.

## 2. Source-resolved architectural basis

The relevant existing modules already establish:

BTA:

> **Transition != Dependency Propagation**

and:

> **Transition of an Object or Function != Transition of Every Attribute Attached to It.**

KCS Change Propagation:

> **Change(x) -> CandidateReview(y)**

not:

> **Change(x) -> AutomaticRejection(y)**

STRA:

> **Condition Satisfied != Action Authorised**

and:

> **Triggering Review != Authority Over Outcome**

CWA:

> **Overlapping Contexts != Merged Authority**

Context Composition:

> **Material State Change In One Context != Global State Change**

Therefore the missing function is not a new universal transition engine. It is a **context-qualified dependency and review bridge**.

## 3. Core topology

**Material State Change In Source Context A**  
-> **Identify Represented Context Dependencies**  
-> **ESCP Dependency/Context Completeness Challenge Where Proportionate**  
-> **Classify Edge Relevance For Decision Object Q**  
-> **Generate Candidate Review / Trigger For Dependent Context B**  
-> **B's Legitimate State Owner Evaluates Effect**  
-> **No Change / Revalidation / Suspension / Transition / Termination / UNKNOWN**  
-> **If B Materially Changes, Record Through BTA**  
-> **Propagate Further Only From Materially Changed B State**  
-> **Monitor / Review / Correct / Recompose Context Set**

The default is therefore:

> **Source Transition -> Dependent Review**

not:

> **Source Transition -> Destination Transition**

## 4. Context-state dependency edge

A useful representation is:

`CSD = <SourceContext, SourceStateOrDecisionObject, TargetContext, TargetStateOrDecisionObject, RelationType, Direction, Materiality, ActivationCondition, EffectClass, TargetOwner, AuthorityBasisRef, ReviewRoute, AutomaticityState, TerminationCondition, Evidence, Uncertainty, Provenance>`

Not every implementation requires this exact schema.

The important requirement is that a relation be more specific than "these contexts are connected."

> **Context Connection != State Dependency**

## 5. Candidate relation types

### 5.1 PREREQUISITE

A source state is a required condition for a target function/state.

Example: current medical fitness may be a prerequisite for participation in a hazardous activity.

### 5.2 ENABLES

The source state permits the target context to become reachable or operable, without itself granting target authority.

### 5.3 CONSTRAINS

The source state narrows what is legitimately possible in the target context.

### 5.4 SUSPENDS

A legitimately defined source condition can place a target function into a bounded pending/suspended state.

This relation requires an independently legitimate basis; dependency alone does not create suspension authority.

### 5.5 TERMINATES

A source condition satisfies an externally established termination condition for a target state.

### 5.6 REVALIDATES

A source change requires the target state to be re-evaluated before continued reliance.

### 5.7 INFORMS

The source change is materially relevant evidence for the target owner but creates no predetermined target result.

### 5.8 EXTERNALITY

The source change may materially affect another context or party without creating authority over it.

### 5.9 NONE / NON-DEPENDENT

The contexts may coincide or relate socially/physically while the source change has no material target-state implication for the declared decision.

## 6. Dependency is directional

If B depends on A:

`A -> B`

it does not follow that:

`B -> A`

Example:

Medical fitness may be a prerequisite for continuing a boxing bout.

Bout participation is not a prerequisite for the participant to retain ordinary medical standing.

Therefore:

> **Dependency(A,B) != Dependency(B,A)**

and:

> **Propagation Direction Must Be Explicit**

## 7. Dependency is decision-object specific

A source context may affect one target decision while leaving another untouched.

Example:

A clinician identifies acute neurological impairment during a boxing match.

This may materially affect:

- **Q1: continuation of bout** — strong dependency;
- **Q2: immediate medical treatment** — direct medical decision;
- **Q3: contractual payment** — may require later review but no automatic conclusion;
- **Q4: civil standing** — no dependency;
- **Q5: future licensing** — possible later review under separate rules;
- **Q6: ownership of personal property** — no dependency.

Therefore:

> **Context Dependency != Whole-Context Dependency**

A dependency should be scoped to the relevant state or decision object wherever practical.

## 8. Review propagation versus state propagation

This architecture distinguishes at least four effects.

### P0 — No propagation

The source change is not materially relevant to the target decision.

### P1 — Information propagation

The target owner should receive/consider the changed source state.

No review result is implied.

### P2 — Review propagation

The source change creates a legitimate reason or requirement to reconsider the target state.

> **Review Required != Target State Changed**

### P3 — Bounded automatic effect

An already legitimate rule explicitly maps a verified source condition to a bounded target effect.

Examples may include a machine interlock or a pre-authorised safety stop.

Even here:

> **Automatic Effect Requires Prior Legitimate Authority And Declared Scope**

P3 is not the default merely because automation is technically possible.

## 9. Target-state ownership

The propagation mechanism does not own the target state.

For target B:

`TargetEvaluation(B) -> LegitimateOwner(B)`

The source actor, source context, dependency graph, STRA trigger or BTA record does not acquire B's substantive authority merely by identifying a dependency.

> **Dependency Discovery != Target-State Authority**

> **Review Routing != Decision Authority**

> **Source Expertise != Destination Sovereignty**

## 10. STRA as review-trigger interface

STRA supplies the natural trigger layer.

A material source transition may satisfy a condition such as:

`IF MedicalFitnessState becomes MATERIAL_CHANGE THEN ReviewDue(MatchContinuation)`

STRA can represent and route that condition.

It does not decide whether the bout must stop unless a separate legitimate rule has already authorised that exact bounded automation.

Therefore:

**Source Change**  
-> **STRA Condition Evaluation**  
-> **REVIEW-DUE / ACTION-CANDIDATE**  
-> **Legitimate Target Owner**  
-> **Substantive Decision**

This prevents the trigger system from becoming a hidden authority system.

## 11. BTA as transition record/interface

If the target owner determines that B materially changes, BTA can coordinate the resulting transition.

Example:

`MatchParticipation: ACTIVE -> TERMINATED`

BTA may preserve:
- transition basis;
- authority/permission references;
- prior and next state;
- surviving duties;
- non-propagation rules;
- external consequences;
- recovery/reversion where relevant.

BTA does not decide that the medical change logically caused the match transition merely because both states are present.

> **Review Causation != Transition Ownership**

## 12. KCS Change Propagation as generic propagation grammar

KCS Change Propagation already supplies the reusable rule:

> **Change upstream -> identify materially affected dependents -> review selectively -> propagate further only when downstream material state actually changes.**

For contextual state this becomes:

> **Change(ContextState A) -> CandidateReview(ContextState B)**

and, only if B's legitimate owner changes B:

> **MaterialChange(B) -> CandidateReview(C)**

This blocks cascade overreaction.

A chain:

`A -> B -> C -> D`

does not mean a change in A automatically changes B, C and D.

Each edge must be materially and legitimately traversed.

## 13. Propagation stop rule

Propagation should stop along an edge when:
- the relation is immaterial to the declared decision;
- the target state remains valid after review;
- an alternative dependency satisfies the requirement;
- the edge is stale, invalid, superseded or outside scope;
- the source change does not meet the edge's activation condition;
- the target owner determines no material state change;
- further propagation would require authority not established.

> **Connected Downstream != Required Downstream Transition**

## 14. Suspension as a special state

Some dependencies cannot safely wait for a full substantive resolution.

Where an independently legitimate rule establishes a precautionary or protective suspension condition, the target may enter a bounded state such as:

`ACTIVE -> SUSPENDED_PENDING_REVIEW`

This is not equivalent to final termination or guilt/failure.

A suspension record should identify:
- legitimate basis;
- trigger;
- affected function;
- duration/backstop;
- review owner;
- rights/protections retained;
- termination/reversion conditions;
- provenance.

> **Protective Suspension != Final Determination**

> **Suspension Authority != General Authority**

## 15. Automatic propagation is exceptional

Automatic state propagation may be legitimate where all of the following are established:

1. the source state is sufficiently defined and reliably observable;
2. the target effect is explicitly pre-authorised;
3. the dependency and direction are explicit;
4. scope is bounded;
5. material false-positive/false-negative risks are addressed;
6. rights/protected constraints are preserved;
7. the effect is proportionate;
8. termination/reversion is defined;
9. provenance/audit is preserved;
10. consequential uncertainty can trigger review rather than false certainty.

Examples may include:
- physical safety interlocks;
- access credentials expiring when an underlying role legitimately terminates;
- bounded machine shutdown on verified hazard state.

Automaticity does not convert the propagation architecture into the authority source.

## 16. Boxing transfer test

Participant P occupies:

`{sport, match, employment, medical, venue, commercial, civil}`

Event:

`MedicalState: neurologically fit -> acute impairment suspected/established`

Candidate edges:

### Medical -> Match continuation

Relation: PREREQUISITE / CONSTRAINS / possible SUSPENDS or TERMINATES under established rules.

Effect: P2 review or P3 bounded stop where legitimate pre-authorised sporting/medical rules provide it.

### Medical -> Employment

Relation: INFORMS / possible REVALIDATES depending on employment function.

Immediate result:

> **Medical Match Stop != Employment Termination**

The employer may have surviving duties, including care, payment, reporting or rehabilitation.

### Medical -> Commercial/Broadcast

Relation: INFORMS.

The broadcast may be affected operationally, but the medical authority does not become commercial authority.

### Medical -> Civil standing

Relation: NONE for ordinary standing absent a separately established decision-specific basis.

> **Impairment For Bout Continuation != Global Loss Of Civil Authorship**

### Match termination -> Venue

Relation may be INFORMS/ENABLES regarding event operations.

It does not grant the sporting authority general control over the venue.

**Result:** PASS. The architecture prevents state bleed while permitting legitimate safety propagation.

## 17. Hospital transfer test

Participant P is simultaneously:
- patient;
- employee;
- research participant;
- data subject.

A clinical incapacity state may affect immediate treatment authorship.

Candidate effects:
- treatment decision: material;
- research participation: review/suspension may be required;
- employment: perhaps informs/revalidates depending on role;
- data-use permission: no automatic expansion;
- civil standing: no global change.

> **Clinical Incapacity != General Incapacity**

**Result:** PASS.

## 18. Custody transfer test

A detainee develops a medical emergency.

Custody -> medical context may enable physical access/transport.

Medical state may constrain custodial handling.

Neither authority absorbs the other.

A medical change may trigger review of:
- placement;
- restraint;
- transport;
- observation;
- treatment.

It does not automatically change:
- legal guilt;
- sentence;
- property ownership;
- general civil standing.

**Result:** PASS with high rights/completeness burden.

## 19. AI/digital transfer test

An AI service has:
- sandbox permission;
- production permission;
- data-access permission;
- economic interface;
- communications interface;
- experimental status.

A sandbox validation success may trigger production-readiness review.

It must not automatically produce:

`SandboxValidated -> ProductionAuthorised`

Similarly:

`ProductionPermissionTerminated -> WalletOwnershipTerminated`

is invalid unless an independently legitimate dependency establishes it.

**Result:** PASS; particularly strong demonstration of CAP != PERM != AUTH and non-propagation.

## 20. Employment/hazardous-work transfer test

A worker's certification expires.

Certification state may be a prerequisite for a particular hazardous function.

Legitimate effect may be:

`HazardousFunction: ACTIVE -> SUSPENDED_PENDING_REVALIDATION`

It does not automatically imply:

`Employment: TERMINATED`

The worker may remain employed, retrain, perform another role, or restore certification.

> **Loss Of Permission For Function X != Loss Of Participant Role Y**

**Result:** PASS.

## 21. ESCP dependency-completeness problem

Even perfect propagation over represented edges can fail if a material dependency is absent.

Let represented graph be:

`G_A = <V_A, E_A>`

while materially relevant graph is:

`G_R = <V_R, E_R>`

It is possible that:

`E_A subset E_R`

Therefore:

> **Correct Propagation Over Represented Dependencies != Complete Consequence Propagation**

High-consequence transitions should proportionately ask:

> **What materially relevant dependency, affected context, owner, protected boundary or externality would have to be missing for this propagation decision to be wrong or over-scoped?**

This does not require exhaustive graph discovery.

## 22. New-dependency discovery

A transition may reveal a dependency that was not previously known.

Discovery should:
1. preserve the new relation as candidate/uncertain where appropriate;
2. review affected prior conclusions if material;
3. avoid pretending the dependency always was operationally known;
4. trigger bounded retrospective review where consequences justify it;
5. update provenance and future propagation paths.

> **Dependency Discovery At Time T != Dependency Knowledge Before Time T**

## 23. Reversion and dependency release

When the source condition ends, the target does not necessarily revert automatically.

Example:

A medical condition resolves.

This may satisfy a trigger for re-evaluation of match/work eligibility.

It does not itself restore:
- expired licence;
- terminated contract;
- revoked access;
- completed event;
- other independently changed states.

Therefore:

> **Source Recovery != Automatic Destination Restoration**

BTA's rule remains applicable:

> **Rollback != Restoration Unless Prior-State Equivalence Is Actually Re-established**

## 24. Failure modes

### 24.1 State bleed

A source state directly overwrites unrelated target states.

### 24.2 Review-authority collapse

A review trigger is treated as authority to decide the target outcome.

### 24.3 Dependency-authority collapse

The existence of a dependency is treated as authority over the dependent context.

### 24.4 Cascade overreaction

Every downstream node changes because an upstream node changed.

### 24.5 Silent dependency failure

A material prerequisite changes but no dependent review occurs.

### 24.6 Whole-context propagation

A dependency concerning one decision object is treated as dependency of the entire target context.

### 24.7 Reverse inference

A directional dependency is silently treated as bidirectional.

### 24.8 Automatic restoration

Ending the source condition is assumed to restore all target states.

### 24.9 Graph-completeness overclaim

Correct traversal of represented dependencies is treated as proof all material dependencies were represented.

### 24.10 Protective suspension laundering

A temporary protective state is treated as a final substantive determination.

## 25. Candidate invariants

SCTP-01 Source Transition -> Dependent Review, not automatic destination transition.  
SCTP-02 Context Connection != State Dependency.  
SCTP-03 Dependency(A,B) != Dependency(B,A).  
SCTP-04 Propagation Direction Must Be Explicit.  
SCTP-05 Context Dependency != Whole-Context Dependency.  
SCTP-06 Review Required != Target State Changed.  
SCTP-07 Automatic Effect Requires Prior Legitimate Authority And Declared Scope.  
SCTP-08 Dependency Discovery != Target-State Authority.  
SCTP-09 Review Routing != Decision Authority.  
SCTP-10 Source Expertise != Destination Sovereignty.  
SCTP-11 Connected Downstream != Required Downstream Transition.  
SCTP-12 Protective Suspension != Final Determination.  
SCTP-13 Suspension Authority != General Authority.  
SCTP-14 Medical Match Stop != Employment Termination.  
SCTP-15 Impairment For Bout Continuation != Global Loss Of Civil Authorship.  
SCTP-16 Clinical Incapacity != General Incapacity.  
SCTP-17 Loss Of Permission For Function X != Loss Of Participant Role Y.  
SCTP-18 Correct Propagation Over Represented Dependencies != Complete Consequence Propagation.  
SCTP-19 Dependency Discovery At Time T != Dependency Knowledge Before Time T.  
SCTP-20 Source Recovery != Automatic Destination Restoration.

## 26. Architectural allocation

This architecture should not absorb the functions of its components.

- **CWA** owns contextual boundary/composition representation and precedence routing.
- **Context Composition + ESCP** challenges whether relevant contexts are represented.
- **KCS Change Propagation** supplies the generic dependency-review grammar.
- **STRA** supplies state/event-triggered review routing.
- **legitimate domain/context owners** decide substantive target state.
- **BTA** coordinates consequential transitions after those states legitimately change.
- **SMM** may represent context-specific sufficiency/maturity where relevant.
- **ESCP** challenges dependency-space completeness.
- **Cross-Boundary Externality Recognition** handles material effects outside the originating authority/context.

The cross-domain architecture supplies the interface contract among them.

## 27. Resulting topology

The resulting contextual transition topology is:

> **State Change -> Dependency Discovery -> Candidate Review -> Legitimate Target Evaluation -> Selective State Transition -> Further Propagation Only If Material Target State Changes -> Recomposition / Monitoring / Review**

Combined with the previous architecture:

> **Decision/Event -> Context Discovery -> Completeness Challenge -> Decision Decomposition -> Bounded Composition -> Legitimate Action -> State Monitoring -> Selective Transition Propagation -> Recomposition**

This preserves a central Concord rule:

> **A Change May Travel As Information Or Review Obligation Without Traveling As Authority Or State.**
