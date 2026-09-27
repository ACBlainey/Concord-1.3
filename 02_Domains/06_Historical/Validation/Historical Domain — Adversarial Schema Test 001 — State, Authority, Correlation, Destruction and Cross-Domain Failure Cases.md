# Historical Domain — Adversarial Schema Test 001 — State, Authority, Correlation, Destruction and Cross-Domain Failure Cases

**Project:** The Concord
**Domain:** Historical
**Status:** ADVERSARIAL DEVELOPMENT TEST / NOT CANONICAL
**Date:** 25 September 2026
**Target:** Formal Schema Set 001

## 1. Test objective

This test attempts to make the formal schemas silently misrepresent history.

A successful schema should not necessarily solve every external legal, constitutional or operational conflict. It should instead preserve the conflict, scope, provenance and unresolved state without collapsing them into a false answer.

Failure classes:

- **SILENT FAILURE** — schema can represent a false/simple state while losing a material distinction.
- **VISIBLE INCOMPLETENESS** — schema cannot resolve the issue but records that it cannot.
- **EXTERNAL RESOLUTION REQUIRED** — Historical correctly represents the state while another legitimate system must decide it.
- **PASS** — existing objects/interfaces represent the case without material loss.

---

## 2. Case 1 — Repeated privacy-state change

A participant record moves:

PRIVATE → SEALED → PARTIALLY DISCLOSED → RESEALED → ANONYMISED.

If HSO-1 stores only the latest PrivacyState, the sequence is lost.

HIST-1 solves the transition history, but HSO-1 must not imply that its current Historical state field is the complete history.

**Result: PASS WITH REQUIREMENT.**

Requirement: state-bearing fields in HSO-1 are snapshot state; consequential changes must reference transition history.

New rule:

> **Current Historical Object State ≠ Historical State Sequence.**

---

## 3. Case 2 — Authority valid at exercise, later adjudicated unlawful

At T1 an actor exercises authority accepted as valid. At T2 a court rules the authority was unlawful.

HAE-1 can preserve contemporaneous recognition, exercise, contest and later adjudication separately.

The original event must not be rewritten to "no authority event occurred." Nor may later adjudication be omitted from present reconstruction.

**Result: PASS.**

> **Later Invalidity ≠ Historical Non-Occurrence.**

---

## 4. Case 3 — Source destroyed, trained model survives

Personal source data is legitimately destroyed. A model trained on it survives.

HIST-1 can reference KnownDerivativeRefs, but a trained model may not permit clean removal of an individual contribution and may have uncertain reconstructive leakage.

The binary derivative question is insufficient.

A derivative needs a residual-dependence state.

Candidate states:

- INDEPENDENT_NONIDENTIFYING;
- AGGREGATE_DEPENDENCE;
- CONTRIBUTION_PRESENT_NONEXTRACTABLE;
- RECONSTRUCTION_RISK;
- IDENTIFYING_DERIVATIVE;
- DEPENDENCE_UNKNOWN.

**Result: SCHEMA REFINEMENT REQUIRED.**

New object/extension: **Derivative Residual State**.

---

## 5. Case 4 — Anonymous records reidentified through graph joins

Three records are independently anonymous. Combining time, location and relationship edges identifies a participant.

HCP-1 correctly makes correlation separately permissioned, but HSO-1/HPR-1 need a way to express that identity exposure is contextual rather than intrinsic to one record.

A record can be non-identifying alone and identifying in combination.

**Result: PASS WITH REFINEMENT.**

New rule:

> **Non-Identifying in Isolation ≠ Non-Identifying in Combination.**

Candidate field: ReidentificationRiskContextRefs.

---

## 6. Case 5 — Secrecy review is missed

A sealed record reaches ReviewTime but no review occurs.

HSE-1 can represent ReviewTime but CurrentSecrecyState could remain ACTIVE indefinitely unless overdue review is itself machine-visible.

Required derived state:

**REVIEW_OVERDUE / AUTHORITY_FOR_CONTINUED_SECRECY_UNCONFIRMED**

Historical must not automatically disclose the record merely because review was missed; nor may it represent secrecy as freshly justified.

**Result: SCHEMA REFINEMENT REQUIRED.**

> **Missed Review ≠ Automatic Disclosure ≠ Rejustified Secrecy.**

---

## 7. Case 6 — Repeated emergency renewal

An emergency authority is renewed five times with changing evidence.

One HAE-1 object repeatedly edited would destroy the justification sequence.

Each renewal must be a distinct Authority Activation and Exercise Record or distinct authority-justification event linked by RENEWS / SUPERSEDES / CONTINUES_FROM relations.

