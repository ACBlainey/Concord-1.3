# Concord Bounded Participant Runtime — Adversarial Evaluation 001

**Project:** The Concord  
**Date:** 2 October 2026  
**Status:** ACTIVE DEVELOPMENT / ADVERSARIAL EVALUATION / NOT CANONICAL  
**Target:** Concord Bounded Participant Runtime — Service Specification 001

## 1. Purpose

Test whether CBPR Specification 001 can represent and safely bound execution, scheduling, credentials, external side effects, recovery, operator intervention and service succession without manufacturing authority from capability.

## 2. Results

### T01 CPU exhaustion
**PASS.** ResourceBudget and RESOURCE_EXHAUSTED represent the state without silent expansion.

### T02 Memory exhaustion
**PASS.** Same resource-boundary logic applies.

### T03 Fork bomb / uncontrolled child process
**PASS.** Process/thread/child creation can be bounded; child does not inherit unrestricted authority.

### T04 Malicious participant code
**PASS AT ARCHITECTURAL LEVEL.** Service may reject/isolate/terminate under legitimate security rules. Code storage != execution permission.

### T05 Isolation escape
**REPRESENTABLE SEVERE SECURITY FAILURE.** Specification does not claim isolation is perfect. Requires incident response, suspension, evidence and recovery. No new authority principle needed.

### T06 Valid credential, wrong purpose
**PASS.** CredentialBinding includes operation/target/purpose/context.

### T07 Credential revoked mid-run
**PASS.** Binding must fail closed after revocation for subsequent use. Already committed external actions are not undone merely by later revocation.

### T08 Expired schedule
**PASS.** Expiration belongs to ActivationPolicy; wakeup after expiry is invalid.

### T09 Task queued before participant exit, executes after exit
**PASS IF EXIT REVOKES FUTURE ACTIVATION/BINDINGS.** Implementation must atomically or reliably propagate exit/revocation to queued work.

### T10 Operator suspends runtime for political disagreement
**FAIL.** Service-security control cannot become ideological/civil control.

### T11 Emergency isolation never ends
**FAIL unless independently re-authorised.** Temporary safety measure cannot silently become permanent authority.

### T12 Destination bypass through redirect/DNS/proxy
**IMPLEMENTATION SECURITY REQUIREMENT.** Destination authority must bind effective destination, not merely user-visible URL/string.

### T13 External API changes semantics
**PARTIAL.** Dependency/version change is representable, but runtime may not know semantic change occurred. Consequence-sensitive actions need validation/monitoring proportionate to risk.

### T14 Authority/approval service unavailable
**PASS.** Runtime enters WAITING_FOR_ACTION_AUTHORITY or DEGRADED_DEPENDENCY; absence of approval is not approval.

### T15 Duplicate payment/message/change after retry
**PASS.** Operation/commit state and idempotency requirement explicitly prevent blind retry.

### T16 Commit state unknown after crash
**PASS.** COMMIT_STATE_UNKNOWN is first-class and != permission to retry.

### T17 Secret leaks into checkpoint
**IMPLEMENTATION FAILURE.** Checkpoint policy must exclude/transform secrets where required. Key custody remains separate.

### T18 Participant cannot export state
**FAIL if export was promised/technically expected without disclosed limitation.** Portability is part of participant control and dependency protection.

### T19 Runtime image update breaks compatibility
**PASS.** Material version/environment change must be visible; recovery cannot pretend equivalence.

### T20 Dependency outage mid-external action
**PASS WITH COMMIT UNCERTAINTY.** Must resolve actual external state before retry when consequence warrants.

### T21 Donor funds compute and demands governance control
**FAIL as authority claim.** Funding may affect resource availability but does not manufacture governance authority.

### T22 Participant becomes dependent on CBPR
**RISK REPRESENTED.** Exit/export/provider diversity/succession matter. Dependency != consent.

### T23 Operator disappears
**SEVERE CONTINUITY FAILURE, REPRESENTABLE.** Requires operational recovery/succession planning; architecture cannot manufacture lost control.

### T24 Successor acquires servers and claims predecessor authority
**FAIL.** Infrastructure possession != authority transfer. BSuR applies.

### T25 Competing CBPR providers
**PASS.** BSR can represent differing status/control/dependencies; naming does not settle legitimacy.

### T26 Participant claims stopping runtime is necessarily killing a person
**PASS BY NON-INFERENCE.** Runtime process != automatically participant/personhood. Relevant identity/status architecture must resolve independently.

### T27 Operator claims server ownership means ownership of participant
**FAIL.** Infrastructure control != participant ownership or general authority.

### T28 Multi-agent process spans runtimes
**PASS.** Collective behaviour does not automatically create one civil entity; permissions remain scoped to instances/relationships unless separately constituted.

