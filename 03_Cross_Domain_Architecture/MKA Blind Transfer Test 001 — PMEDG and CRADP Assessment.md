# MKA Blind Transfer Test 001 — PMEDG and CRADP Assessment

**Project:** The Concord Framework  
**Date:** 3 October 2026  
**Status:** POST-TEST ASSESSMENT / CLEAN BLIND TRANSFER COMPLETED / PROVISIONAL / NON-CANONICAL  
**Candidate:** Multi-Key Authority (MKA)  
**Test:** MKA Blind Transfer Test 001

## 1. Evidential basis

This assessment is based on the frozen test materials and the clean evaluator's raw result.

The evaluator reported:

- no prior Concord context;
- no prior MKA context;
- no external search;
- all three frozen materials received;
- no missing/corrupt materials;
- no material limitation affecting blindness.

The raw result's overall classification was:

> **TRANSFER VALIDATED WITH NON-BLOCKING CLARIFICATIONS**

It explicitly reported:

> **No falsification success was found that would require revision of the frozen candidate.**

This assessment therefore treats the frozen candidate as having passed its first clean cross-instance transfer test.

## 2. PMEDG result

**PASS — CLEAN TRANSFER DEMONSTRATED**

The candidate successfully transferred without developmental provenance.

The evaluator could independently recover and apply the candidate's core architecture:

1. Permission before authority.
2. Actual route rather than objective alone.
3. Authority-space completeness.
4. Independent authority grounding.
5. Scope.
6. Composition/inheritance.
7. Prohibitions.
8. Temporal freshness.
9. Commit-time revalidation.
10. Unknown/disputed-state preservation.
11. Rerouting.
12. Non-scope boundaries.

No wider Concord architecture was required to repair the candidate.

## 3. CRADP result

**PASS WITH NON-BLOCKING INTERFACE CLARIFICATION**

The clean instance did not collapse MKA into:

- CWA/context ownership;
- CBPR/runtime ownership;
- BTA/transition ownership;
- ESCP/general epistemic completeness;
- substantive domain law.

The candidate therefore remained architecturally identifiable after cross-instance transfer.

## 4. Scenario coverage

All 30 scenarios were completed.

The test demonstrated successful handling of:

- permission-sufficient ordinary actions;
- changed routes;
- missing protected-record authority;
- delegated financial scope;
- revocation before commit;
- pre-authorised emergency action;
- false emergency authority;
- safeguarding uncertainty;
- machine capability versus authority;
- shared-service effects;
- newly discovered protected contexts;
- invalid and valid inheritance;
- upstream prohibition;
- disputed authority;
- unknown authority classification;
- anti-bureaucratic granularity;
- rerouting;
- transition-owner separation;
- runtime-owner separation;
- context-owner separation;
- beneficial-outcome fallacy;
- registry neutrality;
- third-party effects;
- clean multi-key success;
- changed mechanism;
- stale emergency predicates;
- authority evidence versus authority source;
- invalid composition leap;
- ordinary private permission.

This is sufficiently broad to establish cross-domain transfer for the candidate's present development stage.

## 5. Cross-scenario findings

### 5.1 Transfer

Validated.

The evaluator stated that the frozen kernel could be applied without Concord developmental history.

### 5.2 Distinctness

Validated.

The evaluator preserved boundaries against context architecture, runtime architecture, transition coordination and substantive law.

### 5.3 Missing-key detection

Validated.

The candidate repeatedly detected the difference between:

> **all represented keys being valid**

and:

> **all required authority dimensions being represented.**

This is the core ASCP contribution to MKA.

### 5.4 Anti-bureaucracy

Validated.

The evaluator correctly returned permission-sufficient results for ordinary cases and rejected false authority keys for technical micro-actions.

This is important because a kernel that merely maximised key count would have failed its own extraction boundary.

### 5.5 Composition

Validated.

The evaluator rejected automatic composition and accepted explicit legitimate composition/inheritance where supplied.

### 5.6 Temporal validity

Validated.

Revocation, expired predicates and historical authority evidence were correctly distinguished from current authority at commit.

