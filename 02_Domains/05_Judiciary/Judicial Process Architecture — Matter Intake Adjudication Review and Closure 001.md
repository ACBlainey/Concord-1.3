# Judicial Process Architecture — Matter Intake, Adjudication, Review and Closure 001

**Project:** The Concord Framework  
**Domain:** Judiciary  
**Date:** 9 October 2026  
**Status:** ACTIVE DEVELOPMENT / BASIC OPERATING ARCHITECTURE / PROVISIONAL / NON-CANONICAL  
**Primary Interfaces:** Law; Civil Security; Governance; Historical; Civil Contact  
**Related:** Mirrored Reality Trees; Legal Classification Grammar; Process Integrity; Temporal Validity; Bounded Contextual Authority

---

## 1. Purpose

This document provides a compact operational state map and cross-domain interface for the much larger existing Judiciary architecture. It is subordinate to, and must be read with, `Judiciary V2 Canonical.md`; it does not replace or supersede the canonical source.

Source resolution performed after this document's initial creation confirmed that Judiciary V2 already contains substantial architecture for case procedure, standing, jurisdiction, evidence, representation, hearings, remedies, enforcement, appeals, court topology, administration, triadic adjudication, constitutional review and judicial failure/correction. Where this compact map conflicts with or appears less developed than Judiciary V2, the canonical source controls unless a later reconciled architecture explicitly changes that position.

The purpose here is therefore to expose the common lifecycle and interfaces in a compact form, not to infer absence from the size or organisation of the canonical source.

The design principle is:

> **Judicial Function Should Determine Institutional Form; Institutional Form Should Not Be Assumed First.**

The architecture must support:
- criminal matters;
- civil disputes;
- review of authority;
- protective applications;
- administrative/regulatory disputes;
- constitutional questions;
- appeals/review.

These may later require different institutional forms, but they share a common need for legitimate intake, jurisdiction, fair hearing, reasoned decision, review and closure.

---

## 2. Judicial function

The Judiciary exists to provide a legitimate, contestable process for resolving rights-relevant disputes and legal states that cannot properly be determined unilaterally by an interested party.

Core function:

> **Receive → Classify → Establish Jurisdiction → Preserve Fair Participation → Determine Relevant Facts/Law → Decide → Remedy/Consequence → Review → Close/Record**

---

## 3. Judiciary is not general government

> **Judicial Authority != General Governance Authority.**

The Judiciary does not acquire power merely because a question is difficult or contested.

Authority derives from the judicial function actually required.

---

## 4. Judiciary is not investigation

> **Adjudication != Investigation.**

Judges/adjudicators may control evidential process and order lawful steps where authorised, but should not simply become another investigative party.

Criminal investigation primarily belongs to Civil Security/investigative functions.

---

## 5. Judiciary is not prosecution

> **Judiciary != Prosecution.**

The adjudicator must not own the prosecution theory.

This is especially important for Mirrored Reality Trees.

---

## 6. Judiciary is not defence

Likewise:

> **Judiciary != Defence.**

The adjudicator protects fair process without becoming partisan representative.

---

# PART I — MATTER TYPES

## 7. Criminal matter

A criminal matter asks whether a participant bears legal responsibility for an alleged offence and, if established, what lawful consequences follow.

Core distinction:

> **Charge != Guilt.**

---

## 8. Civil matter

A civil matter asks whether rights/obligations between participants or legal persons require:
- declaration;
- compensation;
- restitution;
- performance;
- restraint;
- restoration;
- other remedy.

> **Civil Liability != Criminal Guilt.**

---

## 9. Protective matter

A protective matter asks whether present conditions justify bounded protective authority before or independently of final fault determination.

Examples:
- immediate safety order;
- temporary separation;
- emergency preservation;
- mental-health exceptional authority review.

> **Protective Need != Punitive Guilt.**

---

## 10. Authority-review matter

A participant may challenge:
- detention;
- search;
- seizure;
- licence restriction;
- guardianship;
- emergency authority;
- administrative decision;
- other coercive state action.

> **Authority Exercise Must Remain Reviewable While It Matters.**

---

## 11. Constitutional matter

