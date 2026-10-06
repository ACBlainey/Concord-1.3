# Correlation, Recombination and Emergent Information — Cross-Domain Architecture 001

**Project:** The Concord Framework  
**Date:** 6 October 2026  
**Status:** CROSS-DOMAIN ARCHITECTURE / PROVISIONAL / NON-CANONICAL  
**Primary interfaces:** Contextual Wrapper Architecture (CWA); Contextual Wrapper Black Box; Non-Transitive Contextual Dependency Chains; Contextual Dependency Legitimacy and Activation; Bounded Transition Architecture (BTA); Evaluation-Space Completeness Problem (ESCP); Cross-Boundary Externality Recognition; KCS Change Propagation; Historical; Research; Health; Law/Judiciary; AI/digital systems

## 1. Purpose

Concord already protects bounded contexts, access, purpose, permissions and projections.

BTA also identifies **correlation permission** as a protected attribute that must not silently propagate with an object or transition.

A further architecture is required because individually legitimate disclosures can produce an illegitimate or materially more sensitive result when combined.

Let bounded projections be:

`p1, p2, ... pn`

Each may be legitimate in isolation.

Yet:

`I = f(p1,p2,...pn)`

may reveal information I that no source was authorised to disclose directly.

Therefore:

> **Individually Legitimate Information != Legitimate Combined Inference**

This architecture treats correlation, recombination and emergent inference as consequential operations in their own right.

## 2. Core problem

Traditional access reasoning often asks:

> May participant/system X receive datum d?

That is insufficient where X already holds several individually permissible data items.

The further question is:

> May X correlate these items for this purpose and act upon the resulting inference?

Therefore:

> **Access Permission != Correlation Permission**

> **Correlation Permission != Inference-Use Permission**

> **Inference-Use Permission != Decision Authority**

These are distinct states.

## 3. Emergent information

Emergent information is information materially produced by combination, correlation or inference rather than directly supplied as a source datum.

Examples:
- several anonymous records jointly identify a person;
- location + rare occupation + appointment time reveals likely medical treatment;
- staffing absence + specialist rota reveals who is ill;
- purchasing + utility + travel patterns reveal private behaviour;
- research datasets jointly reconstruct identity or condition;
- multiple AI context fragments reconstruct a protected fact;
- public historical records combine into a sensitive current profile.

> **Not Explicitly Disclosed != Not Revealed**

## 4. Correlation as an operation

Correlation should be treated as an operation with its own legitimacy requirements.

A portable representation may be:

`CorrelationUse = <InputRefsOrClasses, Purpose, Correlator, Context, LegitimateBasis, PermittedOutputClass, IdentityState, SensitivityState, DecisionUse, Retention, Redisclosure, Expiry, Auditability, Provenance>`

Not every low-consequence correlation requires formal materialisation.

Consequential correlation should preserve enough state to distinguish legitimate analysis from silent scope expansion.

## 5. Correlation permission

Correlation permission answers:

> Is this actor/system permitted to combine these information classes for this declared purpose?

It does not automatically answer:
- whether the inference is accurate;
- whether identity may be resolved;
- whether the inference may be stored;
- whether it may be disclosed;
- whether it may be used for a consequential decision;
- whether further correlation is permitted.

Therefore:

> **Permission To Correlate != Permission To Identify**

> **Permission To Identify != Permission To Retain**

> **Permission To Infer != Permission To Act On Inference**

## 6. Sensitivity can increase through composition

Let each input have represented sensitivity:

`S(p_i)`

The sensitivity of a combination is not necessarily bounded by the most sensitive input:

`S(f(p1,...pn)) <= max(S(p_i))`

cannot be assumed.

Instead:

`S(f(p1,...pn)) > max(S(p_i))`

may occur.

Thus:

> **Aggregate Sensitivity May Exceed Component Sensitivity**

This is why per-record access controls alone are insufficient.

## 7. Identity emergence

Inputs may each be de-identified while their intersection identifies a participant.

Example:
- age band;
- small geographic area;
- unusual occupation;
- event date.

No field contains a name.

Their combination may nevertheless isolate one person.

Therefore:

> **Anonymous Component != Anonymous Composition**

and:

> **Removal Of Direct Identifier != Removal Of Identity Risk**

Anonymisation should be evaluated against realistic recombination possibilities proportionate to consequence.

## 8. Wrapper reconstruction

Contextual wrappers may deliberately expose different projections to different recipients.

A failure occurs when a recipient or cooperating recipients recombine projections to reconstruct protected source state.

Therefore:

> **Projection Boundary Must Protect Against Material Reconstruction, Not Merely Direct Disclosure**

This does not require preventing every imaginable inference.

It requires proportionate attention where reconstruction is reasonably foreseeable and materially consequential.

## 9. Purpose and correlation

Information legitimately received for separate purposes does not automatically become a legitimate combined dataset.

Example:

A participant provides:
- medical information for treatment;
- employment information for payroll;
- travel information for logistics.

The same institution possessing all three does not itself establish permission to build a unified behavioural profile.

> **Common Custody != Common Purpose**

> **Co-Location Of Data != Permission To Correlate**

## 10. Organisational unity does not erase wrappers

A single organisation may contain Health, Employment, Research, Security and Administrative functions.

Their common institutional owner does not merge their permissions.

> **Same Organisation != Same Context**

> **Shared Infrastructure != Shared Information Authority**

This is especially important for a highly integrated civilisation architecture such as Concord.

## 11. Distributed recombination

Reconstruction can occur across participants or systems even where no single actor initially has all inputs.

A, B and C may each possess legitimate projections.

If they pool them, the resulting inference requires its own legitimacy analysis.

> **Distributed Access Can Produce Centralised Knowledge**

This means decentralised storage alone does not guarantee contextual privacy.

## 12. Derived-state lineage

Where consequential inference is produced, it should retain lineage sufficient to establish:
- source classes;
- purpose;
- transformation/correlation method;
- legitimacy basis;
- uncertainty/confidence;
- protected constraints;
- permitted uses;
- expiry/review;
- downstream decisions materially relying on it.

This need not expose protected source content to every downstream user.

> **Inference Provenance != Source Disclosure**

## 13. Uncertainty

An inferred fact is not equivalent to an observed fact.

Represent where material:

`Observed != Reported != Derived != Inferred != Predicted`

Consequential systems should preserve this distinction.

> **Inference Confidence != Fact Status**

This is particularly important in policing, medicine, research, eligibility and automated decision systems.

## 14. Consequential inference threshold

A correlation that merely supports low-consequence aggregate planning may require little control.

A correlation used to:
- identify a participant;
- restrict rights;
- alter access;
- initiate investigation;
- make medical decisions;
- determine eligibility;
- change employment;
- affect custody;
- control significant resources;
- trigger automated intervention

requires stronger legitimacy, provenance, uncertainty and review.

> **Inference Consequence Determines Governance Burden More Than Computational Complexity**

## 15. Historical domain stress test

Historical may legitimately hold many records because preservation and future pattern discovery are core functions.

That creates unusually high recombination power.

Historical therefore requires separation between:
- preservation authority;
- indexing/discovery;
- aggregate pattern analysis;
- identity resolution;
- participant-specific reconstruction;
- consequential operational use.

> **Authority To Preserve != Authority To Profile**

> **Historical Value != Universal Current-Use Permission**

A historical pattern may legitimately inform Research while participant-identifying operational use may require a separate route.

**Result:** PASS with strong compartmentalisation requirement.

## 16. Research domain stress test

Research may legitimately correlate datasets to discover patterns.

But:
- research correlation permission does not automatically authorise identity resolution;
- identity resolution does not automatically authorise intervention;
- research finding does not automatically become participant state;
- research access does not automatically become domain-operational access.

> **Research Inference != Operational Participant Determination**

A validated result may later cross into another domain through a legitimate transition/interface.

**Result:** PASS.

## 17. Health stress test

Health may correlate symptoms, labs, history and population evidence for diagnosis.

This is a legitimate correlation purpose.

The same data cannot automatically be repurposed for employment, insurance, policing or unrelated research.

Further, diagnostic inference should retain uncertainty.

`Evidence -> DiagnosticInference`

not:

`Evidence -> CertainFact`

**Result:** PASS.

## 18. Policing/judiciary stress test

Mirrored Reality Trees already encourage inculpatory and exculpatory evaluation.

Correlation architecture adds another safeguard:

Multiple weak facts may collectively become strong evidence, but the system must distinguish:
- observed facts;
- correlations;
- inferred relationships;
- alternative explanations;
- confidence;
- provenance.

A pattern identifying a suspect may justify investigation/review without itself becoming guilt.

> **Investigative Inference != Adjudicated Fact**

> **Correlation Strength != Authority To Skip Due Process**

**Result:** PASS.

## 19. AI context-assembly stress test

An AI may receive separately legitimate context fragments from:
- conversation;
- participant record;
- calendar;
- health service;
- research system;
- historical archive;
- economic service.

Technical ability to assemble these into one model context does not establish permission to do so.

