# Triadic Decision Making — Authority-Conserving Substitution Interface 007

**Status:** PMEDG candidate, developmental specification, not a graduated portable module or constitutional amendment.

## 1. Core invariant

An authorised triadic decision position may be exercised through an expanded deliberative triad. The expanded triad supplies **one resultant** for **one original position**, with exactly the decision weight and authority that position possessed. It does not supply three new original-level votes or three times the authority.

The original three-position triad contains positions P1, P2, P3. Each has one decision position (one-third of the triad's voting positions). If P2 is delegated to an authorised three-position internal triad Q1, Q2, Q3, the internal result of Q occupies P2; P1 and P3 remain unchanged. This substitution does not create a fourth position.

**Authority conservation:** Authority(resultant(Q)) ≤ Authority(P2), and weight(resultant(Q) at original level) = weight(P2). Any substantive restriction on P2 persists through the substitution. The equality of weight does not imply automatic eligibility or jurisdiction; a substitution must be authorised separately.

## 2. Resolution interface

- Input: an existing legally valid decision position, question, bounded mandate, an independently authorised substitute forum and valid internal participation.
- Internal resolution: F/F/A → F, A/A/U → A, F/A/U → U, subject to separately valid quorum and procedural rules.
- Output: **one** F/A/U resultant attached to the original position's identity and provenance, not the internal ballots as original-level votes.
- Final resolution: combine the three original-level positions or resultants as three equally weighted positions. Never flatten a nested structure into pooled ballots.

A member's one-third **voting position** is not a grant of one-third of all constitutional jurisdiction or an independently divisible quantum of executive power.

## 3. Recursive substitution (formal design invariant, not authorisation)

If Q2 is itself lawfully substituted by triad T1, T2, T3, the T resultant occupies Q2; Q's resultant still occupies P2. The original P2 weight is unchanged. Thus the maximum original-level contribution from any nested subtree remains **one position**. This is a mathematical conservation property, not permission for repeated expansion. Each actual substitution requires its own authority and stopping rule.

## 4. Distinguish two arrangements

**Single-position substitution:** An internal extended triad occupies one position of an original triad; the other two positions may remain individual Stewards.

**Three-position virtual triad:** Three authorised constituent triads each supply one resultant; their three resultants together occupy the three positions of the final triad. The three constituent triads do not form a nine-position voting body.

Both conserve original-level position weight. Neither manufactures jurisdiction, makes an advisory Steward an automatic voter, or bypasses quorum.

## 5. Worked examples

1. Original P1=F, P3=A, substituted P2 is Q=[F,F,A] → F. Original-level result F/F/A → F. Q's three internal ballots are not counted alongside P1 and P3.
2. Three constituent triads: A=[F,F,A]→F, B=[F,F,A]→F, C=[A,A,A]→A. Virtual F/F/A→F. Flattened nine-ballot 4F/5A→A is invalid.
3. P2=Q where Q1=F, Q3=A, Q2=T=[F,F,A]→F. Q=F/F/A→F. Original P1=F, P3=A → original F/F/A→F. T adds no new original-level vote.
4. Internal triad unresolved: Q=[F,A,U]→U. The original-level position becomes U, not an automatic Against or vacancy.
5. One original-level position's substitution lacks lawful appointment: even if Q=[F,F,F], Q has no valid resultant for legal effect. Do not treat its mathematical F as authorised.

## 6. Required provenance

Original position identifier; source of authority; question and scope; substitution authorisation; each internal position's identity and eligibility; quorum; conflict/recusal and abstention codes; internal ballots; internal resultant; original-level position resultant; timestamps, expiry, review and termination. For recursive cases, preserve the complete path of substitutions and the one-position mapping at every interface.

## 7. Unresolved interfaces

Six-Steward vertex-to-office mapping; origin-included repeated R participation and independence; quorum and procedural validity; common-competence authorisation; exceptional expansion stopping conditions. These are blockers for operational deployment, not grounds to invent rules.

## 8. PMEDG development status

**Candidate:** Triadic Decision Making — Authority-Conserving Substitution. Proposed as a module-level invariant for later extraction and clean-instance validation under PMEDG. No claim of completed extraction, graduation, or independent blind testing.

**Concord source interface:** Governance V2.1 Chapter 12 Reconciled Candidate 007, §12.9.3. Other relevant interfaces: Chapters 9, 28–30, 54, 100, 132, 149–151 and 198.
