# G05 — Bounded Governance, Continuity and Recovery Integration 001

**Status:** V2.1 working architecture / integration candidate. **Not canonical, not deployed, not a grant of authority.**

## Purpose and scope
Consolidates G05 validation stages 070–087 into a coherent Governance interface. These prototypes describe safeguards for cross-resolution coordination, BTA transition evidence, recovery, continuing obligations, emergency intervention and aggregate restrictions. They do not replace the graduated BTA portable module, KCS, SMM, Civilisation Clock, Constitutional Emergency V2, Historical, Continuity or owner-domain mandates.

## Constitutional and architectural invariants
1. **CAP ≠ PERM ≠ AUTH.** Technical ability, permission and legitimate authority are distinct. No fixture issues authority.
2. **GTP is a simultaneous-resolution spatial mesh.** Parent/child denote geometry only. Overlap, proximity, wider scale or coordination do not imply governance rank. Triadic stewardship and independent domain mandates remain separate.
3. **BTA owns transition semantics.** Crossings may be partial and asynchronous; recovery or rollback does not erase external effects, records or duties.
4. **KCS propagates dependency changes but does not confer authority.** SMM describes state, not permissions.
5. **Civilisation Clock may pause indefinitely.** Emergency operational windows expire on their own clock. Any deferred execution needs live owner, scope and dependency revalidation.
6. **Recovery ≠ restoration ≠ closure.** A resumed function may still owe remediation, custody, privacy, archival, evidentiary and beneficiary duties.
7. **Referral ≠ succession ≠ authority.** Civil Contact can route a case; Historical can preserve provenance; Continuity can coordinate its interface; only duly authorised owners may make consequential decisions.
8. **Emergency intervention is temporary, scoped, reviewable and independently justified.** Renewal is a fresh decision. Cumulative effects must be examined across successive mandates and across different controllers.
9. **Review flags are not findings of unlawfulness.** Numerical exposure thresholds are provisional test configuration, not Concord constitutional law.

## Functional map and evidence status

| Stages | Candidate interface | Governance integration |
| --- | --- | --- |
| 070, 072–073 | Original BTA transfer fixture, compatibility projection, adversarial record validation | Accept source records only with provenance; quarantine legacy-only fields; reject authority inference |
| 074–075 | Owner attestation and asynchronous evidence ledger | Obtain externally verified, live owner decisions; distinguish record receipt from transition completion |
| 076–078 | GTP resource collision, reconciliation proposals, execution revalidation | Detect spatial/functional overlap without hierarchy; proposals do not allocate authority; recheck at execution |
| 079–080 | Partial execution, recovery, outcome classification | Keep surviving effects and duties visible; require independent evidence before any restoration claim |
| 081 | Continuing-duty ledger | Operational recovery must not automatically close duties |
| 082 | Duty succession | Transfer custody only with verified parties, provenance and revision; obligation remains open |
| 083 | Orphaned duties | Detect, preserve and refer; nomination is not assignment |
| 084 | Protective intervention | Require external mandate, scope, time bounds, necessity, proportionality and review; never assign permanent custody |
| 085 | Renewal | Fresh mandate and independent/cumulative review; no extension by inertia |
| 086 | Cumulative exposure | Union and longest uninterrupted control for one controller; flag review, not illegality |
| 087 | Distributed exposure | Union across controllers and concurrent-controller counts; detect de facto aggregate restrictions |

All test results are **unit-level fixture evidence**, not end-to-end system certification. See `Validation/README.md` for the register and current CI state.

