# Bounded Transition Architecture — Existing Concord Source Resolution 003 — State Machines, Handover and Partial Transition

**Author:** Alexander C. Blainey — Independent Researcher  
**Project:** The Concord Framework  
**Framework Version:** Concord V1.3  
**Status:** ACTIVE DEVELOPMENT / SOURCE-RESOLUTION AUDIT / NON-CANONICAL  
**Date:** September 2026

# 1. Purpose

Source Resolution 002 treated generic intermediate/partial transition state as the strongest remaining BTA-specific function. The user then recalled earlier Concord discussion of state-machine use. This audit checks the existing corpus before BTA 002 is drafted.

Question:

> Did Concord already solve partial/intermediate consequential transition in narrower systems, such that BTA should generalise an existing pattern rather than invent a new one?

**Finding: YES — SUBSTANTIALLY.**

# 2. Civil State Handover Protocol is the strongest precursor

Source:

`03_Cross_Domain_Architecture/Invention_Frontier/Civil State Handover Protocol.md`

CSHP explicitly models migration as a **civil handover transaction** in which responsibility for bounded live civil state changes while identity remains unchanged.

> **Data Copy != Civil Responsibility Transfer.**

It contains:

- **Transition Epoch (TE):** versioned marker identifying which provider/path is responsible for which state at which stage;
- **Pending-State Capsule (PSC):** unresolved live obligations/current status during transfer;
- **Handover Witness (HW):** records initiation, offer, acceptance/rejection, completion/failure/recovery;
- **Recovery Anchor (RA):** last known valid handover state;
- **Transition Hold (TH):** protected uncertainty state while consequential handover remains unresolved.

CSHP explicitly distinguishes whether responsibility remains with A, has moved to B, or is in **protected transition**.

This is already a specialised bounded-transition architecture.

# 3. Existing failure semantics

CSHP already tests:

- source failure mid-transfer;
- destination failure before completion;
- both parties claiming authority;
- neither claiming responsibility;
- events arriving during transition;
- duplicate consequence;
- corrupted transfer;
- long partition;
- obsolete rollback.

Its failure-safe question is:

> **Which transition epoch currently carries responsibility for this live obligation?**

If that cannot be answered confidently, the architecture enters Transition Hold.

Therefore Concord already contains an explicit protected intermediate transition state.

# 4. Historical independently contains partial transition semantics

Historical validation independently uses:

- `PendingInformationStateTransitions`;
- `ReconciliationStatus`;
- `PENDING_REPLICA`;
- `PARTIALLY_EXECUTED`;
- consequential transition history linked from snapshot state.

It also recognises that the same object can legitimately possess multiple simultaneous states depending on jurisdiction, actor, purpose, context and authority source.

This is independent evidence that partial execution is not merely a CSHP-specific concept.

# 5. Infrastructure independently contains multidimensional transition state

Infrastructure already defines a multidimensional lifecycle representation:

`InfrastructureState = <OperationalState, StewardshipState, PhysicalState, LogicalAccessState, TransitionState, HistoricalState>`

Example:

`<RETIRED, ACTIVE, IN_PLACE, REVOKED, COMPLETE, PRESERVED>`

It also contains successor transition, withdrawal pending, decommissioning, degraded transition, irreversibility threshold, physical/logical retirement and residual stewardship.

> **A consequential transition cannot safely be reduced to one scalar lifecycle state.**

# 6. Civilisational topology already reserves transition representation

The canonical Mathematical Civilisational Topology includes:

**L1-03 — Civilisational State and Transition Representation**

and includes temporal/state-transition information in the civil self-model.

The Clock/CRSTL architecture separately represents ordering and relations among transitions, including branching, concurrency, precedence, correction and supersession.

Therefore BTA is not discovering that civilisation needs state-transition representation.

# 7. Distributed state-machine architecture

The V1.3 corpus contains multiple specialised state machines or state-transition grammars:

- CSHP — handover/migration;
- Historical — information-state transition and partial execution;
- Infrastructure — multidimensional lifecycle transition;
- STRA — trigger/review state;
- KCS — dependency/change state;
- Clock/CRSTL — relation/order among civil transitions;
- FPA/BCA — permission/authority activation and termination;
- Continuity — recovery/succession state.

The recurrent pattern is:

> **Represent consequential functions as explicit multidimensional states with bounded transition conditions, provenance, uncertainty and domain-owned authority.**

# 8. Does this eliminate BTA?

No. It changes what BTA is.

The corpus contains multiple **domain-specific state machines**. What remains distributed is a common cross-domain grammar for coordinating one consequential transition across those state machines without replacing them.

Example: enterprise closure may simultaneously produce:

- Commerce lifecycle change;
- BCA authority termination;
- FPA permission change;
- Accountability residual duties;
- Resource Stewardship recovery routing;
- Historical provenance;
- KCS dependency review;
- CBER externality review.

Each system may be locally correct. Something still has to bind these changes into one bounded transition event.

# 9. Revised interpretation of TransitionProgressState

Source Resolution 002 proposed BTA ownership of `TransitionProgressState`. That is now too strong.

CSHP, Historical and Infrastructure already demonstrate legitimate transition-progress vocabularies.

