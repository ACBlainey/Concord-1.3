# GTP Vertex-Adjacent Random Substitute — Authorial Mechanism 022

**Status:** Authorial design proposal recorded 2026-10-11; provisional governance integration, not canonical adoption.

## Defined example

Triangle A has a top abstract vertex whose ordinary triangle-owned Steward voting position is occupied by A1. Five other distinct triangle-owned Steward positions correspond to the five other triangles meeting at that same abstract vertex. If A1 is lawfully unavailable for a particular vote, the five other Stewards form the **local alternate candidate pool** for filling A1's **one** decision position.

The five are **not** a six-Steward governing body, joint office or standing cross-triangle authority. They ordinarily work for their respective triangles, potentially from separate buildings within those triangles. The shared vertex is conceptual and identifies the local substitution pool, not a physical workplace.

## Randomised substitution and anti-capture

Once a valid vacancy trigger and eligibility checks are satisfied, randomly select one eligible alternate. That alternate acts solely as a bounded substitute for A1's existing position in the defined decision; the position's weight, jurisdiction and permitted effect do not increase. Appointment expires with the vote-specific authority. No general power over triangle A is conferred.

**Illustrative threat model:** If five alternatives are equally eligible and the draw is uniform and tamper-resistant, a single corrupt alternative B3 has selection probability 1/5 = 20%. If an attacker can control only B3 but cannot influence the vacancy, eligibility screening, draw or other candidates, certainty of a compromised substitute requires controlling all five. This is a **conditional** anti-capture property, not an unconditional security guarantee. Compromising the draw or eligibility filter, inducing multiple vacancies, collusion, or repeatedly rerunning the draw changes the threat model.

For `k` compromised eligible alternatives out of `n` equally likely eligible alternatives, the probability of selecting a compromised substitute in a single fair draw is `k/n`. The pool may contain fewer than five eligible holders after legitimate recusals or one-person-one-position checks; record the actual `n`.

## Vacancy trigger requires authorial/legal resolution

- **Absence, incapacity, recusal, failed authentication or lawful unavailability:** possible grounds for declaring a vacancy subject to a separately authorised rule and proof.
- **Abstention:** do **not** silently treat a valid intentional abstention as a vacancy. It may be an exercise of the Steward's authorised voting position and must not be converted into a substitute's affirmative vote without an explicit legitimate rule. The author's example proposes substitution after abstention, but the constitutional interaction remains a question for resolution.
- A disliked vote, delay, or predicted outcome cannot itself create a vacancy.

## Minimum safe substitution workflow

1. Identify the original decision event, triangle A, vertex, A1 position, and lawful cause for replacement.
2. Prove the position is legally open for substitution; distinguish absence from abstention.
3. Resolve the five adjacent triangle-owned Steward identities at the same vertex. This geometric relation nominates candidates but grants no authority.
4. Verify each candidate's eligibility, conflicts, availability, identity uniqueness within the **entire** decision event, and any applicable independence and quorum requirements.
5. Conduct a **single** fair, auditable, tamper-resistant random selection from the remaining eligible pool. Record method, inputs, exclusion causes and verifiable draw evidence, protecting sensitive identities where necessary.
6. Independently authorise the selected person for exactly A1's bounded decision position; check authorisation again before consequential commit.
7. Record the result as a substitution, **not** an additional or pooled vote. Close and expire the temporary vote authority after the lawful decision event.
8. If no eligible alternate remains, or validity cannot be established, mark the position unresolved and apply the independently established quorum/decision rules. Do not silently redraw until a desired outcome appears.

## Interface to extended virtual triads

The ordinary **one-position vacancy substitution** is distinct from an **extended triad's three-to-one resultant substitution** and from a **three-constituent virtual triad**. A vertex-adjacent random substitute occupies **one** original Steward position; it does not generate an additional constituent resultant or grant a new shared jurisdiction.

If the proposed alternate already occupies any Steward voting position in the same complete decision event, they are ineligible under the one-Steward-one-position rule. Do not let selection indirectly bypass the nine-distinct-holder requirement in expanded arrangements.

## Questions before operational authorisation

- Which forms of abstention, if any, can legitimately trigger replacement, and who has authority to determine that?
- What is the exact vacancy-declaration and challenge procedure?
- Is the eligible pool always the five other incident triangle Stewards, or can legitimate disqualification reduce it without mandatory postponement?
- What randomness source, anti-manipulation audit, retry policy and emergency exception are lawful?
- How does this substitution interact with quorum, deadlock, and the original Triadic Governance Decision Protocol?

**Disposition:** Record as a provisional GTP vertex-adjacent random substitute mechanism and PMEDG candidate. No change to Governance V2 Canonical.
