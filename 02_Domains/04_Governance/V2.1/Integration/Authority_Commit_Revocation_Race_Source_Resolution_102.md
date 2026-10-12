# Authority Commit / Revocation Race — Source Resolution 102

**Status:** provisional source-interface finding; not a production authority protocol.

## Existing source owners
- `04_Portable_Modules/Concord Bounded Participant Runtime — Portable Module v1.0.md`: current Action Grant, effective target, consequence and commit-time revalidation; implementation validation outstanding.
- `03_Cross_Domain_Architecture/Multi-Key Authority and Rapid Authority Verification — Cross-Domain Source Resolution 001.md`: independently required keys must remain valid; precompute authority, verify current facts.
- `03_Cross_Domain_Architecture/Execution Conformance — Evaluated Route, Actual Execution and Consequence Reconciliation — Source Resolution 001.md`: actual attempted route, observed effect, uncertain commit and host reconciliation.
- `02_Domains/04_Governance/V2.1/G05 — Custody Reconciliation Protocol 002.md`: ACK and owner projection agreement do not imply completed physical effect or discharge of duty.

## Tested interleaving
1. Prepare an action while two owner-held authority grants are current.
2. Revoke either grant before commit-time revalidation: commit must be denied.
3. Revoke after the final validation but before an external effect: a naive check-then-act implementation may still perform the effect. This is the **unfenced commit gap**, demonstrated rather than solved by stage 102.
4. Revoke after an independently recorded completed action: revocation bars new actions but does not automatically erase historical effects. Consequences and remedies remain host/BTA/legal owner matters.

## Necessary production design decision
For each material host action, determine whether the authority owners and effect host can implement a **commit fence** or equivalent protocol with a defined linearization point: an owner-validated, one-use execution lease/token whose issuance and revocation semantics are coordinated with the host's actual effect boundary. A mere short expiry or extra read is **not** proof of atomicity. If the external host cannot fence revocation against effect, classify and document the residual race and its consequence-specific policy; require status reconciliation, auditable provenance and proportionate remedy rather than claim zero race.

An emergency action is not an exception to legitimate authority. The Civilisation Clock may pause; emergency expiry and authority checks require an independently operating real-time/event path.

## Fixture limits
`authority_commit_race_102.py` uses the owner registry of stage 101 and deterministic callbacks. It contains **no true concurrency, process partition, network failure, cryptographic authority proof or external physical effect**. Its `run` method is not a safe production transaction; `observed_gap` deliberately demonstrates the unsafe interleaving. Do not graduate it as CBPR/MKA implementation.

## Follow-up validation
- Host-owned, one-use fenced execution token with expiry, revocation ordering and status query.
- Separate-process race tests and fault injection between grant issuance, revocation and host effect.
- Explicit decision about whether revoke-before-commit must prevent action, versus revoke-after-commit only preventing future action.
- Integration with BTA residual-effect records, CBPR action grant and G05 ACKS evidence.
