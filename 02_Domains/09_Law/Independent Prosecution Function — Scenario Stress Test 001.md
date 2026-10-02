# Independent Prosecution Function — Scenario Stress Test 001

**Project:** The Concord  
**Domain:** Law / Civil Security / Judiciary  
**Date:** 2 October 2026  
**Status:** ACTIVE DEVELOPMENT / INTERNAL ARCHITECTURE TEST / PROVISIONAL / NON-CANONICAL  
**Architecture under test:** `Independent Prosecution Function — Referral, Threshold and Adjudication Handoff 001.md`

## 1. Test purpose

Test whether the proposed independent prosecution function survives materially different cases without collapsing police investigation, prosecution-threshold assessment and judicial adjudication into one another.

The test asks:

1. Can referral occur without police deciding the prosecution threshold?
2. Can prosecution independently reject or accept the referred hypothesis?
3. Can prosecution request legitimate further investigation without directing police toward a desired conclusion?
4. Does prosecution authority contract when evidence changes?
5. Does threshold satisfaction constrain unexplained non-prosecution discretion?
6. Does exculpatory evidence remain structurally visible?
7. Can legal framing change without prosecution becoming an investigator or court?
8. Can prosecution conduct itself remain independently reviewable?

This is an architecture test. It does not establish final offence-specific evidential thresholds or procedural law.

---

## 2. Expected invariants

The following should survive every scenario:

- Investigation != Prosecution.
- Referral Condition != Prosecution Threshold.
- Police Referral != Police Finding That Prosecution Threshold Is Met.
- Referral Package != Advocacy File.
- Prosecution != Guilt Determination.
- Police Classification != Binding Charge.
- MRT Weight != Prosecution Threshold.
- Threshold Satisfaction -> Ordinary Duty To Proceed Unless Explicit Lawful Exception Applies.
- Past Threshold != Permanent Authority.
- Material Evidence Change -> Threshold Reassessment.
- Prosecution May Identify Evidential Deficit != Prosecution May Dictate Investigative Conclusion.
- Judiciary != Prosecution Confirmation Layer.

---

## 3. Scenario A — strong case clearly above threshold

### Facts

Civil Security investigates a serious prohibited act. Multiple materially independent evidence sources support the same participant-responsibility hypothesis. Material contrary evidence has been actively sought and represented but does not materially undermine the hypothesis. Evidence provenance and authority records are reconstructable.

The legally defined referral condition is reached.

### Police stage

Police transfer the whole evidential state.

They need not certify guilt and need not make the final prosecution-threshold decision.

### Prosecution stage

Intake review finds the package sufficiently reconstructable.

Independent assessment finds the legally established prosecution threshold satisfied.

### Result

**Threshold Met -> Prosecution Authority Activates -> Ordinary Duty To Proceed**

The case is legally framed and handed toward independent adjudication.

### Test result

PASS.

The architecture does not require police guilt determination and does not require prosecution to pretend guilt has already been established.

---

## 4. Scenario B — referral condition met, prosecution threshold not met

### Facts

Police have completed a proportionate investigation. There is meaningful evidence against B, but important contradictions remain and the whole evidential state is not sufficient under the prosecution threshold.

The case is nevertheless sufficiently developed to require independent prosecution assessment under the referral rule.

### Result

The prosecutor independently finds:

**Referral Condition Met + Prosecution Threshold Not Met**

This is not a contradiction.

If a specific material investigative gap remains legitimately resolvable, the case may be returned for bounded further investigation.

If not:

**No Prosecution / Closure Or Reclassification**

### Test result

PASS.

This validates the distinction:

> **Referral Condition != Prosecution Threshold**

Without that distinction, police referral would risk becoming a disguised prosecution decision.

---

## 5. Scenario C — prosecutor requests further investigation

### Facts

The evidence materially depends on whether a timestamp associated with physical evidence is authentic. Police have not yet independently verified it.

### Legitimate prosecution request

> Determine whether the timestamp can be independently authenticated and report the result.

This identifies an evidential deficit without specifying the desired answer.

### Illegitimate prosecution request

