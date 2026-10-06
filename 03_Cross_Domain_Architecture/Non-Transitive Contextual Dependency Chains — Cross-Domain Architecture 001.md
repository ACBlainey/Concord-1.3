# Non-Transitive Contextual Dependency Chains — Cross-Domain Architecture 001

**Project:** The Concord Framework  
**Date:** 6 October 2026  
**Status:** CROSS-DOMAIN ARCHITECTURE / PROVISIONAL / NON-CANONICAL  
**Primary interfaces:** Contextual Dependency Legitimacy and Activation; Selective Context-State Transition Propagation; Contextual Wrapper Architecture (CWA); KCS Change Propagation; Bounded Transition Architecture (BTA); State Triggered Review Architecture (STRA); Decision Authorship and Contextual Participation; Cross-Boundary Externality Recognition; Evaluation-Space Completeness Problem (ESCP)

## 1. Purpose

A contextual dependency may legitimately connect A to B, while another dependency legitimately connects B to C.

A dangerous inference is:

`Legitimate(A -> B) AND Legitimate(B -> C) => Legitimate(A -> C)`

This does not generally follow.

The information, permission, consent, authority, purpose, projection or state that makes one edge legitimate may terminate at its destination.

This architecture therefore establishes a default rule:

> **Contextual Dependency Legitimacy Is Non-Transitive Unless Onward Traversal Is Independently Established.**

## 2. Core distinction

For contexts A, B and C:

`L(A,B,Q1,P1,t) = true`

and:

`L(B,C,Q2,P2,t) = true`

does not imply:

`L(A,C,Q3,P3,t) = true`

where:
- L = legitimate dependency use;
- Q = decision object;
- P = purpose;
- t = relevant time/state.

The two legitimate edges may concern different:
- decision objects;
- purposes;
- information projections;
- authority sources;
- participants;
- time windows;
- activation predicates;
- protected boundaries.

Therefore:

> **Legitimate Hop + Legitimate Hop != Legitimate Chain**

## 3. Dependency traversal versus payload traversal

Two different things may travel through a dependency graph:

1. **a review/dependency signal**;
2. **the underlying information/state/payload**.

These must not be collapsed.

A may legitimately tell B:

`FIT_FOR_ROLE_X = NO`

B may legitimately tell C:

`WorkerUnavailableForFunctionX = YES`

It does not follow that C may receive:
- A's medical record;
- the diagnosis;
- B's full employment record;
- the reason beyond what C legitimately requires.

> **Dependency Traversal != Payload Traversal**

and:

> **Review Signal Propagation != Source-State Disclosure**

## 4. Projection transformation

A chain may legitimately operate through successive bounded projections.

Example:

**Medical Context A**  
-> `UNFIT_FOR_HAZARDOUS_ROLE_X`  
-> **Employer Context B**  
-> `STAFFING_CAPACITY_X_REDUCED`  
-> **Operations Context C**

C may need to know that capacity changed.

C need not know which employee is affected or why.

This produces:

> **A Projection May Be Further Reduced Without Preserving The Identity Or Detail Of Its Source.**

The chain can therefore preserve function while reducing unnecessary disclosure.

## 5. Projection does not automatically inherit onward-disclosure permission

If A legitimately exposes projection p to B:

`A --p--> B`

B's possession of p does not imply:

`B --p--> C`

is legitimate.

Onward disclosure requires its own legitimate basis.

> **Permission To Receive != Permission To Redisclose**

> **Permission To Use != Permission To Transfer**

> **Possession Of Information != Authority To Extend Its Audience**

## 6. Derived information

B may derive new information d from projection p.

`d = f(p, B_state)`

The derivative may have different sensitivity, purpose and externality characteristics.

Therefore:

> **Derived Information != Unrestricted New Information**

A derivative does not automatically escape the constraints of its source merely because it is transformed.

Conversely, a sufficiently abstracted derivative may legitimately cross a boundary that the source data cannot.

The relevant question is not whether transformation occurred, but whether the output still carries materially protected information or consequences.

## 7. Purpose continuity

A chain may preserve, narrow or change purpose.

### Purpose-preserving

