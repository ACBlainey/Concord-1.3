# Cross Boundary Externality Recognition — Portable Module

**Version:** 1.0  
**Status:** GRADUATED PORTABLE MODULE / SPECIFICATION-LEVEL TRANSFER VALIDATED  
**Development level:** Level B — Extractable Architecture  
**Origin:** Concord Cross-Boundary Externality Recognition and Responsibility Mechanism (CBERRM)  
**Date:** 23 September 2026

## 1. Purpose

Bounded systems can impose consequences outside their own boundaries without sharing a government, authority structure, ontology, trust relationship or decision process with those affected.

The portable problem is:

> **How can a material consequence crossing an organisational, technical, jurisdictional or other legitimate boundary be recognised, evidenced, contested and routed toward an appropriate response without allowing the consequence itself to manufacture unlimited authority across that boundary?**

This module provides a bounded architecture for representing and routing such cases.

It is not itself a court, regulator, mediator, government or enforcement authority.

## 2. Core principle

> **Recognise and evidence cross-boundary consequences without allowing consequence recognition to create authority beyond what is independently legitimate and functionally necessary.**

Operational shorthand:

> **Make the consequence legible; keep responsibility, authority and remedy separate.**

## 3. Core separations

The module depends on preserving these distinctions:

> **Consequence ≠ Responsibility**

> **Responsibility ≠ Authority / Jurisdiction**

> **Authority / Jurisdiction ≠ Remedy**

> **Remedy ≠ General Authority**

> **Communication ≠ Recognition**

> **Coordination ≠ Subordination**

> **Standing to Raise ≠ Authority to Decide**

> **Severity ≠ Proof of Causation**

> **Refusal ≠ Exoneration**

> **Refusal ≠ Automatic Authority Over Refuser**

> **Disputed Standing ≠ No Possible Consequence**

> **Mitigation Capability ≠ Sole Causal Responsibility**

A valid externality case may exist even where responsibility, standing, authority or remedy remains unresolved.

## 4. Scope

The module applies where:

1. an action, omission, failure, persistent condition or system state may produce a material consequence;
2. the consequence crosses a meaningful boundary;
3. the affected side is not automatically governed by the originating side's internal decision process; and
4. some evidence-bearing response, coordination or review may be useful.

Possible boundaries include:

- organisational;
- jurisdictional;
- technical;
- contractual;
- network;
- infrastructure;
- resource;
- community;
- institutional;
- civilisational;
- other explicitly bounded domains.

## 5. What the module does not do

The module does not:

- manufacture authority from harm;
- determine universal legal jurisdiction;
- decide universal personhood or standing;
- compel participation;
- convert communication into recognition;
- impose a remedy;
- assume accusation is proof;
- require a shared government;
- require all parties to share one ontology;
- require every party to participate before a case can remain represented.

## 6. Minimum inputs

A case requires at least:

1. initiating signal or event;
2. claimed originating action, system or domain;
3. claimed affected domain or parties;
4. asserted consequence;
5. initial evidence and provenance;
6. known standing or representation state;
7. known authority or coordination interfaces;
8. known uncertainty or dispute state.

Unknown fields may remain UNKNOWN rather than being invented.

## 7. Core operating chain

**Signal/Event → Externality Candidate → Affected Party/Domain → Standing to Raise → Evidence/Causal Confidence → Materiality → Responsibility Mapping → Authority/Coordination Mapping → Minimum Necessary Response → Review/Correction → Provenance/State Update**

Each transition should preserve unresolved and disputed information.

## 8. Externality candidate

Open an externality candidate when there is credible reason to examine whether an action, omission, failure, persistent condition or system state produces a material consequence outside its originating domain.

Candidate classes may include:

- environmental/resource;
- infrastructure;
- informational/digital;
- biological/health;
- economic/resource-flow;
- security/safety;
- rights/personhood;
- migration/mobility;
- shared-space/shared-system;
- delayed/cumulative;
- unknown/mixed.

Opening a candidate means only:

> **This possible cross-boundary consequence warrants bounded examination.**

It does not establish harm, fault, authority or remedy.

## 9. Affected parties and domains

Identify, where possible:

- directly affected parties;
- indirectly affected parties;
- affected shared systems/resources;
- affected bounded domains;
- parties unable to raise the issue themselves;
- potentially disputed representatives;
- relevant operators or custodians.

Do not erase an affected entity merely because another party disputes its classification.

## 10. Standing to raise

A case may be raised by parties occupying different standing roles, including:

- **DIRECTLY-AFFECTED** — a party directly experiencing the claimed consequence;
- **AUTHORISED-REPRESENTATIVE** — a party authorised to represent an affected party or population within a defined scope;
- **CONSULTATION/ADVOCACY-STANDING** — a recognised consultation or advocacy body permitted to raise concerns without thereby possessing representative or decision authority;
- **SYSTEM/OPERATOR-STANDING** — a legitimate bounded system, shared-resource operator or infrastructure operator acting within its remit;
- **MONITORING-STANDING** — an agreed monitoring interface;
- **EVIDENCE-BEARING-THIRD-PARTY** — a party presenting credible evidence where an affected party cannot practically raise the issue;
- **DISPUTED/UNKNOWN** — standing or representation cannot yet be resolved.

The threshold to open examination is deliberately weaker than the threshold to decide or impose a response.

> **Standing to Raise ≠ Authority to Decide**

Standing may be CONFIRMED, DISPUTED, UNKNOWN or otherwise explicitly qualified.

Standing should record both role and scope:

**Standing = <Party, Role, Scope, SourceOfAuthority, Limits, State>**

Authority to raise concerns does not by itself include authority to receive protected information, negotiate, settle, bind another party, accept compensation, or exercise any other ungranted function.

## 11. Evidence state

Record evidence without forcing premature certainty.

Candidate evidence states:

- OBSERVED;
- CORROBORATED;
- CONTESTED;
- INCOMPLETE;
- INDIRECT;
- MODEL-DEPENDENT;
- UNKNOWN;
- DISPUTED;
- REFUTED;
- SUPERSEDED.

Evidence state should retain provenance.

Where measurement, semantic or interpretive systems differ, record translation assumptions rather than silently normalising them.

## 12. Causal confidence

Represent causal confidence separately from:

- consequence severity;
- materiality;
- responsibility;
- authority;
- remedy.

A severe alleged consequence with weak causal evidence is not equivalent to a moderate consequence with strong causal evidence.

> **Severity of Allegation ≠ Causal Confidence**

No universal numeric confidence scale is required.

## 13. Materiality

Not every cross-boundary effect requires a formal response.

Materiality must be evaluated against the **declared context and consequence under examination**. Where the available evidence does not support a stable material/non-material conclusion, record **MATERIALITY-UNCERTAIN** rather than forcing binary closure.

Opening a candidate is a triage action, not a finding that escalation is required.

> **Candidate Opened ≠ Escalation Required**



Materiality may consider:

- severity;
- scale;
- duration;
- reversibility;
- recurrence;
- affected population/system;
- rights impact;
- resource/ecological impact;
- dependency criticality;
- uncertainty;
- cumulative effect;
- recovery cost.

A low-probability but irreversible consequence may remain material for examination.

Materiality does not establish causation.

One consequence may have different materiality states in different legitimate contexts. Record them separately:

**MaterialityAssessment = <Consequence, Context, Threshold/Function, State, Evidence, Uncertainty>**

> **One Consequence ≠ One Universal Materiality State**

## 14. Responsibility mapping

Candidate responsibility states include:

- DIRECT;
- CONTRIBUTORY;
- SHARED;
- INDIRECT;
- FAILURE-TO-MITIGATE;
- UNKNOWN;
- DISPUTED;
- NOT-ESTABLISHED.

Before assigning responsibility, causal mapping may record:

- **POSSIBLE-CONTRIBUTOR** — compatible with the evidence but weakly supported;
- **PLAUSIBLE-CONTRIBUTOR** — evidence provides a credible causal pathway but contribution is not established;
- **SUPPORTED-CONTRIBUTOR** — evidence materially supports actual contribution;
- **NON-AGENT-CONTRIBUTOR** — environmental, systemic or other non-agent causal factor;
- **UNIDENTIFIED-CONTRIBUTOR** — evidence supports an additional causal source whose responsible party, if any, is not identified.

Only supported causal contribution, combined with the relevant normative/domain criteria, should be advanced to CONTRIBUTORY responsibility.