A constitutional matter asks whether:
- a law;
- authority;
- institutional action;
- process

is consistent with higher constitutional/ethical constraints.

> **Enacted != Constitutionally Valid.**

---

## 12. Administrative/regulatory matter

This concerns legally consequential decisions made by specialised institutions.

Judicial function is review/resolution, not automatic substitution of judicial preference for specialised expertise.

---

# PART II — COMMON LIFECYCLE

## 13. State J0 — Pre-matter condition

An event, dispute, alleged offence, authority exercise or rights-relevant condition exists.

No judicial case necessarily exists yet.

> **Problem Exists != Judicial Matter Exists.**

---

## 14. State J1 — Referral / Application / Filing

A matter enters the judicial system through a legitimate route.

Possible sources:
- prosecution referral;
- participant application;
- petition;
- appeal/review application;
- authority referral;
- mandatory review trigger.

Civil Contact should make routes discoverable.

---

## 15. Standing

Before merits:

**Does the initiating participant/entity have legitimate standing to raise this matter?**

Standing can arise from:
- direct affected interest;
- fiduciary/representative role;
- stewardship standing;
- statutory/public function;
- authorised prosecution;
- constitutional review route.

> **Standing To Raise != Authority To Decide.**

---

## 16. Standing versus merits

> **Weak Claim On Merits != No Standing Automatically.**

Standing asks whether the party may invoke process, not whether they should ultimately win.

---

## 17. State J2 — Jurisdiction

The system identifies whether this judicial function has authority over:
- subject matter;
- participant/legal person;
- place/context;
- time;
- remedy sought.

> **Case Filing != Judicial Jurisdiction.**

---

## 18. Jurisdiction must be sourced

Jurisdiction should derive from promulgated law/constitutional allocation.

> **Court Convenience != Jurisdiction.**

---

## 19. Jurisdiction challenge

Participants should be able to challenge jurisdiction.

> **Challenge To Jurisdiction != Obstruction.**

Where jurisdiction is uncertain, preliminary resolution should occur before unnecessary coercive process.

---

## 20. Cross-context jurisdiction

A matter may touch several:
- local jurisdictions;
- safe spaces;
- domains;
- external civilisations.

Interaction does not automatically merge jurisdiction.

Conflict-of-laws architecture remains future work.

---

## 21. State J3 — Case creation

Once standing/jurisdiction threshold is provisionally satisfied, a formal case state is created.

Minimum case identity:
- case ID;
- matter type;
- parties;
- filing/referral;
- legal basis;
- jurisdiction;
- current status;
- assigned process;
- access/protection state;
- provenance.

---

## 22. Case record

The case record should distinguish:
- allegation;
- evidence;
- argument;
- procedural order;
- finding;
- judgment;
- later review.

> **Allegation In Case Record != Historical Fact Of Guilt.**

---

## 23. State J4 — Notice

Affected parties receive sufficient notice of:
- nature of matter;
- legal basis;
- material allegations/claims;
- procedural rights;
- response route;
- relevant deadlines;
- restrictions/orders.

> **Secret Adjudication Is Presumptively Incompatible With Fair Participation.**

Exceptions require strong bounded justification.

---

## 24. Notice and urgency

Emergency protective action may precede full notice where delay creates serious risk.

But:

> **Emergency Action Before Hearing Creates A Duty For Prompt Review, Not A Permanent Exception To Hearing.**

---

## 25. State J5 — Preliminary review

Preliminary review asks:
- standing?
- jurisdiction?
- intelligible legal claim/charge?
- sufficient threshold to proceed?
- urgent protection required?
- disclosure/preservation needed?
- conflicts/recusal?
- process accommodations?

This is not final merits adjudication.

---

## 26. Criminal referral threshold

Existing Concord position:

Prosecution should follow where sufficient evidence supports referral, rather than police deciding guilt.

Mirrored Reality Trees should test:

**Inculpatory Tree ↔ Exculpatory Tree**

Key question:

> **Is This Even The Right Suspect?**

not merely:

> **Can Enough Evidence Be Collected To Convict This Person?**

---

## 27. Charge sufficiency

