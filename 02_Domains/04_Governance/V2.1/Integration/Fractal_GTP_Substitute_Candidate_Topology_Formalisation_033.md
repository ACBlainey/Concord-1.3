# Fractal GTP Substitute Candidate Topology — Formalisation 033

**Status:** PROVISIONAL engineering specification. Source: authorial resolutions 020, 022–023, 029 and 031; not a claim that higher-ring enumeration was present in original Governance V2. No canonical changes.

## 1. Distinct objects

Let a fixed GTP resolution define a conforming triangular mesh `M=(T,V,E)` with triangle IDs `T`, abstract vertex IDs `V`, and geometric edges `E`. A **Steward position** is the ordered pair `(triangle_id, vertex_id)` for a vertex of that triangle. Every triangle has three separate Steward positions. A holder is a participant assigned to a position for the relevant mandate; different positions do not imply different holders without identity verification.

A vertex is an abstract geographic reference, not a joint office or authority. Geometric parent/child relations between resolutions confer no governmental hierarchy.

For an origin triangle `A` and its vacant vertex-position `p0=(A,v)`, let `I(v)={t in T : v is a vertex of t}`. The authorial six-triangle case assumes `|I(v)|=6` at a regular interior GTP vertex; **mesh seams, boundaries, pentagonal defects and cross-resolution interfaces must not be assumed to have degree six**. Validate topology, rather than fabricating five neighbours where the degree differs.

## 2. Precisely specified rings

**Ring 1 (vertex incident):**
`R1={(t,v): t in I(v) and t != A}`.
At a regular degree-six vertex, `|R1|=5`.

**Ring 2 (other vertices of those same triangles):**
`R2={(t,w): t in I(v)\{A}, w in vertices(t), w != v}`.
At a regular degree-six vertex, there are ten **distinct triangle-owned positions**. These need not represent ten distinct eligible participants.

`R1` and `R2` are disjoint as positions. Ring 2 is **not** a set of ten extra triangles; it is the two remaining Steward positions in each of five already incident triangles.

## 3. Proposed further-ring enumeration

The user established fractal outward expansion and reuse of the same eligibility and selection procedure, **not** an exact third-ring formula. To make that principle executable, propose a deterministic frontier traversal on the *triangle edge-adjacency graph*, with a frozen resolution and geometry version:

- Set `VisitedTriangles=I(v)`, `FrontierTriangles=I(v)\{A}`. Do not include the origin triangle's other two Stewards as substitutes by default.
- For each outward step, discover triangles sharing a **full geometric edge** with a triangle in `FrontierTriangles` that have not yet appeared in `VisitedTriangles`. Call them `NextTriangles`. Sort by stable triangle ID for deterministic audit only; sorting must not bias selection.
- Proposed `R3` comprises the three triangle-owned Steward positions of each triangle in `NextTriangles`, excluding any position already in a prior ring. Add `NextTriangles` to `VisitedTriangles` and repeat to obtain later rings.
- Maintain two deduplication layers: **position key** `(triangle_id,vertex_id)` for topology, then **verified holder identity** for candidate eligibility. A participant already voting anywhere in the complete decision event is ineligible; if the same holder occurs twice in a candidate ring, that holder must not receive double lottery weight.
- Reconcile different GTP resolutions by an **explicit, independently authorised resolution-transition mapping**. Never silently merge triangles at different scales or infer authority from containment.

This BFS frontier is a **proposed engineering convention**, not yet authorially adopted. It gives a finite, reproducible expansion order without claiming a fixed exponential growth factor. A different lawful definition of a further ring can replace it after review.

## 4. Selection algorithm (applies identically to each ring)

1. Verify lawful vacancy, event identity, substitution authority and topology snapshot.
2. Build the next permitted ring, respecting contextual security decisions. Audit candidate positions and holders.
3. Independently check conflicts, capability/mandate, identity uniqueness, availability and security exclusions. If a person holds multiple candidate positions, do not treat those as multiple independent chances.
4. Let `n` be the number of **distinct eligible holders**, not the number of positions.
5. `n=0`: advance to next permitted ring, or withhold if the lawful expansion basis is missing.
6. `n=1`: that holder fills the original position by default.
7. `n>=2`: unbiased, auditable, tamper-resistant **uniform draw over distinct eligible holders**.
8. Revalidate eligibility and independent authority at commitment. The substitute exercises **only p0's single bounded voting position** and cannot hold any other voting position in that decision event.
9. Record ring number, geometry version, exclusions, random proof, authority basis, event boundary and expiry. No outcome-driven redraw.

## 5. Context-controlled exceptional widening

A credible, independently reviewed severe capture threat may justify bypassing a populated ring or selecting from a larger independent candidate set. Such a response requires a **recorded security authority basis**; a convenor cannot expand merely because a selected Steward is unpopular.

**Emergency jurisdiction is a separate interface.** A nuclear station emergency may activate wider legitimate emergency governance due to non-local consequences. That does not itself transform the substitute's single position into a regional mandate.

A wider ring does not guarantee more independent holders or lower capture probability. Independence, screening integrity and fair selection remain necessary.

## 6. Open choices requiring explicit resolution

- Whether edge-adjacency BFS is the adopted `R3+` definition, including seam and non-degree-six vertices.
- Whether a single holder assigned to multiple positions is constitutionally possible and, if so, how selection and temporary position occupancy are constrained.
- How security-driven widening chooses a **single wider ring** versus a **union of rings** without weighting bias.
- Minimum security evidence threshold and independent review route.
- Identity and quorum semantics across nested or concurrent decision events.
- Cross-resolution topology transitions and emergency authority interfaces.

Until these are resolved, the source-specified first two rings are operationally clearer than proposed higher rings.
