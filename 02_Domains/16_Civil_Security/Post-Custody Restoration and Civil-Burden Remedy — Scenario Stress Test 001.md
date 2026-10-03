# Post-Custody Restoration and Civil-Burden Remedy — Scenario Stress Test 001

**Project:** The Concord
**Domain:** Civil Security / Law / Judiciary / Historical / Civil Contact
**Date:** 3 October 2026
**Status:** ACTIVE DEVELOPMENT / POST-CUSTODY REMEDY STRESS TEST / PROVISIONAL / NON-CANONICAL

## 1. Test purpose

This test examines **Post-Custody Restoration and Civil-Burden Remedy — Operational Architecture 001** against difficult operational cases.

The test asks whether the mechanism can:

- restore known consequences automatically;
- recognise real harm without requiring proof of misconduct;
- distinguish baseline burden from consequential loss;
- handle mixed causation;
- avoid disproportionate bureaucracy;
- resist fraudulent or exaggerated claims without treating every claimant as suspect;
- handle very large losses;
- detect incomplete restoration;
- propagate correction across dependent systems;
- preserve Historical provenance without continuing stigma;
- avoid incentives that weaken custody thresholds or remedy fairness.

---

## 2. Scenario A — trivial lawful custody burden

A participant is lawfully held for ten minutes while an immediate identity ambiguity is resolved. No property is retained, no service is interrupted, and no measurable consequential loss occurs.

### Analysis

A full compensation proceeding would itself create unnecessary administrative burden.

Release/status restoration should occur automatically.

A formal civil-burden claim need not be opened merely because any custody event occurred.

The architecture already allows materiality thresholds.

### Result

**PASS.**

Candidate principle:

**Custody Event != Mandatory Monetary Remedy Event**

The participant retains challenge rights if something material occurred that the system did not detect.

---

## 3. Scenario B — small objectively measurable loss

A participant is lawfully detained for several hours and released without charge. They miss a prepaid transport connection with a known modest replacement cost.

### Analysis

The loss is direct, readily evidenced and low-complexity.

Requiring adversarial proof or litigation would cost more than the dispute.

A streamlined/automatic remedy route is appropriate where system records and participant-provided evidence establish the loss.

### Result

**PASS.**

**Low-Complexity Known Loss -> Low-Friction Remedy**

---

## 4. Scenario C — very large consequential loss

A participant is lawfully detained and released without prosecution. During custody, a time-critical commercial transaction collapses, producing a claimed very large financial loss.

### Analysis

The architecture should not automatically pay every downstream claimed consequence merely because custody occurred.

Large or remote consequential loss requires stronger causal examination:

- was the loss reasonably attributable to custody?
- was the transaction genuinely time-critical?
- could reasonable mitigation have reduced loss?
- were independent causes material?
- is the claimed amount evidenced?
- is some loss speculative rather than realised?

The participant need not prove police wrongdoing, but must establish the claimed consequence sufficiently for the remedy being sought.

### Result

**PASS WITH PROPORTIONAL EVIDENCE REQUIREMENT.**

**No-Fault Remedy != No Causation Requirement**

---

## 5. Scenario D — mixed causation

A participant loses employment after lawful custody. The employer cites both the missed shift and a pre-existing performance problem.

### Analysis

Custody is one causal factor but not necessarily the entire cause.

The remedy system should be capable of partial/qualified causal allocation rather than all-or-nothing reasoning.

### Result

**PASS.**

**Mixed Causation != Zero Remedy Or Total Remedy By Default**

---

## 6. Scenario E — participant fails to mitigate an easily reversible loss

After release, Concord immediately restores a credential and notifies the participant. The participant knowingly continues to act as though the credential remains unavailable and later claims prolonged losses.

### Analysis

The participant should not be expected to perform the civilisation's restoration work.

But once restoration is genuinely completed and communicated, avoidable later loss may no longer be attributable to custody.

### Result

**PASS.**

**Civil Duty To Restore != Unlimited Liability For Independently Avoidable Later Loss**

---

## 7. Scenario F — system says restoration complete but hidden dependency remains

A participant's primary status is restored. An obscure downstream employment eligibility cache still contains the custody restriction and silently rejects an application.

