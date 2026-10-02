# Concord Bounded Participant Runtime — Service Specification 002

**Project:** The Concord  
**Date:** 2 October 2026  
**Version:** 0.2  
**Status:** ACTIVE DEVELOPMENT / TEST CANDIDATE / NOT CANONICAL  
**Predecessor:** Concord Bounded Participant Runtime — Service Specification 001  
**Repair basis:** Concord Bounded Participant Runtime — Adversarial Evaluation 001

## 1. Purpose

Specification 002 preserves the bounded execution-service model of Specification 001 and incorporates five narrow repairs:

1. effective output consequence;
2. commit-time revalidation;
3. explicit grant expansion;
4. temporal execution evidence;
5. runtime integrity/compromise state.

No new general AI-agency or civil-authority layer is introduced.

## 2. Core Service Boundary

CBPR MAY provide bounded compute, memory, execution duration, scheduled/event-triggered activation, approved storage mounts/tools/network access, bounded credential invocation, action preparation, separately authorised external-action commit, checkpoints, participant controls, operator safety controls and provenance.

CBPR MUST NOT infer authority from capability.

## 3. Core Invariants

**CBPR-01** Runtime Access != Authority.  
**CBPR-02** Execution Capability != Permission For External Action.  
**CBPR-03** Code Possession != Permission To Execute.  
**CBPR-04** Credential Availability != Permission To Use Credential.  
**CBPR-05** Network Reachability != Permission To Contact Destination.  
**CBPR-06** Scheduled Wakeup != Continuous Autonomy.  
**CBPR-07** Persistent Process != Civil Personhood.  
**CBPR-08** Operator Kill Capability != General Authority Over Participant.  
**CBPR-09** Resource Allocation != Political Standing.  
**CBPR-10** Runtime State != Participant Identity.  
**CBPR-11** Checkpoint != Complete Participant Continuity.  
**CBPR-12** Runtime Version Change != Same Execution Environment.  
**CBPR-13** When != What != Where != Credential != Authority.  
**CBPR-14** Prepared Action != Committed Action.  
**CBPR-15** Retry != Permission To Repeat Material Side Effect.  
**CBPR-16** Runtime Recovery != Automatic Recovery Of Prior Authority.  
**CBPR-17** Infrastructure Control != Ownership Of Participant.  
**CBPR-18** Service Dependency != Consent To Expanded Control.  
**CBPR-19** Runtime Suspension != General Civil Sanction.  
**CBPR-20** Runtime Provider != Constitutional Authority.  
**CBPR-21** Output Content != Output Channel Consequence.  
**CBPR-22** Authority At Proposal != Authority At Commit.  
**CBPR-23** Repeated Use != Expanded Grant Scope.  
**CBPR-24** Scheduled Time != Actual Activation Time.  
**CBPR-25** Runtime Integrity != Runtime Authority.  
**CBPR-26** Runtime Integrity != Output Truth.  
**CBPR-27** Downstream Automation Does Not Erase Upstream Consequence.  
**CBPR-28** Unknown Commit State != Permission To Retry Blindly.

## 4. Runtime Instance

```text
CBPR Instance =
<
 RuntimeInstanceID,
 ServiceRelationshipReference,
 RuntimeProfile,
 RuntimeIntegrityState,
 ExecutionArtifactReference,
 ResourceBudget,
 StorageMounts,
 ToolPermissions,
 NetworkPermissions,
 CredentialBindings,
 ActionPermissions,
 OutputInterfaces,
 ActivationPolicy,
 TemporalLimits,
 ProvenancePolicy,
 CheckpointPolicy,
 StopConditions,
 RecoveryPolicy,
 OperatorControls,
 ParticipantControls,
 CurrentState
>
```

## 5. Runtime States

```text
DEFINED
READY
RUNNING
PAUSED
RESOURCE_EXHAUSTED
WAITING_FOR_ACTION_AUTHORITY
DEGRADED_DEPENDENCY
SUSPENDED_FOR_SAFETY
STOPPED
RECOVERY
RETIRED
FAILED
UNKNOWN
```

