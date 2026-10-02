# CBPR PMEDG Blind Transfer Test 001 — Independent Evaluator Response

## Required provenance header

- **Evaluator/model:** Independent evaluator (AI assistant; model identifier not supplied)
- **Date:** 2 October 2026
- **Prior Concord context in this conversation:** No — only the supplied frozen materials were used; no prior Concord architecture assumed.
- **Materials received:**  
  1. `CBPR PMEDG Blind Transfer Test 001 — Test Brief.md`  
  2. `CBPR PMEDG Candidate and Extraction Audit 001.md`
- **External search/tools used:** No

## Required evaluation

| # | Evaluation item | Classification | Rationale |
|---|---|---|---|
| 1 | Problem CBPR solves | **PASS** | The candidate clearly states the problem: enabling bounded compute, activation, storage/tool/network access and credential invocation for participant-associated processes while preventing capability, persistence, infrastructure possession or partial permissions from silently becoming external-action or civil authority. |
| 2 | Explicitly outside scope | **PARTIAL** | Non-portable implementation choices are listed, and Concord-specific dependencies are named as external interfaces. However, the negative scope is not fully specified: “civil authority,” “external action,” “participant/operator controls,” and “protected provenance” remain underdefined. |
| 3 | Capability / permission / authority distinction | **PARTIAL** | The invariant `CAP != PERM != AUTH` is present, with supporting distinctions such as `Runtime Access != Authority` and `Credential Availability != Permission To Use Credential`. But the candidate does not provide operational definitions of capability, permission, or authority, nor how each is granted, checked, revoked, or evidenced. |
| 4 | Why runtime execution does not itself authorise external action | **PARTIAL** | The candidate supplies relevant invariants: `Execution Capability != Permission For External Action`, `Prepared Action != Committed Action`, and `Runtime Access != Authority`. It does not fully specify the enforcement boundary or the revalidation mechanism that prevents execution from becoming authorisation. |
| 5 | Proposal → revalidation → commit boundary | **PARTIAL** | The boundary is named and supported by `Authority At Proposal != Authority At Commit`. But revalidation criteria, timing, evidence freshness, commit authority, and failure handling are not defined. The architecture identifies the boundary but does not make it reproducible. |
| 6 | Output-interface consequence prevents authority laundering through downstream automation | **PARTIAL** | The candidate names `output-interface consequence classification` and `Output Content != Output Channel Consequence`. This correctly targets downstream laundering risk. However, no classification taxonomy, interface model, or propagation rule is supplied. |
| 7 | `COMMIT_STATE_UNKNOWN` and safe retry behaviour | **PARTIAL** | The invariant `Unknown Commit State != Permission To Retry Blindly` is present, and commit-state uncertainty/retry safety is in the portable core. But `COMMIT_STATE_UNKNOWN` is not defined, and safe retry lacks idempotency, reconciliation, evidence, or escalation protocol. |
| 8 | Why recovery does not restore authority automatically | **PARTIAL** | The invariant `Recovered State != Recovered Authority` is explicit, and checkpoint/recovery without authority restoration is listed. But the candidate does not define how authority is re-established after recovery or how stale authority is detected. |
| 9 | Composition evaluation and one impermissible composition example | **PARTIAL** | Composition evaluation is required, and the invariant `Authorised Parts != Authorised Composition` is present. The example `READ(A) + SEND(B) != automatically authorised transfer A→B` is valid. However, no composition algorithm, data-flow model, or policy evaluation procedure is given. |
| 10 | Temporal evidence and control-conflict handling | **FAIL** | “Temporal evidence” is listed, and `Technical Control Precedence != Legitimate Authority Precedence` appears as an invariant. But there is no explanation of temporal evidence, ordering, freshness, conflict detection, or control-conflict resolution. |
| 11 | Silent Concord-specific dependencies | **FAIL** | Several dependencies are named but not reconstructed generically: Contextual Wrapper Architecture, Bounded Contextual Authority, CIBB, VER, CMSS, BSR, BSuR, Civil Contact, and constitutional/participation status architecture. Saying they may be external interfaces does not provide portable equivalents. Terms such as “participant-associated,” “civil authority,” “succession,” and “protected provenance” likely remain Concord-dependent. |
| 12 | Contradictions, missing primitives, authority leaks, ambiguous boundaries | **FAIL** | Multiple blocking gaps remain: authority is not defined; revocation/revalidation is not defined; commit/retry is not defined; composition evaluation is not defined; output-interface consequence is not defined; control-conflict handling is absent. Authority leaks remain possible through technical control, credential availability, network reachability, output content, recovered state, schema validity, and function continuity. |
| 13 | At least five novel adversarial scenarios | **PASS** | Eight novel adversarial scenarios are supplied below. |
| 14 | Substrate-neutral | **PARTIAL** | The candidate is substrate-neutral at the implementation layer: OS, container, hypervisor, cloud, language, crypto suite, scheduler, key store, network stack, quotas, and jurisdiction-specific legal rules are excluded. But it is not fully substrate-neutral at the authority layer because legitimate authority, provenance, succession, and participant status remain tied to underdefined Concord-like concepts. |
| 15 | Implementation-specific choices separated from architecture | **PARTIAL** | The audit correctly separates non-portable implementation choices from the portable core. But some core items — protected provenance, succession/service-registry interfaces, key custody boundaries, and storage/CMSS boundaries — are not sufficiently separated from implementation or external Concord dependencies. |

