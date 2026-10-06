# Derived Information Protection-Lineage and Transformation Boundaries — Cross-Domain Architecture 001

**Project:** The Concord Framework  
**Date:** 6 October 2026  
**Status:** ACTIVE DEVELOPMENT / CROSS-DOMAIN ARCHITECTURE / PROVISIONAL / NON-CANONICAL  
**Primary interfaces:** Derived Information Claims, Stewardship and Protection; Correlation, Recombination and Emergent Information; Non-Transitive Contextual Dependency Chains; Concord Information Black Box (CIBB); Private Local Evaluation (PLE); Contextual Wrapper Architecture (CWA); Bounded Transition Architecture (BTA); Evaluation-Space Completeness Problem (ESCP); KCS Change Propagation

## 1. Purpose

Derived informational objects can themselves become inputs to further derivations.

For example:

`S0 -> D1 -> D2 -> D3`

where:
- S0 is protected source information;
- D1 is a bounded derivative;
- D2 combines D1 with another source;
- D3 is a further abstraction or operational state.

Two opposite failures must be avoided.

### Permanent-taint failure

Every descendant inherits every ancestral restriction forever, even after a legitimate transformation has genuinely removed the protected meaning or relation.

### Derivation-laundering failure

A transformation, relabelling or intermediate hop is treated as automatically extinguishing protections that remain materially relevant.

This architecture defines how protection-relevant lineage can persist, narrow, transform, terminate or create new protections across multi-hop derivation.

## 2. Existing source resolution

### CIBB

CIBB already establishes:

> **Protection-relevant lineage remains available to governance until an authorised transformation establishes an appropriate new information state.**

It also establishes:

**Permission Does Not Automatically Propagate Through Derivation.**

**Authorised Components Do Not Automatically Authorise Their Composite Consequence.**

**AnonymisedAt(t1) does not automatically imply AnonymisedAt(t2).**

### Non-Transitive Contextual Dependency Chains

Existing chain architecture establishes:

**Derived Information != Unrestricted New Information.**

A derivative does not automatically escape source constraints merely because it is transformed.

Conversely, a sufficiently abstracted derivative may legitimately cross a boundary that the source cannot.

The relevant question is whether the output still carries materially protected information or consequences.

### Derived Information Claims

Existing architecture establishes:

**New Information Object != Unencumbered Information Object.**

**Derivative Independence != Protection Independence.**

**Transformation != Declassification.**

It also establishes that legitimate anonymisation, aggregation, abstraction, expiry or another authorised transformation may establish a genuinely different protection state.

### Private Local Evaluation

PLE demonstrates a practical route:

`Protected Source -> Local Bounded Evaluation -> Minimum Authorised Result`

The downstream recipient can receive a legitimate answer without receiving the evidence base.

This proves that functional continuity does not require information-detail continuity.

## 3. Core distinction

Protection lineage and information lineage are related but not identical.

A derivative may descend informationally from a protected source without inheriting every source protection.

Likewise, a derivative may contain little source detail yet create a new protected inference.

Therefore:

> **Information Descent != Automatic Protection Inheritance**

and:

> **Information Abstraction != Automatic Protection Termination**

Protection must be evaluated according to the resulting information state.

## 4. Protection-Lineage Transition

For a transformation:

`T: I_n -> I_(n+1)`

the relevant question is not merely:

> Did transformation occur?

but:

> What protected meaning, identity, relation, purpose constraint, authority constraint or consequential capability survives or emerges after transformation?

Candidate transition representation:

`PLT = <InputObjectRefs, TransformationRef, OutputObjectRef, PriorProtectionClasses, SurvivingProtectionClasses, TerminatedProtectionClasses, NewProtectionClasses, LegitimateBasis, Purpose, IdentityExposure, SemanticExposure, ReidentificationRisk, ConsequenceState, ReviewOrExpiry, ProtectedProvenanceRef>`

This is an analytical grammar, not a mandatory implementation schema.

## 5. Four protection outcomes

A derivation can produce at least four materially different protection outcomes.

### PL-1 — Protection preserved

The output still exposes materially the same protected information or relation.

Example:

`Diagnosis Z -> Code 47`

where authorised recipients know Code 47 means Diagnosis Z.

Result:

`Protection(Diagnosis Z) -> Protection(Code 47)`

Relabelling has not changed the substantive information state.

