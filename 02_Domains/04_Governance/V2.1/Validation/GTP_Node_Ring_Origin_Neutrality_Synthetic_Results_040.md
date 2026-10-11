# GTP Node Ring Origin-Neutrality — Executed Synthetic Comparison 040

**Status:** Executed deterministic geometric comparison on synthetic regular triangular lattice; not blind validation, not a constitutional decision. Tests proposal 039 against the frontier in 037.

## Fixture

Regular two-triangle-per-cell integer lattice, x,y from -6 to 6, node (0,0), six incident origin triangles: `d-1,-1`, `u-1,0`, `d-1,0`, `u0,-1`, `d0,-1`, `u0,0`. Compared all six origin choices. Triangle neighbours share a full geometric edge. Each ring 3+ is the set of **new triangle IDs**, each representing three candidate Steward positions.

## Observed counts

| Ring | Original frontier counts for six origins | Union of triangle IDs | Intersection of triangle IDs | Node-centred frontier counts | Node-centred sets identical? |
|---|---|---:|---:|---|---|
| 3 | 5, 5, 5, 5, 5, 5 | 6 | 0 | 6, 6, 6, 6, 6, 6 | Yes |
| 4 | 10, 10, 10, 10, 10, 10 | 12 | 0 | 12, 12, 12, 12, 12, 12 | Yes |
| 5 | 12, 12, 12, 12, 12, 12 | 24 | 0 | 12, 12, 12, 12, 12, 12 | Yes |
| 6 | 18, 18, 18, 18, 18, 18 | 36 | 0 | 18, 18, 18, 18, 18, 18 | Yes |

The **original proposed frontier** uses the five incident triangles other than the origin. The **node-centred alternative** starts from all six incident triangles for geometric discovery, but still excludes the originating triangle's positions from eligibility. Neither method grants the origin triangle an extra vote.

## Interpretation

The old frontier is origin-dependent in its discovered triangle sets: union and intersection differ. This is a geometric selection effect even where counts coincide. The node-centred alternative produces identical discovered triangle sets for every origin in this fixture. This is a stronger geometric neutrality property; it is not proof of security independence or of an adopted legal ring definition.

## Caveats

- This compares ring **triangle sets**, not candidate-holder eligibility, randomness, conflict screening or governance outcomes.
- The first two rings intentionally exclude the origin triangle and therefore depend on origin.
- Mesh boundaries, non-six-degree nodes, resolution seams and spherical GTP defects require additional testing.
- A triangle reached in multiple paths is counted once; identity-level candidate deduplication remains a separate requirement.

## Recommendation for authorial review

Prefer the **node-centred discovery frontier** for rings 3+ if origin-neutral outward search is intended. Keep the five first-ring and ten second-ring positions as established, and preserve single-position bounded authority. Do not treat this recommendation as an adopted constitutional rule.