> **Causal Contributor ≠ Responsible Party**

Do not force multi-causal cases into one responsible actor.

Distinguish:

- historical cause;
- current contribution;
- current control;
- current capacity to mitigate;
- agreed responsibility;
- disputed responsibility.

> **Ability to Reduce Harm ≠ Admission of Sole Responsibility**

> **Responsibility Mapping ≠ Quantitative Apportionment**

The module may represent contributors and responsibility states, but it does not calculate legal, financial, scientific or compensatory shares. Where proportional attribution is required, use an appropriate domain-specific method. Preserve UNKNOWN where the evidence cannot support apportionment.

## 15. Authority and coordination mapping

After consequence and responsibility are represented, map what legitimate pathways actually exist.

Candidate states:

- INTERNAL-AUTHORITY;
- SHARED/AGREED-AUTHORITY;
- OVERLAPPING-AUTHORITY;
- AUTHORITY-DISPUTED;
- NO-SHARED-AUTHORITY;
- VOLUNTARY-COORDINATION-AVAILABLE;
- OPTIONAL-MEDIATION-AVAILABLE;
- EMERGENCY-CONTACT-ONLY;
- NO-FURTHER-SHARED-PROCESS;
- UNKNOWN.

Legal jurisdiction is one specialised form of authority.

The absence of shared authority does not erase a consequence.

The existence of a consequence does not create shared authority.

## 16. Minimum necessary response

Select the smallest response scope that is both:

1. capable of addressing the demonstrated consequence; and
2. independently legitimate for the actors undertaking it.

Where no shared authority exists, “minimum necessary” is **actor-relative to independently legitimate authority**. Each actor may select a bounded response within its own legitimate domain. A shared response requires a legitimate shared interface or voluntary agreement; no hypothetical central evaluator gains authority merely by identifying a smaller response.

Where multiple actors independently choose compatible voluntary actions without creating a formal shared authority, record **PARALLEL-VOLUNTARY-COORDINATION**. This records coordination of effect, not a new institution or authority.

Possible pathways include:

- information exchange;
- verification;
- warning;
- temporary mitigation;
- technical coordination;
- repair/compensation negotiation;
- bounded operational agreement;
- functionally bounded negotiation;
- agreed mediation;
- shared-resource procedure;
- existing legitimate adjudication;
- monitoring;
- recorded no-action.

> **Response Scope Should Follow Demonstrated Function, Not Opportunistic Authority Expansion**

## 17. Scope expansion

A bounded case may reveal genuine cross-domain dependencies.

Scope may expand only when:

1. a material dependency is demonstrated;
2. the expansion is recorded;
3. newly relevant parties receive appropriate standing;
4. the expansion does not silently create general authority.

> **Functional Boundedness ≠ Functional Isolation**

## 18. Non-participation

A materially implicated party may refuse the shared process.

Record refusal explicitly.

CB-C9 requires affirmative refusal or non-participation after a relevant participation pathway exists or has been offered. Passive absence, lack of authorisation, non-involvement, or failure to be contacted is not automatically refusal.

The case may retain its evidence, uncertainty and externality state.

Other parties may continue:

- evidence preservation;
- warnings;
- monitoring;
- mitigation within their own legitimate domains;
- other independently authorised responses.

Any stronger action requires independently legitimate authority.

> **Refusal ≠ Exoneration**

> **Refusal ≠ Automatic Authority Over Refuser**

## 19. Classification and standing disagreement

Different systems may classify an affected entity, population, resource or interest differently.

The module does not need to settle the underlying ontology before representing the possible consequence.

Record standing as DISPUTED where appropriate.

> **Foreign Classification ≠ Automatic Epistemic Authority Over Standing**

> **Disputed Standing ≠ No Possible Consequence**

Specialised rights, legal or ontology mechanisms may be required downstream.

## 20. Low-trust operation

Where trust is low, prefer:

- narrow scope;
- explicit evidence provenance;
- independent corroboration where available;
- reversible interim measures;
- function-specific communication;
- visible disagreement states;
- bounded failure;
- no inference from participation to broader recognition.

The module should remain usable without broad political, organisational or institutional trust.

## 21. Correction

Externality cases are corrigible.

New evidence may:

- strengthen causation;
- weaken causation;
- reveal another contributor;
- alter materiality;
- resolve or reopen standing;
- change authority mapping;
- demonstrate successful mitigation;
- invalidate an earlier claim.

Use:

**Case State → New Evidence/Outcome → Review → Correction/Supersession → Updated Case State**

Correction should propagate to materially dependent decisions where possible.

Minimum review-trigger record:

**ReviewTrigger = <Condition/Event, AffectedField, RequiredReview, Provenance>**

Review triggers may arise from changes in evidence, materiality, standing, authority, consequence, recurrence, outcome, or another field that could materially alter the case.

## 22. Provenance

Preserve at minimum:

- who raised the case;
- what was alleged;
- evidence available at each stage;
- causal confidence and uncertainty;
- standing disputes;
- responsibility hypotheses;
- authority claims;
- proposed and rejected responses;
- scope changes;
- participation/refusal;
- outcomes;
- corrections;
- unresolved questions.

Later agreement must not erase the provenance of earlier uncertainty.

## 23. Boundary mapping

A single incident may cross several nested or intersecting boundaries.

For each claimed consequence, identify:

- the **primary evaluated boundary** across which that consequence is being assessed;
- any **secondary/dependency boundaries** materially relevant to causation, standing, authority or response.

Different consequences arising from one incident may therefore require separate boundary mappings.

The **primary evaluated boundary** is selected relative to the specific claimed consequence: it is the boundary across which that consequence is alleged to propagate. Secondary boundaries are dependencies materially relevant to causation, standing, authority or response.

> **One Incident ≠ One Boundary**

## 24. Assertion state

Individual assertions inside a valid externality case may have different evidential dispositions from the case as a whole.

Candidate assertion states include:

- SUPPORTED;
- PARTIALLY-SUPPORTED;
- UNSUPPORTED;
- OVERSTATED;
- CONTESTED;
- REFUTED;
- SUPERSEDED;
- UNKNOWN.

An unsupported or refuted subclaim does not automatically refute the underlying externality case.

> **Assertion Disposition ≠ Case Disposition**

This is an evidential/provenance function. It does not create authority to regulate speech or impose sanctions.

An assertion becomes a separate externality candidate only where a separately alleged material consequence from that assertion crosses a meaningful boundary and independently satisfies the candidate-opening conditions.

> **Unsupported Assertion ≠ Automatically Separate Externality**

## 25. Candidate case record

**ExternalityCase = <ID, Origin, AffectedDomain, AffectedParties, Standing, Evidence, Causality, Materiality, Responsibility, Authority, ResponseScope, Participants, State, Review, Provenance>**

This is a conceptual schema, not a mandated software format.

## 26. Candidate case states

A case may occupy states such as:

- SIGNAL;
- OPEN;
- EVIDENCE-GATHERING;
- CONTESTED;
- MATERIALITY-CONFIRMED;
- RESPONSIBILITY-PARTIAL;
- RESPONSIBILITY-ESTABLISHED;
- AUTHORITY-MAPPED;
- COORDINATION-ACTIVE;
- MITIGATION-ACTIVE;
- REPAIR-ACTIVE;
- MONITORING;
- RESOLVED;
- CLOSED-NO-ACTION;
- SUPERSEDED;
- UNKNOWN;
- DISPUTED.

These states describe the case.

> **Case State ≠ Grant of Authority**

## 27. Output classifications

A portable application should be able to return one or more of:

**CB-C1 — CANDIDATE ONLY**  
Possible cross-boundary consequence represented; materiality/causation not established.

**CB-C2 — EVIDENCE DEVELOPMENT REQUIRED**  
Case is representable but evidence is insufficient for stronger conclusions.

**CB-C3 — MATERIAL CONSEQUENCE SUPPORTED**  
Evidence supports a material cross-boundary consequence; responsibility may remain unresolved.

**CB-C4 — RESPONSIBILITY PARTIAL / DISTRIBUTED**  
One or more responsibilities are supported but responsibility is not singular or complete. Mere POSSIBLE-CONTRIBUTOR or PLAUSIBLE-CONTRIBUTOR status is insufficient for CB-C4.

