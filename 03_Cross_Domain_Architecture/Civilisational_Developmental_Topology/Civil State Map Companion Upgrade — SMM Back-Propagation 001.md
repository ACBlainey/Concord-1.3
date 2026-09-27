# Civil State Map Companion Upgrade — SMM Back-Propagation 001

**Author:** Alexander C. Blainey — Independent Researcher
**Project:** The Concord Framework
**Status:** CANONICAL COMPANION UPGRADE — INTEGRATED / ARCHITECTURAL INTERFACE RETEST PASSED
**Parent architecture:** Civil State Map — Maturity, Sufficiency and Consequence Model
**Evidence source:** State and Maturity Mapping — Portable Module v1.0; PMEDG SMM development record
**Development source:** Portable-Module Back-Propagation Audit — Development Note 001
**Interfaces requiring retest:** KCS Companion Upgrade 001; Civilisation Clock; Civilisational Developmental Topology
**Date:** 24 September 2026

---

## Purpose

This companion upgrade returns evidence-supported refinements discovered during portable State and Maturity Mapping (SMM) development to the Concord Civil State Map from which SMM was extracted.

It is additive.

It does not replace the Civil State Map's existing state model:

**SM(t) = <N, P, M, Q, D, C, U, A, R>**

It does not replace the Concord-specific maturity probes, KCS dependency interface, Civilisation Clock interface, baseline procedure, developmental levelling logic or authority boundaries.

The upgrade closes source-level edge conditions exposed during two materially different non-Concord blind-transfer tests and subsequently retained through SMM graduation.

> **Portable Refinement → Source Review → Bounded Reintegration**

not:

> **Portable Module → Automatic Source Replacement**

# 1. Assessment-Unit Resolution

Add to the Civil State Map unit-of-assessment procedure:

Before consequential assessment, declare the function/unit boundary at the granularity relevant to the claim.

Where a missing element is discovered:

1. determine whether it belongs inside the declared function's required supply boundary;
2. if it is separate, assess it separately or as an interface/dependency;
3. if it is supplied but unusable because an upstream prerequisite is unresolved, preserve presence and represent **DEPENDENCY_BLOCKED/BLOCKED**;
4. if only part of the declared required function is supplied, **PARTIAL** may be appropriate;
5. if the function exists but lacks required assurance/development, preserve presence and record the deficit under maturity/sufficiency;
6. if the boundary itself remains unresolved, use **UNKNOWN** or **DISPUTED**.

> **Missing Subfunction ≠ Automatically Partial Presence**

This is a classification aid, not a new universal civil ontology.

# 2. Multi-Context State Preservation

The existing consequence-context model remains valid.

Where one civil function has materially different states in different contexts, the State Map must preserve an explicit context set rather than force one context-free sufficiency label.

A minimum semantic form is:

**C_set = <function, contexts, material fields considered, material omissions/rationale, evidence boundary>**

If a downstream Concord register, dashboard or interface can display only one state, it must either:

- reference the richer context set; or
- declare the displayed state to be a lossy projection.

A portable reference form such as:

**CTX_REF = <function-ID, context-set-ID, selected/display context if any, projection-loss flag>**

may be used, but the literal serialization is implementation-defined.

> **Single Display State ≠ Complete Multi-Context State**

# 3. Candidate Absence and Required-Function Gap

The existing requirement to source-resolve apparent omissions is strengthened.

**CANDIDATE_ABSENT** may be promoted to a true required-function/architectural gap only when:

- the required function is clearly declared;
- a reasonable search/source-resolution boundary is declared;
- obvious local, distributed and interface suppliers have been checked to that boundary;
- materially relevant unavailable sources have been considered;
- residual uncertainty is recorded;
- and the result remains corrigible.

There is no universal numerical search threshold.

If an unavailable source is reasonably capable of changing the conclusion, promotion should normally be blocked.

If its materiality is itself uncertain, preserve **CANDIDATE_ABSENT / UNKNOWN**.

> **No Supply Found Within Search Boundary ≠ Proven Global Absence**

# 4. Aggregate and Summary Safeguards

The Civil State Map continues not to require a universal maturity score.

Where a bounded downstream use nevertheless creates a consequential aggregate or headline summary, disclose at minimum:

**AGG = <purpose, scope/context, included, excluded/N-A, method/weights, unresolved-state disclosure, high-consequence exceptions, evidence/freshness boundary, source-state reference, limitations>**

The exact representation is implementation-defined.

A consequential aggregate should be marked:

**NOT VALID FOR THE PROPOSED USE**

where its representation cannot preserve or trace materially relevant:

- UNKNOWN;
- DISPUTED;
- BLOCKED;
- high-consequence exceptions;
- or the underlying source state.

> **Aggregation Convenience ≠ State Truth**

The aggregate remains a projection and must not replace the underlying State Map record.

# 5. Consequence Carriage to the Civilisation Clock

The existing Clock interface already exports consequence/exposure.

This upgrade adds a preservation rule:

Where State Map information is projected into a ranking, queue or prioritisation representation, material consequence/exposure must either travel with that projection or remain available through a lossless reference.

If the projection discards that information, it must be identified as lossy and must not be treated as a complete State-Map-derived priority representation.

This is particularly important where a low-centrality function carries high consequence.

> **Low Centrality ≠ Low Consequence**

The State Map still does not choose final priority.

# 6. Existing Work and Duplicate Candidacy

The active-development interface is strengthened.

Where a legitimate active development process already addresses the identified deficit, the State Map may return:

**CONTINUE_EXISTING_WORK / NO_NEW_CANDIDACY**

rather than generating a duplicate candidate.

This formalises the existing requirement that the Civilisation Clock avoid repeatedly selecting work already in progress.

It does not assert that existing work is sufficient or successful.

# 7. Ownership Gap and Governance Escalation

The State Map still cannot create ownership.

Where a material deficit exists but no legitimate owner or ownership-resolution route is presently identified, the State Map may classify:

**OWNERSHIP_GAP / GOVERNANCE_ESCALATION_CANDIDATE**

This means only that a legitimate governance/constitutional process may need to resolve the ownership or authority problem.

It does not authorise the State Map, CDT, Clock or assessor to appoint an owner.

> **Need for an Owner ≠ Authority to Invent One**

# 8. Interface-Evidence Stewardship

For **INTERFACE_SATISFIED** or materially externally supplied functions, record where relevant:

- evidence source/provider;
- validation scope;
- evidence date/freshness;
- refresh/review owner or process;
- uncertainty.

The refresh/review owner may legitimately be **UNKNOWN** or **UNASSIGNED**.

The State Map must not invent a local owner merely to complete the record.

Where missing stewardship creates material uncertainty or integration risk, expose the narrowest applicable bounded response, such as:

- **IMPROVE_MAP_OR_EVIDENCE**; or
- **INTERFACE_OR_INTEGRATION_CANDIDATE**.

# 9. Distributed Supply Preservation

The existing Civil State Map already permits distributed suppliers.

This upgrade prevents downstream schemas from silently collapsing that state into a false single owner.

A minimum semantic reference may be represented as:

**DS_REF = <function-ID, supply-record-ID, supplier-set, interface/reference set, projection-loss flag>**

The literal serialization is optional.

A simplified representation that omits suppliers or interfaces must retain a reference to the authoritative distributed-supply state and identify the loss.

> **Simplified Ownership Field ≠ Authoritative Supply Reality**

# 10. Stale Current Sufficiency

The existing rule remains:

> **Stale ≠ False**

This upgrade distinguishes historical validity from an unqualified current claim.

Where evidence establishes a material context, dependency or capability change after the last assessment, an old **SUFFICIENT** result must not remain presented as unqualified current **SUFFICIENT** without revalidation.

Default current representation:

**current sufficiency = UNKNOWN (REVIEW DUE)**

while the previous **SUFFICIENT** assessment remains preserved historically.

An equivalent State Map representation is acceptable only if it cannot reasonably be mistaken for a current validated sufficiency claim.

> **Prior Valid State ≠ Automatically Current Valid State After Material Change**

# 11. Assessment-History Relations

The existing requirement to preserve prior State Map states is strengthened with explicit relation semantics.

A later assessment may relate to a prior assessment as:

- **CORRECTS**
- **SUPERSEDES**
- **QUALIFIES**
- **DISPUTES**
- **CONFIRMS**

A minimum semantic relation is:

**AR = <new-assessment-ID, relation, prior-assessment-ID, applicable context/scope, effective time, evidence/rationale>**

