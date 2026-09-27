# IF-001B — Concord-Internal Candidate Architecture for Non-Single-Provider Civil Reachability

**Status:** V1.2a INVENTION FRONTIER / INTERNALLY GENERATED CANDIDATE  
**External knowledge state:** E2 — CONCORD CANDIDATE FROZEN  
**Date:** September 2026  
**Canonical effect:** NONE  
**Parent brief:** IF-001A  
**External mechanism use:** NONE

# 1. Candidate Name

# **Plural Reachability Mesh (PRM)**

The name is descriptive. The architecture is derived from the frozen IF-001 requirements rather than from an external communications system.

# 2. Central Design Move

The civil system should not store:

Participant
→ Provider Address

as the fundamental relationship.

Instead it should store a participant-controlled, civilly verifiable **Reachability Set**:

Participant Civil Identity
→ Reachability Set R(P)
→ {Delivery Path 1, Delivery Path 2, ... Delivery Path n}.

No individual path constitutes the participant's civil identity or exclusive civil address.

The Reachability Set is itself replaceable and versioned.

# 3. New Abstract Objects

## 3.1 Civil Reachability Descriptor — CRD

A **Civil Reachability Descriptor** is a civil object associated with a participant's persistent identity.

It contains only the minimum information necessary to determine currently valid ways of attempting authorised civil delivery.

It does not need to reveal physical location.

Conceptually:

CRD(P,v)
= {
  participant-reference,
  version,
  valid reachability paths,
  modality constraints/preferences,
  validity conditions,
  recovery/succession conditions,
  provenance
}.

The CRD is not the participant.

It is not citizenship.

It is not a universal behavioural record.

It is a replaceable reachability object.

## 3.2 Reachability Path — RP

A Reachability Path is any currently valid mechanism capable of carrying an authorised civil communication toward the participant.

Different paths may use different:

- providers;
- physical infrastructures;
- devices;
- locations;
- modalities;
- future substrates.

The architecture does not require every path to expose its internal route to the civil identity layer.

## 3.3 Reachability Quorum — RQ

No single provider's statement should be sufficient to permanently redefine a participant's civil reachability where multiple independent confirmation routes are available.

A **Reachability Quorum** is the minimum evidence required to accept a consequential change to the CRD.

The quorum may combine:

- participant authorisation;
- continuity evidence;
- independent path confirmation;
- recovery declarations;
- bounded civil verification.

The quorum is risk-sensitive rather than universally fixed.

## 3.4 Civil Delivery Envelope — CDE

An authoritative civil message is placed into a **Civil Delivery Envelope** containing:

- message identity;
- issuing authority;
- issue time;
- relevant response/deadline rules;
- minimum necessary recipient reference;
- integrity evidence;
- delivery policy;
- provenance.

The envelope is logically independent of the provider carrying it.

Thus:

Message Authority ≠ Carrier Authority.

## 3.5 Delivery Witness — DW

A Delivery Witness is minimal evidence concerning a delivery event.

Possible states include:

- issued;
- path accepted;
- participant endpoint received;
- participant acknowledged;
- delivery failed;
- path unavailable;
- disputed.

A Delivery Witness should reveal no more routing/location information than necessary for the civil consequence attached to that state.

## 3.6 Continuity Hold — CH

If all ordinary paths become unavailable, authoritative communications should not silently disappear or automatically count as delivered.

A **Continuity Hold** preserves:

- the pending envelope;
- its deadline state;
- failed delivery attempts;
- relevant provenance;
- the reason normal delivery is unavailable.

Civil processes can then apply domain-specific rules for pause, alternate notice, escalation or later delivery.

This prevents infrastructure failure from being misrepresented as participant refusal.

## 3.7 Reachability Succession Package — RSP

A **Reachability Succession Package** is the minimum state required to replace a failed/captured provider or migrate the participant's reachability architecture.

It contains:

- current CRD version;
- unresolved CDEs;
- relevant Delivery Witnesses;
- participant-authorised migration state;
- minimum continuity/provenance data.

It should not require transfer of unnecessary historical routing metadata.

# 4. Architecture

The candidate architecture is:

Persistent Civil Identity
→ Versioned Civil Reachability Descriptor
→ Plural Reachability Paths
→ Provider-Independent Civil Delivery Envelope
→ Minimal Delivery Witnesses
→ Participant Receipt / Response
→ Provenance.

Failure path:

Path Failure
→ Try Alternative Valid Path
→ If Sufficient Reachability Remains, Continue
→ If Not, Continuity Hold
→ Recovery / Reachability Quorum
→ Revised CRD
→ Resume Pending Delivery.

Provider failure path:

Provider Failure/Capture
→ Remove/Disable Affected RP
→ Other RPs Remain Valid
→ Generate/Use Reachability Succession Package
→ Establish Replacement RP
→ Update CRD Through Reachability Quorum
→ Resume Unresolved CDEs
→ Preserve Minimal Provenance.

# 5. Why No Single Provider Is Sovereign

A provider can:

- carry a message;
- report bounded delivery state;
- fail;
- be removed.

It cannot merely by being a provider:

- define participant identity;
- unilaterally redefine the whole Reachability Set;
- acquire constitutional authority;
- erase other paths;
- declare unrelated civil status;
- convert routing metadata into general surveillance authority.

This implements:

**Transport Function ≠ Civil Authority.**

# 6. Plurality Rule

Where consequence and infrastructure permit:

|R(P)| ≥ 2

should be preferred for materially important civil reachability.

This is not an absolute constitutional requirement that every participant maintain two active technical channels at every moment.

The deeper requirement is:

> No ordinary single path should be structurally irreplaceable.

Plurality may be achieved through active parallel paths, standby paths, rapidly activatable recovery paths or another functionally equivalent mechanism.

# 7. Participant Control

The participant should normally control:

- preferred paths;
- modality preferences;
- optional redundant paths;
- routine endpoint changes;
- privacy settings within civil constraints;
- withdrawal of obsolete paths.

High-consequence changes may require stronger continuity verification to prevent hostile redirection.

Thus autonomy and anti-hijacking are balanced through Reachability Quorum rather than provider ownership.

# 8. Privacy Architecture

The civil layer should know only what it needs to establish:

- this CRD is valid;
- these paths are currently authorised;
- this envelope was issued;
- this bounded delivery state occurred.

It should not require routine knowledge of:

- participant physical location;
- full network route;
- unrelated communications;
- social graph;
- continuous device history.

The architecture therefore seeks:

Civil Verifiability
without
Universal Routing Visibility.

# 9. Accessibility Architecture

A Reachability Path is defined functionally rather than as a digital endpoint.

Therefore different paths may terminate in:

- direct participant interfaces;
- assistive interfaces;
- authorised human support;
- physical delivery interfaces;
- delayed/store-and-forward interfaces;
- machine-native interfaces;
- future substrate-specific interfaces.

The CDE remains authoritative across modality transformation.

Transformation itself must preserve message meaning and provenance.

# 10. Migration

Migration is not:

Old Provider → Give Entire Account to New Provider.

It is:

Civil Identity
→ Existing CRD
→ Authorised New RP
→ Reachability Quorum
→ New CRD Version
→ Transfer Only Necessary Pending Civil State
→ Retire Old RP.

The Reachability Succession Package carries unresolved civil obligations, not unnecessary provider history.

# 11. Failure Semantics

A major design principle is:

**Infrastructure failure must not silently become participant fault.**

Therefore:

Delivery Failure
≠ Participant Refusal.

Provider Failure
≠ Loss of Civil Identity.

Endpoint Loss
≠ Loss of Civil Standing.

Network Partition
≠ Automatic Waiver of Participant Rights.

This is implemented through Delivery Witness states and Continuity Hold.

# 12. Governance Boundary

Governance may define:

- required assurance levels;
- consequences attached to delivery states;
- emergency rules;
- minimum accessibility standards;
- dispute procedures.

Governance should not ordinarily select the participant's provider or own the participant's routing paths.

Judiciary/review architecture handles material disputes over:

- false delivery claims;
- hostile redirection;
- improper provider action;
- rights consequences;
- contested exceptional access.

# 13. Emergency Access

Emergency access must not require creation of a universal master routing capability.

Where exceptional access is legitimate:

Need
→ Bounded Authority
→ Minimum Necessary Reachability Action
→ Provenance
→ Review
→ Termination.

Exceptional access should affect only the minimum required part of the Reachability Set.

# 14. Frozen Failure-Test Walkthrough

## F1 Provider disappears suddenly

Other RPs remain; affected RP disabled; RSP supports replacement; pending envelopes continue or enter Continuity Hold.

**PASS IN PRINCIPLE.**

## F2 Provider becomes malicious

Provider cannot redefine identity/whole CRD; disputed Delivery Witnesses can be challenged; provider removable.

**PASS IN PRINCIPLE.**

## F3 Resolver/lookup becomes captured

The current candidate reduces but does not fully eliminate this risk. A CRD itself still requires some way of being discovered/verified.

**PARTIAL — IMPORTANT RESIDUAL.**

## F4 Participant changes jurisdiction/location

CRD paths can change without identity change.

**PASS IN PRINCIPLE.**

## F5 Participant loses device/endpoint

Other/standby paths and Reachability Quorum permit recovery.

**PASS IN PRINCIPLE.**

## F6 Network partition/long delay

