# Concord Contextual Trust Progression — Deterministic Validator 001

This validator defines cross-field rules supplementing JSON Schema 001.

For each record:

## ERR
V-ERR-01 If projectionState = PROJECTED, sourceProviderRef and evidenceProjectedAt MUST exist.
V-ERR-02 If correctionState = CORRECTED or PARTIALLY_CORRECTED, correctionRef MUST exist.
V-ERR-03 If correctionState = SUPERSEDED, supersedesRef MUST exist.
V-ERR-04 If disputeState = OPEN or RESOLVED and dispute is material to consequential use, disputeRef MUST exist.
V-ERR-05 If evidenceType = NON_EVENT_OBSERVATION, observationCoverage MUST NOT equal NOT_APPLICABLE.
V-ERR-06 If reviewState = REQUIRED, reviewOrExpiry MUST exist.
V-ERR-07 Recommendation evidence MUST remain typed RECOMMENDATION when projected/imported.

## ETR
V-ETR-01 Every materially changed requested exposure dimension MUST have one DimensionTransition.
V-ETR-02 PARTIALLY_APPROVED_BOUNDED requires at least two DimensionTransitions with materially different dispositions and at least one approved/approved-with-controls plus at least one non-approved disposition.
V-ETR-03 APPROVED_WITH_ADDITIONAL_CONTROLS requires non-empty addedControls.
V-ETR-04 Any DimensionTransition APPROVED_WITH_CONTROLS requires non-empty dimension addedControls or applicable record-level controls.
V-ETR-05 If prerequisite applicability = NOT_REQUIRED_FOR_FUNCTION, state MUST = NOT_APPLICABLE.
V-ETR-06 If prerequisite applicability = REQUIRED, state MUST NOT = NOT_APPLICABLE.
V-ETR-07 For ordinary approval states APPROVED_BOUNDED or APPROVED_WITH_ADDITIONAL_CONTROLS, no REQUIRED prerequisite may be UNKNOWN, NOT_SATISFIED or DISPUTED.
V-ETR-08 For PARTIALLY_APPROVED_BOUNDED, any approved dimension depending on a prerequisite may not rely on REQUIRED UNKNOWN/NOT_SATISFIED/DISPUTED prerequisite.
V-ETR-09 If consequenceAssessment.consequential = true, all prerequisite wrappers and both material exception arrays MUST be present.
V-ETR-10 If reviewState = REQUIRED, reviewTime and reviewFailureDisposition MUST be present and reviewFailureDisposition MUST NOT be NOT_APPLICABLE.
V-ETR-11 If reviewState = NOT_REQUIRED, reviewFailureDisposition when present MUST = NOT_APPLICABLE.
V-ETR-12 If decisionState = ENDED, endReason MUST exist.
V-ETR-13 authorityPrerequisite.basisRef MUST NOT identify CTP/ETR itself as the sole authority basis.
V-ETR-14 Empty errSet is valid and MUST NOT be interpreted as adverse evidence.
V-ETR-15 evidenceSufficiencyState = NOT_REQUIRED_FOR_TRANSITION permits empty errSet.
V-ETR-16 Overall decision MUST be consistent with DimensionTransition dispositions.
V-ETR-17 A voluntary participant-requested narrowing MUST NOT require adverse evidence.
