# Historical Domain — Cross-Domain Interface Test 002 — Judiciary, Governance and the Historical Event Spine

**Project:** The Concord  
**Domain:** Historical  
**Status:** CROSS-DOMAIN INTERFACE TEST / DEVELOPMENT  
**Date:** 25 September 2026  
**Target:** Historical Domain — Formal Domain Specification v0.2  
**Compared systems:** Judiciary V2; Governance V2; KCS dependency/change-propagation architecture; Historical Event Spine candidate  
**Purpose:** Test whether Historical can preserve constitutional authority, jurisdiction, decisions and cross-domain consequences without acquiring, recreating or accidentally extending the authority it records.

---

# 1. Test Question

Historical must be able to answer:

- who or what possessed authority at time T;
- what the claimed source of that authority was;
- what jurisdictional limits applied;
- what decision was made;
- what evidence/reasoning was recorded;
- whether the decision was appealed, constrained, superseded, invalidated or later reinterpreted;
- what downstream effects followed.

It must answer those questions without itself becoming a source of authority.

The critical distinction is:

> **Historical Evidence of Authority ≠ Present Authority.**

---

# 2. Judiciary ↔ Historical

Judiciary V2 defines judicial authority as delegated constitutional authority held through an office and bounded by jurisdiction.

It explicitly rejects the idea that expertise, prestige, necessity, historical practice or institutional importance manufactures authority.

It also distinguishes:

- judicial judgement from judicial architecture;
- constitutional constraint from executive substitution;
- ordinary adjudication from constitutional adjudication;
- finality from infallibility;
- current canonical architecture from validated truth.

These distinctions are highly compatible with Historical.

## Judiciary owns

- live judicial jurisdiction;
- adjudication;
- findings of fact within judicial process;
- interpretation of law;
- constitutional interpretation within legitimate jurisdiction;
- determination of rights and obligations;
- remedies;
- appeals and judicial review;
- current binding legal/judicial status.

## Historical owns

- preservation of the case state and its transitions;
- provenance of evidence, judgement and reasoning;
- historical jurisdiction/authority state;
- previous holdings and remedies;
- later appeal, reversal, supersession or correction history;
- reconstruction of what the Judiciary knew and could represent at the relevant time;
- long-term pattern analysis subject to non-causal and privacy constraints.

## Core boundary

Historical may preserve:

```text
Court X held at T1 that P.
```

Historical must not silently transform this into:

```text
P is currently legally binding.
```

The first is a historical statement.

The second is a current legal-status claim requiring the current authoritative judicial/legal system.

### Result J-H1 — PASS

The boundary is coherent.

---

# 3. Authority Is a Time-Bounded State

The Judiciary test exposes a necessary Historical object class:

## Authority-State Record

Candidate fields:

- authority_state_id;
- institution/office;
- holder where legitimately recordable;
- authority type;
- source of authority;
- jurisdiction;
- effective start;
- effective end or current-state reference;
- delegation chain;
- constraints;
- emergency status if applicable;
- contested/disputed status;
- judicial review status;
- supersession/revocation relation;
- provenance;
- access/privacy classification.

This does not create authority.

It records that an authority state existed or was claimed to exist.

Therefore:

> **Authority Record ≠ Authority Grant.**

---

# 4. Claimed, Exercised and Legitimate Authority Must Remain Distinct

Historical material frequently contains assertions of authority.

An actor may claim authority it does not possess.

An institution may possess authority but exceed its jurisdiction.

An action may occur before a court later determines it unlawful.

Therefore Historical requires at least:

```text
Claimed Authority
Exercised Authority
Contemporaneously Recognised Authority
Later-Adjudicated Authority
Current Authoritative Interpretation
```

These must not be collapsed.

Example:

At T1 Governance claims emergency authority and acts.

At T2 a Constitutional Court rules that part of the action exceeded delegated authority.

Historical must preserve both:

- the fact that authority was claimed/exercised at T1;
- the later legal determination at T2.

It must not rewrite T1 as though the T2 determination was already known.

### Result J-H2 — PASS WITH REQUIRED STATE SEPARATION

This is a direct application of Historical's non-retrospective reconstruction rule.

---

# 5. Judicial Findings and Historical Reality

Judiciary determines facts for legal purposes through evidence and procedure.

Historical must preserve those findings accurately.

But:

> **Judicial Finding ≠ Ontological Guarantee.**

A finding may later be overturned, undermined by new evidence, or remain legally final despite epistemic uncertainty.

Historical should therefore represent:

```text
Event/Claim
→ Evidence State
→ Judicial Finding
→ Legal Consequence
→ Appeal/Review State
→ Later Evidence
→ Later Judicial or Historical Interpretation
```

A court's finding is historically important partly because it exercised legitimate authority.

