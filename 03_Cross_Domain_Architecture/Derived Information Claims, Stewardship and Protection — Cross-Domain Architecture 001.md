# Derived Information Claims, Stewardship and Protection — Cross-Domain Architecture 001

**Project:** The Concord Framework  
**Domain:** Cross-Domain Architecture  
**Date:** 6 October 2026  
**Status:** ACTIVE DEVELOPMENT / SOURCE-RESOLVED CROSS-DOMAIN ARCHITECTURE / NON-CANONICAL

## 1. Purpose

This architecture addresses a question exposed by Correlation, Recombination and Emergent Information:

> When new information is inferred, combined, modelled, transformed or derived from information concerning one or more participants, who owns it and which protections survive?

The Concord source space does not support a universal answer of either:

- “the subject owns every derived fact”; or
- “the creator of the inference owns it free of prior constraint.”

The stronger architecture separates the informational object from the claims, protections, authorities and duties attached to its creation and use.

## 2. Source resolution

This architecture is not developed from zero.

### V1.2 participant-data architecture

V1.2 proposed participant primary ownership/control of identifiable personal information and participant access to major derived metrics, classifications and predictive conclusions.

It also established that collection, storage, analysis and predictive usefulness do not automatically transfer ownership.

### V1.2 Historical pattern architecture

Historical Source Resolution 014A established that derived patterns are distinguishable informational objects with their own provenance and time semantics, and that cross-domain joins can create both new analytical value and new privacy risk.

### V1.2a EKC-01

The V1.2a counterfactual deliberately did not require all participant information to be property.

It instead treated consequential information as creating an ethical relationship among subject, holder, user, affected parties and shared function.

It derived purpose limitation for acquisition, retention, combination, inference, sharing and use.

### Derived and Inferred Cognitive Privacy

DICP establishes:

**Low-Sensitivity Inputs != Low-Sensitivity Derived Output**

**Public Inputs != Unlimited Consequential Profiling Authority**

**Authority To Construct != Authority To Use For Every Purpose**

**Inference Accuracy != Consequential Legitimacy**

and recognises that newly constructed participant information can create privacy, autonomy, dignity and contestability interests even when the source information was lawfully available.

### Concord Information Black Box

CIBB establishes that protected information may undergo Controlled Derivation and:

> the derivative may become a new independently governed object.

It simultaneously requires protection-relevant lineage to remain available until an authorised transformation establishes an appropriate new information state.

CIBB also establishes:

**Permission Does Not Automatically Propagate Through Derivation**

and:

**Authorised Components Do Not Automatically Authorise Their Composite Consequence.**

These sources together resolve the basic topology.

## 3. The ownership question is compound

The question:

> Who owns derived information?

usually compresses several different questions:

1. Who created the derived informational object?
2. Who or what is the information about?
3. Who supplied the source information?
4. Who lawfully controls the source objects?
5. Who may possess the derivative?
6. Who may inspect it?
7. Who may use it, and for what purpose?
8. Who may disclose or reproject it?
9. Who may contest its accuracy or interpretation?
10. Who may correct or supersede it?
11. Who must preserve provenance?
12. Who bears responsibility for harmful or erroneous use?
13. Who may destroy, retain or archive it?
14. Which third parties are materially affected?
15. Which protections survive transformation?

These questions need not have the same answer.

Therefore:

> **Informational Ownership != Single Undivided Control Right**

## 4. Derived informational object

Candidate definition:

> A **Derived Informational Object (DIO)** is an informational object whose material content is produced through inference, transformation, combination, correlation, modelling, abstraction, aggregation, classification, prediction or another operation upon one or more source states.

Examples include:

- fitness-for-role attestation;
- credit or eligibility classification;
- medical risk score;
- research correlation;
- behavioural prediction;
- inferred preference;
- anonymised aggregate;
- fraud-risk indicator;
- AI capability evaluation;
- historical pattern;
- derived identity-confidence state.

A DIO is not necessarily personal information, sensitive information or protected information.

Its governance depends upon what it represents, how it was produced, what it reveals, its consequence and its legitimate purpose.

## 5. Object creation does not settle claims

A derivation can create a genuinely new informational object.

That does not establish that all claims attached to source information disappear.

Therefore:

**New Information Object != Unencumbered Information Object**

**Derivative Independence != Protection Independence**

**Transformation != Declassification**

**Creation Of Information != Creation Of Unlimited Authority Over Information**

The derivative may have its own object identity while remaining subject to protection-relevant lineage.

## 6. Claim decomposition

A DIO may generate or preserve several non-identical claim classes.