**Result: PASS WITH REFERENTIAL RULE.**

> **Renewal Requires New Justification State.**

---

## 8. Case 7 — KCS changes while Historical remains old by design

At T1 KCS represents proposition P as DISPUTED. At T2 it becomes SUPPORTED.

A query asking "what did KCS represent at T1?" must return DISPUTED even though current KCS says SUPPORTED.

HSO-1 plus HRO-1 can represent this.

Risk: CurrentOperationalRef could tempt implementations to substitute the live object.

Required rule:

> **Live Reference May Locate Current State; It Must Not Override Requested Historical State.**

**Result: PASS.**

---

## 9. Case 8 — Civil Attention reopens a resolved issue

An Issue is resolved at T1 and reopened at T2 after new evidence.

A single ResolutionStatus field is inadequate.

Historical needs transition sequence:

OPEN → ROUTED → DOMAIN_COMPLETE → RESOLVED → REOPENED → ROUTED...

Existing HIST-1 can represent this.

**Result: PASS.**

The distinction Domain Completion ≠ Issue Resolution remains necessary.

---

## 10. Case 9 — Replica offline during destruction

Three legitimate replicas exist. A destruction transition reaches two; the third is offline.

HRI-1 and HIST-1 can represent PendingInformationStateTransitions and ReconciliationStatus.

The dangerous state is claiming DELETED globally.

Required completion states:

- COMPLETE_WITHIN_KNOWN_REACHABLE_SCOPE;
- PENDING_REPLICA;
- PARTIALLY_EXECUTED;
- EXECUTION_SCOPE_UNKNOWN;
- RECONCILED.

**Result: PASS WITH ENUMERATION REFINEMENT.**

> **Deletion Requested ≠ Deletion Executed ≠ Deletion Reconciled.**

---

## 11. Case 10 — Later evidence exposes an unrepresented dimension

A historical decision appears well-supported until a later discovery reveals a variable that contemporary actors did not represent.

HEC-1 explicitly supports LATER_RECOGNISED_UNREPRESENTED_DIMENSION.

The danger is a Present-Best reconstruction contaminating Contemporary-State reconstruction.

HRO-1 supports separation.

**Result: PASS.**

---

## 12. Case 11 — Incompatible cross-jurisdiction retention states

Jurisdiction A requires destruction. Jurisdiction B requires retention.

Historical must not collapse these into one RetentionState.

This exposes a real schema weakness: state may be jurisdiction-relative.

Required pattern:

**State + ApplicableContext/Jurisdiction**

Candidate new object: **Contextual State Assertion**.

It can represent simultaneous claims:

- A: DESTROY_REQUIRED;
- B: RETAIN_REQUIRED;
- conflict: UNRESOLVED;
- current executing authority: separately identified.

Historical must not adjudicate the conflict itself.

**Result: SCHEMA REFINEMENT REQUIRED / EXTERNAL RESOLUTION REQUIRED.**

> **Conflicting Valid State Claims ≠ One Global State.**

---

## 13. Case 12 — Preserved capability cannot be restored

Historical has complete documents for an old system but lost tacit skill, hardware or dependency.

The schema set references capability recoverability but lacks a dedicated object.

Candidate recoverability states:

- DOCUMENTED_ONLY;
- PARTIALLY_RECONSTRUCTABLE;
- TECHNICALLY_RECONSTRUCTABLE;
- OPERATIONALLY_RESTORABLE;
- RESTORATION_UNVERIFIED;
- UNRECOVERABLE_WITH_KNOWN_RESOURCES;
- RECOVERABILITY_UNKNOWN.

Historical must not infer capability from documentation.

**Result: SCHEMA REFINEMENT REQUIRED.**

> **Documentation Completeness ≠ Capability Recoverability.**

---

## 14. Case 13 — Retrospective testimony mistaken for contemporaneous evidence

A witness writes an account 30 years after an event.

HSO-1 distinguishes EventTime from RecordCreationTime and HEC-1 can distinguish evidence available at T.

The record remains historically valuable but cannot silently enter the contemporary evidence set.

**Result: PASS.**

> **Evidence About T ≠ Evidence Available At T.**

---

## 15. Case 14 — Event Spine omits inaccessible domain

An Event Spine view reconstructs a chain across Governance, KCS and Judiciary, but one relevant domain is inaccessible.

HES-1 contains SourceCoverage and SearchBoundaryRefs.

The output must surface the gap rather than render a visually continuous chain that implies completeness.

Required state:

**SPINE_INCOMPLETE_KNOWN_GAP**.

**Result: PASS WITH PRESENTATION REQUIREMENT.**

