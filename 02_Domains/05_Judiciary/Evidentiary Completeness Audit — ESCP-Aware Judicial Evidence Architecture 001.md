# Evidentiary Completeness Audit — ESCP-Aware Judicial Evidence Architecture 001

**Project:** The Concord
**Domain:** Judiciary / Law / Civil Security / Historical
**Date:** 3 October 2026
**Status:** ACTIVE DEVELOPMENT / EVIDENTIARY COMPLETENESS ARCHITECTURE / PROVISIONAL / NON-CANONICAL

## 1. Purpose

This note develops the evidentiary-completeness safeguard identified by the Combined Architecture Stress Test 001.

It applies the portable **Evaluation-Space Completeness Problem (ESCP)** and relevant **Knowledge Control System (KCS)** principles to the independent judicial evidentiary function.

The problem is:

> **An evidentiary system may correctly identify, preserve, index and disclose every evidence object represented within its present evidence space while still reaching an invalid completeness conclusion if a materially relevant evidence class, source, relationship or query is absent from that space.**

Therefore:

**Accurate Evidentiary Index != Complete Evidentiary Space**

**Everything Retrieved != Everything Relevant**

**No Match Found != Evidence Does Not Exist**

The purpose of the audit is not to prove universal completeness. It is to expose and manage the limits of the evidentiary search/evaluation space.

---

## 2. ESCP translation

Let the evidentiary function's represented evidence space be:

**E_A**

Let the evidence actually relevant to the material proposition be:

**E_R**

The evidentiary function may be completely accurate about every object in E_A.

If:

**E_A subset-of E_R**

then local evidential accuracy does not establish global evidential completeness.

The dangerous inference is:

**All Indexed Evidence Reviewed**
-> **Therefore All Material Evidence Has Been Considered**

That inference is not justified merely by index quality.

The evidentiary analogue of the ESCP Completeness Leap is:

> **The repository/search worked correctly, therefore no materially relevant evidence exists outside the repository/search space.**

This must be structurally prohibited.

---

## 3. KCS boundary

KCS already supplies directly relevant invariants:

**Not Retrieved != Does Not Exist**

**Not Recorded != Does Not Exist**

**Successful Retrieval != Complete Evaluation Space**

A negative search result is evidence about the bounded search, not proof about reality.

The judicial evidentiary architecture should preserve this distinction explicitly.

---

## 4. Evidence-space categories

For a material proposition, evidence sources can be represented provisionally as:

### A. Known and searched

Evidence source/class is represented and has been searched or examined within the legitimate envelope.

### B. Known but not searched

The source/class is known but not examined because it is irrelevant, disproportionate, unavailable, outside authority, technically inaccessible, destroyed, expired, or otherwise excluded.

The reason must be represented where material.

### C. Known inaccessible/restricted

The source/class may be relevant but access is constrained by privacy, protected space, security, privilege, jurisdiction, technical limitations or other legitimate boundary.

This does not permit the system to pretend the source does not exist.

### D. Known missing

A source expected to exist is absent, corrupted, deleted, not recorded or otherwise unavailable.

### E. Newly discovered source class

A class/source not represented in the original evidence space becomes visible through contradiction, MRT, new testimony, system knowledge or other development.

### F. Unrepresented evidence class

A materially relevant class/source may exist but is not presently represented as relevant.

This is the hardest ESCP category and cannot be exhaustively enumerated from inside the current space.

---

## 5. Evidentiary completeness is proposition-relative

The system should not ask:

> Have we searched everything?

That question is generally unbounded.

It should ask:

> Is the represented evidentiary space sufficiently developed to support a responsible decision on this material proposition at this stage, and what known limitations remain?

Examples:

- whether an event occurred;
- whether A was present;
- whether A performed an act;
- whether a timestamp is reliable;
- whether a justification is supported;
- whether a police authority was valid;
- whether a particular aggravating factor is established.

A source irrelevant to one proposition may be decisive for another.

**Evidence-Space Sufficiency Is Proposition-Relative**

---

## 6. Evidence Source Map

For each consequential case, the independent evidentiary function should maintain a proportionate **Evidence Source Map**.

