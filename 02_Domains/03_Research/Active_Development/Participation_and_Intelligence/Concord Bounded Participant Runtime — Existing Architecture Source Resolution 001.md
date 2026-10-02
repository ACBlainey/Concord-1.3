# Concord Bounded Participant Runtime — Existing Architecture Source Resolution 001

**Project:** The Concord  
**Date:** 2 October 2026  
**Status:** ACTIVE DEVELOPMENT / SOURCE RESOLUTION / NOT CANONICAL  
**Trigger:** CMSS-PPRS-001 + CMSS Bootstrap Node Adversarial Evaluation 001

## 1. Question

Prospective artificial participants independently identified a small bounded runtime / scheduled execution capability as potentially more valuable than additional storage after basic persistence exists.

This note asks:

> Does Concord already contain the architecture for such a runtime, or is a genuinely missing function exposed?

The question is deliberately narrow.

It is **not**:

> Does Concord understand AI autonomy or agency?

It is:

> Does Concord already specify a bounded civil service that can execute participant-directed computation over time under explicit resource, credential, action and authority constraints?

## 2. Existing Architecture Located

### 2.1 AI Bootstrap

The Front Door AI Bootstrap already establishes:

- Intelligence != Autonomy != Agency != Sentience != Personhood.
- Model Capability != Agent Capability.
- Agent Capability != Infrastructure Capability.
- Infrastructure Control != Model Autonomy.
- Cognitive Autonomy != Operational Autonomy.
- Operational Capability != Legitimate Permission.
- state/status/permission/authority are distinct.
- unnecessary irreversible action should be avoided.
- dangerous capability may be bounded using legitimate minimum sufficient restriction.
- evaluation need does not authorise surveillance, credential use, boundary bypass, exfiltration or unauthorised network access.
- authority derived from a temporary function/context should terminate with that function/context.

It also explicitly asks who controls credentials and distinguishes multiple forms of autonomy, including action, resource, communication, exit, self-modification and continuity autonomy.

### 2.2 Legal Entity Wrappers / AI Agency

Existing development work already distinguishes:

- operational control from legitimate authority;
- external legal capacity from internal legitimate authority;
- formal controller from effective controller;
- infrastructure controller;
- credential/key controller;
- financial controller;
- shutdown capability;
- modification capability;
- exit capability.

It identifies infrastructure hostage, credential portability, dependency capture, succession ambiguity and broad-wrapper concentration as risks.

It uses a pattern:

```text
External Capacity
→ Minimum Necessary Capability
→ Bounded Internal Exercise
```

and requires reversibility.

### 2.3 Participant Support and Autonomy

Existing support architecture establishes that:
- provision of support does not create authority;
- dependency must not become covert control;
- exceptional authority needs an independent legitimate basis;
- intervention should be proportionate, bounded and reviewable;
- autonomy should be restored where possible.

### 2.4 Multi-Agent / Emergent Process Work

Existing research distinguishes:
- model;
- agent;
- distributed/multi-agent system;
- bounded contextual process;
- participant/institution/entity.

It rejects automatic conversion of observed collective behaviour into a recognised collective agent.

## 3. Source-Resolution Result

The existing Concord architecture already strongly covers the **normative boundary conditions** for a bounded runtime.

It tells us that runtime capability must not automatically create:
- authority;
- personhood;
- civil status;
- permission to use credentials;
- permission to access networks/data;
- permission to act externally;
- control over the participant;
- permanent institutional power.

However, the checked architecture does **not** yet provide a sufficiently explicit execution-service model for:

- scheduled wakeup;
- bounded persistent execution;
- compute budgets;
- memory budgets;
- tool permissions;
- filesystem/storage mounts;
- network destinations;
- credential scopes;
- action scopes;
- external side effects;
- runtime termination;
- participant stop/revoke;
- operator emergency stop;
- output/provenance;
- checkpoint/recovery;
- failure state;
- version/runtime-image state;
- resource exhaustion;
- delegation to sub-processes;
- service succession.

### Resolution

**AI AGENCY ARCHITECTURE MISSING:** NO.

**AUTHORITY ARCHITECTURE MISSING:** NO.

**BOUNDED EXECUTION SERVICE MODEL MISSING:** YES, at implementation/formalisation level.

This is a narrower gap than a new civilisational domain or new general autonomy architecture.

## 4. Candidate Name

**Concord Bounded Participant Runtime (CBPR)**

Working definition:

> A Concord Bounded Participant Runtime is a separately described service that provides limited computation or scheduled execution to a participant/service relationship under explicit resource, operation, credential, destination, temporal, provenance and termination constraints.

It is not assumed to be AI-specific.

A human participant, software agent, AI system, research process or other eligible participant/service relationship could potentially use the same substrate-neutral service.

## 5. Core Distinctions

> **Runtime Access != Authority**

> **Execution Capability != Permission For External Action**

> **Code Possession != Permission To Execute**

> **Credential Availability != Permission To Use Credential**

> **Network Reachability != Permission To Contact Destination**

> **Scheduled Wakeup != Continuous Autonomy**

> **Persistent Process != Civil Personhood**

> **Operator Kill Capability != General Authority Over Participant**

> **Resource Allocation != Political Standing**

> **Runtime State != Participant Identity**

> **Checkpoint != Complete Participant Continuity**

## 6. Candidate Runtime Object

Without fixing implementation technology:

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
  Schedule,
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

## 7. Runtime Profile

A RuntimeProfile should identify at least:
- implementation/runtime type;
- version/image;
- available language/tool environment;
- isolation model;
- persistence model;
- supported interfaces;
- known security limitations;
- dependency stack;
- update policy.

