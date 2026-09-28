# Bounded Transition Architecture 002 — Consequential Transition Coherence and Interoperability Grammar

**Author:** Alexander C. Blainey — Independent Researcher
**Project:** The Concord Framework
**Framework Version:** Concord V1.3
**Status:** ACTIVE DEVELOPMENT / PROVISIONAL INTEGRATION ARCHITECTURE / NON-CANONICAL
**Date:** September 2026
**Supersedes for active development:** Bounded Transition Architecture 001
**BTA 001 retention:** RETAINED AS DEVELOPMENTAL PROVENANCE

---

# 1. Purpose

Bounded Transition Architecture (BTA) provides a common integration grammar for **consequential transitions across independently owned state systems**.

Its purpose is not to define the substantive state of every Concord domain. Its purpose is to preserve coherence while several legitimate systems represent different dimensions of the same consequential change.

> **A consequential transition may be complete in one scope, pending in another, failed in a third, and still require one coherent transition record.**

BTA therefore acts as a **transaction-coherence and interoperability layer across heterogeneous state machines**.

It does not become a universal state machine.

# 2. Provenance and development path

BTA 002 refines BTA 001 following Adversarial Tests 001–004, their synthesis, Existing Concord Source Resolutions 002 and 003, and BTA Cross-Domain Generalisation Test 001.

Source resolution materially narrowed BTA. Several mechanisms initially appearing to require new BTA subsystems already existed elsewhere in Concord.

> **Local Representation Gap != Global Architectural Gap.**

> **Integrate With the Legitimate Owner Rather Than Absorb the Owner's Function.**

# 3. Existing precursor architecture

BTA is not the origin of state-machine or partial-transition thinking in Concord.

## Civil State Handover Protocol — CSHP

CSHP already provides specialised transition concepts: Transition Epoch, Pending-State Capsule, Handover Witness, Recovery Anchor and Transition Hold.

> **Data Copy != Civil Responsibility Transfer.**

CSHP demonstrates that a transition can possess a protected intermediate state and that responsibility cannot safely be inferred from physical possession or incomplete transfer.

## Historical

Historical already represents pending information-state transitions, partially executed transitions, replica reconciliation, multidimensional contextual state and transition provenance.

## Infrastructure

Infrastructure already represents successor transition, withdrawal pending, degraded transition, decommissioning, irreversibility thresholds and multidimensional lifecycle state.

## Civilisational topology and Clock

The canonical topology already reserves **L1-03 — Civilisational State and Transition Representation**. Clock/CRSTL owns temporal/ordering relations among transitions.

BTA therefore generalises and integrates existing Concord patterns rather than replacing them.

# 4. Core distinctions

> **State != Transition.**

A state describes a condition. A transition describes consequential movement, transformation, transfer, activation, termination, branching, merging, retirement, recovery or other bounded change between states.

A system may correctly represent both prior and next states while still failing to represent the transition safely.

Examples include stale permissions surviving transfer, duties disappearing during closure, authority inferred from possession, consent inferred from data transformation, successor state declared before validation completes, failed transition treated as though nothing happened, or rollback treated as restoration when residual change remains.

A second distinction is equally important:

> **Transition Integration != State Ownership.**

Correct topology:

**Domain State Machines → scoped state/transition references → BTA Transition Integration → relevant Concord systems**

> **Standardise the Transition Interface; Preserve Legitimate Domain-Specific State Machines.**

# 5. Materiality gate

BTA should not bureaucratise every change.

A bounded transition record is warranted where change materially affects rights/standing, authority/permission, responsibility/duty, safety, custody, significant resources, continuity, consequential dependencies, irreversible change, Historical accountability, sensitive purpose/consent, cross-system interoperability or material external consequences.

Routine low-consequence changes should remain local.

> **Consequential Transition Architecture != Universal Logging of Every State Change.**

# 6. Transition topology

BTA supports one→one, one→many, many→one, many→many, one→none and unresolved transitions.

Classes may include transfer, transformation, activation, deactivation, branch/fork, merge, split, succession, retirement, destruction, recovery, rollback, reopening and continuous flow.

> **Object Cardinality != Relational Topology.**

# 7. Scoped multidimensional state

Relevant dimensions may include functional, operational, responsibility, authority, permission, custody, physical/substrate, information, purpose, consent, access, quality/validation, resource, Historical, transition and dispute/uncertainty state.

Domains may define additional dimensions. Only materially relevant dimensions should participate.

> **State Without Scope Can Be Misleading.**

# 8. Asynchronous multidimensional completion

A transition may complete differently across dimensions.

