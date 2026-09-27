# IF-003B — Concord-Internal Candidate Architecture — Civil Meaning Envelope

**Status:** V1.2a INVENTION FRONTIER / INTERNALLY GENERATED CANDIDATE  
**External knowledge state:** E2 — CONCORD CANDIDATE FROZEN  
**Date:** September 2026  
**Canonical effect:** NONE  
**Parent brief:** IF-003A  
**External mechanism use:** NONE

# 1. Candidate Name

# **Civil Meaning Envelope (CME)**

# 2. Central Design Move

An authoritative civil communication should not be defined by one presentation format.

It should contain a protected **Civil Meaning Core** plus one or more replaceable **Presentation Realisations**.

Thus:

Civil Meaning
≠ Text
≠ Audio
≠ Visual Form
≠ Machine Encoding.

The civil object persists while presentation adapts.

# 3. Civil Meaning Core — CMC

The CMC contains the civilly significant propositions of the communication in structured form, for example:

- issuer;
- recipient reference;
- purpose;
- required/optional action;
- rights affected;
- deadline;
- consequence;
- available challenge/review;
- response routes;
- uncertainty/qualification;
- provenance.

Not every message requires every field.

The purpose is to distinguish legally/civilly significant meaning from formatting.

# 4. Presentation Realisation — PR

A Presentation Realisation renders the CMC into a modality usable by the participant.

Possible forms may include:

- ordinary human-readable text;
- simplified text;
- audio;
- tactile/physical form;
- assisted human interface;
- structured machine-readable form;
- substrate-specific future representation.

The architecture does not assume these are semantically identical merely because they derive from the same source.

# 5. Meaning-Preservation Record — MPR

Every consequential transformation records:

Source CMC
→ Transformation
→ Presentation Realisation
→ transformation provenance.

Where transformation is automated or mediated, the record identifies enough information to permit later review.

# 6. Comprehension Opportunity State — COS

The architecture must distinguish:

- transmitted;
- endpoint received;
- presentation available;
- accessibility-compatible presentation available;
- participant acknowledged;
- participant indicates non-comprehension/dispute;
- response received.

This prevents:

Endpoint Received
→ Automatically Deemed Meaningfully Received.

# 7. Accessible Response Envelope — ARE

Participant response can originate through a different modality from the incoming communication.

The response is converted into its own civil meaning object with provenance.

Thus:

Accessible Participant Expression
→ Response Meaning Core
→ Authoritative Civil Response.

An intermediary assists transmission, not ownership of the participant's decision.

# 8. Semantic Challenge

A participant may challenge:

- mistranslation;
- inaccessible presentation;
- omitted material meaning;
- misleading simplification;
- incorrect machine/human transformation;
- intermediary distortion.

A material challenge can suspend consequences where appropriate until the disputed meaning is reviewed.

# 9. Modality Fallback

Participant preferences define ordinary delivery.

If the preferred modality fails and consequence is material:

Preferred PR
→ Failure
→ Alternative Authorised PR
→ if still unavailable, protected non-delivery/accessibility state
→ escalation according to consequence.

Inability to access one modality is not refusal.

# 10. Privacy Boundary

Accessibility support receives only information necessary to perform the transformation/support function.

Assistive access does not imply general access to:

- unrelated records;
- participant history;
- full civil identity data;
- other communications.

Where an intermediary is required, its access is purpose-bounded and provenance-recorded.

# 11. Machine and Future Substrates

A machine participant need not be forced through a human sensory representation.

The same CMC can produce a structured PR appropriate to that participant.

Conversely, a machine-generated civil communication intended for a human must be rendered into a human-accessible PR without treating the machine's internal representation as sufficient notice.

# 12. Frozen Failure Tests

F1 cannot read text — alternate PR. **PASS.**

F2 cannot hear audio — alternate PR. **PASS.**

F3 cannot use digital device — physical/assisted PR permitted. **PASS ARCHITECTURALLY.**

F4 machine requires structured representation — machine PR. **PASS.**

F5 translation changes meaning — CMC + MPR + semantic challenge. **PASS IN PRINCIPLE.**

F6 intermediary misrepresents — bounded intermediary + provenance + challenge. **PASS IN PRINCIPLE.**

F7 privacy exposed — minimum-purpose accessibility boundary. **PASS ARCHITECTURALLY.**

F8 urgent inaccessible channel — modality fallback/escalation. **PASS.**

F9 response transformed incorrectly — response meaning core + provenance/challenge. **PASS IN PRINCIPLE.**

F10 modalities conflict — CMC provides common civil reference; dispute remains reviewable. **PASS IN PRINCIPLE.**

F11 future substrate — PR abstraction is substrate-neutral. **PASS ARCHITECTURALLY.**

F12 temporary capability loss — alternate PR/fallback. **PASS.**

F13 endpoint received data — COS prevents automatic equivalence to meaningful receipt. **PASS.**

F14 adaptation service unavailable — fallback paths; complete resilience depends on implementation. **PARTIAL.**

F15 later dispute — MPR + COS reconstruct what representation was supplied and its status. **PASS IN PRINCIPLE.**

# 13. Residuals

### CME-R1 — Formalising the Civil Meaning Core

How can civilly significant meaning be represented precisely enough for transformation without falsely implying that all human meaning can be completely formalised?

### CME-R2 — Equivalence Testing Across Modalities

What constitutes sufficient preservation of meaning when sensory/cognitive representations differ radically?

### CME-R3 — Accessibility Without New Gatekeepers

How are transformation services made replaceable/plural so accessibility infrastructure does not become a new point of dependence?

### CME-R4 — Comprehension Without Mind-Reading

The system can establish opportunity/accessibility and participant acknowledgement, but cannot directly prove subjective comprehension.

The architecture must avoid converting a legitimate accessibility requirement into intrusive testing of thought.

# 14. Constraint Fit

C1–C6: satisfied in design through CMC/PR/MPR.
C7: privacy boundary explicit.
C8: intermediary authority bounded.
C9: substrate-neutral PR.
C10: inaccessible channel ≠ refusal.
C11: fallback/escalation.
C12: meaning rather than identical sensory form.
C13: participant modality preferences.
C14: semantic challenge.
C15: new PR types can be added without redefining identity.

# 15. Deeper Architectural Result

IF-003 produces a potentially general relation:

> **For consequential civil communication, the authoritative object should be the preserved civil meaning and provenance, not any one representation of that meaning.**

This may extend beyond accessibility into:

- language translation;
- human–AI communication;
- intercivilisational communication;
- legal notices;
- constitutional texts;
- machine-readable governance;
- future substrate translation.

That broader applicability is a later hypothesis and is not established by this invention test.

# 16. Freeze

CME is frozen as the Concord-internal IF-003 candidate.

External knowledge state:

**E0 → E2**

No external solution search was performed before generation.

No claim of novelty, optimality or technical completeness is made.
