# V2 to V2.1 source-preservation audit 001 — Chapters 1–10

**Status:** Initial structural and quantitative audit; **NOT** a substantive clause-survival certification.

## Provenance and scope

- V2 baseline: author-provided local snapshot `Governance V2 Canonical (2).md` (15–16 October 2026), **not edited**; `# Chapter N` headings verified 1–215 without gaps or duplicates. Snapshot is external to this repository audit and is not asserted identical byte-for-byte to the GitHub source, whose connector fetch returned empty content.
- V2.1 comparison: `Sections/Section_01_Chapters_001-010_Subsection_Integration_Draft_004.md`, fetched from GitHub on 16 October 2026.
- Each chapter is delimited by its top-level `# Chapter N` heading and the next such heading. Character counts include the chapter heading, intervening blank lines and trailing material. Numbered subheadings count Markdown headings beginning with a numeric `N.x` identifier (depth 1–4). This is an inventory, **not** an exact-text diff.

## Chapter-level inventory

| Chapter | V2 characters | V2.1 characters | V2 numbered subheadings | V2.1 numbered subheadings | Initial observation |
| --- | ---: | ---: | ---: | ---: | --- |
| 1 | 48,654 | 50,316 | 34 | 35 | Additional material or altered text; verify retention and change provenance |
| 2 | 16,032 | 16,032 | 19 | 19 | Matching counts; verify text identity |
| 3 | 4,333 | 4,333 | 8 | 8 | Matching counts; verify text identity |
| 4 | 4,160 | 5,258 | 6 | 7 | Additional material or altered text; verify retention and change provenance |
| 5 | 14,523 | 14,523 | 15 | 15 | Matching counts; verify text identity |
| 6 | 24,538 | 24,538 | 29 | 29 | Matching counts; verify text identity |
| 7 | 8,009 | 9,093 | 13 | 14 | Additional material or altered text; verify retention and change provenance |
| 8 | 6,761 | 6,761 | 5 | 5 | Matching counts; verify text identity |
| 9 | 55,046 | 65,104 | 68 | 70 | Additional material or altered text; verify retention and change provenance |
| 10 | 3,743 | 3,743 | 4 | 4 | Matching counts; verify text identity |

## Findings and limitations

1. **All ten expected top-level chapter headings are present, sequential and unique** in the V2.1 section.
2. Chapters **2, 3, 5, 6, 8 and 10** have identical chapter character counts and numbered-subheading counts to the uploaded V2 snapshot. This is strong *screening evidence* for retention, **not proof of byte identity**.
3. Chapters **1, 4, 7 and 9** are longer in V2.1, with increased numbered-subheading counts. Inspect these chapter additions for source provenance, supersession, conflicts and whether every original substantive clause remains; added length cannot prove retention.
4. No source material was deleted or rewritten as part of this audit. No chapter is certified source-complete by this quantitative pass.
5. **Next required test:** exact normalized text comparison and paragraph-level diff for all ten chapters; classify each non-identical segment as retained, authorially corrected, additive, relocated, unresolved or potentially omitted. Then repeat for Sections 02–22 and earlier historical sources. Preserve the V2 snapshot unchanged.

**Issue linkage:** G-024 (preservation) and G-025 (migration-aware source authority). Any substantive contradiction found during comparison also links to G-023.

## Targeted boundary check — 16 October 2026

Original V2 terminal headings compared with V2.1: Chapter 1 ends at original §1.22, Chapter 4 at §4.6, Chapter 7 at §7.11, and Chapter 9 at §9.52. V2.1 adds Chapter 1 §1.23 (authority lifecycle), Chapter 4 §4.7 (aggregate authority), Chapter 7 §7.12 (differentiated accountability), and Chapter 9 §9.53 plus an introductory §9.0a (isolated voting and substitution). The added Chapter 1 heading had incorrectly duplicated original §1.21; corrected to §1.23 in commit `d20481c`. Original source clauses still require exact-text preservation verification; this check is not a certification.

## Distributed exact-phrase source retention check — 16 October 2026

A targeted comparison used **27 distinct original V2 phrases** selected across Chapters 1–10 (not merely chapter titles), including the original opening, middle and terminal portions of Chapters 1–9 where possible. All 27 exact strings occur within their **corresponding V2.1 chapter**, not only elsewhere in the document. Per-chapter matches: Ch1 5/5, Ch2 4/4, Ch3 2/2, Ch4 3/3, Ch5 3/3, Ch6 2/2, Ch7 3/3, Ch8 2/2, Ch9 2/2, Ch10 1/1. This confirms **sampled retention**, not exhaustive paragraph or clause survival. Chapter 1's duplicate §1.21 heading has separately been corrected to §1.23. Original V2 source unchanged.

**Authority status:** Governance V2.1 is the intended master and its settled rules are operative once textual conflicts and wording are corrected. This audit's unfinished preservation work does not make those rules provisional. G-024 remains open until full source comparison.