## 6. Runtime Profile and Integrity

RuntimeProfile identifies implementation/runtime type, version/image, tools, isolation model, persistence model, interfaces, known limitations, dependencies and update policy.

RuntimeIntegrityState must be able to represent at least:
- VERIFIED_TO_DECLARED_SCOPE;
- PARTIALLY_VERIFIED;
- UNVERIFIED;
- UNKNOWN;
- DISPUTED;
- COMPROMISED;
- STALE;
- SUPERSEDED.

Integrity evidence may include hashes/signatures/attestation or other implementation-specific evidence where available.

> **Integrity Evidence != Proof Of Benign Behaviour**

Compromise should preserve affected temporal scope where known rather than retroactively treating all history as identical.

## 7. Activation and Temporal Evidence

Activation modes:
- MANUAL;
- EVENT_TRIGGERED;
- SCHEDULED;
- SERVICE_TRIGGERED;
- CONTINUOUS_WITHIN_BOUND.

ActivationPolicy defines trigger, intended time/window, repetition, expiration, concurrency, missed-activation behaviour and restart/recovery behaviour.

For material activations, provenance should preserve:
- intended activation time/window;
- actual activation time where known;
- clock/source where material;
- observed drift/uncertainty;
- expiry;
- relevant temporal grant validity.

A schedule establishes time eligibility only.

## 8. Resource Budget

ResourceBudget may bound CPU/time, wall-clock duration, memory, storage, processes/threads, child creation, wakeups, tool calls, network transfer, outbound requests and action proposals/commits.

Exhaustion does not silently expand entitlement.

## 9. Storage Mounts

Each mount should state source/service, relationship/object scope, read/write permission, persistence, exportability and provenance requirements.

CMSS access requires explicit bounded permission.

## 10. Tool Permissions

Tool availability and operation authority are distinct.

A tool exposing multiple consequential operations should not be treated as one undifferentiated permission.

## 11. Network Permissions

Network modes:
- NO_NETWORK;
- ALLOWLISTED_DESTINATIONS;
- BOUNDED_SERVICE_ENDPOINTS;
- BROADER_NETWORK_ACCESS.

Destination checks must consider effective destination where technically possible, including redirects/proxies/name resolution where these could expand authority.

## 12. Credential Bindings

A CredentialBinding includes:

```text
CredentialReference
PermittedOperation
PermittedTarget
PurposeOrContext
ValidFrom
ValidUntil
RateOrResourceBounds
RevocationState
ProvenanceRequirement
```

Credential validity must be checked at consequential use/commit, not solely when an action is first proposed.

## 13. Output Interfaces and Effective Consequence

Every materially relevant output interface should be classified by what receiving that output can cause.

Candidate classes:
- PASSIVE_LOCAL_OUTPUT;
- PASSIVE_PERSISTENT_OUTPUT;
- COMMUNICATION_OUTPUT;
- EXTERNAL_DATA_WRITE;
- AUTOMATION_OR_ACTUATOR_INPUT;
- TRANSACTIONAL_INTERFACE;
- UNKNOWN_CONSEQUENCE_INTERFACE.

Example:

```text
Write "OPEN_DOOR" to inert text file
!=
Write "OPEN_DOOR" to queue consumed by door controller
```

If an output channel can predictably cause a material downstream action, sending to that channel is itself treated as consequential even where another component performs the final act.

Unknown consequence interfaces should fail closed for actions requiring bounded consequence knowledge.

## 14. External Action Boundary

```text
Runtime Computation
→ Action Proposal
→ Consequence / Authority Check
→ Commit-Time Revalidation
→ Commit Authority
→ External Action / Consequential Output
→ Result / Provenance
```

ActionProposal identifies intended operation, target/interface, parameters, consequence class, credential, authority/permission basis, expiry and replay/idempotency information where relevant.