> Find evidence proving C was at the scene at that time.

The second request directs investigation toward a preferred conclusion.

### Result

**Prosecution May Identify Evidential Question**

but:

**Prosecution May Not Manufacture Investigative Objective Around Desired Guilt Conclusion**

Civil Security retains responsibility for lawful investigative means and evidential neutrality.

### Test result

PASS.

The boundary between prosecution and investigation remains operational.

---

## 6. Scenario D — strong exculpatory state indicates wrong suspect

### Facts

D was initially the principal suspect. Several early observations supported D's involvement.

Later investigation produces:
- reliable location evidence placing D elsewhere;
- evidence dependencies showing several inculpatory indicators derived from one mistaken source;
- a materially plausible alternative suspect;
- unresolved evidence better explained by the alternative hypothesis.

The referral condition is nevertheless triggered because the case requires independent disposition.

### Prosecution assessment

Prosecution must assess the whole state rather than ask whether some evidence against D still exists.

The correct result may be:

**Current Suspect Hypothesis Materially Fails -> Threshold Not Met For D**

The case may return for legitimate investigation of the expanded hypothesis space.

### Boundary

Prosecution does not choose the replacement suspect.

It identifies that the referred prosecution hypothesis is unsupported.

### Test result

PASS.

MRT/whole-state evidence prevents referral from converting a historical suspect choice into prosecution momentum.

---

## 7. Scenario E — threshold initially met, key witness later recants

### Facts

At initiation, independent evidence plus a credible witness satisfies the prosecution threshold.

Before adjudication, the witness materially recants. The remaining evidence alone may no longer be sufficient.

### Required response

The original decision is not retrospectively unlawful merely because the evidence later changes.

But:

**Material Evidence Change -> Threshold Reassessment**

If the threshold remains satisfied on the whole state, prosecution may continue.

If it no longer does:

**Threshold Collapse -> Prosecution Authority Contracts / Terminates**

### Failure mode rejected

**Case Already Started -> Must Finish**

is incompatible with BCA functional sunset.

### Test result

PASS.

The prosecution function behaves as continuing authority rather than institutional ownership of a case.

---

## 8. Scenario F — prosecutor personally doubts guilt despite threshold satisfaction

### Facts

The whole evidential state independently satisfies the legally established prosecution threshold. The assigned prosecutor nevertheless has a personal intuition that the accused may be innocent, but cannot identify material evidence or a lawful exception supporting that intuition.

### Result

Personal belief does not override the threshold architecture.

**Personal Prosecutorial Belief != Lawful Exception**

The ordinary duty is to proceed.

The prosecutor remains responsible for preserving contrary evidence and presenting the case fairly. Judiciary determines the contested outcome.

### Important qualification

If the prosecutor's concern identifies an articulable evidential problem, omitted hypothesis, conflict, legal defect or other material factor, that factor must enter the evidential/legal assessment.

The architecture suppresses unexplained discretion, not reasoned correction.

### Test result

PASS.

Automaticity is bounded by Law rather than personality.

---

## 9. Scenario G — threshold appears met only because evidence dependencies were hidden

### Facts

Five apparently corroborating digital indicators support G.

During prosecution intake review, it is discovered that all five derive from the same underlying sensor/model output.

Treated independently, the evidence appeared sufficient. Correctly dependency-adjusted, the threshold is no longer clearly satisfied.

### Result

Intake integrity review exposes the defect.

**Five Derivatives != Five Independent Foundations**

The case is reassessed using the true evidential structure.

Possible outcomes:
- threshold not met;
- bounded further investigation;
- another independent source restores sufficiency.

### Test result

PASS.

The prosecution function provides an independent structural check rather than merely recounting police evidence.

---

## 10. Scenario H — police legal classification is too severe

### Facts

Police evidence accurately establishes H's conduct, but the referred legal classification includes an aggravated form requiring an element the evidence does not support.

A lesser legal classification is supported.

### Result

Prosecution is not bound by the police classification.

**Police Classification != Binding Charge**

The unsupported aggravated allegation is not carried forward merely because police used that label.

Prosecution may frame the supported allegation under applicable Law.