## Governance lifecycle (normative candidate, not executable workflow)
1. **Identify:** Civil Contact or domain owner receives the concern; preserve minimum necessary evidence and protected beneficiary references.
2. **Resolve competence:** Identify functional jurisdiction, relevant triad(s), actual mandate and independent owner authority. GTP spatial resolution alone cannot select a superior decision-maker.
3. **Revalidate:** Use KCS change signals, owner attestations, bounded authority and current operational context. A paused Civilisation Clock is not permission to bypass expiry.
4. **Coordinate:** Where contexts overlap, surface collisions and alternatives without imposing a hierarchy or silently reallocating resources.
5. **Execute only under owner-system authority:** The prototype can report eligibility for review, never permission or execution authorisation.
6. **Record outcome:** Distinguish resumption, compensation, reconstruction and verified restoration. Preserve residual externalities, protected records and unresolved duties.
7. **Maintain custody:** Transfer through authorised succession; otherwise retain a discoverable orphan record and route to Civil Contact/Continuity/Historical as appropriate.
8. **Protect provisionally where justified:** Emergency action requires a separate constitutional mandate and independent expiry/review; never substitutes for permanent succession.
9. **Audit aggregate control:** Review successive and distributed restrictions across controllers and resolutions, including continuity, concentration and cumulative consequences.
10. **Close only by authorised evidence:** Preserve original duty provenance and closure audit. Neither retirement, restoration nor elapsed time implies discharge.

## Interfaces requiring authoritative source resolution
- **Governance V1 triadic mechanics and V2.1 chapter patches:** independent steward reasoning, decision aggregation, local competent context, lateral coordination, authority limits and recusal.
- **GTP:** spatial intersections and resource collision identifiers must not silently become jurisdictions.
- **Constitutional Emergency V2:** issuer competence, necessity, proportionality, time limits, review and emergency exit; these are NOT specified by Python fixtures.
- **BTA portable module:** actual 28-field contract and transition owner-system semantics, including six quarantined legacy-only names.
- **KCS/SMM/Civilisation Clock:** authentic state changes, stale dependency detection and independent emergency operational time.
- **Historical/Continuity:** record ownership, privacy wrappers, immutable provenance, survivorship and authorised duty closure.
- **Civil Contact:** discoverability and routing, not adjudication.
- **Stewardship Selection and Allocation:** steward qualification/appointment must not be invented locally.

## Integration gaps and limitations — do not silently graduate
1. **No end-to-end harness:** stages currently validate small isolated Python models; no integrated owner-system BTA/KCS/GTP/emergency run.
2. **Attestations are booleans in prototypes:** cryptographic identity, authorisation scope, issuer trust and tamper-evident provenance are not implemented.
3. **Duty registers are in-memory:** no durable transactional storage, concurrent edits, conflict resolution, privacy enforcement, retention or archival chain of custody.
4. **087 initial CI failure:** five test constructors lacked restriction_kind; corrected after inspecting GitHub Actions logs. Re-run must pass before claiming 087 validated.
5. **Restoration equivalence:** user-provided verification flags are not independent proof of functional, custodial and historical equivalence.
6. **Strict YAML parsing:** duplicate-key rejection, full 28-field schema validation and robust legacy-semantic reconciliation remain incomplete.
7. **Cumulative-control thresholds:** no constitutionally approved threshold, scope harmonisation, aggregation of different restriction kinds or independent review protocol.
8. **Orphan protection:** no mechanism for a real authority to issue, revoke, contest or appeal mandates; model must not autonomously intervene.
9. **Governance reconstruction:** the 215-chapter V2 source and recovered V1 triadic provisions have not been fully incorporated or graduated. This document is an interface chapter, not a claim of full governance completeness.

## Graduation gate
Do not promote this candidate to canonical governance until: (a) source-resolution against preserved V1/V2 and graduated modules; (b) explicit owner and constitutional review; (c) real integrated negative/positive tests with tamper, concurrency, expiry and privacy scenarios; (d) audit of overlapping mandates and surviving duties; (e) tracked chapter-patch integration and section assembly; and (f) documented independent validation and change provenance.

**Preservation rule:** `../Governance V2 Canonical.md` remains unchanged. This file provides modular V2.1 incorporation and a traceable integration boundary, not an overwrite.