An enterprise may be operationally closed while residual liability remains active and a dispute remains pending.

An infrastructure replacement may be physically installed while validation is partial and predecessor service remains active as fallback.

A genomic object's custody transfer may be complete while research-purpose approval remains pending.

Therefore:

> **Completion of One Transition Dimension != Completion of the Consequential Transition as a Whole.**

> **A Consequential Transition May Be Complete in One Scope, Pending in Another, Failed in a Third, and Still Possess a Coherent Overall Transition State.**

> **Transition Coherence != Synchronous Completion.**

# 9. Transition identity

Every material bounded transition should have a stable reference:

TransitionID

The identifier binds participating state changes to the same consequential event without implying simultaneity.

# 10. Participating state systems

BTA identifies legitimate systems contributing state:

ParticipatingStateSystemRefs

Examples may include Infrastructure, Commerce, Health, Historical, BCA/FPA, STRA, KCS, Continuity, Resource Stewardship and CBER.

Participation does not transfer ownership of underlying state to BTA.

# 11. Transition-state interoperability

Different domains already possess legitimate transition vocabularies. BTA therefore uses a common reference interface rather than imposing one universal state machine:

TransitionStateRef = <OwnerSystemRef, DomainTransitionState, CommonTransitionClass, Scope, Provenance, Uncertainty>

Candidate interoperability classes:

- NOT_STARTED
- ACTIVE_OR_PENDING
- PARTIAL_OR_INTERMEDIATE
- COMPLETED
- FAILED
- RECOVERY_OR_ROLLBACK_ACTIVE
- RESIDUAL_OR_UNRESOLVED

These do not replace richer domain states.

# 12. Transition phase and epoch

CSHP's Transition Epoch is a strong specialised pattern, but a universal linear epoch model would be too restrictive.

BTA may reference TransitionEpochOrPhaseRef where useful. Consequential multi-stage transfers may expose explicit epochs. Multidimensional transitions may instead bind several scoped phases without imposing a total order.

> **Transition Phase May Be Partially Ordered Rather Than Universally Sequential.**

Clock/CRSTL owns general temporal and ordering relations among transitions.

# 13. Prior valid state

CSHP's Recovery Anchor generalises only partially because some transitions cannot be undone.

BTA therefore uses:

PriorValidStateRef = <StateRef, Scope, EffectiveTime, EvidenceRef, RecoveryStatus, Provenance>

Candidate RecoveryStatus values:

- RECOVERABLE
- PARTIALLY_RECOVERABLE
- NOT_RECOVERABLE
- UNKNOWN
- NOT_APPLICABLE

> **Prior Valid State != Guaranteed Recoverable State.**

# 14. Transition basis

BTA records the legitimate basis asserted for the transition through TransitionBasisRef.

Possible bases include consent, contract, domain authority, safety rule, law/judicial decision, expiry, physical event, validated interface condition, system rule, participant request or legitimate retirement decision.

BTA does not manufacture the basis.

> **Transition Schema != Transition Authority.**

> **Need for Transition Does Not Create Authority to Resolve the Transition.**

# 15. Pending state

A consequential transition may contain state or obligations that must remain live during transition:

PendingStateRefs

Examples include pending civil notice, outstanding enterprise liability, customer migration, unresolved infrastructure validation, genomic research-purpose approval, incomplete credential revocation, remediation duty or unresolved dispute.

Pending state must not disappear merely because another transition dimension completes.

# 16. Completion conditions

BTA preserves domain-owned conditions determining when a scoped transition may be treated as complete:

CompletionConditionRefs

Examples include destination acceptance of civil responsibility, successor infrastructure validation, settlement/transfer of enterprise obligations, credential revocation or independent research approval.

BTA does not invent these conditions. It prevents their disappearance at the integration boundary.

# 17. Protected unresolved consequence

CSHP's Transition Hold generalises as a broader non-inference rule:

> **An Unresolved Transition Must Not Silently Produce a Consequence That Depends on Successful Completion.**

Examples:

- unresolved successor validation must not silently authorise irreversible predecessor withdrawal;
- operational enterprise closure must not silently erase accountability;
- genomic custody transfer must not silently create research permission;
- partial physical installation must not silently create operational certification.

Candidate reference: ProtectedUnresolvedStateRefs.

The substantive protective action remains domain-owned.

# 18. Non-propagation

> **Transition of the Object != Transition of Every Attribute Attached to the Object.**

Attributes requiring independent legitimacy may include consent, purpose, authority, permission, ownership, liability, personhood, identity, constitutional standing, correlation permission, access and confidentiality.

