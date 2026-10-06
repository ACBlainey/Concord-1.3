# Information Exposure, Reidentification and Successor Protection — Cross-Domain Architecture 001

**Project:** The Concord Framework  
**Date:** 6 October 2026  
**Status:** ACTIVE DEVELOPMENT / CROSS-DOMAIN ARCHITECTURE / PROVISIONAL / NON-CANONICAL  
**Primary interfaces:** Protection-State Transition Authority and Reclassification; Derived Information Protection-Lineage and Transformation Boundaries; CIBB; BTA; Lifecycle Stewardship Review; KCS Change Propagation; STRA; Historical; Civil Contact; Law/Judiciary

## 1. Purpose

Information protection can fail after a previously legitimate transition.

Examples:
- an anonymised dataset becomes re-identifiable;
- a bounded projection is accidentally disclosed;
- a public derivative is discovered to reveal protected meaning;
- a recipient rediscloses information outside scope;
- a repeated-query sequence reconstructs hidden state;
- a new external dataset makes old releases sensitive;
- a classification or disclosure decision is later found defective.

Information cannot always be made unknown again.

This architecture defines successor protection and remedy without relying on fictional rollback.

## 2. Core principle

> **Information Exposure Is A State Change, Not Merely A Policy Violation.**

Once exposure occurs, the system must represent the actual new state.

A label saying PRIVATE does not restore secrecy after public disclosure.

Therefore:

**Declared Protection State != Actual Exposure State**

## 3. Exposure state dimensions

A useful representation distinguishes:
- intended protection state;
- actual audience;
- estimated propagation;
- identity/linkability;
- semantic exposure;
- persistence;
- retrievability;
- downstream copies;
- downstream decisions;
- legitimacy of exposure;
- confidence/uncertainty.

This prevents binary PRIVATE/PUBLIC labels from hiding partial compromise.

## 4. Exposure classes

Candidate classes:

### E0 — Contained
No known unauthorised exposure.

### E1 — Bounded unintended exposure
Known limited recipient/audience; propagation plausibly containable.

### E2 — Distributed controlled exposure
Multiple known holders; still subject to enforceable/technical controls.

### E3 — Unbounded or public exposure
Recall cannot reasonably be assumed.

### E4 — Unknown exposure extent
Material exposure suspected/known but audience/propagation unresolved.

These are operational states, not culpability findings.

## 5. Exposure != legitimacy

Information can be:
- legitimately public;
- illegitimately public;
- legitimately shared to a bounded group;
- accidentally shared;
- technically accessible but not legitimately usable.

Therefore:

**Exposure State != Legitimacy State**

and:

**Publicly Obtainable != Legitimately Usable For Every Purpose**

## 6. Re-identification as successor state

If an anonymised object becomes linkable to a participant:

`ANONYMISED -> REIDENTIFIABLE`

this is a material information-state transition.

The appropriate response is not to pretend the original source was never anonymised.

Instead establish a successor protection state.

> **Reidentification Creates A New Current State; It Does Not Rewrite Historical State.**

## 7. No fictional deletion

Where information has escaped into an unbounded audience, deletion commands may reduce future availability but cannot guarantee restoration of ignorance.

Therefore:

> **Deletion Request != Restoration Of Secrecy**

and:

> **Copy Removal != Knowledge Removal**

Systems should not certify restoration they cannot establish.

## 8. Successor protection

When prior protection cannot be restored, establish the best legitimate successor state.

Possible measures:
- stop future releases;
- revoke controlled access;
- rotate identifiers/keys;
- sever linkage;
- reduce future precision;
- suppress search/indexing where legitimately controllable;
- mark information compromised/stale/disputed;
- notify affected participants;
- notify legitimate downstream holders;
- constrain future use;
- require deletion from controlled holders;
- invalidate credentials/tokens;
- correct false information;
- create replacement identifiers;
- audit consequential decisions;
- provide remedy;
- preserve evidence/provenance.

