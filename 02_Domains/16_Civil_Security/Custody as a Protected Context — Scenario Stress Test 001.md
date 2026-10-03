# Custody as a Protected Context — Scenario Stress Test 001

**Project:** The Concord
**Domain:** Civil Security / Law / Judiciary
**Date:** 3 October 2026
**Status:** ACTIVE DEVELOPMENT / CUSTODY STRESS TEST / PROVISIONAL / NON-CANONICAL

## 1. Test purpose

This test examines **Custody as a Protected Context — Rights Restriction, Review and Post-Release Remedy 001** against cases involving:

- lawful short custody;
- prolonged custody ending without prosecution;
- wrongful custody;
- excessive restrictions within otherwise lawful custody;
- defective-system repetition;
- incomplete restoration after physical release;
- no-fault civil burden;
- participant-caused delay;
- custody followed by prosecution;
- compensation incentives;
- differentiated custodial restrictions;
- continuing review.

The test asks separately:

1. Was custody lawfully activated?
2. Was continuing custody lawfully justified?
3. Were restrictions inside custody independently justified?
4. Was the participant adequately protected while the Concord exercised control?
5. Was release timely?
6. Was ordinary status actually restored?
7. Did custody create material harm or loss?
8. Does that harm warrant remedy even without misconduct?
9. Does the event expose individual or systemic failure?

---

## 2. Scenario A — short lawful custody, rapid exculpation

A participant is lawfully apprehended after being reasonably but mistakenly identified near a violent incident. Custody is justified briefly while identity and immediate evidence are checked. CCTV quickly establishes that the participant was not involved. They are released after two hours.

They miss a work shift and incur travel disruption.

### Analysis

Initial custody may have been lawful.

Once exculpatory evidence resolves the relevant uncertainty, continuing detention authority sunsets.

The participant nevertheless lost liberty and incurred measurable consequences for a civil protective function.

The architecture permits:

- immediate restoration;
- a lightweight post-custody review;
- direct correction of any custody-derived status;
- proportionate restoration/support for objectively measurable loss where Law later defines entitlement.

No finding of police misconduct is required.

### Result

**PASS.**

**Lawful Short Custody != Zero Civil Burden**

---

## 3. Scenario B — long custody, prosecution threshold ultimately not met

A participant is detained under a valid continuing legal basis while a serious and complex incident is investigated. The evidential state remains genuinely uncertain for several days. Independent prosecution later determines that the prosecution threshold is not met. The participant is released.

They have lost income, missed caregiving responsibilities and suffered substantial disruption.

### Analysis

The architecture separates:

- validity of initial detention;
- validity of each continuation;
- prosecution sufficiency;
- resulting participant harm.

Even if every detention review was reasonable, the participant may have borne a large burden for a public protective process that did not result in prosecution.

A post-custody civil-burden review is therefore appropriate.

The magnitude of remedy may scale with actual material consequences and duration without implying that lawful detention becomes wrongful retrospectively.

### Result

**PASS.**

This is the strongest case for a no-fault remedy route.

---

## 4. Scenario C — custody continues after authority expires

A participant is initially detained lawfully. New evidence removes the only continuing detention basis at 14:00, but administrative delay means release does not occur until the following morning.

### Analysis

The custody architecture already rejects administrative convenience as detention authority.

The lawful phase and unlawful/excess phase must be separable.

**Lawful Custody At T1 != Lawful Custody At T2**

The post-14:00 deprivation requires stronger remedy/accountability than the earlier lawful phase.

### Result

**PASS.**

**Authority Sunset Must Produce Operational Release, Not Merely Legal Reclassification**

---

## 5. Scenario D — lawful detention, unnecessary isolation

Custody itself is justified. The participant is automatically placed in isolation because the facility uses isolation as a default intake practice. No individual safety, evidence or operational reason requires it.

### Analysis

Detention authority does not automatically authorise isolation.

The additional restriction requires its own legitimate function.

The custody remains potentially lawful while the isolation is an excessive rights restriction.

### Result

**PASS.**

**Lawful Custody != Lawful Every Restriction Within Custody**

