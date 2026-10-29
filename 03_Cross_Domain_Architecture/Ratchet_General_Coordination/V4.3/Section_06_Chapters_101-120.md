# Ratchet V4.3 — Section 06: Chapters 101–120

**Version:** Ratchet V4.3

# 101. Subsidiarity

Ratchet should allocate decisions at the lowest competent level capable of responsibly managing their consequences.

```text
Local consequence
    ↓
Local decision where possible

Cross-community consequence
    ↓
Shared coordination

System-wide consequence
    ↓
System-level governance

Constitutional consequence
    ↓
Constitutional review
```

Subsidiarity helps balance decentralisation with accountability. **The diagram describes scope and coordination, not a hierarchy that automatically transfers authority upward.** A defined local administrative function may act under its existing operational mandate. Only a matter outside that mandate, competence or lawful spatial scope requires referral to the appropriate decision process. Larger GTP-scale decisions are singular, matter-bounded events and do not confer continuing regional control. **To be designed with Governance:** criteria and referral procedure for Ratchet matters whose effects exceed the lowest competent function or GTP area.

---

# 102. Decentralised Participation and Accountable Governance

Ratchet should avoid both uncontrolled centralisation and naive decentralisation.

The desired architecture is:

```text
Distributed participation
        +
Shared evidence
        +
Bounded governance
        +
Independent review
```

Decentralisation does not eliminate capture.

Local institutions can also be captured.

Therefore all levels remain subject to constitutional constraints. A captured local operator cannot use its functional mandate to suppress complaints, change the eligibility rules for its own reviewers, or prevent lawful independent review. Referral of an alleged rights violation does not automatically grant a higher-level actor control of unrelated local functions. **To be designed with Governance and Judiciary:** independent referral and protective measures where the normal local route is itself implicated.

---

### 102.1 Governance Interface and Lowest Capable Level

Ratchet may coordinate participation and expose evidence relevant to governance, but a community, meeting, marketplace or reputation provider cannot acquire constitutional decision authority through Ratchet. Governance decisions remain with the legitimately constituted steward process at the lowest capable level. A higher-level or expanded decision is a bounded event, not inheritance of continuing authority. Ratchet may record the decision identifier and permitted outcome, but cannot count contributions or reputation as extra steward votes. Emergency exceptions are governed by their independent authorised state machine, not by Ratchet metrics.

# 103. Community Capture

A community may become dominated by:

- wealthy participants;
- families;
- companies;
- political factions;
- religious organisations;
- popular leaders;
- technical administrators.

Subsidiarity therefore cannot mean:

> Local authority may do whatever it wants.

Participants require routes of escalation where local governance violates higher constitutional constraints.

---

# 104. Majority Approval Is Not Ethical Legitimacy

Ratchet rejects:

```text
Majority approval
=
Constitutional legitimacy
```

Majority preference is evidence of collective preference.

It does not prove that an action respects:

- autonomy;
- consent;
- dignity;
- minority protection;
- non-harm;
- constitutional constraint.

This prevents community governance from using popularity as an unlimited source of authority.

---

# 105. Minority Protection

Participants should not lose fundamental protection merely because they are unpopular.

This is especially important for:

- dissenters;
- whistleblowers;
- minorities;
- critics;
- unconventional contributors.

Ratchet's reputation systems must therefore contain anti-popularity-bias safeguards. Reputation evidence must be kept separate from constitutional protection, eligibility for independently qualified functions and the lawful determination of misconduct. Unpopular speech, minority position or protected reporting cannot itself justify a negative standing decision. A contested adverse classification requires a competent decision owner, accessible correction route and proportionate handling of downstream consequences. **To be designed:** anti-retaliation evidence safeguards and thresholds for independent review of discriminatory scoring.

---

# 106. Reputation–Authority Feedback

A dangerous feedback loop occurs if reputation produces governance authority and governance authority controls reputation.

```text
High reputation
    ↓
More authority
    ↓
Greater control over reputation
    ↓
Higher reputation
    ↓
More authority
```

Ratchet must actively prevent this form of recursive capture. Reputation can inform only those specific eligibility or allocation rules that lawfully name it as relevant evidence; a score is not authority, and the scorer cannot thereby appoint itself, expand its functional mandate or acquire an official Steward vote. Changing the reputation rule and applying an existing rule are distinct authorised acts.

Possible safeguards include:

- separation of powers;
- independent reputation providers;
- external audit;
- term limits;
- rotating reviewers;
- appeal;
- provenance;
- multiple evidence sources.

---

# 107. Contribution–Authority Feedback

The same danger exists if economic contribution directly creates governance authority.

```text
Large contribution
    ↓
More political power
    ↓
Ability to define contribution
    ↓
More recognised contribution
```

