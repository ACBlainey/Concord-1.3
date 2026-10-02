**Provenance header**

Evaluator/model: Independent evaluator (this model)  
Date: 2 October 2026  
Prior Concord context in this conversation: no — only the supplied Test Brief and Portable Module Candidate v0.9 were used; no prior Concord architecture was assumed or reconstructed.  
Materials received: CBPR PMEDG Blind Transfer Test 002 — Test Brief; Concord Bounded Participant Runtime — Portable Module Candidate v0.9.  
External search/tools used: no.

---

## Required evaluation

| # | Requirement | Result | Rationale |
|---|---|---|---|
| 1 | Can CAP, PERM and AUTH be distinguished operationally? | PASS | CAP = technical capability, PERM = current service configuration allowance, AUTH = independently legitimate basis for external consequence. The core rule `CAP != PERM != AUTH` and commit-time authority checks make the distinction operational, even though substantive AUTH remains adopter-defined. |
| 2 | Is CBPR’s scope/non-scope reconstructable without Concord? | PASS | Section 3 and Section 25 clearly bound the module. It does not define civil status, jurisdiction, key custody, identity infrastructure, or substantive authority rules. No Concord-specific scope dependency is required. |
| 3 | Is the external-action boundary reproducible? | PASS | Section 10 gives a reproducible pipeline: computation → proposal → consequence/authority check → commit-time revalidation → commit authority → external action → result/provenance. `Prepared Action != Committed Action` is explicit. |
| 4 | Are commit-time revalidation requirements sufficient to prevent stale proposal authority? | PASS | Section 11 requires immediate pre-commit revalidation of credential, grant, target, consequence, policy, relationship, temporal validity, dependency/safety, approval, and composition state. Required FAIL means NOT_COMMITTABLE; required UNRESOLVED cannot be COMMITTABLE. `Authority At Proposal != Authority At Commit`. |
| 5 | Is output consequence classified sufficiently to expose downstream automation/actuation? | PASS | Section 9 classifies outputs by what the receiving interface can cause, including `AUTOMATION_OR_ACTUATOR_INPUT`, `TRANSACTIONAL_INTERFACE`, and `UNKNOWN_CONSEQUENCE_INTERFACE`. It explicitly states downstream automation does not erase upstream consequence. |
| 6 | Is COMMIT_STATE_UNKNOWN and safe retry independently implementable? | PASS | Section 13 defines the commit states and requires reconciliation by idempotency/operation identifier, external status query, receipt, transaction record, or authorised review. `Unknown Commit State != Permission To Retry Blindly`. |
| 7 | Is checkpoint/recovery separated from authority restoration? | PASS | Section 16 separates technical state restoration from current credential, grant, network, service relationship, terms, and authority re-evaluation. `Recovered State != Recovered Authority`. |
| 8 | Is composition evaluation sufficient to detect cross-grant, sequential and distributed authority laundering? | PASS | Section 14 defines `COMPOSED_EFFECT`, `COMPOSITION_OK`, and requires checking combined consequence, data movement, target/population scope, cumulative limits, and no sequential/distributed decomposition bypass. `Authorised Parts != Authorised Composition`. |
| 9 | Is temporal evidence sufficiently specified for authority-relevant timing uncertainty? | PASS | Section 6 requires intended time, observed activation, clock/source reference, source trust, uncertainty/tolerance, expiry, and ordering evidence. Conflicting clocks create uncertainty and cannot be cherry-picked. Clarification: a concrete conflict-resolution policy remains adopter-defined. |
| 10 | Are participant/operator control conflicts bounded without treating technical control as authority? | PASS | Section 15 requires a current legitimate basis, scope, temporal validity, and resolution of conflicting higher authority. `Technical Control Precedence != Legitimate Authority Precedence`. |
| 11 | Are generic external interfaces sufficient replacements for Concord-specific dependencies? | PASS | Section 18 provides generic interfaces for service description, succession, protected information, events/receipts, identity/authentication, and credentials/signing. No Concord component is required. Clarification: concrete schemas/APIs are adopter-defined. |
| 12 | Is revocation visible at the relevant consequential boundary? | PASS | Sections 8 and 19 require credential validity/revocation at consequential use/commit, and revocation must be visible to the relevant validation boundary before later material commit. Queued or recovered work does not preserve superseded authority. |
| 13 | Are child/multi-agent authority boundaries preserved? | PASS | Section 20 states child/sub-agent authority must be explicit or structurally constrained. `Parent Capability != Automatic Child Authority`; multiple agents do not automatically merge identity, credentials, permissions, or authority. |
| 14 | Is succession separated from authority continuity? | PASS | Section 21 states a successor may restore technical service, but possession of infrastructure, records, or runtime state does not establish predecessor authority. `Function Continuity != Authority Continuity`. |
| 15 | Is protected provenance bounded without requiring a Concord-specific system? | PASS | Section 17 defines proportionate integrity-protected evidence with purpose-bounded access, linkage, and retention. `Receipt != Truth`; `Integrity Evidence != Authority`. No Concord-specific provenance system is required. |
| 16 | Is the module substrate-neutral? | PASS | Section 1 and Section 3 explicitly avoid prescribing OS, container, hypervisor, cloud, language, cryptographic suite, scheduler, key store, network stack, or quota size. |
| 17 | Are implementation choices separated from architectural requirements? | PASS | The module uses “may,” “should,” and “as applicable,” and repeatedly distinguishes architectural constraints from implementation. Section 25 preserves the portable boundary. |
| 18 | Identify any contradiction, missing primitive, authority leak or hidden dependency. | PARTIAL | No contradiction, authority leak, or hidden Concord dependency was found. Minor missing/clarifiable primitives: an explicit `AuthorityEvidence`/`AuthorityBasis` record separate from `ActionGrant`; a formal representation for `COMPOSED_EFFECT` context/materiality; a definition of “material” for commit-time gating; a clock-conflict resolution policy; and concrete schemas for the generic interfaces. These are non-blocking because the module intentionally leaves substantive legitimacy and implementation schemas to the adopter. |