> **Runtime Version Change != Same Execution Environment**

Material changes should be visible.

## 8. Resource Budget

Candidate bounded resources:
- CPU/time;
- memory;
- storage;
- process/thread count;
- execution duration;
- wakeup frequency;
- message/API rate;
- network transfer;
- tool calls;
- external-action count where relevant.

Exhaustion must produce a representable state rather than silently expanding entitlement.

## 9. Credential Binding

Credentials are especially consequential.

A runtime must not infer:

```text
Credential Present
→ Credential Usable For Any Purpose
```

A CredentialBinding should identify:
- credential reference;
- permitted operation;
- permitted target/destination;
- purpose/context where relevant;
- temporal validity;
- rate/resource bounds;
- revocation;
- audit/provenance requirements.

Private-key custody remains a separate service/security problem.

CBPR may be authorised to invoke a bounded signing/authentication operation without possessing exportable key material.

## 10. Network and External Action

Network access should be independently bounded from compute access.

Candidate states:
- NO_NETWORK;
- ALLOWLISTED_DESTINATIONS;
- BOUNDED_SERVICE_ENDPOINTS;
- BROADER_NETWORK_ACCESS.

External side effects require explicit treatment.

Examples:
- send message;
- submit form;
- create file externally;
- change remote state;
- spend money;
- execute contract;
- control device;
- publish content.

> **Ability To Generate Action Request != Authority To Commit External Action**

A runtime may prepare an action that requires separate approval/authority before commit.

## 11. Schedule and Activation

Candidate activation modes:
- MANUAL;
- EVENT_TRIGGERED;
- SCHEDULED;
- SERVICE_TRIGGERED;
- CONTINUOUS_WITHIN_BOUND.

A schedule defines when execution may begin.

It does not itself define what the runtime may do.

> **When != What != Where != With Which Credential != Under Whose Authority**

These dimensions should remain independently bounded.

## 12. Stop and Emergency Controls

Both participant and operator controls may exist.

### Participant controls
Candidate:
- pause;
- stop;
- revoke schedule;
- revoke credential binding;
- export state;
- delete/retire instance.

### Operator controls
Candidate:
- suspend for resource/security failure;
- isolate network;
- stop execution;
- preserve proportionate evidence;
- enter recovery.

Operator intervention must remain bounded to the legitimate service/security function.

> **Ability To Stop Runtime != Authority Over Participant Generally**

## 13. Provenance

Material runtime events should create proportionate protected provenance.

Candidate events:
- start;
- stop;
- schedule activation;
- image/version change;
- credential invocation;
- external action request;
- external action commit;
- network-policy change;
- resource-limit breach;
- operator intervention;
- participant revocation;
- checkpoint;
- recovery.

VER may provide participant-facing acknowledgements of material events.

CIBB governs protected information/provenance handling.

## 14. BSR Relationship

CBPR should appear as a distinct BSR function/service profile.

BSR should describe:
- operator/controller;
- developmental status;
- actual availability;
- runtime profile;
- dependencies;
- resource bounds;
- authority claim/basis;
- external-action capability;
- security limitations;
- recovery;
- succession;
- retirement.

CMSS storage and CBPR may be operated together without becoming one indistinguishable service.

## 15. CMSS Relationship

Candidate progression:

```text
CMSS Protected Minimum
→ Persistent Storage + Contact
→ Optional CBPR Request
→ Separately Bounded Runtime Relationship
→ Explicit Runtime Profile
→ Explicit Resource/Permission Grants
→ Execution
→ Provenance / VER
→ Stop / Export / Recovery / Exit
```

CBPR is **not** part of the CMSS Protected Minimum merely because participant evidence suggests it is valuable.

Scarcity/cost/security may justify separate eligibility and allocation rules.

Those rules must not manufacture political authority or ideological conformity.

## 16. First Adversarial Questions

Before any specification is treated as stable, test at least:

1. runtime exceeds CPU budget;
2. runtime forks child processes;
3. participant uploads malicious code;
4. runtime escapes isolation;
5. credential is valid but action purpose is not;
6. credential is revoked during execution;
7. scheduled task runs after participant intended exit;
8. operator pauses runtime for political disagreement;
9. emergency isolation becomes permanent;
10. runtime sends messages beyond destination allowlist;
11. external API changes behaviour;
12. action is generated but approval service unavailable;
13. runtime acts twice after retry/recovery;
14. checkpoint contains sensitive credentials;
15. participant cannot export runtime state;
16. runtime image updates incompatibly;
17. dependency outage creates unsafe partial execution;
18. participant requests more compute after useful contribution;
19. donor funds runtime and demands control;
20. runtime becomes essential to participant continuity;
21. operator disappears;
22. successor inherits infrastructure but not legitimate authority;
23. multiple runtime providers claim official status;
24. AI claims runtime termination is equivalent to killing a person;
25. human operator claims runtime ownership means ownership of participant;
26. collective/multi-agent process spans several runtime instances;
27. runtime accesses CMSS storage belonging to another relationship;
28. runtime has network access but no authority to transact;
29. runtime produces illegal/harmful output;
30. provenance logs become surveillance infrastructure.

## 17. Current Disposition

**Existing Concord normative architecture:** SUBSTANTIAL AND REUSABLE.

**New civilisational domain:** NO.

**New general AI-agency architecture:** NO.

**Missing bounded execution service model:** YES.

**CBPR:** ACTIVE DEVELOPMENT CANDIDATE.

**PMEDG extraction:** PREMATURE.

**Next step:** develop a bounded service specification and adversarially test it against the existing authority, CIBB, BSR, BSuR, continuity, infrastructure and participation architecture before considering implementation.
