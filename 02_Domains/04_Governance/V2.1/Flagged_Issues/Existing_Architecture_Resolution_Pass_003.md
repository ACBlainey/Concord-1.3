# Existing Architecture Resolution Pass 003 — Transition, Continuity, Disclosure and Knowledge

> **Registry-ID correction (14 October 2026):** Issue-number groupings in this early source crosswalk were assigned before reconciliation against the saved 83-row registry and **must not be used as authoritative FI mappings**. Match by the issue *title* and the source's substantive topic, then use the verified FI numbers in `Flagged_Issues_Registry.md`. A corrected thematic mapping is maintained in `Verified_Source_to_Issue_Map_004.md`. The underlying source paths and quoted module clauses remain useful; no issue closure is implied.


**Date:** 14 October 2026  
**Method:** Direct examination of numbered clauses in eight Concord portable modules; this is source resolution, not an implementation test or constitutional adoption.

## Source-derived findings

| FI numbers | Existing source and clause | Architecture already available | Residual governance-specific work |
| --- | --- | --- | --- |
| FI-004, FI-005, FI-022, FI-050 | `04_Portable_Modules/Bounded Transition Architecture — Portable Module v1.0.md` §§10, 12, 17, 19 | Unresolved transitions must identify owner and cannot silently count as completed; explicit non-propagation of authority, permission and consent; surviving duties; failed partial crossings and residual effects | Governance vote/effect IDs, owner acceptance protocol, partial-effects remediation and constitutional review competence |
| FI-004, FI-018, FI-024 | `04_Portable_Modules/Concord Bounded Participant Runtime — Portable Module v1.0.md` §§11, 13 | Revalidate credential, target, grant, consequences, dependency and authority at consequential commit; represent COMMIT_STATE_UNKNOWN instead of retrying blindly | Deployable host semantics, idempotency and independent owner evidence |
| FI-002, FI-003, FI-050 | Same CBPR source §21; `04_Portable_Modules/Fault-Tolerant Accountability and Responsibility Continuity — Portable Module.md` §§9–13 | Infrastructure recovery does not transfer authority; successor eligibility without trigger is not activated power; duties can outlive spent authority; absence of qualified successor leads to bounded safe state | Lawful successor eligibility, activation event, exceptional restoration and safe-state owner |
| FI-017, FI-022, FI-023, FI-039, FI-054 | `04_Portable_Modules/KCS Change Propagation — Portable Module.md` §§16, 20, 24 | Corrections preserve earlier state, traverse material dependencies and generate review, not automatic reversal; dependency is not subordination; graph visibility is purpose-bounded | Historical/KCS object links, owner-triggered reviews, visibility controls and dispute handling |
| FI-013, FI-050, FI-051 | `04_Portable_Modules/Lifecycle Stewardship Review — Portable Module v1.0.md` §§8, 15–16 | Distinguishes need for function from justification for current institution; LSR does not grant power to continue, terminate or appoint; residual remediation and record duties remain | Actual mandate expiry, participant remedy, constitutional competence and successor authorisation |
| FI-018, FI-023, FI-024, FI-025, FI-026, FI-048 | `04_Portable_Modules/Private Local Evaluation — Portable Module v1.0.md`, “Cumulative disclosure”, “Cross-recipient composition”, “Failure behaviour” | Individually safe outputs can combine into unsafe disclosure; known recipient collusion matters; protected queries fail toward bounded refusal/review on unknown authority | Requester classes, aggregate-risk policy, appeal and privacy-preserving disclosure state |
| FI-018, FI-023, FI-024, FI-026, FI-048 | `04_Portable_Modules/Concord Information Black Box Portable Module v1.0.md` §§12–13, 16–17 | Individually permitted operations do not authorise their composition; protected disclosure-state, restore is a workflow, authentic backup does not imply current operational authority; emergency scope/expiry are bounded | Protected-master custodian, section-specific wrapper, restoration approval and independent audit |
| FI-032, FI-034, FI-050 | `04_Portable_Modules/State and Maturity Mapping — Portable Module v1.0.md` §§6–16, 23–26 | Context-relative maturity, sufficiency, blockers and state transitions without universal maturity score; potential workload/capacity observation grammar | GTP-specific workload hysteresis thresholds and non-hierarchical allocation rules |

## Consolidation implications

**Already established general principles:** no propagation of authority through state transfer, continuity or backup; review triggers do not decide outcomes; evidence correction does not automatically revoke a committed vote; owner-independent effect confirmation; function does not imply perpetual institution; cumulative privacy risk must be considered across outputs.

**Still genuinely open:** actual Governance authority issuers, jurisdictional conflict settlement, lawful replacement Steward selection, independent review/remedy owners, host integration guarantees, emergency timebase enforcement, and GTP dynamic mesh calibration. These are not solved merely by adopting the portable modules.

## Recommended implementation sequence

1. Resolve FI-004 with BTA + CBPR + MKA + Historical/KCS as **separate existing owner interfaces**, keeping vote commitment irreversible and effects independently accountable.
2. Resolve FI-005/FI-007 with STRA + MKA + BTA, but separately test the emergency state machine's wall-clock responsiveness and lawful owner.
3. Resolve FI-002/FI-003/FI-050 using fault-tolerant succession, CBPR and LSR without converting eligibility or continuity into active authority.
4. Resolve FI-018/FI-023/FI-024/FI-048 with CWA/CIBB/Private Local Evaluation and Historical projections, avoiding a new universal surveillance layer.
5. For FI-032/FI-034, use SMM as observation input only; geometry, workload and legitimacy remain distinct.

No FI status is marked closed by this source-resolution pass.