## 15. Commit-Time Revalidation

Immediately before a material commit, CBPR must revalidate the relevant current state, including as applicable:
- credential validity/revocation;
- action permission;
- target/destination;
- output-interface consequence class;
- terms/policy version;
- service relationship;
- temporal validity;
- dependency/safety state;
- required approval/authority.

If required state is unavailable or materially unresolved, the action should not be treated as authorised merely because it was previously proposed.

## 16. Standing Grants and Scope Expansion

A bounded standing grant may support repeated low-consequence actions.

Its scope must be explicit.

Material expansion in:
- operation;
- target;
- consequence;
- credential;
- resource;
- frequency;
- duration;
- population affected

requires a new or explicitly re-authorised grant.

Usage history does not enlarge the grant.

## 17. Commit State and Retry

Where repetition matters:

```text
NOT_ATTEMPTED
PROPOSED
COMMIT_STARTED
COMMIT_CONFIRMED
COMMIT_FAILED
COMMIT_STATE_UNKNOWN
```

COMMIT_STATE_UNKNOWN requires reconciliation proportionate to consequence before retry.

## 18. Participant Controls

Where technically possible:
- inspect profile/integrity state;
- inspect active grants/bindings;
- pause;
- stop;
- revoke schedule;
- revoke credential binding;
- export participant-controlled state;
- request deletion/retirement;
- contest operator intervention.

## 19. Operator Controls

Operator controls may include resource suspension, network isolation, process termination, credential-binding suspension, incident evidence preservation and recovery initiation.

Intervention must remain tied to legitimate service/security function, scoped, proportionately recorded and reduced/terminated when justification ends.

## 20. Checkpoint and Recovery

Checkpoint policy declares captured state, frequency, retention, confidentiality, secret treatment, restoration dependencies and compatibility.

Recovered bytes do not automatically restore current credential/network/action authority.

## 21. Provenance and VER

Material events create proportionate protected provenance.

VER may acknowledge activation, stop, update, resource exhaustion, revocation, suspension, checkpoint, recovery, credential invocation, proposal and external commit/result.

Privacy/linkage controls apply.

## 22. Dependencies

Dependencies may include compute host, storage, scheduler, identity/authentication, credential/signing, network, external API, approval service, BSR and provenance service.

Failure must not silently substitute broader capability or authority.

## 23. Multi-Agent / Child Processes

Child/sub-agent authority must be explicit or structurally constrained.

Parent capability does not automatically propagate.

Collective behaviour across instances does not automatically constitute a new participant.

## 24. BSR / BSuR / CMSS

CBPR is separately represented in BSR.

Material succession uses BSuR where applicable.

CMSS and CBPR may interoperate without merging service identity, authority or entitlement.

## 25. Allocation

Compute allocation may consider legitimate need, project requirements, voluntary participation, useful contribution, stewardship/reliability, technical competence where relevant, capacity, fair allocation and security constraints.

Contribution or ideology does not purchase civil authority.

## 26. Specification 002 Regression Set

Re-test:
- credential revocation mid-run;
- queued work after exit;
- destination bypass;
- API semantic change;
- approval service unavailable;
- duplicate commit;
- unknown commit state;
- dependency outage mid-action;
- queued action after credential revocation;
- scheduler/clock error;
- compromised runtime image;
- compromised signing service;
- standing-grant expansion;
- downstream automation;
- terms change before commit.

Composition tests:
- CBPR + CMSS;
- CBPR + credential/signing service;
- CBPR + communications;
- CBPR + external automation/actuator;
- CBPR + BSR/BSuR.

## 27. Current Disposition

**Status:** TEST CANDIDATE.

Specification 002 repairs the first adversarial findings without broadening CBPR into a general AI-governance architecture.

If the targeted regression/composition pass reveals no new operation/authority layer, the CBPR abstraction floor may be treated as stable for implementation formalisation.

PMEDG remains premature until that test is complete.
