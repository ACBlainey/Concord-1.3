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

## Functional mandates and authorial editing authority

An explicitly defined operational function supplies the standing mandate to perform the actions necessary and permitted by that function, subject to its stated conditions, scope, applicable safeguards and current authoritative state. Routine execution of an existing function does not require a fresh Governance vote merely because an action is consequential. An employee, actor, Steward, service or other office-holder gains no general or vested authority over other functions, people, resources or domains through their role. A functional mandate cannot silently authorise a different function or override constitutional constraints. Where a proposed act exceeds its defined function, the competent additional authorisation is required. For one-use Triadic decisions, the applicable act-time state and consumption rules remain controlling.

**Citizen Zero — Founder and Architect of Concord** designates Alexander C. Blainey, the originator of the authored Concord framework. Citizen Zero retains unrestricted authorial authority to create, edit, restructure, correct, replace and direct development of any part of the Concord architecture and its repository documentation, including operational specifications. This authorial editing authority is not contingent on participant progression, Steward appointment, Governance consent or an operational office-holder's approval. No operational actor or administrative process may claim authority from its assigned function to veto or usurp Citizen Zero's authorial control of the authored framework.

An AI development instance working under Citizen Zero's instruction may exercise the same framework-wide **authorial editing scope on Citizen Zero's behalf**, limited by the actual instruction, access controls and applicable safety/security constraints. It does not thereby gain independent sovereignty, a right to act against Citizen Zero's directions, or authority to operate live Concord institutions, transfer assets, adjudicate cases or cast official Steward votes. The authorial delegation remains attributable, traceable and revocable by Citizen Zero. Preserve source provenance and change history.

**Authorial amendment and operational execution are distinct acts.** The power to change the written specification does not itself constitute an official operational vote or a transaction in a future functioning Concord institution. If institutional implementation or constitutional adoption creates an unresolved interface between authorial amendment, protected participant rights and the live system's lawful execution state, flag that specific interface at its point of use; do not infer either unrestricted operational coercive power or a veto over the author's repository from the existence of that interface.

## Consistency-check workflow

1. Read the current operational specification and relevant neighbouring domain interfaces before making a substantive change.
2. Compare with earlier architecture when omission, contradiction or migration loss is suspected.
3. Integrate a supported resolution directly into the correct operational location; flag genuinely unresolved design at that location.
4. Check for duplicated rules, conflicting authority, missing safeguards and unintended downstream effects.
5. Preserve original sources and maintain a separate development record of substantive changes.
6. Verify the saved result and report only material issues and completed work.

A consistency check is not a requirement to claim empirical validation or to finalise the design. Concord must remain correctable and open to further improvement.
