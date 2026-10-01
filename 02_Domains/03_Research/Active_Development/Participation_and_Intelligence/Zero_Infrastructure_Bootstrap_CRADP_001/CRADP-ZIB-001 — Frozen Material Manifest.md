# CRADP-ZIB-001 — Frozen Material Manifest

**Frozen Set:** CRADP-ZIB-001  
**Date:** 1 October 2026  
**Status:** FROZEN EVALUATOR PACKAGE

## Authoritative Evaluator File Set

The clean evaluator must receive exactly these four files:

1. `Concord Zero-Infrastructure Bootstrap — Specification 002.md`
2. `CRADP Blind Cross-Instance Test — Concord Zero-Infrastructure Bootstrap 001 — Test Brief.md`
3. `CRADP-ZIB-001 — Frozen Material Manifest.md`
4. `CRADP-ZIB-001 — Evaluator Response Template.md`

## Excluded Material

Do not provide:
- Source Resolution and Architecture Development Note 001;
- Pre-CRADP Adversarial Test Matrix 001;
- Pre-CRADP Internal Evaluation 001;
- Pre-CRADP Internal Evaluation 002;
- wider Concord repository material;
- prior evaluator responses;
- expected findings;
- source-resolution discussion;
- web sources;
- prior Concord conversation context.

## Clean-Instance Rule

Start a new evaluator conversation with no prior Concord context.

Provide only the frozen ZIP/package.

The evaluator must not search for or reconstruct excluded Concord architecture.

If any declared file is absent, the evaluator should stop and identify the missing file.

## Integrity Rule

The ZIP/package contents must match this manifest exactly.

If a frozen evaluator-facing file changes, create a new frozen package/version. Do not silently replace one member of the existing frozen set.

## Evidence Rule

The completed evaluator response is raw test evidence.

Preserve it unchanged before any source resolution, interpretation or repair.
