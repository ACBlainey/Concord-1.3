# Glass Hammer — CIBB-Informed Owner-Checked Projection 118

**Status:** bounded test adapter, not an authenticated information security service.

## Existing source alignment

- `04_Portable_Modules/Concord Information Black Box Portable Module v1.0.md`: user access means `Projection(Master,Context)`, not possession of master; disclosure is a governed information operation; authority to read does not imply authority to transfer.
- `04_Portable_Modules/Contextual Wrapper Architecture — Portable Module.md`: bounded context grammar; permissions depend on role, scope, purpose and time.
- `02_Domains/04_Governance/V2.1/Validation/authority_owner_registry_101.py`: independently issued and revocable **information-access grants**, separate from immutable Steward ballot authority.
- Stage 117: sealed peer ballots and concerns, minimal review-router projections.

## Implementation

Stage 118 checks owner-issued grants for actor, operation, decision ID, purpose, revision and time before invoking Stage 117's role-specific projections. Reviewer access requires a separate scoped independent-reviewer grant. Revoking an information-access grant denies subsequent projection; it never alters an already committed vote.

This replaces Stage 117's caller-supplied `authority_verified=True` at the outer adapter boundary, while preserving the CIBB distinction between protected master and projection.

## Critical limitations

- The fixture uses two SQLite databases and does **not** establish cross-database atomicity. Revocation could race with projection. Production access requires an owner-mediated read/commit boundary or conservative revocation-aware protocol.
- The caller supplies `subject`, `now` and `revision`; the adapter does not authenticate identity, verify trusted time or establish authoritative current revision.
- Reviewer independence is represented by a separate owner-issued grant, not substantive verification of conflict-of-interest, aliases or relationships.
- The database is not encrypted or physically sealed, and direct DB access bypasses this adapter. This is not the deployed CIBB module.
- No vote content may be disclosed to peers by default; authorised independent review of ballots requires a separate policy and authority.
- A Steward's ballot is immutable. Only unexercised grants and information-access rights may be revoked.