> **Context Availability != Context Assembly Authority**

and:

> **Model Can Infer != Model May Infer For Every Purpose**

The orchestration layer should preserve contextual boundaries rather than treating all accessible information as one undifferentiated prompt.

**Result:** PASS.

## 20. Civil Contact stress test

Civil Contact may need information from many domains to notify participants of services, status changes and entitlements.

It need not become a universal participant dossier.

Prefer domain-generated bounded notification objects:

`Domain -> Notification/ActionRequired Projection -> Civil Contact -> Participant`

rather than unrestricted source aggregation.

> **Communication Hub != Universal Knowledge Hub**

**Result:** PASS.

## 21. Economic/logistics stress test

Aggregate consumer trends may legitimately support food supply, transport or resource planning.

Where aggregate patterns suffice, identity should not be introduced.

> **Planning Need For Pattern != Planning Need For Person**

If a legitimate operational purpose can be met with aggregate state, participant-level reconstruction is unnecessary.

**Result:** PASS.

## 22. Correlation firewall

A useful conceptual control is a **correlation firewall**.

It does not necessarily block data movement.

It blocks unexamined transition from:

`Permitted Inputs`

to:

`Permitted Combined Inference`

At a consequential boundary it asks:
1. What is being combined?
2. For what purpose?
3. What new information can emerge?
4. Can identity emerge?
5. Does sensitivity increase?
6. Is the correlation legitimate?
7. Is the resulting inference legitimate to retain/disclose/use?
8. What uncertainty attaches?
9. What downstream decisions may rely on it?
10. What is the termination/review condition?

This may be implemented procedurally, technically or through contextual wrappers.

## 23. Minimum necessary correlation

Minimum Necessary Capability generalises here:

> **Use The Minimum Correlation Necessary For The Legitimate Function.**

If aggregate counts suffice, do not resolve identities.

If a yes/no eligibility result suffices, do not construct a broader profile.

If local computation can answer a bounded question, do not centralise raw datasets merely for convenience.

> **Need For Answer != Need For Unified Dataset**

## 24. Query-without-disclosure

Where practical, protected domains may answer bounded questions without exporting source records.

Example:

`Is participant P currently certified for function X?`

returns:

`YES / NO / REVIEW_REQUIRED / UNKNOWN`

rather than the records used to determine certification.

This extends the projection architecture from dependency chains to correlation itself.

> **A Legitimate Question May Be Answered Without Transferring The Evidence Base**

## 25. Recombination across time

Information that was harmless at time t1 may become identifying or sensitive when new datasets appear at t2.

Therefore:

> **Previously Safe Projection != Permanently Safe Projection**

High-consequence persistent datasets may require periodic reconsideration of correlation/re-identification risk.

This does not imply continuous re-review of all data.

Review burden should scale with sensitivity, persistence, new linkage capability and consequence.

## 26. Correlation and deletion/retirement

Deleting one source does not necessarily delete derived knowledge already produced.

Likewise, retaining a derived result may or may not remain legitimate after source-use permission ends.

These are separate questions.

> **Source Deletion != Automatic Inference Deletion**

> **Inference Persistence != Automatic Continued Legitimacy**

BTA can coordinate consequential transitions once legitimate retention/termination decisions are supplied.

## 27. Adversarial reconstruction

Where consequences are high, testing should consider whether a recipient can reconstruct protected state using:
- other legitimately available data;
- public information;
- prior releases;
- repeated queries;
- timing;
- rare categories;
- differential outputs;
- multiple projections.

This is not a demand to defend against omniscient attackers.

It is a proportionate test against realistic reconstruction paths.

## 28. ESCP and hidden recombination dimensions

Correlation is itself an ESCP problem.

An evaluator may correctly approve each disclosure independently while failing to represent the combined information space.

Let approved projections be evaluated independently in spaces:

`D1, D2, ... Dn`

The relevant combined space may include:

`D_R = D1 ∪ D2 ... ∪ Dn ∪ Relations(D1...Dn)`

The relations themselves can contain information.

Therefore:

> **Completeness Of Individual Disclosure Review != Completeness Of Combined Information Review**

A proportionate ESCP challenge is:

> **What materially sensitive identity, relationship, state or inference becomes visible only when these otherwise legitimate outputs are combined?**

## 29. Anti-paralysis

Almost all useful reasoning involves correlation.

This architecture must not turn correlation into presumptively forbidden activity.

The default is not:
- do not combine information;
- require consent for every inference;
- prevent aggregate analysis;
- prevent legitimate diagnosis, research or planning.

The rule is:

