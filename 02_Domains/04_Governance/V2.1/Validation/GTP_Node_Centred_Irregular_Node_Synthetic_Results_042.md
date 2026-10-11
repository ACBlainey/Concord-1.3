# Node-Centred Candidate Rings — Irregular Node Validation 042

**Status:** Executed synthetic geometry check; not blind testing and not real spherical GTP validation.

## Fixtures

A finite two-triangle-per-cell integer lattice with x,y in [-6,6] and test node (0,0). Regular fixture includes all triangles. Modified fixture removes triangle `u0,0`, producing a node with five incident triangles. This is a deliberately altered combinatorial mesh, **not a proof that the modified mesh is a valid physical GTP tessellation or a realistic spherical defect**.

For each origin triangle incident at the node, constructed R1/R2 from the other incident triangles and R3–R5 via the node-centred full-edge adjacency frontier, starting from **all** incident triangles.

## Observed results

| Fixture | Incident triangles | R1 positions | R2 positions | R3 new triangles | R4 new triangles | R5 new triangles | Origin-dependent ring counts? |
|---|---:|---:|---:|---:|---:|---:|---|
| Regular | 6 | 5 | 10 | 6 | 12 | 12 | No |
| Modified | 5 | 4 | 8 | 5 | 10 | 12 | No |

The modified fixture has five possible originating triangles; all five gave the same counts at every checked ring. Since the node-centred frontier starts from the **same incident-triangle set regardless of origin**, the discovered higher-ring triangle sets are also identical for each origin within a frozen mesh.

## Interpretation

The proposed mechanism does not rely on inventing a sixth incident triangle. It derives the number of first- and second-ring Steward positions from the actual node degree. The geometric pool can be smaller at irregular nodes, but selection still uses **zero eligible → advance if lawful; one eligible → default; two or more → unbiased random draw**.

## Outstanding real-world geometry and governance checks

- Spherical GTP tessellation defects and edge consistency.
- Mesh resolution seams and simultaneous GTP scales.
- Disconnected incident fans, holes and nonmanifold topology.
- Candidate-holder duplicates, conflict screening and captured random source.
- Emergency authority boundaries, full decision-event identity uniqueness, quorum and security escalation.

**No authorial decision is inferred** that all possible irregular node topologies must be accepted as valid governance geometry.