Its authority does not make every proposition it contains eternally true.

### Result J-H3 — PASS

Historical's existing Claim ≠ Finding and Record ≠ Reality distinctions are sufficient if formally applied.

---

# 6. Finality, Supersession and Correction

Judicial systems require some decisions to become operationally final.

Historical must not confuse finality with epistemic certainty.

Therefore:

> **Procedural Finality ≠ Historical Infallibility.**

Historical may preserve later evidence or scholarship concerning a final case while clearly retaining the case's legal status.

Likewise:

> **Later Reinterpretation ≠ Retroactive Mutation.**

If a precedent is superseded, Historical preserves:

- original precedent;
- period of applicability;
- cases relying on it where reconstructably linked;
- superseding decision;
- current legal status reference.

This is naturally representable through the KCS relation types already available, including SUPERSEDES, CORRECTS, EVIDENCES and PROPAGATES_TO.

---

# 7. Governance ↔ Historical

Governance is the Concord system that exercises legitimate public decision authority within constitutional limits.

Historical therefore faces the same core risk as with Judiciary:

preserving Governance decisions so completely that the archive begins to look like the government.

## Governance owns

- current delegated public authority;
- policy choice within legitimate constitutional scope;
- executive action;
- current appointments/delegations;
- resource decisions;
- operational administration;
- current governance status.

## Historical owns

- past governance state;
- past office/delegation state;
- decision provenance;
- policy history;
- recorded reasons and alternatives where preserved;
- implementation history;
- subsequent consequences;
- later correction/repeal/supersession;
- reconstruction of the information/evaluation space available when the decision was made.

## Core boundary

> **Historical may reconstruct a government. It may not become the government it reconstructs.**

### Result G-H1 — PASS

No intrinsic authority collision exists if current state is resolved through the authoritative Governance system.

---

# 8. Historical Authority Decay

A significant new issue appears when authority-bearing records are archived.

A document may once have been:

- an active executive order;
- a judicial injunction;
- a valid delegation;
- an emergency authorisation;
- an appointment instrument;
- a binding policy;
- a warrant;
- a constitutional determination.

After expiry, revocation, supersession or jurisdictional change, the same document remains historically authentic but may no longer possess operational force.

Historical therefore needs a concept of **authority decay** or, more neutrally, **authority-state transition**.

The content does not cease to exist.

Its operational authority changes.

```text
Authenticity may persist
while
Operational Authority expires.
```

This yields:

> **Persistent Record ≠ Persistent Authority.**

### Result G-H2 — NEW REQUIRED INVARIANT

Historical retrieval interfaces must expose historical authority state prominently enough to prevent obsolete authority-bearing records from being mistaken for current commands.

---

# 9. Retrieval Must Not Reactivate Authority

Consider an archived emergency order that once instructed infrastructure operators to perform action X.

A future search retrieves it.

If a machine system interprets the preserved imperative as a live command, archival retrieval has accidentally reactivated dead authority.

Therefore:

> **Historical Retrieval ≠ Operational Reactivation.**

This existing Historical invariant now becomes a constitutional safety requirement rather than merely an archival convenience.

Authority-bearing historical objects should carry machine-readable status sufficient to distinguish, where known:

- ACTIVE_CURRENT;
- EXPIRED;
- REVOKED;
- SUPERSEDED;
- INVALIDATED;
- HISTORICAL_ONLY;
- STATUS_UNKNOWN;
- STATUS_DISPUTED.

The exact vocabulary remains an implementation candidate, but the distinction is mandatory.

---

# 10. Governance Decision Reconstruction

For consequential Governance decisions, Historical should be capable of reconstructing:

```text
Authority Source
+ Jurisdiction
+ Decision Context
+ Evidence Available
+ Evaluation Architecture
+ Alternatives Considered
+ Recorded Reasoning
+ Decision
+ Implementation
+ Outcome
+ Review/Challenge
+ Later Correction
```

Not every minor operational decision requires this depth.

The requirement is proportional.

The more consequential, irreversible or constitutionally significant the decision, the stronger the case for preserving its evaluation context.

This aligns with ESCP:

> a later observer should not assume the historical decision-maker possessed dimensions that were not available or represented at the time.

---

# 11. The Event Spine Against KCS

Interface Test 001 proposed:

```text
Source Event
→ Domain Transition
→ Knowledge Change
→ Dependency Effect
→ Authority/Decision
→ Operational Outcome
→ Later Correction
```

KCS already supplies typed material relationships including:

- DEPENDS_ON;
- REQUIRES;
- SUPPLIES;
- INTERFACES_WITH;
- ENABLES;
- BLOCKS;
- PROPAGATES_TO;
- CORRECTS;
- REVIEWS;
- SUPERSEDES;
- ALTERNATIVE_TO;
- RECOVERS;
- PRESERVES;
- EVIDENCES.

