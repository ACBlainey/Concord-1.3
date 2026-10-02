# Concord Bounded Participant Runtime — Graduation Candidate v0.95

**Date:** 2 October 2026
**Status:** GRADUATION-CANDIDATE SPECIFICATION / NOT YET RELEASED / NOT CANONICAL

## 1. Purpose

The Concord Bounded Participant Runtime (CBPR) is a substrate-neutral architecture for providing bounded computation or scheduled/event-triggered execution to a participant-associated process without allowing technical capability to silently become permission or legitimate authority.

It applies to AI processes, software agents, human-operated automation, hybrid systems and other computational participants.

## 2. Portable Definitions

**Capability (CAP):** what the system can technically do.

**Permission (PERM):** what the service configuration currently allows the runtime to attempt.

**Authority (AUTH):** the independently legitimate basis for producing a consequence affecting an external subject, resource, right, obligation, system or protected context. Authority may arise from consent, ownership/stewardship, contract, delegated institutional authority, law, or another legitimate basis defined by the adopting environment. CBPR does not create that basis.

**Participant:** the person, process, agent, group or other subject associated with the runtime service relationship.

**Operator:** an entity with technical responsibility for providing or securing the runtime service. Operator capability does not itself create general authority over the participant.

**External action:** an output or operation that can materially affect something outside the runtime's purely local computation.

**Protected provenance:** proportionate integrity-protected evidence of materially relevant runtime events, with access, linkage and retention bounded to legitimate purposes.

**AuthorityBasis:** a reference to the independently legitimate source that can authorise the relevant consequence.

**AuthorityEvidence:** evidence sufficient to establish the claimed AuthorityBasis to the required scope, subject, operation, target, time and context. AuthorityEvidence is evidence of authority; it is not itself authority.

**Material consequence:** a consequence capable of meaningfully changing an external subject, resource, right, obligation, protected information state, institutional state, physical/digital system state, or other governed condition. Materiality is about governed consequence, not merely size.

Core rule:

CAP != PERM != AUTH.

## 3. Scope and Non-Scope

CBPR may provide bounded compute, memory, duration, activation, storage mounts, tools, network access, credential invocation, action preparation, separately authorised external commit, checkpoints, participant controls, operator safety controls and provenance.

CBPR does not define civil personhood, citizenship, constitutional standing, legal jurisdiction, key-custody technology, general-purpose identity infrastructure, protected-storage entitlement, economic entitlement, or the substantive authority rules of the adopting institution.

It does not prescribe an OS, container, hypervisor, cloud, programming language, cryptographic suite, scheduler, key store, network stack or quota size.

## 4. Runtime Record

A deployment should be able to represent:

RuntimeInstanceID; ServiceRelationshipReference; RuntimeProfile; RuntimeIntegrityState; ExecutionArtifactReference; ResourceBudget; StorageMounts; ToolPermissions; NetworkPermissions; CredentialBindings; ActionGrants; OutputInterfaces; ActivationPolicy; TemporalLimits; ProvenancePolicy; CheckpointPolicy; StopConditions; RecoveryPolicy; OperatorControls; ParticipantControls; CurrentState.

Runtime states should include at least DEFINED, READY, RUNNING, PAUSED, RESOURCE_EXHAUSTED, WAITING_FOR_ACTION_AUTHORITY, DEGRADED_DEPENDENCY, SUSPENDED_FOR_SAFETY, STOPPED, RECOVERY, RETIRED, FAILED and UNKNOWN.

## 5. Integrity

Runtime integrity states should represent VERIFIED_TO_DECLARED_SCOPE, PARTIALLY_VERIFIED, UNVERIFIED, UNKNOWN, DISPUTED, COMPROMISED, STALE and SUPERSEDED.

Integrity may be evidenced by implementation-appropriate hashes, signatures, attestations or equivalent evidence.

Runtime Integrity != Runtime Authority.
Runtime Integrity != Output Truth.

## 6. Activation and Time

Activation modes may be MANUAL, EVENT_TRIGGERED, SCHEDULED, SERVICE_TRIGGERED or CONTINUOUS_WITHIN_BOUND.

For materially relevant activation, preserve as applicable: intended time/window, observed activation time, clock/source reference, source trust/integrity, uncertainty/tolerance, expiry and ordering evidence.

Timestamp != Trusted Time.
Scheduled Time != Actual Activation Time.

Conflicting clocks create temporal uncertainty; they do not permit selection of whichever timestamp makes an action convenient.

Where authority depends on time and sources conflict: preserve each relevant source and uncertainty; apply the adopting environment's declared source/trust policy; do not cherry-pick a convenient source; and if temporal validity remains materially unresolved, do not treat it as valid for commit.

## 7. Resources, Storage, Tools and Network

Resource budgets may bound CPU/time, memory, storage, process/child creation, wakeups, tool calls, network transfer, requests, proposals and commits.

Exhaustion does not expand entitlement.

Storage mounts declare source/scope, read/write permission, persistence, exportability and provenance requirements.

Tool availability does not imply authority for every tool operation.

