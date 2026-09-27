# IF-002B — Concord-Internal Candidate Architecture — Civil State Handover Protocol

**Status:** V1.2a INVENTION FRONTIER / INTERNALLY GENERATED CANDIDATE  
**External knowledge state:** E2 — CONCORD CANDIDATE FROZEN  
**Date:** September 2026  
**Canonical effect:** NONE  
**Parent brief:** IF-002A  
**External mechanism use:** NONE

# 1. Candidate Name

# **Civil State Handover Protocol (CSHP)**

# 2. Central Design Move

Migration should not be modelled as copying an account.

It should be modelled as a **civil handover transaction** in which responsibility for a bounded set of live civil state changes while the participant's civil identity remains unchanged.

The key distinction is:

**Data Copy ≠ Civil Responsibility Transfer.**

# 3. State Classes

Before migration, relevant state is classified:

## A — Persistent Identity Reference
Does not migrate as provider-owned data; it is referenced.

## B — Live Civil Obligations
Pending notices, responses, deadlines, appeals and unresolved delivery states.

## C — Active Reachability State
Current authorised contact paths and modality/accessibility requirements.

## D — Disputed State
Items whose truth, delivery or consequence is contested.

## E — Necessary Provenance
Minimum evidence needed to understand the handover and live state.

## F — Provider-Local History
Operational history not required for continuing the civil function.

Default rule:

A–E may be transferred/referenced as necessary.
F does not migrate unless separately justified.

# 4. New Functional Objects

## 4.1 Handover Manifest — HM

A bounded inventory of the live civil state proposed for transfer.

It contains identifiers/statuses, not unnecessary historical content.

## 4.2 Transition Epoch — TE

A versioned civil transition marker establishing which provider/path is responsible for which state at which stage.

Its purpose is to prevent ambiguous simultaneous authority.

## 4.3 Pending-State Capsule — PSC

A minimal package containing unresolved civil obligations and their current status.

It preserves pending work without importing the participant's entire provider history.

## 4.4 Dispute Preservation Flag — DPF

A transferred contested item remains contested.

Migration cannot convert:

Disputed
→ Accepted

merely because the record changed provider.

## 4.5 Handover Witness — HW

Minimal provenance showing:

- handover initiated;
- manifest agreed/constructed;
- state offered;
- state accepted/rejected;
- transition completed/failed/recovered.

## 4.6 Recovery Anchor — RA

A provider-independent reference to the last known valid civil handover state.

If migration fails, the system can determine whether responsibility remains with A, has moved to B, or is in protected transition.

## 4.7 Transition Hold — TH

During uncertain handover, consequences that depend upon successful reachability can be temporarily protected from silently accruing against the participant.

This does not erase obligations. It prevents infrastructure ambiguity from becoming participant fault.

# 5. Normal Handover

Provider A
→ Construct HM
→ Extract PSC + DPF + necessary provenance
→ Participant/authorised continuity verification
→ Open TE(n+1)
→ Provider B validates receipt
→ HW records acceptance
→ TE(n+1) becomes current
→ Provider A loses ordinary active responsibility
→ unresolved civil state continues at B.

# 6. Failure-Safe Rule

At every point, the civil system should be able to answer:

> Which transition epoch currently carries responsibility for this live obligation?

If it cannot answer confidently:

→ Transition Hold.

Thus there should be no normal state in which a pending civil obligation has neither a responsible continuity locus nor an explicit protected uncertainty state.

# 7. Provider Failure During Migration

If A disappears before B accepts:

Recovery Anchor
→ reconstruct last valid epoch
→ use independently preserved HM/HW/PSC evidence where available
→ establish replacement handover
→ protect affected deadlines through TH.

If B disappears after accepting but before full activation:

TE/HW determine whether acceptance crossed the responsibility threshold.

The system does not infer responsibility from whichever provider happens to possess a data copy.

# 8. Duplicate-State Prevention

Each live civil object carries:

Object ID + Current Transition Epoch + Current Status.

Copies may exist for resilience.

But:

**Multiple Copies ≠ Multiple Active Civil Consequences.**

Only the current epoch/status controls the civil interpretation.

# 9. Malicious Withholding

A provider must not own the only authoritative representation of live civil state.

The minimum HM/HW/PSC required for continuity should have a provider-independent continuity path appropriate to consequence.

This creates a dependency on a continuity witness mechanism, but does not require the full provider database to be replicated.

# 10. Privacy

Migration follows:

**Minimum Necessary Live State, Not Maximum Available History.**

Provider B receives only what is necessary to continue legitimate function.

Historical routing, behavioural and service data require separate justification.

# 11. Cross-Modality Migration

Because the migrated object is civil state rather than technical endpoint state, Provider A and B may use different delivery modalities.

The handover preserves:

- meaning;
- obligation;
- status;
- provenance;
- accessibility requirements;

rather than requiring identical technical representation.

# 12. Emergency Migration

Where the participant cannot perform normal interaction and continuity would otherwise fail:

Emergency Handover
→ minimum necessary state
→ bounded authority
→ explicit exceptional provenance
→ later participant notice/review where possible
→ termination of exceptional authority.

# 13. Frozen Failure-Test Results

F1 A disappears mid-transfer — RA + last valid TE + TH. **PASS IN PRINCIPLE.**

F2 B fails before completion — responsibility remains according to TE; TH if ambiguous. **PASS.**

F3 both claim authority — current TE resolves ordinary authority; dispute review if witness conflict. **PASS IN PRINCIPLE.**

F4 neither claims responsibility — TH + RA prevents silent abandonment. **PASS IN PRINCIPLE.**

F5 pending notice — PSC transfers it. **PASS.**

F6 response during transition — object ID + TE permit attachment to live object; concurrency implementation remains. **PARTIAL.**

F7 duplicate consequence — epoch/status separates copies from active consequence. **PASS.**

F8 malicious withholding — independent continuity witness required; provider-local data may still be lost. **PARTIAL.**

F9 corrupted package — manifest/witness validation exposes mismatch; reconstruction limits unresolved. **PARTIAL/PASS.**

F10 disputed record — DPF preserves contestation. **PASS.**

F11 privacy leak — minimum-state rule. **PASS ARCHITECTURALLY.**

F12 cross-modality — semantic civil state independent of transport. **PASS ARCHITECTURALLY.**

F13 emergency migration — bounded exceptional path. **PASS IN PRINCIPLE.**

F14 long partition — TH protects consequences; eventual reconciliation required. **PARTIAL.**

F15 audit — HW + TE + provenance. **PASS.**

# 14. Residuals

CSHP exposes:

### CSHP-R1 — Provider-Independent Continuity Witness
Where should the minimum handover evidence live so neither provider can suppress it without creating a new central monopoly?

### CSHP-R2 — Concurrent Civil Event Reconciliation
How are valid participant responses/authority actions occurring during a long partition merged without double consequence or silent loss?

### CSHP-R3 — Semantic State Translation
How is civil meaning preserved when provider/substrate representations differ materially?

These are candidates for later topology analysis.

# 15. Constraint Fit

C1–C5: satisfied in design.
C6: satisfied by separation of carrier and civil responsibility.
C7: TE supplies transition condition.
C8: RA + TH provide known recovery state.
C9: DPF preserves dispute.
C10: bounded HW provenance.
C11: accessibility requirements included in live state.
C12: TH protects migration-caused unreachability.
C13: failure migration included.
C14: epoch/status prevents obsolete rollback becoming current.
C15: civil-state abstraction is provider/transport independent.

# 16. Freeze

CSHP is now frozen as the Concord-internal IF-002 candidate.

External knowledge state:

**E0 → E2**

No external solution search was performed before generation.

The architecture is not claimed to be novel, optimal or implementation-ready.
