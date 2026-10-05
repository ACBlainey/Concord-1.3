# Contextual Dependency Legitimacy and Activation — Cross-Domain Architecture 001

**Project:** The Concord Framework  
**Date:** 5 October 2026  
**Status:** CROSS-DOMAIN ARCHITECTURE / PROVISIONAL / NON-CANONICAL  
**Primary interfaces:** Selective Context-State Transition Propagation; KCS Change Propagation; Contextual Wrapper Architecture (CWA); Decision Authorship and Contextual Participation; Bounded Transition Architecture (BTA); State Triggered Review Architecture (STRA); Evaluation-Space Completeness Problem (ESCP); Context Composition and Evaluation-Space Completeness; Minimum Necessary Capability / bounded-authority architecture

## 1. Purpose

KCS Change Propagation already supplies a general lifecycle for dependency records: discovery, evidence, state, freshness, change, correction, supersession, removal, alternatives and history.

Selective Context-State Transition Propagation applies that grammar to changes crossing contextual boundaries.

A further distinction is required:

> **A Dependency Can Be Real Without Being Currently Legitimate To Operationalise.**

A relation may exist factually while:
- its activation condition is false;
- the target decision object is outside scope;
- the information needed to traverse it is protected;
- the relevant authority has expired;
- consent does not cover the proposed use;
- the relation is historical rather than current;
- a less intrusive interface satisfies the dependency;
- the dependency is disputed or uncertain;
- the dependency supports review but not automatic action.

This architecture therefore separates **dependency existence/state** from **dependency operational legitimacy and activation**.

## 2. Core distinction

For a contextual dependency edge E:

`Existence(E) != OperationalLegitimacy(E,Q,t)`

and:

`OperationalLegitimacy(E,Q,t) != Activation(E,Q,t)`

and:

`Activation(E,Q,t) != AuthorityOverTarget(E)`

A useful three-stage representation is:

1. **Does the dependency exist?**
2. **Is it legitimate to use this dependency for this decision, purpose and context?**
3. **Are its declared activation conditions currently satisfied?**

Only then should propagation proceed.

## 3. Source-resolved allocation

KCS Change Propagation owns generic dependency lifecycle and review propagation.

This architecture does not duplicate that function.

It adds a contextual legitimacy gate before a dependency is operationally traversed.

Therefore:

**KCS Dependency Record**  
-> **Contextual Legitimacy Gate**  
-> **Activation Evaluation**  
-> **Information / Review / Bounded Effect**  
-> **Legitimate Target Owner**  
-> **BTA Transition If Target State Changes**

## 4. Dependency truth is not access authority

Example:

A worker's medical fitness is genuinely relevant to safe performance of hazardous role X.

That establishes a functional dependency:

`FitnessForX -> EligibilityForX`

It does not establish:

`Employer -> unrestricted medical record access`

The legitimate interface may instead expose only:

- FIT_FOR_X;
- FIT_WITH_RESTRICTIONS_FOR_X;
- TEMPORARILY_UNFIT_FOR_X;
- REVIEW_REQUIRED;
- UNKNOWN/DISPUTED.

Therefore:

> **Need To Know Whether A Dependency Is Satisfied != Need To Access The Source's Full Internal State**

and:

> **Dependency Relevance != General Information Entitlement**

This is a direct application of contextual wrappers and minimum-necessary capability.

## 5. Dependency edge record extension

Where contextual legitimacy is material, an edge may reference:

`CDL = <DependencyRef, DecisionObject, Purpose, SourceContext, TargetContext, LegitimateUseBasis, PermittedProjection, ActivationPredicate, EffectClass, TargetOwner, EffectiveFrom, EffectiveUntilOrTermination, ReviewCondition, ReversionOrExpiryRule, Uncertainty, Provenance>`

This extends rather than replaces the generic KCS dependency record.

## 6. Candidate legitimacy states

A contextual dependency-use state may include:

- **LEGITIMATE_ACTIVE** — use is legitimate and activation predicate is satisfied;
- **LEGITIMATE_DORMANT** — relation is legitimate but current activation condition is false;
- **LEGITIMATE_REVIEW_REQUIRED** — use basis remains plausible but must be revalidated before consequential reliance;
- **LEGITIMATE_BOUNDED_PROJECTION_ONLY** — dependency may be evaluated only through a restricted interface/projection;
- **EXPIRED** — prior legitimate use basis ended;
- **SUPERSEDED** — a newer legitimate relation/use rule replaces it;
- **NOT_AUTHORISED_FOR_PURPOSE** — dependency may exist but proposed use is outside legitimate scope;
- **UNKNOWN** — legitimacy cannot presently be established;
- **DISPUTED** — materially conflicting legitimacy claims remain.

These are not substitutes for the underlying dependency's factual state.

## 7. Two-dimensional edge state

A dependency should be able to hold separate dimensions.

Example:

`DependencyState = ACTIVE`

`LegitimateUseState = LEGITIMATE_DORMANT`

or:

`DependencyState = ACTIVE`

`LegitimateUseState = NOT_AUTHORISED_FOR_PURPOSE`

or:

`DependencyState = DISPUTED`

`LegitimateUseState = LEGITIMATE_REVIEW_REQUIRED`

Therefore:

> **Dependency State != Dependency-Use Legitimacy State**

Collapsing them would create either hidden overreach or false claims that a real dependency does not exist.

## 8. Activation predicates

A legitimate edge may remain dormant until a bounded condition becomes true.

Candidate predicates include:
- entry into a particular wrapper;
- assumption of a defined role;
- initiation of a particular function;
- presence of a defined risk state;
- consent for a declared purpose;
- contractual activation;
- emergency threshold;
- licence/certification state;
- specific externality;
- time or event condition;
- capability state;
- explicit review trigger.

Example:

`IF Participant performs hazardous function X THEN FitnessForX dependency ACTIVE`

not:

`IF Participant is employed THEN all medical dependencies ACTIVE`

> **Role Membership != Activation Of Every Role-Related Dependency**

## 9. Purpose limitation

The same source state may legitimately support one purpose and not another.

Example:

A medical fitness projection may legitimately determine eligibility for hazardous work.

The same information may not legitimately be used to:
- infer unrelated health conditions;
- alter unrelated remuneration;
- profile future insurance risk;
- determine political/civil standing;
- make unrelated research use.

Therefore:

> **Legitimate Use For Purpose A != Legitimate Use For Purpose B**

and:

> **Dependency Traversal Must Preserve Purpose**

## 10. Projection rather than source disclosure

Where a target needs only the result of a dependency test, the source wrapper should expose the minimum sufficient projection rather than its full internal state.

Topology:

**Protected Source State**  
-> **Legitimate Source Owner / Evaluator**  
-> **Bounded Dependency Projection**  
-> **Target Context**

Example:

`MedicalRecord -> OccupationalHealthEvaluator -> FIT_FOR_ROLE_X -> Employer`

The employer can legitimately act on the bounded projection without receiving the underlying diagnosis/history unless a separate legitimate basis exists.

> **Dependency Satisfaction Can Be Exposed Without Exposing Dependency Internals**

This directly interfaces with the Contextual Wrapper Black Box architecture.

## 11. Activation does not create authority

Even when an edge is legitimate and active:

> **Active Dependency != Authority Over Source**

> **Active Dependency != Authority Over Target**

> **Active Dependency != Authority To Expand Purpose**

The edge establishes a relevant relation and propagation route.

Substantive authority remains externally bounded.

## 12. Temporal legitimacy

A dependency-use relation may have:
- start condition;
- active period;
- expiry;
- renewal/revalidation;
- suspension;
- termination;
- historical retention.

A relation that was legitimate yesterday may be illegitimate today even if the factual dependency still exists.

Example:

A temporary research study may legitimately depend on a participant's consent state.

After withdrawal, the historical dependency remains part of provenance, but the operational use basis may terminate.

> **Historical Dependency != Current Operational Permission**

## 13. Withdrawal and termination

Where legitimacy depends on revocable authorship/consent, withdrawal may terminate future use without erasing prior legitimate history.

`LEGITIMATE_ACTIVE -> EXPIRED/TERMINATED_FOR_FUTURE_USE`

This does not necessarily require deletion of all historical records where separate legitimate retention duties exist.

Therefore:

> **End Of Operational Use != Erasure Of Historical Dependency**

