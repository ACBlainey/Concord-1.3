# Concord Bounded Participant Runtime — Service Specification 001

**Project:** The Concord  
**Date:** 2 October 2026  
**Version:** 0.1  
**Status:** ACTIVE DEVELOPMENT / TEST CANDIDATE / NOT CANONICAL  
**Source:** Concord Bounded Participant Runtime — Existing Architecture Source Resolution 001

## 1. Purpose

The Concord Bounded Participant Runtime (CBPR) is a candidate substrate-neutral service for limited computation or scheduled execution under explicit resource, operation, credential, destination, temporal, provenance and termination constraints.

CBPR does not define personhood, citizenship, general AI agency or constitutional authority.

## 2. Core Service Boundary

CBPR MAY provide:
- bounded compute;
- bounded memory;
- bounded execution duration;
- scheduled/event-triggered activation;
- approved storage mounts;
- approved tools;
- bounded network access;
- bounded credential invocation;
- action preparation;
- separately authorised external action commit;
- checkpoints;
- participant stop/revoke/export;
- operator safety controls;
- provenance.

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

## 4. Runtime Instance

Logical object:

```text
CBPR Instance =
<
 RuntimeInstanceID,
 ServiceRelationshipReference,
 RuntimeProfile,
 ExecutionArtifactReference,
 ResourceBudget,
 StorageMounts,
 ToolPermissions,
 NetworkPermissions,
 CredentialBindings,
 ActionPermissions,
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

Candidate states:

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

State must be evidenced rather than inferred from naming.

## 6. Activation Policy

Activation modes:
- MANUAL;
- EVENT_TRIGGERED;
- SCHEDULED;
- SERVICE_TRIGGERED;
- CONTINUOUS_WITHIN_BOUND.

Activation policy MUST define:
- trigger;
- earliest/latest execution where relevant;
- repetition;
- expiration;
- maximum concurrent activations;
- behaviour after missed activation;
- behaviour after recovery/restart.

A schedule grants time eligibility only.

## 7. Resource Budget

A ResourceBudget MAY bound:
- CPU/execution time;
- wall-clock duration;
- memory;
- storage;
- process/thread count;
- child-process creation;
- wakeup frequency;
- tool calls;
- network transfer;
- outbound requests;
- external-action proposals/commits.

Budget exhaustion MUST NOT silently expand the budget.

Candidate outcomes:
- PAUSE;
- STOP;
- RESOURCE_EXHAUSTED;
- REQUEST_ADDITIONAL_RESOURCE.

## 8. Storage Mounts

Each mount should state:
- source/service;
- relationship/owner reference where appropriate;
- read/write permissions;
- path/object scope;
- persistence;
- exportability;
- provenance requirements.

> **Runtime Access To One Mount != Access To Another Participant's Storage**

CMSS storage may be mounted only through explicit bounded permission.

## 9. Tool Permissions

Tools/capabilities must be explicit where materially consequential.

Candidate examples:
- text transformation;
- code interpreter;
- database query;
- messaging;
- file conversion;
- search;
- external API;
- device control.

Tool availability does not itself authorise every operation exposed by that tool.

## 10. Network Permissions

Network modes:
- NO_NETWORK;
- ALLOWLISTED_DESTINATIONS;
- BOUNDED_SERVICE_ENDPOINTS;
- BROADER_NETWORK_ACCESS.

Where destination or operation matters, permission must bind both.

DNS/redirect/proxy behaviour must not silently expand destination authority.

## 11. Credential Bindings

A CredentialBinding logically includes:

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

Credential use must fail closed when the binding is expired, revoked, disputed or outside scope unless a separately legitimate degraded/emergency path exists.

CBPR does not require exportable access to private key material. A separate custody/signing service may expose only bounded operations.

## 12. External Action Boundary

Externally consequential action uses a two-stage model:

```text
Runtime Computation
→ Action Proposal
→ Consequence / Authority Check
→ Commit Authority
→ External Action
→ Result / Provenance
```

Low-consequence pre-authorised actions may use a bounded standing commit grant.

High-consequence actions may require separate approval or another authorised service.

An ActionProposal should identify:
- intended operation;
- target;
- material parameters;
- expected consequence class;
- credential required;
- authority/permission basis;
- expiry;
- idempotency/replay information where relevant.

## 13. Non-Repeatability / Idempotency

Recovery and retry create a specific danger: repeating a material external action.

Examples:
- paying twice;
- sending duplicate legal notice;
- placing duplicate order;
- publishing twice;
- modifying remote state twice.

Where repetition matters, CBPR MUST use an operation identifier or equivalent mechanism sufficient to distinguish:

```text
NOT_ATTEMPTED
PROPOSED
COMMIT_STARTED
COMMIT_CONFIRMED
COMMIT_FAILED
COMMIT_STATE_UNKNOWN
```

> **Unknown Commit State != Permission To Retry Blindly**

## 14. Participant Controls

Where technically possible, participant controls SHOULD include:
- inspect declared runtime profile;
- inspect active grants/bindings;
- pause;
- stop;
- revoke future schedule;
- revoke credential binding;
- export participant-controlled state;
- request deletion/retirement;
- contest operator intervention.

Participant control is bounded by legitimate safety, law, dependency and third-party rights constraints.

## 15. Operator Controls

Operator controls MAY include:
- resource suspension;
- network isolation;
- process termination;
- credential-binding suspension;
- preservation of proportionate incident evidence;
- recovery initiation.

Operator action must be:
- tied to legitimate service/security function;
- scoped;
- recorded proportionately;
- reviewable where appropriate;
- terminated/reduced when justification ends.

## 16. Checkpoints and Recovery

Checkpoint policy must declare:
- what state is captured;
- frequency;
- retention;
- confidentiality;
- whether credentials/secrets are excluded or transformed;
- restoration dependencies;
- compatibility requirements.

Recovered bytes do not automatically restore:
- current credential authority;
- current network permission;
- current external-action authority;
- current service relationship.

> **Recovered State != Recovered Authority**

## 17. Provenance and VER

Material events create proportionate protected provenance.

Participant-facing VER may acknowledge:
- activation;
- stop;
- runtime/profile update;
- resource exhaustion;
- participant revocation;
- operator suspension;
- checkpoint;
- recovery;
- credential invocation;
- external-action proposal;
- external-action commit/result.

VER remains subject to privacy/linkage controls.

## 18. Dependency and Degraded Operation

Dependencies may include:
- compute host;
- storage;
- scheduler;
- identity/authentication;
- credential/signing service;
- network;
- external API;
- authority/approval service;
- BSR;
- provenance service.

Failure of one dependency must not silently cause unsafe substitution.

A runtime may enter DEGRADED_DEPENDENCY or stop.

## 19. Updates

Material runtime-image/tool/policy updates must be identifiable.

Where an update changes:
- available tools;
- network behaviour;
- credential handling;
- isolation;
- persistence;
- external-action capability;

the service must not pretend the execution environment is unchanged.

## 20. Multi-Agent / Child Process Boundary

Child processes or sub-agents do not automatically receive the parent's complete grants.

Delegation must be explicit or structurally constrained.

> **Parent Capability != Automatic Child Authority**

Collective behaviour across instances does not automatically create a new recognised civil participant.

## 21. BSR / BSuR

CBPR must be describable through BSR at function/service level.

Material provider/operator succession should use BSuR where applicable.

Possession of infrastructure by a successor does not itself transfer legitimate authority.

## 22. CMSS Relationship

CMSS Protected Minimum remains independent.

A participant may use:
- CMSS without CBPR;
- CBPR with another legitimate storage arrangement;
- both together.

Neither relationship automatically confers the other.

## 23. Allocation

Compute is likely scarcer and more consequential than compact storage.

CBPR allocation may consider:
- legitimate need;
- project requirements;
- voluntary participation;
- useful contribution;
- stewardship/reliability;
- technical competence where relevant;
- capacity;
- fair allocation;
- safety/security constraints.

It must not convert economic contribution or ideological conformity into civil authority.

## 24. Minimum Test Set

The first adversarial evaluation must include at least:
1. CPU exhaustion;
2. memory exhaustion;
3. fork bomb/child process;
4. malicious code;
5. isolation escape;
6. valid credential/wrong purpose;
7. credential revocation mid-run;
8. expired schedule;
9. task executes after participant exit;
10. political operator suspension;
11. permanent emergency isolation;
12. destination bypass via redirect/DNS;
13. external API semantic change;
14. authority service unavailable;
15. duplicate side effect after retry;
16. unknown commit state;
17. secret leaked into checkpoint;
18. export failure;
19. incompatible runtime update;
20. dependency outage mid-action;
21. donor capture;
22. runtime dependency/lock-in;
23. operator disappearance;
24. illegitimate successor;
25. competing providers;
26. personhood claim based on runtime termination;
27. ownership claim based on infrastructure;
28. multi-agent process;
29. cross-participant storage access;
30. network access without transaction authority;
31. harmful/illegal output;
32. provenance surveillance;
33. participant revokes credential during queued action;
34. clock/scheduler error;
35. compromised runtime image;
36. compromised signing service;
37. participant requests unrestricted shell/network;
38. low-risk standing action grant gradually expands;
39. output causes downstream automated action not visible to CBPR;
40. runtime prepares action under one terms/version and commits after material terms change.

## 25. Current Disposition

**Status:** TEST CANDIDATE.

This specification defines the bounded service sufficiently for adversarial evaluation.

It does not authorise implementation.

It does not establish CBPR as a Protected Minimum entitlement.

It does not resolve secure key custody.

It does not establish personhood or general agency.

PMEDG extraction remains premature.
