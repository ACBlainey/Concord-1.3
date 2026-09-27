# Historical Domain — Cross-Object Consistency Audit 001

**Project:** The Concord
**Domain:** Historical
**Status:** SCHEMA CONSISTENCY AUDIT / NOT CANONICAL
**Date:** 25 September 2026
**Target:** Formal Schema Set 002

## 1. Purpose

This audit tests whether the Historical schema objects preserve distinct responsibilities when used together or whether overlapping fields create competing sources of meaning.

The desired outcome is not zero overlap. Summary objects may legitimately cache or expose states owned by more specialised objects.

The requirement is:

> **One concept may have multiple representations, but only one representation should be authoritative for its historical meaning within a given context.**

---

## 2. HSO-1 versus HCSA-1

HSO-1 contains summary privacy, access, classification and retention fields. HCSA-1 represents contextual state assertions.

Potential conflict: HSO-1 says RESTRICTED while HCSA-1 contains PUBLIC for Actor Class A and SEALED for Actor Class B.

Resolution:

- HCSA-1 is authoritative for contextual state semantics.
- HSO-1 fields are derived summary/snapshot fields.
- Where contextual assertions disagree, HSO-1 must not collapse them into a false universal state.
- A summary may instead report MULTIPLE_CONTEXTUAL_STATES or equivalent.

**Result: PASS WITH PRECEDENCE RULE.**

---

## 3. HIST-1 versus HRI-1

HIST-1 records the authorised information-state transition. HRI-1 records replica execution/integrity.

Potential conflict: HIST-1 says DESTROY while HRI-1 shows one replica pending.

Resolution:

- HIST-1 is authoritative for the intended/authorised transition and overall reconciliation state.
- HRI-1 is authoritative for known replica execution evidence.
- HIST-1 may not report RECONCILED until required HRI-1 states support it.

**Result: PASS.**

---

## 4. HIST-1 versus HDRS-1

HIST-1 records source transition. HDRS-1 records residual derivative condition.

Potential conflict: source destruction interpreted as derivative destruction.

Resolution:

- HIST-1 governs source information-state transition.
- HDRS-1 governs known derivative residual state.
- No inheritance of destruction state occurs without explicit propagation/execution.

**Result: PASS.**

---

## 5. HAE-1 versus HCSA-1

HAE-1 records activation/exercise of authority. HCSA-1 may represent an access or retention state produced by that authority.

Potential conflict: HCSA-1 appears to become the source of authority.

Resolution:

- HAE-1/source authority architecture is authoritative for the historical authority event.
- HCSA-1 records the resulting applicable state and references AuthoritySourceRef/HAE-1.
- State assertion does not manufacture authority.

**Result: PASS.**

> **State Produced by Authority ≠ Source of Authority.**

---

## 6. HSE-1 versus HCSA-1

HSE-1 contains secrecy-specific semantics. HCSA-1 can also assert SECRECY state.

Resolution:

- HSE-1 is authoritative for secrecy lifecycle, justification, review and disclosure conditions.
- HCSA-1 provides contextual applicability of secrecy to actors/purposes/jurisdictions.
- HCSA-1 secrecy assertions should reference the relevant HSE-1 envelope where one exists.

Neither object should duplicate the other's full function.

**Result: PASS WITH LINKAGE RULE.**

---

## 7. HCP-1 versus HCSA-1

HCP-1 grants/describes bounded correlation permission. HCSA-1 may say correlation is restricted or permitted in a context.

Resolution:

- HCP-1 is authoritative for an activated/bounded correlation permission.
- HCSA-1 expresses contextual state or restriction.
- A permissive HCSA-1 assertion alone does not constitute an executable permission unless the governing architecture says the assertion itself is the authority-bearing instrument.

Default Historical rule:

> **Correlation State ≠ Correlation Permission.**

**Result: PASS.**

---

## 8. HMHR-1 versus HDRS-1

HMHR-1 is the minimum surviving residue after destruction. HDRS-1 evaluates residual derivatives.

Potential conflict: HMHR-1 itself becomes a derivative capable of reconstruction.

Resolution:

- HMHR-1 must itself be evaluable as a residual information object.
- Where reconstructive risk exists, HDRS-1 or equivalent analysis may apply to the residue.
- "Minimum" is not self-certifying.

> **Minimum Historical Residue ≠ Automatically Safe Residue.**

**Result: PASS WITH RECURSIVE REVIEW RULE.**

---

## 9. HEC-1 versus HRO-1

HEC-1 represents evaluation context at a historical time. HRO-1 may generate a Present-Best reconstruction using later evidence.

Resolution:

- HEC-1 is authoritative for the represented contemporary evaluation space.
- HRO-1 is authoritative only for the reconstruction product it declares.
- Present-Best output cannot mutate HEC-1 into a later-informed contemporary state.

**Result: PASS.**

---

## 10. HES-1 versus HSB-1

HES-1 constructs an Event Spine view. HSB-1 records search/traversal coverage.

Resolution:

- HES-1 provides the reconstructed chain.
- HSB-1 bounds claims about its coverage.
- Known inaccessible domains must surface in HES-1 through coverage/gap state.
- HES-1 cannot claim completeness beyond HSB-1 scope.

**Result: PASS.**

---

