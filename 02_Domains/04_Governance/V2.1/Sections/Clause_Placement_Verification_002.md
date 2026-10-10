# Governance V2.1 — Clause-Placement Verification 002

**Date:** 11 October 2026  
**Status:** Developmental verification only; not canonical.

## Verified repository artifacts

| Section | Clause-placement draft | Original chapter headings | Proposed insertion blocks | Preservation check |
|---|---|---|---|---|
| 02 | `Section_02_Chapters_11-20_Clause_Placement_Draft_002.md` | 11–20, exactly ten | Chapter 12 | PASS |
| 03 | `Section_03_Chapters_21-30_Clause_Placement_Draft_002.md` | 21–30, exactly ten | Chapters 28, 29, 30 | PASS |

### Preservation test
For each repository Draft 002:
1. Retrieve the corresponding repository Working Assembly 001 and Draft 002.
2. Extract the original Chapter 11–20 or Chapter 21–30 source portion of Assembly 001, stopping before the former non-canonical annex.
3. Extract Draft 002 beginning at the first original chapter heading.
4. Remove only the explicitly delimited `V2.1 PROPOSED INSERTION` blocks and normalise terminal whitespace.
5. Compare source portions character-for-character.

**Result:** Both reconstructed source portions were equal to their respective Working Assembly 001 original chapter text. Chapter numbers were consecutive and unique. This check does **not** establish that Assembly 001 itself is byte-identical to the local V2 canonical file; that upstream source-extraction verification remains a separate task.

## Integration work remaining
- Move each proposed clause into the appropriate numbered V2 subsection with explicit conflict analysis; do not just append it indefinitely.
- Resolve GTP six-Steward vertex eligibility and authority.
- Validate all F/A/U combinations, substitution, recusal, non-action and recursive expansion termination.
- Complete Chapters 9, 54, 100, 132, 149–151, 198 and cross-references.
- Retain original V2 canonical untouched until the user authorises a distinct graduation step.

**No Governance V2 Canonical.md changes were made.**