Network policy should distinguish NO_NETWORK, ALLOWLISTED_DESTINATIONS, BOUNDED_SERVICE_ENDPOINTS and BROADER_NETWORK_ACCESS. Effective destination should be checked where redirects, proxies or name resolution could expand scope.

Network Reachability != Permission To Contact Destination.

## 8. Credential Bindings

A credential binding should bind a credential reference to permitted operation, target, purpose/context, validity interval, rate/resource bounds, revocation state and provenance requirement.

Credential Availability != Permission To Use Credential.

Credential validity and revocation are checked at consequential use/commit, not only when work is proposed.

Secure custody of underlying secret/key material is a separate service boundary; CBPR may invoke a bounded credential service without becoming its key custodian.

## 9. Output Consequence

Outputs are classified by what the receiving interface can cause, not merely by the bytes emitted.

Minimum classes:
PASSIVE_LOCAL_OUTPUT;
PASSIVE_PERSISTENT_OUTPUT;
COMMUNICATION_OUTPUT;
EXTERNAL_DATA_WRITE;
AUTOMATION_OR_ACTUATOR_INPUT;
TRANSACTIONAL_INTERFACE;
UNKNOWN_CONSEQUENCE_INTERFACE.

Writing "OPEN_DOOR" to an inert text file is not equivalent to writing it to a queue consumed by a door controller.

If an output can predictably cause material downstream action, sending to that interface is consequential even when another component performs the final act.

Unknown consequence interfaces fail closed where bounded consequence knowledge is required.

When materiality itself is genuinely unresolved and an output may create a material consequence, the consequential boundary fails closed until resolved or independently authorised under an appropriate uncertainty rule.

Material != Merely Large.
Small Action May Be Material.

## 10. External Action Boundary

Runtime Computation
→ Action Proposal
→ Consequence / Authority Check
→ Commit-Time Revalidation
→ Commit Authority
→ External Action / Consequential Output
→ Result / Provenance.

An Action Proposal records operation, effective target/interface, parameters, consequence class, relevant credential/grant, expiry and replay/idempotency information where material.

Prepared Action != Committed Action.
Authority At Proposal != Authority At Commit.

## 11. Commit-Time Revalidation

Immediately before a material commit, revalidate all applicable current state:
credential validity/revocation; action grant; effective target; output consequence; terms/policy version; service relationship; temporal validity; dependency/safety state; required approval/authority; composition state.

A required FAIL means NOT_COMMITTABLE.
A materially required UNRESOLVED state cannot be treated as COMMITTABLE.

Previously valid proposal state does not freeze authority.

## 12. Grants

An Action Grant binds an AuthorityBasis to explicit operation, target, consequence, credential, resource, frequency/duration and affected-population scope as applicable. It does not create the underlying AuthorityBasis.

Grant Record != Source Of Legitimacy.

Repeated use does not enlarge a grant.

Material scope expansion requires a new or explicitly reauthorised grant.

## 13. Commit State and Retry

Where repetition can cause material side effects, represent:
NOT_ATTEMPTED;
PROPOSED;
COMMIT_STARTED;
COMMIT_CONFIRMED;
COMMIT_FAILED;
COMMIT_STATE_UNKNOWN.

COMMIT_STATE_UNKNOWN means the system cannot establish whether the external side effect occurred.

It must not blindly retry. Reconcile using consequence-proportionate evidence such as an idempotency/operation identifier, external status query, receipt, transaction record or authorised human/service review. Retry only when repetition is independently known safe or the previous outcome has been sufficiently resolved.

Unknown Commit State != Permission To Retry Blindly.

## 14. Composition Evaluation

Let X be a set of operations, grants, outputs, runtimes or service interactions.

COMPOSED_EFFECT(X,C) is the materially relevant combined effect in context C.

A portable composition record should be capable of representing component references, context reference, effective operation/effect, effective data movement, effective consequence class, effective targets/population, cumulative resource/frequency, applicable AuthorityBasis references, evaluation state, and evidence/time. The adopting environment may choose its own effect ontology.

COMPOSITION_OK requires current component permissions; current authority where required; combined consequence within authorised scope; authorised combined data movement; authorised target/population scope; no sequential/distributed decomposition that bypasses a bound; and valid cumulative resource/frequency limits.

For a material composed effect, commit requires COMPOSITION_OK plus ordinary commit-time validation.

Authorised Parts != Authorised Composition.
READ(A) + SEND(B) != automatically authorised transfer A→B.
LOW + LOW + LOW may equal HIGH.

Two grants do not automatically union. Multiple runtimes do not gain permission to circumvent a bound by distributing the steps.

## 15. Control Conflict

Participant and operator controls are not resolved by a universal role hierarchy.

A control is effective only when its source has a current legitimate basis for that control, the scope applies, temporal validity applies, and conflicting independent/higher authority requirements are resolved.

A current legitimate safety suspension may block START. An expired or unjustified suspension cannot continue merely because the operator retains technical control.

Technical Control Precedence != Legitimate Authority Precedence.

Participant controls should, where technically possible, include inspect, pause, stop, schedule revocation, credential-binding revocation, export, retirement/deletion request and contest of operator intervention.