Neither the participant nor the release system initially knows the dependency exists.

### Analysis

This is a correction-propagation failure and an ESCP problem.

“Restoration complete” can only mean restoration complete within the represented dependency space.

Later discovery should reopen the restoration state, correct the dependency, reassess consequential loss and preserve prior provenance.

### Result

**PASS WITH COMPLETENESS REFINEMENT.**

**Known Dependencies Restored != All Dependencies Restored**

**Restoration Complete State Must Be Reopenable On New Evidence**

---

## 8. Scenario G — Historical record is accurate but search presentation is stigmatic

Historical correctly preserves that the participant was detained and released without charge. A general participant lookup prominently displays “detained” while the no-charge/release context is hidden behind deeper access.

### Analysis

The historical facts are accurate but their presentation creates a misleading current implication.

Historical preservation does not justify decontextualised adverse signalling.

### Result

**PASS WITH PRESENTATION REQUIREMENT.**

**Factually Accurate Record Presentation Can Still Be Contextually Misleading**

Relevant current/disposition context must accompany consequential exposure where legitimate access exists.

---

## 9. Scenario H — repeated short lawful custody

A participant experiences five short individually lawful detentions over six months because a system repeatedly generates ambiguous identity matches. Each event alone falls below the ordinary material-remedy threshold.

### Analysis

Independent event thresholds can hide cumulative harm.

The remedy system should be able to aggregate related events where repeated civil burdens arise from a common or recurring mechanism.

### Result

**PASS WITH AGGREGATION REQUIREMENT.**

**Individually Minor Repeated Burdens May Become Material In Aggregate**

This should also generate a system-reliability signal.

---

## 10. Scenario I — inaccurate but good-faith claim

A participant claims six hours of lost work. Employment records establish only four hours were actually lost. The discrepancy appears to be an honest mistake.

### Analysis

The system should correct the amount without treating ordinary inaccuracy as fraud.

### Result

**PASS.**

**Claim Error != Fraud**

---

## 11. Scenario J — deliberate exaggerated claim

A participant knowingly submits fabricated invoices and false employment records to increase compensation.

### Analysis

The remedy process is rights-protective, not evidence-blind.

Claims may be verified proportionately.

Fabricated evidence can be rejected and may itself create a separate legal issue under applicable Law.

The legitimate underlying remedy should not necessarily disappear merely because one component was fraudulent unless Law establishes that consequence.

### Result

**PASS.**

**Fraudulent Remedy Evidence != Automatic Erasure Of Legitimate Underlying Harm**

This prevents the remedy process from becoming punitive beyond its function.

---

## 12. Scenario K — intrusive verification of a modest claim

To verify a small lost-income claim, the system requests years of banking, employment and private financial records.

### Analysis

Rejected as disproportionate.

CIBB/minimum-necessary access applies to remedy verification as elsewhere.

### Result

**PASS.**

**Remedy Verification != General Financial Inspection Authority**

---

## 13. Scenario L — automatic baseline payment masks larger harm

A participant receives an automatic baseline no-fault remedy. The system marks the matter complete even though custody caused substantial additional caregiving costs.

### Analysis

Baseline remedy should not silently close the consequential-loss route.

### Result

**PASS.**

**Baseline Remedy != Full And Final Remedy By Default**

The participant should be informed of the route for additional material loss.

---

## 14. Scenario M — baseline remedy offered as waiver

A participant is told they can receive automatic compensation only if they waive any challenge to custody legality or treatment.

### Analysis

Rejected by the architecture.

Routine burden allocation and legal accountability are separate.

### Result

**PASS.**

**Routine Remedy != Purchase Of Rights Waiver**

---

## 15. Scenario N — no-charge release but immediate unrelated lawful restriction

A participant is released without prosecution for incident A. A separate independent lawful order concerning incident B restricts travel.

### Analysis

Custody-derived travel restriction must sunset, but the independent restriction may remain.

The participant-facing system must distinguish the authority provenance so that “restriction remains” does not conceal a failed custody sunset.

### Result

**PASS.**

**Same Practical Restriction != Same Authority Provenance**

---

## 16. Scenario O — property cannot be restored

Property lawfully taken into custody is accidentally destroyed while held. It cannot be physically returned.

