# Single-Position, Vote-Bounded Authority — Authorial Clarification 013

**Status:** Explicit authorial architecture clarification, proposed for V2.1 integration; not automatically enacted law. Original Governance V2 Canonical and historical portable modules remain unchanged.

## Binding design principles supplied by the author

1. **Vote-bounded authority.** Each vote is a single bounded exercise of authority. The authority to act in that voting position exists only for that vote and within that vote's lawful scope; it is not a continuously held or reusable quantum of voting power. This does not eliminate continuing eligibility, appointment records, fiduciary obligations or other separately authorised non-voting responsibilities.
2. **One Steward, one position per decision.** A Steward can occupy or act in **one and only one** voting position within any one decision, including all constituent triads, nested extensions and the receiving virtual triad. Participation in multiple constituent positions for the same decision is prohibited, even if those positions appear at different stages of that decision.
3. **Three-to-one collective substitution.** An authorised extended triad's three Stewards jointly exercise **one** bounded unit of authority attached to **one** original decision position. Their internal ballots resolve that position into **one** resultant; no constituent Steward acquires a separate original-level vote.
4. **No duplication through geometry, nesting or procedural staging.** Sharing a GTP vertex, holding several eligible offices, or appearing at multiple stages does not permit the same Steward to occupy multiple positions in one decision. A decision's identity and boundaries must be defined to enforce this prohibition across the complete vote structure.
5. **No automatic transfer or persistence.** Substitution cannot grant a broader mandate, extend authority beyond the particular vote, or turn temporary voting participation into continuing executive, implementation or territorial jurisdiction. Separate actions need separate lawful authority.

## Consequences for origin-included expanded triads

Define mixed constituent triads:
- A = [A1,A2,R_A]
- B = [B1,B2,R_B]
- C = [C1,C2,R_C]

All **nine occupied voting positions** must be filled by **nine distinct eligible Stewards** for this decision, subject to separately specified appointment, quorum and independence checks. In particular, R_A, R_B and R_C must be **distinct**; the same originating Steward cannot fill two or three of those positions.

Each mixed triad produces one resultant F/A/U. The three resultants are the only three decision positions in the final virtual triad. A resultant is an output of a constituent group, **not a second vote cast by any of its members**. Thus the final-stage resultants do not violate the one-position rule.

**Invalid configuration:** One originating Steward R appears as the third member in A, B and C. Even if the arithmetic yields a majority, the forum is not valid under the one-position rule. Prior Test 012's seven-unique-person hypothesis is now an explicitly **disallowed counterexample**, not an implementation option.

**Potentially valid configuration:** Three different originating Stewards fill R_A, R_B and R_C, with six distinct eligible neighbour Stewards. This satisfies the non-duplication constraint but does **not by itself** prove lawful appointment, the six-Steward vertex map, independence, quorum, jurisdiction or competence.

## Formal decision-scope uniqueness constraint

For any decision D, let P(D) be the set of **individual Steward-occupied voting positions across the entire nested or expanded vote structure**. Let holder(p) identify the human, AI or hybrid Steward occupying p. Then for any distinct positions p and q in P(D):

`holder(p) != holder(q)`.

This constraint applies to **actual Steward positions**, not resultant placeholders. Each valid constituent triad still contributes only one resultant at its receiving interface. Do not mistakenly count the same internal participant again because their group's resultant is propagated upward.

## Vote-level authority invariant

For a valid substitution of receiving position p by constituent triad Q:

- `authority_scope(result(Q), D) ⊆ authority_scope(p, D)`;
- `receiving_weight(result(Q), D) = receiving_weight(p, D)` (one of three receiving positions);
- `duration(authority_use) = the authorised decision/vote event only`;
- `unique_holders(D) = number_of_occupied_Steward_positions(D)`.

These expressions specify bounded voting interfaces, **not** divisibility of constitutional jurisdiction or creation of new permanent offices.

## Record and validation implications

A decision record should include a unique decision ID, a defined vote-event boundary, the specific authority instrument and duration, each Steward identity or privacy-preserving unique identifier, each occupied position and constituent triad, appointment and eligibility proof, initial/final ballot, resultant, recusal/abstention cause, quorum check, final validity, and authority-expiry evidence.

**Hard failure:** If a Steward identity occurs in more than one occupied voting position in the same decision, the expanded vote cannot produce an operative authorised result. Do not repair the duplication by counting the repeated Steward once while retaining other votes; reconstitute the forum under lawful procedure.

## Open implementation details

Precise GTP six-Steward vertex-to-office eligibility, identity resolution across privacy wrappers, definition of when two staged votes constitute one decision, lawful reconstitution, quorum and recusal, emergency succession, and whether a Steward may separately participate in later distinct decisions remain governed by the relevant independent authorisation rules. The author's constraint applies to **one decision**, not an indefinite prohibition on future service.

## Source status

This document records the author's **new explicit clarification**, not a recovered verbatim historical clause. It supersedes the previously *open* repeated-origin eligibility hypothesis in V2.1 Test 012. The original historical texts remain source-preserved.
