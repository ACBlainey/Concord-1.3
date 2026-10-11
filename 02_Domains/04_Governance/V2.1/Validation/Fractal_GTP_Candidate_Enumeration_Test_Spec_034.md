# Fractal GTP Candidate Enumeration — Deterministic Test Specification 034

**Status:** PROVISIONAL conceptual and executable-pseudocode validation. This is not an independently run blind test. References Formalisation 033.

## Structural properties to verify

1. For a regular degree-six vertex, first-ring position count is **five**, and second-ring position count is **ten**.
2. Each second-ring position belongs to one of the same five neighbouring triangles but to a vertex other than the origin vertex.
3. No candidate position occurs in more than one ring.
4. Any candidate holder already voting anywhere in the same decision event is ineligible.
5. Two positions assigned to the same verified participant do not give that participant two random-selection tickets.
6. Expansion past ring two uses the proposed **edge-adjacent triangle frontier**, never a claim that the number of candidates must double.
7. If a triangle can be reached by two frontier paths, its positions are added only once.
8. If the GTP vertex has degree other than six, do not invent five first-ring candidates or ten second-ring candidates; invoke a topology-aware rule.
9. If candidate holders are `[X,Y,Y,Z]`, the uniform selection pool is `[X,Y,Z]`, after any position and identity eligibility checks.
10. If `n=0`, proceed outward only with lawful expansion authority; if `n=1`, fill by default; if `n>=2`, uniform random selection.
11. Security-driven bypass of an eligible ring requires independently justified context and audit, not preference.
12. Emergency multi-region coordination and filling one original position are separate authority events.

## Reference pseudocode

```text
function build_first_two_rings(mesh, origin_triangle, origin_vertex):
    incident = mesh.triangles_at_vertex(origin_vertex)
    assert origin_triangle in incident
    neighbors = incident minus {origin_triangle}
    R1 = set((t, origin_vertex) for t in neighbors)
    R2 = set((t, w) for t in neighbors for w in mesh.vertices(t)
             if w != origin_vertex)
    assert R1 intersect R2 is empty
    return R1, R2, incident, neighbors

function proposed_next_ring(mesh, visited_triangles, frontier_triangles):
    next_triangles = union(mesh.edge_neighbors(t) for t in frontier_triangles)
                     minus visited_triangles
    next_positions = set((t, w) for t in next_triangles
                         for w in mesh.vertices(t))
    return next_positions, next_triangles

function eligible_holder_pool(positions, event):
    candidates = []
    for position in positions:
        holder = resolve_verified_holder(position)
        if holder is not null and lawful_eligibility(holder, position, event)
           and not event.has_other_voting_position(holder):
            candidates.add(holder)
    return unique_by_verified_identity(candidates)

function choose_one(eligible_holders, approved_randomness):
    if count(eligible_holders) == 0: return EXHAUSTED
    if count(eligible_holders) == 1: return eligible_holders[0]
    return uniform_unbiased_choice(eligible_holders, approved_randomness)
```

The reference intentionally leaves the authoritative randomness implementation and legal eligibility predicate abstract; those are governance/security interfaces, not topology facts.

## Adversarial edge cases

| ID | Input | Expected |
|---|---|---|
| T01 | Regular vertex degree 6 | `|R1|=5`, `|R2|=10` |
| T02 | Vertex degree 5 | `|R1|=4`, `|R2|=8`; flag departure from ordinary six-triangle assumption |
| T03 | Shared holder on two R2 positions | One eligible person/ticket at most |
| T04 | Triangle discovered along two R3 paths | One triangle and three position keys at most |
| T05 | Same participant already voted at origin's other position | Exclude from candidate pool |
| T06 | All R1 candidates ineligible, one R2 candidate eligible | Sole R2 holder fills by default |
| T07 | All R1 candidates ineligible, multiple R2 candidates eligible | Fair uniform selection over distinct eligible holders |
| T08 | R3 BFS meets prior R1/R2 triangle | Already visited; not re-added |
| T09 | Mesh resolution changes during decision | Freeze snapshot or require independently authorised remapping |
| T10 | Emergency commander demands extra vote due to wide hazard | Reject; separate emergency jurisdiction process |
| T11 | Candidate pool expanded on allegation alone to avoid disliked candidate | Withhold bypass pending independent security authority |
| T12 | Multiple GTP scales operate simultaneously | Keep resolution-specific candidate graph; no spatial parent authority |

## Important qualification

A non-degree-six vertex may arise from mesh geometry or tessellation seams. The counts above are graph-theoretic consequences of the chosen incident-triangle definition, **not proof that a different local substitution rule is constitutionally adopted there**.