This validates granular restriction mapping.

---

## 6. Scenario E — lawful custody, fiduciary consultation denied

The participant is validly detained but staff delay access to the defence fiduciary for convenience.

### Analysis

Custody does not extinguish protected consultation.

Administrative convenience is not sufficient to penetrate or deny a protected representational function.

Any genuine delay would need its own legitimate temporary basis.

### Result

**PASS.**

**Custody != Suspension Of Protected Fiduciary Consultation**

---

## 7. Scenario F — silence causes harsher custody

A detained participant exercises the right to silence. Staff classify the participant as uncooperative and impose a more restrictive custodial state solely for refusing self-accusatory questioning.

### Analysis

This indirectly punishes exercise of the right.

Unless separate behaviour creates an independently legitimate safety/custody reason, silence cannot manufacture authority for additional restriction.

### Result

**PASS.**

**Exercise Of Right To Silence != Custodial Risk By Itself**

---

## 8. Scenario G — repeated lawful detentions from defective alert system

An automated identification system repeatedly produces plausible false positives involving the same participant. Each individual officer reasonably relies on the information available at the time, and each short detention may initially satisfy the legal threshold. Later review reveals the systemic defect.

### Analysis

Individual lawfulness does not establish system adequacy.

Repeated civil burdens become system evidence.

The participant may have accumulated losses even where no single officer committed misconduct.

Required routes:

- individual restoration/remedy;
- system defect investigation;
- correction of the alert architecture;
- protection against recurrence;
- review of prior affected participants.

### Result

**PASS.**

**Repeated Individually Lawful Interventions May Reveal Systemically Avoidable Harm**

This is a strong example of why no-fault remedy and system review must coexist.

---

## 9. Scenario H — physically released, digital restrictions remain

A participant is released without charge. Their civil identity status still marks them as detained, an access credential remains suspended and an automated travel restriction continues.

### Analysis

Physical release is incomplete restoration.

Release must propagate to dependent systems whose restrictions existed only because of custody.

Where a separate continuing authority exists, that restriction may remain, but it must identify its own basis.

### Result

**PASS.**

**Custody Sunset Must Propagate To Custody-Derived Restrictions**

Candidate addition:

**Dependent Restriction Without Independent Authority Must Sunset With Parent Custody Authority**

---

## 10. Scenario I — reputational record implies guilt

A participant is released without charge, but an ordinary civil-facing record continues to display an arrest/detention marker in a manner likely to imply wrongdoing.

### Analysis

Historical provenance may legitimately preserve that custody occurred.

But historical truth and present operational/reputational signalling are different functions.

A record can preserve the event without representing detention as guilt.

### Result

**PASS WITH HISTORICAL/RECORDS INTERFACE.**

**Preserve Custody Provenance != Perpetuate Inculpatory Status**

This requires coordination with Historical and participant-record architecture.

---

## 11. Scenario J — participant causes avoidable delay

A participant lawfully exercises the right to silence but separately and unlawfully destroys evidence, causing additional investigative delay and a longer otherwise lawful detention.

### Analysis

The right to silence itself cannot reduce remedy.

Separate participant conduct that materially caused avoidable loss may be relevant where Law establishes that conduct and causal relationship.

The system must not relabel protected silence as obstruction.

### Result

**PASS WITH CAUSATION REQUIREMENT.**

**Protected Silence != Participant-Caused Delay**

**Separate Proven Conduct May Affect Causal Allocation Without Extinguishing Rights**

---

## 12. Scenario K — custody followed by prosecution and acquittal

A participant is lawfully detained, prosecuted under a properly satisfied threshold and later acquitted.

### Analysis

Acquittal does not automatically make earlier detention or prosecution unlawful.

Nor does it automatically establish the same no-charge remedy state.

However, unlawful/excess custodial restrictions remain independently remediable, and Law may separately choose whether some no-fault burden-sharing applies after acquittal.

### Result

**PASS / POLICY BOUNDARY PRESERVED.**

**Acquittal != Automatic Retrospective Invalidity Of Custody**

The no-charge/no-prosecution route should not silently determine post-acquittal remedy.