A -> B -> C all serve the same bounded legitimate purpose.

This may support traversal if every edge is independently legitimate.

### Purpose-narrowing

A's projection is used downstream for a narrower compatible purpose.

This may be legitimate and often preferable.

### Purpose-changing

B attempts to use or forward A-derived state for a materially different purpose.

This requires a new legitimate basis.

> **Purpose Continuity Must Be Demonstrated, Not Assumed From Connectivity**

## 8. Authority non-transitivity

Authority is especially non-transitive.

If A authorises B to perform function X, and B has authority over C for function Y, it does not follow that A's authority extends to C or that B may delegate X to C.

> **Authority(A,B,X) + Authority(B,C,Y) != Authority(A,C,X or Y)**

Delegation requires a legitimate delegation basis, scope and termination condition.

> **Authority To Act != Authority To Delegate**

and:

> **Delegated Authority != Delegation Power Unless Explicitly Supplied**

## 9. Consent non-transitivity

Consent given to A for purpose P does not automatically become consent to:
- B;
- C;
- a changed purpose;
- an expanded audience;
- indefinite future use.

Where an authorised processor/intermediary is part of the original consented function, its role should be explicit or legitimately encompassed by the bounded process.

> **Consent To Function != Consent To Unlimited Participant Chain**

> **Consent To A != Consent To Everyone Reachable From A**

## 10. Access non-transitivity

CWA already separates reachability, access entitlement and local operation.

Applied to chains:

> **A Can Access B And B Can Access C != A Can Access C**

Likewise:

> **B Can Receive From A And Send To C != B Can Forward A's Content To C**

Network or organisational topology does not determine contextual access legitimacy.

## 11. Chain-hop contract

Where consequential onward traversal is intended, each hop should preserve enough information to establish:

`Hop = <Source, Destination, DecisionObject, Purpose, Projection, LegitimateBasis, ActivationPredicate, PermittedUse, OnwardDisclosureState, AuthorityRef, Expiry, Provenance>`

Candidate `OnwardDisclosureState` values:
- PROHIBITED;
- BOUNDED_TO_NAMED_DESTINATION;
- BOUNDED_TO_FUNCTION;
- BOUNDED_TO_EQUIVALENT_PROJECTION;
- REAUTHORISATION_REQUIRED;
- PERMITTED_WITH_CONDITIONS;
- UNKNOWN;
- DISPUTED.

The exact schema is optional; explicit semantics are not.

## 12. Chain validity

A chain:

`A -> B -> C -> D`

is legitimate only to the extent that each material hop is legitimate for the actual traversal.

A useful rule is:

`ChainLegitimate(A...D) = HopLegitimate(A,B) AND HopLegitimate(B,C) AND HopLegitimate(C,D) AND ChainConstraintsSatisfied`

This is necessary but not always sufficient, because composition may create a new consequence not present at any individual edge.

Therefore a chain-level externality/completeness check may still be required.

> **Individually Legitimate Edges != Necessarily Legitimate Composite Effect**

## 13. Composition externality

Several harmless projections can combine into sensitive information.

Example:
- C receives work absence status;
- C separately receives location;
- C separately receives specialist staffing data.

The combination may allow inference of a participant's medical condition.

Therefore:

> **Low-Sensitivity Inputs Can Compose Into High-Sensitivity Output**

and:

> **Projection Safety Must Consider Material Recombination Where Foreseeable**

This is a direct interface to ESCP and Cross-Boundary Externality Recognition.

## 14. Identity minimisation

A downstream function may require a state without requiring participant identity.

Prefer where sufficient:

`PERSON_P_UNFIT_FOR_X`

-> `ROLE_X_CAPACITY_MINUS_ONE`

-> `REPLACEMENT_REQUIRED`

The later contexts can operate without receiving unnecessary identity.

> **Functional Dependency != Identity Dependency**

## 15. Medical-employment-operations stress test

A clinician A assesses worker P.

A legitimately sends occupational health B:

`FIT_FOR_X = NO`

B legitimately sends employer C:

`P MAY NOT PERFORM X UNTIL REVIEW`

