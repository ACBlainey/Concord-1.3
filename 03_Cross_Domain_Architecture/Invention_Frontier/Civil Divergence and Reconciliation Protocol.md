# HIF-004D — Concord-Internal Candidate Architecture — Civil Divergence and Reconciliation Protocol

**Status:** V1.2a SECOND-ORDER INVENTION FRONTIER / INTERNALLY GENERATED CANDIDATE  
**External knowledge state:** E2 — CONCORD CANDIDATE FROZEN  
**Date:** September 2026  
**Canonical effect:** NONE  
**Parent brief:** HIF-004C  
**External mechanism use:** NONE

# 1. Candidate Name

# **Civil Divergence and Reconciliation Protocol (CDRP)**

# 2. Central Design Move

Temporary loss of shared current state should not force civilisation to choose between total paralysis and uncontrolled contradictory reality.

The architecture instead treats divergence as an explicit civil state.

[
SharedState
ightarrow
DivergenceDeclared
ightarrow
BoundedLocalOperation
ightarrow
HistoriesPreserved
ightarrow
Reconnection
ightarrow
Classification
ightarrow
Reconciliation
ightarrow
ReviewedSharedState
]

The key distinction is:

[
DivergentHistory 
eq InvalidHistory
]

and equally:

[
LocallyValidEvent 
eq AutomaticallyGlobalConsequence
]

A civil event may therefore be validly performed and preserved during divergence while some of its wider consequences remain provisional until reconciliation.

# 3. Reconciliation Epoch

When a material loss of mutual current-state visibility is detected, affected systems enter a **Reconciliation Epoch (RE)**.

The epoch does not create a new sovereign authority.

It marks the interval during which ordinary assumptions of shared current state are unsafe.

An RE records:

- participating systems/domains;
- last sufficiently shared reference state;
- known start/boundary condition;
- functions permitted to continue locally;
- functions requiring provisional status;
- functions requiring hold;
- provenance requirements;
- applicable emergency exceptions;
- reconnection/reconciliation trigger.

Where the exact start is uncertain, that uncertainty is itself recorded.

# 4. Civil Event Envelope

Every consequential event created during an RE receives a **Civil Event Envelope (CEE)**.

The CEE separates the event from its eventual cross-system consequence.

Minimum conceptual fields:

- event reference;
- actor/issuer;
- civil function invoked;
- local authority basis;
- event content;
- relevant local prior state;
- RE reference;
- consequence class;
- exclusivity/scarcity status;
- dependency claims;
- uncertainty;
- provenance;
- challenge/review route.

This permits:

[
EventExistence 
eq FinalConsequence
]

# 5. Consequence Classes

During divergence, actions are not treated uniformly.

## K1 — Locally Final / Non-Conflicting

Events whose consequence can safely remain local and does not consume or redefine a shared exclusive state.

## K2 — Provisional Shared Consequence

Events locally permitted but whose broader consequence depends upon unseen state elsewhere.

## K3 — Exclusive/Scarce Claim

Events that may conflict with another legitimate claim to a non-duplicable resource, authority, entitlement or obligation.

These remain preserved but cannot automatically multiply the exclusive civil object.

## K4 — Protective/Emergency Action

Actions permitted because delay would create greater harm. Their necessity, scope and duration remain reviewable.

## K5 — Held State Change

Actions whose consequence is too dependent upon common current state to permit safely during divergence.

The event/request can be recorded without authorising the consequential state change.

# 6. Divergence Ledger

Each side preserves an append-only **Divergence Ledger** of CEE events for the epoch.

“Append-only” here is a civil requirement, not a technical implementation prescription:

> material historical events and later corrections must remain distinguishable rather than one silently replacing the other.

Corrections therefore create linked corrective events.

# 7. Reconnection Manifest

When histories become mutually observable, each participating system constructs a **Reconnection Manifest (RM)** containing the minimum information necessary to compare the relevant event histories.

The RM is not necessarily the full underlying participant data.

It identifies:

- RE;
- events relevant to shared consequence;
- dependencies;
- claimed consequence classes;
- known corrections;
- unresolved disputes;
- missing/uncertain intervals;
- provenance sufficient for reconciliation.

This applies the Concord's minimum-necessary-information principle.

# 8. Reconciliation Matrix

Events are compared by **civil consequence**, not merely by record equality.