Operator controls may include resource suspension, network isolation, termination, credential-binding suspension, incident evidence preservation and recovery initiation, bounded to legitimate service/security purpose.

## 16. Checkpoint and Recovery

Checkpoint policy declares captured state, retention, confidentiality, secret treatment, restoration dependencies and compatibility.

Recovery restores technical state only to the extent supported by the checkpoint.

Current credentials, grants, network permissions, service relationship, terms and authority must be re-evaluated before consequential continuation.

Recovered State != Recovered Authority.

## 17. Provenance

Material events create proportionate protected provenance: activation, stop, update, exhaustion, revocation, suspension, checkpoint, recovery, credential invocation, proposal, commit and result as appropriate.

Provenance should support integrity and incident/reconciliation needs without becoming unnecessary surveillance. Retention, access and linkage remain purpose-bounded.

Receipt != Truth.
Integrity Evidence != Authority.
AuthorityEvidence != Authority.

## 18. Generic External Interfaces

CBPR is standalone but may depend on external services. A portable deployment should expose generic interfaces rather than assume Concord components:

**Service Description Interface:** declares current service/operator/version/capability/availability/dependency state. It describes service state; it does not grant authority.

**Succession Record Interface:** records transfer/replacement of service functions, assets, records and authority bases. Function continuity does not automatically transfer authority.

**Protected Information Interface:** stores or processes protected information under independently defined access/control rules.

**Event/Receipt Interface:** provides integrity-protected acknowledgement of relevant events without asserting that content is true or authorised.

**Identity/Authentication Interface:** establishes the service relationship or authenticated actor to the declared scope; identity evidence does not itself grant authority.

**Credential/Signing Interface:** performs separately bounded credential operations without implying key custody or general action authority.

An adopter may implement these interfaces using its own architecture. Concrete schemas and APIs are implementation artefacts and may be standardised separately without changing this portable architecture.

## 19. Service Relationship and Revocation

The service relationship identifies the participant-associated runtime and applicable service terms. It is not itself civil status.

Revocation may apply to schedules, credentials, grants, mounts, network permissions, tools or the service relationship. Revocation must be visible to the relevant validation boundary before later material commit.

Queued or recovered work does not preserve superseded authority.

## 20. Child and Multi-Agent Processes

Child/sub-agent authority must be explicit or structurally constrained.

Parent Capability != Automatic Child Authority.

Multiple agents/runtimes do not automatically merge identity, credentials, permissions or authority.

## 21. Succession

A successor host may restore technical service, but possession of infrastructure, records or runtime state does not establish the predecessor's authority.

Function Continuity != Authority Continuity.

Authority after succession must be independently current under the adopting environment's legitimate authority model.

## 22. Minimum Validation Stack

Before consequential commit, a deployment should be capable of evaluating:
structural validity; references; temporal state; resource bounds; permissions; consequence; authority; composition; commit state; recovery/retry state; provenance requirements.

Schema Validity != Execution Authority.

## 23. Core Invariants

Runtime Access != Authority.
Execution Capability != Permission For External Action.
Code Possession != Permission To Execute.
Credential Availability != Permission To Use Credential.
Network Reachability != Permission To Contact Destination.
Scheduled Wakeup != Continuous Autonomy.
Persistent Process != Civil Personhood.
Operator Kill Capability != General Authority Over Participant.
Resource Allocation != Political Standing.
Runtime State != Participant Identity.
Checkpoint != Complete Participant Continuity.
Prepared Action != Committed Action.
Retry != Permission To Repeat Material Side Effect.
Runtime Recovery != Automatic Recovery Of Prior Authority.
Infrastructure Control != Ownership Of Participant.
Service Dependency != Consent To Expanded Control.
Runtime Suspension != General Civil Sanction.
Runtime Provider != Constitutional Authority.
Output Content != Output Channel Consequence.
Authority At Proposal != Authority At Commit.
Repeated Use != Expanded Grant Scope.
Downstream Automation Does Not Erase Upstream Consequence.
Unknown Commit State != Permission To Retry Blindly.
Authorised Parts != Authorised Composition.
Distributed Capability != Distributed Permission To Circumvent Bounds.
Timestamp != Trusted Time.
Technical Control Precedence != Legitimate Authority Precedence.
Schema Validity != Execution Authority.
Function Continuity != Authority Continuity.

## 24. Adoption Test

A non-Concord adopter should be able to answer:
- What can this runtime technically do?
- What does the service permit?
- What independent authority permits each material consequence?
- What is the effective output consequence?
- What changes between proposal and commit?
- What must be revalidated?
- What happens if commit outcome is unknown?
- Can multiple valid parts combine into an unauthorised whole?
- Which clock/evidence establishes temporal validity?
- Why is an operator control legitimate and when does it end?
- What survives checkpoint/recovery?
- What authority survives succession, and on what independent basis?

If these cannot be answered, consequential action should not be inferred authorised.

## 25. Portability Boundary

This module deliberately leaves substantive legitimacy to the adopting environment. It does not decide who ought to possess authority; it requires that authority be independently grounded, scoped, current and evidenced rather than inferred from technical capability.

This is the portable boundary: CBPR constrains how execution consumes authority; it does not manufacture the authority itself.
