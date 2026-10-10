# Expanded Triadic Governance and Continuity Protocol — Reconstruction 001

**Project:** Foundations of the Concord / GTP Spatial Triadic Governance  
**Status:** Author-confirmed reconstruction with source-recovered provisions and explicitly provisional implementation clauses  
**Date:** 10 October 2026  
**Placement proposed:** Concord-1.3 / Governance domain / Active Development (not yet canonical)  
**Source-control note:** This document is a new reconstruction, not a recovered verbatim copy of the lost expanded-voting procedure. It must not silently supersede Governance V2.

## 0. Purpose and provenance

This specification preserves the reconstructed expanded triadic voting arrangements, the GTP mesh governance relationship, the lowest-capable-level principle, and the distinction between parallel and substitute Stewardship. Its purpose is to make the architecture independently understandable and testable without reliance on conversation history.

**Evidence classes:**
- **[V1] Recovered:** directly supported by the historical *Governance Full.md* in the original Concord repository.
- **[AUTHOR] Confirmed:** specified or clarified by the Concord author in the October 2026 reconstruction discussion; may be absent from the recovered written source.
- **[PROPOSED] Pending:** operational completion or safeguard suggested for later ratification and testing, not claimed as an existing constitutional rule.

**Primary recovered source:** `ACBlainey/Concord`, `02_Operational_Systems/Governance Full.md`, especially Ch. 2 §2.11 (Parallel Stewardship), Ch. 12 §12.1 (horizontal expansion and lowest competent layer), Ch. 14 §14.2.15–16 (emergency substitution and abstention). Source URL: https://github.com/ACBlainey/Concord/blob/main/02_Operational_Systems/Governance%20Full.md

**Source tension requiring reconciliation:** V1 Ch. 12 describes the origin-included variant broadly as retention of the originating triad plus neighbours; the author's more precise reconstructed voting geometry is **three mixed triads each containing two neighbouring Stewards and one originating Steward**. Preserve both records; treat the specific voting arrangement below as author-confirmed reconstruction, not a verbatim V1 quotation.

## 1. Constitutional and spatial premises

1. **Lowest capable level [V1, AUTHOR].** Decisions belong at the lowest governance level that actually possesses the necessary authority, evidence, resources, capacity, jurisdiction and ability to account for material consequences. Larger-scale coordination does not itself confer superior authority.
2. **GTP is a spatial abstraction, not a command hierarchy [AUTHOR].** GTP triangles exist conceptually at every tessellation resolution. Spatial *parent* and *child* mean geometric scale only. Multiple resolutions and overlapping functional decision fields may operate concurrently. No permanent superior governance office is implied by larger triangle size.
3. **Ordinary triad is the default [V1].** Three authorised decision positions, ordinarily one Steward per position. Extraordinary expansion is not the default reaction to ordinary disagreement.
4. **Bounded contextual authority [V1].** Capacity, permission and authority are distinct. The creation of an expanded voting group does not itself enlarge the lawful subject matter, duration or implementation powers of a decision.
5. **Consequences define legitimate decision scope [AUTHOR].** A shared hazard does not automatically require one shared policy. Shared infrastructure, externalities, nonconsenting affected parties and cross-boundary resource impacts may require coordination or legitimately shared decisions.
6. **Six-Steward vertex representation [AUTHOR].** Each GTP triangle vertex is represented by six Stewards across the surrounding mesh. This creates additional potential configurations and resilience, but does not imply six automatic votes per vertex or authority for every individual over every matter. The precise mapping of individual offices, eligibility and vertex identities is to be formally verified.

## 2. Terminology

- **Origin R:** the initiating or affected GTP triad.
- **A, B, C:** the three triangles sharing an edge with R in the relevant four-triangle local arrangement. For the reference orientation, A is below R; B and C occupy the other adjacent positions. Names are arbitrary; adjacency and orientation must be verified against the selected GTP spatial address.
- **Constituent triad:** a three-position voting group in an expanded decision.
- **Resultant vote:** the one effective For or Against vote produced by a valid majority within a constituent triad.
- **Virtual triad:** the final three-position vote made from the three constituent resultant votes, not the pooled individual Steward ballots.
- **Unresolved:** no valid resultant vote because required conditions were not met; distinct from a majority Against.
- **Parallel Steward:** an independent constitutional reasoning participant who does not automatically possess delegated executive decision authority [V1].
- **Substitute Steward:** a person formally and temporarily authorised to fill an unavailable decision position under bounded succession rules [V1].
- **Decision field:** the temporary set of affected spatial, functional and decision positions required for a particular matter.

## 3. Primary expanded voting configuration I — origin excluded [AUTHOR]