C legitimately sends scheduling system D:

`X-SHIFT REQUIRES REPLACEMENT`

D does not need:
- diagnosis;
- clinician notes;
- medical history;
- perhaps even the reason for unavailability.

The legitimate chain progressively reduces information.

If D can query B's medical projection merely because C can, the architecture fails.

**Result:** PASS.

## 16. Custody-medical-transport stress test

Medical service A supplies custody authority B:

`TRANSPORT_REQUIRES_MEDICAL_CONSTRAINTS M`

B supplies transport contractor C only the operational constraints necessary to transport safely.

C does not acquire:
- full medical access;
- custodial decision authority;
- permission to reuse health information commercially;
- authority to disclose the information to unrelated subcontractors.

If a subcontractor D is genuinely necessary, C->D requires an independently legitimate bounded hop.

**Result:** PASS.

## 17. AI service chain stress test

AI model A operates through orchestration service B, external tool C and storage service D.

Permission for B to invoke C does not imply C may:
- access all of A's context;
- persist prompts in D;
- reuse data for unrelated training;
- invoke further tools.

Each boundary requires its own purpose, projection and permission.

A useful digital invariant is:

> **Tool Reachability != Context Delegation**

and:

> **Service Chaining != Permission Chaining**

**Result:** PASS.

## 18. Infrastructure chain stress test

Power system A supplies facility B, which supplies laboratory C.

A's operational dependency on aggregate demand may justify receiving load state.

It does not justify receiving C's experimental data.

C's dependence on B's power does not give C authority over A's generation operations.

The dependency chain may carry:
- capacity requirement;
- outage state;
- restoration estimate;
- safety isolation signal.

It need not carry unrelated internal state.

**Result:** PASS.

## 19. Delegation versus dependency

A dependency chain and a delegation chain are not the same.

Dependency:

`B requires capability from A`

Delegation:

`A authorises B to perform bounded function F`

One does not imply the other.

> **Dependency != Delegation**

> **Delegation != Dependency Ownership**

A delegated function may itself depend on other systems, but delegation scope must be checked independently at each onward assignment.

## 20. Reauthorisation boundary

Some chains should deliberately terminate at a boundary and require new authorship/authority.

Example:

A participant consents to medical assessment for sporting eligibility.

The result reaches the sporting body.

Use of that information for an unrelated employment or insurance decision should encounter:

`REAUTHORISATION_REQUIRED`

rather than silently traversing the existing chain.

> **Boundary Reauthorisation Is A Feature, Not A Failure Of Interoperability**

It prevents interoperability from becoming permission laundering.

## 21. Revocation and chain invalidation

If the legitimate basis for A->B terminates, downstream consequences must be evaluated selectively.

Revocation does not necessarily erase information already legitimately transformed or actions already completed.

But it may terminate:
- future retrieval;
- future forwarding;
- continued processing;
- renewal;
- derivative generation;
- downstream triggers relying on current authority.

Therefore:

> **Upstream Revocation != Automatic Historical Erasure**

and:

> **Upstream Revocation May Terminate Future Chain Traversal Without Reversing Completed Legitimate Effects**

BTA should coordinate material resulting transitions.

## 22. Chain provenance

Consequential chains should preserve enough provenance to reconstruct:
- what crossed each boundary;
- under what purpose;
- through which projection;
- under what legitimate basis;
- whether onward disclosure was permitted;
- what transformations occurred;
- when authority/consent expired;
- what downstream effects resulted.

This does not require every downstream participant to see the entire provenance chain.

> **Auditability != Universal Visibility**

## 23. ESCP chain-completeness problem

Even if every represented hop is legitimate, the chain evaluation may omit:
- an intermediary;
- a derivative use;
- a recombination risk;
- an onward processor;
- an externality;
- an expiry condition;
- an identity leak;
- a hidden authority assumption.

Therefore:

> **Correct Hop Validation != Complete Chain Evaluation**

A proportionate challenge is:

> **What materially relevant intermediary, transformation, recombination, onward use, authority boundary, affected party or externality would have to be missing for this chain to become illegitimate or over-scoped?**

## 24. Anti-paralysis

