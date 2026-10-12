# Glass Hammer — Concern and Independent Review Integration 116

**Status:** source-reconciled fixture; not a new Judiciary power or production review service.

## Directly inspected V1.3 sources

- `02_Domains/05_Judiciary/Judicial Process Architecture — Matter Intake Adjudication Review and Closure 001.md`: Judiciary receives, classifies, determines jurisdiction, adjudicates, remedies and reviews; it is not general Governance or investigation.
- `02_Domains/06_Historical/Validation/Historical Domain — Cross-Domain Interface Test 002 — Judiciary, Governance and the Historical Event Spine.md`: Historical preserves claimed/exercised/legitimate authority, decision history, review and supersession without granting present authority.
- `03_Cross_Domain_Architecture/Cross-Architecture Review Composition — Existing STRA Boundary and Residual Gap — Source Resolution 001.md`: STRA owns review-trigger routing, provenance and duplicate suppression, not review outcomes; distinct grounds must not be collapsed.

## Implemented bounded adapter

A Steward may append an attributable concern after a validly committed ballot. Corrections are new linked records, never ballot edits. The concern creates an outbox item for STRA-style routing, **not** a judicial decision or an automatic stay.

A separate authority-gated referral can be recorded. A replacement-decision proposal requires a separate authority input, a new decision ID and exclusion of the original Steward named by the concern. No replacement vote or decision is created automatically.

No post-vote concern can withdraw a committed ballot, change a tally, or reactivate the original Steward's consumed authority.

## Limits

- `authority_valid` is fixture input, not independently verified owner-issued authority. Integrate Stage 101's registry and jurisdictional owner before graduation.
- The outbox is not connected to STRA, Civil Contact or Historical; it is an adapter boundary only.
- Sealed vote privacy, coercion reporting, pseudonymous identity aliases, role-appropriate replacement-panel selection and evidence access controls require Contextual Wrapper / Judiciary / Historical integration.
- Review of ballot validity (forgery, corruption or absence of original authority) is separate from voluntary vote withdrawal.
- Neither a concern nor a review referral automatically stays a lawful implementation; any stay requires its own legitimate authority.