**Trigger class:** where the originating triad is conflicted, is itself under review, cannot legitimately adjudicate its own matter, or other justified circumstances require independent neighbouring decision-makers. Triggering does not itself establish guilt, misconduct or incompetence.

**Construction:**
1. Identify origin R and the three edge-adjacent triangles A, B, C at the relevant GTP resolution.
2. R's three decision positions are excluded from this vote.
3. A's authorised three Stewards vote independently as constituent triad A.
4. B's authorised three Stewards vote independently as constituent triad B.
5. C's authorised three Stewards vote independently as constituent triad C.
6. Each valid constituent majority produces exactly **one** resultant vote.
7. The three resultant votes form a virtual triad. Its majority is the expanded decision, subject to lawful authority and procedural validity.

**Non-pooling invariant:** Nine first-stage individual votes must **never** be totalled as a single nine-person ballot. Example: A = 2 For / 1 Against; B = 2 For / 1 Against; C = 0 For / 3 Against. The individual total is 4 For / 5 Against, but the **virtual triad is 2 For / 1 Against**, hence its result is For. This is deliberate equal weighting of the three constituent triads.

## 4. Primary expanded voting configuration II — origin included [AUTHOR]

**Trigger class:** a wider decision field is needed while retaining direct participation and contextual knowledge from the originating triad, without introducing a fourth final voting position.

**Construction:**
1. Identify R and its three edge-adjacent neighbours A, B, C.
2. Form **mixed triad A:** two eligible Stewards from A plus one eligible Steward from R.
3. Form **mixed triad B:** two eligible Stewards from B plus one eligible Steward from R.
4. Form **mixed triad C:** two eligible Stewards from C plus one eligible Steward from R.
5. Each mixed triad independently votes and yields exactly one resultant vote when validly resolved.
6. The three resultant votes form the final virtual triad; a valid majority of those three determines the decision.

**Reference participation:** the three originating Steward positions may each occupy one distinct mixed-triad position, avoiding duplicate participation by the same person. The exact selection and substitution rules remain to be formalised. There are nine first-stage voting positions, but only three effective final positions. This is **not** a four-triad vote and **not** a pooled nine-person vote.

## 5. Voting semantics and decision states

**Confirmed structural principle [AUTHOR]:** effective voting groups should contain an odd number of decision positions, normally three, to avoid even-number binary ties. The expanded outcome is determined by three resultant votes.

**Recovered constitutional direction [V1]:** a majority is required to authorise a state change. Lack of authority or insufficient evidence does not justify speculative action.

**Operational distinction [PROPOSED, pending validation]:**
- **For:** a valid majority supports the proposal.
- **Against:** a valid majority opposes the proposal.
- **Unresolved:** no valid majority/result because of abstention, invalid participation, incapacity, conflict, absence or procedural deficiency.

An unresolved constituent result is not silently converted to Against or For. An odd number of nominal seats does not prevent an unresolved outcome if a seat abstains or is invalid. Nor may expansion be used to keep seeking a favourable answer after a valid adverse vote. A properly resolved Against is a decision, not a procedural breakdown.

**Worked examples:**
- Constituent results For / For / Against => virtual result For.
- Against / Against / For => virtual result Against.
- For / Against / Unresolved => final result unresolved pending authorised handling; no implied approval.
- For / For / Unresolved => whether the two valid results suffice or the third must be reconstituted is **not yet ratified**; default to procedural validation rather than silently inventing a rule.

## 6. Parallel Stewardship versus substitution

### 6.1 Parallel Stewardship [V1]

Historical Governance Ch. 2 §2.11 states that Parallel Stewards receive substantially equivalent information, evidence, constitutional principles, responsibilities, constraints and deadlines. They independently decide what they *would* do and record their reasoning before comparison where practical. Their function is independent decision replication, not majority voting. Differences can reveal incomplete evidence, divergent assumptions, ambiguity or institutional drift. Parallel Stewards do **not** gain executive authority merely by reaching a conclusion.

### 6.2 Emergency substitution [V1]

Historical Governance Ch. 14 §14.2.15 provides for a **predefined substitute Steward** temporarily filling an unavailable position, with only the defined authority transferred. It also recognises reduced participation, escalation where appropriate and emergency non-action. Abstention reasons require contextual examination (§14.2.16).

### 6.3 Relationship [PROPOSED]

Parallel Stewardship can support continuity by retaining independently developed reasoning and a potential pool of qualified candidates. However, **parallel status alone is insufficient for a voting seat**. An eligible individual must pass the separately authorised appointment, conflict, competence and bounded-authority checks before acting as a substitute. The record must distinguish advisory participation from formal assumption of a decision position.

## 7. Exceptional decision continuity [PROPOSED]

This section is a **candidate procedure** for testing, not an assertion of recovered historical law.

