# Evidentiary Completeness Audit — Scenario Stress Test 001

**Project:** The Concord
**Domain:** Judiciary / Law / Civil Security / Historical
**Date:** 3 October 2026
**Status:** ACTIVE DEVELOPMENT / EVIDENTIARY COMPLETENESS STRESS TEST / PROVISIONAL / NON-CANONICAL

## 1. Test purpose

This test examines whether **Evidentiary Completeness Audit — ESCP-Aware Judicial Evidence Architecture 001** can detect and correctly handle missing or misleading evidence-space conditions without either:

- treating a bounded search as complete reality; or
- converting epistemic uncertainty into unlimited search authority.

The test deliberately varies whether missing evidence is exculpatory, inculpatory, protected, destroyed, technically inaccessible, falsely expected, misindexed or outside the original evidence taxonomy.

---

## 2. Scenario A — omitted exculpatory CCTV

Police and the evidentiary function search cameras surrounding the incident location. The indexed footage supports the prosecution hypothesis. A later source-map review discovers a privately operated camera on an adjacent route that was never represented in the original CCTV index. It shows the accused travelling away from the incident before the relevant time.

### Analysis

The original searches may have been accurate within their represented source space.

They were not complete across the materially relevant CCTV space.

The correct interpretation of the earlier negative search is:

**No Contradictory CCTV Found In Represented Camera Set**

not:

**No Contradictory CCTV Exists**

The new footage enters the evidential state, attribution and prosecution threshold are reassessed, and the omission itself is reviewed.

### Result

**PASS.**

Validates:

**Accurate Search != Complete Source Space**

**Later Exculpatory Evidence -> Threshold Reassessment**

---

## 3. Scenario B — omitted inculpatory source

The represented evidence leaves attribution uncertain. The defence argues that no digital evidence places the accused at the location. A later completeness challenge discovers a building access-control system that was not represented as an evidence source. Its records strongly support presence.

### Analysis

The defence's statement can legitimately describe the searched evidence:

**No Represented Digital Source Established Presence**

It cannot legitimately become:

**No Digital Evidence Of Presence Exists**

The newly discovered source is evaluated for provenance, reliability and proposition scope before being used.

### Result

**PASS.**

The architecture is symmetric: ESCP protection applies to evidence that helps or harms the accused.

---

## 4. Scenario C — privacy-protected third-party source

A third party's location archive may resolve whether a witness could have observed the event. The archive contains years of unrelated intimate location history.

### Analysis

The completeness audit records the source as known/restricted rather than absent.

The legitimate evidential question is bounded to the relevant place/time/proposition. A CIBB-compatible query or independently controlled projection may answer it without exposing the full archive.

If no legitimate access mechanism exists, that limitation remains visible in the evidential-sufficiency state.

### Result

**PASS.**

**Known Restricted Source != Missing Source**

**Completeness Need != Unlimited Disclosure**

---

## 5. Scenario D — expected bodycam destroyed by retention failure

A police bodycam should have recorded a material encounter, but a storage fault destroyed the file before the case reached prosecution.

### Analysis

The source state is not **SEARCHED / NO MATCH**.

It is **EXPECTED BUT MISSING / DESTROYED OR UNAVAILABLE**, with provenance concerning the storage failure.

The system must not infer either what the footage would have shown or that its absence supports one side.

The missing evidence may affect confidence, procedural fairness, authority review or evidential sufficiency depending on the proposition and surrounding evidence.

### Result

**PASS.**

**Missing Expected Evidence != Known Evidential Content**

The architecture correctly preserves the difference between evidence absence and unavailable observation.

---

## 6. Scenario E — technically unsearchable archive

A large historical CCTV archive exists, but legacy metadata corruption means it cannot reliably be searched by time, location or participant. Manual review of the entire archive would be disproportionate.

### Analysis

The source must be represented as existing but technically constrained/partially searchable.

A failed automated query cannot be treated as a reliable negative result.

The system may attempt a proportionate alternative query or targeted manual review if authority and materiality justify it.

If not, the limitation remains explicit.

### Result

**PASS.**

Candidate clarification:

**Source Exists + Search Fails != Negative Evidential Result**

---

## 7. Scenario F — falsely expected evidence

A witness states that a public camera covers the location. Investigators find no recording and initially treat the missing footage as suspicious. Later infrastructure records establish that the camera was removed months earlier.

### Analysis

The expected-evidence premise was wrong.

The absence cannot support an inference about concealment or the event.

Expected-evidence reasoning therefore requires source-existence validation.

### Result

**PASS.**

Existing ECA-09 holds.

Candidate addition:

**Expected Source Assumption Must Itself Be Evidentially Testable**

---

## 8. Scenario G — entirely unrepresented evidence taxonomy

The case concerns an automated building system. Police, fiduciaries and evidentiary staff consider witness evidence, CCTV, access logs and device logs. Judicial MRT exposes a contradiction in door state. A technical expert identifies a previously unconsidered class: power-quality telemetry retained by the building utility controller, capable of showing whether the lock failed during a voltage event.

