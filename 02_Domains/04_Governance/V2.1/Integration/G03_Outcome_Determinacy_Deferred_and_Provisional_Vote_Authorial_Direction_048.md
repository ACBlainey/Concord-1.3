# G-03 — Outcome Determinacy, Deferred Participation and Provisional Vote Supersession 048

**Status:** New AUTHORIAL DIRECTION, provisional development record. Supersedes the proposed full-three-occupied default in Integration 047 as the preferred assumption for further design. Does not amend original Governance V2 Canonical.

## Authorial observation

If two valid original Steward positions cast the same F or A vote, the remaining position cannot change that substantive majority. Requiring its immediate occupation for every consequential decision may unnecessarily stall governance. The missing Steward's eventual vote can still matter materially for **provenance, dissent, reasoning, accountability and review**. Therefore **outcome determinacy and record completeness are distinct dimensions**.

This observation does **not** establish that any two ballots automatically confer legal authority. Competence, forum, independently established participation/continuity procedure, identity, decision boundary and commit-time validity remain separate gates.

## Four authorised continuity paths for an unavailable Steward

1. **Deferred original vote:** record two valid matching votes and await the missing Steward's later official ballot. The substantive majority is determined, but record completeness remains pending. A decision's operational status before completion must be explicitly defined.
2. **Expanded decision:** where separately authorised, an expanded constituent triad may provide the missing **one original position's** resultant, conserving its vote weight and enforcing full-event Steward uniqueness.
3. **Parallel temporary Steward:** an eligible independently authorised replacement temporarily fills the unavailable position. Authority is bounded and expires or is relinquished when the original returns under an established handover rule.
4. **Provisional position vote:** a temporary authorised vote is recorded for the absent Steward's position, marked **PROVISIONAL**. On return, the original Steward may cast their own **OFFICIAL** vote, which **supersedes the provisional position vote in the authoritative voting record**. The provisional vote remains preserved in immutable provenance history, not erased or counted as a fourth vote.

These are distinct alternatives, not automatic powers. A material-conflict recusal is not equivalent to ordinary absence; a disqualified Steward cannot regain the position simply by returning. Insufficient-information abstention remains distinct from vacancy.

## Important consequences

- **Two matching F or A votes:** substantive outcome is invariant to the third position's later F/A/U, assuming the two votes are valid and the applicable procedure permits action.
- **Split F/A or otherwise indeterminate ballots:** the missing position may determine the outcome. The system cannot claim outcome determinacy and may need to wait, substitute or apply an authorised expanded mechanism.
- **Provisional supersession:** the later official vote replaces the temporary position vote as the current authoritative ballot, but does **not** retroactively delete the earlier provisional record or automatically unwind actions previously authorised. A separate review/remedy process may be necessary.
- **One position / one current ballot:** original, substitute, expanded resultant and provisional votes must not be simultaneously counted for the same position. Supersession is an explicit state transition with timestamps, authority source and audit trail.
- **Time boundary:** the return deadline, finalisation rule and effect of an original Steward who never returns require authorial specification. A pending provisional state must not confer indefinite temporary authority.
- **No invented authority:** a provisional vote does not create a new jurisdiction, quorum, emergency mandate or implementation power.

## Proposed compact state model

`POSITION_PENDING` → `PROVISIONAL_POSITION_VOTE` → `OFFICIAL_POSITION_VOTE` → `POSITION_FINALISED`

Alternatively a lawful temporary replacement or expanded resultant can fill the position under its own mandate. A record may separately carry `OUTCOME_DETERMINED` or `OUTCOME_UNDETERMINED` without falsely declaring complete provenance.

## Open authorial decisions, deliberately limited

1. When two matching votes make the outcome mathematically invariant, may the decision be **operative before** the third official vote, and under which ordinary safeguards?
2. How long can an original Steward supersede a provisional vote, and what happens after irrevocable external consequences?
3. Can the returning Steward change only the official ballot/provenance, or also trigger a distinct lawful reconsideration of the already committed decision?
4. Which temporary path is preferred for ordinary absence versus conflict recusal, and what is the handover rule?

## Relationship to earlier work

- Integration 047's full-constitution default is **not adopted**; this authorial direction requires a more flexible quorum model.
- Chapter 12 Candidate 012 and Chapter 132 Candidate 010 remain unchanged pending resolution of operational timing.
- The node-ring mechanism and expanded triad rules remain valid as possible one-position substitutes; this note does not require additional GTP permutation testing.
