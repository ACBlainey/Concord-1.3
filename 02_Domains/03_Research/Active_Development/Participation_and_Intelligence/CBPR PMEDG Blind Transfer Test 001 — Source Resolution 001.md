# CBPR PMEDG Blind Transfer Test 001 — Source Resolution 001

**Date:** 2 October 2026
**Status:** PMEDG EXTRACTION REPAIR / NOT CANONICAL

## Finding

Test 001 correctly failed the supplied extraction package. It did not establish that the developed CBPR architecture lacks the reported mechanisms. The evaluator received the Candidate and Extraction Audit, not Service Specification 002, Formal Model 002 or Schema 002.

## Deficit Resolution

| Evaluator deficit | Existing source resolution | Extraction action |
|---|---|---|
| CAP/PERM/AUTH undefined | Formal model distinguishes technical capability, service permission and legitimate authority; Specification requires no authority inference from capability | Define generically in module |
| enforcement/revalidation absent | Specification §§14–15 defines proposal → consequence/authority check → commit-time revalidation → commit | Include procedure |
| output taxonomy absent | Specification §13 provides seven consequence classes and downstream-actuator rule | Include taxonomy |
| unknown commit/retry absent | Specification §17 defines six commit states and reconciliation-before-retry | Include state model |
| recovery authority absent | Specification §20 + formal invariant: recovered state does not restore authority | Include recovery rule |
| composition absent | Formal Model 002 §§2–5 defines COMPOSED_EFFECT, COMPOSITION_OK, cross-grant, sequential and distributed composition | Include model |
| temporal evidence absent | Specification §7 + Formal Model §6 defines intended/observed time, clock source, trust, uncertainty and ordering | Include model |
| control conflict absent | Formal Model §7 defines CONTROL_EFFECTIVE conditions and no universal role hierarchy | Include rule |
| revocation absent | Credential bindings and commit-time current-state validation include revocation | Include |
| provenance underdefined | Specification §21 requires proportionate protected provenance and privacy/linkage controls | Define generic provenance interface |
| registry/succession dependency | BSR/BSuR are Concord implementations, not necessary portable primitives | Replace with generic service-description and succession-record interfaces |
| participant/operator status | Runtime needs authenticated service relationship and scoped control basis, not Concord citizenship | Define generic roles |
| key custody/storage ambiguity | Specification keeps credential/signing and CMSS separate dependencies | State exclusions explicitly |

## Extraction Error

The first package confused an **extraction audit** with an **extracted module**.

PMEDG Test 002 must evaluate the standalone module itself. Development evidence may remain excluded; the module must contain enough architecture to reproduce its constraints without those files.

## Disposition

**CBPR architecture revision required:** NO.

**Portable extraction revision required:** YES.

**Test 001:** VALID FAILED-TRANSFER EVIDENCE.

**Next:** Portable Module Candidate v0.9 → frozen Test 002.
