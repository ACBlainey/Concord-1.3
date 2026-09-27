# State and Maturity Mapping — Portable Module v1.0

**Version:** 1.0  
**Development origin:** Level B — Extractable Architectures  
**Method:** PMEDG v1.2  
**Status:** GRADUATED PORTABLE MODULE / SPECIFICATION-LEVEL TRANSFER VALIDATED  
**Date:** September 2026

## 1. Purpose

State and Maturity Mapping (SMM) is a portable architecture for representing the current developmental condition of required functions in a complex system.

It exists to prevent several common collapses:

- presence into maturity;
- maturity into sufficiency;
- local absence into system absence;
- dependency blockage into local deficiency;
- documentation into capability;
- uncertainty into false certainty;
- state description into authority over what must happen next.

SMM is a self-model, not the system itself.

> **Represented State ≠ Complete System Reality**

## 2. Portable problem

> **How can a complex system represent the current developmental condition of required functions in context without confusing presence with maturity, maturity with sufficiency, local absence with system absence, dependency blockage with absence, or the resulting state description with authority over what must happen next?**

Potential hosts include engineering programmes, research organisations, software/platform architectures, safety and assurance systems, institutional capability maps, long-duration projects, distributed organisations, AI-agent ecosystems and infrastructure portfolios.

## 3. Portable kernel

> **Identify required function → establish context → represent presence → assess applicable maturity dimensions → determine context-relative sufficiency → represent dependencies/blockers → record consequence/exposure and uncertainty → classify unresolved state → produce bounded review/development candidacy → preserve evidence/history**

SMM is descriptive and diagnostic. It may support later review, prioritisation or development, but does not own those decisions.

## 4. Portable owner

SMM owns:

> **function/state identification + context-sensitive presence + maturity + sufficiency representation + dependency/blocker state + consequence/exposure + uncertainty/dispute + evidence/provenance + freshness + bounded response candidacy**

SMM does not own:

- the host's complete topology;
- discovery of every dependency;
- substantive domain authority;
- resource allocation;
- priority selection;
- remediation execution;
- universal maturity criteria;
- universal consequence scoring;
- truth of every underlying datum.

## 5. Core invariants

> **Presence ≠ Maturity**

> **Maturity ≠ Context-Relative Sufficiency**

> **Dependency-Blocked ≠ Absent**

> **Locally Missing ≠ Systemically Absent**

> **Interface-Supplied ≠ Locally Implemented**

> **Documentation ≠ Capability**

> **State Vector ≠ Universal Score**

> **State Description ≠ Permission**

> **Development Need ≠ Authority**

> **Stale ≠ False**

> **UNKNOWN ≠ False**

> **DISPUTED ≠ Resolved**

> **Current State ≠ Erasure of Prior State**

## 6. Core state model

At time t:

**SM(t) = <N, P, M, Q, D, C, U, A, R>**

where:

- **N** — represented required functions/units;
- **P** — presence state;
- **M** — maturity state;
- **Q** — context-relative sufficiency;
- **D** — dependency/blocker state;
- **C** — consequence/exposure;
- **U** — uncertainty/dispute;
- **A** — active work/development state;
- **R** — evidence, provenance, freshness and review state.

The model synthesises evidence. It does not own every underlying datum.

## 7. Unit of assessment

The default unit is a required function or legitimate architectural/operational unit, not a document, team name or repository entry.

Before consequential assessment:

0. declare the assessment-unit/function boundary at the granularity relevant to the claim;
1. identify the required function/unit;
2. identify legitimate owner or distributed suppliers where relevant;
3. identify interfaces;
4. establish assessment context;
5. source-resolve apparent omissions where feasible and material.

An artefact can be evidence about a function without being the function.

If unit identity is unresolved, SMM should preserve that uncertainty rather than manufacture a convenient unit.

A missing subfunction does not automatically make the whole assessed function PARTIAL. Depending on the declared assessment boundary it may instead be a maturity deficit, a partial-function deficit, a dependency blockage, or a separate required function.

