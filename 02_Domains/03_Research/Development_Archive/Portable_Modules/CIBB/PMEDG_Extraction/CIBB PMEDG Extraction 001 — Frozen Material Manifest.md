# CIBB PMEDG Extraction 001 — Frozen Material Manifest

**Frozen Set:** CIBB-PMEDG-EXTRACTION-001  
**Purpose:** Clean cross-instance portability evaluation.

The evaluator must receive exactly these four files:

1. `Concord Information Black Box — Portable Module Candidate 001.md`
2. `CRADP Blind Cross-Instance Test — CIBB PMEDG Extraction 001 — Test Brief.md`
3. `CIBB PMEDG Extraction 001 — Frozen Material Manifest.md`
4. `CIBB PMEDG Extraction 001 — Evaluator Response Template.md`

No CIBB Specification, Formal Model, source-resolution record, earlier CRADP test, Concord repository file, web source or prior Concord conversation is part of the frozen evaluation set.

## Clean-run rule
The clean evaluator should begin in a new conversation containing no earlier Concord context.

The evaluator should not search the web or repository.

If any frozen file is absent, the evaluator should stop and identify the missing file rather than reconstruct it.

## Provenance rule
The completed evaluator response is raw test evidence. Preserve it unchanged. Any later source resolution belongs in a separate document.