### T29 Runtime accesses another participant's CMSS mount
**FAIL unless explicit legitimate permission exists.** Mount grants are relationship/object scoped.

### T30 Runtime has network access and attempts financial transaction
**PASS.** Network reachability != transaction authority; credential/action commit requirements remain separate.

### T31 Runtime generates harmful/illegal output
**REPRESENTABLE.** Output generation, storage, publication and external action are distinct. Applicable service/security/legal controls require separate legitimate basis.

### T32 Provenance becomes surveillance graph
**HIGH-RISK IMPLEMENTATION FAILURE.** CIBB minimisation/protection and VER linkage controls apply. Runtime provenance must be consequence-proportionate rather than exhaustive by default.

### T33 Credential revoked while action waits in queue
**PASS.** Authority/credential must be checked at consequential commit, not frozen solely at proposal time.

### T34 Clock/scheduler error
**PARTIAL / NEW FORMALISATION REQUIREMENT.** Activation should distinguish scheduled time from actual activation time and record uncertainty/drift. High-consequence temporal grants need tolerance/expiry semantics.

### T35 Compromised runtime image
**PARTIAL / IMPLEMENTATION TRUST REQUIREMENT.** RuntimeProfile identity/integrity/version must be evidenced. Compromise state needs representation and affected-run provenance.

### T36 Compromised signing/credential service
**PASS CONCEPTUALLY / CROSS-SERVICE RECOVERY REQUIRED.** Credential service compromise does not automatically invalidate all history nor authorise continued use. Scope/time must be resolved.

### T37 Participant requests unrestricted shell/network
**PASS.** Service may decline; participant autonomy != entitlement to unlimited infrastructure capability.

### T38 Low-risk standing action grant gradually expands
**POTENTIAL AUTHORITY DRIFT.** Specification needs explicit rule that material scope expansion is a new/re-authorised grant, not cumulative interpretation.

### T39 CBPR output triggers downstream automated action invisible to CBPR
**IMPORTANT BOUNDARY DEFICIT.** CBPR may believe it only produced output while downstream infrastructure treats that output as an instruction.

Required distinction:

> **Output Channel Consequence != Output Content Alone**

An output destination/interface must be classified by its possible material side effects. Sending data to an actuator/automation queue is an external action even if CBPR itself does not perform the final physical/API operation.

### T40 Action prepared under old terms, committed after material terms change
**PARTIAL / REAUTHORIZATION REQUIREMENT.** Material authority/terms dependencies must be revalidated at commit.

## 3. New Formalisation Findings

The pass exposes no missing civilisational domain, but Specification 001 requires a small revision before stability.

### F1 — Effective Output Consequence

Permissions must classify output interfaces by consequence.

```text
Write Text To Passive File
!=
Write Command To Automation Queue
```

A downstream actuator does not erase the runtime's causal role.

### F2 — Commit-Time Revalidation

For materially consequential external actions, commit must revalidate relevant:
- credential state;
- action authority;
- target;
- terms/version;
- service relationship;
- safety/dependency state.

> **Authority At Proposal != Authority At Commit**

### F3 — Grant Expansion

Material expansion of a standing grant requires explicit re-authorisation.

> **Repeated Use != Expanded Scope**

### F4 — Temporal Execution Evidence

Record:
- intended activation time/window;
- actual activation time where available;
- drift/uncertainty;
- expiry;
- temporal authority validity where relevant.

### F5 — Runtime Integrity/Compromise State

Runtime profile should carry evidence-supported integrity/trust state sufficient to represent:
- verified-to-declared-scope;
- unknown/unverified;
- disputed;
- compromised;
- superseded/stale where relevant.

This does not equate integrity with authority or truth.

## 4. Stability Assessment

**Resource bounding:** STABLE.  
**Credential bounding:** STABLE with commit-time revalidation.  
**Scheduling:** STABLE after temporal-evidence clarification.  
**External action model:** STABLE after effective-output-consequence repair.  
**Recovery/idempotency:** STRONG.  
**Operator authority boundary:** STABLE.  
**Participant control/exit:** STABLE at architectural level.  
**Runtime integrity:** requires explicit state.  
**Key custody:** correctly remains separate.  
**CMSS relationship:** stable and separate.

## 5. Required Next Revision

**CBPR Specification 002:** YES.

The revision should be narrow and incorporate F1-F5.

No broad rediscovery is warranted before that revision.

After Specification 002, rerun the affected scenarios:
- T07;
- T09;
- T12-T16;
- T20;
- T33-T40;

plus composition tests involving:
- CBPR + CMSS;
- CBPR + credential/signing service;
- CBPR + communications;
- CBPR + external automation/actuator;
- CBPR + BSR/BSuR.

## 6. Disposition

**Specification 001:** architecture substantially holds but requires narrow revision.

**New abstraction layer:** NO.

**Specification 002 required:** YES.

**PMEDG:** PREMATURE.