Use this bounded decision rule where composition is material:

1. **Declare the assessed function/unit.**
2. **Ask whether the missing element is part of the function's required supply boundary.**
   - If no, assess it separately or as a dependency/interface.
   - If yes, continue.
3. **Ask whether the required element is supplied but cannot currently operate because of an upstream prerequisite.**
   - If yes, preserve presence and represent the operational state as **DEPENDENCY_BLOCKED/BLOCKED** as appropriate.
4. **Ask whether only part of the declared required function is actually supplied.**
   - If yes, **PARTIAL** may be appropriate.
5. **If the function is supplied but lacks assurance/development required for the context, preserve presence and represent the deficit in maturity/sufficiency rather than presence.**
6. **If the boundary itself remains unclear, record UNKNOWN/DISPUTED rather than choosing the most convenient presence state.**

This is a classification aid, not a universal domain ontology.

> **Missing Subfunction ≠ Automatically Partial Presence**

## 8. Context record

A state claim is bounded by context.

Where one function is assessed in multiple materially different contexts, SMM should preserve an explicit **context set** rather than forcing one context-free sufficiency label.

**C_set = <function, contexts, material fields considered, material fields omitted with rationale, evidence boundary>**

A context record may include:

**C_x = <domain, consequence class, affected parties/functions, authority/use, scale, environment/platform, operational mode, reversibility, duration, exposure>**

Not every field is mandatory in every host, but materially relevant context must not be omitted merely to obtain a simpler maturity result.

A function may be sufficiently mature for one context and insufficient for another.

Where a host can store only one sufficiency field, the portable record should retain the context set externally and the host field should reference that record or explicitly declare itself a lossy projection. A single field must not silently collapse materially different context states.

Minimum reference pattern:

**CTX_REF = <function-ID, context-set-ID, selected/display context if any, projection-loss flag>**

The exact serialization is host-defined; preservation of the context distinctions is not.

## 9. Presence state

Minimum portable presence vocabulary:

- **PRESENT_EXPLICIT** — the function is directly supplied by an identified unit;
- **PRESENT_DISTRIBUTED** — the function is supplied across multiple units;
- **INTERFACE_SATISFIED** — the local unit does not implement the capability but a legitimate interface supplies it;
- **PARTIAL** — only part of the required function is supplied;
- **DEPENDENCY_BLOCKED** — the function/capability exists or is developing but cannot currently operate because a prerequisite is unresolved;
- **CANDIDATE_ABSENT** — no adequate supply has yet been found after the declared search/source-resolution boundary;
- **UNKNOWN** — available evidence does not support a state determination;
- **DISPUTED** — materially conflicting state claims remain unresolved;
- **NOT_APPLICABLE** — the function is not required in the declared context.

CANDIDATE_ABSENT is deliberately provisional.

CANDIDATE_ABSENT may be promoted to REQUIRED_FUNCTION_GAP only when the required function is clearly declared, a host-appropriate search/source-resolution boundary is declared, relevant obvious/distributed/interface suppliers have been checked to that declared standard, residual uncertainty is recorded, and the classification remains corrigible.

There is no universal quantitative search threshold. A materially unavailable source should block promotion when it is reasonably capable of changing the conclusion about whether adequate supply exists. If unavailable material is judged non-material, that judgement and rationale should be recorded. Where materiality itself is uncertain, retain CANDIDATE_ABSENT/UNKNOWN rather than manufacture certainty.

> **No Supply Found Within Search Boundary ≠ Proven Global Absence**

## 10. Maturity dimensions

SMM does not impose one universal maturity ontology.

A host should declare the dimensions legitimately relevant to the function and context.

A maturity dimension should state:

- dimension identifier/name;
- applicability;
- criterion;
- evidence basis;
- state;
- uncertainty;
- evaluator/process where material.

Candidate cross-domain probes inherited from the source architecture may include:

- bounded scope;
- legitimate/non-self-justifying authority;
- temporal revision, exit or termination;
- contestability, correction and repair;
- affected-party standing and agency;
- asymmetry/anti-capture compensation;
- effective access;
- function-over-form and replaceability;
- recursive review;
- provenance and learning.

These are reusable prompts, not mandatory universal requirements.

> **Candidate Probe ≠ Universal Criterion**

## 11. Maturity-dimension state

For an applicable dimension:

- **SATISFIED_INTERNAL**
- **SATISFIED_INTERFACE**
- **PARTIAL**
- **UNSATISFIED**
- **DEPENDENCY_BLOCKED**
- **UNKNOWN**
- **DISPUTED**
- **NOT_APPLICABLE**

The interface state is first-class because a capability need not be implemented locally to be legitimately supplied.

## 12. Sufficiency

Sufficiency asks:

> **Is the required function adequately developed for this declared context and consequence?**

Minimum states:

- **SUFFICIENT**
- **CONDITIONALLY_SUFFICIENT**
- **INSUFFICIENT**
- **BLOCKED**
- **UNKNOWN**
- **DISPUTED**
- **NOT_APPLICABLE**

A SUFFICIENT judgement should identify the material requirements/thresholds on which it depends.

Sufficiency is provisional and context-sensitive.

It must not be inferred merely from age, document size, formalisation, feature count or general maturity labels.

## 13. No universal maturity score

SMM does not require a single percentage, rank or maturity number.

A system may be strong in provenance and weak in correction; another may be highly corrigible but dependency-blocked.

An aggregate may be used only when a host has a justified bounded purpose and the aggregation does not erase material unresolved dimensions.

Any consequential aggregate should disclose at minimum:

- aggregation purpose;
- scope/context;
- included dimensions;
- excluded or NOT_APPLICABLE dimensions;
- weighting/combination method;
- visibility/count of UNKNOWN, DISPUTED and BLOCKED states;
- material high-consequence exceptions;
- evidence/freshness boundary;
- source-state reference;
- projection limitations.

Minimum portable disclosure pattern:

**AGG = <purpose, scope/context, included, excluded/N-A, method/weights, unresolved-state disclosure, high-consequence exceptions, evidence/freshness boundary, source-state reference, limitations>**

A consequential aggregate should be refused or clearly marked **NOT VALID FOR THE PROPOSED USE** when the host cannot preserve material UNKNOWN/DISPUTED/BLOCKED states, high-consequence exceptions, or a traceable source-state reference.

The aggregate is a projection and must not replace the underlying state vector.

> **Aggregation Convenience ≠ State Truth**

## 14. Contiguous development and feature exposure

Where a host legitimately uses ordered developmental/assurance levels, SMM may distinguish:

- **contiguous developmental level** — highest level reached without an unresolved applicable lower requirement;
- **feature exposure** — highest higher-order capability observed anywhere.

Example:

> Contiguous level C2; feature exposure C5.

Higher-order features do not erase lower unresolved requirements.

This feature is optional when the host has no meaningful ordered levels.

## 15. Dependency/blocker interface

SMM may consume dependency information including:

- prerequisites;
- blocking prerequisites;
- downstream dependents;
- alternatives;
- dependency confidence;
- failure consequence;
- freshness.

SMM does not own dependency discovery or the full dependency graph.

> **Dependency State Representation ≠ Dependency Discovery Ownership**

A downstream function blocked by an upstream prerequisite should not automatically be classified as a local developmental gap.

## 16. Consequence and exposure

Where material, represent:

- severity if unresolved;
- probability/frequency where legitimately estimable;
- affected users/participants/functions;
- reversibility;
- time sensitivity;
- current deployment/exposure;
- safeguards;
- uncertainty.

Consequence/exposure helps preserve low-connectivity but high-consequence deficits.

Downstream projections or ranking systems may use centrality, but material consequence/exposure fields must remain available and must not be silently discarded merely because centrality is low.