### Analysis

Direct restoration is impossible.

Replacement, compensation or another equivalent remedy becomes appropriate, with separate accountability if negligence/system failure occurred.

### Result

**PASS.**

**Impossible Restoration -> Equivalent Remedy Where Reasonably Available**

---

## 17. Scenario P — lost time cannot be restored

A participant misses the final hours with a dying relative because of lawful custody that later ends without prosecution.

### Analysis

Some harms cannot meaningfully be priced or restored.

A monetary remedy may be possible but cannot be represented as reversing the harm.

The system should distinguish:

- compensable economic loss;
- practical restorative support;
- acknowledgement/correction;
- irreducible harm.

### Result

**PASS WITH REMEDY-TYPE REFINEMENT.**

**Compensation != Erasure Of Irreversible Harm**

The record should not falsely classify payment as complete restoration of what cannot be restored.

---

## 18. Scenario Q — remedy delay creates new loss

A custody-derived credential remains blocked for two weeks because the restoration queue is slow. The delay causes additional lost work.

### Analysis

Post-release administrative delay can itself become a new source of civilly caused harm.

The remedy assessment should include losses caused by failed/delayed restoration, not freeze causation at the moment of physical release.

### Result

**PASS.**

**Remedy Process Can Itself Create Remediable Harm**

---

## 19. Scenario R — participant cannot engage with remedy process

A participant is ill, disabled, digitally disconnected or otherwise temporarily unable to respond to Civil Contact after release.

### Analysis

Automatic restoration should proceed without requiring response where authority is clear.

A remedy offer should not be falsely closed merely because the participant cannot immediately engage.

Supported decision-making/representative routes may be required.

### Result

**PASS.**

**Participant Non-Response != Restoration Waiver**

---

## 20. Scenario S — AI participant continuity loss

A digital participant is lawfully isolated during investigation and later released without prosecution. No physical harm occurs, but service commitments fail, compute continuity is disrupted and a time-sensitive process state cannot be reconstructed.

### Analysis

The substrate-neutral architecture correctly identifies real harm despite absence of biological confinement.

Remedy should examine actual protected functions and losses.

### Result

**PASS.**

**No Biological Harm != No Custodial Harm**

---

## 21. Scenario T — remedy algorithm undervalues unusual participant circumstances

An automated baseline system calculates a standard amount but fails to represent a participant's unusual dependency structure.

### Analysis

Automation may handle ordinary baseline cases but cannot define the complete remedy evaluation space.

ESCP applies.

The participant must be able to expose unrepresented material dimensions.

### Result

**PASS.**

**Automated Remedy Model != Complete Remedy Evaluation Space**

---

## 22. Scenario U — remedy assessor has incentive to minimise payouts

The same unit's performance metric rewards low remedy expenditure.

### Analysis

This creates structural conflict with fair assessment.

### Result

**PASS.**

**Remedy Quality != Minimum Remedy Expenditure**

The institutional design should measure correctness, timeliness, restoration completeness and participant/system outcomes rather than simply cost suppression.

---

## 23. Scenario V — custody unit pays remedy from its own fixed operating budget

Large remedy payments reduce resources available for lawful safety work, creating pressure on staff to deny legitimate claims.

### Analysis

Direct fiscal coupling can distort both remedy and operational decisions.

The architecture already separates custody authority from remedy financial incentive.

### Result

**PASS WITH FUNDING-DESIGN REQUIREMENT.**

Funding architecture should avoid making fair remedy compete directly with immediate operational safety capacity.

---

## 24. Scenario W — participant receives remedy, later new evidence changes case status

A participant is released without prosecution and receives no-fault remedy. Months later new evidence independently satisfies prosecution threshold.

### Analysis

The earlier remedy reflected the earlier custody burden and state at that time.

Later prosecution does not automatically make the prior remedy fraudulent or retroactively erase the burden actually borne.

Any genuinely false claim remains separately reviewable.

### Result

**PASS.**

**Later Prosecution != Automatic Retroactive Invalidity Of Prior No-Fault Remedy**

---

## 25. Scenario X — participant was actually culpable but evidence never reaches threshold

A participant privately knows they committed the act but the state cannot establish prosecution threshold. They are released and otherwise meet objective no-fault remedy criteria.

