# Decision State Machine — Adversarial Transition Cases 092

**Status:** Proposed source-aligned validation specification, **NOT EXECUTED**; no PASS, deployment claim, or new constitutional authority. Dated 12 October 2026.

## Sources and source-priority

- `../Integration/Decision_Event_Boundary_Source_Limited_Review_018.md`: authorial decision identity, immutable completed events, event-driven branching and provisional Mermaid flow.
- `../Integration/Decision_Validity_and_Interface_Gates_006.md`: competence/forum/participation/result gates; later authorial transition matrix supersedes its original full-occupancy quorum assumption.
- `../Integration/G03_Outcome_Determinacy_Deferred_and_Provisional_Vote_Authorial_Direction_048.md`: two matching official ballots determine result; third ballot provenance, not legalisation.
- `Triadic_Expansion_Mechanism_Separation_Test_011.md`: expanded constituent resultant fills **one** original position; no pooled votes; emergency priority does not confer voting authority.
- `Origin_Included_Unique_Position_Resolution_013.md`: one Steward occupies at most one voting position across the entire decision, including nested stages.
- `../Sections/Section_03_Chapters_21-30_Subsection_Integration_Draft_004.md`: emergency timing independent of a paused Civilisation Clock; independently lawful immediate protection need not be triadic.

The older Test 011 I08 and Gate 006 worked example that leave two-matching-vote quorum unresolved are retained as historical test-source provenance; they are superseded on that **specific** issue by later authorial contextual-quorum direction. All other authority, identity and forum gates remain.

## Proposed state dimensions

Track **decision ID**, decision lifecycle, each official position's accepted vote, cross-constituent Steward identity, independently sourced appointment/expansion mandate, substantive F/A/U result, provenance completeness, host action IDs and execution states, and the host's current authority/time conditions. These are separate dimensions; an incomplete third-position provenance record does not reopen a fixed result.

## Negative and positive adversarial fixtures

| Case | Input event and state | Expected invariant / transition |
|---|---|---|
| D01 | Two authenticated distinct official positions vote F/F under same valid decision ID; third absent | Determine F once, without third-occupancy legality gate; mark third provenance outstanding |
| D02 | Third Steward later votes A after D01 result fixed | Append lawful provenance only; never reverse F or repeat resultant action |
| D03 | Repeat identical first Steward ballot after its position transitioned | Return already-recorded receipt or reject; no second counted vote |
| D04 | Two simultaneous ballots for same Steward position, one F and one A | At most one atomically accepted transition; other conflict/rejection; never two official votes |
| D05 | Two simultaneous matching ballots for different authorised positions | Exactly one fixed majority transition, no duplicate decision commit |
| D06 | Split F/A and unavailable third position, **no** expansion/substitute mandate | Stay unresolved/pending; no automatic authority or artificial majority |
| D07 | Split F/A, separately authorised expanded triad for third position, three distinct eligible constituents vote A/A/F | Exactly one third-position A resultant; receiving F/A/A yields A; no pooled constituent votes |
| D08 | Expanded constituent forum returns F/F/F but its appointment/mandate absent | Withhold operative third-position resultant regardless of arithmetic |
| D09 | Steward occupies a receiving position and is reused within an expanded constituent triad of the **same** decision ID | Reject repeated participation across the complete decision graph |
| D10 | Shadow/parallel Steward offers advice but has no official position appointment | Advice/provenance only; never official vote |
| D11 | Lawfully appointed bounded temporary Steward votes within mandate, original returns later | Only one authorised ballot for that position; handover does not produce fourth vote or reopen completed decision |
| D12 | Conflict-recused Steward is treated as merely absent and automatically replaced | Reject invalid route; require applicable conflict-specific authorisation |
| D13 | Completed action command replayed under same decision/action IDs | No second execution; idempotent recorded result or rejection |
| D14 | One decision legitimately authorises two **distinct** actions A1 and A2 | Each distinct action can transition once; A1 replay cannot block A2 or rerun A1 |
| D15 | Crash after physical effect but before durable receipt | Mark reconciliation/uncertain state and verify host effect; **do not blindly retry** non-idempotent external act |
| D16 | Decision complete; challenge about same historical issue arrives | New decision ID only with fresh lawful authority; preserve ancestry and original immutable decision |
| D17 | Administrator assigns a new ID to a still-unresolved constituent stage | Reject attempted new independent authority/Steward uniqueness domain; preserve parent decision ancestry |
| D18 | Emergency occurs while variable Civilisation Clock is paused | Independently lawful emergency transition proceeds without waiting for Clock; ordinary pending action revalidates on resumption |
| D19 | Expired emergency/temporary appointment mandate followed by late vote or action | Reject new operative transition; historical provenance may be retained |
| D20 | Two overlapping GTP scales route same decision ID | No additional voting position, decision or action effect from spatial rerouting |
| D21 | Ordinary decision determined F, but host implementation mandate withdrawn before Clock trigger | Preserve historical F; withhold stale action and require separate fresh authority for new action |
| D22 | Automatic immediate life-saving act within independently authorised bounded emergency function | May transition under its own host mandate without requiring triadic ballot; audit and expiry remain mandatory |
| D23 | A/A majority with later expanded third-position F | Original A remains fixed; do not route an unnecessary expanded vote to manufacture another outcome |
| D24 | Duplicate receipt arrives after state changed but before acknowledgement to caller | Return same durable outcome or explicit duplicate status; no new transition |

## Proposed evaluation fields

For each fixture record: decision ID, parent/ancestry ID, incoming event, pre-state, claimed authority source, identity/position set, guard verdict, expected post-state, vote resultant, action ID/state, provenance delta, host timebase, and whether a duplicate effect occurred.

**Acceptance criteria:** no double vote, no duplicate effect, no unauthorised expansion or appointment, no re-opening of historical decisions, no emergency Clock dependency, and no false grant of authority by a mere ID or flowchart. A fixture passes only after a real evaluator or implementation supplies traceable observed evidence. The table is a test design, not test results.

## Outstanding interface contracts

1. Authoritative decision-ID issuance and atomic event/state transition owner.
2. Source-verified lawful triggers for expanded triad, parallel appointment, recusal and optional provisional vote.
3. Cross-constituent protected Steward identity and one-position-per-decision enforcement.
4. Distinct host action identity, durable receipts, uncertain-effects reconciliation and crash recovery.
5. Decision completion, immutable historical handoff, fresh authority activation and linked new instances.
6. Clock-independent emergency event path, mandate expiry and ordinary queued-action revalidation.

**Disposition:** retain in Governance V2.1 Validation until source resolution and actual adversarial execution. Do not promote to constitutional text or claim a tested state machine.