**CORRECTS** preserves the earlier record historically while identifying it as incorrect within the declared correction scope.

**SUPERSEDES** replaces the prior assessment only within the declared scope/context.

**QUALIFIES** narrows or conditions the interpretation of the prior assessment.

**DISPUTES** preserves materially conflicting assessments.

**CONFIRMS** records subsequent support without erasing provenance.

These relations should interface with KCS provenance/change propagation rather than create a parallel history system.

# 12. HOLD and NO_ACTION

The existing vocabularies are retained but explicitly separated.

**HOLD** is an active-development/workflow state. It means existing work is paused, deferred or otherwise held.

**NO_ACTION_CANDIDATE** is an assessment output. It means the current State Map assessment does not justify a material new action candidate in the declared context.

They may coexist.

> **HOLD ≠ NO_ACTION**

> **HOLD ≠ SUFFICIENT**

> **NO_ACTION_CANDIDATE ≠ Permanent Completion**

# 13. Updated Candidate-Response Vocabulary

For State Map operation after this companion upgrade, the bounded candidate responses are:

- SATISFIED → **NO_ACTION_CANDIDATE**
- REPRESENTATION_GAP → **IMPROVE_MAP_OR_EVIDENCE**
- INTEGRATION_INTERFACE_GAP → **INTERFACE_OR_INTEGRATION_CANDIDATE**
- DEVELOPMENTAL_GAP → **DEVELOP_EXISTING_OWNER_CANDIDATE**
- TRUE_ARCHITECTURAL_GAP → **NEW_ARCHITECTURE_CANDIDATE**
- DEPENDENCY_BLOCKED → **RESOLVE_UPSTREAM_CANDIDATE**
- UNKNOWN → **INVESTIGATION_CANDIDATE**
- DISPUTED → **PRESERVE_AND_REVIEW_CANDIDATE**
- legitimate active work already addresses the gap → **CONTINUE_EXISTING_WORK / NO_NEW_CANDIDACY**
- material ownership/authority gap → **OWNERSHIP_GAP / GOVERNANCE_ESCALATION_CANDIDATE**

These are review/development candidates, not commands.

# 14. Minimum State Map Record Additions

The existing minimum State Map record remains the foundation.

Where material, it should additionally support:

- declared assessment-unit boundary;
- context-set/reference;
- projection-loss state;
- distributed-supply reference;
- interface-evidence stewardship state;
- current versus historical sufficiency distinction;
- assessment-history relation;
- ownership-gap state;
- aggregate disclosure/reference where an aggregate exists;
- consequence/exposure reference through downstream projections;
- distinction between HOLD and NO_ACTION_CANDIDATE.

Not every implementation must serialize these identically.

# 15. Updated Failure-Mode Safeguards

The parent State Map's failure modes remain valid.

This companion adds explicit protection against:

**Context collapse** — one displayed state hides materially different context states.  
Safeguard: context-set preservation and lossy-projection declaration.

**Premature absence certainty** — bounded non-discovery becomes a claimed true architectural gap.  
Safeguard: candidate-absence escalation boundary.

**Aggregate masking** — a headline score hides UNKNOWN, DISPUTED, BLOCKED or high-consequence exceptions.  
Safeguard: aggregate disclosure/refusal rule.

**Distributed-supply collapse** — a one-owner schema invents or implies false ownership.  
Safeguard: distributed-supply reference and projection-loss marking.

**Stale-current leakage** — a historically valid state remains presented as current after material change.  
Safeguard: current UNKNOWN (REVIEW DUE) pending revalidation.

**Ownership fabrication** — a real gap causes the mapper to invent an owner.  
Safeguard: ownership-gap/governance-escalation candidacy.

**History overreach** — a later assessment silently replaces a prior assessment beyond the scope justified by evidence.  
Safeguard: scoped assessment relations.

**Duplicate development** — a known deficit repeatedly generates new work despite legitimate work already addressing it.  
Safeguard: CONTINUE_EXISTING_WORK / NO_NEW_CANDIDACY.

**Workflow/action collapse** — HOLD is mistaken for no action need or no-action output is mistaken for a workflow hold.  
Safeguard: explicit semantic separation.

# 16. Authority Boundary

Nothing in this companion changes the State Map's authority.