and:

> **Historical Retention != Continued Operational Authority**

## 14. Emergency activation

An emergency may activate dependencies that are normally dormant.

Example:

An unconscious patient's emergency medical state may activate a bounded emergency treatment dependency.

It does not activate every possible medical, research, employment or administrative use.

> **Emergency Activation != Universal Dependency Activation**

Emergency use should preserve:
- trigger;
- scope;
- legitimate basis;
- minimum necessary information;
- temporary authority;
- termination condition;
- later review/provenance.

## 15. Dependency substitution

A target may need capability C without requiring a particular source S.

If an alternative legitimate supplier satisfies C:

`S1 -> C`

may become dormant/non-blocking while:

`S2 -> C`

is active.

Therefore:

> **Required Capability != Permanent Required Supplier**

This matters for anti-capture, resilience and participant autonomy.

A dependency graph should not turn historical suppliers into permanent gatekeepers.

## 16. Dependency retirement

An edge may retire because:
- the target no longer requires the capability;
- architecture changed;
- a safer/less intrusive route replaces it;
- role/function ended;
- the source/target ceased;
- legal/ethical basis ended;
- the relation was erroneous;
- a dependency was absorbed into a new bounded interface.

Retirement should preserve history where legitimate.

> **Retired Dependency != Dependency Never Existed**

## 17. Boxing transfer test

A boxer enters a sanctioned bout.

Potential dependency:

`MedicalFitnessForBout -> Authorship/EligibilityForBoutContinuation`

The dependency may become LEGITIMATE_ACTIVE because:
- the participant entered the bounded sporting context;
- medical monitoring is part of the known safety architecture;
- the purpose is bout safety;
- the projection is limited to fitness/stop-relevant state.

The medical evaluator does not thereby acquire authority over:
- employment generally;
- payment;
- unrelated medical decisions;
- civil standing;
- property;
- unrelated future activities.

After the bout:

`MedicalFitnessForCurrentBout dependency-use -> EXPIRED`

even though the medical record and historical dependency remain.

**Result:** PASS.

## 18. Employment transfer test

Worker W is employed by E in roles X and Y.

X is hazardous; Y is ordinary administrative work.

Dependency:

`FitnessForX -> PermissionToPerformX`

No equivalent dependency need exist for Y.

If W becomes unfit for X:

`PermissionToPerformX -> review/suspension`

not:

`Employment -> terminated`

and not:

`PermissionToPerformY -> automatically terminated`

The employer may receive a bounded fitness projection without full clinical data.

**Result:** PASS.

## 19. Hospital/research transfer test

Patient P is also enrolled in research R.

Clinical information may be relevant to:
- treatment;
- study eligibility;
- adverse-event safety.

But the research dependency requires its own legitimate purpose/use basis.

Clinical care does not silently activate unrestricted research access.

Withdrawal from R can terminate future research-use legitimacy while clinical treatment dependencies remain active.

> **Shared Medical Source != Shared Purpose Authority**

**Result:** PASS.

## 20. Custody transfer test

A detainee's medical state may legitimately constrain restraint, transport or placement.

Custodial staff may need a bounded operational projection such as:
- mobility restriction;
- urgent treatment required;
- observation level;
- contraindicated restraint condition.

They do not automatically require full diagnostic history.

> **Operational Safety Need != General Medical Access**

**Result:** PASS with high rights/privacy burden.

## 21. AI/digital transfer test

An AI system may depend on:
- credential state;
- sandbox state;
- service contract;
- resource allocation;
- validation status.

A production service may legitimately need to know:

`ModelVersion -> VALIDATED_FOR_PRODUCTION_CONTEXT_X`

It need not receive unrestricted access to all research provenance, private evaluation data or unrelated internal state.

A validation relation may expire when:
- model version changes;
- environment changes materially;
- validation period ends;
- relevant dependency changes.

> **Validated Once != Validated For Every Context Or Time**

**Result:** PASS.

## 22. ESCP legitimacy-space challenge

A represented dependency graph can be correct while the legitimacy model is incomplete.

Possible omissions include:
- a protected information boundary;
- purpose restriction;
- consent condition;
- temporal expiry;
- alternative supplier;
- affected third party;
- withdrawal right;
- domain-specific authority owner;
- less intrusive projection route.

