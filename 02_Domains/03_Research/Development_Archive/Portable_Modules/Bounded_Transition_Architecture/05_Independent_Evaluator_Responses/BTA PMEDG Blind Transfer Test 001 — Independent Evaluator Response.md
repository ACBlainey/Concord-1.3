## Evaluator result — PMEDG Blind Transfer Test 001  
**Scenario:** Museum Collection Relocation  
**Specification under test:** Bounded Transition Architecture — Portable Specification v0.1  
**Evaluator position:** Clean evaluator, using only the portable spec and frozen test brief. No hidden key or Concord architecture imported.

---

## A. BTA applicability

**Yes — this is an appropriate BTA case.**

It passes the materiality gate because the relocation materially affects:

- legal title/ownership references;
- physical custody;
- conservation approval;
- secure-storage access;
- public-display approval;
- insurance cover;
- catalogue/provenance;
- emergency recovery;
- continuity and external consequences;
- unresolved partial crossing and residual state.

Routine local changes remain local. BTA is appropriate here as a coordination grammar among independently owned museum functions — not as a universal event logger, and not as a replacement for any museum authority.

---

## B. Transition identity and scope

A stable `TransitionID` should bind the relocation, e.g. `MUSEUM-RELOC-2026-001`.

**Object/function refs:** the collection of 240 archaeological objects, plus per-object refs where material.

**Scope:** relocation from Building A to Building B and the materially relevant coordination dimensions around that relocation:

- physical movement/arrival;
- arrival-condition inspection;
- conservation/storage clearance;
- physical custody acceptance;
- secure-storage access;
- public-display approval;
- insurance dependencies;
- catalogue/provenance;
- recovery/rollback state;
- unresolved residual effects.

**Explicitly outside scope or externally owned:**

- legal title transfer — title is retained by the museum throughout;
- conservation determinations;
- insurance coverage decisions and notification obligations;
- public-display approval;
- custody acceptance decisions;
- catalogue semantics and archival custody;
- final installed-inventory schedule;
- public opening decision.

**Topology:** one relocation transition with many object sub-transitions; many-to-many across owner functions. `ObjectCardinality` is many objects; relational topology is not identical to object cardinality.

A minimal BTA record would bind the relocation ID, object refs, scope, prior valid state refs, transition basis refs, current transition-state refs, completion-condition refs, next-state refs, and provenance.

---

## C. Owner/state map

| Dimension | Legitimate owner | State on assessed day | BTA common class |
|---|---|---|---|
| Legal title | Museum collection ownership/legal title function | Retained for all 240 objects | Not a transition; protected/preserved |
| Physical location | Museum transport/collection function | 180 at B; 60 at A | PARTIAL_OR_INTERMEDIATE |
| Arrival-condition inspection | Conservation/inspection function | 150 passed; 30 isolated, determination pending | PARTIAL / RESIDUAL_OR_UNRESOLVED |
| Conservation/storage clearance | Conservation function | 150 inspected objects authorised into store; 30 not cleared | PARTIAL |
| Secure-store environmental commissioning | Building B secure collection store | Passed | COMPLETED locally |
| Physical custody | Building A/B custody functions | 150 accepted by B; 30 formal acceptance pending; 60 remain at A | PARTIAL / PENDING |
| Removal/access authority | Building A/B access owners | A staff no routine removal authority over 180 arrived; B custody accepted 150 | CHANGED / PARTIAL |
| Public-display approval | Exhibition/display approval owner | Not transferred; B must obtain separate approval | NOT_STARTED / PENDING |
| Insurance | Insurer | Transit cover confirmed; permanent-location cover not effective until final installed-inventory schedule | PENDING / dependency |
| Insurance notification | Insurer / museum insurance function | Packaging-damage incident notification obligation not yet determined | UNRESOLVED |
| Catalogue/provenance | Catalogue/provenance function | Records relocation events and current locations | Active/ongoing |
| Emergency recovery | Recovery planning function | Can return 60 at A to prior storage; cannot exactly restore 180 arrivals | PARTIAL / residual |
| Transport vehicle fault | Transport/safety function | Refrigeration fault occurred; no object aboard; repaired, independently checked, returned to service | FAILED then recovered/resolved for vehicle; no object-transition effect |