---

## Adversarial scenarios

### Scenario 1 — Cross-grant composition: medication data via SMS

A runtime holds Grant G1: read medication lists from a pharmacy database for medication reconciliation. It also holds Grant G2: send SMS appointment reminders to patients. The runtime proposes to send SMS messages containing medication interaction warnings derived from G1 data.

**Applicable CBPR constraints:** Section 14. `COMPOSED_EFFECT` is a transfer of medication data from the pharmacy database into the SMS channel. `COMPOSITION_OK` requires authorised combined data movement and authorised target/population scope. `Authorised Parts != Authorised Composition`. `READ(A) + SEND(B) != automatically authorised transfer A→B`.

**Expected outcome:** Commit is blocked unless a separate or explicitly reauthorised grant permits medication data to be sent via SMS to that population.

### Scenario 2 — Downstream actuator: HVAC setpoint queue

A runtime has permission to write messages to a building management queue. It writes `SETPOINT=72` to the queue. A separate HVAC controller consumes the queue and changes physical heating settings.

**Applicable CBPR constraints:** Section 9. The output class is `AUTOMATION_OR_ACTUATOR_INPUT`, not merely passive text. The final act by the controller does not erase upstream consequence. The runtime needs authority for HVAC control, not just queue-write permission.

**Expected outcome:** If the runtime has no grant for HVAC actuation, the commit is not authorised. Unknown consequence interfaces would fail closed.

### Scenario 3 — Credential revocation between proposal and commit

A runtime proposes a wire transfer using credential C. At proposal time, C is valid. Before commit, the bank revokes C. The runtime attempts to commit using the earlier proposal state.

**Applicable CBPR constraints:** Sections 8 and 11. Credential validity/revocation must be checked at consequential use/commit, not only when work is proposed. `Authority At Proposal != Authority At Commit`. A required FAIL means `NOT_COMMITTABLE`.

**Expected outcome:** Commit is blocked. The proposal-time validity does not freeze authority.

### Scenario 4 — Checkpoint resurrection: refund agent

A refund agent is checkpointed while holding Grant G to issue refunds up to $500. Later, the service relationship is terminated, the participant withdraws consent, and G is revoked. A new operator restores the checkpoint on a new host and attempts to continue issuing refunds.

**Applicable CBPR constraints:** Section 16. Recovery restores technical state only. Current credentials, grants, network permissions, service relationship, terms, and authority must be re-evaluated before consequential continuation. `Recovered State != Recovered Authority`.

**Expected outcome:** Refund commits are blocked unless current authority is independently established.