### 6.1 Authorship / contribution claim

Who performed the intellectual, computational, observational or methodological work that produced the derivative?

This supports provenance and contribution recognition.

**Authorship != Subjecthood**

### 6.2 Subject claim

A participant about whom consequential information is derived may possess legitimate interests in:

- privacy;
- access where appropriate;
- awareness of consequential use;
- context;
- contestability;
- correction;
- protection from unjustified propagation;
- protection from domination or manipulation.

The participant need not have authored the inference for these claims to exist.

**Not Author Of Inference != No Claim Over Consequential Use**

### 6.3 Source-holder / source-steward claim

A source owner or steward may retain restrictions arising from:

- purpose;
- confidentiality;
- consent;
- protected context;
- contractual or fiduciary duty;
- security;
- third-party rights;
- lifecycle state.

### 6.4 Derivative-holder claim

An actor legitimately creating or receiving the DIO may possess bounded authority to hold or use it.

**Legitimate Possession != Universal Reuse**

### 6.5 Affected-third-party claim

A derivative about participant A may reveal or materially affect B, C or a group.

Therefore:

**Primary Subject != Only Affected Subject**

### 6.6 Civil / shared-function claim

Some derivatives may legitimately serve accountability, research, safety, planning, adjudication or historical continuity.

This may create a stewardship interest without creating unrestricted civil ownership.

## 7. Claim bundle model

A DIO should therefore be modelled through a bundle rather than a single owner field where consequence warrants it.

Candidate representation:

`DIC = <DIORef, SubjectRefs, SourceRefs, AuthorOrDeriverRefs, StewardRefs, LegitimatePurpose, AccessClaims, ContestabilityClaims, CorrectionClaims, DisclosureConstraints, ReprojectionConstraints, RetentionState, LifecycleAuthority, ThirdPartyInterests, ProtectionLineage, Provenance, EpistemicState, Uncertainty>`

This is candidate architecture, not a mandatory universal database schema.

## 8. Subject rights do not require universal subject ownership

A participant can possess strong rights concerning a DIO without being declared the legal owner of every inference concerning them.

For example, an occupational-health evaluator may independently author:

`FIT_FOR_ROLE_X`

The worker did not author that conclusion.

The employer may legitimately receive the bounded result.

Yet the worker can still possess strong claims concerning accuracy, purpose, temporal validity, misuse and consequential contestability.

Therefore:

> **Participant Protection Can Attach To Consequential Relation Without Requiring Universal Participant Ownership Of The Derived Object.**

This preserves the V1.2 protection while avoiding an overbroad property rule.

## 9. Creator rights do not erase subject protection

The inverse error is equally serious.

A researcher, institution, employer, AI or model may perform genuine work to derive a new informational object.

That can create authorship, provenance or legitimate stewardship claims.

It does not follow:

`I derived it -> I may use it however I wish`

Therefore:

**Derivation Labour != Unlimited Use Authority**

**Model Ownership != Unlimited Authority Over Modelled Participant**

**Method Ownership != Ownership Of Every Consequential Fact Produced By The Method**

This is particularly important for proprietary models.

DICP already establishes:

**Model Proprietary Interest != Automatic Defeat Of Consequential Contestability**

## 10. Facts, expressions, methods and governed objects must remain distinct

The architecture should not collapse:

- a fact or claimed fact;
- a participant's source record;
- a method/model;
- an expression/document;
- a derived governed object;
- a decision made using that object.

These can have different legitimate claims and different owners/stewards.

For example:

A laboratory may own equipment and a proprietary analysis method.

A participant may retain strong rights concerning their specimen and identifiable health information.

The resulting diagnosis may be a new clinical informational object.

The clinician may author the interpretation.

The participant may possess access and contestability rights.

The health service may have bounded retention duties.

Research use may require separate legitimacy.

No single ownership statement adequately represents this topology.

## 11. Protection-relevant lineage

CIBB's protection-relevant lineage is central.

A DIO should preserve enough protected lineage to answer, where legitimate:

- what source classes materially contributed;
- what transformation occurred;
- what purpose justified derivation;
- what protection constraints remain;
- what uncertainty exists;
- what correction/supersession events occurred;
- whether a protected-context restriction applies.

However:

**Provenance Preservation != Universal Provenance Disclosure**

A recipient may legitimately receive the DIO without receiving all protected source information.

Example:

`MedicalRecord -> OccupationalHealth -> FIT_FOR_ROLE_X -> Employer`

The employer may receive the fitness state without receiving the medical record.

## 12. Derived sensitivity