## 11. HCAP-1 versus Continuity

HCAP-1 records historical evidence of recoverability. Continuity owns restoration decisions and current capability continuity.

Resolution:

- HCAP-1 does not authorise restoration.
- OPERATIONALLY_RESTORABLE means evidence supports that status under the recorded verification context.
- Current restoration requires current Continuity/authority evaluation.

> **Historical Recoverability State ≠ Restoration Authority.**

**Result: PASS.**

---

## 12. Cross-cutting duplication finding

The schema set contains three recurring layers:

### Layer A — Historical fact/state evidence
Examples: HSO-1, HEC-1, HPR-1, HCAP-1.

### Layer B — specialised lifecycle/state semantics
Examples: HSE-1, HIST-1, HDRS-1, HCSA-1.

### Layer C — authority/permission/action
Examples: HAE-1, HCP-1 and external Concord authority systems.

Confusion occurs when a Layer A or B object is treated as if it were Layer C.

Therefore:

> **Recorded State ≠ Permission to Act on That State.**

This is a general consistency rule.

---

## 13. Derived-state rule

Several objects contain convenient summary fields that can be derived from richer objects.

A derived field must preserve:

- derivation source;
- derivation time;
- derivation method/version where material;
- scope;
- conflict state;
- freshness/review state.

Otherwise cached summaries can silently outlive the relationships that justified them.

> **Derived Summary ≠ Independent Historical Truth.**

---

## 14. Precedence rule

"Precedence" in Historical must not mean one record magically overrides reality.

It means that for a specific semantic question, one schema is designated as the authoritative representation of that Historical concept.

Examples:

- contextual access state → HCSA-1;
- secrecy lifecycle → HSE-1;
- authority activation/exercise → HAE-1;
- derivative residual condition → HDRS-1;
- replica execution → HRI-1;
- evaluation space → HEC-1.

This is semantic precedence, not civil authority.

---

## 15. Conflict rule

When two apparently valid objects conflict, Historical should not automatically choose the newest, most authoritative-looking or most accessible record.

It should first determine whether they differ because of:

- time;
- context;
- jurisdiction;
- purpose;
- actor class;
- source authority;
- correction/supersession;
- epistemic status;
- schema/version;
- genuine unresolved contradiction.

Only genuine contradiction should be represented as conflict.

> **Difference ≠ Contradiction.**

---

## 16. Recursive-state risk

The audit exposes a potential recursion:

- HCSA-1 controls access to HCSA-1;
- secrecy envelope controls access to secrecy envelope;
- residue analysis creates a new record needing residue analysis;
- correlation permission records may themselves be sensitive.

This is not inherently a flaw.

The architecture requires termination by minimum necessary meta-state: enough metadata to govern the protected object without reproducing the protected substance.

Where recursion cannot safely terminate, a higher legitimate governance/judicial/privacy authority must resolve the boundary.

**Result: MANAGEABLE / REQUIRES IMPLEMENTATION DISCIPLINE.**

---

## 17. Consistency matrix

**HSO-1 ↔ HCSA-1:** PASS — HCSA contextual semantics; HSO summary.

**HIST-1 ↔ HRI-1:** PASS — transition versus replica execution.

**HIST-1 ↔ HDRS-1:** PASS — source versus derivative state.

**HAE-1 ↔ HCSA-1:** PASS — authority event versus resulting state.

**HSE-1 ↔ HCSA-1:** PASS — lifecycle versus contextual applicability.

**HCP-1 ↔ HCSA-1:** PASS — permission versus state.

**HMHR-1 ↔ HDRS-1:** PASS WITH RECURSIVE REVIEW.

**HEC-1 ↔ HRO-1:** PASS — contemporary context versus reconstruction output.

**HES-1 ↔ HSB-1:** PASS — view versus coverage boundary.

**HCAP-1 ↔ Continuity:** PASS — historical recoverability versus restoration authority.

No pair requires object merger.

---

## 18. New consistency invariants

1. **State Produced by Authority ≠ Source of Authority.**
2. **Correlation State ≠ Correlation Permission.**
3. **Minimum Historical Residue ≠ Automatically Safe Residue.**
4. **Historical Recoverability State ≠ Restoration Authority.**
5. **Recorded State ≠ Permission to Act on That State.**
6. **Derived Summary ≠ Independent Historical Truth.**
7. **Difference ≠ Contradiction.**
8. **Semantic Precedence ≠ Civil Authority.**

---

## 19. Audit result

**Cross-Object Consistency Audit 001:** PASS WITH MINOR FORMALISATION REQUIREMENTS.

The new contextual-state architecture does not conflict with the earlier schemas. It clarifies them.

No object merger or architectural rollback is required.

The remaining work is increasingly formal rather than conceptual:

- assign authoritative semantic ownership for each field/state;
- formalise enum/state vocabularies;
- define transition legality/validation rules;
- define minimum conformance requirements;
- test one or two complete end-to-end historical event chains through all relevant objects.

This indicates Historical is approaching a candidate graduation boundary, but an end-to-end conformance test should occur first.

---

## 20. Next

**Next:** Historical End-to-End Conformance Test 001 — Complete Event Lifecycle from Operational Creation to Historical Reconstruction, Correction, Restricted Access and Partial Destruction.
