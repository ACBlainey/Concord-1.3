# Governance V2.1 — Decision Validity and Interface Gates 006

**Status:** DEVELOPMENTAL SPECIFICATION ONLY. This document identifies unresolved conditions; it does not establish a new constitutional power, quorum, office or eligibility rule.

## 1. Separate the four stages

1. **Competence gate:** Identify the constitutional source of authority over the exact question, rights, resources, participants and affected jurisdictions. Distinguish local decision, nonbinding coordination, lawful common competence and independently authorised emergency preservation. GTP adjacency, scale or workload alone never passes this gate.
2. **Forum gate:** Identify the correct decision class and whether the ordinary triad, an authorised expanded virtual triad, a legally established federal institution or a specialised emergency body is empowered to decide. No change of forum merely to reverse an unwanted outcome.
3. **Participation gate:** Verify every position's identity, appointment, eligibility, independence, conflicts, recusal and applicable quorum. Abstention, absence, invalid authentication and vacancy must be distinct states. An origin-included virtual triad is **not deployable** until repeated R participation and six-Steward vertex roles are specified.
4. **Result gate:** Only after the preceding gates pass may F/A/U arithmetic establish a decision. In each valid constituent triad, 2+ F→F; 2+ A→A; otherwise U. Apply the same rule to the three constituent resultants. No nine-ballot pooling. An arithmetic F or A with an invalid preceding gate is **not a legally operative decision**.

## 2. Non-operative decision-state proposal

| State | Meaning | Permitted next step |
|---|---|---|
| Not authorised | No lawful jurisdiction, common competence or valid forum | Return to competent body or obtain valid authorisation; no binding decision |
| Awaiting constitution | Authority may exist but membership, appointment, independence or quorum not verified | Correct the forum; no vote taking legal effect |
| Deliberating | Valid forum; evidence and positions under review | Record F/A/U and reasons |
| Unresolved (U) | Valid forum without an applicable substantive majority | Gather evidence, defer, seek legitimate review or use separately authorised emergency route |
| For (F) | Valid forum and sufficient F resultants | Act only within authorised scope |
| Against (A) | Valid forum and sufficient A resultants | Do not treat the decision as a vacancy or emergency deadlock |
| Expired / withdrawn | Previously authorised power no longer valid | Stop action unless renewed by independent lawful process |
| Review / challenge | Outcome or procedure contested through valid route | Preserve records, apply lawful suspension and remedy rules |

**Important:** “Not authorised” and “Awaiting constitution” are **not** the same as a valid forum's U result. They must not be collapsed into one outcome.

## 3. Open design decisions for author review

**G-01 — Six-Steward vertex map.** Precisely identify each of the six positions at a GTP vertex, the triangle-office relation and the independence and representation implications. No inference from geometry alone.

**G-02 — Origin-included repetition.** Determine whether the same R Steward may appear in several constituent mixed triads, how correlated influence is constrained, and whether the repeated votes should be treated as independent. Preserve the three-resultant architecture; do not invent extra votes.

**G-03 — Quorum and procedural invalidity.** Define quorum for ordinary triads, each constituent triad and the virtual resultant; treatment of recusal, conflict, failed authentication and temporary unavailability; and whether F/F/U may be legally operative under each decision class.

**G-04 — Common-competence instrument.** Specify who may authorise a binding cross-jurisdictional question, affected jurisdiction consent and rights, shared resources, limits, record, expiry and review. Mere four-of-five regional agreement cannot override an independent fifth jurisdiction.

**G-05 — Emergency preservation.** Define independently authorised harm threshold, minimum necessary action, expiry, restoration, appeal, audit and remedies. U does not automatically activate emergency authority; A does not convert into U merely because the result is undesirable.

**G-06 — Operational hysteresis.** Define workload measurement, subdivision and consolidation thresholds, persistence windows and independent review. These are staffing and coverage rules, not constitutional jurisdiction rules.

## 4. Worked gate cases