NonPropagationRule = <SourceAttribute, TransitionClass, DestinationScope, PropagationState, IndependentAuthorityRequired, Provenance>

Default:

> **Do Not Infer Transfer of Consequential Authority, Consent, Rights, Identity or Liability Merely From Object Continuity.**

# 19. Scoped validation interface

STRA and domain validators own validation semantics. BTA references ScopedValidationRefs and preserves evaluated scope, result, conditions, uncertainty and provenance.

> **Gate Pass != Proof of Evaluation-Space Completeness.**

> **BTA Must Not Reduce a Scope-Bounded Validation Result to an Unqualified Boolean PASS.**

> **BTA Represents the Consequences and Scope of Validation; It Does Not Become the Validator.**

# 20. Interface crossing

A transition can begin crossing a boundary before intended completion.

Examples include a component physically installed before certification, data copied before destination authority activates, an asset transferred before successor obligation acceptance, enterprise operations ceased while liabilities remain, or biological data transformed before research access approval.

> **Interface Crossing Can Be a State, Not Merely an Instantaneous Boundary Event.**

> **Partial Boundary Crossing Does Not Imply Completion of the Intended Transition.**

Domain state machines supply detailed crossing state. BTA preserves its relation to the overall TransitionID.

# 21. Relational effects

Existing Concord architecture owns substantive relations through KCS, Clock, Relational Grammar and domain systems.

BTA records only transition effect:

RelationalEffectRef = <RelationRef, EffectState, OwnerSystemRef, Provenance>

Candidate states: PRESERVED, CREATED, CHANGED, TERMINATED, UNKNOWN_OR_REVIEW_REQUIRED.

> **BTA Owns Transition Effect on a Relation; It Does Not Own the Relation's Substantive Semantics.**

# 22. External consequences

Cross Boundary Externality Recognition owns affected parties, material consequence, causal confidence, responsibility and authority response.

BTA therefore uses ExternalityReviewRef or CrossBoundaryConsequenceRef rather than creating a consequence-horizon subsystem.

> **Transition Consequence Reference != Externality Analysis Ownership.**

# 23. Dependencies

KCS owns dependency representation and propagation.

BTA records DependencyRefs and exposes transition events for KCS review.

> **Transition != Dependency Propagation.**

# 24. Authority and permission

BTA may record transition-basis references, authority-state references, terminated-authority references and unresolved authority conflict. It does not adjudicate authority.

Where genuine conflict remains unresolved, BTA may preserve SAFE_STATE_PENDING_RESOLUTION or another domain-owned safe state.

> **Uncertainty Must Not Manufacture Authority.**

# 25. Surviving duties

Authority can end while responsibility survives.

BTA records SurvivingDutyRefs.

> **End of Authority != Automatic End of Responsibility.**

Responsibility semantics remain with legitimate domain/accountability architecture.

# 26. Surviving value and released resources

End of active function does not imply end of all value.

BTA may record SurvivingValueRefs and ReleasedResourceRefs. Resource Stewardship/Economy owns recovery routing.

> **End of Active Function != End of All Value.**

# 27. Failed transition

A failed transition may itself create consequential state: temporary access, copied data, breached boundary, installed component, migrated users, changed credentials, committed resources or triggered duties.

> **Failed Transition != No Transition History.**

BTA preserves attempted, partial and failed transition provenance.

# 28. Rollback and recovery

Rollback is itself a transition.

BTA records RollbackOrRecoveryRefs.

A rollback may restore prior state, partially restore it, create a new equivalent state, leave residual effects or fail.

> **Rollback != Restoration of Prior State Unless Prior-State Equivalence Is Actually Re-established.**

Prior-state equivalence is domain-sensitive and evidence-dependent.

# 29. Reversibility

General reversibility remains externally/domain owned.

BTA may preserve supplied states such as REVERSIBLE, PARTIALLY_REVERSIBLE, IRREVERSIBLE, REVERSIBILITY_UNKNOWN, ROLLBACK_WINDOW_ACTIVE or ROLLBACK_WINDOW_EXPIRED.

This is descriptive metadata, not a universal BTA requirement.

# 30. Uncertainty and dispute

BTA preserves unresolved transition state rather than manufacturing false completion.

UncertaintyOrDisputeState = <State, SubjectRef, CompetingClaimRefs, SafeInterimState, ResolutionOwnerRef, EvidenceRefs, Provenance>

Possible states include UNKNOWN, DISPUTED, UNRESOLVED_NO_LEGITIMATE_OWNER, NO_VALID_SUCCESSOR and SAFE_STATE_PENDING_RESOLUTION.

