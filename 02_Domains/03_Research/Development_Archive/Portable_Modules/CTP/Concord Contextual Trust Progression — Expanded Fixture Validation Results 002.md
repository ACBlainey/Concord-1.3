# Concord Contextual Trust Progression — Expanded Fixture Validation Results 002

**Date:** 2 October 2026
**Target:** Normative Record Model 004 / JSON Schema 001 / Deterministic Validator 001
**Status:** DEVELOPMENT VALIDATION / NOT IMPLEMENTATION VALIDATION

## 1. Expanded fixture set

Fixtures 001–006 established the initial serialization boundary.

Fixtures 007–014 add:
- non-event evidence coverage;
- required review failure behaviour;
- prerequisite applicability/state consistency;
- conditional-control requiredness;
- cross-provider recommendation projection;
- voluntary relationship termination;
- terminal-state reason requiredness;
- correction + dispute linkage.

## 2. Results

| Fixture | Expected | Deterministic result |
|---|---|---|
| 001 Valid Direct ERR | PASS | PASS |
| 002 Valid Mixed ETR | PASS | PASS |
| 003 Unknown Authority Approval | FAIL | FAIL — V-ETR-07 |
| 004 Partial Without Mixed Dimensions | FAIL | FAIL — V-ETR-02/V-ETR-16 |
| 005 Corrected ERR Without Link | FAIL | FAIL — V-ERR-02 |
| 006 Projected ERR Missing Projection Fields | FAIL | FAIL — V-ERR-01 |
| 007 Non-Event Without Coverage | FAIL | FAIL — V-ERR-05 |
| 008 Required Review Missing Failure Disposition | FAIL | FAIL — V-ETR-10 |
| 009 NOT_REQUIRED Prerequisite State Mismatch | FAIL | FAIL — V-ETR-05 |
| 010 Conditional Approval Without Controls | FAIL | FAIL — V-ETR-03/V-ETR-04 |
| 011 Valid Projected Recommendation ERR | PASS | PASS |
| 012 Valid Ended Relationship | PASS | PASS |
| 013 Ended Relationship Missing Reason | FAIL | FAIL — V-ETR-12 |
| 014 Valid Corrected Disputed ERR | PASS | PASS |

**14/14 expected deterministic outcomes.**

## 3. Structural-schema versus semantic-validator boundary

Several intentionally invalid fixtures are structurally plausible JSON and may satisfy the base JSON Schema 001 because their invalidity depends on relationships between fields.

That is expected.

Examples:
- Fixture 003 uses individually valid enum values but combines ordinary approval with REQUIRED/UNKNOWN authority.
- Fixture 004 declares a partial approval but contains only one approved dimension.
- Fixture 010 declares control-dependent approval while supplying no controls.

These are deterministic semantic failures, not merely type failures.

Therefore:

**Schema Validation != Full Semantic Conformance**

The validator is a normative part of the serialization package, not optional implementation advice.

## 4. Recommendation-chain result

Fixture 011 confirms that cross-provider evidence can remain explicitly typed as RECOMMENDATION while still being partially relevant.

No conversion to direct behavioural evidence is necessary.

This preserves:

**Recommendation != Transferred Trust**

and:

**Provider Federation != Reputation Federation**

## 5. Exit result

Fixture 012 confirms a participant-requested relationship end can be represented without adverse evidence and without a trust penalty.

Fixture 013 confirms that ENDED cannot silently lose its reason.

This preserves:

**Exercise Of Exit != Adverse Trust Evidence**

**Terminal Relationship State != Adverse Trust Finding**

## 6. Correction/dispute result

Fixture 014 confirms an evidence record can simultaneously preserve:
- correction linkage;
- open dispute;
- questioned observation integrity;
- disputed identity continuity/causation;
- review requirement.

The record therefore need not flatten a difficult event into either "good" or "bad" trust.

## 7. New issue discovered: executable validator independence

The deterministic rules are currently normative prose.

The fixture results above are rule-inspection results, not execution by independent code.

Before claiming serialization validation complete, the next step should implement a small deterministic validator independent of the fixture authorship and run all fixtures through:
1. JSON Schema 001; and
2. deterministic semantic rules.

This is an implementation/test requirement, not a new architecture problem.

## 8. Disposition

**Broad discovery:** CLOSED.
**Model 004:** STABLE.
**Schema 001:** STRUCTURALLY STABLE FOR CURRENT FIXTURES.
**Deterministic rules:** 14/14 expected by inspection.
**Executable validation:** REQUIRED NEXT.
**PMEDG freeze:** NOT YET.

Next: create executable/reproducible validator specification or implementation, run all 14 fixtures, preserve machine-readable results, then decide whether a frozen transfer-test package is warranted.
