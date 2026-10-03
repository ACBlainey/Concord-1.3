# Participant-Directed Diagnostic Testing — Risk-Banded Access and Pathway Review 001

**Project:** The Concord Framework  
**Date:** 3 October 2026  
**Status:** ACTIVE HEALTH DEVELOPMENT / PROVISIONAL / NON-CANONICAL / SPECIALIST VALIDATION REQUIRED  
**Domain:** Health  
**Depends on:** Health Core Architecture 001 / Health Service Topology and Participant-Directed Access 001 / Smart Diagnostic Navigation and Reality-Tree Health Specification 001  
**Primary interfaces:** Professional competence / Health records / Resource coordination / Law / Safety

## 1. Purpose

Participant-directed Health access should extend beyond information and referral to reasonable access to diagnostic evidence.

Where a participant's symptoms, observations or diagnostic-navigation result identify a question that can appropriately be investigated by a low-risk diagnostic test, access should not ordinarily require an unrelated professional gatekeeper merely to authorise the test.

> **Access To Diagnostic Evidence != Requirement For Prior Doctor Permission**

This principle is bounded by the actual risks, limitations, resource consequences and interpretive requirements of the diagnostic pathway.

## 2. Core rule

The access burden should scale with the material risk and complexity of the proposed diagnostic act.

> **Diagnostic Gatekeeping Should Follow Risk, Not Professional Tradition**

A test should not require a clinician merely because historical service design placed clinicians upstream of diagnostics.

Conversely, participant autonomy does not require unrestricted access to tests whose use can itself create material harm.

## 3. Diagnostic access classes

A provisional risk-banded model:

### D0 — Participant observation / non-invasive self-measurement

Examples in principle include symptom recording and ordinary measurements obtainable without material intervention.

Default: direct participant access.

### D1 — Low-risk diagnostic testing

Tests with low direct physical risk and sufficiently bounded collection requirements may ordinarily be participant-initiated.

The participant may arrive through:
- Smart Diagnostic Navigation;
- self-referral;
- continuing monitoring;
- a professional recommendation;
- another legitimate Health route.

Default: direct access subject to test-specific suitability and ordinary service constraints.

### D2 — Low physical risk but clinically/pathway-sensitive testing

Some tests may be physically low-risk yet require stronger pre-test checks because results are difficult to interpret, false positives can create consequential cascades, prerequisites matter, or a different test is materially more appropriate.

Default: bounded automated/pathway review; professional consultation available where unresolved.

### D3 — Materially risk-bearing diagnostics

Tests involving material exposure, invasiveness, physiological risk, sedation, contrast agents, ionising radiation, or other significant test-specific hazard require a pre-test appropriateness and safety review.

Examples may include particular X-ray, CT or invasive diagnostic pathways depending on the actual procedure.

Default: **review required, doctor not automatically required.**

### D4 — High-consequence or specialist-controlled diagnostic procedure

Where safe performance requires specialist clinical judgement, intervention capability, consequential consent, or management of substantial risk, professional involvement is required according to validated specialist rules.

The exact placement of real tests into these bands must be determined by validated Health knowledge, not by this architecture.

## 4. Low-risk participant-initiated pathway

A participant may begin:

**Symptoms/Concern**
→ Smart Diagnostic Navigation / Reality Tree
→ candidate pathology or unresolved branch
→ diagnostic question
→ low-risk relevant test
→ participant self-request
→ test
→ result returned to participant Health record
→ Reality Tree updated
→ reassurance / monitoring / further test / generalist / specialist route.

The system should explain:
- why the test may be useful;
- what question it addresses;
- what it can and cannot establish;
- material preparation requirements;
- likely next routes for different result classes.

> **Test Availability != Test Necessity**

The participant remains free to seek professional advice before testing.

## 5. Potentially harmful test pathway

Where the proposed test itself carries material risk, the system should not simply accept or reject the participant request.

It should perform a bounded pathway review.

Review inputs may include:

- presenting symptoms;
- duration/progression;
- relevant Reality Tree branches;
- proposed diagnoses;
- evidence already obtained;
- urgency;
- relevant participant characteristics;
- contraindications;
- prior similar tests/exposures;
- available safer alternatives;
- whether the proposed test can answer the actual diagnostic question;
- whether another test should precede it.

The review asks:

> **Given the represented clinical question, is this a proportionate and appropriate diagnostic pathway, or is another route materially preferable?**

## 6. Automated review where sufficient

The pathway review need not automatically require a doctor.

Where validated rules and available evidence are sufficient, a bounded diagnostic system may determine that:

- the test is appropriate;
- a lower-risk test should occur first;
- prerequisite information is missing;
- the requested test does not address the represented question;
- professional review is needed;
- the situation requires urgent/emergency assessment.

Thus:

> **Review Required != Doctor Required**

and:

> **Professional Involvement Should Follow Need For Professional Judgement, Not Administrative Convention**

## 7. Professional review when materially needed

A generalist, radiologist, specialist or other appropriately competent professional may enter where:

- symptoms/evidence are ambiguous;
- test selection is uncertain;
- contraindication assessment requires clinical judgement;
- multiple pathways are materially plausible;
- participant reassurance or explanation is requested;
- risk-benefit balance is not safely resolvable by validated automated rules;
- specialist examination is needed before testing;
- the diagnostic procedure itself requires professional authority/competence.

The professional is solving an actual clinical uncertainty, not merely functioning as a permission token.

## 8. Confirmation of correct pathway

For risk-bearing diagnostics, the review should distinguish:

1. **Diagnostic question** — what are we trying to learn?
2. **Candidate explanation(s)** — why might that question matter?
3. **Test capability** — can the proposed test materially answer it?
4. **Test risk** — what harm can the diagnostic act itself create?
5. **Alternative pathway** — is a safer/equivalent or prerequisite test available?
6. **Participant-specific suitability** — are relevant contraindications or modifiers present?
7. **Consequence of delay** — would additional review itself create material risk?

This prevents both unrestricted hazardous testing and unnecessary professional gatekeeping.

## 9. Reality Tree integration

A test should normally attach to a diagnostic branch or discrimination question.

Example grammar:

**Symptoms**
→ Branch A / Branch B / Branch C
→ unresolved discriminator Q
→ Test T can materially distinguish A from B
→ test-risk review
→ T authorised/requested
→ result
→ branch update.

This gives the participant and later professionals a provenance-visible answer to:

> **Why was this test performed?**

Tests may also be appropriate for screening or monitoring rather than a symptom-derived pathology branch; those purposes should be represented explicitly rather than forced into a diagnostic-tree fiction.

## 10. Results belong in the participant Health pathway

Results should return promptly to the participant's longitudinal Health view, subject only to narrowly justified exceptions.

The result should include:
- raw/primary result where appropriate;
- validated interpretation;
- reference/context information;
- uncertainty/limitations;
- test provenance;
- reason/pathway;
- suggested next routing states.

> **Diagnostic Result != Provider Property**

A participant should not need another appointment merely to gain ordinary access to their own result.

## 11. Interpretation and consequential findings

Direct result access does not mean every result is self-explanatory.

Where interpretation is complex or a result may imply serious consequences, the system should provide:
- accessible explanation;
- uncertainty;
- likely differential implications;
- recommended professional route;
- urgent escalation where validated;
- opportunity for human discussion.

The participant may choose professional support even where it is not mandatory.

> **Participant Access To Result != Participant Left Without Interpretive Support**

## 12. False positives, incidental findings and cascade risk

Low physical risk does not mean zero consequential risk.

Some tests can produce:
- false positives;
- uncertain findings;
- incidental findings;
- unnecessary follow-on investigation;
- anxiety;
- inappropriate treatment cascades.

Risk classification should therefore consider both direct test harm and reasonably foreseeable diagnostic cascade harm.

This does not justify blanket gatekeeping. It justifies proportionate explanation and pathway review.

## 13. Resource constraints

A test may be physically low-risk but materially scarce or resource-intensive.

Scarcity may require scheduling, prioritisation or allocation rules.

> **Low Clinical Risk != Unlimited Resource Availability**

