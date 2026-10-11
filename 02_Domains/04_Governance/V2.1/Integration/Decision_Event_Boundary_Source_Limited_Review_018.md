# Decision Event Boundary — Source-Limited Interface Review 018

**Status:** Provisional analysis, not canonical authority.

## Evidence consulted

- `Reconciled_Candidates/Chapter_12_Expanded_Triads_Reconciled_Candidate_007.md`, Git blob `134a4e061433de6ba50badd670f42ece9b727ce0`, is a provisional reconciled chapter, not enacted law. Its introductory status still says repeated origin Steward participation is unresolved; this conflicts with the later explicit one-Steward-one-position clarification and requires reconciliation.
- `Integration/Decision_Validity_and_Interface_Gates_006.md`, Git blob `5c95b967ad3a14a5e972015a09bcefaae96faab3`, distinguishes competence, forum, participation and result gates.
- `Validation/BVC_BTT_002_Result_Review_and_Decision_Boundary_017.md` records the second conceptual evaluator result and identifies R12 as unresolved.
- **Limitation:** An attempted direct fetch of `02_Domains/04_Governance/Governance V2 Canonical.md` returned an empty content field despite a blob SHA; therefore no claim is made that the complete canonical chapter text was searched in this pass. Existing source-preserving reconciliations remain separate evidence.

## Distinguish the relevant operations

1. **Constituent stage:** an internal part of one authorised decision; cannot gain an independent vote grant from a different identifier.
2. **Retry / receipt reconciliation:** a technical repeat or uncertain commit of the same decision; must not create a fresh vote or consequence.
3. **Continued deliberation:** the same unresolved question under the same authority; a new session is not automatically a new decision.
4. **Reconsideration:** may be a distinct decision only if the competent authority and applicable process independently permit it; a label is insufficient.
5. **Appeal / review:** a distinct lawful review forum may exercise its own bounded mandate, but the prior decision does not transfer authority to it automatically.
6. **Renewed mandate:** independently sourced authorisation for a new question or renewed decision, not a reset of expired authority by clerical renaming.
7. **Independent subsequent decision:** distinct legally operative question or event with separate basis; Steward may participate again if newly eligible and authorised.

## Provisional boundary rule

For a proposed vote stage S, the authoritative decision-event boundary must be resolved **before** assigning a new one-position-per-Steward uniqueness domain. A new `DecisionID` is merely a record label.

`BoundaryProof(S)` should identify: question and version; operative mandate; jurisdiction; intended consequence; constituent/continuation/retry/reconsideration/appeal relationship; independently authorised new event where claimed; and verified closure or commit state of related events.

Where a stage's separateness is materially unresolved, record `DECISION_BOUNDARY_UNKNOWN` and withhold operative commit. Do not silently count it as a new event, but do not permanently merge unrelated lawful decisions either.

## Counterexample and safeguard

A Steward occupies position A1 in constituent A, and an administrator creates a second ID for constituent B while the same substantive decision remains pending. The Steward is assigned B1 as well. Both local ballots could appear valid if each ID is treated as an independent decision. **Correct treatment:** resolve common decision-event ancestry, detect duplicate Steward across the combined position graph, and withhold. If separate decisions are independently established, uniqueness is checked within each legitimate event.

## Interfaces still requiring source resolution

- Exact legal meaning of a decision, reconsideration, appeal, review and closure.
- Whether appeal is a new substantive vote, a limited review of validity, or a different procedure.
- Who may authorise reconsideration and under what conditions.
- Privacy-preserving protected identity linking across the full event.
- Quorum and office mapping.
- Original standalone Triadic Governance Decision Protocol, still unrecovered.

**Disposition:** Candidate interface for a subsequent portable module revision and targeted negative tests. No automatic appeal, new authority, or jurisdiction is created by this review.
