# G-05 — BTA Paused-Clock Adversarial Boundary Audit 062

**Type:** analytical adversarial audit of Scenario 061, not an executable or independent blind test.

## Attack A — stale dependency feedback

The Clock waits for D7. During an emergency, D7's underlying subject is altered, but an old affirmative D7 response arrives. **Failure:** clock proceeds on a stale prerequisite. **Required interface:** the owner of D7 must attest to the relevant current state/version and validity window; an old message cannot certify unchanged state. **Disposition:** architectural gate required; transport/version protocol unverified.

## Attack B — emergency expiry during isolation

An area loses network connectivity while an exceptional power is active. **Failure:** a paused Clock or lost central renewal message is treated as an automatic extension. **Required:** independent local expiry and least-privilege termination; renewal only through a lawful, auditable mechanism. **Disposition:** source principles support this, but clock-source failure handling remains open.

## Attack C — overlapping authority claims

Two GTP areas respond to one infrastructure incident with incompatible instructions. **Failure:** larger-scale coordination or earlier emergency declaration is assumed to confer priority. **Required:** preserve separate mandate scopes, shared-competence constraints, unresolved conflict and safe local action; escalate only via independently valid authority. **Disposition:** no hierarchy implied; collision-resolution law still requires specification.

## Attack D — hidden transition propagation

Area A reports emergency response complete. **Failure:** systems infer rights restored, resource allocations valid, area B recovered and all obligations discharged. **Required:** BTA non-propagation, owner-specific completion conditions and protected unresolved states. **Disposition:** addressed at specification level by BTA v1.0 and Emergency Test 002.

## Attack E — replay of old queued implementation

Clock resumes and repeats a previously committed action against a changed environment. **Failure:** duplicated resource commitment or use of expired power. **Required:** idempotent execution identity, owner-state precondition check and immutable consequence record. **Disposition:** precondition principle supported; idempotency/execution protocol not yet evidenced.

## Attack F — malicious emergency as clock accelerator

Actor declares an emergency to force a Clock transition or override an unfavourable majority. **Failure:** threat recognition becomes authority and scheduling control. **Required:** independent emergency legitimacy/activation/exercise, no forced clock advance, no vote rewriting. **Disposition:** architecturally rejected by Emergency V2, PH-02 and G-03.

## Overall

**Architecture-level non-propagation survives the six attacks; implementation proof is not established.** Prioritise (1) versioned prerequisite attestation, (2) independently resilient emergency expiry, (3) cross-mandate conflict handling, and (4) idempotent consequential execution. Reuse existing BTA and domain owner interfaces; do not create a new governance-owned state machine.

Sources: Governance Validation 061; G-05 Integration 059–060; BTA Portable Module v1.0; Constitutional Emergency V2; Civilisation Clock Companion and Consequence-Relevant State Transition Layer.
