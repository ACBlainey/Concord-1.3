# Prosecution Threshold and Evidential Sufficiency — Initial Architecture 001

**Project:** The Concord  
**Domain:** Law / Civil Security / Judiciary  
**Date:** 2 October 2026  
**Status:** ACTIVE DEVELOPMENT / CANDIDATE PROSECUTION ARCHITECTURE / PROVISIONAL / NON-CANONICAL

## 1. Purpose

This note develops the third downstream gap identified by the initial Policing Lifecycle stress test: the transition from investigation to prosecution.

The central principle is:

> **Prosecution is justified by sufficient evidence to require independent adjudication, not by a police determination that the participant is guilty.**

Police investigate. Evidence is assessed against a legally defined prosecution threshold. Judiciary determines contested guilt, liability, justification and other adjudicative questions.

## 2. Core separations

**Complaint != Prosecution Threshold**

**Suspicion != Prosecution Threshold**

**Police Belief != Prosecution Threshold**

**Police Belief != Guilt**

**Prosecution != Guilt**

**Prosecution Threshold != Final Adjudicative Threshold**

A complaint or suspicion may justify attention or investigation without justifying prosecution.

## 3. Evidential trigger

Prosecution should ordinarily follow when the legally established evidential threshold is satisfied, subject only to separately defined legitimate exceptions.

This avoids giving investigators an informal power to decide guilt or to suppress sufficiently evidenced cases through personal preference.

Candidate chain:

**Investigation -> Complete Reasonably Available Evidential State -> Evidential Sufficiency Assessment -> Threshold Met -> Prosecution Trigger**

If the threshold is not met:

**Threshold Not Met -> Continue Legitimate Investigation Where Function Remains OR Close / Reclassify**

The exact threshold is not fixed in this document.

## 4. Whole evidential state

The prosecution assessment must consider materially relevant evidence in all directions.

**Whole Evidential State = Inculpatory Evidence + Exculpatory Evidence + Contradictory Evidence + Unresolved Evidence + Relevant Provenance / Reliability State**

Therefore:

**Prosecution File != Inculpatory Evidence Only**

Known evidence tending materially against prosecution cannot be ignored merely because other evidence supports prosecution.

**Evidence Supporting Prosecution != Permission To Conceal Contrary Evidence**

## 5. Evidence quality and quantity

Evidence should not be reduced to a simple count.

Relevant dimensions may include:
- directness;
- independence;
- reliability;
- authenticity;
- integrity;
- provenance;
- corroboration;
- contradiction;
- specificity;
- temporal relevance;
- forensic strength;
- opportunity to observe;
- source incentives or reliability concerns;
- material evidential gaps.

Therefore:

**Evidence Quantity != Evidence Quality**

and:

**Multiple Reports != Multiple Independent Sources**

Several weak or derivative items do not automatically become strong merely through number.

Conversely, one exceptionally strong and reliable item may sometimes be sufficient.

## 6. First-hand witness evidence

Credible first-hand eyewitness evidence may be sufficient to cross a prosecution threshold depending upon context and applicable Law.

This includes an officer who directly witnesses relevant conduct.

But:

**Officer Witness != Automatic Truth**

Officer testimony remains evidence subject to the same relevant assessment of observation, reliability, consistency, provenance, contradiction and corroboration as other evidence.

Likewise:

**Non-Officer Witness != Automatically Lower Evidential Value**

Status does not replace evidential assessment.

## 7. Recanted or withdrawn evidence

The prosecution threshold is dynamic.

If a witness whose evidence materially supported the threshold recants, withdraws, materially changes or is shown unreliable, the evidential state must be recalculated.

**Material Evidence Change -> Threshold Reassessment**

If the withdrawn evidence was the only basis sufficient to support prosecution:

**Threshold No Longer Met -> Prosecution Authority Must Be Reconsidered**

A recantation does not automatically prove the original statement false. The original statement, recantation, reasons, corroboration and surrounding evidence remain subject to evidential assessment.

## 8. Circumstantial evidence

Circumstantial evidence is not inherently inferior to direct evidence.

Several individually insufficient facts may collectively create a strong evidential case where they are materially independent and mutually reinforcing.

Example form:

**Opportunity + Location + Relevant Possession + Independent Digital/Physical Evidence + Consistent Timeline -> Potential Collective Sufficiency**

But:

**Five Derivative Indicators From One Underlying Source != Five Independent Evidential Foundations**

The threshold must assess evidential structure, not merely volume.

## 9. Contrary evidence

Contrary evidence must be weighed as part of the same threshold assessment.

Example:

**Credible Identification Of Suspect**
may support prosecution.

But:

**Identification + Multiple Independent Credible Alibi Witnesses + Reliable CCTV Showing Suspect Elsewhere**
may materially reduce or eliminate the evidential basis.

No individual item is mechanically decisive. The question is whether the complete evidential state remains sufficient.

## 10. Dynamic prosecution authority

Prosecution is itself a bounded function.

Its authority depends upon the continuing existence of the conditions that justify it.

Therefore:

**Past Prosecution Threshold != Permanent Prosecution Authority**

**Material Evidential Change -> Reassess Continuing Prosecution Basis**

If the evidential foundation materially collapses, prosecution should not continue merely because it was once legitimately initiated.

This is BCA functional sunset applied to prosecution.

## 11. Historical and expert calibration

The exact prosecution threshold should not be invented abstractly by this development note.

It should eventually be informed by:
- legal expertise;
- judicial interpretation;
- evidential science;
- accumulated case outcomes;
- comparable historical cases;
- known failure modes;
- changes in forensic capability;
- changes in Law.

