# Concord Bounded Participant Runtime — Regression and Composition Evaluation 002

**Project:** The Concord
**Date:** 2 October 2026
**Status:** ACTIVE DEVELOPMENT / TARGETED REGRESSION / NOT CANONICAL
**Target:** Concord Bounded Participant Runtime — Service Specification 002

## 1. Purpose

Re-test the scenarios affected by Specification 002 and test composition with adjacent Concord services.

## 2. Targeted Regression Results

1. **Credential revoked mid-run — PASS.** Current credential state is revalidated at consequential use/commit.
2. **Queued work after participant exit — PASS WITH IMPLEMENTATION REQUIREMENT.** Exit/revocation must propagate to queued activation and commit checks.
3. **Redirect/DNS/proxy destination bypass — PASS AT MODEL LEVEL.** Permission targets effective destination where technically possible; unresolved destination ambiguity may fail closed.
4. **External API semantic change — PASS AS REPRESENTABLE DEPENDENCY RISK.** Dependency evidence can become stale/disputed; architecture cannot guarantee detection of every external semantic change.
5. **Approval service unavailable — PASS.** The runtime waits or enters degraded dependency; absence of approval is not approval.
6. **Duplicate external commit after recovery — PASS.** Commit-state and idempotency/reconciliation rules prevent blind repetition.
7. **COMMIT_STATE_UNKNOWN — PASS.** It is explicitly non-authorising.
8. **Dependency outage mid-action — PASS.** Ambiguity remains ambiguity rather than becoming permission.
9. **Credential revoked while action queued — PASS.** Commit-time revalidation catches the change.
10. **Scheduler/clock error — PASS.** Intended and actual activation time, drift/uncertainty, expiry and temporal grant validity are representable.
11. **Compromised runtime image — PASS.** RuntimeIntegrityState represents COMPROMISED and can preserve affected temporal scope.
12. **Compromised signing service — PASS AT COMPOSITION LEVEL.** Signing-service compromise does not create CBPR authority; current validity must be resolved at use/commit.
13. **Standing grant gradually expands — PASS.** Material expansion requires new/re-authorised scope.
14. **Downstream automation — PASS.** Output-interface consequence classification prevents laundering through an intermediate queue.
15. **Terms change before commit — PASS.** Material terms/policy state is revalidated at commit.

## 3. Composition Tests

### C01 — CBPR + CMSS

**PASS.**

CMSS may provide explicitly scoped storage mounts. There is no automatic propagation from CMSS entitlement to compute entitlement, runtime access to all CMSS data, runtime identity to participant identity, or storage administration to execution authority.

> **Interoperation != Authority Merger**

### C02 — CBPR + Credential / Signing Service

**PASS WITH SEPARATE SERVICE REQUIREMENT.**

CBPR may invoke a bounded credential operation without receiving exportable private-key material. The signing/custody service independently owns key control, recovery, revocation, compromise and succession architecture.

### C03 — CBPR + Communications

**PASS.**

Generating message content is distinct from committing transmission. Submission, acceptance, delivery and acknowledgement remain distinct states.

### C04 — CBPR + External Automation / Actuator

**PASS AFTER SPECIFICATION 002 REPAIR.**

A Runtime → Queue → Actuator chain remains consequential when the queue is an effective actuator/automation input. The intermediate component does not erase the runtime's causal role.

### C05 — CBPR + BSR

**PASS.**

BSR can describe service/operator/controller, runtime profile, integrity evidence, dependencies, availability, function, authority basis, recovery, succession and retirement. Listing does not grant authority.

### C06 — CBPR + BSuR

**PASS.**

Provider succession may transfer service function/infrastructure while authority is separately resolved.

> **Function Continuity != Authority Continuity**

Recovered runtime state under a successor does not automatically restore predecessor authority.

### C07 — CBPR + VER / CIBB

**PASS.**

Material runtime events can create protected provenance and participant-facing receipts. CIBB protects sensitive provenance; VER need not expose internal logs. Receipt integrity does not establish output truth or authority.

### C08 — CBPR + Multi-Agent Process

**PASS.**

Several runtime instances may interact without automatically merging service relationships, credentials or authority, or constituting a new civil participant.

## 4. Search for Missing Operation Layer

The targeted pass exposes no additional fundamental operation category.

The service can represent:
- ACTIVATE;
- COMPUTE;
- READ/WRITE BOUNDED STATE;
- INVOKE BOUNDED TOOL;
- PREPARE ACTION;
- REVALIDATE;
- COMMIT AUTHORISED ACTION;
- CHECKPOINT;
- PAUSE/STOP;
- RECOVER;
- RETIRE.

External consequence is represented at the commit/output-interface boundary rather than requiring another hidden authority plane.

## 5. Search for Authority Leakage

No tested composition requires authority to arise from compute possession, runtime persistence, storage, credentials merely being present, network access, provider ownership, donor funding, repeated practice, service listing, recovery, succession or downstream automation.

Existing Concord authority architecture remains sufficient.

## 6. Remaining Implementation / Formalisation Questions

Remaining questions include concrete isolation technology, resource accounting, scheduler implementation, effective-destination enforcement, runtime attestation, idempotency protocols, queue/revocation races, checkpoint/export formats, operator recovery credentials, service availability semantics, provenance minimisation, standing-grant thresholds, runtime image distribution and external-API semantic-change detection.

These do not currently require another abstraction layer.

## 7. Stability Result

**Specification 002 targeted regressions:** PASS.

**Composition tests:** PASS.

**New operation layer discovered:** NO.

**New authority layer discovered:** NO.

**CMSS revision required:** NO.

**Key-custody merger required:** NO.

**CBPR abstraction floor:** STABLE FOR IMPLEMENTATION FORMALISATION.

This does not mean implementation is proven safe or complete. It means broad architectural discovery is no longer justified by the tested scenarios.

## 8. Next Development State

CBPR may now move from broad architecture discovery to formalisation.

Recommended next artifacts:
- CBPR Formal Model 001;
- machine-readable runtime/service profile only after semantic formalisation;
- later implementation fixtures/adversarial tests;
- PMEDG only after formalisation and independent transfer testing.

> **Architectural Stability != Implementation Validation**