**CB-C5 — RESPONSIBILITY SUFFICIENTLY ESTABLISHED FOR BOUNDED RESPONSE MAPPING**  
Evidence supports responsibility strongly enough to examine legitimate response pathways.

**CB-C6 — AUTHORITY / JURISDICTION UNRESOLVED**  
Consequence or responsibility may be supported while authority remains disputed or absent.

**CB-C7 — VOLUNTARY COORDINATION PATH AVAILABLE**  
A bounded non-coercive response interface exists.

**CB-C8 — INDEPENDENTLY AUTHORISED RESPONSE PATH AVAILABLE**  
A response may proceed under authority that exists independently of the externality claim.

**CB-C9 — PARTY NONPARTICIPATING / CASE RETAINED**  
A relevant party refuses the process; the evidential case remains represented.

**CB-C10 — NO FURTHER SHARED PROCESS IDENTIFIED**  
No legitimate shared pathway is presently available; independently legitimate actions may remain possible.

**CB-C11 — CLAIM REFUTED / SUPERSEDED**  
Later evidence materially defeats or replaces the earlier case state.

**CB-C12[dimension] — UNRESOLVED**  
The available evaluation space is insufficient for a stronger classification within a specified dimension, for example CB-C12[responsibility] or CB-C12[materiality]. A whole-case CB-C12 may be used only where insufficient closure applies across the case as a whole.

The classifications are **dimension-specific**, not a single mutually exclusive ladder:

- **Evidence/consequence:** CB-C1, CB-C2, CB-C3;
- **Responsibility:** CB-C4, CB-C5;
- **Authority/coordination:** CB-C6, CB-C7, CB-C8, CB-C10;
- **Participation:** CB-C9;
- **Case disposition:** CB-C11;
- **Evaluation-space closure:** CB-C12[dimension], or whole-case CB-C12 where appropriate.

Multiple classifications may coexist where they answer different questions.

> **Multiple Dimension Classifications ≠ Contradictory Case States**

CB-C11 applies to the disposition of the case or a clearly defined case branch. Use the separate assertion-state vocabulary when only one claim inside a continuing case is unsupported, refuted or superseded.

## 28. Failure modes

### 28.1 Authority laundering

A consequence claim is used to manufacture broad authority over another domain.

### 28.2 Standing laundering

Opening a case is treated as authority to represent every affected party.

### 28.3 Recognition laundering

Communication or coordination is treated as broader political, organisational or legal recognition.

### 28.4 Refusal laundering

Refusal to participate is treated as proof that no valid externality exists.

### 28.5 Evidence laundering

Severity or moral salience is treated as proof of causation.

### 28.6 Boundary denial

A party treats effects outside its own boundary as irrelevant merely because they are external.

### 28.7 Accusation as proof

Opening a candidate is treated as established harm or responsibility.

### 28.8 Single-cause compression

Distributed causation is forced into one responsible actor.

### 28.9 Remedy expansion

A bounded remedy becomes justification for general control.

### 28.10 Scope contamination

Failure in one issue unnecessarily contaminates unrelated relationships or domains.

### 28.11 Uncertainty erasure

UNKNOWN or DISPUTED states are forced into false certainty.

### 28.12 Mitigation-responsibility conflation

Capacity to help is treated as admission of sole fault.

### 28.13 Non-participation paralysis

Refusal prevents evidence preservation or independently legitimate mitigation.

### 28.14 Provenance loss

Later resolution erases the earlier evidential state, disagreement or correction history.

## 29. Adversarial checks

Reject the following inferences:

> “You affected us, therefore we may govern your internal system.”

> “We raised the case, therefore our preferred representative speaks for everyone affected.”

> “You communicated or negotiated with us, therefore you recognise all of our wider claims.”

> “We refused the process, therefore no valid externality finding can exist.”

> “The alleged consequence is severe, therefore causation is proven.”

> “We choose separation, therefore consequences we impose beyond our boundary are irrelevant.”

Each inference collapses distinctions the module exists to preserve.

## 30. Interfaces with other methods

This module may interface with, but does not require:

- Minimum Necessary Capability;
- Functionally Bounded Summits;
- Contextual Wrapper Architecture;
- rights/standing translation mechanisms;
- evidence/provenance systems;
- dependency/topology mapping;
- existing legitimate judiciary, governance or arbitration;
- domain-specific monitoring and measurement systems.