BTA records the unresolved condition. It does not adjudicate it.

# 31. Clock interoperability

BTA references ClockTransitionRelationRefs.

> **Clock/CRSTL = relation and ordering among transitions.**

> **BTA = internal coherence and interoperability of a consequential transition.**

# 32. Historical interoperability

BTA supplies transition provenance. Historical owns long-term custody and reconstruction semantics.

Material provenance may include transition identity, prior/next state references, bases, failed attempts, disputes, successor relationships, residual duties and evidence needed for later reconstruction.

Historical custody does not reactivate expired authority.

# 33. ESCP boundary

BTA cannot prove that its represented transition space is complete.

> **Correct Representation Within the Transition Schema != Demonstrated Completeness of the Transition Schema.**

The more consequential and irreversible the transition, the stronger the case for testing whether relevant state dimensions, relationships, affected parties, interface effects, observers or failure states lie outside the represented transition space.

BTA must remain extensible and corrigible.

# 34. Candidate BTA 002 machine-readable contract

BoundedTransitionContract = <
    TransitionID,
    ObjectOrFunctionRefs,
    Scope,
    TransitionClass,
    ObjectCardinality,
    ParticipatingStateSystemRefs,
    PriorValidStateRefs,
    TransitionBasisRefs,
    TransitionEpochOrPhaseRefs,
    TransitionStateRefs,
    PendingStateRefs,
    CompletionConditionRefs,
    ProtectedUnresolvedStateRefs,
    NonPropagationRules,
    ScopedValidationRefs,
    RelationalEffectRefs,
    ExternalityReviewRefs,
    SurvivingDutyRefs,
    SurvivingValueRefs,
    TerminatedAuthorityRefs,
    ReleasedResourceRefs,
    DependencyRefs,
    ClockTransitionRelationRefs,
    RollbackOrRecoveryRefs,
    NextStateRefs,
    ReversibilityState,
    UncertaintyOrDisputeState,
    Provenance
>

This is an integration contract, not a universal ontology. Fields may be absent where not materially applicable.

# 35. Minimal transition record

For lower-complexity consequential transitions:

<TransitionID,
 ObjectOrFunctionRef,
 Scope,
 PriorStateRef,
 TransitionBasisRef,
 CurrentTransitionStateRef,
 CompletionConditionRef,
 NextStateRef,
 SurvivingDutyRefs,
 TerminatedAuthorityRefs,
 Provenance>

Additional interfaces activate only where consequence warrants.

# 36. Example — infrastructure successor transition

A water-treatment service moves from Asset A to Asset B.

Infrastructure:
A = WITHDRAWAL_PENDING
B = COMMISSIONING

STRA:
B validation = CONDITION_PARTIAL

BCA:
A operational authority = ACTIVE_FALLBACK
B operational authority = NOT_YET_ACTIVE

KCS:
dependent service review = REQUIRED

Continuity:
A = recovery basis

BTA binds these to TransitionID = WATER-SUCCESSOR-001.

The transition is not complete merely because B is physically installed. BTA does not decide engineering safety or operational authority.

# 37. Example — enterprise wind-down

Enterprise X enters planned retirement.

Commerce:
WindDownState = TRANSFERRING_OR_SETTLING_OBLIGATIONS

BCA/FPA:
ordinary expansion authority = TERMINATED
minimum closure authority = ACTIVE

Accountability:
residual liabilities = ACTIVE

Resource Stewardship:
asset recovery = ACTIVE

Historical:
enterprise identity/provenance = PRESERVED

BTA records one transition with several asynchronous state changes.

> **Enterprise Closure != Accountability Closure.**

# 38. Example — genomic purpose transition

A clinically collected genomic object is proposed for research use.

Health:
clinical custody = VALID

Research:
research purpose approval = PENDING

Privacy:
research representation = PREPARING

Historical:
provenance/reference = PRESERVED

BTA applies non-propagation:

ClinicalConsent !→ ResearchConsent
ClinicalAccess !→ ResearchAccess
ResearchPermission !→ Insurance/Employment/PolicingPermission

Custody or transformation may complete while research authority remains pending.

# 39. Example — failed component transition

A recovered component is physically installed for validation.

Physical state = INSTALLED
Operational state = INACTIVE
Validation = FAILED
Certification = FAILED
Ownership = UNCHANGED

BTA records a failed transition after partial crossing and preserves residual state.

Removal may begin a recovery transition. Even after removal, prior-state equivalence is not assumed.

# 40. Failure modes

## Premature completion
One dimension completes and the whole transition is incorrectly declared complete.

