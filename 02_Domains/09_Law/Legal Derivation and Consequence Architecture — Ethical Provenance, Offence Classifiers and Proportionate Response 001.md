# Legal Derivation and Consequence Architecture — Ethical Provenance, Offence Classifiers and Proportionate Response 001

**Project:** The Concord Framework  
**Domain:** Law  
**Date:** 7 October 2026  
**Status:** ACTIVE DEVELOPMENT / CANDIDATE GENERAL LEGAL ARCHITECTURE / NON-CANONICAL  
**Parent architecture:** `Concord Legal Classification Grammar — Illegality, Lawfulness, Justification and Mitigation 001.md`

---

## 1. Purpose

The existing Concord Legal Classification Grammar establishes the sequence:

**Ethical Kernel → Rights / Protected Relations → Legal Prohibition → Act → Justification → Lawful / Unlawful → Culpability → Mitigation / Aggravation → Consequence / Remedy**

This document extends that grammar into a candidate method for deriving compact ordinary law from the Ethical Kernel without creating a catalogue of every physical mechanism or factual permutation.

The central design proposition is:

> **Law Should Be Traceable Upstream To The Ethical Interest That Justifies It.**

and:

> **Factual Variation Should Normally Be Represented By Classifiers Rather Than By Proliferating Near-Duplicate Base Offences.**

---

## 2. Mandatory ethical provenance

Every Concord law should identify the ethical source from which its protected legal interest is derived.

Candidate provenance chain:

**Blainey's Law(s)**  
→ **Protected Ethical Condition**  
→ **Right / Duty / Immunity / Standing / Stewardship / Authority Constraint**  
→ **Protected Legal Interest**  
→ **Legal Boundary / Prohibition / Requirement**  
→ **Offence Or Other Legal Rule**

A legal rule should therefore carry, where applicable:

- Law ID;
- title;
- ethical source(s);
- derived protected interest;
- rights/duties/constraints engaged;
- prohibited or required state;
- legal elements;
- recognised contextual/consent/authority tests;
- available defences/justifications;
- applicable classifiers;
- remedies;
- available sanction classes;
- review dependencies.

> **Every Concord Law Must Carry Ethical Provenance.**

A rule whose ethical derivation cannot be demonstrated should be subject to review rather than gaining legitimacy merely through historical enactment.

> **Legal Existence != Ethical Legitimacy.**

> **Loss Of Ethical Derivability Is Grounds For Review Of The Law.**

This does not mean every law must derive from one Ethical Kernel principle in isolation. Compound laws may identify multiple upstream roots.

---

## 3. Compact law rather than mechanism enumeration

The fundamental offence should normally protect an interest rather than enumerate every mechanism capable of violating it.

For example, a physical-harm law should not require separate foundational offences for:
- shooting;
- stabbing;
- striking;
- burning;
- poisoning;
- electrocution;
- crushing;
- radiation;
- machinery;
- novel future mechanisms.

The relevant question is primarily:

> **What protected interest was interfered with, with what result, intention, context and responsibility?**

Therefore:

> **Mechanism Does Not Define The Protected Interest Or Fundamental Offence.**

However:

> **Mechanism May Be Evidence Relevant To Intent, Foreseeability, Capability, Preparation, Proportionality And Expected Harm.**

This preserves factual relevance without making law technologically brittle.

---

## 4. Base offence and classifiers

A candidate offence representation is:

**Base Offence**  
+ **Completion State**  
+ **Actual Result**  
+ **Intended Result**  
+ **Culpability / Mental State**  
+ **Participation State**  
+ **Context / Authority State**  
+ **Capacity / Authorship State**  
+ **Aggravating Factors**  
+ **Mitigating Factors**

The base offence remains compact.

Classifiers represent material factual variation.

Example:

**Unlawful Physical Harm**  
- Completion: COMPLETED  
- Actual Harm: H3  
- Intended Harm: H3  
- Mental State: DELIBERATE  
- Participation: PRINCIPAL  
- Capacity: SUFFICIENT  
- Aggravation: PREMEDITATED  
- Mitigation: NONE ESTABLISHED

A different event can use the same base law without creating another offence:

**Unlawful Physical Harm**  
- Completion: COMPLETED  
- Actual Harm: H3  
- Mental State: RECKLESS  
- Participation: PRINCIPAL

---

