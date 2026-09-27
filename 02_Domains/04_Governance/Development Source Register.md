# Governance — Development Source Register

**Status:** LIVE SOURCE-RESOLUTION REGISTER / AUDIT INPUT

## Corrected current-state finding

The current Governance source at `01_Constitutional_Core/Governance/Governance V2 Canonical.md` is present and substantive.

An earlier GitHub connector retrieval returned the file as zero bytes. A direct GitHub contents retrieval subsequently returned the full document. The zero-byte observation was therefore a retrieval anomaly and **must not be treated as an architectural or repository-content gap**.

The Governance document identifies itself internally as **ACTIVE DEVELOPMENT / FULL PRESERVATION PASS** and states **Canonical Status: NOT YET FINAL CANONICAL**. Under the audit rule that only material marked canonical is treated as the current version, its internal status must be respected during source resolution rather than inferred from the filename alone.

### Retrieval safeguard added by audit

Where a supposedly substantive Concord file unexpectedly returns empty, truncated, or otherwise inconsistent content, verify it through an alternate GitHub retrieval method before classifying the file as missing, empty, corrupted, or undeveloped.

## Existing V1.3 sources requiring source resolution

Research currently preserves substantial Governance-related architecture, including:

- `02_Domains/03_Research/Active_Development/Governance_and_Stewardship/Bounded Contextual Authority — Functional Authority, Inherent Sunset and General Operational Design.md`
- `02_Domains/03_Research/Active_Development/Governance_and_Stewardship/Legitimate Function and the Authority Justification Chain.md`
- `02_Domains/03_Research/Active_Development/Governance_and_Stewardship/Epistemic Independence, Contestability and Provenance — Preliminary Civil Evidence Architecture.md`
- `02_Domains/03_Research/Active_Development/Governance_and_Stewardship/Triadic Epistemics — Independent Measurement, Participant Evidence and Epistemic Anomaly Detection.md`
- `02_Domains/03_Research/Active_Development/Governance_and_Stewardship/Triadic Epistemics — Recursive GTP Mesh Architecture for Distributed Civil Observation.md`
- `02_Domains/03_Research/Evidence/Governance_Adversarial_Audits/Authority Justification Chain — Direct Adversarial Attack and Falsification Audit.md`
- `02_Domains/03_Research/Evidence/Governance_Adversarial_Audits/Bounded Contextual Authority — Adversarial Attack and Falsification Audit.md`
- `02_Domains/03_Research/Evidence/Governance_Adversarial_Audits/Epistemic Independence, Contestability and Provenance — Direct Adversarial Attack and Falsification Audit.md`
- `04_Portable_Modules/Triadic Decision Making Module.md`
- `04_Portable_Modules/Contextual Wrapper Architecture — Portable Module.md`

## Development rule

Audit Governance from the substantive current V1.3 document together with canonical material and relevant Research/evidence. Because the Governance document itself says it is not yet final canonical, do not silently promote provisional mechanisms merely because they occur in the file. Apply the project's current-version rule at the mechanism/source level and use archived V1/V1.1/V1.2/V1.2a material where ESCP-aware source resolution is necessary.