Scarcity rules must remain transparent and must not be disguised as clinician gatekeeping.

Ability to pay must not silently become greater fundamental standing.

## 14. Participant refusal and alternatives

A participant may decline a recommended test.

The system should explain:
- what uncertainty remains;
- what risk the test was intended to investigate;
- available alternatives;
- what changes should prompt reassessment.

> **Refusal Of Test != Automatic Refusal Of Care**

Other legitimate routes remain available where possible.

## 15. Repeated testing

Participant-directed access should not mean uncontrolled repeated exposure or redundant resource use.

The system should recognise:
- recent equivalent tests;
- cumulative exposure where relevant;
- whether material state has changed;
- whether repetition can answer a new question;
- whether previous result remains valid for the current purpose.

For materially harmful testing:

> **Prior Test Access != Automatic Authority For Repetition**

## 16. Screening

Screening is distinct from symptom-driven diagnostic testing.

Screening pathways require their own evidence about:
- target population;
- benefit;
- false-positive/false-negative burden;
- interval;
- downstream consequences;
- participant preference.

The Health front door may offer validated screening directly without requiring a GP gate where professional mediation adds no necessary function.

## 17. Diagnostic-service professional role

Diagnostic professionals remain substantive participants in Health.

Their functions may include:
- safe test performance;
- protocol selection;
- interpretation;
- quality assurance;
- resolving ambiguous pathway questions;
- modifying or refusing an unsafe/inappropriate procedure;
- escalating unexpected findings.

Their professional authority is bounded to those functions.

> **Diagnostic Professional != General Owner Of Patient Care**

## 18. Contextual record access

A diagnostic service receives only the record context necessary to:
- establish the diagnostic question;
- assess test safety/suitability;
- perform the test;
- interpret the result;
- route material findings.

The diagnostic episode opens a bounded contextual wrapper.

When the diagnostic function ends, ordinary active access ends.

> **Diagnostic Episode != Permanent Record Access**

## 19. Emergency findings

If a diagnostic service discovers an immediate serious threat, it may activate the appropriate bounded emergency Health route.

This does not retrospectively create general authority over the participant.

## 20. Safety architecture

The participant-directed diagnostic system must prevent two opposite failures:

### Over-gatekeeping
Safe useful evidence is withheld unless a professional performs a function that adds no material safety or clinical value.

### Under-gatekeeping
Materially harmful tests are provided without checking appropriateness, contraindications or safer pathways.

The target is:

> **Minimum Necessary Gatekeeping For The Actual Risk**

## 21. Compact topology

**Participant concern**
→ Reality-Tree diagnostic navigation
→ diagnostic question
→ candidate test
→ test risk/pathway classification

If low risk:
→ participant request
→ test
→ result
→ tree update / next route

If material test risk:
→ bounded symptoms + diagnosis + pathway review
→ automated approval where validated and sufficient
OR
→ professional review where judgement is materially required
→ test / alternate test / further assessment
→ result
→ tree update / next route.

## 22. Core invariants

> **Access To Diagnostic Evidence != Requirement For Prior Doctor Permission**

> **Diagnostic Gatekeeping Should Follow Risk, Not Professional Tradition**

> **Review Required != Doctor Required**

> **Test Availability != Test Necessity**

> **Professional Involvement Should Follow Need For Professional Judgement, Not Administrative Convention**

> **Diagnostic Result != Provider Property**

> **Participant Access To Result != Participant Left Without Interpretive Support**

> **Refusal Of Test != Automatic Refusal Of Care**

> **Low Clinical Risk != Unlimited Resource Availability**

> **Diagnostic Episode != Permanent Record Access**

> **Minimum Necessary Gatekeeping For The Actual Risk**

## 23. Development dependencies

Further work must establish:
- validated diagnostic-test risk taxonomy;
- biological test catalogue and specialist pathways;
- digital-substrate diagnostic equivalents;
- radiation/exposure accounting where applicable;
- invasive-test consent rules;
- diagnostic knowledge governance;
- screening architecture;
- diagnostic service registry and competence;
- result communication standards;
- incidental-finding pathways;
- Health-record wrapper implementation.
