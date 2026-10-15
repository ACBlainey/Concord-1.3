# V2.1 — Flagged Issues 2 — Reconciliation Register

## Purpose
This register records issues discovered during the V2.1 substantive duplication and source-preservation reconciliation. It is separate from the earlier `Flagged_Issues` work and its registers. All new working notes, comparison registers, and supporting reconciliation documents for this pass belong in this folder.

## Preservation rules
- This is architectural integration, **not editing**. Do not compress, abridge, paraphrase, simplify, or silently change substantive material.
- Preserve all unique reasoning, examples, qualifications, constraints, interfaces, and architectural details.
- Similarity is not proof of duplication. Only remove **obvious, demonstrable duplication** after verifying that no unique material is lost.
- Record conflicts and uncertain overlaps here for later resolution; do not silently choose between competing provisions.
- Historical source files remain available for provenance, but current unique architecture must survive in V2.1.
- Do not treat prior "canonical" labels as proof of completeness or validation.

## Issue numbering
Assign each newly identified issue a permanent sequential identifier: `FI2-001`, `FI2-002`, etc. Never reuse identifiers. Record the exact repository path, chapter/subsection, competing passages or precise locations, issue type, why it matters, and proposed follow-up. Do not label a suspected conflict resolved without explicit supporting verification.

## Issue register

| ID | Type | Exact source locations | Description and unique-material risk | Status |
|---|---|---|---|---|
| FI2-001 | Architectural conflict / superseded interpretation | `Outstanding_Issues_Register.md`, G-001 through G-003; `Sections/Section_02_Chapters_11-20_Subsection_Integration_Draft_004.md`, Chapter 12; `Sections/Section_03_Chapters_21-30_Subsection_Integration_Draft_004.md`, Chapters 28–30; `Sections/Section_06_Chapters_051-060_Subsection_Integration_Draft_004.md`, Chapter 54 | Older register asserts two matching votes settle ordinary decisions before the third vote, while later authorial clarification requires all three selected stewards to cast final votes for ordinary outcomes, with two sufficient only for emergency action. Compare actual chapter provisions and distinguish decision majority, vote completion, and emergency execution; preserve unique reasoning. | Needs source comparison |

| FI2-002 | Architectural overlap / possible redundant rule definition | `Sections/Section_01_Chapters_001-010_Subsection_Integration_Draft_004.md` §§9.26–9.34; `Sections/Section_06_Chapters_051-060_Subsection_Integration_Draft_004.md` §§54.26–54.35 | Decision-record fields, minority reasoning, publication/privacy, audit, outcome review, reconsideration and supersession recur across Chapters 9 and 54. Chapter 54 includes distinct operational detail, custody integration and lifecycle controls; therefore do **not** delete either treatment. Compare rule ownership and identify only demonstrably redundant restatements. | Needs source comparison |
| FI2-003 | Architectural overlap / inconsistent completion gate | `Sections/Section_01_Chapters_001-010_Subsection_Integration_Draft_004.md` §9.53; `Sections/Section_02_Chapters_11-20_Subsection_Integration_Draft_004.md` §§12.0, 12.27; `Sections/Section_06_Chapters_051-060_Subsection_Integration_Draft_004.md` §54.38 | Repeated decision-state mechanics distinguish second matching vote, remaining third participation and host effect. The §54.38 assertion that outcome is determined 'without requiring a third occupied position' needs checking against later authorial requirement for three selected Stewards and three ordinary votes. Possible redundant/conflicting operative definitions across three chapters; retain unique state, record, owner and emergency details. | Pending decision |

| FI2-004 | Repeated architectural definition / spatial activation | `Sections/Section_14_Chapters_131-140_Clause_Integration_Draft_003.md` §§132.0, 132.4, 132.13; `Sections/Section_15_Chapters_141-150_Subsection_Integration_Draft_004.md` §§149.8, 149.16 | The same GTP invariants (all levels always exist, simultaneous operational resolutions, workload-driven activation, hysteresis, geometry not authority) are substantively defined in several places, including repeated definitions within Chapter 132 and Chapter 149. Chapter 132 includes unique geometry/continuity qualifications and Chapter 149 unique decentralisation framing; preserve all unique content. Check whether multiple independent operative definitions are erroneous rather than treating useful cross-references as duplicates. | Needs source comparison |
| FI2-005 | Repeated architectural definition / shared competence | `Sections/Section_14_Chapters_131-140_Clause_Integration_Draft_003.md` §132.5; `Sections/Section_15_Chapters_141-150_Subsection_Integration_Draft_004.md` §§149.17, 150.11–150.13; `Sections/Section_16_Chapters_151-160_Subsection_Integration_Draft_004.md` §§151.13–151.14; `Sections/Section_20_Chapters_191-200_Subsection_Integration_Draft_004.md` §§198.9, 198.21–198.23 | Multiple provisions independently restate that conference/adjacency/mesh scale cannot create shared jurisdiction and binding action requires lawful common competence. Distinct portable-module interfaces, externality examples, federation, permission composition and jurisdiction remedies are unique and must remain. Determine primary architectural ownership and whether any restatement is genuinely erroneous duplication. | Needs source comparison |
| FI2-006 | Possible conflicting interpretation / geometric versus institutional nesting | `Sections/Section_16_Chapters_151-160_Subsection_Integration_Draft_004.md` §§151.1, 151.13; `Sections/Section_14_Chapters_131-140_Clause_Integration_Draft_003.md` §§132.0, 132.3; `Sections/Section_20_Chapters_191-200_Subsection_Integration_Draft_004.md` §§198.10, 198.21 | §151.1 uses 'nested governance' and discusses multiple layers, while later provisions deny any GTP-derived superior/subordinate relationship. Institutional federation may independently establish hierarchy; verify that 'nested' does not imply geometric inheritance of authority. Existing §151.13 already flags this, so do not assume a fresh substantive conflict or remove language. | Needs source comparison |

## Reconciliation log

- 2026-10-15: Compared substantive GTP mesh, decentralisation, central coordination, federation and jurisdiction provisions in Chapters 132, 149, 150, 151 and 198. Recorded FI2-004–006 as architectural overlap/interpretation candidates; no deletion or rewriting.


- 2026-10-15: Direct chapter-level architectural comparison of Chapter 9 and Chapter 54 identified overlapping decision-record and lifecycle mechanisms (FI2-002) and repeated triadic completion rules (FI2-003). These are candidates, not permission to delete; no substantive text changed.


- 2026-10-15: Reviewed V2.1 README, Change Register, G05 integration/graduation register, G05 source-to-rule map, G05 architecture and Outstanding Issues Register. Shifted audit from literal matches to substantive architectural overlap and contradictions. FI2-001 opened as a candidate requiring chapter-level verification. No substantive architecture changed.


- 2026-10-15: Register established as a clean, separate workspace. Existing earlier issue registers are unchanged. Section 22's prior exact-line source-preservation comparison reported zero missing non-empty lines; this is not a semantic duplication/conflict clearance.


- 2026-10-15: Preliminary exact-block duplication scan completed across 22 integration files (3,140 substantive blocks, checked in two batches of 8 and 14 files). No repeated normalized full blocks within either batch. Cross-batch, partial-overlap, and semantic duplication checks remain outstanding. No source text was changed and no issue was numbered without a verified candidate.

## Status vocabulary
- **Open** — issue identified, awaiting examination.
- **Needs source comparison** — relevant passages require direct comparison.
- **Pending decision** — architectural choice must be made later.
- **Verified duplicate** — exact redundant material confirmed with no unique detail lost.
- **Resolved** — supported by documented reconciliation and verification.