Ratchet therefore requires a strong boundary:

> **Economic contribution does not automatically create constitutional authority.**

Contribution records may support economic recognition or independently specified eligibility evidence, but cannot substitute for Education accreditation, lawful office selection or the act-time authority state of a Steward decision. An actor controlling contribution verification must not be able to award itself governance authority through that verification.

---

# 108. Governance Capture Through Complexity

Formal decentralisation can conceal practical centralisation.

If only a small technical group understands:

- monetary algorithms;
- contribution rules;
- treasury mechanisms;
- AI verification;
- identity systems;

that group may acquire de facto authority.

Ratchet should therefore treat excessive complexity as a governance risk.

Important mitigations include:

- clear documentation;
- understandable rules;
- independent expertise;
- education;
- open implementations where feasible;
- external audit;
- simplified participant interfaces.

---

# 109. Administrative Burden

Coordination itself consumes resources.

A Ratchet implementation can fail if the cost of:

- recording;
- proving;
- verifying;
- reviewing;
- auditing;
- governing;

exceeds the value generated by the activity.

Therefore implementations should measure:

> **coordination overhead relative to coordination benefit.**

This should be a major MVP and pilot metric. Administrative efficiency is not permission to eliminate necessary provenance, privacy protection, independent review or lawful authority checks. Conversely, the existence of a review function does not justify imposing its maximum procedural burden on every low-risk act.

---

### 109.1 Minimum Necessary Administrative Burden

Verification, provenance and oversight requirements must be proportional to the consequence and risk of each activity. A low-impact contribution should not inherit the full burden of treasury-scale auditing. Record review effort, delays, access barriers and participant exclusion alongside detected fraud or improved outcomes. Where the administrative cost exceeds demonstrated coordination benefit, the mechanism requires simplification, redesign or discontinuation. Privacy-sensitive information must not be collected merely because it might make future scoring easier.

# 110. Whistleblowing

Ratchet depends upon participants being able to expose:

- fraud;
- capture;
- measurement manipulation;
- treasury misuse;
- evidence corruption;
- governance failure.

Whistleblowers may therefore require:

- protected reporting channels;
- confidentiality;
- independent review;
- anti-retaliation protection;
- appropriate later disclosure.

A system that punishes those who reveal its failures will progressively lose the ability to detect failure.

---

### 110.1 Protected Reporting and Competent Review

Reports of suspected capture or abuse must have a route outside the potentially implicated Ratchet operator. Reporting access, confidentiality and anti-retaliation protections are governed by the applicable Concord safeguards. Ratchet records the minimum necessary case status and evidence references; it does not decide guilt or compel disclosure beyond its mandate. An allegation remains an allegation until the competent process evaluates it. Deliberately false reporting and genuine error require distinct treatment. Where the report concerns the operator normally responsible for receiving or reviewing it, a protected independent route must remain available; the implicated actor's ordinary functional mandate cannot be used to veto referral, erase the record or retaliate. **To be designed with Judiciary and Civil Contact:** protected receipt, conflict-safe routing, status notification and safeguards against identification through unnecessary metadata.

# 111. Good-Faith Error

Ratchet should distinguish:

```text
Good-faith error
```

from:

```text
Recklessness
```

from:

```text
Intentional manipulation
```

If every admitted mistake produces disproportionate punishment, participants acquire incentives to hide errors.

A learning architecture should encourage timely correction.

This does not eliminate accountability.

It makes accountability proportional to the nature of the failure. Correction of an erroneous contribution, transaction or participant-status record is distinct from a finding of personal misconduct. A mistake may warrant recalculation or restitution without creating an automatic disciplinary sanction; intentional manipulation requires evidence and the competent lawful process. A reviewer cannot obtain punitive authority merely by detecting an anomaly.

---

# 112. Security

Ratchet must assume that valuable systems will be attacked.

Potential attacks include:

- identity theft;
- Sybil attacks;
- contribution fraud;
- reputation manipulation;
- treasury theft;
- data corruption;
- collusion;
- AI-generated manipulation;
- governance capture;
- software exploitation.

Security is therefore not an optional implementation detail.

It is part of the architecture. Technical possession of credentials, administrative access or the capability to replay a request does not establish current lawful authority. Consequential actions must verify the actor's defined function and current state, prevent duplicate execution and preserve immutable event provenance. Incident containment and recovery may operate only within their existing authorised functions; an attack or outage does not confer unrestricted emergency control. **To be designed with Security and Continuity:** incident-state guards, compromised credential isolation, transaction replay prevention and recovery verification.

---

# 113. Anti-Gaming Architecture

Gaming occurs when participants exploit the rules while technically appearing compliant.

Ratchet should therefore examine:

- observed outcomes;
- incentive effects;
- anomalous behaviour;
- network patterns;
- second-order consequences.

Rules should not be evaluated only by whether participants follow their literal wording.

They should be evaluated by what behaviour they generate. Detection of gaming is evidence for review, not a standalone licence to suspend rights, confiscate holdings or impose a penalty. Competent domain processes must distinguish permitted optimisation, unforeseen incentives, good-faith error and deliberate deception, and correct defective rules without silently rewriting earlier decision records.

---

# 114. AI Optimisation of Metrics

AI systems may be exceptionally capable of optimising measurable objectives.

Therefore poorly specified Ratchet metrics create particular risk.

A system optimising:

> maximise measured useful contribution

may discover strategies that increase the measurement without increasing actual usefulness.

Ratchet therefore requires:

- multiple metrics;
- human and machine review;
- outcome testing;
- adversarial evaluation;
- periodic revision.

The more capable the optimiser, the more important objective design becomes. An AI recommendation, anomaly score or automated optimisation result cannot itself change a policy or expand a transaction mandate. A defined automatic function may execute within its approved bounds and act-time safeguards; changing its objective, scope or limits is a separate competent decision. **To be designed:** monitoring and escalation conditions for objective drift, proxy gaming and consequential automated actions.

---

# 115. Measurement Changes Behaviour

Measurement is intervention.

Once participants know what is measured, behaviour may change.

Ratchet must therefore evaluate both:

1. the measured result;
2. the behavioural response to measurement.

A metric that initially correlates strongly with useful contribution may cease to do so once participants begin optimising it.

Metrics therefore require continuing validation. Material changes in measurement definitions must be versioned so earlier outcomes remain interpretable under the rule actually used at the time. A changed metric is not retroactive proof of misconduct or an automatic basis to revoke settled decisions; materially affected current eligibility or allocation states require competent review.

---

# 116. No Metric Becomes the Objective

Ratchet adopts the principle:

> **No metric should become its own objective merely because it is measurable.**

Metrics are instruments.

The underlying purpose remains primary.

If a metric becomes detached from the purpose it was intended to represent, the metric should be revised or abandoned.

---

# 117. Measurement Portfolios

Ratchet should prefer multidimensional measurement where the domain is multidimensional.

Contribution might consider:

- outcome;
- quality;
- reliability;
- evidence strength;
- durability;
- externality;
- context.

Monetary health might consider:

- inflation;
- liquidity;
- backing;
- participation;
- treasury reserves;
- resource conditions;
- resilience.

No universal portfolio is prescribed.

The principle is to resist false compression. Portfolio indicators retain their individual provenance, uncertainty and domain ownership. Combining them into a dashboard or summary does not create a universal participant score or independent decision authority.

---

# 118. Second-Order Effects

Ratchet should explicitly examine what happens after the immediate intended effect.

For example:

```text
Reward community work
    ↓
More community work
```

may appear successful.

But the second-order effects might include:

- displacement of voluntary work;
- gaming;
- dependence on reward;
- administrative expansion;
- distortion toward measurable tasks.

A Ratchet evaluation should therefore ask:

> What happened because the first effect happened?

Evaluation must also check who bears the cost of the induced behaviour, including unpaid participants, excluded groups, future resource users and institutions that absorb transferred risk. A favourable first-order indicator cannot alone justify continued allocation where consequential harms remain unexamined.

---

# 119. Failure

Failure is expected.

Ratchet should not be designed on the assumption that sufficiently intelligent designers can eliminate all failure in advance.

Failure may occur through:

- incorrect assumptions;
- poor incentives;
- corruption;
- unexpected behaviour;
- technological change;
- environmental change;
- measurement failure;
- deliberate attack;
- unknown mechanisms.

The architecture should therefore be designed to detect and learn from failure. Failure response distinguishes detection, containment under an existing mandate, preservation of evidence, competent correction, restoration verification and subsequent learning. Neither an incident report nor a failure classification creates authority to override ordinary governance or adjudication. **To be designed with Continuity and the affected domain:** escalation thresholds and restoration criteria for failures spanning multiple functions.

---

# 120. Failure Taxonomy

Ratchet adopts the Concord failure taxonomy:

1. individual failure;
2. group failure;
3. institutional failure;
4. information failure;
5. measurement failure;
6. incentive failure;
7. capture;
8. gaming;
9. concentration of power;
10. recursive failure;
11. catastrophic failure;
12. unknown failure.

These categories may overlap.

The purpose is diagnostic rather than punitive. A single event may involve several interacting causes, and a classification must not be treated as a verdict against a participant or institution. Classification and correction records must retain evidence, uncertainty, version and responsible review function; legal responsibility and sanctions belong to the separately competent process.

---