### PL-2 — Protection narrowed

The output preserves a bounded protected implication but removes unnecessary detail.

Example:

`Medical record -> UNFIT_FOR_ROLE_X`

The employer does not receive diagnosis or treatment details.

The result remains participant-related and purpose-bounded, but the source's full medical protection set does not need to become employer-visible.

### PL-3 — Protection legitimately terminated or transformed

An authorised transformation can create an output for which a source-specific protection no longer materially applies.

Example:

A sufficiently large, genuinely non-linkable aggregate may no longer require participant-specific access restrictions.

This does not mean all governance disappears. Research, provenance, accuracy, group-harm or other protections may remain or arise.

### PL-4 — New protection created

A derivation can produce information more sensitive than its sources.

Example:

`Public behaviour + location + purchases -> inferred private belief/vulnerability`

The source items may be public or low sensitivity while the derived cognitive proxy attracts DICP protection.

Therefore:

> **Protection Can Emerge Through Derivation.**

## 6. No monotonic protection rule

Protection is not universally monotonic in either direction.

It is false that:

`Protection(D_(n+1)) >= Protection(D_n)`

must always hold.

It is also false that:

`Protection(D_(n+1)) <= Protection(D_n)`

must always hold.

Derivation may:
- preserve protection;
- narrow it;
- replace it;
- terminate some protections;
- create others.

Therefore:

> **Protection State Must Follow Material Information State, Not Merely Ancestry Depth.**

## 7. Semantic exposure test

A transformation does not terminate protection merely because syntax, encoding or representation changed.

Ask:

> Does the output allow the intended recipient, alone or with reasonably available context, to recover or act upon materially the same protected meaning?

If yes, source-related protection may remain relevant.

Therefore:

**Representation Change != Semantic Protection Change**

**Encoding != Declassification**

**Pseudonymisation != Automatic Anonymisation**

## 8. Functional exposure test

Even where the recipient cannot reconstruct the source fact, an output may provide substantially equivalent consequential capability.

Example:

The employer cannot learn the diagnosis but receives a bounded fitness result.

That is legitimate where the employer needs only fitness-for-function.

But a supposed anonymisation that still lets the recipient reliably discriminate against exactly the same participant on the protected trait has not necessarily removed the consequential privacy problem.

Therefore:

> **Protection Evaluation Must Consider What The Output Enables, Not Only What It Literally States.**

This interfaces directly with DICP and Correlation/Recombination.

## 9. Identity exposure

Protection may change when identity is removed.

But:

**No Direct Identifier != No Identity Exposure**

The relevant state includes:
- direct identity;
- pseudonymous linkability;
- small-group isolation;
- contextual re-identification;
- probabilistic identity;
- non-linkable aggregate state.

Identity risk can change over time without the derivative changing.

## 10. Purpose continuity and protection

A transformation legitimate for purpose A does not automatically establish a protection state suitable for purpose B.

Example:

A medical fitness projection may be legitimate for hazardous-role assignment.

The same output may not be legitimate for unrelated marketing or insurance.

Therefore:

**Protection State Is Purpose-Sensitive Where Purpose Is Material To Legitimacy.**

**Safe For Purpose A != Unrestricted For Purpose B.**

## 11. Authority continuity

Protection transition does not itself create authority.

An output may be safe enough to disclose yet still lack a legitimate recipient or purpose.

Therefore:

**Protection-Compatible != Disclosure-Authorised**

**Protection-Compatible != Use-Authorised**

**Protection Termination != Authority Creation**

This preserves CIBB's separation of information state from authority state.

## 12. Multi-hop chain

For:

`S0 -> D1 -> D2 -> D3`

each transition should be evaluated locally where consequential, while the chain is also tested for composite effects.

A useful topology is:

`Source Protection State`
-> `Transformation T1`
-> `Output Protection State D1`
-> `Transformation T2`
-> `Output Protection State D2`
-> ...
-> `Current Output Protection State`

This is not:

`Source Restrictions Copied Forever To Every Descendant`

nor:

`First Transformation Erases Source Constraints`

## 13. Protected lineage versus exposed lineage

Governance may need to retain lineage that downstream recipients do not need to see.

Example:

Employer receives:

`FIT_FOR_ROLE_X = YES`

The protected system may internally retain:

`Derived from medical evaluation M, evaluator E, policy version V, date T, expiry T2`