Where SMM exports state to a ranking/prioritisation interface, the projection should carry either the material consequence/exposure fields or a lossless reference to them. If the downstream representation cannot carry or reference them, the projection should be marked lossy and not treated as a complete SMM-derived priority representation.

SMM does not itself define universal severity scales or action thresholds.

## 17. Uncertainty and dispute

UNKNOWN and DISPUTED are operational states.

**UNKNOWN** means evidence is insufficient for the declared claim.

**DISPUTED** means materially conflicting claims/evidence remain unresolved.

Neither should be silently converted into SATISFIED, ABSENT, SUFFICIENT or INSUFFICIENT.

A dispute record should preserve the competing claims and provenance where feasible.

## 18. Gap/state classification

After the declared source-resolution/evidence boundary, classify unresolved state where useful as:

- **REQUIRED_FUNCTION_GAP**
- **DEVELOPMENTAL_GAP**
- **INTEGRATION_INTERFACE_GAP**
- **DEPENDENCY_BLOCKED**
- **REPRESENTATION_GAP**
- **SATISFIED**
- **UNKNOWN**
- **DISPUTED**

Definitions:

**REQUIRED_FUNCTION_GAP** — a required function has no adequate identified supply after the declared search boundary.

**DEVELOPMENTAL_GAP** — the legitimate owner/supply exists but lacks a required capability or maturity.

**INTEGRATION_INTERFACE_GAP** — required capabilities exist but are not adequately connected or exposed.

**DEPENDENCY_BLOCKED** — progress/use is blocked by an upstream prerequisite.

**REPRESENTATION_GAP** — the underlying capability may exist, but the current state model/evidence does not adequately represent it.

Classification remains corrigible.

## 19. Candidate response classes

SMM may produce bounded response candidacy:

- SATISFIED → **NO_ACTION_CANDIDATE**
- REPRESENTATION_GAP → **IMPROVE_MAP_OR_EVIDENCE**
- INTEGRATION_INTERFACE_GAP → **INTERFACE_OR_INTEGRATION_CANDIDATE**
- DEVELOPMENTAL_GAP → **DEVELOP_EXISTING_OWNER_CANDIDATE**
- REQUIRED_FUNCTION_GAP → **NEW_FUNCTION/ARCHITECTURE_CANDIDATE**
- DEPENDENCY_BLOCKED → **RESOLVE_UPSTREAM_CANDIDATE**
- UNKNOWN → **INVESTIGATION_CANDIDATE**
- DISPUTED → **PRESERVE_AND_REVIEW_CANDIDATE**
- legitimate active work already addresses the gap → **CONTINUE_EXISTING_WORK / NO_NEW_CANDIDACY**
- material ownership/authority gap prevents legitimate assignment → **OWNERSHIP_GAP / GOVERNANCE_ESCALATION_CANDIDATE**

Where interface evidence is materially stale, unowned or insufficiently validated, use the narrowest applicable existing class — normally **IMPROVE_MAP_OR_EVIDENCE** or **INTERFACE_OR_INTEGRATION_CANDIDATE** — while preserving review owner/process as UNKNOWN or UNASSIGNED when that is the evidence-supported state.

**OWNERSHIP_GAP / GOVERNANCE_ESCALATION_CANDIDATE** means only that a legitimate ownership/governance process may need to resolve the gap. It does not authorise SMM or the assessor to assign an owner.

These outputs do not authorise action.

> **Candidate Response ≠ Command**

A host's legitimate priority/resource/action process remains external.

## 20. Ownership and supply

Where material, record:

- legitimate owner;
- distributed suppliers;
- interface suppliers;
- fallback;
- disputed ownership;
- unknown ownership.

SMM cannot create ownership.

Portable ownership state may include **IDENTIFIED**, **DISTRIBUTED**, **UNKNOWN**, **DISPUTED**, and **UNASSIGNED/NO_LEGITIMATE_OWNER_IDENTIFIED**.

