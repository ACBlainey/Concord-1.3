# State Triggered Review Architecture — Portable Module

**Project:** The Concord — Portable Modules  
**Source:** Civilisation Clock source family  
**Development method:** PMEDG v1.1  
**Version:** 1.0  
**Status:** GRADUATED PORTABLE MODULE / SPECIFICATION-LEVEL TRANSFER VALIDATED  
**Date:** September 2026

## 1. Purpose

State Triggered Review Architecture (STRA) is a portable mechanism for deciding **when review, reconsideration, reactivation or action candidacy becomes due** when meaningful change is not adequately represented by calendar time alone.

It supports conditions based on time, represented state, capability, dependency, events, risk, recurrence, evidence, participant-declared conditions and combinations of those conditions.

STRA does not decide the substantive outcome of the review it triggers.

> **Triggering Review ≠ Authority Over Outcome**

## 2. Problem

Many systems schedule review primarily by elapsed time:

- review every year;
- reconsider after six months;
- inspect every 1,000 hours;
- reopen the issue next quarter.

Time can be useful, but the meaningful reason to reconsider may instead be:

- a prerequisite becoming available;
- a capability threshold being reached;
- new evidence appearing;
- risk materially changing;
- a previously observed problem recurring;
- a relevant event occurring;
- a represented system state changing;
- a participant-declared condition becoming true;
- several conditions becoming true together.

STRA represents these conditions explicitly.

## 3. Portable kernel

> **Represent condition → bind relevant state/evidence → watch → evaluate → signal review/action candidacy → route to legitimate owner → record outcome → continue, complete, reset, correct or supersede.**

The mechanism separates:

1. **whether a trigger condition is represented as satisfied;**
2. **whether review/action is due;**
3. **who legitimately owns the substantive decision;**
4. **what substantive decision is made.**

These are not interchangeable.

## 4. Core invariants

> **Condition Satisfied ≠ Action Authorised**

> **Review Due ≠ Required Outcome**

> **Trigger Owner ≠ Domain Authority**

> **Observed State ≠ Complete Reality**

> **Missing Evidence ≠ Condition False**

> **Timestamp Order ≠ Universal Material Precedence**

> **Dependency Trigger ≠ Dependency Graph Ownership**

> **Participant Condition Satisfied ≠ Forced Action**

## 5. Trigger object

A trigger may be represented as:

**T = <ID, subject, class, condition, sources, dependencies, bounds, consequence, owner, route, state, provenance, history>**

Where:

- **ID** — stable trigger identifier;
- **subject** — object/process/problem/participant/function under review;
- **class** — trigger class or classes;
- **condition** — bounded condition expression;
- **sources** — represented state/evidence inputs used to evaluate the condition;
- **dependencies** — referenced prerequisite/dependency states where material;
- **bounds** — temporal boundaries/backstops or other evaluation limits;
- **consequence** — what review/action candidacy follows satisfaction;
- **owner** — legitimate substantive review/action owner where known;
- **route** — notification, retrieval, escalation or review path;
- **state** — current trigger state;
- **provenance** — origin and evidential basis;
- **history** — corrections, resets, completions and supersession.

This is an information model, not a mandatory database schema.

## 6. Trigger classes

### TEMPORAL

Condition depends on elapsed time, date, interval or deadline.

### STATE

Condition depends on a represented state changing or reaching a declared value.

### CAPABILITY

Condition depends on a capability existing, becoming available or reaching a threshold.

### DEPENDENCY

Condition depends on a prerequisite/dependent state.

### EVENT

Condition depends on occurrence of a specified event.

### RISK

Condition depends on represented probability, consequence, exposure or other risk state changing materially.

### RECURRENCE

Condition depends on a materially relevant previously encountered pattern/problem returning.

### EVIDENCE

Condition depends on new evidence materially changing the represented problem state.

### PARTICIPANT

Condition is declared by a participant or legitimate subject and becomes satisfied according to its declared terms.

### COMPOUND

Condition combines two or more trigger classes or subconditions.

The vocabulary is extensible. Implementations may add domain-specific trigger classes without changing the portable kernel.

## 7. Condition grammar

STRA must support at least simple and compound conditions such as:

- A;
- A AND B;
- A OR B;
- A AND NOT C;
- dependency D reaches state S;
- capability C reaches threshold X;
- evidence E materially changes represented state R;
- review every N months OR earlier if risk changes materially.