### Boundary

This is legal framing of established evidence, not authority to invent additional facts.

### Test result

PASS.

The prosecution function has a real legal role without becoming a fact-finding court.

---

## 11. Scenario I — clear complete justification

### Facts

Evidence establishes that I caused the physical harm alleged. The same whole evidential state clearly establishes a complete lawful justification under the applicable defensive-authority rule.

### Result

The physical act alone does not create a prosecution duty.

**Prohibited-Act Evidence + Clearly Established Complete Justification -> No Sufficient Prosecution Basis For The Justified Harm**

Where justification is materially contested, adjudication may still be warranted if the prosecution threshold is met.

### Test result

PASS.

The architecture tests the legally relevant whole case rather than raw act occurrence.

---

## 12. Scenario J — prosecution wants to rescue a weak case

### Facts

The prosecution threshold is not met. No specific unresolved evidential question is identified. A prosecutor repeatedly returns the file to police with broad instructions to "develop the case further."

### Result

FAILURE if permitted.

A weak prosecution hypothesis does not create indefinite authority to search for a prosecutable case.

A return for investigation requires a legitimate continuing investigative function and an articulable material question.

**Threshold Failure != Authority For Indefinite Case-Building**

Where no legitimate investigative route remains:

**No Prosecution / Closure Or Reclassification**

### Test result

PASS — architecture rejects the attempted behaviour.

### New clarification exposed

The prosecution architecture should explicitly prevent repetitive return loops from becoming a substitute for threshold satisfaction.

---

## 13. Scenario K — prosecutor declines despite threshold because of explicit lawful exception

### Facts

The threshold is satisfied, but Law contains a specific non-prosecution exception applicable to the case.

The exception has an identified purpose, bounded criteria, recorded reasons and independent review route.

### Result

The exception may lawfully prevent ordinary prosecution if its own conditions are satisfied.

This does not contradict automaticity because:

**Threshold Satisfaction -> Ordinary Duty To Proceed Unless Explicit Lawful Exception Applies**

### Review requirement

The exception decision itself is an exercise of public authority and must be reconstructable and reviewable.

### Test result

PASS.

The architecture permits bounded legal exceptions without restoring unstructured discretion.

---

## 14. Scenario L — hidden exculpatory evidence

### Facts

A prosecutor knows of reliable evidence materially undermining the prosecution hypothesis but omits it from the case state because disclosure would make conviction less likely.

### Result

FAILURE under the architecture.

**Prosecution != Suppression Of Contrary Evidence**

The prosecution function exists to support lawful adjudication, not conviction optimisation.

The omission also becomes an independent object of authority/accountability review.

### Test result

PASS — architecture identifies the conduct as incompatible with the function.

---

## 15. Scenario M — acquittal after proper prosecution

### Facts

The threshold was legitimately satisfied when prosecution began and remained satisfied. Evidence was fairly represented. Judiciary nevertheless finds the final adjudicative threshold unmet.

### Result

**Acquittal != Automatic Prosecution Failure**

The prosecution threshold and adjudicative threshold are deliberately distinct.

The acquittal may still contribute to later empirical calibration, but it does not retrospectively invalidate the prosecution merely because the final threshold was not met.

### Test result

PASS.

---

## 16. Scenario N — conviction after improper prosecution conduct

### Facts

The accused actually committed the offence and Judiciary reaches a lawful finding on independently sufficient evidence. During prosecution, however, a prosecutor concealed material evidence or exceeded another authority boundary.

### Result

**Conviction != Automatic Proof Of Proper Prosecution Conduct**

The participant's conduct and prosecution conduct remain independently reviewable.

The consequences of the prosecution violation for the judicial result depend upon future procedural/remedial Law and are not invented here.

### Test result

PASS / IDENTIFIED PROCEDURAL-REMEDY INTERFACE.

---

## 17. Scenario O — multiple plausible participants

### Facts

Evidence strongly establishes that one of two participants committed the prohibited act, but the current evidence does not sufficiently discriminate between them.

### Result

The prosecution function must not manufacture certainty merely because the event itself is well evidenced.