## 5. Completion and attempt

Attempt should normally be represented as a reusable completion classifier where the relevant base offence permits attempt liability.

Candidate progression:

**Thought / Desire**  
→ **Intention**  
→ **Preparation**  
→ **Executory Attempt**  
→ **Completion**

Important boundaries:

> **Thought != Crime.**

> **Intent Without Executory Action != Attempt.**

> **Preparation != Necessarily Attempt.**

A future legal test must define when conduct has crossed from preparation into sufficiently direct execution of a prohibited result.

Each base law should declare whether attempt is:
- applicable;
- inapplicable;
- or conditional.

Candidate field:

**Attempt Liability: YES / NO / CONDITIONAL**

Examples likely capable of attempt classification include unlawful killing, theft, fraud, kidnapping and deliberate property destruction.

The existence of an attempt classifier does not predetermine the eventual sanction.

---

## 6. Intended result and actual result

Legal classification should preserve both what the actor attempted to cause and what actually occurred.

Example:

A participant deliberately performs an executory act intended to kill another participant. The target survives with serious injury.

Candidate representation:

- Intended Result: DEATH / H5
- Actual Result: H3
- Completion Relative To Intended Offence: ATTEMPTED

Therefore:

> **Intended Result != Actual Result.**

> **Outcome != Complete Measure Of Wrongdoing.**

Likewise:

> **Severe Outcome != Automatic Severe Culpability.**

A catastrophic accidental outcome and an unsuccessful deliberate attempt may require very different responsibility assessments.

---

## 7. Candidate physical-harm bands

A future physical-harm law may use consequence bands independent of mechanism.

Provisional conceptual bands:

### H0 — Attack / prohibited physical interference without established injury
The prohibited physical act or executory attack is established but no resulting physical injury is established.

### H1 — Minor physical harm
Limited injury or impairment with comparatively minor consequence.

### H2 — Significant physical harm
Material injury, substantial pain, treatment requirement or temporary functional impairment.

### H3 — Serious physical harm
Major injury, serious internal injury, prolonged impairment or substantial loss of function.

### H4 — Catastrophic physical harm
Permanent or profound impairment, loss of organ/limb/function, severe irreversible injury or comparable consequence.

### H5 — Death

These are provisional conceptual bands requiring medical/legal calibration.

Visible injury is not required.

> **Visible Damage != Complete Measure Of Physical Harm.**

Internal, neurological, physiological or other objectively supportable harm remains harm even where external marks are absent.

---

## 8. Mental state

The legal system should preserve relevant mental state separately from result.

Candidate categories may include:
- deliberate / intentional;
- knowing;
- reckless;
- negligent;
- non-culpable accidental.

Exact definitions require later development.

The architecture must preserve:

> **Harm != Intent.**

> **Intent != Harm.**

> **Foreseeability != Intention.**

---

## 9. Capacity and authorship

Intent, planning and capacity must remain separate dimensions.

A participant may clearly intend and carefully plan an act while suffering a severe impairment affecting the premises, reality model or authorship from which that intention arose.

Therefore:

> **Planning Competence != Decision Capacity.**

> **Premeditation != Full Capacity.**

> **Intent != Full Authorship.**

Mental illness or diagnosis should not automatically create a legal mitigation.

The relevant chain is:

**Condition / Impairment Evidence**  
→ **Relevant Functional Effect**  
→ **Capacity / Authorship Assessment**  
→ **Responsibility Consequence**

Therefore:

> **Diagnostic Label != Functional State.**

Candidate capacity states may eventually distinguish:
- sufficient relevant capacity;
- impaired but sufficient capacity;
- insufficient relevant capacity for ordinary punitive responsibility.

These states require specialist development and should interface with Health, Judiciary and the existing Mental Health Exceptional Authority architecture.

---

## 10. Aggravation

Aggravating factors identify circumstances that legitimately increase culpability or the justified response without rewriting the base offence.

Candidate factors for later testing include:
- premeditation;
- repeated or continuing offending;
- abuse of entrusted authority;
- deliberate exploitation of known vulnerability;
- multiple affected participants;
- leadership/direction of others;
- concealment or obstruction;
- continuation after justification/authority clearly ended;
- fabricated justification;
- deliberately increased foreseeable danger.

Every aggravating factor requires evidence.

> **Aggravating Label != Assumed Fact.**