> **Need for an Owner ≠ Authority to Invent One**

Distributed or interface supply must remain representable without forcing a false single-owner model.

A host registry may project this state into a simpler schema, but a lossy projection must not redefine the underlying SMM state. A single-owner field may reference a distributed-supply record rather than inventing one owner.

Minimum distributed-supply reference pattern:

**DS_REF = <function-ID, supply-record-ID, supplier-set, interface/reference set, projection-loss flag>**

A host may serialize this differently, but a projection that omits suppliers/interfaces must retain a reference to the authoritative distributed-supply record and identify that loss. A simplified export is not authoritative merely because it is easier to consume.

## 21. Evidence and provenance

Consequential state claims should link to evidence.

Evidence may include:

- specifications/architecture;
- operating records;
- tests;
- audits;
- metrics;
- user/participant reports;
- failure records;
- external evidence.

A minimum state-claim record may be:

**E_s = <claim, function, context, evidence/source, evaluator/process, time, scope, confidence, uncertainty>**

Confidence is evidence about the assessment, not a guarantee of truth.

For an interface-satisfied function, record where material the evidence source/provider, refresh or review owner/process, freshness, validation scope and uncertainty. This does not transfer evidence ownership to SMM.

The refresh/review owner or process may legitimately be **UNKNOWN** or **UNASSIGNED**. SMM must not invent a local owner to complete the record. Where the missing stewardship itself creates material uncertainty or integration risk, expose the corresponding bounded candidate response without assigning authority.

## 22. Freshness

Operational state should support, where material:

- state date;
- evidence date;
- last review;
- next review/backstop;
- changed-since-review;
- stale-state flag.

A stale state creates review pressure.

It does not automatically invert or erase the prior state.

Where evidence shows a material context, dependency or capability change since review, an old SUFFICIENT claim must not be presented as unqualified current SUFFICIENT without revalidation. The prior state remains historically valid as a prior assessment.

Portable default: where material change is established and no new assessment supports a current sufficiency claim, **current sufficiency = UNKNOWN (REVIEW DUE)** while the prior SUFFICIENT state remains preserved historically.

A host may use an equivalent bounded state such as prior-state-with-review-due only if it cannot be mistaken for unqualified current SUFFICIENT.

## 23. Active work state

Optional active-work metadata may include:

- NONE
- INVESTIGATING
- SOURCE_RESOLUTION
- FROZEN_FOR_TEST
- DEVELOPMENT_ACTIVE
- EVALUATION
- AWAITING_INTEGRATION
- INTEGRATED_AWAITING_RETEST
- RETEST
- HOLD
- CLOSED

Hosts may map these to local workflow vocabulary.

Where the relevant gap already has legitimate active work, SMM may emit **CONTINUE_EXISTING_WORK / NO_NEW_CANDIDACY** so downstream queues do not create duplicate development merely because the underlying gap remains open.

**HOLD** is an active-work/workflow state: work exists or has been considered but is legitimately paused/deferred.

**NO_ACTION_CANDIDATE** is a candidate-response state: the current SMM assessment does not expose a material action candidate for the declared context.

They may coexist, but they are not synonyms. HOLD does not imply sufficiency, and NO_ACTION_CANDIDATE does not imply that a work item is on hold.

The purpose is to distinguish unresolved work from work already being addressed and to distinguish workflow state from candidate response.

## 24. Minimum portable state record

**SMR = <ID, function, owner/suppliers, context, presence, maturity dimensions, sufficiency, dependencies, blockers, interfaces, consequence/exposure, unresolved requirements, gap/state class, candidate response, evidence/provenance, confidence, uncertainty/dispute, freshness/review, active-work state>**

UNKNOWN and NOT_APPLICABLE are legitimate values. Missing data must not be silently converted into negative state.

## 25. State transition and history

State update:

**SM_t → SM_t+1**

Material transitions should preserve:

- prior state;
- new state;
- what changed;
- why;
- evidence;
- evaluator/process;
- known downstream review effects;
- unresolved disagreement.

