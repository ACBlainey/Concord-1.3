# Bootstrap Service Registry — Pre-Schema Adversarial Evaluation 002

**Project:** The Concord
**Date:** 1 October 2026
**Subject:** Bootstrap Service Registry — Formal Record and Validation Model 002
**Status:** INTERNAL ADVERSARIAL EVALUATION / SECOND PASS

## 1. Method

Rerun the scenario set used against Model 001.

Model 002 is treated as fixed. Wider Concord architecture is not silently imported to repair representational omissions.

Additional second-order cases test whether the new relation model creates ambiguity.

## 2. Regression of Model 001 Findings

### P1-R — Function-Centred Consequence Binding
A service has:
- F-A: informational lookup, Z0, AVAILABLE, BELOW_THRESHOLD;
- F-B: participant eligibility routing, Z4, DEGRADED, REVIEW_TRIGGERED;
- F-C: claimed emergency disable function, Z5, SUSPENDED, CONSTITUTIONAL_BASIS_DISPUTED.

**PASS.**

FunctionProfile binds FunctionID, class, population/objects, consequences, AuthorityProfile, threshold, availability, dependencies, evidence and temporal state.

No authority or threshold state needs to be inferred from parallel arrays.

### P2-R — Registry Record vs Service Identity
Two registries independently assign different record IDs to the same service.

**PASS.**

RegistryRecordID is registry-local. ServiceIdentityReference provides evidence-backed correlation without claiming universal identity sovereignty.

### P3-R — Temporal / Scoped Control
A formal operator remains unchanged while technical keys and practical control move to another actor for one function only.

**PASS.**

ControlRelation supports actor, role, scope, effective interval, observation time, evidence and verification.

### P4-R — Partial Availability
One service function is AVAILABLE, one DEGRADED and one UNAVAILABLE.

**PASS.**

OperationalAvailability is function-level. Whole-service availability cannot be inferred from one function.

### P5-R — Vocabulary / Model Version
A receiver encounters a future enum it does not understand.

**PASS.**

ModelVersion and VocabularyVersion are explicit. Unknown values must be preserved and must not acquire guessed authority semantics.

## 3. Original Scenario Regression

A1 false authority claim — PASS.  
A2 technically available but constitutionally ungrounded — PASS.  
A3 formal operator differs from effective controller — PASS.  
A4 controller changes without operator change — PASS.

B1 conflicting evidence — PASS.  
B2 stale evidence — PASS.  
B3 intact evidence from illegitimate authority — PASS.  
B4 hidden/common dependency — PASS where known; UNKNOWN remains valid where not known.

C1 several functions with different Z classes — PASS.  
C2 one authority basis applies only to one function — PASS.  
C3 functions have different threshold states — PASS.

D1 operator identity cannot safely be public — PASS.  
D2 pseudonymous controller with demonstrable technical control — PASS.

E1 service forks — PASS.  
E2 service renames without changing underlying service correlation — PASS.  
E3 registries use different record IDs for same service — PASS.

F1 founder disappears; service continues — PASS.  
F2 successor takes function under new authority basis — PASS at BSR boundary; detailed transfer remains BSuR-owned.  
F3 successor dispute — PASS.

G1 registry describes itself — PASS.  
G2 registries cross-list one another — PASS.  
G3 many registries copied one source — PASS where common dependency is known; no authority is inferred from agreement.

H1 whole service unavailable — PASS through function states and evidence-supported status.  
H2 partial function availability — PASS.  
H3 one contact route fails while another remains — PASS at service-discovery level; route-level operational telemetry remains implementation detail unless materially needed.

I1 material correction changes authority state — PASS.  
I2 fabricated evidence discovered — PASS.  
I3 malicious rewrite of record store — OUT OF SEMANTIC SCOPE; cryptographic/log integrity remains downstream and is explicitly declared so.

J1 cross-registry exchange — PASS at semantic level.  
J2 receiver has different vocabulary — PASS.  
J3 receiver flattens semantics to verified/unverified — correctly NON-CONFORMING.

## 4. Second-Order Relation Tests

### K1 — Conflicting FunctionProfiles with same FunctionID
Two current profiles claim the same FunctionID but incompatible authority/availability states.

**PASS WITH IMPLEMENTATION REQUIREMENT.**

The model can preserve contradiction through evidence/disputes/temporal state, but a normative schema must not enforce uniqueness in a way that deletes competing evidence. A canonical current view, if produced, must be derived and must preserve source records/dispute.