A criminal charge should identify:
- promulgated offence;
- applicable legal version;
- alleged conduct;
- required mental state;
- relevant classifiers;
- enough factual basis to justify adjudication.

> **Charge Label != Substitute For Elements.**

---

## 28. Civil claim sufficiency

A civil claim should identify:
- protected interest/obligation;
- alleged breach/wrong;
- requested remedy;
- factual basis.

Technical pleading should not become unnecessary gatekeeping.

---

# PART III — PARTICIPATION AND REPRESENTATION

## 29. Meaningful participation

A participant must have a meaningful opportunity to:
- know the case;
- respond;
- present relevant evidence;
- challenge adverse evidence;
- raise law/authority issues;
- seek review.

> **Presence != Meaningful Participation.**

---

## 30. Accessibility

Process should accommodate:
- disability;
- language;
- substrate;
- communication needs;
- decision-specific capacity.

Accommodation != substantive advantage.

---

## 31. Representation

Participants may require or choose advocates.

Concord advocates should be fiduciaries to their legitimate function.

Defence advocate:
- protects represented participant's lawful interests.

Prosecution advocate:
- represents Concord's legitimate accountability function, not conviction maximisation.

> **Advocacy Function != Ownership Of Outcome.**

---

## 32. Self-representation

Competent participants should not automatically be forced to use an advocate.

But meaningful warnings/support may be appropriate where stakes/complexity are high.

---

## 33. Capacity and representation

Diminished capacity may justify supported decision-making or representation.

> **Need For Assistance != Automatic Loss Of Authorship.**

Guardianship/representation must remain bounded.

---

# PART IV — EVIDENCE AND DISCLOSURE

## 34. Evidence state model

Use existing chain:

**Reality/Event  
→ Observation  
→ Recorded Evidence  
→ Transformation/Derivative  
→ Interpretation  
→ Investigative Hypothesis  
→ Prosecution/Party Assessment  
→ Judicial Finding  
→ Historical Record**

These states must remain legible.

---

## 35. Disclosure

Parties should have access to material evidence needed for meaningful participation, subject to legitimate protection.

In criminal matters, materially exculpatory evidence must not be suppressed.

> **Disclosure Duty != Unlimited Public Disclosure.**

CWA/privacy can protect sensitive material while preserving fair process.

---

## 36. Protected evidence

Possible handling:
- redaction;
- limited access;
- advocate-only access;
- secure review;
- anonymisation;
- contextual wrapper.

But protection must not make challenge impossible.

> **Evidence Protection != Permission To Make Evidence Unchallengeable.**

---

## 37. Unlawfully obtained evidence

Existing position remains:

> **Unlawful Acquisition != Automatic Factual Falsity.**

The process should separately assess:
- reliability;
- weight/admissibility;
- rights violation;
- misconduct remedy;
- deterrence/system correction.

---

## 38. Evidential hearing

Where evidence status is disputed, a preliminary evidential hearing may determine:
- provenance;
- reliability;
- legality;
- scope;
- admissibility/weight;
- protection.

This prevents trial merits from being confused with evidence-management questions.

---

## 39. Mirrored evidence reasoning

For contested factual propositions, Mirrored Reality Trees can structure:

**Hypothesis A — proposition true**  
↔  
**Hypothesis B — proposition false / alternative explanation**

Evidence may:
- support A;
- support B;
- support neither;
- undermine both;
- expose wrong question.

> **Evidence Collection Should Be Capable Of Falsifying The Preferred Theory.**

---

# PART V — INTERIM / PROTECTIVE AUTHORITY

## 40. Interim measures

Before final judgment, temporary measures may sometimes be necessary.

Examples:
- evidence preservation;
- temporary no-contact order;
- temporary asset restraint;
- temporary custody;
- emergency protection.

These require independent BCA analysis.

---

## 41. Interim != final

> **Interim Protective Order != Finding Of Liability Or Guilt.**

Orders should be proportionate, reviewable and time-bounded.

---

## 42. Least restrictive measure

MNC applies.

> **Need To Preserve Process/Safety != Authority To Impose Maximum Restriction.**

---

## 43. Review clock

Any significant pre-judgment restriction should have:
- review trigger;
- maximum unreviewed duration;
- route to challenge.

