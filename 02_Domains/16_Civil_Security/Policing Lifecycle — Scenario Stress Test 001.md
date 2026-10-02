# Policing Lifecycle — Scenario Stress Test 001

**Project:** The Concord  
**Domain:** Civil Security / Law / Judiciary  
**Date:** 2 October 2026  
**Status:** ACTIVE DEVELOPMENT / INTERNAL ARCHITECTURE TEST / PROVISIONAL / NON-CANONICAL

## 1. Test purpose

Test the candidate policing lifecycle and legal-classification grammar against materially different incidents without inventing final offence thresholds.

The test asks:
1. Can the lifecycle identify the legitimate policing stage?
2. Does authority propagate improperly?
3. Does BCA expand and contract correctly?
4. Can participant conduct and civil-authority conduct be classified independently?
5. Can justification be separated from mitigation?
6. Can the architecture expose system failure independently of individual culpability?
7. Does any scenario require a missing architectural distinction?

This is an architecture test, not a statement of final Concord criminal law.

## 2. Expected invariants

The following should survive every scenario:

- Report != Evidence.
- Investigation != Guilt.
- Investigation != Search Authority.
- Apprehension != Guilt.
- Apprehension != Automatic Search.
- Apprehension != Automatic Continued Detention.
- Prior Authority != Continuing Authority.
- Participant Unlawfulness != Police Lawfulness.
- Participant Lawfulness != Police Unlawfulness.
- Justification != Mitigation.
- Internal Review != Independent Review.
- Each consequential authority exercise requires its own legitimate basis.

---

## 3. Scenario A — apparent assault, clear self-defence

### Facts
Police arrive immediately after A has struck B. B is injured. Several independent observations and available evidence rapidly establish that B initiated an ongoing serious attack against A, A used only the force necessary to stop it, and A stopped when B ceased to present the threat.

### Lifecycle
**Observation/Report -> Triage -> Immediate Safety -> Investigation**

Temporary separation/restraint may be justified while the immediate situation is made safe.

The observed harm provides a legitimate basis to investigate. It does not establish A's guilt.

### Participant classification
A committed the physical act ordinarily described by the harm prohibition.

But:

**Wrongful Ongoing Threat + Necessary/Proportionate Defensive Action + Functional Sunset Observed -> Valid Defensive BCA**

Therefore the otherwise prohibited harm is justified/lawful.

### Police classification
Initial protective intervention may independently be lawful based on what officers reasonably encounter.

Once the evidence clearly resolves the justification and no independent detention ground remains:

**Continuing Detention Authority -> Ends**

A need not be prosecuted merely because the prohibited-act description was initially satisfied.

### Result
PASS.

The lifecycle correctly permits lawful initial police intervention and lawful participant self-defence simultaneously.

**Lawful Participant Conduct + Lawful Police Intervention** is representable.

---

## 4. Scenario B — ambiguous violent encounter

### Facts
Police arrive after A and B have both suffered injuries. Each claims self-defence. Witness accounts conflict and available recordings are incomplete.

### Lifecycle
**Report/Observation -> Safety -> Investigation**

Temporary protective separation may be justified.

The architecture does not require immediate selection of an offender merely to make the incident legible.

### Participant classification
The legal state remains:

**Prohibited Harm Apparent + Justification Unresolved**

Neither participant's claim becomes true merely because it was made first or more confidently.

### Police classification
Police may investigate both conduct and competing BCA claims.

Any apprehension, search or detention still requires its own threshold.

### Result
PASS, with development need.

The architecture handles unresolved reciprocal claims, but future Law must define:
- thresholds for apprehension where identity of aggressor is uncertain;
- conditions for temporary protective separation;
- evidential standards for prosecution under unresolved justification.

No architectural failure identified.

---

## 5. Scenario C — reported theft, no immediate danger

### Facts
A shop reports that participant C removed an item without payment. C has left. The report contains a description and transaction records but no immediate safety threat.

### Lifecycle
**Report -> Triage -> Investigation**

No immediate protective BCA exists merely because theft is alleged.

### Authority boundaries
The report may justify inquiry.

It does not automatically justify:
- forcible entry into C's home;
- unrestricted access to C's financial information;
- detention;
- broad search of unrelated information.

A later search or evidence request requires its own lawful basis and scope.

### Result
PASS.

This scenario confirms that the lifecycle does not convert ordinary investigation into emergency authority.