It also preserves provenance, state and history.

The test therefore finds that Historical does **not** presently justify creation of an independent Event Spine database.

Instead:

> **Historical Event Spine is a temporal reconstruction view over provenance-bearing cross-domain relationships, not necessarily a separate civil graph.**

KCS can provide much of the relational substrate.

Historical adds the historical semantics:

- time-bounded state;
- contemporary versus later reconstruction;
- historical authority state;
- archival custody;
- access/retention state;
- negative space;
- evaluation-space context.

### Result ES-KCS1 — PASS

Existing KCS architecture appears sufficient as the primary shared relationship substrate, subject to future implementation testing.

---

# 12. New KCS Relation Requirements?

The existing KCS vocabulary is strong but authority history may require relations not explicitly listed in the initial shared set.

Candidates include:

- AUTHORIZED_BY;
- DELEGATED_BY;
- JURISDICTION_OF;
- DECIDED_BY;
- APPEALED_TO;
- INVALIDATED_BY;
- REVOKED_BY;
- EXPIRED_BY;
- IMPLEMENTED_BY.

These should **not** automatically be added to KCS merely because Historical can imagine them.

They are candidate relation types to be tested against existing KCS extension rules.

The important requirement is that the semantics be representable somewhere without Historical inventing a competing authority graph.

---

# 13. Event Spine Example — Governance Decision Challenged in Judiciary

At T1:

Governance body G exercises authority A and issues decision D.

At T2:

Civil Attention receives challenge C.

At T3:

The challenge reaches Judiciary J.

At T4:

J determines part of D exceeded jurisdiction.

At T5:

Governance issues corrected decision D2.

At T6:

KCS marks D as superseded and affected dependent systems for review.

At T7:

Continuity updates recovery/configuration material that relied on D.

Historical should be able to reconstruct:

```text
G
→ AUTHORITY_STATE A
→ DECISION D
→ CHALLENGE C
→ JUDICIAL REVIEW J
→ FINDING F
→ CORRECTION D2
→ KCS PROPAGATION
→ CONTINUITY UPDATE
```

while preserving the fact that D was operationally real between T1 and its legitimate cessation even if later found partly unlawful.

That is crucial.

Otherwise Historical creates a false past in which invalidated actions never happened.

---

# 14. Illegal, Invalid or Unconstitutional Acts Are Still Historical Events

Historical must not erase an act merely because legitimate authority later determines it should not have occurred.

Therefore:

> **Invalid Authority Does Not Imply Non-Event.**

The archive may need to preserve:

- the act;
- the claimed authority;
- the actual authority later determined;
- affected participants;
- remedies;
- corrections;
- consequences.

This supports accountability without granting the invalid act continuing force.

---

# 15. Authority Provenance and Privacy

Authority provenance generally requires stronger identity/office traceability than ordinary historical material because accountability depends on knowing which office or actor exercised power.

But this does not justify universal personal exposure.

Historical should distinguish:

```text
Office Accountability
≠
Unlimited Personal Disclosure
```

For public authority, the default provenance requirement may be stronger.

For protected judicial participants, witnesses, jurors, minors, vulnerable persons, confidential advisers or security-sensitive roles, identity access may legitimately differ.

The invariant remains:

> **Provenance Completeness ≠ Universal Identity Visibility.**

---

# 16. Historical Analysis of Governance and Judiciary

Historical may identify longitudinal patterns such as:

- repeated jurisdictional disputes;
- reversal rates;
- emergency-authority duration;
- recurring procedural failures;
- delayed implementation;
- concentration of delegated authority;
- recurring evidence failures;
- policy-outcome sequences.

But:

> **Pattern ≠ Causation.**

And:

> **Historical Pattern Analysis ≠ Judicial Finding ≠ Governance Mandate.**

Historical analysis can surface questions and evidence.

It cannot convict, invalidate authority, create policy or manufacture constitutional meaning.

---

# 17. ESCP and Authority

Authority systems are particularly vulnerable to retrospective completeness errors.

A later civilisation may possess evidence, concepts or constitutional safeguards unavailable to earlier decision-makers.

Historical should therefore be able to distinguish:

1. what authority existed;
2. what authority was believed to exist;
3. what evidence about authority was accessible;
4. what constitutional interpretation existed;
5. what challenges were available;
6. what dimensions were missing from the evaluation space;
7. what later architecture changed the interpretation.

This yields:

> **Present Constitutional Understanding ≠ Historical Constitutional Evaluation Space.**

That distinction does not immunise past authority from criticism.

It makes criticism historically accurate.

---

# 18. Governance/Judiciary Boundary Stress Result

Historical survives the constitutional-authority test if five invariants are maintained:

1. **Authority Record ≠ Authority Grant.**
2. **Persistent Record ≠ Persistent Authority.**
3. **Historical Retrieval ≠ Operational Reactivation.**
4. **Procedural Finality ≠ Historical Infallibility.**
5. **Invalid Authority Does Not Imply Non-Event.**

These should be promoted into the formal Historical specification.

---

# 19. Event Spine Resolution

The Event Spine candidate is retained, but reclassified.

It should not presently be treated as a new standalone Historical subsystem.

Preferred architecture:

```text
Operational Domain Objects
        ↓
KCS / Shared Provenance-Bearing Relationships
        ↓
Historical Temporal Projection and Reconstruction
```

Historical therefore consumes and preserves relationships while adding time, historical state and reconstruction semantics.

If future implementation shows KCS cannot preserve the required temporal relationship history, a Historical companion may be justified.

Until then:

> **Do Not Duplicate a Shared Graph Merely to Obtain a Historical View of It.**

---

# 20. Required Formal-Specification Refinements

The next Historical specification revision should add or strengthen:

- Authority-State Record;
- claimed/exercised/recognised/later-adjudicated/current authority separation;
- authority-bearing record status;
- explicit anti-reactivation safeguards;
- Historical Handoff modes from Test 001;
- Operational Current State ↔ Historical State Sequence;
- Event Spine as temporal reconstruction over shared relationships;
- Domain-Level Completeness ≠ Cross-Domain Historical Completeness;
- public-authority provenance with protected identity boundaries;
- invalid/unlawful acts as preservable historical events;
- present constitutional understanding versus historical constitutional evaluation space.

---

# 21. Test Result

**Judiciary ↔ Historical:** PASS  
**Governance ↔ Historical:** PASS  
**Authority-State Preservation:** PASS WITH NEW EXPLICIT OBJECT REQUIREMENT  
**Event Spine ↔ KCS:** PASS WITHOUT JUSTIFYING A NEW DATABASE  
**Obsolete Authority Reactivation Risk:** MATERIAL / REQUIRES FORMAL SAFEGUARD  
**Major Authority Collision:** None if current authority remains resolved by current authoritative systems

The test strengthens rather than destabilises the Historical architecture.

The most important result is that the same record may remain permanently authentic while its authority changes radically across time.

Historical must therefore preserve **authority as state**, not treat authority as an intrinsic permanent property of a document.

---

## Status

**Cross-Domain Interface Test 002:** COMPLETE  
**Major New Invariant:** Persistent Record ≠ Persistent Authority  
**Major Safety Requirement:** Historical Retrieval ≠ Operational Reactivation  
**Event Spine Status:** RETAIN AS SEMANTIC/TEMPORAL VIEW; DO NOT YET CREATE SEPARATE GRAPH  
**Next:** Integrate Interface Tests 001–002 into the formal Historical specification, then test privacy/forgetting/destruction against participant rights and accountability requirements.


---

# 22. BCA Alignment Addendum

Subsequent review against Bounded Contextual Authority refines the authority model used above. Authority is better represented as a contextual activation and bounded exercise than as a durable property of a document, actor or office.

```text
Standing Eligibility
→ Context Satisfies Conditions
→ Authority Activates
→ Bounded Exercise
→ Exercise Terminates
→ Context Is Changed
→ Fresh Justification for Any Further Authority
```

The locked-case and glass-hammer metaphor captures this: the case opens only when context, legitimate function, need and required conditions are satisfied. The glass hammer represents the particular bounded authority available for use. Once used, that exercise is spent. Its consequences become part of the new context against which any later authority must be justified.

For a warrant or analogous instrument:

```text
C0 → A1 justified → A1 exercised → A1 spent → C1
C1 → fresh evaluation → A2 only if independently justified
```

A1 and its consequences may materially alter C1, but A1 does not reproduce itself.

Historical should therefore prefer an **Authority Activation and Exercise Record** over a primarily durable Authority-State model. Where material it should preserve pre-exercise context, standing eligibility, authority source, legitimate function, functional need, conditions, bounded authority envelope, activation, exercise, consequences and post-exercise context.

This yields four further distinctions:

- **Historical Evidence of Authority ≠ Preserved Authority.**
- **Past Legitimate Authority ≠ Reusable Authority.**
- **Previous Authority May Alter Future Context ≠ Previous Authority Grants Future Authority.**
- **Historical Retrieval Reconstructs an Authority Event; It Does Not Recreate Its Generating Context.**

The earlier reactivation concern is therefore refined. Historical does not need to neutralise dormant authority in an archive. It must prevent evidence that contextual conditions were satisfied at one historical point from being mistaken for evidence that they are satisfied now.

**BCA alignment result:** PASS WITH ONTOLOGICAL REFINEMENT.