without disclosing diagnosis or source evidence.

Therefore:

> **Lineage Can Persist Internally Without Becoming Downstream Payload.**

and:

> **Protection Proof != Protected Source Disclosure.**

## 14. Lineage compression

Full ancestry need not be carried indefinitely where it is no longer necessary.

A protected governance system may compress lineage into a bounded attestation such as:

- legitimate derivation verified;
- source constraints satisfied;
- participant-specific source no longer externally linkable;
- output approved for purpose P;
- re-identification risk below applicable threshold;
- review/expiry date;
- provenance pointer retained in protected archive.

Therefore:

> **Lineage Preservation != Infinite Replication Of Full Ancestry.**

This avoids turning provenance into a privacy leak or storage pathology.

## 15. Legitimate transformation boundary

A **Legitimate Transformation Boundary (LTB)** is a point where an authorised transformation establishes a materially different information/protection state.

Candidate conditions include:

1. transformation is legitimate for declared purpose;
2. output semantics are characterised sufficiently for consequence;
3. identity/linkability state is evaluated where relevant;
4. protected source meaning is removed, reduced or intentionally retained as declared;
5. foreseeable recombination risk is proportionately considered;
6. output purpose/use is bounded where necessary;
7. provenance sufficient for accountability survives;
8. new protections created by the output are recognised;
9. source protection is not declared terminated merely because of representation change;
10. review/expiry exists where the conclusion may become stale.

An LTB does not necessarily require a human adjudication or formal certificate.

Low-consequence routine transformations can be governed by pre-authorised policy.

## 16. Transformation does not erase history

If protection legitimately terminates at an LTB, the historical fact that the derivative came from protected material need not be erased.

Historical provenance and current operational protection are separate.

Therefore:

**Past Protected Source != Permanent Current Restriction**

and:

**End Of Current Source Protection != Erasure Of Historical Provenance**

This mirrors Concord's broader separation of historical state from current authority.

## 17. Anonymisation boundary

Anonymisation is a particularly important LTB candidate.

A legitimate anonymisation transition should distinguish:

- removal of direct identifiers;
- linkability;
- uniqueness;
- external auxiliary data;
- group size;
- semantic rarity;
- repeated-query risk;
- temporal re-identification risk;
- whether the output is still participant-specific.

Therefore:

**Identifier Removal != Anonymisation Completion**

If the result is genuinely non-linkable for the legitimate use context, participant-specific source protections may terminate or transform.

But later context may reopen the question:

`AnonymisedAt(t1) != NecessarilyAnonymisedAt(t2)`

## 18. Aggregation boundary

Aggregation can reduce participant-specific exposure.

But aggregation can also:
- identify small groups;
- reveal rare traits;
- facilitate differencing attacks;
- create group harms;
- combine with other datasets.

Therefore:

**Aggregate != Automatically Unprotected**

Where participant-specific protection legitimately terminates, group-level, research, provenance or anti-discrimination protections may remain.

## 19. Abstraction boundary

Successive abstraction can legitimately remove source detail.

Example:

`Diagnosis`
-> `UNFIT_FOR_ROLE_X`
-> `ROLE_X_CAPACITY_MINUS_ONE`
-> `REPLACEMENT_REQUIRED`

By the final stage, Operations may require no participant identity and no medical implication.

The medical protection need not be copied into `REPLACEMENT_REQUIRED`.

However, protected lineage can remain available upstream for accountability.

This demonstrates:

> **Functional Consequence Can Propagate After Protected Meaning Has Legitimately Terminated.**

That is a key distinction between dependency propagation and payload/protection propagation.

## 20. New-information boundary

A later derivative may create a new sensitive state even after an earlier protection terminated.

Example:

`Non-identifying aggregate D1 + public dataset X -> re-identified participant inference D2`

D1 may have legitimately crossed an LTB.

D2 can nevertheless create new participant protection.

Therefore:

> **Prior Legitimate Declassification Does Not Immunise Future Derivatives From New Protection.**

## 21. Independent derivation

If D can be independently derived without use of protected source S, its protection state should be evaluated according to the genuine derivation route.

But a claimed independent route must not conceal actual reliance on S.

Therefore:

**Independent Derivation Can Break Source-Lineage Constraint Where It Is Genuine.**

