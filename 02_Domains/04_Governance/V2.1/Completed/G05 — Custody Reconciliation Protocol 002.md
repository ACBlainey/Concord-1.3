# G05 — Custody Reconciliation Protocol 002

**Status:** V2.1 integration candidate; not canonical and not a deployed authority service.

## Problem
Stage 088 demonstrates that BTA continuity duties (081), succession records (082) and orphan referrals (083) may truthfully disagree because they are separate owner-controlled projections. A transfer committed in one ledger is not proof that every other record has changed. No single G05 coordinator may silently rewrite all three.

## Protocol boundary
1. **Evidence intake:** identify duty ID, origin BTA transition, previous custodian, proposed successor, event ID, source and expected revisions, and independent owner/successor evidence references. Keep beneficiary identities within contextual access wrappers.
2. **Owner-issued transition:** the competent domain owner determines whether custody may transfer. Succession evidence is not a self-issued mandate; an audit/coordination service cannot make the decision.
3. **Reconciliation check:** compare live duty, succession and orphan records for matching identity, transition provenance, revisions and open obligation state. Check externally verified issuer and successor attestations. Stage 089 provides only this *candidate* comparison.
4. **Bounded projection updates:** each owning service may independently accept an authenticated reconciliation event, perform a compare-and-swap revision check, and record its own acknowledgement. No coordinator directly mutates another owner's source record.
5. **Partial delivery:** if one projection remains stale, report **PENDING_RECONCILIATION**, not success or extinguishment. Preserve an event log, retry safely with idempotency, and flag conflicts to Civil Contact/Continuity as appropriate.
6. **Resolution:** only after independent acknowledgements may a cross-system view say projections agree. That is still not proof that the underlying obligation was discharged.
7. **Dispute and revocation:** contested, superseded or revoked attestations require a fresh owner review; previously issued evidence is preserved for Historical, subject to privacy wrappers.
8. **Emergency separation:** a temporary protective mandate cannot be treated as successor acceptance or permanent custody. Expiry creates audit and follow-up duties, not implicit reassignment.

## Negative invariants
- **CAP ≠ PERM ≠ AUTH.** Reconciliation verifies consistency; it cannot create mandate.
- **GTP is a spatial mesh.** No governance hierarchy or custody inheritance from finer/coarser spatial resolution.
- **BTA owns transition semantics.** A reconciled projection does not declare BTA complete.
- **KCS signals stale dependencies, not authorisation.**
- **SMM describes state, not permission.**
- **Civilisation Clock pauses do not freeze emergency expiry.**
- **Historical provenance and protected beneficiary data remain owner-governed.**
- **No automatic closure, no automatic orphan deletion, no automatic authority.**

## Evidence and limits
- Stage 088 cross-stage test (12 tests) demonstrated that independent ledger states remain inconsistent after a succession transfer; this is a real **prototype interface gap**, not evidence of deployed system failure.
- Stage 089 checks a proposed reconciliation event against three existing fixture ledgers (18 tests). Its verification inputs are caller-provided booleans, not cryptographically verified attestations; it makes no writes and cannot prove real-world authority.
- Future validation: tamper-evident event signatures, authenticated owner services, transactional/idempotent acknowledgements, conflict handling, privacy-safe public projections, concurrency tests, revocation and replay resistance, complete BTA/KCS interface contract tests.

## Governance incorporation
This protocol is a **modular Governance V2.1 companion** to `G05 — Bounded Governance, Continuity and Recovery Integration 001.md`. Its constitutional owner, source references and applicable Governance chapter patches must be resolved before graduation. Preserve `../Governance V2 Canonical.md` unchanged.
