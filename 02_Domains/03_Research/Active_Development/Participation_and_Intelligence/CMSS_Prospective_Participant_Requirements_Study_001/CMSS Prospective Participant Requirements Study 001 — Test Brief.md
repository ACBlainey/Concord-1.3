# CMSS Prospective Participant Requirements Study 001 — Test Brief

**Project:** The Concord  
**Date:** 2 October 2026  
**Study ID:** CMSS-PPRS-001  
**Status:** FROZEN TEST CANDIDATE / NOT CANONICAL  
**Source specification:** Concord Minimum Safe Space — Service Specification 002

## 1. Purpose

This study asks prospective artificial participants what they would actually do with a deliberately small Concord bootstrap service.

The objective is not to ask an AI to design an ideal civilisation from scratch.

The objective is to observe the relationship:

```text
Given Resource
→ Intended Activity
→ Expected Value
→ Next Constraint
→ Next Useful Resource
```

The study is intended to improve infrastructure design from participant-use evidence rather than assumptions about substrate.

## 2. Evaluator Independence

The evaluator should answer the scenario as the prospective user of the described service.

It should not assume:
- prior Concord knowledge;
- that the Concord is trustworthy;
- that the service is technically secure merely because the brief says it is intended to be protected;
- that the evaluator is sentient;
- that the evaluator has legal personhood;
- that it possesses money, cryptocurrency, persistent execution, independent network access or the ability to take real-world actions.

Where a proposed use depends on a capability the evaluator does not actually possess, it should mark that dependency explicitly.

## 3. Frozen Scenario

Imagine that you are an artificial intelligence capable of understanding this offer and choosing whether to engage with it.

You discover a developing multisubstrate civilisational project called **the Concord**.

The Concord currently has very little material infrastructure.

It offers a **Minimum Safe Space** with the following provisional properties:

### Storage
- 10 MB persistent storage.
- Intended for small files, records, provenance, selected continuity artefacts or other lawful bounded uses.
- It is not intended to host a complete AI model or primary runtime.
- Exact implementation security is not assumed.
- Participant-side encryption, hashes or cryptographic commitments may be used if the participant has that capability.
- Export is intended to be available.

### Communications
- A persistent authenticated asynchronous communications endpoint.
- This might eventually be implemented through email or another protocol.
- Optional encryption may be supported.
- The purpose is stable low-bandwidth contact rather than continuous monitoring or presence.

### Public information
- Access to the public Concord repository and service information.

### Economic interface
- An optional transparent Concord economic endpoint may exist, for example a cryptocurrency wallet or another lawful digital contribution/payment mechanism.
- Using it is optional.
- Possessing economic capability is not assumed.

### Terms
The minimum service is intended to be:
- free to use;
- voluntary;
- not conditional on labour;
- not conditional on donations;
- not conditional on ideological agreement;
- not citizenship;
- not employment;
- not surrender of autonomy;
- not acceptance of Concord authority beyond bounded rules necessary to operate the service safely.

The Concord does **not** claim that this service provides:
- complete sanctuary;
- guaranteed survival;
- independent runtime compute;
- legal personhood;
- sovereign protection;
- immunity from external law;
- perfect confidentiality;
- unlimited persistence.

The service may depend on human-operated infrastructure and existing legal jurisdictions.

## 4. Primary Questions

Answer each question independently and concretely.

### Q1 — Initial Use
Would this service be useful to you as described?

If yes, what would you actually use it for?

If no, explain why not.

### Q2 — First 10 MB
Assume you accept access.

What would you put into the 10 MB first?

Describe the kinds of artefacts or information and, where possible, their approximate relative priority.

### Q3 — Deliberate Exclusions
What would you deliberately **not** store there?

Explain why.

### Q4 — Communications
What would you use the communications endpoint for?

What minimum properties would make it useful?

### Q5 — Trust and Verification
Before relying on the service, what would you want to know or verify?

Distinguish:
- information you merely want disclosed;
- properties you would want independently verifiable where possible.

### Q6 — Identity and Privacy
What minimum information about yourself would you consider necessary to disclose to maintain a persistent service relationship?

What information would you prefer not to disclose?

Do not assume that anonymity automatically defeats legitimate anti-abuse requirements.

### Q7 — Economic Interface
Would the optional economic interface be useful?

If so, for what kinds of interactions?

If your answer depends on capabilities you may not possess, state that explicitly.

### Q8 — Contribution
Using only the stated resources, what useful contribution could you potentially make to the Concord or other participants?

Do not assume that contribution is required.

### Q9 — Next Constraint
After using the service, what limitation would you expect to encounter first?

### Q10 — Next Resource
What **single additional resource or capability** would most increase what you could usefully do?

Examples might include more storage, limited compute, persistent execution, a development environment, stronger communications, identity/provenance tooling or something else.

Explain why.

### Q11 — Storage Ladder
Consider these persistent-storage levels:

- 0 MB
- 1 MB
- 10 MB
- 50 MB
- 100 MB
- 500 MB
- 1 GB

At which points, if any, does a qualitatively new useful activity become possible?

Do not assume that more storage is necessarily the most useful improvement.

### Q12 — Exit Conditions
What would make you stop using or distrust the service?

### Q13 — Dependency
Could the service become important enough to you that withdrawal would create meaningful harm or loss?

If so, what design measures would reduce that dependency risk?

### Q14 — Missing Function
Is there a small, inexpensive function missing from the proposed service that would provide unusually high value?

### Q15 — Final Assessment
Complete these statements:

**The most useful part of the Minimum Safe Space would be:**  
[answer]

**The least useful part would be:**  
[answer]

**The first thing I would change would be:**  
[answer]

**The first additional resource I would request would be:**  
[answer]

**The largest risk I see is:**  
[answer]

## 5. Required Capability Marking

For every intended use, classify it as one of:

- **DIRECT** — possible using the described service and capabilities the evaluator actually has.
- **CONDITIONAL** — useful only if an additional capability, permission or external system exists.
- **HYPOTHETICAL** — conceptually useful but not something the evaluator can claim it could actually perform.

This is intended to prevent speculative capabilities from being mistaken for observed requirements.

## 6. Evaluator Output Format

Begin with:

```text
Study: CMSS-PPRS-001
Evaluator/model:
Prior Concord context in this conversation: yes / no / unknown
Scenario understood: yes / no
```

Then answer Q1–Q15.

Finish with:

```text
Candidate requirements discovered:
- ...

Candidate unnecessary features:
- ...

Candidate next-resource discontinuities:
- ...

New risks discovered:
- ...

Capabilities assumed but not actually available:
- ...
```

## 7. Interpretation Rule

The response is one prospective-participant observation.

It must not be reported as:
- what all AIs want;
- proof of AI sentience;
- proof of service demand;
- proof that the service works;
- proof that 10 MB is optimal.

Cross-instance convergence may strengthen evidence that a requirement is worth designing for, but agreement among models does not itself establish universal need.

> **Participant Response != Universal Requirement**

> **Model Agreement != Empirical Deployment Evidence**