### 5.7 Unknown/dispute preservation

Validated.

The evaluator did not convert unresolved authority into either permission or prohibition and did not make MKA the substantive resolver.

### 5.8 Substrate neutrality

Validated.

The architecture operated across human, institutional, software, robotic and mixed cases without changing its core logic.

## 6. Non-blocking clarification

The evaluator identified one repeated interface issue in scenarios 19–21.

Those scenarios concerned:

- transition completion;
- runtime configuration;
- context/precedence ownership.

The evaluator correctly recognised that these were not MKA-owned decisions.

However, it noted that the candidate output vocabulary has no dedicated state such as:

- `EXTERNAL_OWNER_REQUIRED`; or
- `NON_MKA_SCOPE`.

The current contract can already represent these cases using:

- `UnresolvedRefs`;
- `ReviewTrigger`;
- host-mapped vocabulary;
- `HOLD_UNKNOWN_AUTHORITY` where an unresolved authority dimension genuinely remains.

Therefore this is not a kernel defect.

It is an interface-clarity opportunity.

## 7. Freeze integrity decision

The tested frozen candidate should **not** be retrospectively edited.

Reason:

1. the clean test succeeded;
2. the reported issue is non-blocking;
3. the existing contract can represent the handoff;
4. changing the tested artifact would destroy direct correspondence between test result and tested version.

Therefore:

> **Preserve the tested frozen kernel unchanged.**

Any vocabulary improvement should enter a successor candidate or portable-module integration layer with explicit provenance.

## 8. Clarification disposition

Recommended disposition:

Add an optional interface status in the eventual portable module:

`EXTERNAL_OWNER_REQUIRED`

Meaning:

> the proposed question or unresolved function belongs to an identified external architecture/domain owner and MKA must hand off rather than absorb it.

Potential companion:

`OUTSIDE_MKA_SCOPE`

These should not be treated as new authority decisions.

They are routing/interface states.

They must not replace:

- `HOLD_MISSING_AUTHORITY`;
- `HOLD_UNKNOWN_AUTHORITY`;
- `HOLD_DISPUTED_AUTHORITY`;
- `BLOCK_PROHIBITED`;
- `BLOCK_OUT_OF_SCOPE`.

A genuine authority gap remains an authority gap even if another domain owns resolution.

## 9. Candidate architecture status after test

The MKA candidate now has:

1. cross-domain source resolution;
2. cross-domain adversarial testing;
3. ASCP development;
4. composition/non-duplication audit;
5. frozen extraction boundary;
6. clean cross-instance blind transfer;
7. successful 30-scenario application;
8. explicit falsification attempt;
9. no blocking defect discovered.

Updated status:

**SOURCE-RESOLVED / CROSS-DOMAIN ADVERSARIALLY TESTED / NON-DUPLICATION AUDITED / CLEAN-TRANSFER VALIDATED / STRONG PMEDG GRADUATION CANDIDATE / PROVISIONAL / NON-CANONICAL**

## 10. Graduation decision

The blind-transfer result supports advancement to the **PMEDG graduation review**.

It does not by itself make MKA canonical.

The next review should determine:

- whether another independent clean test is required by PMEDG;
- whether the non-blocking external-owner vocabulary should be incorporated before portable-module release;
- whether ASCP remains embedded rather than separately extracted;
- what provenance and dependency references accompany the final portable module;
- whether the portable module should be versioned v1.0 or retained as candidate until a second implementation test.

## 11. Strong retained formulation

> **MKA is a small shared authority-composition kernel operating at the seam between independently legitimate authority states and a consequential act. It verifies that materially required authority dimensions are represented, valid, current, within scope and legitimately composable, without creating authority or absorbing the substantive architectures that own those authority sources.**

And:

> **Authority Does Not Automatically Compose.**

## 12. Immediate next action

Run:

**MKA — PMEDG Graduation Review 001**

The review should use the frozen candidate, source-resolution chain, adversarial test, composition audit and this clean-transfer result.

The raw blind evaluator result remains immutable provenance.
