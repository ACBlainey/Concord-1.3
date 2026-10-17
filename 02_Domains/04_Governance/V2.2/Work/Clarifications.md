# Governance V2.2 — Authorial Clarifications

These are the author's clarifications supplied during the V2.2 Section 01 review. **Use this file as a cross-section comparison reference when examining every V2.2 section.** Compare each section's architecture against every applicable clarification, identify missing rules, inconsistencies, duplicate formulations and unresolved interfaces, and incorporate necessary additions **without condensing, compressing, abridging, silently editing or deleting existing architecture**. Preserve conflicts and unresolved issues explicitly for later resolution. Do not assume a clarification has been fully implemented merely because it appears in one section.

This is a reference for integration and checking, **not** an independent grant of governance authority or a replacement for the full section text. Cross-references below identify initial additions to Section 01, not an exhaustive verification of the rest of V2.2.

## C01 — Preserve all source architecture during integration

- Combine the existing Section 01 and its companion integration draft in full, preserving all substantive architecture, including apparent duplication, conflicting statements and unresolved issues.
- Do not condense, compress, abridge or silently edit source material.
- First produce the complete combined material; only then check for duplication, conflicts and unresolved issues. Keep all findings visible until addressed.
- Apply the same preservation and comparison approach to each subsequent V2.2 section.

## C02 — Fixed vote instances and separate subsequent decisions

- Every vote is fixed once committed. Its official ballots and historical result cannot be edited, withdrawn, revoked or retrospectively rerun.
- The same issue may be decided again, but this is a **new, separate decision event** with a **new unique identifier**, not a redo or reopening of the original vote.
- A subsequent decision can change the operative policy or outcome within its own lawful authority without rewriting the original decision record.
- Distinguish a unique decision-event identifier from the version of a policy or rule produced by that decision.
- Initial Section 01 integration: §9.37.1.

## C03 — Lowest competent decision scale

- All decisions should be made at the **lowest possible competent and lawfully authorised level**.
- Some decisions exceed the competence or scope of ordinary local stewards. Illustrative categories include wide-area effects, high-security matters, Concord-wide questions and presently unforeseen types.
- Such a matter may need to be passed to a **larger GTP spatial scale** so that a decision can cover all affected smaller GTP areas.
- GTP is a conceptual spatial mesh, **not a governance hierarchy**. Larger spatial levels are available for decision-making without creating inherently superior stewards.
- We cannot yet specify exhaustively what decisions require this treatment, how competence will be determined, or how referral will work. Keep this as an outline with design questions explicitly open; do not invent binding thresholds.
- Initial Section 01 integration: §9.20.1.

## C04 — Higher-scale authority is singular and event-bounded

- A decision made at a larger GTP scale is a **singular event**, confined to its specific matter and scope.
- It confers **no authority over any other decision**, no standing regional control and no power to approve or override unrelated ordinary triad decisions.
- All other decisions continue at their normal competent triad level.
- **Ordinary expansion of voting is the distinct exception/mechanism** to consider separately; expanded voting does not itself create a permanent higher governance tier.
- Initial Section 01 integration: §9.20.2.

## C05 — Higher-scale steward composition and aggregation are undecided

- The exact makeup and number of stewards for larger-scale decisions remain to be determined. These votes may include **substantially more than three stewards**.
- One possible composition includes all lower-level GTP-area stewards whose regions are affected.
- Possible counting arrangements include aggregation into a larger triadic result (as in expanded voting), **or direct aggregation of many individual votes**. Example only: 30 stewards vote, 20 For and 10 Against.
- The examples are **possibilities, not adopted procedures, mandatory composition rules or fixed thresholds**.
- Do not silently apply the ordinary three-steward voting process to every larger-scale event, nor treat these possibilities as permission to change ordinary triad voting rules.
- Any adopted larger-scale procedure will need its own lawful constitution, eligibility, authority bounds, aggregation/completion rules and event records.
- Initial Section 01 integration: §9.20.3.

## C06 — Emergency authority coexists with ordinary governance

- Emergency systems and emergency authority **do not displace, suspend or take over** stewards' ongoing normal duties and contextual bounded authority.
- Emergency authority has effect **only for the emergency** and within its legitimate emergency scope.
- No external party or emergency actor may enter a region and assume control of its ordinary governance functions merely because an emergency has occurred.
- Ordinary and emergency functions can operate simultaneously; interaction must remain limited to actual emergency necessity and must not transfer general governance control.
- Emergency provisions must not provide a route to institutional takeover, capture or a coup.
- Initial Section 01 integration: §9.40.2.

## C07 — Extreme existential-crisis exception

- **Only an extreme existential crisis** may justify temporarily setting aside daily ordinary governance where its continuation is incompatible with survival, continuity or defence.
- Illustrative circumstances include an enormous disaster, black-swan event or war posing an existential threat.
- The event's label is not sufficient by itself: actual existential necessity matters.
- Interruption is confined to affected functions, areas and duration. Unaffected normal governance continues, and ordinary functions must resume when the exceptional necessity ends.
- This is not automatic sovereignty transfer or an unrestricted takeover power.
- The precise crisis threshold, lawful authorisation route, safeguards and restoration mechanism are **not yet determined**; retain these as open design questions rather than inventing powers.
- Initial Section 01 integration: §9.40.3.


## C08 — Meetings, groups and actions cannot acquire authority

- **No meeting, action or group can acquire authority** through assembling, discussing, voting, reaching consensus, recording minutes, coordinating or acting.
- Authority must be **separately and lawfully constituted**, contextual and bounded; it cannot emerge from the activity itself. Distinguish lawful exercise of an existing bounded authority from supposed acquisition of authority by an event.
- Check the dedicated **bounded contextual authority** and **state-machine** architecture: lawful steward selection and decision-state guards do not mean that the meeting or state machine manufactures authority. Official voting consumes the bounded authority of the steward position at commitment.
- Conference, emergency coordination, ordinary expanded voting and larger-GTP decision arrangements cannot create general or superior authority through aggregation or participation.
- Apply **CAP ≠ PERM ≠ AUTH** and preserve separate execution-system authority.
- Initial Section 01 integration: §9.41.1. Exact state-machine and authority source interfaces must be checked during further integration.

## Cross-section review procedure

For **each** V2.2 section:

1. Read the entire section and compare its relevant rules against **C01–C08**, including cross-references to other sections.
2. Identify any missing clarification, inconsistent architecture, unintended implied hierarchy, unauthorised authority transfer, ambiguity or unresolved interface.
3. Preserve existing text and conflicts; add the necessary clarification in the relevant numbered subsection without silently deleting or rewriting source passages.
4. Do not convert undecided mechanisms into fixed rules. Record exactly what remains to be designed.
5. Retrieve the saved section from GitHub and verify the intended additions and preservation of prior content.
6. Revisit this file when the author supplies further clarifications, and apply them to subsequent section reviews.