> **Continuous Visualisation ≠ Complete Causal or Evidential Chain.**

---

## 16. Case 15 — Records individually accessible but correlation forbidden

A researcher may inspect A and B separately but lacks authority to correlate them.

HCP-1 directly represents this.

Historical query tooling must prevent derived joins, not merely raw retrieval.

**Result: PASS.**

---

## 17. Case 16 — Destruction residue becomes a reconstruction key

HMHR-1 stores record class, time, authority and derivative classes. Combined with public information, those metadata identify the destroyed subject.

The current Minimum Residue schema acknowledges ReconstructionRiskAssessment but does not require minimisation after contextual reidentification analysis.

Required rule:

> **Minimum Residue Is Determined by Reconstructive Risk, Not Field Count.**

A residue itself must be subject to privacy/correlation review.

**Result: SCHEMA REFINEMENT REQUIRED.**

---

## 18. Case 17 — Authority conditions satisfied by evidence later found fabricated

At T1 the authority chain appears valid because evidence E is accepted. At T2 E is proven fabricated.

HAE-1 + HEC-1 + correction relationships can represent both states.

Historical must distinguish:

- authority justified within represented evidence at T;
- whether evidence was legitimately obtained/assessed;
- later discovery of fabrication;
- later adjudication of authority validity.

Historical should not itself decide the legal consequence.

**Result: PASS / EXTERNAL ADJUDICATION MAY BE REQUIRED.**

---

## 19. Case 18 — Authority action itself creates the evidence for renewed authority

Emergency surveillance A1 discovers evidence E1, then E1 is used to justify A2.

This is legitimate in some contexts but dangerous because authority can become self-reinforcing.

The schema can represent the chain, but it should explicitly expose evidence provenance:

A1 → produces E1 → E1 contributes to justification for A2.

This enables the Authority Justification Chain to test authority-generated evidence.

**Result: PASS WITH RELATIONSHIP REQUIREMENT.**

> **Authority-Generated Evidence Must Remain Traceable to the Authority That Generated It.**

---

## 20. Case 19 — Classification taxonomy changes

A record classified CATEGORY-X at T1 is automatically remapped to CATEGORY-Y after taxonomy migration.

If the old category disappears, historical reconstruction is corrupted.

HSO-1 VersionOrStateID and self-audit help, but classification vocabulary itself requires version reference.

Candidate field:

**ClassificationSchemeRef / ClassificationSchemeVersion**.

**Result: SCHEMA REFINEMENT REQUIRED.**

> **Taxonomy Migration ≠ Historical Reclassification of the Past.**

---

## 21. Case 20 — Same object has simultaneous legitimate states

A document is public in one jurisdiction, sealed in another, and restricted to a cultural community under a third legitimate custody relationship.

This confirms Case 11 is broader than retention.

Privacy, access, secrecy, classification and retention may all be contextual assertions rather than singular global fields.

HSO-1's simple state fields are therefore insufficient as the only representation.

**Result: MATERIAL SCHEMA REFINEMENT REQUIRED.**

The generic solution is a **Contextual State Assertion** layer.

---

## 22. New Schema HCSA-1 — Contextual State Assertion

Candidate schema:

- StateAssertionID
- ObjectOrRelationshipRef
- StateDimension
- StateValue
- ApplicableActorClass
- ApplicablePurpose
- ApplicableJurisdictionOrSpace
- ApplicableContext
- AuthoritySourceRef
- EffectiveStart
- EffectiveEnd
- ReviewCondition
- PriorityOrPrecedenceRef
- ConflictState
- ProvenanceRefs

StateDimension may include:

- PRIVACY;
- ACCESS;
- SECRECY;
- CLASSIFICATION;
- RETENTION;
- DISCOVERABILITY;
- CORRELATION;
- DISCLOSURE;
- PUBLICATION.

This permits multiple simultaneous state assertions without forcing Historical to invent one global answer.

> **Historical State May Be Contextual Without Historical Reality Becoming Arbitrary.**

The assertions themselves remain evidence-bearing, scoped and contestable.

---

## 23. New Schema HDRS-1 — Derivative Residual State

Candidate fields:

- DerivativeStateID
- SourceTransitionRef
- DerivativeRefOrClass
- DerivationType
- ContributionState
- IdentityLeakageRisk
- ReconstructionRisk
- Extractability
- IndependentLegitimateBasis
- RequiredAction
- ExecutionStatus
- ReviewCondition
- ProvenanceRefs

ContributionState may include:

- INDEPENDENT_NONIDENTIFYING;
- AGGREGATE_DEPENDENCE;
- CONTRIBUTION_PRESENT_NONEXTRACTABLE;
- RECONSTRUCTION_RISK;
- IDENTIFYING_DERIVATIVE;
- DEPENDENCE_UNKNOWN.

