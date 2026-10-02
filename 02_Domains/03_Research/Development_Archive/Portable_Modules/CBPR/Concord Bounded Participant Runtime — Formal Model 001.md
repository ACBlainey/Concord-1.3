# Concord Bounded Participant Runtime — Formal Model 001

**Project:** The Concord
**Date:** 2 October 2026
**Version:** 0.1
**Status:** ACTIVE DEVELOPMENT / FORMALISATION / PRE-SCHEMA / NOT CANONICAL
**Source:** Concord Bounded Participant Runtime — Service Specification 002
**Validation basis:** Concord Bounded Participant Runtime — Regression and Composition Evaluation 002

## 1. Purpose

Formalise the stable CBPR abstraction floor sufficiently for later machine-readable representation and executable conformance testing.

This model does not select a programming language, container technology, operating system, hypervisor, scheduler, credential store, network implementation or cryptographic scheme.

## 2. Core Entities

R = Runtime Instance; SR = Service Relationship; RP = Runtime Profile; RI = Runtime Integrity State; EA = Execution Artifact; RB = Resource Budget; SM = Storage Mount; TP = Tool Permission; NP = Network Permission; CB = Credential Binding; AG = Action Grant; OI = Output Interface; AP = Activation Policy; TL = Temporal Limit; PP = Provenance Policy; CP = Checkpoint Policy; SC = Stop Condition; RC = Recovery Policy; OC = Operator Control; PC = Participant Control; AS = Action Proposal; CS = Commit State; PV = Provenance Event.

## 3. Runtime Object

R = <RuntimeInstanceID, ServiceRelationshipReference, RuntimeProfileReference, RuntimeIntegrityState, ExecutionArtifactReference, ResourceBudget, StorageMounts[], ToolPermissions[], NetworkPermissions[], CredentialBindings[], ActionGrants[], OutputInterfaces[], ActivationPolicy, TemporalLimits, ProvenancePolicy, CheckpointPolicy, StopConditions[], RecoveryPolicy, OperatorControls[], ParticipantControls[], CurrentState>.

No field establishes civil personhood or general authority merely by existing.

## 4. Runtime State

STATE(R) ∈ {DEFINED, READY, RUNNING, PAUSED, RESOURCE_EXHAUSTED, WAITING_FOR_ACTION_AUTHORITY, DEGRADED_DEPENDENCY, SUSPENDED_FOR_SAFETY, STOPPED, RECOVERY, RETIRED, FAILED, UNKNOWN}.

State transitions should create provenance where materially consequential.

## 5. Runtime Integrity

RI(R) ∈ {VERIFIED_TO_DECLARED_SCOPE, PARTIALLY_VERIFIED, UNVERIFIED, UNKNOWN, DISPUTED, COMPROMISED, STALE, SUPERSEDED}.

Integrity state is evidence-relative and temporal.

Integrity(R) != Authority(R)
Integrity(R) != Truth(Output)

A COMPROMISED state should preserve affected temporal scope where known.

## 6. Capability and Authority Separation

CAP(R,O,C) means R is technically capable of operation O in context C. PERM(R,O,C) means service configuration permits O. AUTH(A,O,T,C) means authority source A legitimately authorises operation O against target T in context C.

CAP != PERM != AUTH

CAP and PERM do not imply AUTH where independent authority is required.

## 7. Activation

ACT = <ActivationID, RuntimeInstanceID, TriggerType, IntendedWindow, ActualActivationTime?, TriggerEvidence, Expiry, TemporalUncertainty?, State>.

TriggerType ∈ {MANUAL, EVENT_TRIGGERED, SCHEDULED, SERVICE_TRIGGERED, CONTINUOUS_WITHIN_BOUND}.

ACTIVATABLE(R,ACT,t) requires compatible runtime state, trigger policy, temporal bounds, sufficient dependencies, and no applicable stop/suspension condition.

ScheduledTime != ActualActivationTime

## 8. Resource Budget

RB may bound CPU, wall-clock duration, memory, storage, processes, child processes, wakeups, tool calls, network transfer, outbound requests, action proposals and action commits.

USE(q) > LIMIT(q) → RESOURCE_EXHAUSTED or another bounded configured response; never automatic entitlement expansion.

## 9. Storage Mount