An interface must not silently transfer authority from one module or institution to another.

## 31. Specialised domains

Additional domain rules may be required for:

- legal jurisdiction;
- environmental science;
- medical/public-health causation;
- cybersecurity;
- financial systems;
- rights/personhood;
- shared infrastructure;
- international or intercivilisational relations.

The portable module supplies the case architecture, not domain certification.

## 32. Epistemic safeguards

The following safeguards are mandatory:

> **No Evidence Found in Examined Space ≠ Evidence Does Not Exist**

> **No Shared Authority Found ≠ Consequence Did Not Occur**

> **Case Opened ≠ Claim Proven**

> **Material Consequence Supported ≠ Responsibility Fully Established**

> **Responsibility Established ≠ Remedy Automatically Legitimate**

> **Tested in One Context ≠ Validated in Every Context**

Where source or dependency resolution is incomplete, classify the field as UNKNOWN or UNRESOLVED rather than inventing closure.

## 33. Minimum operating procedure

1. Define the boundary crossed.
2. Record the signal/event and alleged consequence.
3. Identify potentially affected parties/domains.
4. Record standing and representation state.
5. Record evidence and provenance.
6. Assess causal confidence separately from severity.
7. Assess materiality.
8. Map responsibility without forcing singular causation.
9. Map existing authority and coordination pathways.
10. Select the minimum legitimate response scope.
11. Record refusal, disagreement and exclusions.
12. Preserve correction/review triggers.
13. Update provenance and dependent decisions when the case changes.

## 34. Minimal record

A minimal implementation should record:

- case ID;
- boundary;
- origin;
- affected domain/parties;
- alleged consequence;
- standing state;
- evidence state;
- causal state;
- materiality;
- responsibility state;
- authority state;
- selected response path;
- explicit scope;
- explicit exclusions;
- participation/refusal;
- unresolved fields;
- review trigger;
- provenance.

## 35. Portability claim

The architecture is intended to be usable outside Concord because its central problem is generic:

**effects can cross boundaries even when authority does not.**

The module does not require adoption of Concord institutions or civilisation-level governance.

Its portability has now demonstrated functional specification-level transfer in two materially different non-Concord domains. This does not constitute empirical validation in real operational systems.

## 36. Validation status

The source mechanism contains seven bounded internal scenarios and adversarial checks, but those tests were part of source development.

They are not independent portable-transfer validation.

Current supported claims:

> **A coherent standalone specification has been extracted from a source mechanism with explicit pre-development requirements and falsification conditions.**

> **BTT-001 demonstrated functional independent transfer: 22/22 frozen predictions materially confirmed.**

> **BTT-002 demonstrated functional independent transfer in a materially different domain: 28/28 frozen predictions materially confirmed.**

> **Combined blind-transfer record: 50/50 frozen predictions materially confirmed across two materially different non-Concord domains.**

These are specification-level transfer results, not universal or empirical validation.

## 37. Development provenance

Primary development sources:

- `02_Epistemic_and_Research/Civilisational_Developmental_Topology/Exposure Investigation E2 - L3-13 Externality Recognition Beyond Current Civil Boundaries.md`
- `11_Intercivilisational_Architecture/07_Disputes_Jurisdiction_and_Externalities/Development Freeze 001 — L3-13 Cross-Boundary Externality Mechanism.md`
- `11_Intercivilisational_Architecture/07_Disputes_Jurisdiction_and_Externalities/Cross-Boundary Externality Recognition and Responsibility Mechanism.md`
- `Source Resolution and Extraction Audit 001.md`

## 38. Release status

Portable-package graduation review: **PASS**.

Validation record:

- BTT-001: 22/22 frozen predictions materially confirmed — CB-T3 Functional Transfer.
- BTT-002: 28/28 frozen predictions materially confirmed — CB-T3 Functional Transfer.
- Combined: **50/50 frozen predictions materially confirmed across two materially different non-Concord domains.**
- Graduation review found the v0.3 delta clarificatory rather than architecturally transformative.
- No release blocker identified.

> **Specification-Level Transfer Validated ≠ Empirical or Universal Validation**

Version 1.0 is the graduated portable package. Future revisions should preserve provenance and re-test any materially altered mechanism.