A condition should identify what counts as satisfaction strongly enough that evaluation does not silently invent the criterion after observing the result.

## 8. Trigger states

A minimum candidate vocabulary is:

- **DORMANT** — defined but not currently being watched;
- **WATCHING** — active evaluation is permitted/expected;
- **CONDITION-PARTIAL** — part of a compound or threshold condition is represented as satisfied;
- **CONDITION-SATISFIED** — the represented condition is satisfied;
- **REVIEW-DUE** — satisfaction has generated a review requirement/candidate;
- **ACTION-PENDING** — a legitimate owner has accepted/queued a consequential action or decision;
- **COMPLETED** — the current trigger cycle has completed;
- **SUPERSEDED** — a newer trigger definition replaces this one;
- **IMPOSSIBLE** — the declared condition can no longer be reached under the represented assumptions;
- **RETIRED** — the trigger has been deliberately closed and is no longer watched;
- **ROUTING-UNRESOLVED** — condition/review state is known but a legitimate destination or owner is unresolved;
- **UNKNOWN** — available information cannot establish trigger state;
- **DISPUTED** — materially conflicting interpretations/evidence remain.

Implementations may refine these states, but must preserve uncertainty and must not collapse satisfaction into substantive authority.

## 9. State transition is not authority transition

A typical sequence may be:

**WATCHING → CONDITION-SATISFIED → REVIEW-DUE → ACTION-PENDING → COMPLETED**

But:

**CONDITION-SATISFIED → AUTOMATIC SUBSTANTIVE ACTION**

is not a general STRA rule.

Automatic execution may exist in a host system only where an external legitimate process has already authorised that bounded automation.

STRA records/evaluates the condition; it does not manufacture the authority.

## 10. Inputs

A trigger may consume:

- trigger definition;
- represented subject state;
- evidence;
- capability state;
- dependency state;
- event records;
- risk state;
- recurrence indicators;
- temporal data;
- participant-declared conditions;
- provenance;
- correction/supersession information;
- access/privacy constraints;
- legitimate routing/owner information.

STRA does not guarantee that these inputs are true, complete or legitimate merely because they are supplied.

## 11. Outputs

STRA may produce:

- trigger state;
- satisfaction/partial/unknown/disputed result;
- evidential/provenance record;
- review-due signal;
- action candidate;
- notification;
- retrieval/revalidation request;
- routing target;
- next evaluation condition;
- temporal backstop;
- reset/completion/supersession state.

Outputs are control/review signals, not automatic domain conclusions.

## 12. Evidence and uncertainty

Evaluation should preserve the evidential basis of consequential trigger-state changes.

Where relevant, an evaluation record should identify:

**E_t = <trigger, evaluated condition, input state/evidence, result, uncertainty, source/process, time, scope>**

A trigger must be able to remain UNKNOWN or DISPUTED.

It must not silently transform:

- absent evidence into false;
- partial evidence into satisfied;
- disputed evidence into settled;
- stale evidence into current;
- unobserved state into nonexistence.

## 13. Materiality

Not every detected change should fire every related trigger.

A trigger definition may require **material change**.

Materiality is domain/context dependent and should therefore be supplied by the trigger definition or legitimate host process rather than invented by STRA.

For example:

**new evidence exists**

may differ from:

**new evidence materially changes the represented decision state.**

## 14. Temporal backstops

Functional triggers may fail because the model omitted a relevant change, evidence stopped arriving, or an impossible/stale condition persisted.

A temporal backstop should identify its **review target** where ambiguity is possible, such as:

- trigger-definition review;
- subject/domain review;
- ownership/routing review;
- evidence/revalidation review.

A trigger may therefore combine functional conditions with a temporal backstop:

> **Review when state/evidence/risk changes materially OR no later than time T.**

Temporal backstops are safeguards, not proof that calendar time is always the correct primary trigger.

## 15. Dependency triggers

A dependency trigger can represent:

> **Reconsider A when prerequisite B reaches required state S.**

STRA consumes represented dependency state.

It does not inherently discover every dependency, calculate full propagation, or own the dependency graph.

If dependency information is incomplete:

> **No Represented Dependency ≠ No Dependency**

## 16. Capability triggers