Historical case performance can provide calibration evidence.

For example:

**Materially Comparable Evidence Profiles Repeatedly Fail To Sustain Required Adjudicative Findings -> Evidence Threshold May Require Recalibration**

But:

**Past Failure != Automatic Present Failure**

A current case may differ materially in evidence quality, corroboration, Law, technology or context.

Historical evidence informs the threshold; it does not decide the present case.

## 12. Independent prosecution function

The prosecution function should not simply inherit the police conclusion.

Police provide the investigation/evidential state.

The prosecution function independently determines whether the legally established prosecution threshold is satisfied.

**Police Referral != Prosecutorial Obligation Unless Threshold Is Independently Satisfied**

**Police Classification != Prosecutorial Finding**

**Prosecution Function != Police Confirmation Layer**

The exact institutional form, appointment structure and independence safeguards remain to be developed.

## 13. Automaticity and bounded exceptions

Candidate principle:

> **Where the prosecution threshold is independently satisfied, prosecution should ordinarily proceed automatically rather than depend upon discretionary police belief about guilt or innocence.**

Any future exception to proceeding despite a satisfied threshold should:
- have an explicit lawful basis;
- identify the legitimate function;
- remain bounded;
- preserve reasons/provenance;
- be independently reviewable;
- not become informal unrecorded discretion.

**Discretion != Unrecorded Permission To Ignore Threshold**

## 14. Relationship to justification and defence

Evidence sufficient to establish the prohibited-act elements is not necessarily sufficient to prosecute if the complete evidential state clearly establishes a complete lawful justification.

Example:

**Physical Harm Established + Clear Self-Defence Established -> No Sufficient Basis For Prosecution Of Justified Harm**

Where the justification remains materially contested:

**Prohibited Act Evidence + Materially Unresolved Defence -> Prosecution May Be Appropriate If Threshold Is Met -> Judiciary Resolves Contest**

The prosecution function does not determine final guilt merely by deciding that adjudication is warranted.

## 15. Relationship to unlawfully obtained evidence

Evidence remains assessed under:

`Unlawfully Obtained Evidence — Evidential Continuity and Independent Accountability 001.md`

Unlawful acquisition does not automatically erase evidence.

The evidence enters the evidential state on its evidential merits while the acquisition violation follows its independent accountability track.

## 16. Decision provenance

A prosecution-threshold assessment should preserve enough provenance to reconstruct:
- material supporting evidence;
- material contrary/exculpatory evidence;
- reliability/provenance concerns;
- material unresolved questions;
- threshold standard applied;
- decision;
- material later changes;
- reassessments;
- reason for continuation or termination.

This supports audit without converting every case into universal public disclosure.

## 17. Candidate invariants

PTE-01 Complaint != Prosecution Threshold.  
PTE-02 Suspicion != Prosecution Threshold.  
PTE-03 Police Belief != Prosecution Threshold.  
PTE-04 Police Belief != Guilt.  
PTE-05 Prosecution != Guilt.  
PTE-06 Prosecution Threshold != Final Adjudicative Threshold.  
PTE-07 Evidence Quantity != Evidence Quality.  
PTE-08 Multiple Reports != Multiple Independent Sources.  
PTE-09 Officer Witness != Automatic Truth.  
PTE-10 Prosecution File != Inculpatory Evidence Only.  
PTE-11 Material Evidence Change -> Threshold Reassessment.  
PTE-12 Past Prosecution Threshold != Permanent Prosecution Authority.  
PTE-13 Past Failure != Automatic Present Failure.  
PTE-14 Police Classification != Prosecutorial Finding.  
PTE-15 Prosecution Function != Police Confirmation Layer.  
PTE-16 Historical Evidence Informs Threshold != Historical Evidence Decides Case.  
PTE-17 Known Contrary Evidence Must Remain In The Evidential State.  
PTE-18 Evidential Sufficiency Must Be Assessed As A Whole Rather Than By Raw Count.  
PTE-19 Threshold Satisfaction Creates A Presumption To Proceed Subject Only To Explicit Legitimate Exceptions.  
PTE-20 Material Collapse Of Threshold Evidence Requires Reassessment Of Continuing Prosecution Authority.

## 18. Provisional architecture

**Complaint / Observation / Suspicion**  
-> **Investigation**  
-> **Evidence Collection**  
-> **Whole Evidential State**  
-> **Independent Evidential Sufficiency Assessment**

If insufficient:

**Continue Legitimate Investigation OR Close**

If sufficient:

**Prosecution Trigger -> Independent Prosecution Function**

Then continuously:

**Material Evidence Change -> Threshold Reassessment**

Where the threshold continues:

**Prosecution -> Independent Judiciary**

Where it no longer does:

**Prosecution Authority Contracts / Terminates As Law Requires**

The final guilt determination remains with Judiciary.

## 19. Resolution

The prosecution-interface gap is provisionally resolved at architectural level.

The Concord need not presently invent a numerical universal evidence threshold.

It requires instead:
1. a legally established sufficiency threshold;
2. whole-state evidential assessment;
3. independent prosecution assessment rather than police guilt determination;
4. ordinary prosecution when the threshold is met;
5. continuing reassessment when evidence materially changes;
6. expert, judicial and empirical calibration of the threshold over time;
7. explicit and reviewable treatment of any future exceptions.

In compact form:

> **Police establish the evidential state. Prosecution tests whether that state justifies adjudication. Judiciary determines the contested legal outcome.**