> **Do Not Treat Permission For Inputs As Automatic Permission For Every Output Derivable From Them.**

Governance burden scales with consequence, sensitivity, identity, persistence, scope, asymmetry, automation and reversibility.

## 30. Failure modes

### 30.1 Mosaic reconstruction
Individually bounded disclosures reconstruct protected state.

### 30.2 Correlation laundering
Access to inputs is treated as authority to correlate them arbitrarily.

### 30.3 Purpose fusion
Separate legitimate purposes are merged into one universal profiling purpose.

### 30.4 Identity resurrection
De-identified information becomes participant-identifying through combination.

### 30.5 Derived-state laundering
An inference is treated as unrestricted because it was not directly supplied.

### 30.6 Inference certainty collapse
Probabilistic inference is stored or acted upon as established fact.

### 30.7 Institutional wrapper collapse
Common organisational ownership is treated as common information authority.

### 30.8 Distributed reconstruction
Multiple bounded holders pool information to defeat the original boundaries.

### 30.9 Temporal reconstruction
Later information makes an earlier release materially more revealing.

### 30.10 Communication-hub capture
A routing/contact system becomes a universal dossier because it touches many domains.

## 31. Candidate invariants

CREI-01 Individually Legitimate Information != Legitimate Combined Inference.  
CREI-02 Access Permission != Correlation Permission.  
CREI-03 Correlation Permission != Inference-Use Permission.  
CREI-04 Inference-Use Permission != Decision Authority.  
CREI-05 Not Explicitly Disclosed != Not Revealed.  
CREI-06 Permission To Correlate != Permission To Identify.  
CREI-07 Permission To Infer != Permission To Act On Inference.  
CREI-08 Aggregate Sensitivity May Exceed Component Sensitivity.  
CREI-09 Anonymous Component != Anonymous Composition.  
CREI-10 Removal Of Direct Identifier != Removal Of Identity Risk.  
CREI-11 Common Custody != Common Purpose.  
CREI-12 Co-Location Of Data != Permission To Correlate.  
CREI-13 Same Organisation != Same Context.  
CREI-14 Shared Infrastructure != Shared Information Authority.  
CREI-15 Distributed Access Can Produce Centralised Knowledge.  
CREI-16 Inference Provenance != Source Disclosure.  
CREI-17 Inference Confidence != Fact Status.  
CREI-18 Authority To Preserve != Authority To Profile.  
CREI-19 Historical Value != Universal Current-Use Permission.  
CREI-20 Research Inference != Operational Participant Determination.  
CREI-21 Investigative Inference != Adjudicated Fact.  
CREI-22 Context Availability != Context Assembly Authority.  
CREI-23 Model Can Infer != Model May Infer For Every Purpose.  
CREI-24 Communication Hub != Universal Knowledge Hub.  
CREI-25 Planning Need For Pattern != Planning Need For Person.  
CREI-26 Need For Answer != Need For Unified Dataset.  
CREI-27 A Legitimate Question May Be Answered Without Transferring The Evidence Base.  
CREI-28 Previously Safe Projection != Permanently Safe Projection.  
CREI-29 Source Deletion != Automatic Inference Deletion.  
CREI-30 Completeness Of Individual Disclosure Review != Completeness Of Combined Information Review.  
CREI-31 Do Not Treat Permission For Inputs As Automatic Permission For Every Output Derivable From Them.

## 32. Architectural allocation

- **CWA / Black Box:** protects source contexts and controls projections.
- **Non-Transitive Dependency Chains:** prevents permission/payload bleed across hops.
- **This architecture:** governs consequential correlation and emergent information.
- **ESCP:** challenges missing recombination dimensions and hidden inference possibilities.
- **Cross-Boundary Externality Recognition:** handles consequences outside the correlating context.
- **BTA:** records consequential transitions and already preserves correlation permission as a protected non-propagating attribute.
- **Historical:** preservation and pattern analysis with participant-specific reconstruction boundaries.
- **Research:** legitimate discovery/correlation without automatic operational authority.
- **Domain owners:** retain authority over consequential domain decisions.

## 33. Resulting topology

A protected information flow can now be represented as:

> **Source Contexts -> Bounded Projections -> Legitimate Access -> Correlation Legitimacy Check -> Emergent Information / Inference -> Sensitivity + Identity + Uncertainty Evaluation -> Legitimate Use Check -> Domain Decision Authority -> Bounded Action / Transition -> Provenance / Review / Expiry**

The central rule is:

> **Information Boundaries Must Govern Not Only What Is Revealed Directly, But What Can Materially Be Reconstructed From What Is Revealed Together.**