> **Failure To Restore Prior State != Failure To Protect The Successor State.**

## 9. BTA relation

BTA already establishes:

**Rollback != Restoration Unless Prior-State Equivalence Is Actually Re-established.**

Information exposure is a strong example.

A successor transition might be:

`PROTECTED_AND_SECRET`
-> `EXPOSED_UNAUTHORISED`
-> `COMPROMISED_BUT_FUTURE_USE_RESTRICTED`

rather than falsely recording:

`EXPOSED_UNAUTHORISED -> PROTECTED_AND_SECRET`

## 10. Reversibility gradient

Information operations vary in reversibility.

Examples:
- internal projection before egress: highly reversible;
- controlled disclosure to one trusted system: partly reversible;
- distribution to many controlled holders: less reversible;
- public internet release: effectively irreversible in ordinary governance terms.

Therefore:

> **Information Irreversibility Is Graduated, Not Binary.**

Pre-transition review burden should reflect this gradient.

## 11. Downstream review

If exposed/reidentified information was used for consequential decisions, those decisions may need review.

Use KCS:

`MaterialExposureOrCorrection -> CandidateReview(DependentDecision)`

Do not automatically reverse every decision.

A decision may remain valid for independent reasons.

## 12. Participant notification

Where exposure materially affects a participant, notification may itself be a legitimate protective function.

Civil Contact can provide a bounded route.

Notification should distinguish:
- what is known;
- what is uncertain;
- what information was affected;
- likely scope;
- protective actions available;
- contest/remedy route.

Notification should not unnecessarily disclose additional protected information.

## 13. Exposure to the participant

A participant learning an inference about themselves can itself be consequential.

For example, a probabilistic medical/genetic or cognitive inference may cause harm if presented as certainty.

Therefore:

**Participant Access != Permission To Misrepresent Epistemic Status**

Access should preserve uncertainty/context where material.

## 14. False information exposure

If exposed information is false, the harm can persist even after correction.

Therefore:
- preserve correction provenance;
- propagate correction signals where legitimate;
- distinguish original claim from corrected state;
- review consequential downstream decisions.

> **Correction != Automatic Erasure Of Prior Consequence**

This interfaces with Historical and KCS.

## 15. Controlled-holder obligations

A legitimate recipient may have ongoing obligations after receiving information:
- purpose limitation;
- no onward disclosure;
- expiry;
- deletion;
- correction uptake;
- access termination;
- incident reporting.

These obligations can remain enforceable even if the information later becomes publicly obtainable elsewhere.

> **External Public Availability != Automatic Termination Of Existing Bounded Duties**

## 16. Public-domain reality

Concord should not construct a fictional architecture in which public information can always be recalled.

Where information is genuinely unbounded:
- focus on future misuse constraints where legitimate;
- prevent institutional amplification without basis;
- correct falsehoods;
- prevent stale classifications from continuing;
- restrict protected systems from using it merely because it is technically available;
- provide remedy for unlawful exposure.

This respects reality without treating exposure as moral/legal absolution.

## 17. Right to be forgotten versus historical integrity

A participant may have legitimate interests in reducing active operational exposure.

Historical may simultaneously have legitimate duties to preserve accurate provenance, accountability or civil history.

These are not necessarily contradictory if:
- operational discoverability is reduced;
- access is restricted;
- historical retention is preserved under stronger wrapper;
- public projections are corrected/removed where legitimate;
- provenance survives without active operational use.

Therefore:

> **Reduced Operational Discoverability != Historical Erasure**

and:

> **Historical Retention != Continued Operational Exposure**

## 18. Exposure evidence

Exposure assessment should distinguish:
- confirmed recipient;
- likely recipient;
- possible recipient;
- public indexing;
- download/copy evidence;
- downstream repost;
- inferred access;
- unknown.

Do not inflate uncertainty into certainty.

**Possible Exposure != Confirmed Universal Exposure**

## 19. Cumulative query reconstruction