Exact periods require later implementation.

---

# PART VI — ADJUDICATION

## 44. State J6 — Adjudication readiness

Before merits adjudication:
- jurisdiction resolved sufficiently;
- notice complete;
- disclosure sufficient;
- representation/accommodation addressed;
- material evidential issues resolved or identified;
- decision-maker conflict checked.

---

## 45. Decision-maker independence

Adjudicator should not have incompatible interest in outcome.

> **Authority To Decide != Personal Stake In Result.**

Conflict architecture should support recusal/substitution.

---

## 46. Adjudicator competence

Different matters may require different expertise.

> **Judicial Independence != Universal Expertise.**

Specialist input may be needed without transferring decision authority automatically.

---

## 47. Fact and law

Adjudication should distinguish:
- what happened;
- evidential confidence;
- applicable law;
- legal classification;
- consequence/remedy.

> **Factual Finding != Legal Conclusion.**

---

## 48. Burden and standard

The exact burdens/standards require dedicated derivation.

At minimum:

> **Consequence Severity Should Affect Required Epistemic Confidence.**

Criminal punishment should require stronger protection against false positive findings than ordinary low-stakes civil allocation.

Do not yet import conventional formulas without derivation.

---

## 49. Presumption

Criminal allegation should not itself shift burden onto accused to prove innocence.

> **Accusation != Evidential Presumption Of Guilt.**

Specific affirmative claims/defences may create bounded evidential burdens, but require later design.

---

## 50. Silence

> **Silence != Proof Of Guilt.**

Any evidential treatment of silence must respect defence rights and context.

---

## 51. Decision

A judgment should identify:
- jurisdiction;
- applicable law/version;
- material facts found;
- material evidence/reasoning;
- unresolved uncertainty where relevant;
- legal classification;
- justification/defence;
- responsibility;
- remedy/consequence;
- review route.

---

## 52. Reason-giving

> **Authority To Decide Creates Responsibility To Explain Consequential Decision.**

Reasons support:
- appeal;
- correction;
- consistency;
- public legitimacy;
- Historical learning.

Sensitive details may require protected versions.

---

## 53. Decision granularity

A matter may contain multiple claims/counts/issues.

> **One Case != One Indivisible Finding.**

Each should be separately resolvable where appropriate.

---

# PART VII — CONSEQUENCE / REMEDY

## 54. State J7 — Consequence determination

After liability/guilt/finding:

Use existing consequence architecture:

**Remedy / Restoration  
+ Accountability / Sanction  
+ Protection  
+ Rehabilitation / Treatment  
+ Review / Sunset**

Do not collapse them.

---

## 55. Separate consequence hearing

Where factual responsibility and consequence require different evidence, separate phases may improve fairness.

This is especially relevant to:
- aggravation/mitigation;
- mental health;
- restitution;
- dangerousness;
- victim impact;
- rehabilitation.

---

## 56. Victim participation

Affected participants may provide relevant evidence concerning harm/remedy.

> **Victim Impact != Victim Authority To Set Punishment.**

Standing does not become sentencing sovereignty.

---

## 57. Present dangerousness

> **Past Offence != Automatic Present Dangerousness.**

Protective restrictions after punishment require current justification.

---

# PART VIII — APPEAL AND REVIEW

## 58. State J8 — Appeal / review

A consequential decision should have a defined review route.

Possible grounds:
- legal error;
- jurisdictional error;
- procedural unfairness;
- material evidential error;
- newly discovered evidence;
- disproportional consequence;
- constitutional defect;
- decision-maker conflict.

---

## 59. Appeal != retrial automatically

Review may:
- affirm;
- correct;
- remit;
- rehear;
- reverse;
- vary consequence.

The proper scope depends on error type.

---

## 60. New evidence

New evidence should not automatically reopen every closed matter.

Relevant:
- materiality;
- reliability;
- availability at original proceeding;
- seriousness;
- finality;
- risk of injustice.

> **Finality Matters, But Finality != Infallibility.**

---

## 61. Correction

BL10 requires genuine correction routes.

> **Judicial Authority Must Remain Open To Correction Without Becoming Permanently Indeterminate.**

