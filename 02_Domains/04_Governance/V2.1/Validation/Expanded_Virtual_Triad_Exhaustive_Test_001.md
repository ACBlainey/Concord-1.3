# Expanded Virtual-Triad Voting — Exhaustive Test 001

**Status:** Arithmetic verification of author-confirmed proposed expanded voting, not a grant of voting authority or a claim that V2 canon already defines this rule.

## Model
Each of three constituent triads independently yields F if at least two positions vote For, A if at least two vote Against, otherwise U (Unresolved). Apply the same rule to the **three resultant positions**. Do not pool the nine individual votes.

Enumerated all **19,683 = 3^9** nine-position inputs over F, A, U. The intentionally incorrect pooled comparator returns F if the total count F exceeds A, A if A exceeds F, and U if tied.

| Virtual result | Pooled F | Pooled A | Pooled U | Total |
|---|---:|---:|---:|---:|
| F | 3121 | 27 | 135 | 3283 |
| A | 27 | 3121 | 135 | 3283 |
| U | 5124 | 5124 | 2869 | 13117 |
| **Total** | **8272** | **8272** | **3139** | **19683** |

**Total differences:** 10,572/19,683. **Direct F-versus-A reversals:** 54/19,683. The large number of U-versus-decision differences partly reflects the deliberately simplistic pooled comparator.

**Counterexample:** constituent ballots FFF / FAA / FAA yield resultant F/A/A and final **Against**; pooled individual votes are 5F:4A and would incorrectly return **For**.

## Checks
- Two F constituent results guarantee virtual F; two A guarantee virtual A.
- One F, one A, one U yield U, not A or F.
- Permuting constituent triads or votes *within* a constituent triad does not alter the result.
- Abstention is not absence. The F/A/U arithmetic is not a substitute for a procedural cause code or eligibility checks.
- Mixed R-included triads may have overlapping R representatives: this calculation does not validate the independence, identity or duplicate-influence constraints of that configuration.
- Neither majority outcome confers authority without lawful jurisdiction and a valid voting forum.

## Integration targets
V2.1 Chapters 12, 29, 30, 54 and 132. Keep original V2 untouched.