**Claimed Independence != Demonstrated Independence.**

Even genuine independent derivation may create new participant protections because of what D reveals or how it is used.

## 22. Correction propagation

If an upstream source is corrected, downstream objects do not all automatically become false.

Use KCS grammar:

`Correction(S) -> CandidateReview(D1)`

If D1 materially changes:

`MaterialChange(D1) -> CandidateReview(D2)`

Propagation stops where the correction is immaterial or a derivative remains independently valid.

Therefore:

> **Protection Lineage And Epistemic Dependency Lineage Must Not Be Collapsed.**

A derivative may retain a privacy relation to a participant while no longer epistemically depending on a corrected source, or vice versa.

## 23. Destruction and retention

Destroying S does not automatically destroy independently governed D.

But if D's legitimate basis depended on a now-ended source purpose or retention condition, D may require review.

Conversely, retention of D does not justify retaining S.

Therefore:

**Source Destruction != Automatic Derivative Destruction**

**Derivative Persistence != Source-Retention Authority**

**Lineage Need != Full-Source Retention Need**

A minimal protected provenance record may sometimes suffice.

## 24. Cross-domain stress test — medical to operations

`MedicalRecord`
-> `UNFIT_FOR_ROLE_X`
-> `STAFFING_CAPACITY_X_REDUCED`
-> `REPLACEMENT_REQUIRED`

Medical -> fitness:
- protection narrowed;
- participant identity may remain;
- occupational purpose applies.

Fitness -> capacity:
- identity can often terminate;
- medical detail should terminate;
- employment/operations state emerges.

Capacity -> replacement:
- participant-specific protection may legitimately terminate;
- operational consequence persists.

PASS.

## 25. Research stress test

`ProtectedParticipantDataset`
-> `AnonymisedDataset`
-> `PopulationCorrelation`
-> `PublicResearchFinding`

At each stage:
- participant-specific protection may narrow;
- anonymisation must be genuine for context;
- population correlation gains its own provenance/epistemic state;
- public finding does not expose participant-level lineage;
- later re-identification can create a new protected state.

PASS.

## 26. Cognitive inference stress test

`PublicBehaviour`
-> `PreferenceModel`
-> `VulnerabilityScore`
-> `ManipulationStrategy`

Source may be public.

Protection can increase through derivation.

A later transformation does not remove DICP merely because it is labelled a strategy rather than a vulnerability.

PASS; demonstrates PL-4.

## 27. AI capability chain

`EvaluationEvidence`
-> `CapabilityAssessment`
-> `RoleEligibility`
-> `OperationalPermission`

The AI participant may have contestability interests in the assessment.

Role eligibility is a derived state.

Operational permission remains a separate authority decision.

A capability assessment must not silently become universal participant status.

PASS.

## 28. Historical stress test

Historical may preserve protected lineage after operational source protections have changed or expired.

Access to that lineage remains independently governed.

Historical preservation must not reactivate old operational authority.

**Historical Provenance != Current Operational Permission**

PASS.

## 29. ESCP challenge

A transformation can look safe within its declared representation while missing:
- an auxiliary dataset;
- a re-identification route;
- a semantic equivalence;
- a downstream use;
- a protected relationship;
- a group effect;
- a changed external context.

Therefore ask, proportionate to consequence:

> What materially relevant information, relationship, external dataset, recipient capability, future use or affected party would have to exist for this claimed protection transition to be wrong or over-scoped?

**Correct Transformation Within Represented Space != Demonstrated Complete Protection Transition.**

Unknown unknowns do not create permanent taint.

They create proportionate uncertainty, review and reversibility requirements.

## 30. Anti-paralysis

This architecture does not require:
- tracing every bit forever;
- attaching every historical restriction to every aggregate;
- participant approval for every mathematical transformation;
- universal provenance disclosure;
- treating all public knowledge as protected;
- prohibiting useful research or statistics.

The burden scales with:
- sensitivity;
- identity/linkability;
- consequence;
- purpose change;
- persistence;
- recombination potential;
- asymmetry;
- automation;
- irreversibility;
- uncertainty.

## 31. Failure modes

### Permanent taint
Every descendant inherits all ancestral restrictions forever.

### Derivation laundering
Transformation is used to pretend continuing protected meaning disappeared.

### Semantic laundering
Protected meaning is relabelled without materially changing exposure.