CDE + Continuity Hold preserve pending state; store/delayed path allowed.

**PASS IN PRINCIPLE.**

## F7 Conflicting/duplicate delivery claims

Message IDs + Delivery Witnesses expose conflict; adjudication/review remains possible.

**PASS IN PRINCIPLE.**

## F8 False non-delivery claim

Bounded witnesses/provenance allow dispute, although evidential implementation remains unresolved.

**PARTIAL/PASS IN PRINCIPLE.**

## F9 Surveillance by infrastructure operator

Provider sees only its path; civil layer minimises route/location data. Collusion/correlation remains a residual technical risk.

**PARTIAL.**

## F10 Participant cannot use default digital modality

Functional RPs permit alternate modality.

**PASS ARCHITECTURALLY; IMPLEMENTATION REQUIRED.**

## F11 Emergency exceptional access

Bounded exceptional action + provenance/review.

**PASS IN PRINCIPLE.**

## F12 Migration with pending notices

RSP explicitly carries unresolved CDE state.

**PASS IN PRINCIPLE.**

## F13 Future technology transition

CRD/RP/CDE abstractions are transport-independent.

**PASS IN PRINCIPLE.**

## F14 Providers disagree about routing state

Versioned CRD + Reachability Quorum provides a conflict-resolution locus.

**PASS IN PRINCIPLE; QUORUM GOVERNANCE REQUIRES DEVELOPMENT.**

## F15 Governance converts routing into participant control

Separation of provider/routing/civil identity/constitutional authority creates an architectural barrier; independent review remains required.

**PASS IN PRINCIPLE.**

# 15. Residual Problems Exposed by the Invention

The candidate does not close everything.

It generates at least four new questions:

### PRM-R1 — Descriptor Discovery Without a New Monopoly

How is the current valid CRD located without creating a single indispensable resolver?

### PRM-R2 — Independent Reachability Quorum

How are quorum participants selected so that the quorum itself does not become the new gatekeeper?

### PRM-R3 — Privacy-Preserving Delivery Evidence

How can sufficient evidence of civil delivery exist without producing a high-resolution surveillance history?

### PRM-R4 — Cross-Modality Semantic Integrity

How is an authoritative CDE transformed across human, assistive, physical and machine modalities without changing legally/civilly relevant meaning?

These may be integration problems, technical research problems or new invention-frontier positions.

# 16. Constraint Fit

C1 persistent identity independence — SATISFIED IN DESIGN.

C2 no indispensable ordinary provider — SATISFIED IN DESIGN, subject to PRM-R1.

C3 provider failure does not destroy addressability — SATISFIED IN DESIGN.

C4 migration without identity reconstruction — SATISFIED.

C5 authoritative messages without carrier sovereignty — SATISFIED.

C6 bounded delivery evidence — PARTIAL; PRM-R3.

C7 privacy/minimal routing exposure — SATISFIED AS REQUIREMENT, implementation unresolved.

C8 multisubstrate — SATISFIED ARCHITECTURALLY.

C9 multimodality — SATISFIED ARCHITECTURALLY; implementation unresolved.

C10 carrier ≠ civil authority — SATISFIED.

C11 bounded exceptional/admin access — SATISFIED BY INTERFACE TO EXISTING CONCORD GRAMMAR.

C12 migration preserves pending obligations — SATISFIED THROUGH RSP.

C13 no silent loss/duplication — SATISFIED IN MODEL THROUGH CDE/DW/CH; implementation requires testing.

C14 future technology independence — SATISFIED.

C15 corrigibility/replaceability — SATISFIED.

# 17. Generative Result

The topology did not merely return:

“Use multiple providers.”

It generated a candidate object model:

- Civil Reachability Descriptor;
- Reachability Path;
- Reachability Quorum;
- Civil Delivery Envelope;
- Delivery Witness;
- Continuity Hold;
- Reachability Succession Package.

Together they create a proposed civil communications architecture whose governing relation is:

**Identity persists; reachability changes; carriers remain replaceable; civil meaning survives transport change.**

# 18. Freeze and External Knowledge State

This candidate is now frozen as the first Concord-internal response to IF-001.

External knowledge state advances:

**E0 → E2**

without an E1 mechanism search.

That is intentional: no external existence/mechanism search was performed before generation.

External mechanism details may now be examined in a later E3 comparison without contaminating this candidate's generative independence.

# 19. Experimental Claim

This document does not claim that PRM is novel, technically optimal or implementable as written.

It establishes a narrower result:

> Given a topology-derived invention position and frozen constraints, the Concord-internal generative process produced a coherent candidate architecture with explicit objects, flows, failure handling and residual problems without importing an external mechanism.

Whether that candidate converges with, differs from or underperforms existing real-world architectures is a separate E3 experiment.