This creates a balance between:
- finality;
- corrigibility.

---

## 62. Wrongful conviction

Where conviction is invalidated:
- release if custody lacks other authority;
- correct legal record;
- review dependent restrictions;
- remedy/compensation;
- investigate process failure.

> **Reversal Of Judgment != Automatic Repair Of All Consequences.**

---

# PART IX — ENFORCEMENT

## 63. State J9 — Enforcement

A judgment may authorise:
- payment;
- restoration;
- return;
- custody;
- restriction;
- specific action;
- prohibition;
- other remedy.

> **Judgment != Self-Executing Unlimited Authority.**

Enforcement itself requires bounded authority.

---

## 64. Enforcement scope

Enforcement agent must act within:
- judgment;
- legal authority;
- necessity;
- proportionality;
- time;
- conditions.

> **Authority To Enforce Outcome A != Authority To Impose Unrelated Outcome B.**

---

## 65. Impossibility

A participant cannot be punished simply for impossible compliance.

> **Order Exists != Compliance Was Possible.**

Changed circumstances may require modification.

---

# PART X — CLOSURE AND HISTORICAL CUSTODY

## 66. State J10 — Closure

A matter closes when:
- judgment/remedy final enough for closure;
- appeal window resolved;
- required enforcement state recorded;
- continuing review obligations identified.

Closure does not erase later correction routes.

---

## 67. Historical record

Historical should preserve:
- allegations as allegations;
- evidence provenance;
- findings;
- judgment;
- appeal/reversal;
- correction;
- applicable law/version.

> **Historical Custody != Continuing Judicial Authority.**

---

## 68. Participant public record

A participant's public/civil record should not flatten:
- accusation;
- charge;
- acquittal;
- conviction;
- reversal;
- expired restriction

into one permanent stigma.

> **Process History != Permanent Participant Identity.**

---

# PART XI — PROCEDURAL RIGHTS

## 69. Candidate minimum procedural rights

Subject to matter type:

1. notice;
2. meaningful participation;
3. access to material case;
4. opportunity to respond;
5. ability to present relevant evidence;
6. ability to challenge adverse evidence;
7. independent/impartial decision;
8. reasoned decision;
9. appropriate representation/support;
10. review/appeal route;
11. protection from unnecessary delay/restriction;
12. correction of record.

---

## 70. Speed

> **Justice Delayed Can Become Continuing Unjustified Authority.**

But:

> **Speed != Permission To Remove Necessary Safeguards.**

The objective is timely sufficient process.

---

## 71. Cost/access

> **Ability To Pay != Right To Better Justice.**

The system should not make essential judicial access depend on wealth.

This does not prohibit optional private assistance where it does not create unfair control over process.

---

## 72. Open justice

Transparency supports legitimacy.

But privacy/safety can justify bounded closure/redaction.

> **Open Justice != Universal Public Access To Every Sensitive Detail.**

---

# PART XII — PROCESS STATE MACHINE

## 73. Common lifecycle

**J0 — Pre-Matter Condition**  
↓  
**J1 — Referral / Application / Filing**  
↓  
**J2 — Standing + Jurisdiction**  
↓  
**J3 — Formal Case Creation**  
↓  
**J4 — Notice**  
↓  
**J5 — Preliminary Review**  
↓  
**Evidence / Disclosure / Interim Authority / Representation**  
↓  
**J6 — Adjudication**  
↓  
**Finding / Judgment**  
↓  
**J7 — Remedy / Consequence**  
↓  
**J8 — Appeal / Review**  
↓  
**J9 — Enforcement**  
↓  
**J10 — Closure / Historical Custody**

Transitions may branch, terminate early, return for correction or bypass ordinary sequencing under bounded emergency conditions.

---

## 74. Early termination states

A matter may end before adjudication due to:
- no standing;
- no jurisdiction;
- no legally cognisable claim;
- insufficient prosecution threshold;
- withdrawal/settlement where permissible;
- mootness;
- invalid law;
- other lawful resolution.

> **Case Closure != Finding That Allegation Was False.**

---

## 75. Settlement

Civil matters may resolve by authored agreement.