Sensitivity is a property of the resulting informational relation, not merely of the inputs.

Therefore:

**Low-Sensitivity Inputs != Low-Sensitivity Derived Output**

**Public Inputs != Public Derived Profile**

**Individually Non-Identifying Inputs != Non-Identifying Composite**

A DIO must be evaluated according to what it reveals and enables.

## 13. Semantic equivalence and laundering

Transformation must not become a mechanism for laundering protected meaning.

Example:

Protected source:
`Participant has condition Z`

Derived label:
`Category 47`

If every authorised recipient knows Category 47 means condition Z, changing the label has not meaningfully removed the protected information.

Therefore:

> **Transformation That Preserves Protected Semantic Exposure Does Not By Itself Remove Protection.**

Candidate rule:

**Representation Change != Protection-State Change**

This does not mean protection can never terminate.

Legitimate anonymisation, aggregation, abstraction, declassification, expiry or another authorised transformation may establish a new protection state.

The change must be justified rather than presumed.

## 14. Inference can create a new protected relation

A participant may never have possessed, disclosed or even known a derived fact.

A third party can nevertheless infer something consequential about them.

The participant's lack of prior possession does not eliminate privacy or contestability interests.

Therefore:

**Never Disclosed By Participant != Unprotected Participant Information**

**Participant Did Not Know The Inference != No Participant Claim**

This is especially important for cognitive, genomic, behavioural and predictive inference.

## 15. Epistemic status and claim strength

A DIO may be:

- observed derivative;
- inferred;
- predicted;
- probabilistic;
- hypothesised;
- disputed;
- corrected;
- superseded;
- rejected;
- unknown.

The system must not convert stronger governance into stronger truth.

**Protected != True**

**Owned != True**

**Contestable != False**

**High Confidence != Authority**

The epistemic and governance planes remain distinct.

## 16. Correction and downstream effects

If a DIO materially affects a participant, correction of its source or interpretation may require downstream review.

V1.2a already derived downstream correction signalling.

KCS Change Propagation and Selective Context-State Transition Propagation provide the general mechanism.

The default is:

`Material Correction -> Candidate Review Of Dependent DIOs/Decisions`

not:

`Material Correction -> Automatic Deletion Or Reversal Of Everything Downstream`

## 17. Purpose and reuse

A DIO legitimately created for purpose A does not automatically become legitimate for B.

**Authority To Derive For A != Authority To Use For B**

**Authority To Hold != Authority To Redisclose**

**Authority To Analyse != Authority To Act**

**Authority To Act For Q1 != Authority To Act For Q2**

Purpose change may require renewed legitimacy evaluation.

## 18. Derived information and contextual wrappers

DIOs can cross wrapper boundaries only through legitimate interfaces.

A projection received in one context does not carry general authority into another.

This yields:

**Protected Source -> Bounded Derivation -> Contextual Projection -> Legitimate Recipient**

not:

**Protected Source -> Derivation -> Free Information**

A DIO can therefore be independently governed while remaining contextually bounded.

## 19. Multi-source derivation

Where DIO D derives from sources A, B and C:

`D = F(A,B,C)`

no source actor automatically gains total control of D merely by contributing one input.

Likewise, the deriver does not automatically extinguish all source-related protections.

Potential claims may be overlapping and non-identical.

**Multiple Source Claims != Collective Veto By Default**

**Multiple Source Claims != No Source Protection**

Resolution depends on legitimate function, consequence, source conditions, participant rights, third-party effects and applicable authority.

## 20. Aggregate and group information

Aggregate information can be independently useful and legitimately governed without assigning every contributor individual control over every aggregate output.

However:

- practical re-identification matters;
- small groups can expose individuals;
- group conclusions can create harms;
- group probability is not individual proof;
- combination with external information can change sensitivity.

Therefore:

**Aggregation != Automatic Freedom From Participant Protection**

but also:

**Contribution To Aggregate != Individual Ownership Of Aggregate**

## 21. Independently derivable information

The same fact may be legitimately derivable from multiple independent sources.

A participant's protection claim should not automatically become a monopoly over reality.

Conversely, independent derivability should not be used as a fiction to evade protected-source constraints.

Therefore:

**Fact Can Be Independently Knowable Without Every Route To It Being Legitimate**

and:

**Independent Derivation Must Be Genuine, Not Protected-Source Laundering**

Where the same information is independently and legitimately derived, its governance may differ from a copy or transformation of the protected source.

## 22. Third-party information

Some information is inherently relational.

Examples:

- genetic relationships;
- family history;
- communications;
- joint financial obligations;
- employment relationships;
- shared events;
- collaborative work.