Where possible, aggravating factors should themselves identify the protected legal/ethical reason that makes them relevant.

---

## 11. Mitigation

Mitigating factors identify circumstances that reduce culpability or appropriate consequence while leaving the unlawful classification intact.

Potential factors for later testing include:
- materially impaired but sufficient capacity;
- duress insufficient for complete defence;
- reduced foreseeability;
- limited participation;
- genuine mistake insufficient for complete defence;
- voluntary cessation;
- voluntary prevention of further harm;
- assistance to harmed participants;
- voluntary restitution/repair;
- early truthful admission/cooperation;
- relevant developmental/capacity circumstances.

> **Mitigation != Exoneration.**

> **Mitigated != Lawful.**

A circumstance that completely justifies the conduct or defeats responsibility belongs in justification/defence rather than merely mitigation.

---

## 12. Mirrored aggravation and mitigation

Sentencing/consequence reasoning should be structurally required to inspect both directions.

Candidate architecture:

**Established Offence / Responsibility State**  
→ **Aggravation Tree**  
↔ **Mitigation Tree**  
→ **Proportionality Assessment**

The purpose is to prevent consequence reasoning from becoming a one-direction search for reasons to increase punishment.

> **Evidence Increasing Culpability Does Not Erase Evidence Reducing Culpability.**

> **Evidence Reducing Culpability Does Not Erase Established Aggravation.**

Both may be simultaneously true.

Example:

- deliberate intent: established;
- premeditation: established;
- serious mental impairment: established;
- relevant capacity: substantially impaired but not absent.

The legal system should preserve all four facts rather than numerically cancelling them into an information-poor score.

---

## 13. Multidimensional rather than premature scalar scoring

The architecture should not initially reduce factors to a crude arithmetic model such as:

**Premeditation +2; Impairment -2; Net 0.**

Such compression can conceal why the result was reached.

Instead, the adjudicative record should preserve the dimensions and explain how they affect the justified response.

> **Equivalent Numerical Total != Equivalent Legal State.**

Any future quantitative decision support must remain subordinate to inspectable multidimensional reasoning.

---

## 14. Justification, mitigation and aggravation

These must remain distinct.

### Justification / complete defence
The act is lawful in context or responsibility is defeated according to recognised law.

### Mitigation
The conduct remains unlawful and responsibility remains, but culpability or justified consequence is reduced.

### Aggravation
The underlying offence remains, but culpability or justified consequence is increased.

Therefore:

> **Justification != Mitigation.**

> **Mitigation != Aggravation In Reverse.**

They may rely on different facts and legal interests.

---

## 15. Remedy and sanction are separate

A harmed participant's restoration should not be confused with punishment of the responsible participant.

Candidate split:

**Established Harm**  
→ **Restoration / Compensation / Remedy**

and separately:

**Established Culpable Violation**  
→ **Accountability / Sanction**

Therefore:

> **Remedy != Punishment.**

> **Restitution != Automatic Extinguishment Of Responsibility.**

> **Ability To Repair Harm != Right To Commit Harm.**

Voluntary repair may nevertheless be relevant mitigation because it supplies evidence about post-event conduct and reduces outstanding harm.

---

## 16. Protection and punishment are separate

Current dangerousness and retrospective culpability are also different dimensions.

A participant may:
- have greatly diminished culpability but remain dangerous;
- have high culpability but present little continuing danger.

Therefore:

> **Reduced Culpability != Reduced Present Danger.**

> **Present Danger != Retrospective Culpability.**

A protective intervention must derive from present protective need rather than being disguised punishment.

Likewise punishment cannot be extended merely because a participant is considered risky if its punitive justification has ended.

---

## 17. Candidate consequence decomposition

A judicial outcome may therefore need several independent outputs:

### Remedy / restoration
What can legitimately repair or compensate for harm to affected participants?

### Accountability / sanction
What consequence is justified by established culpability?

### Protection
What current bounded intervention is necessary to prevent sufficiently evidenced serious harm?

### Rehabilitation / treatment
What voluntary or legitimately authorised intervention addresses causal conditions or capability deficits?

### Review
What conditions trigger continuation, reduction, modification or termination of each intervention?

This yields:

> **One Offence != One Undifferentiated Punishment Function.**

and:

> **Different Civil Functions Require Different Authority Bases.**

---

## 18. Authority sunset