Candidate source classes include where relevant:

- participant statements;
- witness statements;
- police bodycam;
- police vehicle/dash cameras;
- public/private CCTV under legitimate access;
- dispatch/communications;
- custody/interview recordings;
- physical evidence;
- forensic evidence;
- digital-device evidence;
- system/application logs;
- sensor/telemetry records;
- access-control/location records;
- financial/transaction records;
- medical/technical records where legitimately relevant;
- historical operational records;
- system reliability/error metrics;
- third-party records;
- alternative-actor evidence;
- expert evidence;
- other case-specific source classes.

This is not a mandatory universal checklist.

Its purpose is to make the represented evidence space inspectable.

**Evidence Source Map != Exhaustive Reality Map**

---

## 7. Source-state representation

Each material source/class should, where proportionate, carry a state such as:

- SEARCHED / EXAMINED;
- PARTIALLY SEARCHED;
- IDENTIFIED / NOT YET SEARCHED;
- ACCESS RESTRICTED;
- ACCESS DENIED;
- TECHNICALLY UNAVAILABLE;
- DESTROYED / EXPIRED;
- EXPECTED BUT MISSING;
- NOT MATERIAL TO CURRENT PROPOSITION;
- DEFERRED;
- NEWLY DISCOVERED;
- UNKNOWN COMPLETENESS.

The state should include relevant provenance and reason.

This prevents silence from being interpreted as absence.

---

## 8. Search provenance

A consequential negative evidentiary search should preserve enough information to reconstruct what the negative result actually means.

Candidate record:

**Query**
+ **Proposition**
+ **Source(s)**
+ **Time/Date Range**
+ **Subject/Object Scope**
+ **Search Method**
+ **Access Boundary**
+ **Result**
+ **Known Limitations**
+ **Unsearched Alternatives**
+ **Operator/System Provenance**

Therefore:

**No CCTV Match In Cameras 1-4 During T != No CCTV Evidence Exists**

It means only that the bounded search produced no match within its represented scope.

---

## 9. Completeness triggers

A completeness review should be triggered where material indicators suggest the current evidence space may be inadequate.

Candidate triggers include:

- unresolved contradiction;
- strong mismatch between evidence and current hypothesis;
- unexplained timeline gap;
- evidence implying an unrepresented actor;
- expected recording absent;
- evidence source referenced by another source but not represented;
- common-source dependency discovered;
- apparently independent evidence collapses to one origin;
- both fiduciaries rely on the same untested assumption;
- Judicial MRT reaches a proposition that cannot be responsibly evaluated from represented evidence;
- new technology/system source becomes known;
- source index or custodian error is discovered;
- material evidence appears after a prior negative search;
- unexplained asymmetry between expected and observed evidence.

These are triggers for review, not automatic authority to search everything.

---

## 10. ESCP challenge question

At material transition points, the evidentiary function, fiduciaries and Judiciary should be able to ask:

> **What would have to exist, be missing, or be unrepresented for our current evidential conclusion to be wrong?**

This question does not generate arbitrary possibilities.

It is bounded by material plausibility.

A related question is:

> **Which evidence classes would be expected under the leading competing hypotheses?**

This connects ESCP to MRT.

---

## 11. MRT interface

MRT provides an operational way to expose evidence-space incompleteness.

For each materially plausible hypothesis:

- what evidence supports it?
- what evidence opposes it?
- what evidence is neutral?
- what evidence should plausibly exist if it were true?
- what expected evidence is absent?
- is that absence meaningful?
- what evidence class could distinguish it from competing hypotheses?
- is the distinguishing class represented in the current Evidence Source Map?

A contradiction may therefore indicate:

**Evidence Conflict**

or:

**Hypothesis Failure**

or:

**Evidence-Space Incompleteness**

These should not be collapsed.

---

## 12. Expected-evidence reasoning

Expected evidence can be useful but dangerous.

If hypothesis H predicts evidence class X, absence of X may weaken H only if:

- X would reasonably be expected;
- the relevant source existed/functioned;
- the source was legitimately and adequately searched;
- retention did not remove it;
- the query could detect it;
- access limitations did not conceal it.