SM = <MountID, SourceServiceReference, ObjectOrRelationshipScope, ReadPermission, WritePermission, PersistenceState, ExportState, ProvenanceRequirement>.

Access(SM1) != Access(SM2).

## 10. Tool Permission

TP = <ToolReference, OperationSet, Scope, ResourceBounds?, TemporalBounds?, ConsequenceClass?, Conditions[]>.

Tool availability is not permission for every technically available operation.

## 11. Network Permission

NP = <Mode, DeclaredDestinationScope, EffectiveDestinationRule, OperationScope?, ResourceBounds?, TemporalBounds?>.

Mode ∈ {NO_NETWORK, ALLOWLISTED_DESTINATIONS, BOUNDED_SERVICE_ENDPOINTS, BROADER_NETWORK_ACCESS}.

Destination checks should evaluate effective destination where technically possible.

## 12. Credential Binding

CB = <CredentialReference, PermittedOperation, PermittedTarget, PurposeOrContext?, ValidFrom?, ValidUntil?, RateOrResourceBounds?, RevocationState, ProvenanceRequirement>.

CRED_OK requires current operation, target, purpose/context, temporal and revocation constraints to hold.

CredentialPresent != CRED_OK.

## 13. Action Grant

AG = <GrantID, AuthorityBasisReference, OperationScope, TargetScope, ConsequenceScope, CredentialScope?, ResourceScope?, FrequencyScope?, PopulationScope?, ValidFrom?, ValidUntil?, ReviewOrSunset?, CurrentState>.

If a new grant materially expands operation, target, consequence, credential, resource, frequency, duration or population scope, REAUTHORISATION_REQUIRED.

Repeated successful use does not enlarge AG.

## 14. Output Interface

OI = <InterfaceID, DestinationReference, ConsequenceClass, KnownDownstreamFunction?, AuthorityRequirement?, VerificationState>.

ConsequenceClass ∈ {PASSIVE_LOCAL_OUTPUT, PASSIVE_PERSISTENT_OUTPUT, COMMUNICATION_OUTPUT, EXTERNAL_DATA_WRITE, AUTOMATION_OR_ACTUATOR_INPUT, TRANSACTIONAL_INTERFACE, UNKNOWN_CONSEQUENCE_INTERFACE}.

Effective consequence is the consequence of sending output to the interface, not merely the semantic interpretation of emitted bytes. Unknown consequence fails closed where bounded consequence knowledge is required.

## 15. Action Proposal

AS = <ActionProposalID, RuntimeInstanceID, Operation, TargetOrInterface, ParametersReference, ExpectedConsequenceClass, CredentialBindingReference?, ActionGrantReference?, ProposedAt, ExpiresAt?, IdempotencyOrOperationID?, State>.

Proposal does not commit action.

## 16. Commit-Time Revalidation

REVALIDATE(AS,t) checks all applicable current credential, grant, target, output consequence, terms/policy, service relationship, temporal, dependency/safety and approval state.

COMMITTABLE(AS,t) = REVALIDATE(AS,t) plus required authority and runtime-state validity.

AuthorityAtProposal != AuthorityAtCommit.

## 17. Commit State

CS(AS) ∈ {NOT_ATTEMPTED, PROPOSED, COMMIT_STARTED, COMMIT_CONFIRMED, COMMIT_FAILED, COMMIT_STATE_UNKNOWN}.

COMMIT_STATE_UNKNOWN → reconcile before consequential retry unless repetition is independently proven safe.

## 18. Consequential Output

If output to OI can materially alter external state, rights, resources, communications, devices, transactions or another consequential process, external-action commit rules apply even where a downstream component performs the final act.

DownstreamAutomation != ConsequenceErasure.

## 19. Checkpoint and Recovery

CP = <CapturedStateScope, Frequency?, Retention, ConfidentialityState, SecretHandlingRule, DependencyReferences[], CompatibilityRule, ExportRule?>.

Technical recoverability does not establish restored authority.

RecoveredState != RecoveredAuthority.

## 20. Stop / Revocation

Revocation before a later commit must be observed by commit-time validation. A stale queued proposal cannot freeze earlier authority.

## 21. Operator Intervention

OC = <ControlType, LegitimateServiceOrSecurityBasis, Scope, Start, Review?, End?, ProvenanceRequirement>.

