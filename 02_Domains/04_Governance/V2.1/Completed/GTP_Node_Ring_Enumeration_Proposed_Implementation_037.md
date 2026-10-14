# GTP Node Ring Enumeration — Proposed Implementation 037

**Status:** PROVISIONAL engineering method, not canonical. Continues Formalisation 033 and terminology standard 035. All governance prose and interfaces use **node**.

## Domain objects

A `node` is an abstract geometric location. A `steward_position` is owned by one triangle at one of its three nodes, represented by `(triangle_id,node_id)`. Multiple triangle-owned positions at a shared node remain separate. A `holder_id` is the verified participant occupying a position. Geometric containment and adjacency confer no jurisdiction.

A GTP resolution and mesh revision must be frozen for a decision-event candidate search. Triangle IDs, node IDs and holder IDs are distinct types.

## Source-defined first two rings

For vacant `(A,N)`, let `incident(N)` be all triangles with node `N`.

- `R1 = {(T,N) : T in incident(N), T != A}`.
- `R2 = {(T,M) : T in incident(N), T != A, M in nodes(T), M != N}`.

At a regular six-triangle node, `R1` has five Steward positions and `R2` ten. At a non-regular node, validate the actual incident degree rather than fabricate six triangles.

## Proposed further rings — edge frontier

The following is a **proposed formal implementation**, not yet an adopted authorial definition of rings three onward:

```text
function enumerate_candidate_rings(mesh, A, N):
    assert N in mesh.nodes(A)
    incident = mesh.triangles_at_node(N)
    adjacent = incident - {A}
    yield ring(1, positions={(T,N) for T in adjacent})
    yield ring(2, positions={(T,M) for T in adjacent
                             for M in mesh.nodes(T) if M != N})

    visited_triangles = incident
    frontier_triangles = adjacent
    k = 3
    while frontier_triangles is not empty:
        next_triangles = union(mesh.edge_adjacent(T)
                               for T in frontier_triangles) - visited_triangles
        if next_triangles is empty: break
        yield ring(k, positions={(T,M) for T in next_triangles
                                 for M in mesh.nodes(T)})
        visited_triangles |= next_triangles
        frontier_triangles = next_triangles
        k += 1
```

Candidate positions are deduplicated by `(triangle_id,node_id)`; actual eligible candidates by **verified holder identity**. A holder assigned to multiple positions receives no additional selection weight. A holder already occupying any voting position in the complete decision-event graph is ineligible.

## Uniform selection at every permitted ring

```text
eligible = unique_verified_eligible_holders(ring.positions, event)
if len(eligible) == 0:
    return EXHAUSTED_RING
if len(eligible) == 1:
    return eligible[0]       # default substitution
return auditable_unbiased_uniform_draw(eligible)
```

A higher ring is used ordinarily when the current ring has zero eligible holders. An independently evidenced serious capture threat can justify earlier widening, with a separately valid security authority. A localised emergency with non-local effects may independently activate wider emergency governance; it does **not** enlarge the substitute's single decision position.

## Deduplication and topology integrity

- Never infer participant identity from a position label; resolve and verify holder IDs.
- Prevent overlapping paths from counting a triangle or position more than once.
- Never give a participant multiple lottery tickets because of duplicate position records.
- Freeze the mesh revision and resolution. Mixed-resolution traversal requires an explicit mapping; spatial parent/child is not an authority hierarchy.
- A ring with more positions need not have more distinct eligible holders or lower capture risk.
- Preserve the original three-position decision denominator; selecting a substitute fills one original position only.

## Formal dependencies

The exact third-and-later-ring topology remains subject to authorial review. Other outstanding dependencies: extraordinary security threshold, fair randomness source, recusal challenge procedure, event-boundary definition, quorum, and resolution-seam handling.