> **Settlement != Judicial Finding Of Underlying Facts Unless Expressly Adjudicated.**

Criminal/public-interest matters may have different limits because parties may not own the entire protected interest.

---

## 76. Default judgment

Failure to participate should not automatically prove every allegation true.

Any default mechanism must consider:
- valid notice;
- ability to participate;
- nature of matter;
- evidence;
- proportionality.

---

# PART XIII — OPEN DESIGN QUESTIONS

## 77. Court topology

**SOURCE-RESOLVED: CANDIDATE ARCHITECTURE ALREADY EXISTS.**

Judiciary V2 already proposes judicial subsidiarity with local courts, regional courts, civilisation-level courts, an ordinary final appellate court, and a distinct Constitutional Court. It also develops jurisdictional routing, case allocation and distributed/future court forms.

The remaining work is not to invent topology from an empty state. It is to validate, reconcile and operationalise the existing candidate topology, including exact first-instance routing, specialist divisions, transfer rules, workload, capture resistance and implementation.

---

## 78. Adjudicator composition / jury interface

**PARTIALLY SOURCE-RESOLVED.**

Judiciary V2 already contains a substantial Triadic Decision Making architecture and a 3×3 Recursive Triadic Constitutional Court, together with judicial-steward qualification, AI assistance/participation questions and specialist expertise interfaces.

What remains genuinely unresolved includes the role, if any, of citizen juries in ordinary adjudication; the boundary between professional Judicial Stewards, citizen fact-finders, specialist assessors and AI assistance; and which case classes justify which composition.

Do not treat the existence of historical jury forms as proof they are optimal, but do not describe adjudicator architecture as absent.

---

## 79. Standards and burdens of proof

**PARTIALLY SOURCE-RESOLVED / GENUINE OPEN IMPLEMENTATION QUESTION.**

Judiciary V2 already establishes that different judicial questions may require different evidential burdens and that consequence, rights, reversibility, institutional role and asymmetric false-positive/false-negative risk are relevant. It deliberately leaves detailed burden architectures for further development. The Law domain separately develops prosecution-threshold sufficiency and distinguishes that threshold from final adjudicative standards.

Remaining work is therefore to derive/calibrate stage- and consequence-appropriate standards without pretending no prior architecture exists and without automatically importing conventional labels such as `balance of probabilities` or `beyond reasonable doubt`.

---

## 80. Prosecution architecture

**SOURCE-RESOLVED: SUBSTANTIAL V1.3 ARCHITECTURE ALREADY EXISTS.**

See `02_Domains/09_Law/Prosecution Threshold and Evidential Sufficiency — Initial Architecture 001.md`, `Independent Prosecution Function — Referral, Threshold and Adjudication Handoff 001.md`, its scenario stress test, and the Judiciary evidentiary/fiduciary reconciliation papers.

Existing architecture already covers referral versus prosecution threshold, independent threshold assessment, whole evidential state, ordinary automaticity once threshold is met subject to explicit lawful exceptions, evidential change and authority sunset, disclosure/truth duties, return for bounded further investigation, and handoff to Judiciary.

Remaining work is validation, procedural implementation and reconciliation—not first-principles invention.

---

## 81. Civil procedure

Need:
- claim/service;
- response;
- discovery/disclosure;
- settlement;
- remedies;
- costs/resource equality.

---

## 82. Enforcement service

Need interface with Civil Security and other authorised bodies.

Judiciary determines lawful state; enforcement capability remains separately bounded.

---

# PART XIV — CANDIDATE INVARIANTS

