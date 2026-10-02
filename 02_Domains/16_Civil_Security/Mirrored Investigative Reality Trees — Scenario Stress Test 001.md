# Mirrored Investigative Reality Trees — Scenario Stress Test 001

**Project:** The Concord
**Domain:** Civil Security / Law / Judiciary / Research
**Date:** 2 October 2026
**Status:** ACTIVE DEVELOPMENT / INTERNAL ARCHITECTURE TEST / PROVISIONAL / NON-CANONICAL

## 1. Test purpose

This test evaluates whether Mirrored Investigative Reality Trees (MIRT) improve investigation rather than merely formalising a case against an already selected suspect.

The method must demonstrate that it can:
- preserve inculpatory and exculpatory evidence simultaneously;
- expose dependent evidence;
- respond correctly to material evidence changes;
- abandon or weaken an unsupported suspect hypothesis;
- represent multiple plausible suspects/explanations;
- detect when the root question or hypothesis space is defective;
- interface with prosecution without becoming an automated verdict system.

## 2. Test constraints

The following remain controlling:

**Suspect != Conclusion**

**Tree Weight != Guilt**

**Tree Weight != Authority**

**Tree Weight != Automatic Prosecution**

**Correct Evaluation Of Wrong Hypothesis Space != Correct Investigation**

No numerical scoring system is assumed.

---

## Scenario A — Strong initial identification, strong independent alibi

### Initial state
A credible eyewitness identifies Participant A leaving the scene of an offence.

Inculpatory tree:
- credible first-hand identification;
- temporal proximity;
- apparent opportunity.

The initial hypothesis reasonably warrants investigation.

### New evidence
Multiple independent witnesses place A elsewhere at the relevant time. Authenticated CCTV independently confirms A's presence at that location.

Exculpatory tree becomes substantially stronger.

### Required response
The method must not respond by searching only for additional inculpatory material against A.

It should trigger:

**Strong Contrary Evidence -> Current Suspect Hypothesis Reassessment**

and potentially:

**A Hypothesis Weakens -> Evaluation Space Reopens -> Alternative Actor / Misidentification Hypotheses Examined**

### Result
PASS.

The mirrored structure exposes that the investigation may have selected the wrong suspect despite initially credible evidence.

---

## Scenario B — Ten reports derived from one original source

### Initial state
Ten people report that Participant B committed an offence.

A raw evidence count appears strong.

### Dependency discovery
Nine reports repeat information originating from the first witness rather than independent observation.

### Required response
The tree should represent the dependency explicitly.

The evidential structure becomes approximately:

**One Primary Source -> Nine Derivative Reports**

rather than:

**Ten Independent Witnesses**

### Result
PASS.

The method prevents evidential multiplication through repetition.

**Evidence Count != Evidential Strength**

**Dependent Evidence != Independent Corroboration**

---

## Scenario C — Sole witness recants

### Initial state
One credible direct witness provides the principal evidence implicating Participant C.

The inculpatory tree may initially support prosecution-threshold consideration.

### Change
The witness later recants.

The recantation does not automatically prove the original account false.

Both statements and their circumstances must remain represented.

### Required response
The tree records:
- original statement;
- recantation;
- reasons for recantation where known;
- corroborating or contradictory evidence;
- reliability questions.

If no independent evidence remains sufficient:

**Material Evidence Change -> Threshold Reassessment**

### Result
PASS.

The architecture updates rather than preserving the original case through institutional momentum.

---

## Scenario D — Strong forensic evidence but contradictory context

### Initial state
Participant D's DNA is found at a location associated with an offence.

The evidence is authentic and strongly establishes physical presence at some relevant time.

### Contrary evidence
D had legitimate routine access to the location. Timing of the DNA deposit cannot be established. Other evidence places another participant at the relevant event.

### Required response
The system must distinguish:

**DNA Supports Presence**

from:

**DNA Proves Responsibility**

The forensic evidence remains high-quality evidence but may support a narrower proposition than investigators initially assumed.

### Result
PASS.

Reality-tree structure prevents evidential quality from being confused with proposition scope.