Each consequence must terminate or be re-justified when the function supporting it ends.

> **Punitive Authority Ends When Its Justification Ends.**

> **Protective Authority Exists Only While The Relevant Protective Need Exists.**

> **Treatment Need != Punitive Authority.**

> **Mental Illness != Authority To Punish.**

> **Danger != Moral Guilt.**

This directly interfaces with Bounded Contextual Authority and State Triggered Review Architecture.

---

## 19. Candidate general derivation chain

The expanded legal derivation architecture is:

**Ethical Kernel**  
→ **Protected Ethical Condition**  
→ **Right / Duty / Standing / Constraint**  
→ **Protected Legal Interest**  
→ **Base Legal Rule / Offence**  
→ **Elements**  
→ **Observed Conduct**  
→ **Actual Result**  
→ **Intended Result**  
→ **Completion State**  
→ **Mental State**  
→ **Participation State**  
→ **Consent / Context / Authority**  
→ **Justification / Defence**  
→ **Capacity / Authorship**  
→ **Responsibility**  
→ **Aggravation ↔ Mitigation**  
→ **Remedy + Sanction + Protection + Rehabilitation**  
→ **Proportionality**  
→ **Review / Sunset**

No downstream stage may silently manufacture authority absent from its upstream justification.

---

## 20. Candidate legal invariants

LDA-01 Every Concord Law Must Carry Ethical Provenance.  
LDA-02 Legal Existence != Ethical Legitimacy.  
LDA-03 Mechanism != Fundamental Offence.  
LDA-04 Mechanism May Be Relevant Evidence.  
LDA-05 Thought != Crime.  
LDA-06 Intent Without Executory Action != Attempt.  
LDA-07 Preparation != Necessarily Attempt.  
LDA-08 Intended Result != Actual Result.  
LDA-09 Outcome != Complete Measure Of Wrongdoing.  
LDA-10 Severe Outcome != Automatic Severe Culpability.  
LDA-11 Harm != Intent.  
LDA-12 Intent != Full Authorship.  
LDA-13 Planning Competence != Decision Capacity.  
LDA-14 Diagnostic Label != Functional State.  
LDA-15 Aggravating Label != Assumed Fact.  
LDA-16 Mitigation != Exoneration.  
LDA-17 Evidence Increasing Culpability Does Not Erase Evidence Reducing Culpability.  
LDA-18 Equivalent Numerical Total != Equivalent Legal State.  
LDA-19 Remedy != Punishment.  
LDA-20 Restitution != Automatic Extinguishment Of Responsibility.  
LDA-21 Reduced Culpability != Reduced Present Danger.  
LDA-22 Present Danger != Retrospective Culpability.  
LDA-23 Treatment Need != Punitive Authority.  
LDA-24 Mental Illness != Authority To Punish.  
LDA-25 Danger != Moral Guilt.  
LDA-26 Different Civil Functions Require Different Authority Bases.  
LDA-27 Each Consequence Requires Its Own Continuing Justification.

---

## 21. Relationship to existing Concord architecture

This architecture extends rather than replaces:
- Blainey's Laws — Ethical Kernel;
- Rights Derivation;
- Concord Legal Classification Grammar;
- Bounded Contextual Authority;
- Self-Defence and Defensive Authority;
- Mistaken Authority and Reasonable Belief;
- Mental Health Exceptional Authority;
- State Triggered Review Architecture;
- Reality Trees / Mirrored Reality Trees;
- Judiciary evidence architecture;
- Health capacity/mental-health interfaces.

The Law domain remains responsible for defining legal elements and available consequences.

Judiciary remains responsible for contested application and adjudication.

Health evidence may inform functional capacity but does not itself determine legal culpability.

---

## 22. Next development step

The architecture should be tested by deriving a small set of foundational offence families directly from the Ethical Kernel and candidate rights.

The first recommended worked derivation is:

**Unlawful Physical Harm**

because it forces simultaneous testing of:
- ethical provenance;
- bodily integrity/self-ownership;
- harm bands;
- attempt;
- intended versus actual result;
- deliberate/reckless/negligent states;
- consent;
- contextual wrappers;
- self-defence;
- capacity;
- aggravation;
- mitigation;
- remedy;
- protection;
- proportionality.

Only after cross-case testing should this candidate architecture be elevated into a general Law-domain method.
