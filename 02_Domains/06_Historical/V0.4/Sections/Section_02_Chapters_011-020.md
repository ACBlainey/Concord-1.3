# 11. Historical Evaluation Context

Where consequential, Historical should support a linked **Historical Evaluation Context** describing:

- evidence available;
- evidence known to have been inaccessible;
- evidence actually examined;
- method or model used;
- model version;
- categories or variables represented;
- known missing dimensions;
- interface or sensor limitations;
- search or sampling boundary;
- uncertainty;
- contemporary scope claim;
- decision context;
- later-discovered dimensions.

This object exists to preserve the evaluation environment without requiring every source record to duplicate it.

---

# 12. Custody Lifecycle

The default conceptual lifecycle is:

```text
Operational Creation
        ↓
Operational Custody
        ↓
Historical Qualification / Handoff
        ↓
Historical Custody State
        ↓
Access / Derivation / Reconstruction
        ↓
Review / Reclassification
        ↓
Cold Storage / Continued Archive / Authorised Destruction
```

Historical does not automatically become the original custodian at creation.

Operational systems retain operational responsibility until a defined handoff, dual-custody state or other authorised transition occurs.

---

# 13. Custody States

Historical shall be capable of representing states equivalent to:

- OPERATIONAL
- DUAL_OPERATIONAL_HISTORICAL
- ARCHIVAL_ACTIVE
- ARCHIVAL_RESTRICTED
- COLD_STORAGE
- RETRIEVED_FOR_BOUNDED_PURPOSE
- SUPERSEDED_BUT_PRESERVED
- PENDING_RETENTION_REVIEW
- AUTHORISED_FOR_DESTRUCTION
- DESTROYED_WITH_PROVENANCE_MARKER

These are semantic states. Implementations may use different labels provided the distinctions survive.

---

# 14. Historical Qualification and Handoff

A record may qualify for Historical custody because of:

- legal or constitutional requirement;
- accountability significance;
- civilisational significance;
- system-state significance;
- developmental significance;
- evidential significance;
- cultural significance;
- capability lineage;
- unresolved dispute;
- future reconstruction need;
- retention policy;
- explicit source-domain handoff.

Qualification does not automatically imply indefinite retention.

The precise handoff threshold remains a design question requiring domain-specific companion rules.

A qualification finding identifies possible historical value; it does not create a right to seize operational records, override consent or compel unrestricted retention. The source domain and Historical must apply the expressly authorised custody mode and any applicable privacy, retention and jurisdiction limits. Until a valid handoff is completed, operational custody remains with the responsible source system; an unresolved or failed handoff must not be treated as a completed transfer.

---

# 15. Access Architecture

Historical access must be evaluated as a relation:

```text
Record
+
Actor
+
Action
+
Purpose
+
Context
+
Time
+
Permission State
```

Historical shall not collapse the following properties:

```text
Preserved
Discoverable
Searchable
Accessible
Retrievable
Disclosable
Publishable
Correlatable
```

A record may legitimately occupy different states across these dimensions.

A valid judicial disclosure order, Governance request or Continuity recovery request must still be evaluated against its actual bounded mandate, subject, purpose, protected scope and effective time. The existence of a court case, emergency or archived authority receipt does not itself create unrestricted search or correlation rights. Where evidence is required for review, Historical should provide an independently permitted projection or sealed review path, preserving provenance and a record of disclosure without revealing unrelated participant information. Architecture to be designed — request authentication, competing restrictions, sealed judicial access and appeal.

---

# 16. Purpose-Bounded Retrieval

Temporary or exceptional access must carry effective-time, expiry or review, authority, purpose and reversion semantics where applicable. Historical self-audit should detect permissions surviving their authorising condition.


Access permission should be capable of depending upon purpose.

Examples include:

- personal access;
- academic research;
- institutional audit;
- legal review;
- safety investigation;
- statistical analysis;
- public historical inquiry;
- restoration or recovery;
- authorised governance review.

Permission for one purpose does not imply unrestricted permission for another.

---

# 17. Privacy and Participant Rights

Historical custody must not automatically terminate legitimate participant rights.

Depending upon constitutional and domain-specific rules, these may include:

- access rights;
- correction rights;
- contextualisation rights;
- privacy rights;
- restriction rights;
- anonymisation rights;
- legitimate forgetting mechanisms.

Historical must distinguish correction from erasure.

Where an original record must remain for legitimate reasons, correction may be represented through linked state rather than silent mutation.

---

# 18. Forgetting

Historical should support intermediate information states rather than forcing a binary choice between unrestricted retention and destruction. Depending on authority and purpose, these may include de-identification, aggregation, protected linkage, restricted research environments, sealed custody and reduced discoverability.


Forgetting is not limited to physical byte deletion.

It may include authorised transitions such as:

- removal from ordinary discovery;
- removal from participant correlation;
- anonymisation;
- pseudonymisation;
- aggregation;
- sealed custody;
- cold storage;
- cryptographic inaccessibility;
- destruction.

Different mechanisms have different reversibility and epistemic consequences.

The least irreversible mechanism adequate to the legitimate purpose should be preferred where other constraints permit.

Historical's standing functional mandate includes implementing a valid, authorised information-state transition within its custody. It does not include independently deciding that a participant has forfeited privacy or that a lawful destruction requirement may be disregarded for historical interest. Requests must be assessed against the relevant retention, rights and custody rules; where the mandate or entitlement is disputed, Historical preserves the existing protected state pending the competent decision rather than granting itself adjudicative authority.

---

# 19. Destruction

A destruction claim must state its scope. Source destruction does not establish that summaries, aggregates, trained models, derived representations or other derivatives have also been destroyed.


Authorised destruction must record, where lawful and safe:

- what class of material was destroyed;
- authority for destruction;
- retention rule applied;
- date/time;
- method or process;
- whether derivatives remain;
- whether relationship information was affected;
- whether a provenance marker may legitimately survive.

A destruction marker must not preserve the sensitive substance whose destruction was required.

Historical has functional authority to carry out destruction within its own lawful custody when the applicable mandate and retention conditions require or permit it. This does not confer authority to destroy another domain's operational source, order the deletion of judicial evidence, or override a preservation obligation. The authorising decision, execution, surviving derivatives and any failed or partial destruction must remain distinguishable. Where disclosure of the destruction record would defeat the protection, only a lawful minimal provenance marker may survive.

---

# 20. Reconstruction Services

Historical shall support at least two logically distinct reconstruction modes.

## HR-1 — Contemporary Reconstruction

Question:

> What could a participant or system at time T reasonably have known or represented through the information and evaluation architecture available at time T?

Later knowledge must be excluded or explicitly separated.

## HR-2 — Present-Best Reconstruction

Question:

> Given preserved records and subsequent discoveries, what is the present best reconstruction of the historical state at time T?

Later evidence may be used but must be identified as retrospective.

Therefore:

```text
Contemporary Reconstruction(T)
≠
Present-Best Reconstruction(T)
```

Neither should overwrite the other.

Both modes fall within Historical's standing functional mandate when applied to records it may lawfully process. They produce evidence-based reconstructions, not operational restorations, judicial verdicts or renewed authority. Where the reconstruction concerns a disputed decision, the output must identify the decision-time evidence separately from later evidence and any competent adjudication; it cannot silently rewrite the original state.

---