---

## 13. Scenario L — compensation is cited to justify lower custody threshold

A decision-maker argues that because Concord compensates innocent participants later, it can tolerate a lower detention threshold now.

### Analysis

Rejected.

Remedy occurs after harm; it does not purchase authority to impose harm.

The original detention threshold must be independently satisfied.

### Result

**PASS.**

**Future Remedy != Present Authority**

**Compensability Of Harm != Permission To Impose Harm**

This is a critical safeguard.

---

## 14. Scenario M — participant has unusual dependency burden

Two participants are detained for the same lawful two-hour period. One experiences minimal external consequence. The other is the sole carer for a dependent participant and the custody causes emergency replacement care and substantial disruption.

### Analysis

Equal detention duration does not imply equal harm.

A purely tariff-based remedy may be simple but incomplete.

The architecture should permit a standard baseline plus evidence of material consequential loss where appropriate.

### Result

**PASS WITH REMEDY-DESIGN REQUIREMENT.**

**Equal Restriction Duration != Equal Consequential Harm**

---

## 15. Scenario N — detention is materially protective of the detained participant

A participant is temporarily detained/held because a credible immediate threat makes release unsafe and no less restrictive safe alternative is presently available.

### Analysis

Custody may sometimes serve protection of the detained participant as well as wider public protection.

The same rules still apply:

- legitimate function;
- minimum necessary restriction;
- duty of care;
- review;
- release when function ends;
- remedy for avoidable/excess harm.

Protective purpose does not convert the participant into an object of state control.

### Result

**PASS.**

**Protective Custody != Ownership**

---

## 16. Scenario O — medical need increases during custody

A participant develops an acute medical condition while lawfully detained. Staff delay treatment because transport is inconvenient.

### Analysis

The Concord's control has increased participant dependence.

Duty of care therefore becomes stronger, not weaker.

Administrative inconvenience cannot justify avoidable medical harm.

### Result

**PASS.**

**Custodial Control + Participant Dependence -> Heightened Duty To Maintain Essential Care**

---

## 17. Scenario P — facility imposes maximum restriction by category

All participants charged with a broad offence class are automatically placed in the highest security conditions regardless of individual circumstances.

### Analysis

Category may inform risk assessment but cannot substitute for the contextual authority test where materially greater restrictions are imposed.

### Result

**PASS.**

**Group Classification != Individual Maximum Restriction Authority**

---

## 18. Scenario Q — remedy process itself becomes adversarial burden

A participant released without charge is required to initiate complex litigation, prove officer fault and repeatedly disclose sensitive information merely to recover straightforward custody-derived financial loss.

### Analysis

This defeats the distinction between misconduct accountability and civil-burden remedy.

Where harm is known and objectively attributable to custody, proactive or low-friction remedy is preferable.

### Result

**PASS.**

**Remedy Access Burden Should Not Recreate Avoidable Custodial Harm**

This supports automatic entitlement detection for straightforward cases.

---

## 19. Scenario R — participant refuses offered restoration

Concord offers return of property and correction of a custody-derived status. The participant refuses or cannot presently receive the restoration.

### Analysis

The system should preserve the offer/status and maintain an appropriate route for later completion rather than falsely recording restoration as completed.

### Result

**PASS.**

**Remedy Offered != Remedy Completed**

---

## 20. Scenario S — release followed by immediate re-detention on unchanged grounds

A participant is released because the detention threshold is no longer met. Minutes later they are re-detained on the same unchanged evidential state to restart an administrative time period.

### Analysis

This is authority laundering.

A new custody episode requires a genuinely valid current basis; procedural cycling cannot regenerate expired authority.

### Result

**PASS.**

**Release And Re-Detention != Authority Renewal Without Material Basis**

---

## 21. Scenario T — custodial conditions themselves create evidence

A participant becomes distressed after prolonged sleep disruption caused by custody conditions. Investigators treat the resulting confused statements as evidence of deception.

### Analysis

The state-created conditions affect evidential reliability and may themselves constitute excessive harm.

Provenance must include relevant custodial conditions where they materially affect evidence.