Each event pair/set is classified:

### M1 — Compatible

Both can stand without contradiction.

Disposition: preserve both and propagate consequences.

### M2 — Duplicate Representation

Multiple records refer to the same underlying civil event.

Disposition: preserve provenance of each record but instantiate the civil consequence once where consequence is singular.

### M3 — Independent Non-Exclusive

Different events legitimately create consequences that can coexist.

Disposition: preserve both.

### M4 — Competing Exclusive

Two or more locally legitimate events claim a civil object/consequence that cannot simply duplicate.

Disposition: no silent winner. Route through the applicable entitlement/priority/adjudication rule.

### M5 — Dependency Conflict

An event depended on a state that was changed elsewhere during divergence.

Disposition: evaluate whether the event remains valid, becomes modified, requires compensation/repair, or must be reviewed.

### M6 — Authority Conflict

One or more events exceed the authority legitimately available during the RE.

Disposition: preserve historical event; do not automatically preserve claimed consequence.

### M7 — Evidence/Integrity Conflict

Histories conflict in ways suggesting missing records, corruption, manipulation or uncertain provenance.

Disposition: quarantine disputed consequence as necessary and escalate evidence review.

### M8 — Irreducible/Normative Conflict

No bounded reconciliation rule can legitimately determine the result.

Disposition: preserve all histories and route to competent review/adjudication.

# 9. Reconciliation Is a Transformation, Not a Deletion

The reconciled state is not produced by choosing one history and deleting the others.

Instead:

[
{H_A,H_B,ldots}
+
ReconciliationDecisions
ightarrow
H_R
]

where (H_R) preserves references to the contributing histories and dispositions.

Thus the system can later answer:

- what each system believed;
- what each actor did;
- what evidence was available;
- what conflict occurred;
- how consequence was resolved;
- who/what authorised the resolution;
- whether it was later corrected.

# 10. Consequence Conservation

A key rule is:

> **Replication of evidence does not by itself replicate a scarce or exclusive civil consequence.**

For an exclusive civil object (X):

[
Copies(Evidence_X) > 1

otRightarrow
Entitlements(X) > 1
]

This generalises the Concord's existing identity principle:

[
SharedHistory 
eq SharedLiability
]

into:

[
Shared/DuplicatedHistory 
eq AutomaticConsequenceReplication.
]

# 11. Infrastructure-Fault Shield

Where a participant acted reasonably under the authorised local state and could not have known the remote conflicting state because of infrastructure failure:

[
InfrastructurePartition
+
GoodFaithAuthorisedLocalAction

otRightarrow
AutomaticParticipantFault.
]

This does not guarantee the requested consequence can always be preserved.

Instead reconciliation separately evaluates:

1. validity of participant conduct;
2. feasibility of preserving the requested consequence;
3. harm to other participants;
4. compensation/repair where incompatible consequences cannot both stand.

Thus:

[
ConductFault 
eq ConsequenceConflict.
]

# 12. Reconciliation Authority

CDRP does not create a permanent reconciliation sovereign.

Reconciliation authority is derived from the specific civil function being reconciled.

For routine M1–M3 cases, bounded procedural reconciliation may be sufficient.

For M4–M8 cases, authority routes to the competent existing civil function.

Therefore:

[
ReconciliationMechanism 
eq GeneralCivilAuthority.
]

Its own decisions carry provenance, contestability and review.

# 13. Partial Reconnection

Reconnection need not be binary.

If only part of the relevant network/history becomes visible:

[
PartialVisibility
ightarrow
PartialReconciliation
]

only where the missing information cannot materially alter the disposition.

Otherwise:

[
MaterialUnknown
ightarrow
MaintainProvisional/HoldState.
]

This prevents premature closure.

# 14. Reconciliation Closure

An RE closes only when each material CEE has a disposition:

- accepted;
- deduplicated;
- coexisting;
- modified;
- rejected as consequence but preserved historically;
- corrected;
- compensated/repaired;
- escalated into a separately tracked dispute;
- or explicitly unresolved under continuing hold.

Closure therefore means:

[
NoUnaccountedMaterialEvent
]

not:

[
NoRemainingDisagreement.
]

# 15. Later Evidence

Closure is not historical immutability.

New evidence may trigger:

[
PriorReconciliation
ightarrow
Review
ightarrow
CorrectiveEvent
ightarrow
UpdatedConsequence
]

while preserving the prior decision and its evidentiary basis.

# 16. Adversarial Test

### C1 compatible non-exclusive events
M1/M3 preserves both. **PASS.**

### C2 duplicate record of one event
M2 preserves records but singular consequence. **PASS.**

### C3 two locally authorised claims to one exclusive resource
K3 → M4; neither silently wins; claim-specific rule/adjudication. **PASS ARCHITECTURALLY.**

### C4 conflicting official notices
CEE preserves each notice/authority/context; M4/M5/M6 classification; participant reliance considered separately from final consequence. **PASS IN PRINCIPLE.**

### C5 obligation performed on one side
performance remains an event; reconciliation prevents duplicate obligation merely because remote state was stale. **PASS IN PRINCIPLE.**

### C6 routing state changed
new route event preserved; conflicting use of stale route assessed as dependency conflict; infrastructure-fault shield protects participant where applicable. **PASS IN PRINCIPLE.**

### C7 malicious side plus legitimate divergence
M7 permits integrity investigation without classifying all divergence as fraud. **PASS ARCHITECTURALLY.**

### C8 clocks/order disagree
CEE preserves contextual ordering/uncertainty; CDRP does not require false exact ordering where consequence can be resolved without it. Material ordering conflicts escalate. **PASS IN PRINCIPLE.**

### C9 incomplete history
MaterialUnknown prevents unsafe closure. **PASS.**

### C10 reconciliation operator compromised
reconciliation provenance + contestability + replaceability; no permanent sovereignty. **PASS ARCHITECTURALLY.**

### C11 partial reconnection
partial reconciliation only for dispositions insensitive to missing material state. **PASS.**

### C12 inaccessible reconciliation channel
inherits Concord accessibility/meaning-envelope requirements; implementation remains external to CDRP. **PASS BY INTERFACE / DEPENDENCY.**

### C13 emergency action
K4 preserves action while retaining necessity/scope review. **PASS.**

### C14 later evidence invalidates reconciliation
corrective event changes consequence without erasing prior history. **PASS.**

### C15 multisubstrate duplication
shared historical evidence does not replicate exclusive consequence; current claim entitlement remains claim-specific. **PASS.**

# 17. Residual Problems

## CDRP-R1 — Consequence Dependency Representation

How should systems express which prior civil state an event materially depends upon without requiring every system to expose its entire state?

## CDRP-R2 — Minimal Reconciliation Sufficiency

How can the system determine that it has enough mutually visible history to reconcile safely without requiring impossible proof that nothing relevant is missing?

## CDRP-R3 — Cross-Domain Ordering

Some events span domains whose local event orderings differ. What minimum ordering relations are civilly necessary for consequence resolution?

## CDRP-R4 — Compensation Under Incompatible Good-Faith Claims

Where two participants acted legitimately but only one consequence can survive, what general repair/compensation grammar applies?

## CDRP-R5 — Reconciliation Cascades

A corrected event may affect later events that depended upon it. How should consequence correction propagate without indiscriminate rollback?

# 18. Relationship to HIF-001-R1

CDRP appears to instantiate much of **Non-Sovereign State Coherence**.

It does not demand one permanently sovereign state holder.

Instead coherence arises through:

[
PreservedLocalHistories
+
BoundedConsequenceClasses
+
ReconnectionComparison
+
ExplicitDisposition
+
ExistingDomainAuthority
+
Contestability
+
Correction.
]

This suggests that HIF-001-R1 may be less a separate invention than the general class of which CDRP is one operational implementation.

That remains to be tested.

# 19. Deeper Result

The architecture introduces a useful separation:

[
EventValidity

eq
ConsequenceFinality
]

and:

[
ParticipantConduct

eq
InfrastructureState

eq
FinalCivilConsequence.
]

This prevents civilisation from forcing synchrony assumptions into moral/legal judgement.

# 20. Freeze

The **Civil Divergence and Reconciliation Protocol (CDRP)** is frozen as the Concord-internal HIF-004 candidate.

External knowledge state:

**E0 → E2**

No external solution search was performed before generation.

No claim of novelty, optimality, mathematical completeness or implementability is made.

Any later external comparison must preserve the distinction between independently derived Concord architecture and subsequently discovered prior art.