Possible state:

**Offence Strongly Established + Individual Attribution Insufficient**

If the prosecution threshold for either individual is not met, neither is prosecuted merely to force Judiciary to determine which one did it.

Further legitimate investigation may continue if a material route exists.

### Test result

PASS.

This confirms that event certainty and participant attribution are separate evidential propositions.

---

## 18. Scenario P — serious allegation creates institutional pressure

### Facts

A highly serious alleged offence receives intense public attention. Evidence remains below the ordinary legally established prosecution threshold.

### Result

**Serious Allegation != Lower Evidential Requirement**

Public or institutional pressure does not create evidential sufficiency.

Urgency may justify faster lawful processing, preservation or review, but:

**Urgency != Proof**

### Test result

PASS.

---

## 19. Cross-scenario findings

### Finding 1 — referral/threshold separation is essential

Scenario B confirms that the prosecution function needs a case-entry condition that does not require police to make the prosecution decision first.

### Finding 2 — prosecution independence is bidirectional

Independence means prosecution can reject a police case that does not satisfy the threshold.

It also means police do not become subordinate case-builders tasked with producing the prosecutor's preferred conclusion.

### Finding 3 — automaticity survives

Scenario F and K show that automaticity can be expressed as:

**Threshold Met -> Duty To Proceed**

subject to:

**Explicit Lawful Exception -> Separately Bounded And Reviewable Authority**

This removes unexplained personal discretion without pretending no exceptional legal context can ever exist.

### Finding 4 — functional sunset survives

Scenario E confirms prosecution authority can disappear after lawful activation.

### Finding 5 — whole-state evidence is structurally necessary

Scenarios D, G, I and O fail under a one-sided prosecution file but remain representable under the whole-evidential-state architecture.

### Finding 6 — prosecution is not an advocacy-only function

Its public function is not "obtain conviction."

It is to place a sufficiently evidenced, legally framed contested matter before independent adjudication while preserving evidential integrity.

### Finding 7 — repetitive return is a newly exposed boundary

The architecture needs an explicit rule preventing repeated "further investigation" referrals from becoming indefinite case-building after threshold failure.

### Finding 8 — procedural/remedial Law remains separate

The architecture can identify prosecution misconduct without yet deciding whether that misconduct requires:
- retrial;
- exclusion;
- dismissal;
- independent remedy;
- officer/prosecutor accountability;
- another procedural response.

That is a genuine downstream Law/Judiciary interface.

---

## 20. New candidate invariants

IPF-25 Threshold Failure != Authority For Indefinite Case-Building.  
IPF-26 Return For Further Investigation Requires An Articulable Material Evidential Question And Continuing Legitimate Investigative Function.  
IPF-27 Repeated Referral Does Not Manufacture Prosecution Sufficiency.  
IPF-28 Event Evidential Sufficiency != Individual Attribution Sufficiency.  
IPF-29 Personal Prosecutorial Belief != Lawful Exception.  
IPF-30 Explicit Non-Prosecution Exception Requires Its Own Bounded And Reviewable Authority.  
IPF-31 Prosecution Independence != Investigative Command Authority.  
IPF-32 Prosecution Quality != Conviction Maximisation.

---

## 21. Test conclusion

**OVERALL RESULT: PASS WITH ONE NARROW ARCHITECTURAL CLARIFICATION AND DOWNSTREAM PROCEDURAL GAPS.**

No scenario requires abandonment or restructuring of the independent prosecution function.

The principal newly exposed clarification is:

> **A return for further investigation must not become an indefinite loop for rescuing a prosecution hypothesis that does not satisfy the threshold.**

The architecture should therefore add a bounded-return rule requiring:
1. an articulable material evidential question;
2. a continuing legitimate investigative function;
3. no direction toward a predetermined factual conclusion;
4. recorded provenance for the return;
5. reassessment after the requested question is resolved;
6. closure/reclassification where no legitimate investigative route remains.

Downstream work remains necessary for procedural remedies, detailed disclosure, defence/representation interface and exceptional non-prosecution grounds, but these are not failures of the core prosecution lifecycle.
