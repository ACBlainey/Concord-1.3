# GTP Node Candidate Rings — Synthetic Mesh Execution 038

**Status:** Reproducible synthetic geometry check, not a blind validation or real GTP deployment. Evaluates the **proposed** edge-frontier convention from Formalisation 033 and Implementation 037.

## Fixture

Constructed a finite regular triangular lattice with integer coordinates `x,y=-4..4`. For each lattice cell, added two triangles:
- `u(x,y)`: nodes `(x,y),(x+1,y),(x,y+1)`;
- `d(x,y)`: nodes `(x+1,y+1),(x+1,y),(x,y+1)`.

Selected origin triangle `d(-1,-1)` at node `(0,0)`. There are exactly six incident triangles at that node. Rings 1 and 2 follow the authorial first-two-ring definition. Rings 3+ follow the **proposed** edge-adjacent triangle frontier with visited-triangle deduplication.

## Actual computed results

| Ring | Newly discovered triangles | Candidate Steward positions |
|---|---:|---:|
| 1 | Five neighbouring incident triangles | **5** (one at the origin node in each) |
| 2 | Same five triangles, two other nodes each | **10** |
| 3 | 5 new edge-frontier triangles | 15 |
| 4 | 10 new triangles | 30 |
| 5 | 12 new triangles | 36 |
| 6 | 18 new triangles | 54 |

The implementation reported **five distinct R1 position keys**, **ten distinct R2 position keys**, and **zero overlap between R1 and R2**. Beyond ring two, the observed counts are specific to this synthetic fixture, chosen origin, and proposed traversal. They are **not** universal ring-size formulas.

## Test method (executed in JS)

- Enumerated triangles with three node-coordinate pairs each.
- Identified `incident(0,0)` by exact node-coordinate membership.
- Constructed R1 from the five non-origin incident triangles at node `(0,0)`.
- Constructed R2 from their two other node positions.
- For each later ring, discovered previously unvisited triangles sharing a full edge with any current frontier triangle, and assigned three positions to each newly discovered triangle.
- Deduplicated triangles by stable IDs and positions by `triangle_id@node_id`.

## Limitations

This tests **geometric enumeration**, not holder identities, conflicts, eligibility, randomness, authority, quorum, security escalation, mesh seams, GTP resolution transitions or legal decision outcomes. It also does not establish that edge-frontier enumeration is the preferred or final definition of ring three onward.

## Next checks

Run boundary/non-six-degree fixtures; inject duplicate holder identities; compare edge-frontier with alternative node-distance rings; evaluate whether origin-triangle choice makes higher rings asymmetrical; then request authorial confirmation before adopting a third-ring definition.
