# GTP Node Ring Origin-Neutrality — Synthetic Comparative Test 039

**Status:** Provisional computational geometry test. Tests the *proposed* edge-frontier third-and-later-ring convention, not an adopted governance rule.

## Question

At a regular GTP node shared by six triangles, does choosing a different origin triangle change the eligible **geometric position pool** at the third or subsequent ring? If so, does that introduce a design issue for substitution fairness?

## Method

Use a regular two-triangle-per-cell lattice, integer coordinates `-6..6`, with node `(0,0)`. Enumerate all six incident triangles as possible origins. For each:
- `R1` consists of the other five triangle-owned positions at node `(0,0)`.
- `R2` consists of the other two node positions in each of those five triangles.
- `R3+` uses the proposed edge-adjacent frontier of triangles, excluding the complete set of six triangles incident at the node.
- Compare **sets of triangle-owned position keys**, not merely ring sizes.

## Distinguish two types of variation

**Expected origin dependence:** R1 and R2 necessarily exclude the originating triangle. Each different origin removes a different set of positions; this is legitimate because the originating triangle is the decision owner.

**Potentially problematic origin dependence:** R3+ may depend on which five of the six incident triangles are used as the frontier. Even if counts coincide, different positions could be reached at different ring depths, changing who is eligible for the nearest nonempty ring. Equal ring sizes are not enough to prove neutral selection.

## Candidate refinement for review

For R3+, define a **node-centred frontier** from the entire set `incident(N)` of six triangles, rather than the five excluding origin. Then exclude all three positions owned by the originating triangle and all positions already present in R1/R2. This makes outward distance bands independent of which triangle initiated the decision while retaining the original-triangle exclusion.

**This is an engineering proposal only.** It does not change the source-defined first and second rings, nor does it allow cross-triangle jurisdiction or new vote weight.

## Invariants

Node is the standard governance term; spatial parent/child is not governance hierarchy; candidate pools are geometric positions screened down to unique eligible holders; n=1 appoints by default, n>=2 selects fairly at random, n=0 expands under context; severe capture may justify wider selection; emergency jurisdiction is a separate bounded authority.
