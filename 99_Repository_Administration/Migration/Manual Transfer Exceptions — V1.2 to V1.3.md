# Manual Transfer Exceptions — V1.2 → V1.3

**Status:** LIVE EXCEPTION REGISTER

These objects have been source-resolved for V1.3 but could not be transferred through the current GitHub connector. Their failure does **not** halt migration. They must be copied manually from the V1.2 snapshot/repository to the exact target path below and then verified.

| ID | Source path in V1.2 | Intended V1.3 target | Reason | State |
|---|---|---|---|---|
| XFER-001 | `01_Constitutional_Core/The Concord.md` | `01_Constitutional_Core/The Concord.md` | Large authoritative source exceeds safe connector transfer path | MANUAL TRANSFER REQUIRED |
| XFER-002 | `01_Constitutional_Core/Recursive Constitutional Architecture V2/Recursive Constitutional Architecture V2 Canonical.md` | `01_Constitutional_Core/Recursive Constitutional Architecture V2/Recursive Constitutional Architecture V2 Canonical.md` | Very large authoritative source exceeds safe connector transfer path | MANUAL TRANSFER REQUIRED |
| XFER-003 | `01_Constitutional_Core/Governance/Governance V2 Canonical.md` | `02_Domains/04_Governance/Governance V2 Canonical.md` | Large/current source; connector transfer path unsuitable | MANUAL TRANSFER REQUIRED |
| XFER-004 | `01_Constitutional_Core/Judiciary V2/Judiciary V2 Canonical.md` | `02_Domains/05_Judiciary/Judiciary V2 Canonical.md` | Very large authoritative source exceeds safe connector transfer path | MANUAL TRANSFER REQUIRED |
| XFER-005 | `01_Constitutional_Core/Constitutional Emergency V2/Constitutional Emergency V2.md` | `03_Cross_Domain_Architecture/Emergency_Coordination/Constitutional Emergency V2.md` | Connector content/safety block | MANUAL TRANSFER REQUIRED |
| XFER-007 | `06_Portable_Modules/Reality Trees — Portable Module.md` | `04_Portable_Modules/Reality Trees — Portable Module.md` | Connector content/safety block | MANUAL TRANSFER REQUIRED |
| XFER-008 | `06_Portable_Modules/Safe Spaces, Special Jurisdictions and Bounded Legal Variation — Concord Wrapper Architecture for Internal Peaceful Distance.md` | `04_Portable_Modules/Safe Spaces, Special Jurisdictions and Bounded Legal Variation — Concord Wrapper Architecture for Internal Peaceful Distance.md` | Connector content/safety block | MANUAL TRANSFER REQUIRED |
| XFER-006 | `11_Intercivilisational_Architecture/04_Intercivilisational_Protocols/Functionally Bounded Summits — Failure-Contained Negotiation for Hostile and Low-Trust Interoperability.md` | `04_Portable_Modules/Functionally_Bounded_Summits/Functionally Bounded Summits — Failure-Contained Negotiation for Hostile and Low-Trust Interoperability.md` | Connector content/safety block | MANUAL TRANSFER REQUIRED |

| XFER-009 | `11_Intercivilisational_Architecture/01_Concord_Civilisational_Wrapper/README.md` | `02_Domains/08_Intercivilisational_Relations/Civilisational_Wrappers/README.md` | Connector content/safety block | MANUAL TRANSFER REQUIRED |
| XFER-010 | `11_Intercivilisational_Architecture/07_Disputes_Jurisdiction_and_Externalities/CBERRM Companion Upgrade 001 — Scoped Standing, Materiality and Responsibility Architecture.md` | `02_Domains/08_Intercivilisational_Relations/Externalities/CBERRM Companion Upgrade 001 — Scoped Standing, Materiality and Responsibility Architecture.md` | Connector content/safety block | MANUAL TRANSFER REQUIRED |
| XFER-011 | `08_Active_Development/01_DEVELOPMENT_NOTES/03_CONCORDIAN_METHODOLOGY/Outliers as Gateways to Hidden Architecture — Methodological Observation.md` | `02_Domains/03_Research/Methodologies/Outliers as Gateways to Hidden Architecture — Methodological Observation.md` | Connector content/safety block | MANUAL TRANSFER REQUIRED |

## Verification rule

After manual transfer, compare the V1.3 Git blob SHA or file bytes against the V1.2 source. Do not mark an exception complete merely because a file with the same name exists.

> **Transfer Failure != Migration Failure**

> **Manual Transfer != Manual Rewriting**