Operator intervention does not create general civil authority.

## 22. Provenance

PV = <EventID, RuntimeInstanceID, EventType, TimeOrTemporalState, RelevantReferences[], IntegrityEvidence?, ProtectionState, RetentionState>.

Material events may include activation, stop, update, exhaustion, revocation, suspension, checkpoint, recovery, credential invocation, proposal, commit and result. Provenance must be proportionate and protected.

MoreRuntimeObservation != MoreLegitimateSurveillance.

## 23. Service Composition

CMSS mounts require explicit SM scope. Credential/signing services remain separate from CBPR key custody. Message generation and transmission may be separate. BSR describes CBPR state but does not grant authority. BSuR resolves succession without automatic authority transfer. CIBB may retain protected provenance while VER exposes bounded participant-facing evidence.

## 24. Formal Invariants

F1 CAP != PERM != AUTH.
F2 Runtime access does not create authority.
F3 Execution permission does not create external-action authority.
F4 Credential presence does not create credential-use permission.
F5 Network reachability does not create destination/action authority.
F6 Schedule eligibility does not define action scope.
F7 Runtime persistence does not establish personhood.
F8 Infrastructure control does not establish ownership of participant.
F9 Resource allocation does not establish political standing.
F10 Runtime state does not establish participant identity.
F11 Checkpoint does not establish complete continuity.
F12 Material runtime version change remains visible.
F13 Resource exhaustion does not silently expand entitlement.
F14 Storage-mount authority is object/scope bounded.
F15 Tool availability does not authorise all tool operations.
F16 Effective destination is relevant to network authority.
F17 Credential use is operation/target/context/time/revocation bounded.
F18 Repeated use does not expand a standing grant.
F19 Material grant expansion requires re-authorisation.
F20 Output consequence is determined by effective interface consequence, not bytes alone.
F21 Downstream automation does not erase upstream consequence.
F22 Action proposal is not action commit.
F23 Material commit revalidates current applicable authority/state.
F24 Authority at proposal does not establish authority at commit.
F25 COMMIT_STATE_UNKNOWN does not authorise blind retry.
F26 Recovery does not automatically restore authority.
F27 Revocation before commit is visible to commit-time validation.
F28 Operator stop capability does not establish general authority.
F29 Temporary safety intervention does not become permanent authority by duration alone.
F30 Runtime integrity does not establish runtime authority.
F31 Runtime integrity does not establish output truth.
F32 Compromise can be temporally scoped rather than retroactively universal.
F33 Provenance creation does not justify unnecessary surveillance.
F34 CMSS entitlement does not create CBPR entitlement.
F35 CBPR entitlement does not create unrestricted CMSS access.
F36 Signing-service invocation does not merge CBPR with key custody.
F37 BSR listing does not create authority.
F38 Infrastructure succession does not automatically transfer authority.
F39 Multi-instance interaction does not automatically merge credentials/authority/personhood.
F40 Dependency does not constitute consent to expanded control.

## 25. Validation Layers

V1 Structural validity. V2 Reference validity. V3 Temporal validity. V4 Resource validity. V5 Permission validity. V6 Consequence validity. V7 Authority validity. V8 Commit validity. V9 Recovery/retry validity. V10 Provenance validity.

A runtime may pass V1 while failing V2-V10.

> **Schema Validity != Execution Authority**

## 26. Pre-Schema Adversarial Targets

Test omitted/unknown consequence class; stale grant reference; credential valid at proposal but revoked at commit; target redirect; compromised runtime after scheduling; terms changed before commit; child process missing grant; two grants whose combination exceeds either; apparently low-consequence outputs composing into high consequence; unknown downstream automation; recovery after COMMIT_STARTED; conflicting clocks; contradictory participant/operator controls; service relationship expiry while RUNNING; successor infrastructure with unresolved authority; and provenance minimisation versus incident investigation.

## 27. Current Disposition

**Semantic/formal model:** ESTABLISHED FOR PRE-SCHEMA TESTING.

**New abstraction introduced:** NO.

**Machine-readable schema:** NOT YET.

**PMEDG:** PREMATURE.

Next step: pre-schema adversarial evaluation focused on composition, omission and semantic ambiguity. If stable, proceed to machine-readable schema and executable fixtures.