> **Current State Must Not Silently Erase the Path to Current State**

Where material, assessment relations should be explicit, for example **CORRECTS**, **SUPERSEDES**, **QUALIFIES**, **DISPUTES**, or **CONFIRMS**. A later assessment must not silently overwrite competing evidence.

Assessment relations should carry scope where the relation is not global:

**AR = <new-assessment-ID, relation, prior-assessment-ID, applicable context/scope, effective time, evidence/rationale>**

A scope-limited SUPERSEDES or QUALIFIES relation changes current interpretation only within its declared scope. Outside that scope, the earlier assessment may remain current if otherwise valid. CORRECTS preserves the corrected record as historical evidence rather than deleting it.

## 26. Update/review conditions

A record may require reconsideration when:

- underlying function changes;
- dependency changes;
- interface changes;
- new evidence appears;
- failure occurs;
- correction propagates;
- deployment context changes;
- a materially affected user/participant class changes;
- review becomes overdue;
- a prediction/test fails;
- a legitimate challenge is raised.

SMM defines reasons a state may need reconsideration. It does not require one particular scheduler or trigger implementation.

## 27. Minimum operating cycle

1. **DEFINE** — identify function/unit and declared context.
2. **RESOLVE** — identify supply, ownership, interfaces and evidence boundary.
3. **REPRESENT** — record presence and applicable maturity dimensions.
4. **ASSESS** — determine context-relative sufficiency.
5. **TRACE** — represent material dependencies/blockers.
6. **EXPOSE** — record consequence/exposure and uncertainty.
7. **CLASSIFY** — assign bounded gap/state class.
8. **CANDIDATE** — produce a non-authoritative response candidate if warranted.
9. **REVIEW** — preserve evidence, freshness and challenge routes.
10. **UPDATE** — record transition without erasing prior state.
11. **STOP/HOLD** — permit adequate, blocked, unknown, disputed or no-current-development states.

## 28. Worked example 1 — distributed software capability

A platform requires audit logging.

Service A has no local audit logger. A shared infrastructure service supplies signed audit records through a validated interface.

Incorrect classification:

> ABSENT because Service A has no logger.

SMM classification:

- presence: INTERFACE_SATISFIED;
- maturity: evaluate the relevant audit dimensions against the shared interface;
- sufficiency: context-dependent;
- dependency: shared logging infrastructure;
- gap: SATISFIED unless a material interface/maturity deficit is found.

## 29. Worked example 2 — dependency-blocked engineering function

A test programme has a mature analysis pipeline, but required sensor calibration is incomplete.

Incorrect classification:

> Analysis capability is immature.

SMM classification:

- presence: PRESENT_EXPLICIT;
- relevant maturity dimensions: may be satisfied;
- sufficiency for current operational test: BLOCKED;
- blocker: calibration prerequisite;
- gap/state: DEPENDENCY_BLOCKED;
- candidate response: RESOLVE_UPSTREAM_CANDIDATE.

## 30. Worked example 3 — context-relative sufficiency

A decision-support model is adequate for internal exploratory analysis but has not been validated for autonomous consequential control.

SMM may represent:

**Context A — exploratory/advisory**
- presence: PRESENT_EXPLICIT;
- sufficiency: SUFFICIENT.

**Context B — autonomous consequential control**
- same underlying function;
- higher/different applicable maturity requirements;
- sufficiency: INSUFFICIENT or UNKNOWN.

The function does not possess one universal sufficiency state independent of context.

## 31. Worked example 4 — low-centrality high-consequence deficit

A rarely used emergency shutdown interface has few dependencies and little network centrality, but failure could create severe irreversible harm.

SMM records the low connectivity without allowing it to erase consequence/exposure.

Priority remains external, but the state representation preserves the information needed to avoid centrality-only selection.

## 32. Worked example 5 — stale state

A capability was assessed SUFFICIENT two years ago. Its dependency and deployment environment have since changed.

