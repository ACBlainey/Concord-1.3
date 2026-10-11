# GTP Six-Steward Vertex Mapping — Constraints and Source Questions 019

**Status:** Provisional research specification. No appointment rule, voting office or constitutional amendment is established here.

## Established architectural constraints

1. GTP is a continuously existing conceptual triangular tessellation at multiple scales; its spatial parent/child relations are not governance chains of command.
2. A vertex is associated in the historical design with **six Stewards**. That count is a spatial/representation description, **not** sufficient evidence of which people may vote in a particular forum.
3. A standard decision triad has three bounded positions. A constituent triad yields **one** resultant, preserving its receiving-position weight.
4. Origin-excluded and origin-included three-constituent virtual triads require **nine distinct eligible Steward holders** across the entire decision event. For origin-included mode, R_A, R_B and R_C must be distinct people.
5. Each Steward may occupy one voting position in a single decision event; eligibility or office does not confer standing vote authority.
6. Geometry, vertex adjacency, concurrent resolution or workload changes cannot appoint a Steward or establish jurisdiction.
7. The identity of a distinct decision event requires independent legal proof; new labels cannot reset the one-position rule.

## What remains unknown

The available Chapter 132 Candidate 006 and Chapter 12 Candidate 008 do **not** establish:
- whether the six at a vertex are six separate persons, six office associations, or a positional representation;
- which of those associations belong to each incident triangle and at which GTP level;
- whether a person can be associated with multiple vertices or spatial scales, and the resulting conflicts;
- how R_A/R_B/R_C are chosen from lawful origin eligibility without double occupancy;
- whether the relevant nine eligible people exist for every requested expanded arrangement;
- who lawfully appoints, recuses or substitutes a position, and quorum/independence tests.

No unique mapping can be inferred from the number six alone.

## Candidate *validation* interface, not a candidate allocation rule

Input: `GTPLevel; VertexRef; TriangleRef; StewardIdentityRef; OfficeBasis; EligibilityProof; MandateRef; DecisionEventRef; PositionRef; ConflictState; TimeWindow`.

For every proposed constituent:
- Resolve each occupied position to one verifiable distinct Steward identity and a current, independent lawful basis.
- Reject repeated identities anywhere in the full decision-event position graph, including across vertex aliases, constituent groups and concurrent scales.
- Verify each triangle/vertex association against an authoritative mapping source **without deriving authority from the map**.
- Verify external competence, common jurisdiction, quorum and independence.
- If mapping, appointment or eligibility is unknown, withhold consequential commit; do not fill a vacancy with a repeated person merely to make nine positions.
- Preserve non-operative diagnostic arithmetic separately from valid decisions.
- Preserve distinct causes: `VERTEX_MAPPING_UNKNOWN`, `HOLDER_DUPLICATE`, `POSITION_INELIGIBLE`, `COMMON_JURISDICTION_UNKNOWN`, `QUORUM_UNKNOWN`, `DECISION_BOUNDARY_UNKNOWN`.

## Adversarial mapping cases for later testing

**V01:** Six office labels at a vertex resolve to fewer than six unique people. Do not infer six eligible votes.

**V02:** R_A, R_B, R_C are all mapped to one origin Steward. Reject the origin-included forum; no triple reuse.

**V03:** Nine distinct people exist, but one is ineligible for the question. Withhold rather than silently replacing.

**V04:** A Steward has legitimate associations with two neighbouring triangles. The same person cannot occupy both positions within one decision.

**V05:** Multiple GTP resolutions are concurrently used. An identical underlying Steward appears at two scales in one event. Reject duplicate occupancy.

**V06:** Nine valid holders are mapped but there is no common jurisdiction. Withhold operative result.

**V07:** Only eight independently eligible Stewards can be identified for a nine-position arrangement. Do not invent a ninth, pool eight ballots or relax uniqueness.

**V08:** Two genuinely independent decisions occur at overlapping GTP scales; the same Steward is independently authorised once in each. The one-position rule alone does not prohibit participation across separate lawful decisions.

## Source-resolution gate

Locate the original GTP paper, diagrams and Steward vertex allocation definitions; compare exact source passages with the provisional chapter candidates. Do not convert a graphical six-Steward convention into a legal office map without authorial confirmation. Resolve appointment, decision-event identity and quorum from their own authoritative sources.

**Disposition:** Constraint specification and PMEDG test candidate only. No source-proven vertex mapping has yet been established.