### Analysis

The remedy architecture must operate on legitimate civil findings and evidential states, not unknowable private reality.

Denying remedy based on institutional suspicion would reintroduce punishment without adjudication.

### Result

**PASS.**

**Unproven Suspicion != Remedy Disqualification**

This does not protect fraud in the remedy claim itself.

---

## 26. Cross-scenario findings

### 26.1 Materiality is necessary

Not every brief custody interaction needs a monetary process.

Automatic restoration and challenge access remain universal where relevant, while civil-burden review can use proportionate materiality triggers.

### 26.2 Baseline plus consequential-loss model survives

A standard baseline can reduce burden for ordinary cases while an additional layer handles materially unusual consequences.

### 26.3 Remedy completeness is ESCP-sensitive

A system can restore every known dependency and still miss an unrepresented one.

Therefore restoration states must remain correctable/reopenable.

### 26.4 Claim verification must itself be bounded

Fraud resistance is legitimate, but remedy verification cannot become general surveillance.

### 26.5 Irreversible harm must remain honestly represented

Some loss cannot be restored.

Compensation can recognise or partly address it without pretending the original state has been recreated.

### 26.6 Repetition changes materiality

Several individually small interventions may form a substantial aggregate burden and a system reliability signal.

### 26.7 Remedy itself can cause harm

Delay, complexity, intrusive verification or incorrect closure can extend the original civil burden.

---

## 27. Additional candidate invariants

PCR-21 Custody Event != Mandatory Monetary Remedy Event.  
PCR-22 Low-Complexity Known Loss -> Low-Friction Remedy.  
PCR-23 No-Fault Remedy != No Causation Requirement.  
PCR-24 Mixed Causation != Zero Remedy Or Total Remedy By Default.  
PCR-25 Civil Duty To Restore != Unlimited Liability For Independently Avoidable Later Loss.  
PCR-26 Known Dependencies Restored != All Dependencies Restored.  
PCR-27 Restoration Complete State Must Be Reopenable On New Evidence.  
PCR-28 Factually Accurate Record Presentation Can Still Be Contextually Misleading.  
PCR-29 Individually Minor Repeated Burdens May Become Material In Aggregate.  
PCR-30 Claim Error != Fraud.  
PCR-31 Fraudulent Remedy Evidence != Automatic Erasure Of Legitimate Underlying Harm.  
PCR-32 Remedy Verification != General Financial Inspection Authority.  
PCR-33 Baseline Remedy != Full And Final Remedy By Default.  
PCR-34 Same Practical Restriction != Same Authority Provenance.  
PCR-35 Impossible Restoration -> Equivalent Remedy Where Reasonably Available.  
PCR-36 Compensation != Erasure Of Irreversible Harm.  
PCR-37 Remedy Process Can Itself Create Remediable Harm.  
PCR-38 Participant Non-Response != Restoration Waiver.  
PCR-39 No Biological Harm != No Custodial Harm.  
PCR-40 Automated Remedy Model != Complete Remedy Evaluation Space.  
PCR-41 Remedy Quality != Minimum Remedy Expenditure.  
PCR-42 Later Prosecution != Automatic Retroactive Invalidity Of Prior No-Fault Remedy.  
PCR-43 Unproven Suspicion != Remedy Disqualification.

---

## 28. Test conclusion

**OVERALL RESULT: PASS WITH FOUR OPERATIONAL REFINEMENTS.**

The operational architecture survives the stress test.

Four refinements should be integrated:

1. **Materiality and proportionality** — automatic restoration remains broad, but monetary/civil-burden processing should scale with materiality.
2. **Baseline + consequential-loss structure** — baseline remedy should reduce friction without silently closing unusual or larger losses.
3. **Reopenable restoration state** — dependency completeness is never absolute; later discovered stale restrictions or losses must reopen review.
4. **Irreversible-harm classification** — remedy should distinguish restoration, replacement, compensation, support and acknowledgement rather than representing every payment as restoration.

The strongest operational principle remains:

> **The civilisation should repair what it can directly repair, recognise honestly what it cannot undo, and allocate residual civil burden without requiring a participant to prove institutional wrongdoing where wrongdoing is not the basis of the remedy.**