SMM does not automatically declare it insufficient.

Instead:

- prior state remains reconstructable;
- stale-state flag = TRUE;
- changed-since-review = TRUE;
- portable-default current sufficiency = UNKNOWN (REVIEW DUE);
- a host-equivalent prior-state-with-review-due label is acceptable only if it cannot appear as unqualified current SUFFICIENT;
- review candidacy is exposed.

## 33. Failure modes

**SMM-F1 — False completeness**  
Unrepresented function appears complete or irrelevant.

**SMM-F2 — False maturity**  
Documentation, formalisation or labels substitute for capability.

**SMM-F3 — Presence/maturity collapse**  
Presence is treated as adequate development.

**SMM-F4 — Maturity/sufficiency collapse**  
General maturity is treated as sufficient for every context.

**SMM-F5 — Locality error**  
Locally absent capability is treated as systemically absent.

**SMM-F6 — Interface blindness**  
Externally/interface-supplied capability is missed.

**SMM-F7 — Dependency blindness**  
Blocked downstream function is treated as locally deficient.

**SMM-F8 — Centrality bias**  
Highly connected items dominate while low-connectivity high-consequence deficits disappear.

**SMM-F9 — Staleness**  
Old state drives current judgement without reconsideration.

**SMM-F10 — Ownership fabrication**  
The map assigns a convenient owner.

**SMM-F11 — Authority capture**  
State classification becomes command/resource authority.

**SMM-F12 — Score collapse**  
Multidimensional state is hidden by an unjustified scalar score.

**SMM-F13 — Uncertainty erasure**  
UNKNOWN/DISPUTED is forced into binary classification.

**SMM-F14 — Anti-gaming failure**  
Labels, prose or state manipulation improve apparent maturity without capability.

**SMM-F15 — History erasure**  
Current state destroys provenance of prior states/corrections.

**SMM-F16 — Perpetual-development bias**  
The model cannot represent adequate sufficiency, HOLD or legitimate stopping.

## 34. Anti-gaming requirements

A host should not improve represented maturity merely by:

- renaming a state;
- increasing document volume;
- adding untested requirements;
- declaring a capability complete;
- splitting one unresolved function into many apparently complete records;
- moving a deficit across an interface without validating supply;
- hiding UNKNOWN/DISPUTED data;
- changing aggregation weights to improve a headline score.

Where consequential, state claims require evidence/provenance and remain challengeable.

## 35. Stopping and hold behaviour

SMM must be able to represent:

- no known material insufficiency in the declared context;
- no action currently required;
- dependency-blocked work;
- investigation rather than development;
- disputed state;
- legitimate HOLD.

It must not create development work merely to keep the mapping process active.

> **No Current Development Candidate ≠ Perfect System**

## 36. Minimum implementation requirements

A conforming implementation should:

1. define assessed function/unit and context;
2. keep presence separate from maturity;
3. keep maturity separate from sufficiency;
4. represent distributed/interface supply;
5. preserve dependency blockage separately from local deficiency;
6. preserve UNKNOWN and DISPUTED;
7. use evidence/provenance for consequential state claims;
8. support freshness/staleness;
9. preserve prior state/history;
10. externalise legitimate ownership/authority;
11. avoid mandatory universal scalar maturity scoring;
12. expose consequence independently of network centrality;
13. produce only bounded response candidacy;
14. permit adequate/hold/stop states;
15. identify the declared search/evidence boundary for candidate absence;
16. preserve context-set references through lossy host schemas;
17. preserve distributed-supply references through simplified projections;
18. scope material assessment relations;
19. distinguish HOLD workflow state from NO_ACTION candidate response;
20. carry or reference material consequence/exposure through downstream projections.

## 37. Non-requirements

SMM does not require:

- Concord;
- the Civilisation Clock;
- KCS;
- CDT;
- a universal maturity scale;
- a universal dependency graph;
- one owner per function;
- automated prioritisation;
- automated remediation;
- a single source of truth;
- complete knowledge of the host system.