This object does not decide whether a derivative must be destroyed. It makes the relevant state visible to the legitimate decision-maker.

---

## 24. New Schema HCAP-1 — Capability Recoverability State

Candidate fields:

- CapabilityStateID
- CapabilityRef
- DocumentationRefs
- DependencyRefs
- TacitKnowledgeRefs
- RequiredInfrastructureRefs
- RequiredSkillRefs
- RecoverabilityState
- LastVerifiedTime
- VerificationMethod
- MissingElements
- RestorationAuthorityRef
- ProvenanceRefs

RecoverabilityState may include:

- DOCUMENTED_ONLY;
- PARTIALLY_RECONSTRUCTABLE;
- TECHNICALLY_RECONSTRUCTABLE;
- OPERATIONALLY_RESTORABLE;
- RESTORATION_UNVERIFIED;
- UNRECOVERABLE_WITH_KNOWN_RESOURCES;
- RECOVERABILITY_UNKNOWN.

This remains Historical evidence, not Continuity restoration authority.

---

## 25. Refinement to HSE-1 — Missed Review State

Add explicit secrecy states:

- REVIEW_DUE;
- REVIEW_OVERDUE;
- CONTINUED_SECRECY_AUTHORITY_UNCONFIRMED.

A missed review neither automatically discloses nor silently reauthorises secrecy.

---

## 26. Refinement to HSO-1

The state fields in HSO-1 should be interpreted as summary/snapshot fields only.

Where a state is context-dependent, HSO-1 should reference HCSA-1 assertions.

Candidate additions:

- ContextualStateAssertionRefs;
- StateSequenceRefs;
- ReidentificationRiskContextRefs;
- ClassificationSchemeRef;
- ClassificationSchemeVersion.

This avoids turning the generic object into an ever-expanding universal record.

---

## 27. Refinement to HIST-1 / HRI-1

Information-state execution requires separate states for:

- REQUESTED;
- AUTHORISED;
- DISPATCHED;
- PARTIALLY_EXECUTED;
- COMPLETE_WITHIN_KNOWN_REACHABLE_SCOPE;
- PENDING_REPLICA;
- RECONCILED;
- EXECUTION_SCOPE_UNKNOWN;
- FAILED;
- CONTESTED.

This prevents a request, local execution and reconciled distributed execution from collapsing into DELETED=true.

---

## 28. Test Summary

Cases passed without material schema change: 2, 7, 8, 10, 13, 15, 17.

Cases passed with explicit referential/presentation refinement: 1, 4, 6, 9, 14, 18.

Cases exposing material schema additions/refinements: 3, 5, 11, 12, 16, 19, 20.

No case demonstrates that the v0.3 conceptual architecture is incoherent.

Instead, the test identifies a deeper implementation principle:

> **Many Historical states are not intrinsic properties of objects. They are scoped relationships between an object, context, authority, actor, purpose, jurisdiction and time.**

This mirrors the BCA result for authority.

It suggests a broader convergence:

**Object + Context + Relationship + Time → Interpretable State**

rather than:

**Object → Permanent State Attribute**

---

## 29. Major Architectural Finding — Contextual State

The strongest new result is HCSA-1.

Historical originally treated privacy, access, secrecy, classification and retention partly as object fields. That is useful as a summary but insufficient as ontology.

The adversarial cases show that the same object can legitimately have multiple simultaneous states depending on jurisdiction, actor, purpose, context and authority source.

Therefore:

> **State Is Often Relational and Contextual, Not Merely Object-Intrinsic.**

This is structurally consistent with:

- Bounded Contextual Authority;
- Contextual Wrapper Architecture;
- purpose-bounded data access;
- jurisdiction;
- protected spaces;
- emergency authority;
- cultural custody.

This may be a cross-Concord pattern rather than a Historical-only discovery.

It should be recorded for later portable-module/topology review, but should not yet be generalised beyond the evidence from this test.

---

## 30. Status

**Adversarial Schema Test 001:** COMPLETE

**Cases tested:** 20

**Conceptual architecture failure:** NONE

**Material schema additions:** HCSA-1 Contextual State Assertion; HDRS-1 Derivative Residual State; HCAP-1 Capability Recoverability State

**Material refinements:** missed secrecy review; distributed execution states; contextual/reidentification references; classification scheme versioning

**Major finding:** State Is Often Relational and Contextual, Not Merely Object-Intrinsic

**Next:** revise Formal Schema Set to v0.2 and then run a smaller cross-object consistency audit before considering Historical domain graduation.
