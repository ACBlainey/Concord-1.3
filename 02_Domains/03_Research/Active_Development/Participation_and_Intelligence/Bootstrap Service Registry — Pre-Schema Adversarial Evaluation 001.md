# Bootstrap Service Registry — Pre-Schema Adversarial Evaluation 001

**Project:** The Concord
**Date:** 1 October 2026
**Subject:** Bootstrap Service Registry — Formal Record and Validation Model 001
**Status:** INTERNAL ADVERSARIAL EVALUATION / PRE-SCHEMA

## 1. Method

Treat Formal Record and Validation Model 001 as fixed.

Do not repair a scenario by silently importing fields or rules from wider Concord architecture. Test whether the semantic model can represent the state without collapsing claim, evidence, control, authority, provenance, time, continuity or uncertainty.

## 2. Scenario Results

### A1 — False authority claim
A service claims AUTHORITATIVE_CONCORD but evidence supports only PROVISIONAL_CONCORD.

**PASS.** ClaimedServiceStatus and EvidenceSupportedStatus are explicitly separate.

### A2 — Technically available, constitutionally ungrounded
**PASS.** Availability, authority and threshold state are separate.

### A3 — Formal operator differs from effective controller
**PASS.** DeclaredFormalOperator, TechnicalController and EffectiveController are distinct.

### A4 — Effective controller changes without operator change
**PASS WITH REPRESENTATIONAL CLARIFICATION.** The model requires temporal state and says such change should trigger review, but control relationships themselves lack explicit observation/effective time and scope.

### B1 — Conflicting evidence
Two valid-looking evidence items support incompatible status claims.

**PASS.** Evidence disagreement and DISPUTED state are representable.

### B2 — Evidence was valid yesterday but is stale today
**PASS.** EvidenceTimestamp, EvidenceFreshnessState and temporal fields represent this.

### B3 — Cryptographically intact evidence from illegitimate authority
**PASS.** Integrity and authority are explicitly separated.

### B4 — Evidence source and registry share hidden dependency
**PASS where known; UNKNOWN otherwise.** KnownCommonDependencies and uncertainty support the state without fabricating independence.

### C1 — Service has two functions with different Z classes
**PASS WITH REPRESENTATIONAL CLARIFICATION.** Model says class should bind to function, but current formal record stores DeclaredFunction[] and BootstrapClass[] as parallel arrays without a normative relation object. Serialization could accidentally lose the binding.

### C2 — One authority basis applies only to one function
**REPRESENTATIONAL GAP.** AuthorityClaim[], AuthorityBasis[], AuthorityScope[] are parallel collections. The model does not formally bind a particular claim/basis/scope/review state to the particular function/consequence it authorises.

### C3 — One function is below threshold; another is Z5
**REPRESENTATIONAL GAP.** ConstitutionalThresholdState is singular at service-record level. A multi-function service can require different threshold states simultaneously.

### D1 — Operator identity cannot safely be public
**PASS.** Protected or externally verifiable references are permitted with uncertainty represented.

### D2 — Anonymous controller with demonstrable technical control
**PASS WITH CLARIFICATION.** A protected/pseudonymous reference can represent the controller, but the model should distinguish actor reference from human-readable identity.

### E1 — Service forks
Two services share provenance until a fork and then diverge.

**PARTIAL PASS.** ArtifactProvenance can describe it, but there is no explicit relationship vocabulary for SAME_SERVICE, FORK_OF, SUCCESSOR_OF, PREDECESSOR_OF or RELATED_SERVICE.

### E2 — Service renames without changing identity
**PARTIAL PASS.** Stable ServiceRecordID permits continuity, but name history is not explicitly represented except through generic corrections.

### E3 — Two registries independently create different record IDs for the same service
**REPRESENTATIONAL GAP.** Section 3 says preserve sufficient provenance to determine sameness/relationship, but no explicit service identity/correlation field exists distinct from registry-local ServiceRecordID.

### F1 — Founder disappears; service continues
**PASS.** Continuity plus authority separation prevents infrastructure from inheriting authority.

### F2 — Successor takes function but receives new authority basis
**PASS.** Bootstrap Succession Record is explicitly expected and authority continuity is denied.

### F3 — Successor dispute
**PASS.** Succession unresolved/disputed can be represented, although detailed succession belongs in BSuR.

### G1 — Registry describes itself
**PASS.** Required by registry behaviour.

### G2 — Registry A lists Registry B; Registry B lists A
**PASS.** Recursion does not manufacture authority.