## 38. External interfaces

SMM may interface with:

- architecture/function registries;
- dependency systems;
- evidence/provenance stores;
- review/trigger systems;
- project/workflow systems;
- risk/consequence models;
- ownership/governance systems;
- prioritisation/resource processes.

Interfaces do not transfer ownership automatically.

## 39. Falsification and revision conditions

The portable architecture should be revised or rejected if independent transfer shows that:

- presence/maturity/sufficiency cannot remain meaningfully distinct;
- distributed/interface supply cannot be represented without host-specific Concord machinery;
- dependency blockage cannot be separated from local deficiency;
- context-relative sufficiency is unusable outside civil architecture;
- UNKNOWN/DISPUTED cannot be operationally preserved;
- candidate response cannot remain separate from substantive authority;
- the model systematically hides low-connectivity high-consequence deficits;
- state history/provenance cannot be preserved without importing KCS;
- the architecture cannot produce legitimate hold/stop states;
- the required record becomes so broad that it ceases to be a bounded portable mechanism.

## 40. Validation status

Source evidence includes canonical formalisation, populated internal State Map work, frozen prospective queue rules, a graph-selected bottleneck test and later frozen State Map inputs.

Independent transfer evidence:

> **BTT-001: SMM-T3 FUNCTIONAL TRANSFER — 50 / 50 FROZEN PREDICTIONS MATERIALLY CONFIRMED; 0 / 14 FUNDAMENTAL FAILURES**

> **BTT-002: SMM-T3 FUNCTIONAL TRANSFER — 52 / 52 FROZEN PREDICTIONS MATERIALLY CONFIRMED; 0 / 14 FUNDAMENTAL FAILURES**

Cross-test evidence summary:

> **102 / 102 FROZEN PREDICTIONS MATERIALLY CONFIRMED ACROSS TWO MATERIALLY DIFFERENT NON-CONCORD DOMAINS**

> **0 / 28 TEST-SPECIFIC FUNDAMENTAL-FAILURE CHECKS OBSERVED**

> **CROSS-TEST CONVERGENCE: ESTABLISHED**

These counts are evidence summaries, not statistical probabilities or claims of universal validity.

v0.3 incorporates only bounded specification/interface clarifications supported by the two-test evidence. It does not add a new SMM kernel mechanism.

> **v1.0 — GRADUATED PORTABLE MODULE / SPECIFICATION-LEVEL TRANSFER VALIDATED**

## 41. Provenance and validation boundary

This graduation candidate derives from the resolved SMM source architecture and the PMEDG development record retained alongside it.

Development evidence includes:

- Source Resolution and Extraction Audit 001;
- Portable Specification v0.1;
- BTT-001 frozen brief and expected-findings key;
- BTT-001 independent response and post-test evaluation;
- Portable Specification v0.2;
- BTT-002 frozen brief and expected-findings key;
- BTT-002 independent response and post-test evaluation;
- Cross-Test Convergence Review;
- Portable Specification v0.3;
- v0.3 Evidence and Regression Audit.

The evidence supports specification-level portability across the two tested non-Concord domains. It does not establish universal empirical validity, correctness of every host implementation, completeness of every host state map, or authority to act on an SMM result.

No additional blind transfer test is presently required under the PMEDG trigger rule because the v0.3 convergence revision introduced no materially new kernel mechanism.

## 42. Release status

> **v1.0 — GRADUATED PORTABLE MODULE / SPECIFICATION-LEVEL TRANSFER VALIDATED**

This release preserves the substantively reviewed v0.3 graduation candidate. Release changes are metadata/status changes only; no new kernel mechanism is introduced.

The retained development record contains the source-resolution audit, frozen blind-test materials, independent responses, post-test evaluations, convergence review, v0.3 regression audit, consistency check and Portable-Package Graduation Review.

Future material mechanism changes should return to PMEDG development rather than being silently folded into this release.