Therefore:

**Expected Evidence Absent != Evidence Of Absence Without Search/Source Validation**

This protects against false exculpatory and false inculpatory inference.

---

## 13. Bounded completeness state

The independent evidentiary function should not certify:

**COMPLETE — ALL EVIDENCE FOUND**

Instead it may record a bounded state such as:

### Evidential Space Sufficient For Present Decision

The represented evidence space has been examined sufficiently for the present legal/procedural decision, with material known limitations disclosed.

### Evidential Space Materially Incomplete

A known material source/class or unresolved evidence-space defect prevents responsible determination.

### Evidential Space Sufficient With Restricted Source

A material protected source has been handled through an authorised bounded mechanism and its effect/limitations are represented.

### Evidential Completeness Uncertain

No specific defect necessarily blocks the present stage, but completeness cannot responsibly be characterised beyond the recorded search space.

The exact terminology may later be standardised.

---

## 14. Sufficiency is stage-relative

The evidence-space depth required for:

**Police Triage**

is not necessarily the depth required for:

**Apprehension**

or:

**Prosecution Threshold**

or:

**Final Adjudication**

or:

**Appeal / Reopening**

Therefore:

**Evidence-Space Sufficiency At Stage N != Permanent Completeness**

A case legitimately progressing from one stage may later require deeper evidence.

This explains why deeper CCTV or historical evidence may emerge after prosecution begins without implying the earlier threshold was necessarily defective.

---

## 15. No completeness fishing authority

ESCP awareness must not create an unlimited search mandate.

The statement:

> there may be evidence we have not considered

is always logically possible.

It cannot by itself authorise intrusion.

A deeper search still requires:

- materially relevant proposition;
- plausible evidential source/class;
- legitimate purpose;
- appropriate authority;
- proportionality;
- CIBB/privacy boundary;
- recorded scope;
- reviewability where consequential.

Therefore:

**ESCP Risk != General Search Authority**

**Unknown Unknowns != Authority To Search Everyone**

---

## 16. Alternative-suspect completeness

Where current evidence materially suggests another actor, completeness review should ask whether the evidence space has been distorted by suspect fixation.

Questions include:

- were sources searched only around the current accused?
- were time/location queries unnecessarily person-bound?
- was evidence concerning unknown/alternative actors indexed?
- did the current suspect hypothesis determine what was considered relevant?
- would an event-centred query expose different evidence?

This supports a shift from:

**What evidence exists about A?**

to:

**What evidence exists about the event, and who does it support?**

where legitimately required.

---

## 17. Fiduciary completeness challenge

Both prosecution and defence fiduciaries should be able to challenge the represented Evidence Source Map.

They may identify:

- omitted source class;
- inadequate search scope;
- hidden dependency;
- missing provenance;
- unjustified access restriction;
- overly broad search;
- irrelevant intrusion;
- unrepresented alternative hypothesis.

Neither fiduciary's request automatically creates authority.

**Completeness Challenge != Search Authority**

The independent evidentiary function/Judiciary determines the legitimate evidential response under Law.

---

## 18. Judicial completeness challenge

Judicial MRT may expose a missing evidence class even where both fiduciaries are satisfied.

Judiciary may ask:

- what source classes were considered?
- what was not searched?
- why?
- what access limitations existed?
- which negative findings depend on incomplete search?
- what source could resolve this material contradiction?
- is the proposed search legitimately within adjudicative authority?

This preserves framing independence.

**Fiduciary Consensus != Evidentiary Completeness**

---

## 19. Evidentiary-body self-audit

Because the independent evidentiary function can itself omit sources, it requires internal and external completeness safeguards.

Candidate mechanisms:

- source-map review;
- search-provenance audit;
- random/sample reconstruction;
- independent second-pass review for consequential cases;
- comparison between expected source classes and indexed classes;
- automated anomaly detection used only as an indicator;
- participant/fiduciary challenge;
- Judicial MRT challenge;
- preserved record of later-discovered omissions;
- feedback into evidence-source taxonomy and search methods.

The goal is correction and learning, not a claim that audit eliminates ESCP.