- **A=F/F/A, B=F/F/A, C=A/A/A:** arithmetic final F; legal decision only if common competence, forum and participation gates pass.
- **A=F/F/U, B=F/F/U, C=F/A/U:** constituent F/F/U → arithmetic F, subject to all gates.
- **Two Stewards agree while third is absent:** arithmetic majority alone does not prove quorum; apply independently established degraded decision rule.
- **Five regions, four want evacuation in fifth:** no authority to command the fifth unless a valid common constitutional competence specifically covers that evacuation.
- **Parallel Steward appointed by no one:** advisory only; cannot occupy a vacant voting position by virtue of advice.
- **An unresolved emergency:** preservation requires separately valid powers; cannot infer an emergency appointment from U.

## 5. Review and graduation

The purpose of this interface is to keep **CAP ≠ PERM ≠ AUTH** visible: practical capability, permission and lawful authority are distinct. This document supplies diagnostic gates, not permission to act. All open decisions require source resolution, testing, explicit approval and provenance before incorporation into any binding text.

Original Governance V2 Canonical unchanged.


## Later authorial source-priority correction — event-driven state machine (12 October 2026)

This 006 developmental document predates the author's subsequent decisions. Its **four gates** (competence, forum, participation, result) remain useful; however its statements that a two-matching-vote majority requires a separate three-occupied/degraded quorum rule, or that a completed decision may be reopened through a generic review state, are **superseded**. Quorum is contextual: two independently valid matching official Steward votes in the legitimate decision instance determine F/A without waiting for a third occupied position. The third ballot is informational provenance. A completed state-machine decision is immutable history; a later appeal, remedy, challenge or renewed consideration is a **new uniquely identified decision instance** with freshly activated authority, not a return to deliberation under the old ID. See Integration 018 and 048.

### Provisional event/guard/transition matrix — no new constitutional authority

| Current state | Event | Required guard | Transition / effect |
|---|---|---|---|
| Created | Authority validation | Competence, forum, contextual mandate and legitimate participation established | Open voting under unique decision ID; otherwise hold/reject without a vote |
| Voting open | First valid position ballot | Authenticated eligible official Steward; correct decision ID and position; no prior accepted ballot for that position | Atomically record ballot and updated position state |
| Voting open | Matching second valid ballot | Two distinct authorised official positions; same decision ID and current valid context | Atomically fix F/A result; third-position ballot no longer changes substantive outcome |
| Voting open / unresolved | Split, U or missing decisive position | No matching valid majority yet | Remain pending; consider separately authorised continuation routes, not an automatic new mandate |
| Voting open / unresolved | Steward absence or conflict | Actual event classification, eligible authorised route and position exclusivity | Await, initiate authorised expanded constituent vote, or activate lawfully appointed bounded parallel replacement; otherwise hold |
| Constituent expanded vote | Constituent resultant returned | Independently authorised expansion; one-resultant-for-one-position; unique Steward participation within the whole decision | Record exactly one original-position resultant; re-evaluate same decision ID |
| Any nonterminal voting state | Duplicate or stale vote | Same ID/position already transitioned, or invalid mandate | No second vote or state effect; record duplicate receipt or reject |
| Determined | Ordinary implementation trigger | Applicable variable Clock transition and revalidated host authority | Initiate lawful host action without re-voting |
| Determined | Lawful urgent implementation trigger | Independent emergency/urgent host mandate, not merely the vote | Initiate bounded host action without waiting for Clock |
| Action pending | Resultant action receipt / retry | Distinct action identity; host-owned state; atomic durable idempotency | Complete each authorised action once; duplicate delivery causes no repeat consequence |
| Completed | Late third ballot / evidence | Historical provenance permission | Append provenance without changing fixed result or replaying action |
| Completed | Appeal, new evidence, remedy, changed circumstances | Independently lawful fresh decision mandate | Create new unique decision instance with ancestry link; historical event remains unchanged |

**Orthogonal states:** substantive result, provenance completeness, position availability, host action execution and Clock timing must not be collapsed into one status. A decision can have an F/A majority while its third-position provenance remains outstanding, and its lawful action can be awaiting an ordinary Clock trigger. Parallel Stewards can provide advice without an official ballot; an expanded vote is not automatically triggered by any vacancy. State-machine triggers **route** only to existing authorised procedures. CAP ≠ PERM ≠ AUTH.

**Validation still required:** precise host state/event definitions, real appointment/expansion authority, concurrent atomic vote and action receipts, constituent identity across nested expansion, cancellation/expiry, and paused-Clock emergency transitions. This is a source-aligned developmental matrix, not a tested executable state machine.