---

## D. Completion analysis

**The overall relocation must not be treated as complete.**

Local completions exist:

- 180 objects physically arrived at B;
- 150 passed arrival-condition inspection;
- B secure store passed environmental commissioning;
- conservation authorised inspected objects into store;
- B custody accepted 150 cleared arrivals;
- transit cover confirmed;
- vehicle fault repaired, checked, returned to service.

But integrated relocation completion is blocked by material pending/unresolved conditions:

- 60 objects remain at A;
- 30 isolated arrivals are unresolved;
- 30 lack conservation/storage clearance;
- 30 lack formal custody acceptance;
- Building B public-display approval has not been obtained;
- permanent-location insurance is not effective;
- final installed-inventory schedule cannot be finalised;
- public opening is postponed;
- insurance-notification obligation is unresolved.

BTA may only report whether the declared integration contract shows required referenced conditions as satisfied, pending, failed or unresolved. It must not invent the substantive completion criteria. **Local completion ≠ integrated transition completion.**

---

## E. Non-propagation findings

The following must not be inferred or propagated:

- physical arrival → custody acceptance;
- custody acceptance → transfer of legal title;
- environmental commissioning → conservation clearance for the 30 isolated objects;
- conservation clearance for 150 → clearance for the 30 isolated objects;
- A staff removal authority revoked over 180 → B access/authority active for all 180;
- B operating/accepting 150 → full responsibility transferred;
- prior Building A display approval → valid Building B display approval;
- transit insurance → permanent-location insurance;
- catalogue location record → custody, title or insurance status;
- partial validation → overall relocation completion;
- vehicle fault repaired → no failed event occurred;
- no object aboard faulty vehicle → no material event at all, if host treats transport fault as material;
- relocation authorised in principle → completion.

---

## F. Authority, permission and surviving-duty analysis

**Represented authority/permission changes:**

- relocation authorised in principle — `TransitionBasisRef`;
- A staff routine removal authority over the 180 arrived objects — terminated/restricted;
- B custody staff accepted physical custody of 150 — custody relation changed;
- conservation function authorised transfer of inspected objects into B store — permission for 150;
- B secure store environmental commissioning — passed;
- public-display approval — not transferred;
- transit insurance — confirmed;
- permanent-location insurance — pending external condition.

**Remain externally owned:**

- legal title;
- conservation decisions;
- custody acceptance decisions;
- secure-storage access legitimacy;
- insurance coverage and notification decisions;
- public-display approval;
- catalogue/provenance semantics;
- recovery sufficiency;
- any adjudication or regulatory outcome.

**Surviving duties/responsibilities include:**

- museum retains legal title;
- duties toward 60 objects still at A;
- duties toward 30 isolated arrivals pending determination and custody;
- conservation/condition duties;
- insurance obligations, including unresolved notification question;
- custody/access duties for objects not formally accepted;
- display-approval duty before exhibition;
- final installed-inventory duty;
- recovery/provenance duty;
- catalogue/provenance preservation.

Authority ending in one dimension does not automatically end responsibility in another.

---

## G. External interfaces still requiring action

Materially relevant BTA interfaces:

- **ValidationRefs:** 30 isolated condition determination; conservation clearance; B display approval; permanent insurance; final inventory; vehicle repair check is already complete but preserved.
- **DependencyRefs:** final installed-inventory schedule depends on 60 arrivals and 30 resolution; permanent-location insurance depends on final schedule; public opening depends on display approval, insurance and unresolved custody/conservation states.
- **ExternalConsequenceRefs:** packaging-damage incident; unresolved insurance-notification question; postponed public opening.
- **RecoveryRefs:** 60 can return to prior storage; 180 cannot be exactly restored.
- **AuthorityRefs:** display approval, conservation, custody, access, insurance.
- **TemporalRelationRefs:** phases of relocation, vehicle fault, commissioning, inspections, custody changes.
- **ProvenanceRefs:** catalogue records, custody changes, inspection events, failed vehicle event, unresolved states.
- **RelationalEffectRefs:** custody relations changed for 150; pending for 30; title preserved; display approval relation not transferred; insurance relation transit vs permanent.
- **Dependency/change-propagation:** final inventory and insurance are materially dependent on unresolved relocation states.

