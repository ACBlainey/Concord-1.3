# Decision, ACKS and Bounded Authority — Source Interface 097

**Status:** provisional source-interface crosswalk; not constitutional graduation or a deployed credential-verification design.

## Source anchors

- `02_Domains/04_Governance/Governance Operating Boundary and Authority Lifecycle — Source Resolution 001.md`: legitimate function precedes bounded authority; authority envelope includes actor, purpose, function, permitted action, affected resource, spatial/information/time scope, activation, delegation, revocation, review and provenance. CAP ≠ PERM ≠ AUTH; an existing office or technical capability is not a sufficient authority proof.
- `02_Domains/03_Research/Active_Development/Governance_and_Stewardship/Legitimate Function and the Authority Justification Chain.md`: legitimacy → function → need → authority, never self-authorising function or historic authority.
- `02_Domains/04_Governance/V2.1/Validation/g05_reconciliation_acknowledgements_090.py`: owner-separated, event- and revision-bound ACK/REJECT prototype; authenticated/scope-verified inputs; replay and owner conflict checks; explicitly no authority grant, duty closure, orphan clearance or source mutation.
- `02_Domains/04_Governance/V2.1/Validation/decision_ballot_acks_097.py`: SQLite test fixture; transactional votes, fixed two-matching-ballot result, revision-bound action claims and ACKs. The caller still supplies `mandate`, `host_authorised`, `authenticated` and `scope_verified` booleans; **these are assertions, not source-backed proof**.

## Required interface separation

1. **Decision-owner ballot gate:** verify Steward identity, appointment, position, participation rights, conflict state, context and current mandate **at acceptance**, before atomically recording the ballot. The fixture's boolean mandate cannot substitute for this.
2. **Decision revision gate:** the unique decision and revision identify the determined substantive result; late third-position material is provenance only. Expanded triads provide one authorised constituent resultant per position; no pooled nine-vote majority.
3. **Host-owner execution gate:** independently verify the host's legitimate function, specific action scope, resource, time, necessity, revocation and applicable Clock/emergency conditions. A governance result alone does not authorise execution.
4. **Receiver/ACKS gate:** authenticate the **actual** expected receiving owner, bind the ACK to decision ID, action ID, source/target revision, nonce and evidence, and distinguish RECEIVED/ACCEPTED/COMMITTED/EFFECT_CONFIRMED from an ordinary ACK/REJECT. Existing 090 does not yet provide the richer status vocabulary.
5. **Reconnect gate:** sender queries the authoritative receiver's recorded action state before resending the *same* event identity. Lost ACK does not prove failure; an ACK does not prove external effect. Unknown physical effects require reconciliation, not automatic retry.
6. **Historical gate:** completed decisions are immutable. A later challenge is a newly authorised decision instance, not a revision that retroactively changes the old event. Historical custody and privacy wrappers remain separate from execution authority.

## Open technical contracts

- Real authority and identity attestations, including source owner, verifier, version, expiry and revocation; no selector/issuer invented here.
- Atomic transition plus durable outbox/inbox transport and receiver status query.
- Multi-node partitions, crash injection between physical effect and persisted receipt, reconciliation with real host evidence.
- Existing ACKS source lineage in earlier versions: migration completeness **not verified**. Do not infer that the G05 090 prototype exhausts the earlier ACKS architecture.
- Civilisation Clock ordinary scheduling versus independently event-driven lawful emergency protection.

**Evidence boundary:** stage 097 fixture CI passing validates only the tested local implementation; it does not resolve the above authority contracts or guarantee exactly-once real-world effects.