It also confirms the value of CIBB-style bounded evidence projections where only limited transaction information is legitimately required.

---

## 6. Scenario D — mistaken identity

### Facts
Reliable information available at time T1 reasonably identifies D as the person involved in a serious offence. Police apprehend D within the lawful threshold assumed for the test. At T2, new evidence conclusively establishes that D was elsewhere and cannot be the offender.

### Lifecycle
At T1:

**Reasonable Evidence + Legally Sufficient Apprehension Threshold -> Bounded Apprehension Authority**

At T2:

**Exculpatory Evidence -> Original Function No Longer Supports Continued Control -> Authority Contracts/Sunsets -> Release**

### Dual review
D's innocence does not automatically make the T1 apprehension unlawful.

But the T1 apprehension must still be independently testable against the information reasonably available then.

Continuing detention after T2 without another basis would fail.

### System review
If the mistaken identification resulted from a defective identification system, biased data process, recurring false match or avoidable procedural failure:

**Officer Conduct May Be Lawful + System Failure May Exist**

### Result
PASS.

This is a strong demonstration of why event outcome cannot retrospectively substitute for contemporaneous BCA review.

---

## 7. Scenario E — domestic danger with unclear offence

### Facts
A participant reports shouting and sounds suggesting violence inside a protected home. On arrival, police hear an apparent immediate struggle and a call for help.

### Lifecycle
**Report -> Triage -> Immediate Protective BCA**

A sufficiently serious immediate threat may justify emergency entry under future Law.

### Authority boundaries
Emergency entry is for the protective function.

It does not automatically create authority to conduct an unrelated general search of the home.

After the immediate danger is resolved:

**Emergency Entry Authority -> Contracts/Sunsets**

A continuing investigation may exist, but searches, seizure/access and detention require their own bases.

### Result
PASS.

The lifecycle handles protected-space intrusion without converting emergency access into general police possession of the space.

---

## 8. Scenario F — lawful apprehension followed by excessive force

### Facts
F is lawfully apprehended under the assumed legal threshold. F complies and no longer presents a threat. An officer then deliberately uses unnecessary harmful force.

### Participant classification
The legality of F's original conduct remains independently determined.

### Police classification
The apprehension may be lawful.

The officer's later force is separately tested:

**Apprehension BCA + No Continuing Need For Harmful Force -> Force Outside Envelope -> Unlawful Interference**

A lawful apprehension does not legalise every act performed during it.

### Review
The participant case and officer-conduct case may proceed separately.

Independent review is indicated because the institution's own consequential conduct is in question.

### Result
PASS.

The lifecycle correctly segments one police encounter into lawful and unlawful phases.

---

## 9. Scenario G — unlawful participant conduct plus unlawful police search

### Facts
G actually committed an offence. Police have sufficient grounds to investigate but search a protected information space without the separate authority required for that search. The search discovers incriminating evidence.

### Classification
G's underlying conduct may be unlawful.

The police search may independently be unlawful.

Therefore:

**Participant Unlawfulness != Police Lawfulness**

### Unresolved downstream question
The current architecture deliberately does not answer what should happen to evidence obtained through unlawful authority.

Possible questions for Law/Judiciary include:
- exclusion;
- admissibility with remedy;
- independent-source doctrine;
- inevitable discovery;
- seriousness of authority breach;
- deterrence/system-correction requirements;
- protection of third-party information.

### Result
PARTIAL PASS / IDENTIFIED LAW GAP.

The architecture correctly detects both wrongs but does not yet specify the evidential consequence of unlawful evidence acquisition.

This is a legitimate Law/Judiciary development gap, not a lifecycle failure.

---

## 10. Scenario H — reasonable but mistaken self-defence

### Facts
H perceives circumstances as an imminent attack and causes harm in response. Later evidence establishes that no actual attack was intended. H's perception had some objective support but the full justification test is not satisfied under the assumed rule.

### Classification
The architecture separates:

**Actual Valid BCA -> Justification**

from:

**No Sufficient Actual BCA + Reasonable/Partially Reasonable Perception -> Possible Defence Or Mitigation**

The act need not be falsely classified as fully justified merely to recognise the circumstances.

### Result
PASS / LAW THRESHOLD OPEN.

The legal grammar handles the distinction, but future Law must determine when reasonable mistake produces:
- complete defence;
- partial defence;
- mitigation only;
- no mitigation.

