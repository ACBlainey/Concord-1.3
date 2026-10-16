# V2 to V2.1 Source Preservation Audit 008 — 125 Chapters, Direct Verbatim Comparison

**Scope:** Chapters 31–50, 61–90, 101–130 and 161–190, 201–215 (13 complete V2.1 section pairs; 125 chapters). Each source-preserved chapter was compared against the chapter of the same number in the corresponding latest subsection-integration file, not merely against document-length statistics.

**Method:** For each section, fetch `Section_XX_Chapters_..._Source_Preserved_001.md` and `Section_XX_Chapters_..._Subsection_Integration_Draft_001.md`, split on top-level `# Chapter N` headings and check whether the **entire source chapter string** occurs contiguously within the corresponding integrated chapter. Check exact equality separately. The comparison is direct string equality, not a probabilistic fingerprint.

## Findings

| Section | Chapters | Full contiguous source text preserved | Exceptions |
| --- | --- | ---: | --- |
| 04 | 31–40 | 10/10 | None |
| 05 | 41–50 | 10/10 | None |
| 07 | 61–70 | 10/10 | None |
| 08 | 71–80 | 10/10 | None |
| 09 | 81–90 | 9/10 | Chapter 83 renumbered headings |
| 11 | 101–110 | 10/10 | None |
| 12 | 111–120 | 10/10 | None |
| 13 | 121–130 | 10/10 | None |
| 17 | 161–170 | 10/10 | None |
| 18 | 171–180 | 10/10 | None |
| 19 | 181–190 | 10/10 | None |
| 21 | 201–210 | 10/10 | None |
| 22 | 211–215 | 5/5 | None |

**Result: 124/125 entire source chapters are preserved as a single verbatim contiguous text block in their V2.1 integrated counterpart.**

### Chapter 83 exception — numbering correction, not omitted source prose

Chapter 83's original full text does not appear as one contiguous substring because its heading `## 83.8 New Evidence` was renumbered `## 83.18 New Evidence` in V2.1 (and following headings adjusted to remove collision with pre-existing §§83.8–83.17). Direct inspection shows the original source section headings' **titles** remain present. All **34 original prose paragraphs longer than 90 characters**, excluding headings, occur verbatim in the V2.1 Chapter 83. This supports preservation of the original substantive paragraphs while allowing changed section numbering and new material; it is not a proof that every short fragment and heading remains byte-for-byte unchanged.

### Interpretation and limitations

- Contiguous full-text preservation is strong evidence that no text was removed from the corresponding source-preserved chapter; it does **not** prove the appended V2.1 additions are conflict-free or constitutional.
- The preserved files are repository source baselines. This audit does **not** independently compare those baselines with the author's local original V2 for all 125 chapters. That remains a separate source-authenticity check.
- Source and integrated files remain unchanged by this audit. V2.1 is the intended operative governance master after wording/conflicts are reconciled; historical V2 source is not a competing operative authority.
- Remaining detailed conflict checking should focus on **added clauses**, especially voting completion, emergency exceptions, authority consumption, GTP mesh semantics and appeal/finality distinctions. Do not reopen already verified preserved paragraphs merely because newer additions follow them.