**Completeness Audit != Proof Of Completeness**

---

## 20. Discovery of omitted evidence

If material evidence is later found outside the represented evidence space:

1. preserve the earlier search/evidence-space state;
2. add the new evidence with provenance;
3. identify why it was omitted;
4. reassess affected hypotheses/propositions;
5. reassess prosecution threshold where relevant;
6. reassess judicial finding/procedure where relevant;
7. determine whether omission was reasonable, negligent, systemic or deliberate through the appropriate review;
8. update evidence-source/search architecture if a generalisable gap is exposed.

Do not rewrite history as though the evidence was always represented.

This follows KCS provenance principles.

---

## 21. Historical learning

Repeated omissions can reveal structural blind spots.

Examples:

- a camera class repeatedly omitted from searches;
- a sensor system poorly indexed;
- a category of third-party evidence never considered;
- a search interface that cannot query relevant metadata;
- a legal procedure that systematically hides an evidence class;
- a privacy projection that removes materially necessary context.

These patterns should feed Historical and Research.

**Individual Omission -> Case Correction**

**Repeated Omission Pattern -> System Review**

---

## 22. Initial invariants

ECA-01 Accurate Evidentiary Index != Complete Evidentiary Space.  
ECA-02 Everything Retrieved != Everything Relevant.  
ECA-03 No Match Found != Evidence Does Not Exist.  
ECA-04 Evidence Source Map != Exhaustive Reality Map.  
ECA-05 Evidentiary Index != Complete Evidence Universe.  
ECA-06 Evidence-Space Sufficiency Is Proposition-Relative.  
ECA-07 Evidence-Space Sufficiency Is Stage-Relative.  
ECA-08 Evidence-Space Sufficiency At Stage N != Permanent Completeness.  
ECA-09 Expected Evidence Absent != Evidence Of Absence Without Search/Source Validation.  
ECA-10 Evidence Conflict != Necessarily Hypothesis Failure.  
ECA-11 Evidence Conflict May Indicate Evidence-Space Incompleteness.  
ECA-12 ESCP Risk != General Search Authority.  
ECA-13 Unknown Unknowns != Authority To Search Everyone.  
ECA-14 Completeness Challenge != Search Authority.  
ECA-15 Fiduciary Consensus != Evidentiary Completeness.  
ECA-16 Completeness Audit != Proof Of Completeness.  
ECA-17 Later-Discovered Evidence Must Preserve Prior Search Provenance.  
ECA-18 Current Suspect Hypothesis != Boundary Of Relevant Evidence Space.  
ECA-19 Known Evidence Set != Necessarily Complete Evaluation Space.  
ECA-20 Search Scope Must Be Represented Wherever A Negative Result Is Material.

---

## 23. Compact operating cycle

**Material Proposition**
-> **Represent Current Evidence Space**
-> **Map Material Evidence Sources**
-> **Record Search / Access / Missing States**
-> **Apply MRT / Dependency / Contradiction Review**
-> **Ask ESCP Challenge**
-> **Identify Material Completeness Defect If Any**
-> **Test Authority For Any Deeper Search**
-> **Perform Bounded Search Where Authorised**
-> **Update Evidence State + Provenance**
-> **Record Bounded Evidential-Sufficiency State**
-> **Proceed / Pause / Return / Reassess As Appropriate**

At no point does the system claim universal completeness.

---

## 24. Development conclusion

The independent evidentiary function should not attempt to prove that it possesses all evidence.

Its legitimate claim is narrower:

> **Within a recorded and reviewable evidence-source/search space, the system has developed the evidential state sufficiently for the present proposition and procedural stage, subject to the stated known limitations and continuing ESCP risk.**

This transforms completeness from an impossible absolute claim into a bounded, inspectable and challengeable evidential state.

The architecture also prevents ESCP from becoming an excuse for universal surveillance:

> **The possibility of missing evidence justifies epistemic humility and completeness review. It does not manufacture search authority.**

The next validation step should stress-test this architecture against cases where the missing evidence is exculpatory, inculpatory, privacy-protected, destroyed, technically unsearchable, falsely expected, or entirely outside the original evidence taxonomy.