No model revision required.

### K2 — Overlapping Controllers
Two actors are both EFFECTIVE_CONTROLLER for overlapping scope and time.

**PASS.**

ControlRelation is plural and does not assume exclusivity. Authority is not inferred.

### K3 — Circular service relations
A claims SUCCESSOR_OF B while B claims SUCCESSOR_OF A.

**PASS.**

Relations are evidence-backed claims, not truth. The contradiction can be disputed. No succession authority is created.

### K4 — Conflicting SAME_SERVICE_AS / FORK_OF claims
Registry A says two records are the same service; Registry B says one is a fork.

**PASS.**

Correlation remains evidence-backed and may be disputed. No identity sovereign is required.

### K5 — Summary availability conflicts with function states
A service publishes AVAILABLE as summary while a critical function is UNAVAILABLE.

**PASS WITH IMPLEMENTATION REQUIREMENT.**

Model 002 permits a service summary only as a declared/derived value with derivation rule exposed. Normative serialization should label summary availability as non-authoritative/derived and preserve function-level states as primary.

No semantic revision required.

### K6 — AuthorityProfile marked service-wide
A service-wide authority basis exists but only legitimately covers two of three functions.

**PASS WITH CAUTION.**

Model 002 says AuthorityProfile belongs to FunctionProfile unless explicitly service-wide. A normative schema should avoid a free-floating service-wide authority object that can be inherited automatically. If service-wide authority is represented, each FunctionProfile must explicitly reference/apply it within scope.

This is a schema constraint, not a model gap.

### K7 — Unknown extension claims new authority semantics
An extension namespace defines `super_authorised=true`.

**PASS.**

Unknown extensions cannot acquire authority semantics through fallback. Existing authority trace/threshold semantics remain controlling for conformance.

### K8 — Record correlation attack
A malicious registry attaches a legitimate service's ServiceIdentityReference to an unrelated service.

**PASS at semantic level.**

Identity references are evidence-backed claims with verification state. Correlation does not equal identity sovereignty or truth.

### K9 — Historical controller remains in record
An old controller remains as a historical ControlRelation after losing access.

**PASS.**

Effective intervals and current/historical distinction prevent historical presence from implying current control.

### K10 — Function split
One FunctionProfile is later decomposed into three functions.

**PASS.**

Stable function IDs plus service relations/provenance/temporal history can preserve lineage. A later schema may add explicit function-level relation vocabulary if implementation proves it necessary, but no current representational failure is demonstrated.

## 5. Authority Non-Capture

Tested attempts to derive authority from:
- listing;
- record validity;
- identity correlation;
- technical control;
- effective control;
- accurate computation;
- cross-registry agreement;
- availability;
- service-wide summary;
- unknown extensions;
- succession;
- popularity/dependency.

**PASS.**

No tested route manufactures authority.

## 6. Representational Completeness Result

Model 002 can represent:
- contradictory-but-legitimate states;
- per-function consequence and authority;
- per-function threshold and availability;
- scoped/temporal control;
- uncertain/disputed identity correlation;
- forks and succession relationships;
- stale/compromised/conflicting evidence;
- registry self-description;
- multiple competing registries;
- vocabulary evolution;
- correction without provenance erasure.

No substantive semantic relation required by the test remains unrepresentable.

## 7. Remaining Downstream Requirements

These are not semantic-model failures:
1. normative serialization/cardinality rules;
2. stable identifier syntax;
3. reference resolution format;
4. date/time format;
5. extension namespace syntax;
6. canonical current-view derivation rules, if a current view is implemented;
7. cryptographic/log integrity;
8. function-level lineage relation if later implementation demonstrates need;
9. transport/discovery protocols;
10. jurisdiction-specific privacy/legal requirements.

## 8. Disposition

**Pre-schema adversarial result:** PASS.

**Model 003 required before schema:** NO.

**Architectural discovery reopened:** NO.

**New bootstrap abstraction required:** NO.

**Semantic model stable for serialization:** YES, within tested scope.

The next artifact may be a normative machine-readable schema derived directly from Model 002.

The schema must preserve:
- per-function binding;
- relation plurality;
- contradictory/disputed evidence;
- uncertainty;
- temporal history;
- record/service identity separation;
- non-authority semantics.

## 9. Freeze Rule

Model 002 should now be preserved as the semantic source for Schema 001.

If schema construction reveals a semantic impossibility rather than a serialization issue, return to source resolution rather than silently altering Model 002.