Therefore:

> **Complete Dependency Discovery != Complete Dependency-Use Legitimacy Evaluation**

For consequential use ask:

> **What materially relevant right, boundary, purpose, authority condition, temporal condition, alternative route or affected party would have to be missing for operationalising this dependency to be illegitimate or over-scoped?**

## 23. Anti-paralysis

Not every dependency requires a formal legitimacy dossier.

Review depth should scale with:
- consequence;
- privacy/sensitivity;
- rights impact;
- irreversibility;
- asymmetry;
- scope;
- duration;
- automation;
- uncertainty.

Routine public technical dependencies may require little additional legitimacy analysis.

Dependencies involving medical, legal, financial, custodial, identity, intimate, security or similarly protected state require stronger separation.

## 24. Failure modes

### 24.1 Dependency truth laundering

A real dependency is treated as sufficient justification for any use of source information.

### 24.2 Access inflation

Need for a bounded dependency result becomes access to full source state.

### 24.3 Purpose drift

Information obtained for dependency purpose A is reused for purpose B without legitimate basis.

### 24.4 Dormancy failure

A conditional dependency is treated as permanently active.

### 24.5 Historical-authority persistence

A once-legitimate edge remains operational after its authority/consent/role ended.

### 24.6 Supplier capture

One historical supplier becomes a permanent gatekeeper even though equivalent alternatives exist.

### 24.7 Emergency expansion

Emergency activation silently enables unrelated dependency uses.

### 24.8 Edge-state collapse

Factual dependency state and legitimate-use state are compressed into one status.

### 24.9 Projection failure

A target receives protected source internals when a bounded projection would satisfy the legitimate need.

### 24.10 False deletion

Termination of operational legitimacy is represented as though the historical dependency never existed.

## 25. Candidate invariants

CDLA-01 A Dependency Can Be Real Without Being Currently Legitimate To Operationalise.  
CDLA-02 Existence(E) != OperationalLegitimacy(E,Q,t).  
CDLA-03 OperationalLegitimacy(E,Q,t) != Activation(E,Q,t).  
CDLA-04 Activation(E,Q,t) != AuthorityOverTarget(E).  
CDLA-05 Dependency Relevance != General Information Entitlement.  
CDLA-06 Need To Know Whether A Dependency Is Satisfied != Need To Access The Source's Full Internal State.  
CDLA-07 Dependency State != Dependency-Use Legitimacy State.  
CDLA-08 Role Membership != Activation Of Every Role-Related Dependency.  
CDLA-09 Legitimate Use For Purpose A != Legitimate Use For Purpose B.  
CDLA-10 Dependency Traversal Must Preserve Purpose.  
CDLA-11 Dependency Satisfaction Can Be Exposed Without Exposing Dependency Internals.  
CDLA-12 Active Dependency != Authority Over Source.  
CDLA-13 Active Dependency != Authority Over Target.  
CDLA-14 Historical Dependency != Current Operational Permission.  
CDLA-15 End Of Operational Use != Erasure Of Historical Dependency.  
CDLA-16 Historical Retention != Continued Operational Authority.  
CDLA-17 Emergency Activation != Universal Dependency Activation.  
CDLA-18 Required Capability != Permanent Required Supplier.  
CDLA-19 Retired Dependency != Dependency Never Existed.  
CDLA-20 Shared Medical Source != Shared Purpose Authority.  
CDLA-21 Operational Safety Need != General Medical Access.  
CDLA-22 Validated Once != Validated For Every Context Or Time.  
CDLA-23 Complete Dependency Discovery != Complete Dependency-Use Legitimacy Evaluation.

## 26. Resulting topology

The refined cross-context propagation chain is:

> **Dependency Discovery -> Dependency State -> Contextual Legitimacy -> Activation Predicate -> Minimum Necessary Projection -> Information/Review Signal -> Legitimate Target Evaluation -> Bounded Transition If Required -> Further Propagation Only On Material Change -> Expiry/Revalidation/Retirement**

This adds an important protection to the previous architecture:

> **The Existence Of A Causal Or Functional Relationship Does Not, By Itself, Authorise Anyone To Traverse It.**