### G3 — Ten registries agree because all copied Registry A
**PASS where dependency known.** Cross-registry agreement and common-dependency rules prevent automatic authority inference.

### H1 — Service becomes unavailable
**PASS.** Availability vocabulary covers it.

### H2 — One function unavailable while other functions remain available
**REPRESENTATIONAL GAP.** CurrentAvailability is singular at service level; multi-function partial availability cannot be represented cleanly without either splitting the service or adding function-level operational state.

### H3 — Contact route fails but service remains available by another route
**PASS.** ContactRoute[] permits multiple routes, but route-level availability is not formalised.

### I1 — Material correction changes authority status
**PASS.** Correction history is append-preserving.

### I2 — Registry learns old evidence was fabricated
**PASS.** COMPROMISED plus correction/history preserves evidence lineage.

### I3 — Record itself is maliciously rewritten
**OUT OF CURRENT IMPLEMENTATION SCOPE.** Semantic model requires provenance/history but cryptographic/log integrity is explicitly downstream.

### J1 — Two registries exchange a record
**PASS at semantic level.** Required distinctions are enumerated.

### J2 — Receiver has different enum vocabulary
**INTEROPERABILITY CLARIFICATION.** Semantic preservation is required, but version/namespace handling for vocabularies is not yet explicit.

### J3 — Receiver flattens all status to verified/unverified
**PASS as rejection case.** Explicitly non-conforming.

## 3. Findings

### P1 — Function-Centred Consequence Binding

**Classification:** SUBSTANTIVE REPRESENTATIONAL GAP / NOT NEW BOOTSTRAP ABSTRACTION.

The current service-level parallel arrays cannot reliably bind:
- function;
- Z class;
- material consequence;
- authority claim;
- authority basis;
- authority scope;
- review/sunset;
- constitutional threshold state;
- availability.

A service may legitimately contain several functions with different authority and consequence states.

Required repair: introduce a repeatable **FunctionProfile** (or equivalent relation object) that owns those fields per function.

This is a formal data-model correction, not a new civilisational architecture.

### P2 — Service Identity vs Registry Record Identity

**Classification:** SUBSTANTIVE REPRESENTATIONAL GAP / NOT NEW BOOTSTRAP ABSTRACTION.

ServiceRecordID currently identifies the registry record. Cross-registry correlation requires a distinct service identity/reference layer.

Required repair:
- RegistryRecordID — identity of this registry's record;
- ServiceIdentityReference(s) — evidence-backed references used to correlate the underlying service;
- RelatedService relationship vocabulary with relation type and evidence.

Do not create a universal identity sovereign. Correlation may remain uncertain/disputed.

### P3 — Temporal/Scoped Control Relations

**Classification:** REPRESENTATIONAL CLARIFICATION.

Control roles should be relation records rather than bare actor arrays where material:
- actor/reference;
- role;
- scope;
- observed/effective time;
- evidence;
- state.

This allows effective control to change without rewriting historical control.

### P4 — Partial Availability

**Classification:** REPRESENTATIONAL GAP.

Service-level CurrentAvailability is insufficient for multi-function services.

FunctionProfile should carry operational availability. Service-level availability may remain as summary/derived state if clearly marked as such.

### P5 — Vocabulary / Schema Versioning

**Classification:** IMPLEMENTATION INTERFACE CLARIFICATION.

Machine exchange will require:
- schema/model version;
- vocabulary namespace/version;
- extension handling;
- unknown-enum preservation.

Do not solve this by silently mapping unknown values into known ones.

## 4. Architecture Check

No finding requires:
- a new Zero-Infrastructure Bootstrap abstraction layer;
- new authority theory;
- new constitutional mechanism;
- new registry authority;
- central identity authority.

The gaps are caused by moving from architecture-level field families to a relational/machine-exchange model.

## 5. Disposition

Formal Record and Validation Model 001 should **not** be converted directly into normative JSON Schema.

Create Model 002 with:
1. FunctionProfile relation;
2. RegistryRecordID separated from service identity references;
3. explicit related-service relations;
4. scoped/temporal control relations;
5. function-level availability;
6. schema/vocabulary version metadata.

Then rerun this same adversarial set before serialization.

## 6. Status

**Pre-schema pass:** REVISION REQUIRED.

**Architectural discovery reopened:** NO.

**New bootstrap abstraction required:** NO.

**Reason for revision:** semantic relational completeness for implementation.