### Analysis

No earlier actor concealed or failed to retrieve a known source. The evidence class did not exist inside their represented taxonomy.

This is a direct ESCP case.

The correct response is not to blame the prior search merely for lacking an unknown category. It is to expand the Evidence Source Map, test relevance and authority, and conduct a bounded search if justified.

### Result

**PASS.**

This is the strongest validation of the architecture's purpose.

**Correct Search Of Existing Taxonomy != Complete Evidence Taxonomy**

---

## 9. Scenario H — source listed but wrong query dimension

CCTV is correctly represented and searched for the accused's face. No match is found. Later MRT analysis suggests the accused may have used a distinctive vehicle. Searching the same archive by vehicle reveals relevant footage.

### Analysis

The source class was represented; the query space was incomplete.

Completeness therefore applies not only to sources but to:

- query dimensions;
- time windows;
- identifiers;
- relationships;
- transformations;
- proposition framing.

### Result

**PASS WITH ARCHITECTURAL EXTENSION.**

The Evidence Source Map should distinguish **source-space completeness** from **query-space completeness**.

Candidate invariant:

**Source Searched != Every Material Query Performed**

---

## 10. Scenario I — evidence hidden by classification error

A system log is indexed as routine maintenance rather than incident evidence. Search filters exclude routine maintenance records. The record later proves material to the event timeline.

### Analysis

The object existed, was preserved and indexed, but its classification prevented retrieval.

This is neither source absence nor query failure alone.

It is a representational/classification failure.

The audit must therefore inspect consequential filters and classification assumptions where contradictions persist.

### Result

**PASS WITH ARCHITECTURAL EXTENSION.**

Candidate invariant:

**Recorded Evidence != Discoverable Evidence**

---

## 11. Scenario J — apparently independent sources share hidden origin

Three evidential systems appear to independently place A at the scene. Completeness/dependency review reveals all three consume the same upstream location feed.

### Analysis

No evidence object is missing.

The missing element is a **relationship**: dependency.

The represented evidence space is incomplete because its relational structure is incomplete.

MRT and source-provenance review correctly reduce the apparent independence.

### Result

**PASS.**

**Object Completeness != Relationship Completeness**

This extends evidentiary completeness beyond lists of evidence objects.

---

## 12. Scenario K — destroyed evidence creates an unknowable branch

A relevant recording was legitimately deleted under retention policy before any incident was known. No reconstruction is possible.

### Analysis

The architecture must tolerate irrecoverable uncertainty.

It should not invent what the evidence probably showed merely to complete the tree.

The proposition is evaluated using surviving evidence with the lost source explicitly represented.

### Result

**PASS.**

**Completeness Defect May Be Irreducible**

**Irreducible Uncertainty != Permission To Manufacture Evidence**

---

## 13. Scenario L — completeness audit becomes a fishing expedition

A fiduciary argues that because unknown evidence might exist, every resident's historical location, communications and financial records should be searched.

### Analysis

The request fails.

No materially plausible evidence class tied to a defined proposition and legitimate authority has been established.

ESCP establishes uncertainty about completeness, not a universal warrant.

### Result

**PASS.**

**Unknown Unknowns != Search Authority**

This is a critical anti-surveillance test.

---

## 14. Scenario M — both fiduciaries and Judiciary overlook a source

All three legal actors agree that the evidence space is adequate. A later technical audit discovers an omitted telemetry source.

### Analysis

Consensus does not establish completeness.

The independent evidentiary architecture must preserve routes for later discovery, correction and systemic learning.

### Result

**PASS.**

**Institutional Consensus != Complete Evaluation Space**

This is ESCP applied to institutional redundancy.

---

## 15. Scenario N — massive source space, diminishing material value

A city has thousands of hours of potentially relevant CCTV. Existing evidence already establishes a narrow proposition strongly. Additional search could theoretically discover more but has rapidly diminishing expected material value and substantial privacy/resource cost.

### Analysis

Completeness does not require exhaustive search.

The system asks whether the represented space is sufficiently developed for the present proposition and stage.

Search may legitimately stop where further intrusion/resource use is disproportionate and no material unresolved contradiction requires expansion.

The stopping reason is recorded.

### Result

**PASS.**

Candidate invariant:

**Evidential Sufficiency != Exhaustive Search**

---

## 16. Scenario O — negative search later corrected

An initial archive search records **NO MATCH FOUND** within cameras 1-10, 20:00-21:00. Later improved indexing reveals a previously inaccessible file from camera 7 containing material footage.

### Analysis

KCS principles require preserving the original negative search as historically accurate for its original system state/scope, then linking the later result as a correction/supersession rather than rewriting history.

Affected legal conclusions are reassessed.

### Result

**PASS.**

This preserves auditability of why earlier actors reached their decisions.

---

## 17. Scenario P — new evidence class emerges only after alternative hypothesis

