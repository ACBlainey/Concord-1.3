# Node-Centred GTP Candidate Ring Enumeration — Provisional Revision 041

**Status:** PROVISIONAL engineering selection following comparative test 040; not adopted constitutional law. Uses the authorially standardised term **node**. Supersedes the origin-excluded *discovery frontier* for ring 3+ in 033/037, while preserving their source-defined first two rings.

## Geometric construction

Given originating Steward position `(A,N)`, with node `N` and incident triangle set `I(N)`:

1. **Ring 1:** `{(T,N) | T in I(N), T != A}`.
2. **Ring 2:** `{(T,M) | T in I(N), T != A, M in nodes(T), M != N}`.
3. **Ring 3+:** Discover outward triangles by full-edge adjacency from **all triangles in `I(N)`**, not merely the five non-origin incident triangles. Exclude the complete incident set from new-triangle discovery. Each newly discovered triangle contributes its three triangle-owned Steward positions, subject to position and holder deduplication. Continue breadth-first outward in stable geometry snapshots.

**Why:** Synthetic six-origin comparison 040 found the old five-triangle discovery frontier produced different ring memberships for different originating triangles despite equal ring sizes. The node-centred six-triangle discovery frontier produced identical geometric sets for all six origins.

## Reference algorithm

```text
function candidate_rings(mesh, origin_triangle A, origin_node N):
    require N in mesh.nodes(A)
    incident = set(mesh.triangles_at_node(N))
    yield R1 = {(T,N) for T in incident if T != A}
    yield R2 = {(T,M) for T in incident if T != A
                for M in mesh.nodes(T) if M != N}

    visited = incident
    frontier = incident
    ring_number = 3
    while frontier not empty:
        next = union(mesh.edge_adjacent(T) for T in frontier) - visited
        if next empty: break
        yield ring(ring_number, {(T,M) for T in next for M in mesh.nodes(T)})
        visited |= next
        frontier = next
        ring_number += 1
```

At a regular six-triangle node, R1 contains five positions and R2 ten; the synthetic lattice yielded six newly discovered triangles (18 nominal positions) in R3. The latter count is fixture-specific, **not** a universal theorem for GTP.

## Selection and authority invariants

At each legally permitted ring: independently screen candidate positions and verified distinct holders. Zero eligible → continue outward if authorised; one eligible → appoint by default; two or more eligible → auditable unbiased uniform random draw. Serious independently substantiated capture can justify wider-ring selection before local exhaustion. Emergency governance over a wider area is a **separate mandate** from filling one original position.

No repeated participant in the complete decision event, no extra voting position, no geometric grant of authority, no automatic cross-resolution transfer, no preference-driven expansion or redraw.

## Unresolved boundaries

Non-degree-six nodes; mesh seams and resolution changes; capture threshold and independent review; actual randomness standard; holder multiplicity; decision-event boundaries and quorum. These remain formal validation requirements.