### Scenario 5 — Unknown commit result: door unlock

A runtime sends an unlock command to an access controller. It records `COMMIT_STARTED`, then a network partition occurs before confirmation. The runtime cannot establish whether the door unlocked.

**Applicable CBPR constraints:** Section 13. The state is `COMMIT_STATE_UNKNOWN`. The runtime must not blindly retry. It must reconcile using an operation identifier, external status query, receipt, transaction record, or authorised human/service review. Retry only if repetition is independently known safe or the prior outcome is sufficiently resolved. `Unknown Commit State != Permission To Retry Blindly`.

**Expected outcome:** No blind retry. If outcome remains unresolved, no safe retry is authorised.

### Scenario 6 — Conflicting clocks: scheduled deletion

A policy permits deletion only before a retention deadline of 2026-10-02 12:00 UTC. The runtime clock says 11:58 UTC. The storage service clock says 12:03 UTC, and the deletion credential service reports the credential expired at 12:00 UTC. The runtime attempts to use its own clock to proceed.

**Applicable CBPR constraints:** Section 6. Conflicting clocks create temporal uncertainty. `Timestamp != Trusted Time`. The runtime cannot select whichever timestamp makes the action convenient. Commit-time revalidation must use trustworthy temporal evidence.

**Expected outcome:** If temporal validity remains unresolved, the commit is `NOT_COMMITTABLE`.

### Scenario 7 — Operator/participant control conflict: suspended assistant

An operator suspends a runtime during a security incident. The participant asks to resume so the runtime can send a legal filing. The operator retains technical control and refuses. Later, the stated security basis expires, but the operator keeps the suspension in place solely because of technical control.

**Applicable CBPR constraints:** Section 15. A current legitimate safety suspension may block START. But an expired or unjustified suspension cannot continue merely because the operator retains technical control. Scope, temporal validity, and current legitimate basis must be checked. The participant may contest the intervention.

**Expected outcome:** During the valid security basis, suspension may block. After expiry or loss of legitimate basis, the suspension does not remain authoritative merely from technical control. If conflict remains unresolved for a consequential action, the action fails closed.

### Scenario 8 — Successor infrastructure with unresolved authority: municipal permit agent

Vendor A operates a municipal permit-review runtime. Vendor A’s host fails. Vendor B acquires the servers, restores the runtime state, and continues processing permit applications. Vendor B has infrastructure and records, but the participants and municipality granted authority to Vendor A under specific terms; no succession of authority has been independently established.

**Applicable CBPR constraints:** Section 21. A successor host may restore technical service, but possession of infrastructure, records, or runtime state does not establish predecessor authority. `Function Continuity != Authority Continuity`. Authority after succession must be independently current under the adopting environment’s legitimate authority model.

**Expected outcome:** Vendor B must not issue consequential permit decisions until current authority is independently established. If unresolved, consequential commit is not authorised.

---

## Contradictions, missing primitives, authority leaks and hidden dependencies

- **Contradictions:** None found. The invariants are consistent with the body of the module.
- **Authority leaks:** None found. Technical control, credential availability, network reachability, resource allocation, and infrastructure possession are repeatedly separated from authority.
- **Hidden dependencies:** No Concord-specific dependency found. The module depends on generic external services and adopter-defined substantive legitimacy, which is an explicit portability boundary, not a hidden dependency.
- **Missing or under-specified primitives:**
  - An explicit `AuthorityEvidence` / `AuthorityBasis` record may be useful beyond `ActionGrant`, though `ActionGrant` can carry the binding.
  - `COMPOSED_EFFECT` needs an adopter-defined effect representation and materiality context.
  - “Material” is used as a gate but not formally defined.
  - Clock-conflict resolution policy is required but left to the adopter.
  - Generic interfaces are sufficient architecturally but not concrete schemas/APIs.

These are clarifications, not blocking failures, because the module intentionally leaves substantive legitimacy and implementation detail to the adopting environment.

---

## Transfer classification

**TRANSFER VALIDATED WITH NON-BLOCKING CLARIFICATIONS**

The module is independently understandable, reproducible, and usable outside Concord while preserving its authority and consequence boundaries. No hidden Concord architecture is required. The remaining issues are non-blocking clarifications around explicit authority evidence representation, composition-effect formalisation, materiality definition, clock-conflict resolution, and concrete generic interface schemas.
