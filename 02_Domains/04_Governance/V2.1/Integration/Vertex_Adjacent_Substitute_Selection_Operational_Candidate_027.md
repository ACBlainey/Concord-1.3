# Vertex-Adjacent Substitute Selection — Operational Candidate 027

**Status:** PROVISIONAL; proposed operating procedure, not a constitutional rule. Interfaces with Chapter 12 Candidate 010, Chapter 132 Candidate 008, and source resolutions 024–026.

## Purpose and invariants

Fill **one lawfully vacant Steward voting position** for a single bounded decision event without changing the triad's three-position denominator, original jurisdiction or vote weight. The shared abstract GTP vertex identifies five *other* triangle-owned Steward positions as the normal candidate pool; it does not constitute a six-Steward governing body. The substitute receives no standing authority in the originating triangle.

## Preconditions

1. An independently valid **decision event ID**, original triad ID, Steward position ID and abstract vertex ID are recorded.
2. The original Steward is **lawfully recused for material conflict** or is unavailable under some *separately authorised* absence/incapacity rule. The original Steward's vote-specific authority for the matter is suspended before replacement. Insufficient-information abstention is **not** a vacancy trigger: route to evidence gathering.
3. The relevant constitutional or delegated mandate permits **temporary position substitution**. Geometry only identifies candidates; it does not itself confer authority.
4. The complete decision-event participation graph is known enough to enforce **one human/AI participant per Steward voting position for the entire event**.

## Construct candidate pool

Resolve the five incident triangles other than the origin triangle at the original abstract vertex. For each, identify the **single Steward assigned to that same vertex position**, not an arbitrary Steward from that triangle.

Screen every candidate against: independently established eligibility and mandate; identity uniqueness across the complete event; availability; material conflict concerning the decision; valid authentication; legally required independence; and any other applicable safeguards. Record exclusions by reason code with confidential detail protected.

**Critical:** The normal pool size is five, but the *eligible* pool size `n` may be 0–5. Never silently substitute an ineligible holder, invent an additional sixth alternate, or alter the decision jurisdiction.

## Fair selection and authority binding

1. Freeze the candidate list and its eligibility proofs for this attempt; canonicalise and hash its order-independent membership.
2. Commit to an auditable randomness procedure **before** seeing the outcome. The authorised procedure must prevent the requester, recusing Steward or convening authority from biasing the draw. A future publicly verifiable randomness beacon or multi-party commit/reveal could implement this; the actual source and verification standard remain to be specified.
3. Select exactly one of the `n` eligible candidates with equal probability, using an unbiased index (e.g., rejection sampling, **not** modulo reduction with bias). Record draw ID, seed evidence, eligible-set commitment and selected candidate, with privacy-preserving public projection where appropriate.
4. Revalidate selected candidate's conflict, identity uniqueness, event scope and independent authority **at commit time**. If validation fails, record the invalidation. A new draw is allowed only by a predefined neutral failure policy; do not redraw because of vote preference.
5. Issue a **single-use bounded position-substitution authority** that names the original position, substitute, event, scope, termination condition and authorising basis. The original Steward may not also exercise the position. One valid vote occupies one original position; the substitute is not a fourth triad vote.
6. Close/expire substitute authority at the decision-event boundary; preserve audit/provenance records without preserving vote authority.

## When the pool is reduced

| Eligible `n` | Action |
|---|---|
| 5–2 | Uniform random selection from all eligible candidates, with `k/n` single-draw probability of choosing one of `k` compromised eligible candidates, assuming an uncompromised draw and screening |
| 1 | No randomness is meaningful. **Do not assume automatic appointment**; invoke independent legitimacy and capture-risk checks. If policy does not permit deterministic appointment, withhold |
| 0 | No eligible local substitute. Withhold decision commitment and invoke an **independently authorised** postponement, other substitution or escalation procedure; never fabricate a voter |

**No minimum eligible pool threshold is established by this candidate.** Whether a pool of one is sufficient, or a minimum of two is required to retain anti-capture benefits, requires explicit authorial/constitutional choice.

## Failure codes

`NOT_A_VACANCY`, `CONFLICT_UNRESOLVED`, `AUTHORITY_MISSING`, `EVENT_BOUNDARY_UNKNOWN`, `CANDIDATE_POOL_INCOMPLETE`, `CANDIDATE_INELIGIBLE`, `IDENTITY_DUPLICATE`, `NO_ELIGIBLE_ALTERNATE`, `DRAW_INTEGRITY_FAILURE`, `SELECTED_HOLDER_BECAME_INELIGIBLE`, `QUORUM_UNVERIFIED`, `COMMIT_AUTHORITY_EXPIRED`.

A mathematically calculated For/Against/Unresolved tally is **diagnostic only** if any procedural gate is invalid. No majority or invalid decision cannot cause a state change.

## Anti-capture and abuse controls

- **Vacancy manipulation:** independent proof of conflict/absence; reviewable challenge path; no substitute merely for unpopular votes.
- **Eligibility manipulation:** objective and recorded exclusions; independent review; no exclusion to shrink the pool toward a preferred alternate.
- **Randomness manipulation:** precommitted fair draw; public audit of method; private identity data protected.
- **Repeated attempts:** same decision-event ID, immutable audit trail and a neutral predefined retry policy. Do not reset identity-uniqueness checks by renaming the event.
- **Nested expansion:** substitute cannot already occupy any position in the decision event; single-position substitution is not a three-to-one constituent resultant.
- **Quorum:** original denominator stays three; any valid quorum and recusal effects must come from separately adopted rules.

## Source attribution

Historical governance already distinguished cause-coded abstention, recusal, absence, and temporary or neighbouring-Steward replacement, while explicitly leaving the voting denominator incomplete. The **five-position vertex pool, fair random draw, exact workflow and security controls** are new authorial development and implementation proposals, not historical quotations.

## Open decisions

Minimum pool size; binding randomness source; treatment of a selected candidate who declines or becomes ineligible; lawful recusal determination/challenge; permitted retries; exact quorum rule; emergency alternatives; and independent event-boundary authority.
