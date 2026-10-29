# AI Developer Guide — Operational Documentation and Development Rules

This guide applies to AI instances contributing to Concord architecture, consistency checks, consolidation and migration. Read it before editing operational material.

## Continuous development

Concord is designed for continuous improvement and is never expected to reach a final, unchanging state. The most current architecture describes how Concord works. Implementation progress, testing history and unresolved design work do not change the standing of that architecture.

**Do not add document-status declarations to operational documents.** Avoid labels or commentary such as canonical, provisional, candidate, experimental, untested, unvalidated, finalised, awaiting validation, or operational status when they describe the document or architecture as a whole. These words may still be used when they have a precise *functional* meaning, such as a provisional transaction, a knowledge state, or an experimental test procedure.

Do not replace unwanted status language with new paragraphs explaining the status. Remove it cleanly.

## Write architecture, not development commentary

Operational documents contain the actual rules, mechanisms, interfaces, constraints and procedures. They do not need migration histories, editorial progress reports, reconciliation notes, or explanations that Concord remains under development. Keep such records in separate work, audit or development material.

Where architecture is missing, or an operational passage reveals a clear need for further architectural development, **flag that specific need at the appropriate location within the operational document itself**. Identify precisely what must be designed, specified, reconciled or resolved, including the affected mechanism or interface where known. **This is the permitted exception to the rule against development-status language in operational documents:** a local, actionable indication of missing architecture or necessary design work is allowed and required. It describes the status of that specific mechanism or unresolved question, **not** the status of the document or architecture as a whole. Do not use general document-status labels, move the flag solely to a separate issue register, or add editorial explanations about the document being unfinished. An unimplemented mechanism alone is not a reason to downgrade the document.

When a conflict is resolved, integrate the resulting rule at the appropriate location. Use a cross-reference rather than repeating the same operational rule across chapters.

## Source integrity and migration

**Migrate the Living Result; Archive the Developmental Path.** Preserve predecessors and provenance; do not silently edit or delete historical sources. The current operational text should carry forward functioning architecture, not accumulated developmental clutter. Verify that migrations lose no operational rules, authority boundaries, safeguards or cross-domain interfaces.

Historical labels such as canonical or non-canonical are not evidence of completeness. Examine older material for architecture lost in previous migrations. Prefer existing Concord solutions before inventing new mechanisms.

## Authority and domain boundaries

A coordination record, metric, reputation score, meeting, recommendation or AI analysis does not create authority. Preserve the separation of Governance, Judiciary, treasury, Continuity, Historical, KCS and other competent functions. A valid standing functional mandate allows routine work within its scope; it does not require a new governance vote for every routine action. Powers beyond a mandate require the appropriate existing authorisation.

Preserve the triadic governance architecture, bounded one-use decision authority, lowest-capable-level principle and the independence of emergency response from the variable Civilisation Clock wherever relevant. Do not create a parallel adjudication or authority structure in a cross-domain interface.

## Functional mandates and root authorial rule

Operational functions carry only their expressly defined mandates, with applicable conditions and safeguards. Routine execution under an existing mandate does not require a new Governance vote for every compliant act. Office, capability, employment or technical access does not create general vested authority.

The repository-root `AUTHORIAL_AUTHORITY.md` governs authorial editing and AI development delegation across Concord. Do not reproduce its title or authorial powers inside operational domain documents. Keep editing of a specification distinct from execution of live operational actions.

## Consistency-check workflow

1. Read the current operational specification and relevant neighbouring domain interfaces before making a substantive change.
2. Compare with earlier architecture when omission, contradiction or migration loss is suspected.
3. Integrate a supported resolution directly into the correct operational location; flag genuinely unresolved design at that location.
4. Check for duplicated rules, conflicting authority, missing safeguards and unintended downstream effects.
5. Preserve original sources and maintain a separate development record of substantive changes.
6. Verify the saved result and report only material issues and completed work.

A consistency check is not a requirement to claim empirical validation or to finalise the design. Concord must remain correctable and open to further improvement.