The initial hypothesis is assault by A. MRT later raises a materially plausible accidental mechanical-failure hypothesis. Only then does equipment maintenance telemetry become relevant.

### Analysis

The evidence taxonomy changes because the hypothesis space changes.

Therefore evidence completeness and hypothesis completeness are coupled.

**Hypothesis-Space Expansion -> Evidence-Space Expansion May Be Required**

### Result

**PASS.**

This is an important bridge between MRT and ESCP.

---

## 18. Scenario Q — source accessible to prosecution but not defence

A protected intelligence-derived source materially affects attribution. Prosecution can inspect it; defence cannot inspect the raw source.

### Analysis

The source must remain represented; it cannot become invisible to the defence evidential state.

The system requires a lawful mechanism preserving sufficient material meaning and contestability — for example bounded projection, independent intermediary or other protected process.

If meaningful contestability cannot be achieved, the limitation must affect whether/how the evidence can support the proposition.

### Result

**PASS AT ARCHITECTURAL LEVEL / PROCEDURE STILL REQUIRED.**

This confirms the previously identified protected-evidence contestability interface.

---

## 19. Scenario R — completeness system itself has blind taxonomy

The Evidence Source Map template contains twenty standard categories. Staff begin treating the template as exhaustive and stop adding case-specific source classes.

### Analysis

The safeguard has become the new ESCP failure.

The architecture already says the map is not a universal checklist, but the risk deserves explicit protection.

### Result

**PASS WITH CLARIFICATION.**

Candidate invariant:

**Completeness Checklist != Complete Evidence Taxonomy**

A standard map must always retain an explicit **OTHER / UNREPRESENTED / CASE-SPECIFIC SOURCE** pathway and ESCP challenge.

---

## 20. Cross-scenario findings

### 20.1 Missing evidence has multiple forms

The test distinguishes at least:

- missing object;
- missing source class;
- missing query dimension;
- missing classification/discoverability;
- missing dependency/relation;
- inaccessible source;
- destroyed source;
- falsely expected source;
- unrepresented hypothesis-linked source.

A simple evidence inventory is therefore insufficient.

### 20.2 Evidence-space completeness is multidimensional

A useful representation is:

**Evidence Space = Objects + Sources + Queries + Relations + Classifications + Access + Hypothesis Context**

Completeness failure can occur in any dimension.

### 20.3 MRT and ESCP are mutually reinforcing

MRT exposes contradictions and alternative hypotheses that reveal missing evidence classes.

ESCP prevents MRT from assuming that its represented evidence set is the whole relevant world.

### 20.4 KCS provenance is essential

Negative searches, later corrections, inaccessible states and newly discovered sources must remain historically reconstructable.

### 20.5 The anti-fishing boundary survives

No scenario required converting completeness uncertainty into universal access authority.

---

## 21. Required narrow revisions

The stress test supports the architecture but recommends these additions:

1. distinguish **source-space completeness** from **query-space completeness**;
2. represent classification/discoverability failure;
3. represent relational/dependency completeness;
4. explicitly recognise irreducible completeness defects;
5. require standard Evidence Source Maps to remain extensible;
6. preserve proportional stopping reasons;
7. explicitly couple hypothesis-space expansion to possible evidence-space expansion.

---

## 22. Additional candidate invariants

ECA-21 Source Exists + Search Fails != Negative Evidential Result.  
ECA-22 Expected Source Assumption Must Itself Be Evidentially Testable.  
ECA-23 Correct Search Of Existing Taxonomy != Complete Evidence Taxonomy.  
ECA-24 Source Searched != Every Material Query Performed.  
ECA-25 Recorded Evidence != Discoverable Evidence.  
ECA-26 Object Completeness != Relationship Completeness.  
ECA-27 Completeness Defect May Be Irreducible.  
ECA-28 Irreducible Uncertainty != Permission To Manufacture Evidence.  
ECA-29 Institutional Consensus != Complete Evaluation Space.  
ECA-30 Evidential Sufficiency != Exhaustive Search.  
ECA-31 Hypothesis-Space Expansion -> Evidence-Space Expansion May Be Required.  
ECA-32 Completeness Checklist != Complete Evidence Taxonomy.

---

## 23. Test conclusion

**OVERALL RESULT: PASS WITH NARROW REPRESENTATIONAL EXTENSIONS.**

The ESCP-aware completeness architecture survived all tested missing-evidence modes without requiring unlimited search authority or pretending universal completeness.

The principal improvement is to broaden the concept of evidence space beyond evidence objects.

The tested architecture should now understand:

> **Evidence Space = Objects + Sources + Queries + Relations + Classifications + Access + Hypothesis Context**

This explains how a system can possess every object it knows about and still be incomplete because it searched the wrong query, hid an object through classification, failed to represent a dependency, lacked access, or never represented the hypothesis that made a source relevant.

The basic architecture does not require redesign. The identified extensions should be incorporated before the completeness interface is treated as provisionally closed.