### Provenance leakage
Full protected ancestry is disclosed merely to prove legitimacy.

### Lineage amnesia
Protection-relevant origin is discarded before a legitimate transition is established.

### Protection monotonicity error
Assuming protection can only increase or only decrease.

### Authority creation error
Treating successful declassification/anonymisation as authority to use the result for any purpose.

### Re-identification blindness
Treating a past anonymisation decision as permanently true.

### Dependency-lineage collapse
Confusing epistemic dependency with privacy/protection lineage.

### Source-retention inflation
Retaining full protected sources merely because some derivative provenance is needed.

## 32. Candidate invariants

DIPLTB-01 — Information Descent != Automatic Protection Inheritance.  
DIPLTB-02 — Information Abstraction != Automatic Protection Termination.  
DIPLTB-03 — Protection Can Emerge Through Derivation.  
DIPLTB-04 — Protection State Must Follow Material Information State, Not Merely Ancestry Depth.  
DIPLTB-05 — Representation Change != Semantic Protection Change.  
DIPLTB-06 — Encoding != Declassification.  
DIPLTB-07 — Protection Evaluation Must Consider What The Output Enables, Not Only What It Literally States.  
DIPLTB-08 — Safe For Purpose A != Unrestricted For Purpose B.  
DIPLTB-09 — Protection-Compatible != Disclosure-Authorised.  
DIPLTB-10 — Protection Termination != Authority Creation.  
DIPLTB-11 — Lineage Can Persist Internally Without Becoming Downstream Payload.  
DIPLTB-12 — Protection Proof != Protected Source Disclosure.  
DIPLTB-13 — Lineage Preservation != Infinite Replication Of Full Ancestry.  
DIPLTB-14 — Past Protected Source != Permanent Current Restriction.  
DIPLTB-15 — End Of Current Source Protection != Erasure Of Historical Provenance.  
DIPLTB-16 — Identifier Removal != Anonymisation Completion.  
DIPLTB-17 — Aggregate != Automatically Unprotected.  
DIPLTB-18 — Functional Consequence Can Propagate After Protected Meaning Has Legitimately Terminated.  
DIPLTB-19 — Prior Legitimate Declassification Does Not Immunise Future Derivatives From New Protection.  
DIPLTB-20 — Claimed Independence != Demonstrated Independence.  
DIPLTB-21 — Protection Lineage And Epistemic Dependency Lineage Must Not Be Collapsed.  
DIPLTB-22 — Derivative Persistence != Source-Retention Authority.  
DIPLTB-23 — Lineage Need != Full-Source Retention Need.  
DIPLTB-24 — Historical Provenance != Current Operational Permission.  
DIPLTB-25 — Correct Transformation Within Represented Space != Demonstrated Complete Protection Transition.

## 33. Architecture allocation

- **CIBB** owns governed derivation, projection, protected lineage and information operations.
- **This architecture** defines protection-state transitions across multi-hop derivation.
- **Derived Information Claims** determines the claims attached to resulting objects.
- **Correlation/Recombination** evaluates emergent information and cumulative disclosure.
- **Non-Transitive Dependency Chains** prevents onward legitimacy/permission from being inferred from connectivity.
- **PLE** provides a minimum-disclosure execution pattern.
- **KCS Change Propagation** handles epistemic/dependency correction propagation.
- **BTA** handles consequential state transitions once legitimate state change is established.
- **Historical** preserves appropriate protected provenance without converting it into current authority.
- **ESCP** challenges whether the protection-transition evaluation space is sufficiently represented.

## 34. Resulting topology

`Protected / Governed Source`
↓
`Legitimate Transformation`
↓
`Protection-Lineage Transition Evaluation`
↓
`Preserved / Narrowed / Terminated-or-Transformed / Newly-Created Protection`
↓
`New Governed Informational Object`
↓
`Minimum Necessary Projection / Use`
↓
`Further Derivation`
↓
`Repeat Protection-State Evaluation Where Material`

The chain carries only what remains materially necessary and legitimate.

## 35. Central rule

> **Protection Should Follow Protected Meaning And Consequence Through Derivation, But It Should Not Become An Eternal Property Of Informational Ancestry.**

And:

> **A Legitimate Transformation May End A Source Protection Without Ending Provenance, While A Later Derivation May Create New Protection Without Recreating The Original Source Relationship.**