A capability trigger may reopen work when a required capability reaches a specified state or threshold.

The trigger should distinguish, where material:

- capability claimed;
- capability available;
- capability validated;
- capability authorised for the relevant use.

STRA does not itself certify the capability unless the host explicitly assigns it that bounded evidential role.

## 17. Event triggers

An event trigger should identify enough event semantics to avoid superficial matching.

For consequential triggers, relevant properties may include:

- event type;
- subject;
- scope;
- source;
- provenance;
- confidence;
- context;
- materiality.

> **Event Match ≠ Material Equivalence**

## 18. Recurrence triggers

Recurrence may reopen dormant/closed work when a materially relevant pattern returns.

A recurrence trigger should preserve the distinction between:

- same label;
- similar pattern;
- materially equivalent recurrence.

Domain interpretation determines the relevant equivalence.

## 19. Risk triggers

Risk triggers may respond to represented changes in:

- probability;
- consequence;
- exposure;
- reversibility;
- uncertainty;
- affected scope;
- other host-defined risk dimensions.

STRA detects the declared threshold/condition. It does not define the host's entire risk model.

## 20. Evidence triggers

An evidence trigger may reopen review when new evidence materially changes a represented state.

New evidence need not mean the prior state was irrational or false at the time.

The trigger/history should preserve:

**Prior state → new evidence → review due → revised/retained state**

rather than rewriting history.

## 21. Participant-declared triggers

A participant or legitimate subject may define a condition such as:

- notify me when X;
- reconsider when capability Y exists;
- wake/recontact me when condition Z is satisfied.

STRA may represent and evaluate the declared condition.

Identity, consent, continuity, authentication and legitimate execution remain external.

> **Participant Trigger ≠ Consent to Every Consequence**

## 22. Compound triggers

Compound conditions should preserve Boolean/conditional structure rather than flattening every input into one opaque score.

Examples:

**A AND B**

**A OR B**

**A AND NOT C**

**(A AND B) OR TemporalBackstop**

Where one component is UNKNOWN or DISPUTED, evaluation should preserve that uncertainty according to the declared condition semantics.

## 22A. Minimum compound uncertainty semantics

Unless a host declares stricter domain semantics, compound evaluation must preserve uncertainty rather than force binary truth.

Minimum rules:

- `TRUE AND UNKNOWN → UNKNOWN`;
- `FALSE AND UNKNOWN → FALSE` only for satisfaction of that exact conjunction, without asserting the unknown subcondition false;
- `TRUE OR UNKNOWN → TRUE`;
- `FALSE OR UNKNOWN → UNKNOWN`;
- `NOT UNKNOWN → UNKNOWN`;
- any materially relevant `DISPUTED` subcondition remains DISPUTED unless the compound result is already determined independently of it.

A host may use richer many-valued logic, but must document it with the trigger definition.

Natural-language operators such as **unless**, **except when**, **until**, or equivalent forms must be normalised into explicit logical/conditional structure before consequential evaluation. STRA must not infer an unstated exception grammar.

> **Compound Result ≠ Erasure of Subcondition Uncertainty**

## 22B. Materiality interface

Where a trigger depends on material change, STRA should consume a host-supplied materiality determination:

**M_t = <subject, change/evidence, criterion, result, evaluator/authority, provenance, time, scope, uncertainty>**

STRA does not define the domain criterion. It records and uses the bounded determination.

## 22C. Validation and authority provenance

Where a condition distinguishes AVAILABLE, VALIDATED or AUTHORISED, consequential evaluation should identify the evidence/process and legitimate source supporting that state.

> **State Label Without Provenance ≠ Validation**

Where material, capability validation may be scope-qualified (for example laboratory, operational, commissioned, environment-specific or use-specific). STRA does not impose those domain labels, but it must not collapse validation in one declared scope into validation in another.

## 23. Trigger ownership and routing

A consequential trigger should identify:

- who/what owns the trigger definition;
- who/what owns substantive review;
- where the signal is routed;
- what happens if no legitimate owner can be resolved.

If a condition is satisfied but ownership is unresolved, STRA may produce:

**CONDITION-SATISFIED / ROUTING-UNRESOLVED**

rather than executing the substantive consequence.

> **Need for Action ≠ Authority to Invent an Actor**

### 23.1 Role separation