The State Map may represent, classify, expose and route candidate needs.

It does not:

- allocate resources;
- command development;
- appoint owners;
- determine substantive constitutional outcomes;
- replace KCS provenance;
- replace the Civilisation Clock;
- own the full dependency graph;
- define universal maturity or severity scales.

> **State Description ≠ Permission**

> **Development Need ≠ Governance Authority**

> **Candidate Response ≠ Command**

# 17. Integration With Existing Concord Architecture

The intended integrated relation is:

**CDT required functions / topology**
→ **KCS dependency + provenance state**
→ **Civil State Map + SMM Back-Propagation 001**
→ **Civilisation Clock review/development eligibility**
→ **legitimate domain owner / governance process**
→ **state update + KCS propagation**

The companion therefore strengthens existing interfaces rather than creating a new civil authority.

# 18. Retest Requirements

Before this companion is treated as fully integrated canonical capability, perform a bounded interface regression review against:

### KCS

Check that:

- CORRECTS/SUPERSEDES/QUALIFIES/DISPUTES/CONFIRMS can be carried through existing provenance/change relations without contradiction;
- distributed supply and evidence references do not create duplicate ownership systems;
- state changes after material updates can trigger appropriate review without destroying history.

### Civilisation Clock

Check that:

- consequence/exposure survives queue projection;
- CONTINUE_EXISTING_WORK suppresses duplicate candidacy without hiding unresolved insufficiency;
- OWNERSHIP_GAP routes to legitimate review rather than arbitrary assignment;
- UNKNOWN (REVIEW DUE) can create review pressure without being interpreted as automatic insufficiency;
- NO_ACTION_CANDIDATE remains distinct from HOLD and permanent completion.

### CDT / State Map

Check that:

- assessment-unit rules do not alter the canonical topology merely to simplify classification;
- multi-context and distributed-supply representations remain tractable;
- candidate-absence escalation remains compatible with ESCP/source-resolution discipline.

# 19. Evidence Boundary

The refinements in this companion were not invented solely during reintegration.

They were traced in the SMM v0.3 Evidence and Regression Audit to pressures observed before v0.3 in BTT-001 and BTT-002.

Across those two blind transfer tests:

- **102 / 102 frozen predictions were materially confirmed**;
- **0 / 28 test-specific fundamental-failure indicators were observed**;
- both independent evaluations classified SMM as **SMM-T3 — FUNCTIONAL TRANSFER**;
- the convergence audit found no wholly unpredicted mechanism failure;
- the v0.3 regression audit found no kernel regression, authority expansion or unsupported universalisation.

These counts are evidence summaries, not statistical probabilities and not proof of universal validity.

Their relevance here is narrower: the twelve refinements being returned to the Civil State Map have documented pre-graduation evidence origins rather than being arbitrary post hoc additions.

# 20. Current Status

This companion is:

> **CANONICAL COMPANION UPGRADE — INTEGRATED / ARCHITECTURAL INTERFACE RETEST PASSED**

The bounded interface regression defined in Section 18 has now been completed in:

**Civil State Map — SMM Back-Propagation 001 — Interface Regression Review**

Result:

- KCS interface: PASS with one bounded assessment-relation vocabulary follow-up;
- Civilisation Clock interface: PASS;
- CDT / State Map interface: PASS;
- twelve returned SMM refinements: 12 / 12 PASS;
- authority regression: none observed;
- epistemic regression: none observed.

The companion may therefore be treated as part of the current integrated Civil State Map architecture at the architectural-interface level.

This does not establish implementation correctness or empirical outcome validity.

# Conclusion

The SMM back-propagation pilot demonstrates a real two-way developmental relationship between Concord source systems and their extracted portable modules.

The Civil State Map supplied the original mechanism.

PMEDG transfer testing then exposed and resolved edge conditions that were not fully represented in the source architecture.

This companion returns those tested refinements without replacing the source system or importing portable abstraction indiscriminately.

The resulting developmental path is:

**Concord Source → Portable Extraction → Independent Transfer Pressure → Evidence-Supported Refinement → Graduated Module → Source-Relevance Audit → Companion Upgrade → Interface Retest → Integrated Capability**

This closes the first identified back-propagation loop while preserving provenance, authority boundaries and corrigibility.
