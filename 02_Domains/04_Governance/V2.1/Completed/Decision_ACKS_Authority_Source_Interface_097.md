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


## Source recovery: CBPR/BTA execution conformance and G05 custody reconciliation

Further V1.3 source review identifies existing architecture that must **own** the recovery semantics, rather than letting the 096/097 SQLite fixtures become a parallel system:

- `03_Cross_Domain_Architecture/Execution Conformance — Evaluated Route, Actual Execution and Consequence Reconciliation — Source Resolution 001.md` identifies CBPR as owner of Action Proposal, effective target, consequence classification, scoped Action Grants, commit-time revalidation, unknown-commit reconciliation, receipt and idempotency boundaries; BTA as owner of transition and residual-effect history; KCS as owner of downstream material-change review; MKA/BRSP as upstream route evaluation. **Unknown commit state is already a reconciliation problem in CBPR**, not a new Governance or ACKS authority.
- `02_Domains/04_Governance/V2.1/G05 — Custody Reconciliation Protocol 002.md` specifies independently owner-issued, authenticated, revision-checked ACKs; partial delivery remains PENDING_RECONCILIATION; owner projections are not silently rewritten; ACK consensus does not extinguish an underlying duty. Its G05 090 prototype is a candidate projection mechanism, not universal action execution evidence.

**Revised integration boundary:** Governance records the uniquely identified ballot/result and references a host-owned proposed action; CBPR/MKA/CWA and host owners validate commit-time authority and route/effect envelope; BTA tracks partial/residual transitions; the receiving host owns actual action status and effect receipts; ACKS transports and reconciles owner-specific acknowledgements; KCS tracks relevant downstream changes; Historical preserves provenance. Do not infer that an ACK of message receipt is an ACK of commit, effect, custody discharge or constitutional approval.

**Gap remaining:** bind 097's `expected_revision`, `mandate`, `host_authorised` and ACK owner to real owner-controlled versioned attestations and CBPR commit/effect references. The SQLite fixture does not currently implement this source contract. Avoid describing 097 as the deployed implementation of CBPR, BTA, MKA or G05.