Where material, distinguish:

- **trigger-definition owner** — legitimately defines/maintains the trigger;
- **trigger evaluator** — evaluates represented condition inputs;
- **substantive review/action owner** — owns the domain decision;
- **ownership-resolution route** — process/target used when the substantive owner is unresolved.

One actor may legitimately fill several roles, but STRA must not assume that identity.

An unresolved-owner record should preserve the trigger, condition state, candidate consequence, disputed/unknown owners, routing request, provenance and resolution status.

A ROUTING-UNRESOLVED state must itself have a bounded review/escalation/backstop appropriate to consequence and host context. Repeated evaluation cycles must not silently convert unresolved ownership into legitimate ownership, nor permit indefinite unresolved persistence without a defined review route.

### 23.2 Reconciliation handoffs

STRA does not reconcile every conflicting domain state itself. When dependency/state sources conflict, it should emit or consume a bounded reconciliation result carrying:

**R_h = <subject, conflicting claims, sources, requested question, legitimate resolver, result/status, provenance, time, scope>**

The same pattern may be used for domain-owned recurrence/event equivalence determinations.

If reconciliation returns **DISPUTED**, STRA preserves the unresolved state and routes according to the host's legitimate resolution path. DISPUTED is not a silent terminal success/failure state.

## 24. Memory/retrieval interface

STRA may signal that dormant/cold information has become relevant.

A generic sequence is:

**Trigger → Relevance Signal → Legitimate Retrieval → Revalidation → Domain Use or Return to Dormant State**

STRA owns the relevance/trigger signal.

A memory/knowledge system owns retrieval/provenance.

The domain owner determines substantive use.

## 25. Revalidation

Material retrieved after dormancy should not automatically be treated as current.

A reactivation trigger may therefore produce a **revalidation request** rather than an immediate substantive use signal.

> **Relevance Returned ≠ Validity Restored**

## 26. Event-order interface

Some trigger conditions require knowing whether one event materially preceded another.

STRA may consume an externally supplied consequence-relevant ordering relation.

Where STRA consumes an externally supplied consequence-relevant ordering relation, that relation should include enough information to preserve:

- events/subjects ordered;
- claimed relation;
- source/process;
- provenance;
- confidence or uncertainty;
- reconciliation status;
- time/scope of the determination.

It does not require a universal total order and should not infer material precedence merely from timestamps.

> **Timestamp(A) < Timestamp(B) ≠ A materially precedes B for every consequence**

## 27. Privacy and minimum necessary observation

Trigger evaluation should observe/access only the information legitimately necessary to evaluate the declared condition.

A trigger must not become a pretext for broad surveillance or retrieval.

Where protected information is involved, the host may supply:

- a bounded condition result;
- a privacy-preserving signal;
- a redacted state;
- an authorised evaluator output;

instead of exposing the underlying content to STRA.

### 27.1 Privacy-preserving bounded result

Where STRA lacks legitimate access to underlying protected evidence, it may consume:

**P_r = <condition/subject, result, authorised evaluator, provenance, time, scope, uncertainty>**

The result may be a bounded token such as SATISFIED / NOT-SATISFIED / UNKNOWN without exposing protected source content.

## 28. Correction and supersession

Trigger definitions and evaluations are corrigible.

A correction should preserve:

**Original trigger/evaluation → correction/supersession → updated trigger/evaluation**

where legitimate retention permits.

Do not silently rewrite prior trigger history.

## 29. Stale and impossible triggers

A trigger may become stale because:

- its subject no longer exists;
- its assumptions changed;
- the condition became impossible;
- its owner disappeared;
- its dependency model changed;
- the desired review is no longer legitimate/relevant.

Long-lived WATCHING triggers must have a bounded trigger-definition review condition or backstop appropriate to the host context. STRA should not permit indefinite WATCHING with no route for checking whether the trigger remains meaningful.

Possible outcomes:

- continue watching;
- modify;
- reset;
- suspend;
- supersede;
- retire;
- route for ownership resolution.

## 30. Cascade control

One satisfied trigger may legitimately create or activate another trigger.

However uncontrolled trigger cascades can amplify noise or create accidental authority chains.

Minimum portable cascade semantics are:

- a superseded/retired trigger must not be treated as live merely because a stale replica or downstream subscriber still exposes an older WATCHING state;
- host integration must provide a bounded way to propagate or reconcile supersession to relevant replicas/subscribers before consequential duplicate activation;


- preserve parent/initiating-trigger provenance;
- detect direct cycles where represented;
- suppress duplicate activation of the same consequence for the same material condition where host semantics allow;
- require each consequential child trigger to satisfy its own declared condition or explicit activation rule;
- apply a materiality gate before consequential propagation where materiality is required;
- validate owner/routing before substantive consequence.

Depth/rate limits remain host-defined because appropriate values are domain-dependent.

Implementations may additionally support bounded cascade controls such as:

- provenance of trigger creation;
- cycle/depth limits;
- duplicate suppression;
- materiality checks;
- owner/routing validation;
- human/domain review where consequence warrants it.

Exact controls are host-dependent.

## 31. Minimum operating cycle

1. **DEFINE** — represent subject, condition, class and consequence.
2. **BIND** — identify inputs, provenance and legitimate routing/owner.
3. **WATCH** — observe permitted relevant represented state/evidence.
4. **EVALUATE** — test condition without manufacturing certainty.
5. **SIGNAL** — record partial/satisfied/unknown/disputed/review-due state.
6. **ROUTE** — send review/action candidacy to legitimate owner.
7. **RECORD** — preserve evaluation provenance and outcome.
8. **UPDATE** — complete, reset, continue, correct, suspend or supersede.
9. **BACKSTOP** — re-evaluate trigger/assumptions at bounded fallback where defined.

## 32. Worked example A — Engineering qualification

A team has deferred qualification of a component until a new test facility becomes available.

Trigger:

> **When Facility F is AVAILABLE AND VALIDATED for Test Class Q, reopen Component C qualification.**

The facility state becomes AVAILABLE but validation remains UNKNOWN.

STRA records CONDITION-PARTIAL rather than REVIEW-DUE.

When validation is later established, STRA marks the condition satisfied and routes a qualification-review candidate to the engineering owner.

It does not itself approve Component C.

## 33. Worked example B — Research recurrence

A research team archives a failed hypothesis after repeated negative results.

Trigger:

> **Reopen if a materially new measurement technique becomes available OR new evidence contradicts the negative result. Review no later than five years if the trigger remains active.**

Three years later a new instrument becomes available.

STRA signals REVIEW-DUE and requests retrieval/revalidation of the archived research package.

The old hypothesis does not become true merely because review reopened.

## 34. Worked example C — Long-duration maintenance

A system normally receives a full review every 24 months.

The host defines:

> **Review at 24 months OR earlier if risk exposure rises above R OR a specified failure event recurs.**

After nine months, a relevant failure pattern recurs but equivalence is disputed.

STRA records DISPUTED/REVIEW-ROUTING-REQUIRED according to host semantics rather than silently declaring the risk threshold met.

## 35. Worked example D — Participant-declared notification

A participant requests:

> **Notify me when capability X reaches validated state Y.**

STRA watches the permitted capability-state source.

When Y is represented as reached, it generates the notification/review candidate.

It does not infer consent to any further action beyond the declared consequence.

## 36. Failure modes

**STRA-F1 — Calendar collapse:** elapsed time becomes the only meaningful trigger.

**STRA-F2 — Trigger-authority collapse:** condition satisfaction becomes automatic substantive authority.

**STRA-F3 — False satisfaction:** weak/incomplete evidence is treated as fulfilled condition.

**STRA-F4 — False non-satisfaction:** missing/unobserved evidence is treated as proof condition is false.

**STRA-F5 — Stale trigger:** old condition persists after assumptions materially change.

**STRA-F6 — Impossible trigger persistence:** unreachable condition watches indefinitely without review/backstop.

**STRA-F7 — Event overmatching:** superficial similarity fires recurrence/event triggers.

**STRA-F8 — Cascade amplification:** trigger chains expand without bounded control.

**STRA-F9 — Dependency absorption:** STRA attempts to own the whole dependency graph.

**STRA-F10 — Domain absorption:** STRA decides substantive domain outcomes.

**STRA-F11 — Consent bypass:** participant-declared condition becomes forced action.

**STRA-F12 — Privacy leakage:** evaluation/retrieval exposes unnecessary protected information.

**STRA-F13 — Stale reactivation:** dormant material is treated as current without revalidation.

