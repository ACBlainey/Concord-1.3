# Bounded Voting Context — Portable Module Candidate 015

**Status:** PMEDG candidate / design specification only; not graduated, implemented, or constitutionally adopted.
**Lineage:** V2.1 authorial one-Steward-one-position clarification 013; abstract contextual wrapper review 014; MNC v0.2, CBPR v1.0, CIBB v1.0 and original Triadic Decision Making module.
**Boundary:** This is a **new voting-specific composition**, not a claim that the source modules already implement a voting service.

## 1. Purpose and minimal kernel

A Bounded Voting Context (BVC) is a temporary abstract wrapper for a **single decision event**, enforcing lawful entry, exactly one occupied voting position per Steward, authority limited to that decision and position, correct composition of substituted triads, consequence-aware validation, and termination of vote-specific authority.

**Authority basis ≠ eligibility ≠ technical capability ≠ voting permission ≠ valid outcome ≠ implementation authority.**

The governing flow is:

`DEFINE → VERIFY BASIS → CONSTITUTE → BIND POSITIONS → OPEN → COLLECT → RESOLVE → REVALIDATE → COMMIT OR WITHHOLD → CLOSE → AUDIT`.

No stage manufactures the authority required by another stage.

## 2. Interfaces and required external services

BVC **consumes**, without becoming authoritative for:
- constitutional competence, common jurisdiction and mandate;
- Steward identity, eligibility, appointment, recusals and conflicts;
- quorum and voting thresholds;
- GTP office mapping and eligible positions;
- time, decision provenance and protected records;
- implementation or enforcement mandate.

If a material required basis is missing, invalid, expired or unresolved, BVC must not produce an **operative** result. A mathematical tally may still be recorded as non-operative evidence.

## 3. Bounded context record

Required fields:

`DecisionID; QuestionVersion; Scope; AffectedSubjects; JurisdictionBasis; MandateRef; AuthorityValidity; VoteEventBoundary; PositionGraph; ConstituentRefs; HolderBindings; IdentityUniquenessCheck; EligibilityChecks; IndependenceChecks; ConflictAndRecusalStates; QuorumRuleRef; QuorumState; BallotState; ResultantState; CompositionState; ConsequenceClass; CommitState; CloseState; AuditRefs`.

Record actual unique identities through privacy-preserving verifiable references where appropriate. A pseudonym is not sufficient if the same person can be registered twice under different identifiers.

## 4. Steward-occupied positions versus resultant slots

A **Steward-occupied position** is one location in the entire decision tree at which a particular Steward is permitted to cast a vote.

A **resultant slot** is a receiving interface populated by the output of an authorised constituent triad. It is **not** a new vote cast by the constituent's members.

For each decision D, the function `holder: occupied_positions(D) → unique_Steward_identity` must be **injective**. No Steward may occupy two positions anywhere in D, including parallel constituent triads, nested substitution or a receiving-level direct position.

Each receiving triad has exactly three **decision slots**. A slot is filled by either one eligible direct Steward vote or one valid constituent resultant. It is never filled by a pool of leaf ballots.

## 5. Capability and authority constraints

Each Steward-occupied position receives only the minimum authority to make its one authorised decision-specific contribution. A constituent triad collectively exercises the authority of the one receiving position it substitutes.

`receiving_weight(constituent_resultant) = receiving_weight(substituted_slot)`.

`scope(constituent_resultant) ⊆ scope(substituted_slot)`.

This does not divide legal jurisdiction into numeric thirds: one-third describes **voting position weight in a three-position triad**, not an independently transferable fraction of constitutional power.

Authorisation to vote ends at the defined voting event. The decision's valid legal consequences may persist, but the voter gains no continuing implementation power.

## 6. Composition and voting result

For a valid three-slot triad:
- two or more F → F;
- two or more A → A;
- otherwise U (no resolved majority).

Abstention is an individual participation state and must not be silently converted to A or treated as identical to the aggregate U. Absence, recusal, conflict, failed identity check, procedural invalidity and insufficient evidence require distinct codes.

**Arithmetic result ≠ legally operative result.** An arithmetic F/A/U outcome is non-operative unless authority, forum, identity uniqueness, independence, quorum, composition and commit-time checks pass.