BTA should instead provide a **minimum cross-domain transition-phase grammar** and preserve richer domain states by reference.

Candidate common classes:

- NOT_STARTED;
- ACTIVE/PENDING;
- PARTIAL/INTERMEDIATE;
- COMPLETED;
- FAILED;
- RECOVERY/ROLLBACK_ACTIVE;
- RESIDUAL/UNRESOLVED.

Candidate interface:

`TransitionStateRef = <OwnerSystemRef, DomainTransitionState, CommonTransitionClass, Scope, Provenance, Uncertainty>`

> **Standardise the transition interface; preserve legitimate domain-specific state machines.**

# 10. Transition Epoch as reusable pattern

CSHP's Transition Epoch appears potentially generalisable for consequential multi-stage transitions.

It answers:

> During consequential change, which state/authority/responsibility interpretation is currently operative?

Candidate generalised reference:

`TransitionEpoch = <TransitionID, EpochID, EffectiveStateRefs, ResponsibilityRefs, AuthorityRefs, PendingStateRefs, EntryBasis, ExitCondition, Provenance>`

Not every transition requires explicit epochs; simple atomic transitions should not inherit unnecessary overhead.

# 11. Recovery Anchor as reusable pattern

CSHP's Recovery Anchor also generalises: preserve a reference to the last known valid state from which legitimate recovery can be reasoned.

Candidate BTA interface:

`RecoveryAnchorRef`

BTA would not own recovery. It would preserve the state reference required by the domain recovery mechanism.

# 12. Transition Hold as reusable pattern

CSHP demonstrates that uncertain transition state must not silently manufacture consequence.

General form:

> **Where a consequential transition is materially unresolved, consequences that depend on successful completion should not be inferred solely from attempted or partial crossing.**

This aligns with BTA's existing:

> **Uncertainty Must Not Manufacture Authority.**

A generic BTA transition hold may map to `SAFE_STATE_PENDING_RESOLUTION`, while substantive consequences remain domain-owned.

# 13. State-machine boundary

BTA should **not** become the universal state machine of Concord.

Correct topology:

`Domain State Machines → bounded state/transition references → BTA Transition Integration → relevant external systems`

BTA standardises the transition interface while preserving legitimate domain-specific semantics.

# 14. Revised BTA residual

The remaining BTA-specific problem is now narrower again.

It is not:

- discovering state machines;
- inventing partial states;
- defining every domain transition state;
- owning rollback;
- owning authority;
- owning dependency propagation;
- owning externalities.

It is:

> **Providing a common integration contract through which independently owned domain state machines can participate in one consequential bounded transition without losing state, authority boundaries, pending obligations, non-propagation rules, provenance or recovery position.**

# 15. Concrete manifestation

Suppose a critical infrastructure service transfers from Asset A to Asset B.

Infrastructure may report:

`A = WITHDRAWAL_PENDING`  
`B = COMMISSIONING`  
`ServiceTransition = SUCCESSOR_TRANSITION`

BCA may report:

`A operational authority = SUNSETTING`  
`B operational authority = NOT_YET_ACTIVE`

STRA may report:

`B validation = CONDITION_PARTIAL`

KCS may report:

`dependent services = REVIEW_REQUIRED`

Historical may report:

`transition event = ACTIVE / provenance preserved`

Continuity may retain A as recovery fallback.

CBER may have external participant effects under review.

No individual system is wrong.

The unresolved integration question is:

> **What single bounded transition event ties those independently valid states together and prevents one system from treating the transition as complete while another still legitimately represents it as partial?**

That is the surviving BTA function.

# 16. Candidate cross-domain contract

`BoundedTransitionContract = <TransitionID, ObjectOrFunctionRefs, Scope, ParticipatingStateSystemRefs, PriorStateRefs, TransitionBasisRefs, TransitionEpochOrPhaseRef, PendingStateRefs, ScopedValidationRefs, RelationalEffectRefs, ExternalityReviewRefs, NonPropagationRules, SurvivingDutyRefs, TerminatedAuthorityRefs, DependencyRefs, RecoveryAnchorRef, RollbackOrRecoveryRefs, NextStateRefs, Provenance, UncertaintyOrDisputeState>`

This is an **integration contract**, not a universal ontology.

# 17. Source-resolution decision

**The partial/intermediate-state problem is not a genuinely new Concord invention.**

It already exists in specialised form in CSHP, Historical, Infrastructure and the broader state/transition topology.

What remains missing is the **cross-domain generalisation and interface contract**.

> **BTA should be developed as a generalised bounded-transition interoperability layer derived partly from existing Concord state-machine/state-transition architecture, not as an independent replacement for those architectures.**

# 18. Next step

Before drafting BTA 002:

1. treat CSHP as a major precursor/source;
2. preserve its useful patterns: Transition Epoch, Pending State, Handover Witness, Recovery Anchor and Transition Hold;
3. test which patterns survive outside civil handover;
4. avoid forcing domain-specific state vocabularies into one universal machine;
5. formulate BTA 002 as the common contract among state machines.

A focused cross-domain generalisation test should apply the CSHP-derived transition patterns to infrastructure transition, enterprise wind-down and genomic/data-purpose transition, then identify the smallest common kernel that survives all three.