**STRA-F14 — Ownership vacuum:** condition fires but no legitimate owner exists.

**STRA-F15 — Total-order assumption:** timestamp order is mistaken for all material precedence.

**STRA-F16 — Completeness illusion:** unobserved relevant state is assumed not to exist.

## 37. Falsification/revision conditions

Revise or reject the portable architecture if testing shows that:

1. useful non-temporal review cannot operate without the full Concord Clock;
2. condition satisfaction cannot remain separate from action authority;
3. UNKNOWN/DISPUTED cannot survive compound evaluation;
4. temporal backstops cannot coexist with functional triggers;
5. dependency triggers require STRA to own the dependency graph;
6. participant conditions inherently imply forced action;
7. retrieval triggers cannot preserve revalidation/privacy boundaries;
8. legitimate routing cannot be externalised;
9. correction/supersession necessarily erases trigger history;
10. event/recurrence conditions cannot avoid systematic overmatching;
11. cascade control requires STRA to become general governance;
12. clean evaluators cannot apply STRA outside civilisational development.

## 38. Minimum implementation requirements

A conforming STRA implementation must provide:

1. identifiable trigger objects;
2. explicit condition representation;
3. at least temporal plus one non-temporal trigger class;
4. represented trigger state;
5. UNKNOWN or equivalent;
6. separation of satisfaction from substantive authority;
7. evidence/state provenance for consequential evaluations;
8. legitimate review/action routing interface;
9. correction/supersession history;
10. bounded handling of stale/impossible triggers;
11. access/privacy boundary;
12. support for temporal backstop where required;
13. bounded compound-condition semantics where compound triggers are used;
14. explicit external dependency/state interfaces rather than assumed completeness.

## 39. Non-requirements

STRA does not require:

- a universal scheduler;
- a central database;
- one global clock;
- a universal risk model;
- a universal dependency graph;
- a universal event ontology;
- automatic execution;
- Concord governance;
- KCS;
- the Civil State Map;
- CDT;
- a particular AI architecture;
- a particular programming language;
- universal access to underlying evidence.

## 40. External interfaces

### Host state/evidence system

Supplies represented state/evidence and relevant provenance.

### Dependency system

Supplies prerequisite/dependency states where a trigger requires them.

### Capability-validation system

Supplies relevant capability state.

### Memory/knowledge system

Receives retrieval/revalidation requests and supplies authorised material.

### Domain owner

Owns substantive review/action.

### Identity/consent/continuity system

Owns participant identity, consent and continuity where participant triggers are used.

### Event-order/reconciliation system

Supplies consequence-relevant ordering where a trigger genuinely requires it.

## 41. Validation status

Current status:

> **v1.0 — GRADUATED PORTABLE MODULE**

> **SOURCE RESOLUTION SUBSTANTIALLY COMPLETE**

> **INTERNAL SOURCE-FAMILY OPERATIONAL EVIDENCE EXISTS**

> **BTT-001: STRA-T3 FUNCTIONAL TRANSFER — 50 / 50 FROZEN PREDICTIONS MATERIALLY CONFIRMED; 0 / 12 FUNDAMENTAL FAILURES**

> **BTT-002: STRA-T3 FUNCTIONAL TRANSFER — 52 / 52 FROZEN PREDICTIONS MATERIALLY CONFIRMED; 0 / 14 FUNDAMENTAL FAILURES**

> **COMBINED: 102 / 102 FROZEN PREDICTIONS; 0 / 26 FUNDAMENTAL FAILURES; CROSS-TEST CONVERGENCE YES**

> **THIRD BLIND TEST NOT CURRENTLY JUSTIFIED UNDER PMEDG**

The specification must not be represented as graduated.

## 42. Validation and graduation status

This release incorporates only bounded clarifications supported by BTT-001 and BTT-002.

It demonstrated functional architectural transfer in two materially different non-Concord domains and passed formal PMEDG Graduation Review.

> **Two-Domain Transfer ≠ Universal Validation**

> **Graduation ≠ Empirical Proof in Every Host Domain**

## 43. Release status

STRA v1.0 is released as a graduated portable module. Future revision should be evidence-driven and versioned. New deployment evidence, a materially new host class, or a newly discovered mechanism-level uncertainty may justify renewed testing or revision.