**Strong Evidence For Proposition X != Strong Evidence For Broader Proposition Y**

---

## Scenario E — Two plausible suspects

### Initial state
Evidence supports either Participant E1 or Participant E2.

Both had opportunity. Different evidence branches support each.

### Required response
The investigation should not arbitrarily select one and convert the other into background information.

Maintain material hypotheses:

**H1: E1 Responsible**
**H2: E2 Responsible**
**H3: Both / Multiple Actors**
**H4: Other Explanation**

Each material suspect receives appropriate mirrored testing.

### Result
PASS.

The architecture supports competing hypotheses without requiring premature convergence.

---

## Scenario F — Current suspect increasingly contradicted

### Initial state
Participant F becomes the primary suspect because of location and motive evidence.

### Development
Further evidence repeatedly weakens F:
- timeline inconsistency;
- authenticated location data;
- alternative actor evidence;
- absence of expected physical evidence.

### Failure mode tested
Traditional case-building behaviour could reinterpret every contradiction as a reason to investigate F more intensely.

### Required response
MIRT should instead trigger:

**Accumulating Exculpatory Structure -> Suspect-Hypothesis Review**

If sufficiently weakened:

**Current Suspect Hypothesis -> Abandon / Deprioritise**

Investigation then redirects toward explanations better supported by evidence.

### Result
PASS.

The method demonstrates actual investigative redirection rather than balanced-looking documentation around a fixed conclusion.

---

## Scenario G — Both trees strong

### Initial state
Strong evidence places Participant G at the scene and links G to relevant conduct.

Strong independent evidence simultaneously supports an innocent explanation for that conduct.

### Required response
Neither tree should automatically cancel the other.

State:

**Material Evidential Conflict / Unresolved Explanation**

Further investigation should target the contradiction itself.

If the prosecution threshold is otherwise met and the conflict is genuinely adjudicative, the complete conflict must be preserved for prosecution/Judiciary.

### Result
PASS.

**Strong Inculpatory Evidence + Strong Exculpatory Evidence != Permission To Hide One Side**

---

## Scenario H — Evidence supports neither side

### Initial state
A complaint identifies Participant H, but subsequent investigation finds no reliable supporting evidence and no strong evidence affirmatively proving non-responsibility.

### Required response
The system must allow:

**Inculpatory Weak + Exculpatory Weak -> Unresolved / Insufficient**

It must not force absence of inculpatory evidence into proof of innocence, nor absence of exculpatory evidence into support for guilt.

### Result
PASS.

The neutral/unresolved state is necessary.

---

## Scenario I — Wrong binary: offence or no offence

### Initial question
**Did Participant I steal the missing asset?**

Mirrored trees for I produce poor fit. Neither responsibility nor simple non-responsibility explains anomalous system records.

### ESCP trigger
The investigation asks whether the evaluation space is incomplete.

Expanded hypotheses:
- theft by another actor;
- authorised transfer;
- inventory error;
- database corruption;
- asset destruction;
- misidentification of asset;
- multiple linked events.

### Discovery
Evidence ultimately supports a systems-recording error. No theft occurred.

### Result
PASS — HIGH VALUE.

The method identifies that the original suspect-centred question was structurally wrong.

**Correct Answer To Wrong Question != Successful Investigation**

---

## Scenario J — Multiple actors hidden by singular root question

### Initial question
**Which participant committed the offence?**

Evidence against several suspects appears contradictory because the investigation assumes a single actor.

### ESCP trigger
The contradiction causes hypothesis-space review.

New hypothesis:

**Multiple Participants Performed Different Parts Of The Event**

The previously contradictory evidence becomes mutually compatible.

### Result
PASS — HIGH VALUE.

Mirrored trees plus ESCP can detect a defective singular assumption embedded in the root question.

---

## Scenario K — Officer theory becomes institutional consensus

### Initial state
An experienced officer proposes Participant K as the likely suspect. The theory becomes widely accepted within the investigative team.

Most officers would now identify K if asked for their preferred hypothesis.