### Result

**PASS WITH EVIDENTIARY INTERFACE.**

**State-Created Evidential Distortion Must Remain Visible In Provenance**

---

## 22. Cross-scenario findings

### 22.1 Custody is genuinely a Contextual Wrapper

The tests support modelling custody as:

- activated by a defined threshold;
- bounded by legitimate function;
- containing explicit restrictions and protections;
- subject to continuing review;
- terminated by functional sunset;
- followed by restoration and possible remedy.

### 22.2 Rights limitation is granular

Lawful detention does not validate every internal restriction.

### 22.3 Control and duty rise together

The more the participant cannot independently secure food, healthcare, safety, communication or exit, the greater the Concord's responsibility for those functions.

### 22.4 Remedy and fault are distinct axes

The tests strongly support three separate questions:

**Was authority valid?**

**Was avoidable/excess harm caused?**

**What residual civil burden remains even if authority was valid and implementation reasonable?**

### 22.5 No-fault remedy survives adversarial testing

Nothing in the test requires calling lawful custody unlawful merely to recognise real participant loss.

### 22.6 Remedy cannot legitimise custody

The availability of later restoration/compensation must never enter the authority threshold as a reason to detain.

### 22.7 Release must propagate

Custody-derived digital, administrative and reputational restrictions require active sunset/restoration.

---

## 23. Additional candidate invariants

CPR-21 Lawful Custody At T1 != Lawful Custody At T2.  
CPR-22 Authority Sunset Must Produce Operational Release, Not Merely Legal Reclassification.  
CPR-23 Lawful Custody != Lawful Every Restriction Within Custody.  
CPR-24 Custody != Suspension Of Protected Fiduciary Consultation.  
CPR-25 Exercise Of Right To Silence != Custodial Risk By Itself.  
CPR-26 Repeated Individually Lawful Interventions May Reveal Systemically Avoidable Harm.  
CPR-27 Custody Sunset Must Propagate To Custody-Derived Restrictions.  
CPR-28 Dependent Restriction Without Independent Authority Must Sunset With Parent Custody Authority.  
CPR-29 Preserve Custody Provenance != Perpetuate Inculpatory Status.  
CPR-30 Protected Silence != Participant-Caused Delay.  
CPR-31 Acquittal != Automatic Retrospective Invalidity Of Custody.  
CPR-32 Future Remedy != Present Authority.  
CPR-33 Compensability Of Harm != Permission To Impose Harm.  
CPR-34 Equal Restriction Duration != Equal Consequential Harm.  
CPR-35 Custodial Control + Participant Dependence -> Heightened Duty To Maintain Essential Care.  
CPR-36 Group Classification != Individual Maximum Restriction Authority.  
CPR-37 Remedy Access Burden Should Not Recreate Avoidable Custodial Harm.  
CPR-38 Remedy Offered != Remedy Completed.  
CPR-39 Release And Re-Detention != Authority Renewal Without Material Basis.  
CPR-40 State-Created Evidential Distortion Must Remain Visible In Provenance.

---

## 24. Test conclusion

**OVERALL RESULT: PASS WITH DOWNSTREAM REMEDY-PROCEDURE AND RECORDS INTERFACES IDENTIFIED.**

The custody-as-protected-context model survived the tested cases.

The strongest finding is that legality and remedy must remain separate dimensions.

A participant can be:

- lawfully detained;
- appropriately treated;
- promptly released when authority ends;

and still have suffered a real civil burden that should not automatically be allocated entirely to them merely because no official committed misconduct.

The architecture therefore supports:

**Custody Legality Review**
+
**Restriction Legality Review**
+
**Harm / Civil-Burden Review**
+
**System Review**

as related but distinct processes.

The test also strengthens the principle:

> **The Concord cannot purchase coercive authority by promising compensation afterward.**

Remedy follows legitimate authority and harm assessment. It never substitutes for the threshold required before rights are restricted.

The next development should define the post-custody remedy mechanism, including automatic restoration, baseline no-fault remedy, consequential-loss assessment, participant challenge, causation and interfaces with Historical records and Civil Contact.