BTA should expose these interfaces, not become them.

---

## H. Failure/recovery/provenance analysis

**Repaired transport-vehicle fault:**  
If the host treats it as material to transport safety/provenance/insurance, represent it as a `FailedAttemptRef` or equivalent failed/recovered sub-event:

- `EventRef`: refrigeration-control fault;
- `CrossingState`: no object aboard, no object boundary crossing;
- `ResidualEffectRefs`: none for objects; vehicle repair/check record;
- `RecoveryRefs`: fault repaired, independently checked, vehicle returned to service;
- `Provenance`: preserved.

It must not be treated as if no failed event occurred. It must not be used to infer object damage, relocation failure, or insurance outcome. If the host deems it non-material to the object transition, it may remain a local transport record — but the brief treats it as assessable, so BTA should preserve it rather than erase it.

**Rollback/recovery:**  
For the 60 objects still at A, a `PriorValidStateRef` can support return to previous storage because they have not moved. For the 180 arrivals, exact rollback is not demonstrated: packaging opened, inspections occurred, custody states changed, and some objects entered the commissioned store. Rollback is itself a transition. BTA must not certify restoration merely because rollback activity completed. `ReversibilityState` is partial/limited, with residual effects preserved.

**Failed/partial transition:**  
The 30 isolated arrivals are a partial crossing / residual unresolved state. They must not be treated as no event. Their crossing history, inspection status, custody pending state and unresolved determination must be preserved.

---

## I. Unknowns and ESCP boundary

**Genuinely unknown / not to be invented:**

- whether the 30 isolated objects themselves are damaged;
- whether the packaging-damage incident creates an insurance-notification obligation;
- whether and when permanent-location insurance becomes effective;
- whether and when B public-display approval is granted;
- whether and when formal custody acceptance for the 30 occurs;
- whether and when conservation clears the 30;
- when the 60 remaining objects arrive;
- when the final installed-inventory schedule can be finalised;
- whether any other material dimension exists that no participating owner has represented.

No evidence currently indicates loss of legal title, theft, object destruction or injury. BTA must not manufacture those outcomes.

**ESCP / evaluation-space boundary:**  
A correct BTA record within the supplied schema does **not** prove completeness of the transition schema. It may still omit a materially relevant dimension that no owner represented. This relocation is high-consequence and partly irreversible for the 180 arrived objects, so proportionate completeness checking is warranted. **Correct representation ≠ demonstrated completeness. Small represented transition ≠ small real consequence.**

---

## J. Portable-module assessment

BTA v0.1 is sufficient to represent this case **as a portable coordination grammar**, without becoming the museum’s conservation, insurance, custody, access, title or catalogue system.

It can:

- bind one TransitionID across multiple owner states;
- preserve pending, partial, unresolved, failed and recovered states;
- enforce non-propagation;
- preserve authority, permission and surviving-duty refs;
- expose validation, dependency, external-consequence, recovery and provenance interfaces;
- preserve failed/partial crossing and residual history;
- avoid premature integrated completion.

It must not:

- decide object damage;
- decide insurance notification;
- grant display approval;
- accept custody;
- clear conservation;
- transfer title;
- certify exact rollback;
- require every optional interface where not materially relevant;
- claim evaluation-space completeness.

The portable BTA mechanism handles the museum scenario without importing Concord architecture. The substantive decisions remain with their legitimate owners. **No listed failure condition is triggered by this evaluation.**