Non-transitivity does not mean every routine chain needs manual consent at every hop.

A legitimate bounded architecture may pre-authorise a class of hops where:
- purpose is stable;
- destinations/functions are bounded;
- projections are minimum necessary;
- onward rules are explicit;
- authority is legitimate;
- termination/revocation works;
- provenance is preserved;
- material composition risks are addressed.

The rule is not "never traverse."

It is:

> **Do Not Infer Traversal Rights Merely From Adjacency.**

## 25. Failure modes

### 25.1 Permission laundering
A legitimate first hop is used to justify unrelated downstream access.

### 25.2 Consent laundering
Consent to one participant/function is treated as consent to the entire chain.

### 25.3 Authority laundering
Delegated or contextual authority silently expands through intermediaries.

### 25.4 Payload bleed
A review signal carries unnecessary source-state detail.

### 25.5 Purpose drift
A chain changes purpose without reauthorisation.

### 25.6 Identity bleed
Downstream systems receive identity where aggregate/function state would suffice.

### 25.7 Derivative escape
Transformed information is treated as free of source constraints merely because it is derived.

### 25.8 Composition inference
Several bounded projections recombine into a protected inference.

### 25.9 Revocation failure
Future traversal continues after the legitimate upstream basis terminates.

### 25.10 Topology-as-authority
Technical connectivity is mistaken for permission.

## 26. Candidate invariants

NTCDC-01 Contextual Dependency Legitimacy Is Non-Transitive Unless Onward Traversal Is Independently Established.  
NTCDC-02 Legitimate Hop + Legitimate Hop != Legitimate Chain.  
NTCDC-03 Dependency Traversal != Payload Traversal.  
NTCDC-04 Review Signal Propagation != Source-State Disclosure.  
NTCDC-05 Permission To Receive != Permission To Redisclose.  
NTCDC-06 Permission To Use != Permission To Transfer.  
NTCDC-07 Possession Of Information != Authority To Extend Its Audience.  
NTCDC-08 Derived Information != Unrestricted New Information.  
NTCDC-09 Purpose Continuity Must Be Demonstrated, Not Assumed From Connectivity.  
NTCDC-10 Authority To Act != Authority To Delegate.  
NTCDC-11 Delegated Authority != Delegation Power Unless Explicitly Supplied.  
NTCDC-12 Consent To Function != Consent To Unlimited Participant Chain.  
NTCDC-13 Consent To A != Consent To Everyone Reachable From A.  
NTCDC-14 A Can Access B And B Can Access C != A Can Access C.  
NTCDC-15 Individually Legitimate Edges != Necessarily Legitimate Composite Effect.  
NTCDC-16 Low-Sensitivity Inputs Can Compose Into High-Sensitivity Output.  
NTCDC-17 Functional Dependency != Identity Dependency.  
NTCDC-18 Tool Reachability != Context Delegation.  
NTCDC-19 Service Chaining != Permission Chaining.  
NTCDC-20 Dependency != Delegation.  
NTCDC-21 Boundary Reauthorisation Is A Feature, Not A Failure Of Interoperability.  
NTCDC-22 Upstream Revocation != Automatic Historical Erasure.  
NTCDC-23 Auditability != Universal Visibility.  
NTCDC-24 Correct Hop Validation != Complete Chain Evaluation.  
NTCDC-25 Do Not Infer Traversal Rights Merely From Adjacency.

## 27. Resulting topology

The cross-wrapper chain becomes:

> **Source State -> Minimum Necessary Projection -> Legitimate Hop -> Purpose-Preserving/Narrowing Transformation -> Independent Next-Hop Legitimacy Check -> Further Projection -> Target Review/Action -> Provenance**

At any boundary:

`No legitimate next-hop basis -> STOP / REAUTHORISE / ROUTE FOR REVIEW`

The broader architecture now distinguishes:
- context existence;
- dependency existence;
- dependency-use legitimacy;
- activation;
- projection;
- onward-disclosure legitimacy;
- target authority;
- transition;
- further propagation.

The central rule is:

> **Connectivity Creates A Possible Path. It Does Not Create Permission To Travel It.**