PLE already provides the primary mechanism for repeated-query reconstruction:
- cumulative disclosure state;
- query budgets;
- semantic restrictions;
- result coarsening;
- anti-correlation rules;
- purpose binding;
- recipient restrictions.

This architecture consumes PLE's result.

It does not duplicate PLE.

If reconstruction nevertheless occurs, treat the newly inferred protected state as a current exposure/protection event.

## 20. Emergency containment

A severe exposure may justify temporary protective action:
- suspend an interface;
- stop publication;
- disable a query class;
- freeze onward transfer.

Emergency containment remains bounded.

**Emergency Containment != Permanent Information Authority**

Normal review should follow.

## 21. Accountability

Exposure response and culpability are separate.

An actor may cause exposure:
- deliberately;
- negligently;
- reasonably despite safeguards;
- through unforeseeable external change;
- through system failure;
- through later re-identification capability.

The successor protection response should occur regardless of blame.

> **Need To Protect Current State != Prior Finding Of Fault**

Law/audit can determine responsibility separately.

## 22. Transfer tests

### Reidentified research dataset
Previously legitimate anonymised release becomes linkable using new public registry.
- mark current re-identification risk;
- stop future release/version;
- reassess controlled distributions;
- notify where warranted;
- constrain institutional reuse;
- preserve historical fact that earlier release passed then-current legitimate standard.
PASS.

### Leaked medical projection
A bounded fitness result reaches unintended recipients.
- source medical record need not be considered fully compromised unless evidence supports it;
- fitness projection exposure state changes;
- future distribution can be stopped;
- affected participant can be notified;
- misuse can remain prohibited.
PASS.

### Public false risk score
A false modelled score becomes public.
- deletion cannot guarantee forgetting;
- correction should propagate;
- future official use can be prohibited/corrected;
- downstream consequential decisions reviewed.
PASS.

### AI context leak
AI system exposes protected context in an answer.
- answer is new exposed object;
- source wrapper remains independently protected;
- query/context route should be reviewed;
- downstream copies may be unbounded;
- future model/context access can be changed.
PASS.

## 23. Failure modes

- secrecy-restoration fiction;
- exposure-totalisation;
- public-equals-permitted;
- historical rewrite;
- deletion absolutism;
- notification leakage;
- blame-before-protection;
- uncontrolled correction cascade;
- right-to-forget historical destruction;
- emergency containment capture.

## 24. Candidate invariants

IERSP-01 — Information Exposure Is A State Change, Not Merely A Policy Violation.  
IERSP-02 — Declared Protection State != Actual Exposure State.  
IERSP-03 — Exposure State != Legitimacy State.  
IERSP-04 — Publicly Obtainable != Legitimately Usable For Every Purpose.  
IERSP-05 — Reidentification Creates A New Current State; It Does Not Rewrite Historical State.  
IERSP-06 — Deletion Request != Restoration Of Secrecy.  
IERSP-07 — Copy Removal != Knowledge Removal.  
IERSP-08 — Failure To Restore Prior State != Failure To Protect The Successor State.  
IERSP-09 — Information Irreversibility Is Graduated, Not Binary.  
IERSP-10 — Participant Access != Permission To Misrepresent Epistemic Status.  
IERSP-11 — Correction != Automatic Erasure Of Prior Consequence.  
IERSP-12 — External Public Availability != Automatic Termination Of Existing Bounded Duties.  
IERSP-13 — Reduced Operational Discoverability != Historical Erasure.  
IERSP-14 — Historical Retention != Continued Operational Exposure.  
IERSP-15 — Possible Exposure != Confirmed Universal Exposure.  
IERSP-16 — Emergency Containment != Permanent Information Authority.  
IERSP-17 — Need To Protect Current State != Prior Finding Of Fault.

## 25. Central rule

> **When Information Cannot Be Made Secret Again, Concord Must Govern The State That Actually Exists Rather Than Pretend The Previous State Was Restored.**

The objective becomes bounded successor protection, correction, containment, review, remedy and prevention of unjustified future use.
