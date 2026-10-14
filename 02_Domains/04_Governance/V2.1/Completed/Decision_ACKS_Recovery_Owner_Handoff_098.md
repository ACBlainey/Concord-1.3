# Decision–ACKS Recovery: Owner Handoff and Failure Matrix 098

**Status:** provisional interface specification / source-derived crosswalk / not graduated.

## Owner boundaries

The existing Concord sources determine the responsibilities:

| Stage | Responsible architecture | Record / invariant |
|---|---|---|
| Legitimate decision | Governance and bounded Steward authority | Unique decision ID; one official ballot per position; fixed two-matching-vote result; completed event immutable |
| Action proposal and grant | CBPR / competent host / MKA / contextual wrapper | Action identity, evaluated route, actual target, bounded authority, consequences, validity and expiry |
| Material commit | CBPR and receiving host | Revalidate current grant and target; atomically claim idempotency identity where host supports it |
| Transition and partial effects | BTA | Crossing state, residual effect and recovery references; failed attempt is not zero history |
| Receipt and owner projections | Receiving host and G05 owner-specific ACKS | Authenticated owner, expected revisions, nonce, event/action reference and evidence |
| Downstream dependency | KCS | Propagate only material changes and retain stale/disputed state |
| Historical record | Historical under contextual access wrappers | Immutable provenance and rights-preserving custody |

Source anchors: `03_Cross_Domain_Architecture/Execution Conformance — Evaluated Route, Actual Execution and Consequence Reconciliation — Source Resolution 001.md`; `02_Domains/04_Governance/V2.1/G05 — Custody Reconciliation Protocol 002.md`; `02_Domains/04_Governance/Governance Operating Boundary and Authority Lifecycle — Source Resolution 001.md`.

## Failure / reconnect matrix

| Point of interruption | Known evidence | Safe continuation |
|---|---|---|
| Before durable ballot receipt | No owner commit established | Query decision owner by same event/position ID; only re-present the same vote with valid mandate |
| Ballot committed, response lost | Decision-owner revision and position record | Return recorded outcome; no second ballot or new decision ID |
| Result fixed, action not yet authorised | Governance result only | No execution; obtain host's independent bounded action grant |
| Action authorised, commit not attempted | Valid current host grant and same action ID | Revalidate at actual commit time, including Clock/expiry/context |
| Commit request sent, ACK lost | Unknown receiving-host commit | Query host status by idempotency ID; never assume no effect |
| Physical effect possible, receipt missing | Partial or uncertain BTA/CBPR evidence | Hold UNCERTAIN, reconcile actual effects; no blind repeat |
| ACK recorded, owner effect disputed | ACK evidence but no effect proof | Preserve dispute; ACK does not close underlying action/duty |
| Projection owner unavailable | Other owners acknowledged | PENDING_RECONCILIATION; do not mutate absent owner's record |
| Mandate revoked during outage | Prior authority evidence stale | No new commit; record revocation and reconcile effects already made |
| Emergency while Clock paused | Separate emergency trigger and authority | Lawfully bounded immediate emergency route; no wait for ordinary Clock tick |

## Negative invariants

1. ACK is not a grant, not an execution receipt unless its authenticated type/evidence establishes that specific fact, and not proof of completed real-world consequences.
2. A communications retry is the **same event identity**; creating a new decision or action identity to escape an unresolved old one is prohibited.
3. Local transactional SQLite tests (093–097) do not establish multi-host atomicity, authenticated service ownership, external exactly-once execution or correctness of a constitutional mandate.
4. No G05 coordinator may unilaterally rewrite CBPR, BTA, KCS, Historical or host-owner state.
5. An emergency route must be separately authorised and must not be blocked by a paused variable Civilisation Clock.

## Validation required before graduation

- Recover any earlier ACKS-specific sources not present in V1.3, retaining provenance and version differences.
- Derive actual CBPR action-grant and host status-query schema; bind G05 event/revision/owner attestation.
- Exercise network partition, replay, crash after external effect but before receipt, expired grant and owner disagreement against separate durable processes.
- Distinguish owner **receipt**, **acceptance**, **commit**, **effect** and **projection agreement**; none should silently imply another.
- Review effects on BTA/KCS/Historical and domain-specific emergency exceptions.

This document is a source-owner routing companion, not a replacement for the underlying CBPR, BTA or G05 protocols.
