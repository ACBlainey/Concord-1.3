# Voting as an Abstract Contextual Wrapper — Cross-Module Source Review 014

**Status:** Provisional architectural synthesis. Source claims below are distinguished from proposed voting application. No canonical or portable module amended.

## Primary source documents inspected

1. `04_Portable_Modules/Minimum Necessary Capability — Portable Module.md`, blob `c37c86925bcde1a1ac58bb56723d18e62ca23143`, v0.2 Level B candidate, graduation review required.
2. `04_Portable_Modules/Concord Bounded Participant Runtime — Portable Module v1.0.md`, blob `47300fac3c771fa5f0408f12863b131b3eb65a15`, graduated portable module, implementation validation outstanding.
3. `04_Portable_Modules/Concord Information Black Box Portable Module v1.0.md`, blob `9ee989c6e7961f036bceb4d6888ef04e556722d5`, graduated portable module, specification-level transfer validated.
4. `04_Portable_Modules/Contextual Trust Progression — Portable Module v1.0.md`, blob `1def82a270f2d8f48d7d6c102b727dc8694c3b4e`, graduated module.
5. `04_Portable_Modules/INDEX.md` and `README.md` for maturity/provenance. The specific file `04_Portable_Modules/Contextual Wrapper Architecture — Audit 001.md` was **not found at that path**; do not claim it was reviewed.

## Source-supported cross-module rules

**MNC §§1–3, 12, 15–16, 19, 24:** Purpose→Function→Need→Minimum Sufficient Capability→Bounded Exercise→Review→Termination/Re-Justification; multidimensional bounds; local and aggregate capability differ; formal authority and effective power differ; expiry and escalation require justification. MNC is not an independent source of legitimacy.

**CBPR §§2, 8–14:** CAP != PERM != AUTH; an AuthorityBasis is independently supplied; authority evidence is not authority; a credential's presence is not permission; material consequences require commit-time revalidation; composed authorised parts do not automatically authorise their combination; uncertain commit state is not permission to blindly retry.

**CIBB §§2–7, 12, 15, 20, 24:** Context-specific projections and protected operation boundaries; authorised operations do not automatically authorise their composite; workflow authority is not general plane authority; containment does not imply authority inheritance; externally supplied authority states are consumed, not created by the wrapper. CIBB is an **information-governance** module, not already a voting protocol.

**CTP §§1–4:** Evidence != Permission; evidence relevance does not itself authorise exposure transition. This is useful for eligibility and appointment evidence, but does not itself create voting authority.

## Proposed synthesis: vote as an abstract contextual wrapper

A voting event may be modelled as a bounded, temporary **decision context**, or abstract wrapper. This is a **new proposed application** of the cross-module rules, not an existing claim that CIBB itself implements voting.

Wrapper instance `VoteContext(D)` contains:

- **Identity:** decision ID, defined vote-event scope, decision question and version.
- **Authority basis:** externally legitimate mandate for the particular decision, including lawful forum, position and consequence scope.
- **Entry:** eligibility, appointment, distinct-person identity across the entire vote tree, independence, quorum and conflicts.
- **Capability grant:** exactly one Steward-occupied position per person per decision; a constituent triad collectively resolves one substituted position.
- **Operation:** one authorised vote per occupied position; abstention, recusal, invalidity and unresolved result are not interchangeable.
- **Composition:** every constituent triad emits **one resultant**, and the receiving triad accepts only its three positions. Neither nine-ballot pooling nor repeated Steward participation is authorised.
- **Commit:** revalidate identity, authority, quorum, scope, expiry, composition and consequence immediately before accepting the result as operative.
- **Exit:** terminate vote-specific authority after the event; retain a protected audit record without treating that record as continuing authority.
- **Aftermath:** implementation, enforcement, review or subsequent decisions require their own legitimate basis. A completed vote's consequence may persist while the vote-specific authority does not.

## Crucial distinction: ephemeral authority versus persistent decision consequences

**Authority to cast or jointly resolve a vote expires with that vote.** The decision outcome, however, may have continuing legal or operational effects if separately supported by the applicable governance framework. Expiry of voting authority does not automatically reverse a valid past decision, and a valid decision does not automatically grant its voters continuing implementation authority.

This follows the author's clarification plus the source modules' temporal and consequence distinctions; it is not a verbatim portable-module clause.

## Nested-wrapper interface

A constituent triad can be represented as a nested voting context whose output is a signed/auditable resultant for exactly one receiving decision position. The receiving context must verify the constituent's authority and validity, rather than inherit authority merely because it is nested. The same Steward may not occupy any other Steward position anywhere in the same decision tree. A propagated resultant is a record/output, **not a second vote by a person**.

## Failure and adversarial tests to run

- A technically available vote credential lacks a current AuthorityBasis → reject.
- A Steward is appointed to two nested/parallel positions within the same decision → reject entire unreconstituted forum.
- A valid constituent vote is submitted after its decision-bound expiry → reject/revalidate, do not extend implicitly.
- Three valid constituent triads together exceed a common-jurisdiction boundary → reject composite as unauthorised.
- A group has F/F/A internally but no lawful substitution grant → arithmetic valid, legal commit invalid.
- A final result is valid but an executor claims authority to implement solely because they voted → reject implementation claim without separate basis.
- A previously successful vote is replayed under a new decision ID without fresh authority → reject.
- A historical record or CIBB projection appears to show an authorisation but is stale or incomplete → evidence alone cannot authorise a new vote.

## Open questions

- What precise state constitutes the vote's beginning/end and commit point?
- Does every vote require a unique non-replayable authority token or can equivalent protected provenance suffice?
- How do abstention, recusal, missing positions and procedural invalidity affect the denominator/quorum?
- How is person-identity uniqueness enforced without violating protected personal information?
- What GTP office mapping makes nine distinct Stewards eligible in an origin-included expansion?
- What is the authority basis for binding cross-jurisdictional consequences?

## Status boundary

This is a **cross-module architectural proposal**, not proof of implemented wrappers, legal authorisation, a tested runtime, or portable-module graduation. MNC's own status is Level B candidate, while CBPR/CIBB/CTP have their separately declared release statuses.
