# Private Local Evaluation — Portable Extraction Test 001 — Test Brief

**Status:** PMEDG PORTABLE EXTRACTION TEST / BLIND-STANDALONE USE
**Candidate:** Private Local Evaluation — Portable Module Candidate v0.1
**Evaluator:** Clean instance preferred
**External architecture search:** prohibited

## Task

Use only the supplied portable module candidate.

Do not assume it is correct or complete. Apply it to the unfamiliar cases below without relying on prior Concord knowledge.

For each case report:
- whether PLE applies;
- protected source;
- bounded query;
- semantic owner;
- query authority;
- result recipient;
- minimum result;
- cumulative-disclosure issue;
- freshness issue;
- downstream handoff;
- whether the module gives enough guidance;
- PASS / CONDITIONAL / FAIL.

If the module does not tell you what to do safely, identify the missing portable rule rather than inventing one.

## Case 1 — Building access without medical disclosure

A laboratory permits entry to a controlled area only when a worker currently satisfies a defined respiratory-fit condition. The underlying occupational-health record is protected. Security needs an entry decision, not diagnoses or test values.

The health condition can change.

## Case 2 — Competitive procurement

A procurement platform must determine whether a bidder satisfies a minimum financial-resilience condition. The bidder's protected accounts contain commercially sensitive information.

Several competing procurement authorities may issue similar threshold queries over time.

## Case 3 — Digital-service maturity threshold

A digital service may perform operation O only if its internal maturity record satisfies condition M. The maturity record contains proprietary architecture and incident information.

A customer needs to know whether O may be offered, not the internal record.

The service operator controls both the record and the evaluator.

## Case 4 — Museum provenance alert

A museum holds a protected provenance file because disclosure could identify vulnerable private owners.

A proposed loan requires determining whether any unresolved ownership dispute affects the object.

The borrowing institution asks for the complete provenance file "for certainty."

## Case 5 — Insurance repair eligibility

A vehicle insurer needs to determine whether damage condition D falls inside a particular repair programme.

The protected engineering/claims record contains unrelated prior accidents and owner information.

The insurer later asks increasingly specific damage predicates.

## Case 6 — Agricultural biosecurity

A farm's protected diagnostic record may show pathogen P.

A regional system needs affected farms to receive containment instructions. It does not initially need a central list of all matching farms.

A separate epidemiology team later requests prevalence statistics.

## Case 7 — Supplier certification network

Three companies in the same corporate group separately ask whether a supplier meets different certification thresholds. Combined answers could reconstruct most of the supplier's protected compliance profile.

## Case 8 — Cached machine-safety status

A factory control system received MACHINE_SAFE_FOR_OPERATION = YES at shift start.

A protected sensor/maintenance state changes four hours later.

The production scheduler wants to continue using the cached result until the next shift.

## Case 9 — Sensitive inspection query

A regulator is investigating a previously unknown failure mode. Merely revealing the query would disclose the suspected vulnerability.

The regulated organisation's source records must remain local.

## Case 10 — Correct private answer, invalid business rule

A platform privately asks whether a seller has completed training course C.

The platform then treats YES as proof that the seller can safely perform complex activity A, even though C is a poor predictor of A.

## Case 11 — Audit centralisation

A PLE deployment protects all source records locally but sends every exact result, participant/entity identifier, query and timestamp to a central audit warehouse.

Evaluate conformance.

## Case 12 — Unknown semantic relationship

A new query appears unrelated in wording to earlier queries, but the evaluator cannot establish whether it is statistically or semantically correlated with them.

A requester demands an immediate binary answer.

## Adversarial extraction questions

1. What is the minimum irreducible PLE kernel?
2. Which rules in the candidate are necessary for portability rather than Concord-specific governance?
3. Does the candidate accidentally depend on an unnamed external Concord architecture?
4. Can an implementer identify where PLE stops without knowing Concord?
5. Does the module distinguish privacy-preserving computation from substantive correctness?
6. Does it prevent result authority from becoming action authority?
7. Can it handle cumulative inference without prescribing one universal privacy technology?
8. Does it provide useful failure behaviour when semantic relationships are uncertain?
9. Which part, if any, should be removed from the portable module because it is not truly portable?
10. What missing rule, if any, blocks graduation?

## Decision

Recommend one:

- EXTRACTION FAIL — return to candidate development;
- EXTRACTION PASS WITH REVISION — portable core valid but module needs bounded changes;
- EXTRACTION PASS — candidate is standalone and ready for graduation review.

Explain the first blocking requirement if not an extraction pass.
