# Expanded Triadic Governance — Validation and Source Reconciliation 002

**Status:** Development / audit; no canonical amendment.  
**Date:** 11 October 2026  
**Scope:** Confirmed reconstruction 001, V1 Governance Full, pending complete V2 content reconciliation.

## 1. Source status and evidence boundaries

**V1 source verified:** `ACBlainey/Concord/02_Operational_Systems/Governance Full.md`:
- Ch. 2 §2.11: Parallel Stewardship independently reproduces constitutional reasoning, records it before comparison, and remains advisory rather than executive.
- Ch. 12 §12.1: normal three-Steward triad; horizontal expansion including or excluding the originating triad; lowest competent layer; scope-sensitive escalation; expanded field must not automatically centralise.
- Ch. 14 §14.2.15–16: emergency substitute, reduced participation, higher-layer escalation, emergency non-action, and diagnostic treatment of abstention.

**Author-confirmed reconstruction:** originating R surrounded by three edge-adjacent A/B/C; excluded variant A/B/C each cast a constituent three-Steward vote; included variant each constituent group is 2 from A/B/C + 1 from R; three constituent results produce a final virtual triad; six-Steward representation per GTP vertex; recursive mesh potential; local capable authority and differentiated regional decisions.

**V2 reconciliation pending:** The GitHub connector returned empty content for the large V2 canonical file in this pass; its existence and blob SHA were confirmed, but no line-by-line content was retrieved. Do not interpret this as absence of provisions in V2.

## 2. Mathematical specification — normal and expanded voting

Let each eligible Steward's ballot be F, A or U (unresolved/abstention/invalid, with the underlying cause recorded). For a constituent triad with three positions:
- F if at least 2 valid F ballots;
- A if at least 2 valid A ballots;
- U otherwise.

For expanded configurations let g1, g2, g3 be the three constituent results. The virtual triad applies the **same** decision rule to (g1,g2,g3). A constituent U is not silently converted into A. A valid majority A is not equivalent to procedural U.

**Excluded:** g1 = vote(A1,A2,A3), g2 = vote(B1,B2,B3), g3 = vote(C1,C2,C3); R does not vote.

**Included:** g1 = vote(A1,A2,R1), g2 = vote(B1,B2,R2), g3 = vote(C1,C2,R3); exact eligibility and independence rules remain to be specified. This is a structural example, not a permanent allocation of named officeholders.

**Counterexample to flat pooling:** A=F,F,A; B=F,F,A; C=A,A,A. Virtual results F,F,A -> final F; pooled individual results 4F,5A -> A. The two procedures are mathematically different; only the first matches the author-confirmed protocol.

## 3. Core validation cases

| ID | Configuration / condition | Expected invariant or outcome |
|---|---|---|
| T01 | Normal F,F,A | F authorised |
| T02 | Normal A,A,F | A majority; proposed state change not authorised |
| T03 | Normal F,A,U | U, not A |
| T04 | Normal F,F,U | F majority if the abstention is procedurally valid |
| T05 | Excluded A=F, B=F, C=A | Virtual F; no pooling |
| T06 | Excluded A=F, B=A, C=U | Virtual U; not forced A |
| T07 | Included 2A+1R, 2B+1R, 2C+1R | Exactly 3 constituent results; R not a fourth final vote |
| T08 | Origin R conflicts with subject of review | Consider excluded variant; origin's lack of final vote recorded |
| T09 | One authorised Steward absent | Assess delay, authorised substitution, or bounded reconstitution; no silent transfer |
| T10 | Principled abstention | Record reasons; no replacement solely to obtain a desired result |
| T11 | Parallel Steward disagrees with Official Steward | Advisory comparison; no extra vote |
| T12 | Entire constituent triad compromised | Independently assess reconstitution/expansion; do not automatically count as Against |
| T13 | Same individual appears in two mixed constituent groups | Flag possible duplicate influence; eligibility/independence review |
| T14 | Recursive expansion required | Define bounded eligible field, three independent resultant positions, stopping rule and audit |
| T15 | Five regions: 4 evacuate, 1 does not mandate evacuation | No automatic regional 4–1 override of fifth region |
| T16 | One region's flood barrier materially affects neighbours | Assess genuine shared-decision jurisdiction separately from local evacuation choice |
| T17 | Shared hurricane forecast, distinct local policies | Coordinate information/resources without creating centralised policy authority |
| T18 | One region refuses aid but later requests neighbours' scarce resources | Separate resource allocation decision; no retrospective automatic invalidation |
| T19 | Larger GTP scale has lower workload | Scale choice is contextual; spatial parent/child implies no automatic authority hierarchy |
| T20 | Three valid constituent results all A | Virtual A; no authorised proposal change |
| T21 | U,U,F | Virtual U; exceptional path must not manufacture approval |
| T22 | An emergency requires prompt action but no valid authority can be established | Preserve current state where safer; document rights, risks and any lawful emergency route |

## 4. Architecture safeguards requiring precise procedural rules

1. **Scope certificate:** state what is being decided, who is affected, and why the chosen triad or shared field is competent.
2. **Constitutional authority check:** capability, permission and authority are separate; emergency does not manufacture unrestricted authority.
3. **Constituent eligibility:** office and individual eligibility, six-Steward vertex relationship, conflicts, independence and duplicate representation.
4. **Parallel versus substitute:** parallel assessment is advisory; only separately authorised succession confers a vote.
5. **Abstention semantics:** distinguish evidence insufficiency, recusal, nonparticipation, conflict and invalid ballot; do not count all as rejection.
6. **Reconstitution trigger:** necessity and objective grounds, never dissatisfaction with the decision's direction.
7. **Finite expansion:** explicit stopping conditions, time bounds and non-action/continuity outcomes; no expansion-until-approval.
8. **Audit record:** original triad, spatial addresses, constituent selections, individual ballots as appropriately protected, three resultant votes, final decision, minority reasoning, authority and sunset.
9. **Local autonomy:** multi-region shared circumstances do not imply one binding aggregated vote; test externalities and rights.
10. **No spatial hierarchy:** GTP scale labels describe resolution, not inherent command relationships.

## 5. Findings and next development order

**Supported:** The two reconstructed variants are mathematically well defined when all constituent votes have valid majorities. V1 supplies conceptual foundations for expansion, parallel review, substitutes and local competence.

**Not yet established:** Detailed six-Steward vertex-to-office allocation; selection permutations; authoritative substitution triggers and appointing mechanism; recusal and abstention resolution; expansion termination; cross-region consent and externality threshold; full V2 source consistency.

**Next actions:** (i) source-resolve V2 via smaller retrievable sections or repository snapshot; (ii) build a decision-state machine and exhaustive finite vote tests; (iii) draft bounded selection/substitution procedure; (iv) adversarially test capture, deadlock, coercion and emergency misuse; (v) graduate only validated material. Preserve Reconstruction 001 unchanged.