A valid nested constituent produces exactly one resultant for its receiving slot. No nine-vote flattening or resultants-as-new-people.

## 7. Vote-specific state machine

`DEFINED → BASIS_VERIFIED → CONSTITUTED → OPEN → COLLECTING → TALLIED → COMMIT_CHECK → COMMITTED → CLOSED`.

Exceptional states: `WITHHELD_INVALID_BASIS; WITHHELD_DUPLICATE_HOLDER; WITHHELD_INELIGIBLE; WITHHELD_QUORUM; WITHHELD_EXPIRED; WITHHELD_COMPOSITION; UNRESOLVED_SUBSTANTIVE; COMMIT_UNKNOWN; CANCELLED; CLOSED`.

`UNRESOLVED_SUBSTANTIVE` is a valid non-majority outcome if all procedural gates pass; it is not the same as a withheld/invalid vote.

At `COMMIT_CHECK`, revalidate authority, time, holder uniqueness, appointments, quorum, effective consequence and composition. If material commit status is unknown, do not blindly replay or resubmit: reconcile under the applicable decision record.

## 8. Origin-included and origin-excluded structures

**Origin-excluded:** constituent A, B, C each use three distinct eligible Steward holders; across the entire decision all occupied Steward positions must have distinct holders.

**Origin-included:** three mixed constituent triads [A1,A2,R_A], [B1,B2,R_B], [C1,C2,R_C]. All nine occupied Steward positions must be held by **nine distinct** eligible Stewards. Reusing R_A as R_B or any neighbouring holder across constituents is forbidden.

Both structures require separately valid common jurisdiction and appointment. GTP adjacency or vertex co-location alone cannot grant authority.

## 9. Contextual-wrapper boundaries

**Entry boundary:** lawful decision identity, external authority and role proof, eligibility, non-duplication.

**Internal boundary:** permitted ballots and evidence, protected personal information, abstention and recusal semantics, bounded deliberation.

**Composition boundary:** constituent resultants are verified outputs for receiving slots, not inherited or pooled authority.

**Exit boundary:** a validated result or a specific withheld/unresolved status; audit record survives, voting authority does not.

**Consequence boundary:** an implementation process needs its own independently legitimate mandate. A vote result does not grant general access, enforcement or executive powers.

## 10. Worked cases

- A1=F,A2=F,A3=A → constituent F. Its receiving position counts once.
- Constituent outcomes F,F,A → final F, regardless of nine-leaf pooled majority.
- One origin Steward appears in R_A and R_B → WITHHELD_DUPLICATE_HOLDER, not a valid F/A/U decision.
- Nine unique holders, but no common jurisdiction → WITHHELD_INVALID_BASIS.
- Valid ballot count, appointment expires before consequential commit → WITHHELD_EXPIRED.
- Three constituent groups are valid separately, but composed result exceeds mandate → WITHHELD_COMPOSITION.
- Valid F/A/abstention with no two-of-three majority → UNRESOLVED_SUBSTANTIVE, subject to separate quorum validity.
- A decision is committed, then an operator tries to use its voting credential for a second action → reject; new independent basis required.

## 11. Failure resistance and provenance

Explicitly guard against: duplicated holder identities, duplicated position slots, pooled-ballot multiplication, authority inheritance by containment, stale authorisation, replay, fabricated urgency, self-appointment, cross-jurisdictional capture, and confusion between a valid result and implementation authority.

Protected logs should preserve decision ID, mandate source, holder-position mapping, relevant evidence references, quorum and procedural states, each constituent resultant, final decision status, expiry and review pathway without unnecessary disclosure of sensitive personal information.

## 12. Unresolved dependencies and graduation gate

- Exact decision/vote-event boundaries and identity verification method.
- GTP six-Steward vertex mapping and eligible office assignment.
- Quorum, recusal and independence requirements.
- Common-jurisdiction authorisation and review.
- Source recovery of the historical Triadic Governance Decision Protocol.
- PMEDG blind transfer, negative/adversarial tests, revision and graduation review.

**Disposition:** Candidate for PMEDG development and blind standalone transfer. Do not publish as a graduated module or incorporate into the canonical governance document without those gates.