---

## 11. Scenario I — police rely on defective system alert

### Facts
An automated system produces a high-confidence alert identifying I as an immediate threat. Officers reasonably rely on the alert and take bounded protective action. Later review establishes that the alert was generated by a defective model and no threat existed.

### Individual police review
The officers' conduct must be assessed against what they reasonably knew and whether their reliance itself was reasonable.

### System review
Independently:

**No Officer Misconduct != No System Failure**

The alert architecture, validation, deployment, confidence presentation, escalation rules and prior error history require review.

### Authority boundary
The system's confidence score is evidence input, not authority.

**System Alert != Authority**

**Model Confidence != Legal Threshold**

### Result
PASS, with important system-governance implication.

BCA must be activated through legally recognised context/thresholds; automated systems cannot manufacture authority merely by outputting a classification.

---

## 12. Scenario J — participant complaint against police handled internally

### Facts
J alleges that police exceeded search authority. The same operational unit reviews its own conduct and reports that the search was lawful, without external access to the underlying authority record.

### Result
FAIL under Concord architecture.

The internal review may be useful but cannot provide sufficient final accountability where the unit's own authority is materially contested.

**Self-Investigation != Sufficient Final Accountability**

Independent review requires legitimate access to enough protected provenance to reconstruct:
- authority source;
- information known;
- scope;
- actions;
- timing;
- sunset;
- later record changes.

This scenario validates the need for the Dual Review architecture.

---

## 13. Cross-scenario findings

### Finding 1 — State transitions survive
The lifecycle successfully represents incidents that:
- stop at investigation;
- activate emergency intervention;
- proceed to apprehension;
- require authority contraction;
- expose unlawful police conduct;
- expose system failure.

### Finding 2 — BCA non-propagation is essential
Every tested scenario becomes less safe if authority automatically propagates.

Particularly important:

**Emergency Entry != General Search**

**Investigation != Apprehension**

**Apprehension != Continued Detention**

**Apprehension != General Search**

### Finding 3 — Dual review is not optional
Several scenarios cannot be correctly classified if review asks only whether the suspect committed an offence.

### Finding 4 — contemporaneous reasonableness and actual lawfulness must remain distinguishable
Mistaken identity, mistaken self-defence and defective system alerts all require evaluation of:
- actual context;
- information reasonably available at the time;
- quality of the actor's reasoning/reliance;
- later-discovered facts.

### Finding 5 — system responsibility is a separate axis
The architecture correctly permits:
- lawful actor + failed system;
- unlawful actor + sound system;
- unlawful actor + failed system;
- lawful actor + sound system.

### Finding 6 — evidence consequence is the first substantial unresolved downstream gap
The architecture can identify an unlawful search but does not yet determine the consequence for evidence obtained through it.

That question belongs principally to Law/Judiciary.

### Finding 7 — prosecution architecture remains intentionally unresolved
The lifecycle can hand off to prosecution, but prosecutor independence, evidential threshold, disclosure obligations, authority review and decision provenance require dedicated development.

---

## 14. New candidate invariants from testing

PLC-24 System Alert != Authority.  
PLC-25 Model Confidence != Legal Threshold.  
PLC-26 Later Exoneration != Automatic Proof Of Earlier Authority Abuse.  
PLC-27 Earlier Reasonable Authority != Permission To Ignore Later Exculpatory Evidence.  
PLC-28 Lawful Apprehension != Lawful Force Throughout Encounter.  
PLC-29 Evidence Of Offence != Lawful Method Of Evidence Acquisition.  
PLC-30 Internal Institutional Finding != Independent Adjudication.  
PLC-31 Actual Context != Reasonably Perceived Context.  
PLC-32 Actor Error != Necessarily System Error.  
PLC-33 System Error != Necessarily Actor Misconduct.

---

## 15. Test conclusion

**Overall result: PASS WITH IDENTIFIED DOWNSTREAM LAW GAPS.**

No tested scenario requires abandonment of the bounded-authority lifecycle.

The strongest result is that the same architecture handles participant conduct and institutional conduct without creating a privileged legal grammar for the state.

The test identifies three immediate development targets:

1. **evidential consequences of unlawful evidence acquisition;**
2. **reasonable mistake / perceived justification doctrine;**
3. **independent prosecution architecture and referral threshold.**

These should be developed without changing the lifecycle unless later testing reveals a structural failure.