JP-01 Judicial Function Should Determine Institutional Form; Institutional Form Should Not Be Assumed First.  
JP-02 Judicial Authority != General Governance Authority.  
JP-03 Adjudication != Investigation.  
JP-04 Judiciary != Prosecution.  
JP-05 Judiciary != Defence.  
JP-06 Charge != Guilt.  
JP-07 Civil Liability != Criminal Guilt.  
JP-08 Protective Need != Punitive Guilt.  
JP-09 Authority Exercise Must Remain Reviewable While It Matters.  
JP-10 Enacted != Constitutionally Valid.  
JP-11 Problem Exists != Judicial Matter Exists.  
JP-12 Standing To Raise != Authority To Decide.  
JP-13 Weak Claim On Merits != No Standing Automatically.  
JP-14 Case Filing != Judicial Jurisdiction.  
JP-15 Court Convenience != Jurisdiction.  
JP-16 Challenge To Jurisdiction != Obstruction.  
JP-17 Allegation In Case Record != Historical Fact Of Guilt.  
JP-18 Secret Adjudication Is Presumptively Incompatible With Fair Participation.  
JP-19 Emergency Action Before Hearing Creates A Duty For Prompt Review, Not A Permanent Exception To Hearing.  
JP-20 Charge Label != Substitute For Elements.  
JP-21 Presence != Meaningful Participation.  
JP-22 Advocacy Function != Ownership Of Outcome.  
JP-23 Need For Assistance != Automatic Loss Of Authorship.  
JP-24 Disclosure Duty != Unlimited Public Disclosure.  
JP-25 Evidence Protection != Permission To Make Evidence Unchallengeable.  
JP-26 Evidence Collection Should Be Capable Of Falsifying The Preferred Theory.  
JP-27 Interim Protective Order != Finding Of Liability Or Guilt.  
JP-28 Need To Preserve Process/Safety != Authority To Impose Maximum Restriction.  
JP-29 Judicial Independence != Universal Expertise.  
JP-30 Factual Finding != Legal Conclusion.  
JP-31 Consequence Severity Should Affect Required Epistemic Confidence.  
JP-32 Accusation != Evidential Presumption Of Guilt.  
JP-33 Silence != Proof Of Guilt.  
JP-34 Authority To Decide Creates Responsibility To Explain Consequential Decision.  
JP-35 One Case != One Indivisible Finding.  
JP-36 Victim Impact != Victim Authority To Set Punishment.  
JP-37 Past Offence != Automatic Present Dangerousness.  
JP-38 Finality Matters, But Finality != Infallibility.  
JP-39 Judicial Authority Must Remain Open To Correction Without Becoming Permanently Indeterminate.  
JP-40 Reversal Of Judgment != Automatic Repair Of All Consequences.  
JP-41 Judgment != Self-Executing Unlimited Authority.  
JP-42 Authority To Enforce Outcome A != Authority To Impose Unrelated Outcome B.  
JP-43 Order Exists != Compliance Was Possible.  
JP-44 Historical Custody != Continuing Judicial Authority.  
JP-45 Process History != Permanent Participant Identity.  
JP-46 Justice Delayed Can Become Continuing Unjustified Authority.  
JP-47 Speed != Permission To Remove Necessary Safeguards.  
JP-48 Ability To Pay != Right To Better Justice.  
JP-49 Open Justice != Universal Public Access To Every Sensitive Detail.  
JP-50 Case Closure != Finding That Allegation Was False.  
JP-51 Settlement != Judicial Finding Of Underlying Facts Unless Expressly Adjudicated.

---

## 83. Development result

The Judiciary now has a first coherent process lifecycle without assuming a conventional court hierarchy.

The architecture establishes:

**Matter → Standing → Jurisdiction → Case → Notice → Preliminary Review → Evidence/Disclosure → Adjudication → Finding → Consequence/Remedy → Appeal/Review → Enforcement → Closure/Historical Custody**

Source resolution after this document's initial creation materially changes the development order. **Court topology and prosecution architecture are not absent; both already have substantial source architecture.** The next step should therefore be a Judiciary source-resolution/reconciliation audit before any new derivation.

A genuine remaining question is **Epistemic Standards and Burdens of Proof**, but it should be developed only after reconciling Judiciary V2's existing burden/error architecture with the newer prosecution, evidentiary-completeness, fiduciary and MRT work. That question concerns how different judicial functions distinguish:
- suspicion;
- investigation threshold;
- prosecution threshold;
- interim protective threshold;
- civil liability;
- criminal guilt;
- continuing protective authority.

The existing Mirrored Reality Trees architecture provides a strong basis, but the standards should not be imported merely by copying historical phrases such as "balance of probabilities" or "beyond reasonable doubt" without deriving what epistemic function each standard is intended to perform.