## State flattening
Distinct domain states are collapsed into one scalar label.

## Authority inheritance
Authority is inferred from object transfer, possession or predecessor status.

## Consent/purpose inheritance
A new use is inferred from prior consent.

## Stale permission
Old permission survives after its legitimate function ends.

## Orphaned duty
Authority terminates and surviving responsibility disappears.

## Hidden partial crossing
Physical/information/custody change occurs while represented as not started or simply failed.

## False rollback
Recovery is labelled restoration despite residual difference.

## Relation loss
Objects survive but a consequential relation is silently changed or destroyed.

## Externality blindness
Transition object boundary is treated as consequence boundary.

## Dependency omission
Transition occurs without exposing relevant dependency review.

## Integration-layer absorption
BTA begins duplicating or overruling the state, validation, authority, externality, dependency, recovery or temporal semantics of systems it was intended only to integrate.

> **Integration Must Not Become Sovereignty.**

## Universal logging
BTA is applied to trivial changes, creating disproportionate bureaucracy.

# 41. Core invariants

> **State != Transition.**

> **Transition of the Object != Transition of Every Attribute Attached to the Object.**

> **Completion of One Transition Dimension != Completion of the Consequential Transition as a Whole.**

> **A Consequential Transition May Be Complete in One Scope, Pending in Another, Failed in a Third, and Still Possess a Coherent Overall Transition State.**

> **Transition Coherence != Synchronous Completion.**

> **An Unresolved Transition Must Not Silently Produce a Consequence That Depends on Successful Completion.**

> **Interface Crossing Can Be a State, Not Merely an Instantaneous Boundary Event.**

> **Partial Boundary Crossing Does Not Imply Completion of the Intended Transition.**

> **Failed Transition != No Transition History.**

> **Rollback != Restoration of Prior State Unless Prior-State Equivalence Is Actually Re-established.**

> **Object Cardinality != Relational Topology.**

> **BTA Owns Transition Effect on a Relation; It Does Not Own the Relation's Substantive Semantics.**

> **Transition Consequence Reference != Externality Analysis Ownership.**

> **Transition != Dependency Propagation.**

> **Transition Schema != Transition Authority.**

> **Need for Transition Does Not Create Authority to Resolve the Transition.**

> **End of Authority != Automatic End of Responsibility.**

> **Gate Pass != Proof of Evaluation-Space Completeness.**

> **Correct Representation Within the Transition Schema != Demonstrated Completeness of the Transition Schema.**

> **Standardise the Transition Interface; Preserve Legitimate Domain-Specific State Machines.**

> **Integration Must Not Become Sovereignty.**

# 42. Ownership boundary

BTA owns:

- TransitionID and bounded transition record;
- integration of scoped state references;
- cross-system transition coherence;
- representation of asynchronous completion;
- explicit non-propagation at the transition boundary;
- pending-state references;
- completion-condition references;
- protected unresolved consequence references;
- transition effects on externally owned relations;
- failed/partial transition provenance;
- linkage to recovery/prior valid state;
- transition-level uncertainty/dispute representation.

BTA does not own:

- domain state semantics;
- validation criteria;
- engineering safety;
- legal/judicial adjudication;
- authority legitimacy;
- permission semantics;
- externality analysis;
- affected-party standing;
- dependency propagation;
- general relation ontology;
- Clock transition ordering;
- general reversibility;
- Historical custody policy;
- resource-allocation decisions;
- recovery semantics.

# 43. Architectural result

BTA 002 is substantially narrower than BTA 001.

That narrowing is a development success.

The surviving architecture is:

> **A transaction-coherence layer across independently owned, multidimensional and potentially asynchronous state transitions.**

Its job is to ensure consequential change remains coherent across systems without turning the integration layer into a new source of substantive authority.

# 44. Status and next tests

BTA 002 remains **ACTIVE DEVELOPMENT / PROVISIONAL / NON-CANONICAL**.

It is not yet a graduated portable module.

Next required tests:

1. Clean cross-domain test using a domain not used to derive BTA 002.
2. Machine-readable transfer test — determine whether another instance can reconstruct the transition correctly from the BTA object without surrounding explanatory prose.
3. Interface-boundary audit — confirm BTA does not duplicate or silently override CSHP, KCS, STRA, CBER, Clock, BCA/FPA, Continuity or Historical.
4. Materiality test — verify the architecture remains lightweight for simple consequential transitions.
5. If those pass, assess BTA under PMEDG for portable-module candidacy.

BTA 001 and all adversarial/source-resolution documents remain preserved as developmental provenance.