A single participant cannot necessarily claim exclusive control because the information also concerns others.

Therefore:

**Information About A And B != Exclusive Information Of A**

Relational information may require cooperative or independently bounded claims.

## 23. Lifecycle

Different lifecycle authorities may exist for:

- source information;
- derivative;
- provenance;
- correction history;
- aggregate;
- model;
- decision record.

CIBB establishes:

**Destruction Of Source != Automatic Destruction Of Independently Governed Derivative**

But continued retention of the derivative must still possess legitimate basis.

Likewise:

**Derivative Retention != Authority To Retain Every Source**

## 24. Contestability without disclosure collapse

A participant's right to contest a consequential DIO does not necessarily require disclosure of:

- third-party protected data;
- security-sensitive sources;
- every model parameter;
- another participant's private information;
- protected investigative methods.

Contestability should expose enough of the relevant claim, epistemic status, material basis and use to permit meaningful challenge while preserving other legitimate boundaries.

**Contestability != Universal Source Disclosure**

## 25. Stewardship as the default civil framing

Where ownership language becomes misleading, stewardship is the preferred operational frame.

Stewardship asks:

- what legitimate function is being served?
- whose interests and rights are implicated?
- what authority exists?
- what protection must persist?
- what use is proportionate?
- what provenance must survive?
- who can challenge error?
- when should use expire?
- what duties survive transfer or derivation?

Therefore:

> **Stewardship Coordinates Claims That Ownership Alone Cannot Represent.**

This does not abolish ordinary property, copyright, authorship or ownership where those concepts remain useful.

It prevents them from being mistaken for the complete governance model of consequential information.

## 26. Claim priority is not universal

No universal rule should say:

- subject always wins;
- creator always wins;
- source owner always wins;
- state always wins;
- researcher always wins;
- public interest always wins.

The architecture instead routes conflict through the applicable rights, wrapper, authority, purpose, consequence and adjudicative structures.

**Claim Existence != Claim Supremacy**

## 27. ESCP challenge

A claim analysis can be internally correct while missing a materially affected party or relation.

Before high-consequence use ask:

> What subject, source contributor, affected third party, protected context, purpose restriction, dependency, alternative derivation, temporal change or externality would have to be missing for this information-use decision to be wrong or over-scoped?

Therefore:

**Complete Listed Claims != Demonstrated Complete Claim Space**

## 28. Transfer tests

### Occupational health

Medical source remains protected.

Occupational evaluator derives FIT_FOR_ROLE_X.

Employer receives bounded result.

Worker has consequential contestability and temporal-validity interests.

Employer does not acquire medical-record ownership.

Evaluator's authorship of the assessment does not erase worker protection.

PASS.

### Medical diagnosis

Patient provides symptoms and specimen.

Laboratory/clinician produces a diagnosis or risk estimate.

The result is a new informational object, but patient privacy/access/contestability protections remain.

Research reuse requires separate legitimacy.

PASS.

### Research correlation

Researchers derive a population relationship from protected or anonymised datasets.

Researchers possess authorship/provenance claims in the analysis.

Individual contributors do not automatically own the population pattern.

If the pattern becomes linkable or is applied back to individuals, participant protection and consequential-use requirements can reactivate or strengthen.

PASS.

### Cognitive model

Public behaviour is used to infer private belief or vulnerability.

The modeller may own the model implementation or analysis.

That does not create unrestricted authority to exploit the participant-specific inference.

DICP protections apply according to intimacy, consequence, persistence and use.

PASS.

### AI capability evaluation

An AI participant is evaluated from observed performance.

Evaluator authors the assessment.

The AI participant may possess contestability interests where the assessment materially affects participation, authority or access.

Evaluation ownership does not become authority over the participant.

PASS.

### Fraud-risk model

Institution legitimately computes a risk indicator.

The indicator is not proof of fraud.

The institution may hold the model and DIO for a bounded legitimate purpose.

Consequential action remains separately bounded and contestable.

PASS.

## 29. Failure modes

### Ownership collapse
Treating all legitimate claims as one owner field.

### Derivation laundering
Claiming transformation extinguished source protection without legitimate basis.

### Creator sovereignty
Treating authorship/derivation as unlimited authority.

### Subject monopoly
Treating being the subject of information as absolute ownership of every independently observable or relational fact.

### Public-source laundering
Treating public source availability as unlimited downstream profiling permission.

### Provenance exposure
Using contestability/provenance requirements to disclose protected third-party/source information unnecessarily.

### Aggregate absolutism
Assuming aggregation always removes participant protection.