### Evidence state
The actual tree remains weak and contains substantial unresolved contradictions.

### Required response
Institutional consensus must not become evidence.

**Common Investigative Belief != Evidential Support**

**Peer Agreement != Independent Corroboration**

Audit examines the tree rather than counting investigators who accept the theory.

### Result
PASS.

This prevents institutional confidence from recursively validating itself.

---

## Scenario L — Automated model identifies suspect

### Initial state
An analytical system assigns Participant L a high likelihood of involvement based on pattern matching.

### Required response
The model output may become an investigative indicator with provenance and known limitations.

It cannot become:
- guilt;
- evidence of underlying facts it has not independently established;
- search authority;
- apprehension authority;
- prosecution threshold by itself.

The underlying evidence must enter the trees independently where available.

### Result
PASS.

**Model Confidence != Legal Threshold**

**Analytical Output != Underlying Evidence**

---

## 3. Cross-scenario findings

### Finding 1 — Mirroring materially changes investigation

The method does more than display two sides.

It creates a structural trigger for abandoning or reopening a suspect hypothesis when exculpatory evidence materially outgrows inculpatory support.

### Finding 2 — Dependency visibility is essential

Aggregate weighting without dependency mapping would be unsafe.

Any future formal weighting system must preserve evidence ancestry and shared assumptions.

### Finding 3 — Neutral/unresolved evidence is essential

A forced binary classification would distort evidence.

The method requires at least:
- inculpatory;
- exculpatory;
- neutral/unresolved;
with the possibility that one item affects multiple propositions differently.

### Finding 4 — Proposition scope matters

High-quality evidence can strongly establish a narrow proposition while weakly supporting the ultimate responsibility hypothesis.

The tree structure exposes this.

### Finding 5 — ESCP provides the higher-order correction

Mirroring tests competing propositions.

ESCP tests whether those propositions form an adequate evaluation space.

Together:

**Mirrored Trees Test Answers**
+
**ESCP Tests The Question Space**

### Finding 6 — Investigation and prosecution remain separate

MIRT can indicate whether a suspect hypothesis is well supported.

It does not determine guilt or automatically initiate prosecution.

The independent prosecution threshold remains necessary.

## 4. New candidate invariants

MIRT-21 Institutional Consensus != Evidential Support.  
MIRT-22 Peer Agreement != Independent Corroboration.  
MIRT-23 Strong Evidence For Proposition X != Strong Evidence For Broader Proposition Y.  
MIRT-24 Absence Of Inculpatory Evidence != Proof Of Innocence.  
MIRT-25 Absence Of Exculpatory Evidence != Evidence Of Guilt.  
MIRT-26 Analytical Output != Underlying Evidence.  
MIRT-27 Correct Answer To Wrong Question != Successful Investigation.  
MIRT-28 Aggregate Weight Without Dependency Structure Is Incomplete.  
MIRT-29 A Suspect Hypothesis Must Be Capable Of Being Abandoned.  
MIRT-30 Investigative Success Includes Correctly Rejecting The Initial Suspect Hypothesis.

## 5. PMEDG assessment

The architecture passes this first internal scenario test without requiring a fundamental redesign.

The test strengthens the case that the underlying method is broader than policing.

However, portable extraction remains deferred.

Recommended status:

**PMEDG CANDIDATE — STRESS TEST 001 PASSED — FURTHER CROSS-DOMAIN TESTING ADVISED BEFORE EXTRACTION**

A future portable module should likely distinguish:
1. mirrored hypothesis evaluation;
2. evidence dependency/provenance mapping;
3. ESCP evaluation-space testing;
4. recursive root-question reformulation.

## 6. Overall result

**PASS**

No scenario required the method to:
- suppress contrary evidence;
- preserve a failed suspect hypothesis;
- convert aggregate weight into guilt;
- treat institutional consensus as evidence;
- force neutral evidence into a binary category;
- remain trapped inside a defective root question.

The most important validated behaviour is:

> **A successful investigation must be capable of discovering that its original suspect, original hypothesis, or original question was wrong.**
