# Triadic Module — Authority-Conservation Regression Matrix 008

**Basis:** Original V1.1 `06_Portable_Modules/Triadic Decision Making Module.md` §§2,6,8–10,18,21–22; V2.1 proposed companion 008. **Status:** design validation, not a completed independent blind test.

| ID | Input / context | Expected result | Status |
|---|---|---|---|
| R01 | Ordinary original triad F/F/A, no substitution | For | Consistent with V1.1 §6 |
| R02 | Ordinary triad F/A/Abstain | No majority; no authorised state change | Consistent with V1.1 §§6,8 |
| R03 | Original P1=A, P3=A, substituted P2=Q[F,F,F] | Original A/F/A → Against; not pooled A/A/F/F/F | Conserves one position |
| R04 | Original P1=F, P3=A, substituted P2=Q[F,F,A] | Original F/F/A → For | Conserves one position |
| R05 | Original P1=F, P3=A, substituted P2=Q[F,A,Abstain] | Original F/U/A → unresolved; no majority | Preserves abstention distinction |
| R06 | Three constituent triads Q1[F,F,A], Q2[F,F,A], Q3[A,A,A] | F/F/A → For; pooled 4F/5A prohibited | Two-stage result |
| R07 | Nested Q2=T[F,F,A] | T resolves Q2; Q resolves one original P position | Recursion conserves position weight |
| R08 | Substituted Q[F,F,F] without appointment | No legally operative resultant | Competence/forum gate fails |
| R09 | Same Steward repeatedly occupies R positions in multiple constituent triads | No automatic independence assumption | **BLOCKED: identity/independence specification needed** |
| R10 | Third member absent and remaining two vote For | Arithmetic For; legal effect requires quorum and decision-class rules | **BLOCKED: quorum specification needed** |
| R11 | Parallel Steward advises For, no appointment | Advice only; no voting position | Authority boundary maintained |
| R12 | Internal triad has unresolved result while status quo is dangerous | No automatic emergency power; separate authorised preservation route | Compatible with V1.1 §10 |

## Terminology reconciliation

The original module uses **Abstain** for a participant decision state and **no majority** for an outcome. The companion uses **Unresolved (U)** as a resultant interface state, not as a synonym for an individual participant's abstention, procedural invalidity or lack of appointment. A future formal module should specify whether the F/A/U shorthand is confined to resultants or extended to individual ballots with separately recorded abstention causes.

## Findings

The companion is consistent with the original module's three equal positions, two-of-three majority, abstention diagnostics, no-majority safety default, modularity and experimental status. The original source does not explicitly define nested substitution; the companion adds it. This review does **not** establish operational readiness. Formal quorum, eligibility, authority and identity-correlation tests remain outstanding.

**Recommended next action:** Resolve historical Triadic Governance Decision Protocol source lead, then prepare a clean-instance PMEDG test packet that contains both original source and optional companion without telling the evaluator the expected conclusion.
