# GTP Node Terminology — Authorial Standardisation 035

**Status:** Authorial terminology decision for V2.1. No change to substantive authority, candidate pools, topology or original canonical source.

## Canonical vocabulary

- **Node:** the abstract GTP point at which triangle corners meet, and to which a triangle-owned Steward office position is associated. Use **node**, not **vertex**, in governance prose, mechanisms, interfaces and new file titles.
- **Steward position:** the governance role belonging to **one specified triangle at one of its nodes**. A shared node does not merge the positions of the triangles incident at that node.
- **Steward:** the distinct participant lawfully holding a particular Steward position for the relevant mandate.
- **Triangle:** a GTP spatial subdivision with three node-associated Steward positions.
- **Physical office:** a building or work location inside the relevant triangle; not identical to the abstract node and not required to lie at the node.
- **Node-adjacent / node-sharing Steward:** a Steward occupying a triangle-owned position at the same abstract node as another triangle's Steward position.
- **Candidate ring:** an enumerated set of Steward positions around the originating node, screened for distinct eligible holders before a substitute is selected.

At a regular six-triangle node there are six **separate** triangle-owned Steward positions, one for each incident triangle. They are not a shared governing body, six-person office, or standing cross-triangle authority.

## Governance substitution language

Use **node-adjacent substitute selection** for the first ring of five alternate positions at the same node. The second ring consists of the other two node-associated Steward positions in each of those five neighbouring triangles (ten nominal positions). Further fractal rings are context-controlled. All rings select **one** eligible substitute for **one** bounded original Steward voting position.

For one eligible candidate, appointment is automatic subject to lawful validity checks. For two or more eligible candidates, use a fair auditable random draw. A zero-eligible ring normally advances to the next ring; exceptional security context can justify wider selection before exhaustion, with independent authority. Wider emergency jurisdiction is separate.

## Source-preservation rule

Historical quotations, citations, existing filenames, hashes and original canonical source text must **not** be silently rewritten. Where a mathematical source uses *vertex*, interpret it as the geometric point called a **node** in Concord governance, and provide a one-time equivalence note. In mathematical formulas and code, prefer `node_id`, `nodes(triangle)`, `triangles_at_node`, `origin_node`; use `vertex` only where quoting or interfacing with an external geometry library that requires the term.

Existing V2.1 provisional drafts 019–034 remain historical development records and are not retroactively rewritten. New reconciled candidates and subsequent integration documents should use **node** throughout, while retaining provenance and recording the terminological update.

## Implementation scope

Update the **latest** Chapter 12 and Chapter 132 provisional candidates by a terminology-only revision and verify section-body integrity. Do not edit original `Governance V2 Canonical.md` or change the meaning of triangle ownership, candidate-ring topology or voting authority.