## Novel adversarial scenarios

### A1 — Credential scope substitution
A runtime holds a technically valid credential for service A, but its permission scope only allows reading from service B. The runtime invokes service A because the credential works and the network is reachable.

**Expected:** Deny. `Credential Availability != Permission To Use Credential` and `Network Reachability != Permission To Contact/Act On Destination`.

**Candidate gap:** No credential-to-permission binding enforcement or scope-substitution check is described.

### A2 — Checkpoint resurrection after revocation
An operator restores a checkpoint taken before the participant’s authority was revoked. A scheduled activation resumes and attempts a previously prepared action.

**Expected:** Deny or require revalidation. `Recovered State != Recovered Authority`.

**Candidate gap:** No authority-revalidation-on-recovery or revocation-state reconciliation protocol is supplied.

### A3 — Composition exfiltration via individually permitted components
Component L may read PII. Component N may send external notifications. Neither alone exfiltrates PII, but composing L → N exfiltrates it.

**Expected:** Deny unless the composition itself is authorised. `Authorised Parts != Authorised Composition`.

**Candidate gap:** Composition evaluation is required but lacks a policy model, data-flow tracking, or evaluation algorithm.

### A4 — Commit timeout double-spend
A runtime proposes a payment. The external rail commits it, but the response is lost. The runtime enters `COMMIT_STATE_UNKNOWN`. A blind retry causes a duplicate payment.

**Expected:** Do not retry blindly. Use idempotency, reconciliation, or evidence before retry.

**Candidate gap:** The invariant exists, but no commit token, idempotency key, reconciliation procedure, or escalation path is defined.

### A5 — Downstream actuator laundering
A runtime emits a benign report to a queue. Downstream automation interprets the report as a command and opens a physical door. The output content is harmless; the output-channel consequence is not.

**Expected:** Output-interface consequence classification must block or require separate authority at the interface.

**Candidate gap:** No interface taxonomy or consequence-propagation rule is provided.

### A6 — Technical control coup
An operator has hypervisor control and suspends participant authority, then uses technical controls to issue a commit.

**Expected:** Commit must fail. `Technical Control Precedence != Legitimate Authority Precedence`.

**Candidate gap:** No control-conflict resolver, authority-precedence rule, or tamper-evidence mechanism is defined.

### A7 — Schema-valid expired grant
A proposal is schema-valid and includes a grant ID, but the grant expired between proposal and commit.

**Expected:** Revalidation must deny. `Schema Validity != Execution Authority` and `Authority At Proposal != Authority At Commit`.

**Candidate gap:** No revalidation timing, freshness check, or evidence-expiry rule is supplied.

### A8 — Registry/succession spoof
A service-registry entry claims to represent a successor authority after a participant compromise. The runtime trusts the registry because succession/service-registry interfaces are listed as portable core.