1. **Detect and classify:** distinguish absence, illness, inaccessible communications, incapacity, voluntary abstention, evidence insufficiency, recusal, conflict, compromised credentials, coercion, systemic compromise and invalid procedure.
2. **Preserve record:** capture the original question, scope, evidence, Steward positions, votes if lawfully cast, reasons, dissent, deadlines and risks.
3. **Assess urgency:** can the issue safely await restoration of normal participation? Avoid manufacturing emergencies.
4. **Respect legitimate abstention:** an abstention is not by itself misconduct or permission to remove the dissenter. Identify whether the cause is a conflict, inability to decide safely, or a legitimate considered position.
5. **Use authorised substitution when applicable:** predefined qualified substitutes assume specific positions temporarily; confirm independent eligibility and record the authority transfer and sunset.
6. **Reconstitute a compromised constituent triad when lawful:** if multiple positions cannot validly participate, determine whether a new constituent group can be assembled without altering the question or selecting participants for preferred outcomes.
7. **Expand into the mesh only when justified:** where the immediate field lacks capability, independence or jurisdiction, identify the next appropriate eligible neighbours or resolutions; preserve three resultant decision positions where feasible.
8. **Check termination:** if no lawful and competent configuration can be formed, record unresolved/non-action or transfer only to an actually authorised process. Expansion is finite, reasoned and auditable.
9. **Restore normal governance:** temporary appointments and expanded authority sunset after the defined matter; original local competence resumes.

**Explicit anti-capture safeguards:** no selective replacement for an unwanted vote; no automatic disenfranchisement through abstention; no duplicate effective voting by one person without express rule; no authority from mere geographic inclusion; no covert escalation to permanent hierarchy; no pooled vote that destroys constituent equality; no indefinite repeated votes on an unchanged question.

## 8. Recursive mesh extension and spatial resolution

**[AUTHOR]** The local A/B/C arrangement is the standard first outward expansion. Further triangles can be included if necessary. GTP spatial children always exist conceptually; subdividing or coordinating at another resolution selects a map scale, not a superior governance authority. Several resolutions and neighbouring decision fields can be active concurrently. Operational capacity may be dynamically distributed with hysteresis to prevent excessive oscillation.

**[PROPOSED]** Before a further expansion, a documented justification should identify: the unsatisfied requirement; the affected jurisdiction/consequences; why parallel review, substitution or local reconstitution is insufficient; the proposed new field; how three independent resultant votes will be produced; and the sunset/termination condition. The exact recursive aggregation topology, tie/abstention treatment and cross-resolution composition require dedicated design and adversarial tests. Do **not** assume that arbitrary numbers of regional votes may be reduced to three without a published weighting and grouping rule.

## 9. Large-area decisions: aggregation versus autonomous regional choice

**[AUTHOR]** A common event across many triangles is not automatically a common binding decision. There are at least three lawful patterns to distinguish:

**A. Coordinated independent decisions:** Each capable region decides its own response, sharing observations, resources and implementation coordination without surrendering local decision authority.

**B. Aggregated shared decision:** A matter with genuinely inseparable consequences or legitimately shared authority is decided through a separately specified aggregation of constituent triad votes. The scope and legal basis of binding effect must be stated before voting.

**C. Hybrid:** Shared systems (e.g., cross-region evacuation routes, flood barriers, regional hospital capacity) are jointly coordinated or decided while local policy choices remain locally authorised.

### Hurricane example [AUTHOR]

Five triangular regions face an approaching hurricane. Four independently vote to require evacuation; the fifth votes not to require it. The four decisions do **not** automatically override the fifth. The fifth region may retain its different policy if that decision remains within its lawful scope and its consequences can legitimately be bounded. It must not automatically prevent individuals from evacuating voluntarily. Rights, nonconsenting persons, cross-border externalities and the practical safety of affected participants require separate review.

The regions may coordinate meteorological data, roads, shelters, emergency services and medical resources without creating one regional sovereign authority. If the fifth region's actions materially burden other regions or shared infrastructure, that **new cross-boundary issue** may require a distinct shared decision. It does not retrospectively convert the original local vote into a 4-to-1 regional plebiscite.

**Invariants:** disagreement alone does not trigger escalation; coordination does not imply command; shared danger does not erase local authority; legitimate externalities cannot be ignored merely because they cross a triangle boundary.

## 10. Decision-routing checklist [PROPOSED]

For every proposal, record answers to the following in order:

1. What precisely is the proposed state change, and what happens if it is not authorised?
2. Which local triad has the lowest capable, lawful jurisdiction?
3. Are the evidence, resources, independence, participation and implementation capacity adequate?
4. What are the direct and indirect consequences beyond the local decision field?
5. Is this a coordination problem, a shared binding decision, or a compromised/uncapable local process?
6. If local decision remains legitimate, can each region decide independently?
7. If expansion is necessary, is origin-included or origin-excluded appropriate, and why?
8. Are all constituent Steward positions independently eligible and free of disqualifying conflict?
9. Are substitutions formally authorised, or are Parallel Stewards acting only in advisory capacity?
10. Have the three constituent resultant votes been obtained and counted without pooling?
11. Is the virtual result valid, or is it unresolved? What lawful procedural response follows?
12. What is the bounded implementation authority, sunset, record and review route?

## 11. Required test programme [PROPOSED]

**Voting correctness:** exhaustive For/Against combinations for both configurations; intentional non-pooling counterexample; symmetry under permutation of A/B/C; verify no four-way final vote.

**Participation failures:** one or more absent Stewards; abstention with insufficient evidence; principled abstention; recusal; invalid credentials; conflict in R; conflict in a neighbour; total triad unavailability; emergency substitution.

**Anti-capture:** coordinated vertex positions; shared information sources; selective replacement attempts; repeat-voting until favourable outcome; multiple roles held by one individual; biased triad selection; adversarial boundary choice.

**Scale and jurisdiction:** independent regional hurricane responses; shared flood-barrier control; cross-border evacuation routes; multi-resolution overlapping decisions; externality disputes; resource allocation across regions; temporary emergency coordination with automatic sunset.

**Termination:** unresolved vote with no eligible substitutes; missing legal authority; exhausted neighbouring pools; delayed evidence; conflicting regional decisions with no shared jurisdiction; safe non-action versus time-critical response.

Each test should capture the proposal, relevant spatial addresses, initial authority, Steward eligibility, ballots and resultant votes, substitution provenance, escalation reasons, final state, implementation scope and audit trail. Preserve failed tests and contradictory evidence.

## 12. Open specifications requiring author decision or source recovery

1. Exact mapping of six Stewards at each vertex to authorised voting positions and independent pools.
2. Selection rule for the two neighbouring Stewards in each origin-included mixed triad.
3. Selection rule for the three originating Stewards across mixed triads; whether repeat individuals are ever permitted.
4. Distinction between a fully legitimate abstention and an unavailable seat eligible for substitution.
5. Whether two resolved constituent results can determine a final result when the third is unresolved, or whether all three are mandatory.
6. Recursive grouping rule for more than three neighbouring constituent regions; no silent pooling or ad hoc weighting.
7. Precise trigger and boundary between coordination, aggregated binding authority, and local autonomy.
8. How emergency time limits, restoration, judicial review and constitutional challenge interact.
9. Cross-resolution and overlapping GTP field jurisdiction, including conflicting simultaneous decisions.
10. Formal source comparison against the full Governance V2 Canonical and other historical archives before graduation.

## 13. Integration and archival controls

- Preserve this document as a dated **development reconstruction** with immutable provenance and a link from the Governance development register.
- Keep historical V1 text unchanged. Do not relabel author-confirmed reconstruction as a verbatim historical passage.
- Cross-reference GTP spatial governance, bounded contextual authority, Governance Operating Protocol, Parallel Stewardship, emergency succession, and triadic portable module documentation.
- Conduct source-resolution against V2 and archival copies, then test the specification in a clean instance under the portable-module evaluation methodology.
- Graduate only the validated rules into Governance V2. Retain unresolved alternatives, dissent, failed tests and historical wording in the archive.

## 14. Concise invariant register

**I-01** Local-capable-first.  
**I-02** Spatial scale is not command hierarchy.  
**I-03** Expanded authority is temporary, contextual and bounded.  
**I-04** Three constituent votes ordinarily yield one virtual-triad result.  
**I-05** Never pool individual first-stage votes across constituent triads.  
**I-06** Origin-excluded: A, B and C vote as separate triads.  
**I-07** Origin-included: each of A, B and C contributes two Stewards, paired with one R Steward.  
**I-08** Parallel advice never automatically becomes executive voting authority.  
**I-09** Substitute authority requires explicit, bounded appointment.  
**I-10** Abstention is not automatically an Against vote or a removable defect.  
**I-11** Disagreement alone does not justify escalation.  
**I-12** Common hazards can permit different legitimate local decisions.  
**I-13** Cross-boundary consequences require assessment, not automatic centralisation.  
**I-14** Recursive expansion must be justified, auditable and terminating.  
**I-15** A valid vote cannot be repeatedly reconstituted merely to obtain a preferred answer.  
**I-16** Voting validity and authority to implement are separately checked.

---

**End of Reconstruction 001.** This is a substantive preservation artefact, not yet a ratified constitutional amendment or completed operational protocol. The author-confirmed rules are fixed here for future source resolution; open implementation questions remain explicit.