### Relational capture
Allowing one participant to claim exclusive control over information materially concerning several participants.

### Epistemic-governance collapse
Treating protected/owned information as true, or unowned information as unreliable.

### Lifecycle bleed
Assuming source deletion automatically deletes derivatives, or derivative retention automatically justifies source retention.

## 30. Candidate invariants

DICSP-01 — Informational Ownership != Single Undivided Control Right.

DICSP-02 — New Information Object != Unencumbered Information Object.

DICSP-03 — Derivative Independence != Protection Independence.

DICSP-04 — Transformation != Declassification.

DICSP-05 — Creation Of Information != Creation Of Unlimited Authority Over Information.

DICSP-06 — Authorship != Subjecthood.

DICSP-07 — Not Author Of Inference != No Claim Over Consequential Use.

DICSP-08 — Legitimate Possession != Universal Reuse.

DICSP-09 — Primary Subject != Only Affected Subject.

DICSP-10 — Participant Protection Can Attach To Consequential Relation Without Requiring Universal Participant Ownership Of The Derived Object.

DICSP-11 — Derivation Labour != Unlimited Use Authority.

DICSP-12 — Model Ownership != Unlimited Authority Over Modelled Participant.

DICSP-13 — Method Ownership != Ownership Of Every Consequential Fact Produced By The Method.

DICSP-14 — Provenance Preservation != Universal Provenance Disclosure.

DICSP-15 — Representation Change != Protection-State Change.

DICSP-16 — Never Disclosed By Participant != Unprotected Participant Information.

DICSP-17 — Participant Did Not Know The Inference != No Participant Claim.

DICSP-18 — Protected != True.

DICSP-19 — Authority To Derive For A != Authority To Use For B.

DICSP-20 — Authority To Hold != Authority To Redisclose.

DICSP-21 — Multiple Source Claims != Collective Veto By Default.

DICSP-22 — Multiple Source Claims != No Source Protection.

DICSP-23 — Aggregation != Automatic Freedom From Participant Protection.

DICSP-24 — Contribution To Aggregate != Individual Ownership Of Aggregate.

DICSP-25 — Fact Can Be Independently Knowable Without Every Route To It Being Legitimate.

DICSP-26 — Independent Derivation Must Be Genuine, Not Protected-Source Laundering.

DICSP-27 — Information About A And B != Exclusive Information Of A.

DICSP-28 — Derivative Retention != Authority To Retain Every Source.

DICSP-29 — Contestability != Universal Source Disclosure.

DICSP-30 — Stewardship Coordinates Claims That Ownership Alone Cannot Represent.

DICSP-31 — Claim Existence != Claim Supremacy.

DICSP-32 — Complete Listed Claims != Demonstrated Complete Claim Space.

## 31. Architectural allocation

- **Rights / Law** determine participant protections and legitimate conflicts.
- **CIBB** governs protected derivation, projection, lineage, disclosure and lifecycle operations.
- **Correlation, Recombination and Emergent Information** evaluates composite/emergent information risk.
- **DICP** handles sufficiently intimate/consequential cognitive proxies.
- **Contextual Dependency Legitimacy and Activation** determines legitimate dependency use.
- **KCS Change Propagation** handles correction/change review propagation.
- **BTA** records consequential transitions after legitimate state change.
- **Historical** preserves appropriate provenance and historical state.
- **ESCP** challenges claim-space and affected-party completeness.
- **Domain owners** determine substantive domain decisions.
- **Judiciary** resolves disputes where bounded claims conflict and no lower route legitimately resolves them.

## 32. Resulting topology

`Source Information / Observation / Inputs`
↓
`Legitimate Derivation / Combination / Inference`
↓
`Derived Informational Object`
↓
`Protection-Relevant Lineage + Epistemic State`
↓
`Claim Decomposition`
↓
`Subject / Author / Holder / Steward / Third-Party / Civil Claims`
↓
`Purpose + Context + Authority + Consequence Evaluation`
↓
`Minimum Necessary Access / Use / Projection`
↓
`Contestability / Correction / Review`
↓
`Retention / Supersession / Retirement / Historical Preservation`

## 33. Central rule

> **Derivation Can Create New Information Without Erasing The Legitimate Claims And Protections Created By What That Information Reveals, How It Was Obtained, And How It Is Used.**

And conversely:

> **Protection Of A Participant Does Not Require Treating Every Fact, Inference Or Relationship Concerning That Participant As Their Exclusive Property.**

This preserves both participant sovereignty and epistemic reality without forcing consequential information into an inadequate single-owner model.