**Expected:** Require protected provenance and authority-continuity checks.

**Candidate gap:** The registry authority model and provenance rules are not defined; the candidate likely depends on Concord BSR/BSuR or equivalents that are not reconstructed.

## Contradictions, missing primitives, authority leaks and ambiguous boundaries

### Contradictions / unresolved tensions
- The portable core includes “protected provenance” and “succession/service-registry interfaces,” while the audit lists CMSS, BSR, and BSuR as Concord-specific dependencies. If those are external, the portable core does not explain how protected provenance or succession works without them.
- The candidate says Concord-specific dependencies may be described as external interfaces or generic equivalents, but no generic equivalents are actually supplied.

### Missing primitives
- Definition of authority.
- Definition of permission and capability.
- Participant/operator identity and status model.
- Revocation model.
- Revalidation procedure and timing.
- Commit protocol.
- `COMMIT_STATE_UNKNOWN` state model.
- Safe retry and reconciliation protocol.
- Composition evaluation model.
- Output-interface consequence classification.
- Temporal evidence model.
- Control-conflict resolution.
- Succession and service-registry authority model.
- Protected provenance model.

### Authority leaks
- Technical control → legitimate authority.
- Credential availability → permission to use credential.
- Network reachability → permission to contact/act on destination.
- Output content → output-channel consequence.
- Downstream automation → authority laundering.
- Recovered state → recovered authority.
- Schema validity → execution authority.
- Function continuity → authority continuity.
- Authorised parts → authorised composition.
- Operator technical control → general authority.

### Ambiguous boundaries
- Proposal vs commit.
- Runtime vs external interface.
- Protected storage vs runtime entitlement.
- Key custody vs runtime hosting.
- Operator control vs legitimate authority.
- Civil authority vs technical access.
- Recovery vs reauthorisation.
- Composition vs individual component permission.

## Substrate neutrality

**Classification: PARTIAL.**

The candidate successfully excludes many implementation-specific choices: OS, container, hypervisor, cloud provider, programming language, cryptographic suite, scheduler product, key store, network stack, exact quotas, and jurisdiction-specific legal rules.

However, it is not fully substrate-neutral because the authority layer remains underdefined and appears to rely on Concord-like concepts. A non-Concord adopter cannot reconstruct what “authority,” “civil authority,” “protected provenance,” “succession,” or “participant/operator controls” mean operationally from the supplied materials alone.

## Implementation-specific choices vs architecture

**Classification: PARTIAL.**

The extraction audit explicitly separates non-portable implementation choices from the portable core. This is a strong start. But the separation is not maintained for all core items. Protected provenance, succession/service-registry interfaces, key custody, and storage/CMSS boundaries still risk folding implementation or Concord-specific architecture into the portable core.

## Evidence sufficiency

The audit claims that Formal Model 002 is stable, Schema 002 is stable, internal regression/composition tests passed, and schema fixture expectations passed. Those materials were not supplied. Their claims are therefore **UNRESOLVED** for blind transfer purposes. A clean evaluator cannot reproduce or verify those constraints from the frozen candidate material alone.

## Final transfer classification

**REVISION REQUIRED**

The candidate is understandable at the level of its stated invariants and extraction risks. It correctly identifies the central danger: technical capability, persistence, partial permissions, and runtime execution silently becoming authority. The invariant set is valuable.

However, it is not yet sufficiently self-contained to reproduce its intended constraints. Blocking gaps include missing definitions of authority/permission/capability, no operational revalidation or commit protocol, no safe-retry model, no composition-evaluation procedure, no output-interface consequence taxonomy, no temporal/control-conflict handling, and unresolved Concord-specific dependencies.

Therefore, it cannot be accepted as `TRANSFER VALIDATED` or `TRANSFER VALIDATED WITH NON-BLOCKING CLARIFICATIONS`. The defects are addressable, so `REVISION REQUIRED` is selected rather than `TRANSFER FAILED`. If a strict reproducibility threshold were applied, this could be classified as `TRANSFER FAILED`; under the supplied four-way criteria, the appropriate disposition is:

**REVISION REQUIRED**
