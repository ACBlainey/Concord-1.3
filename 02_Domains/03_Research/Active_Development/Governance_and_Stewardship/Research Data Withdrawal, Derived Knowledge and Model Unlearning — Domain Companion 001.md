# Research Data Withdrawal, Derived Knowledge and Model Unlearning — Domain Companion 001

**Project:** The Concord Framework  
**Date:** 6 October 2026  
**Status:** ACTIVE DEVELOPMENT / RESEARCH DOMAIN COMPANION / PROVISIONAL / NON-CANONICAL  
**Interfaces:** Withdrawal After Learning; Temporal Consent; CIBB; KCS Change Propagation; BTA; Historical; Research evidence/provenance

## 1. Purpose

Research must represent withdrawal truthfully across source data, derivatives, publications and trained models.

## 2. Separate states

A withdrawal event should not be represented as one generic deletion state.

Distinguish:
- SOURCE_COLLECTION_AUTHORITY;
- SOURCE_ACCESS_AUTHORITY;
- SOURCE_RETENTION_AUTHORITY;
- FUTURE_TRAINING_AUTHORITY;
- FUTURE_PARTICIPANT_SPECIFIC_INFERENCE_AUTHORITY;
- DERIVATIVE_RETENTION_STATE;
- PUBLICATION_STATE;
- MODEL_CONTRIBUTION_STATE;
- HISTORICAL_PROVENANCE_STATE.

## 3. Default transition

Where applicable:

`ACTIVE_RESEARCH_AUTHORITY -> WITHDRAWN_FOR_FUTURE_USE`

This does not imply:

`PRIOR_RESEARCH_NEVER_AUTHORISED`

or:

`ALL_DERIVED_KNOWLEDGE_ERASED`

## 4. Source data

Where retention authority ends, delete or seal the source according to the applicable legitimate rule.

Record enough protected provenance to establish that withdrawal occurred and what actions followed.

## 5. Future training

Withdrawal should ordinarily prevent new training/fine-tuning on the withdrawn source where the withdrawn authority was the training basis.

> **Prior Training Authority != Future Training Authority**

Copies, caches, vector stores and derived training corpora should be included where they remain materially source-equivalent.

## 6. Existing model

Do not claim a trained model has forgotten a participant merely because the source record was deleted.

Possible states include:
- SOURCE_REMOVED_MODEL_UNCHANGED;
- UNLEARNING_ATTEMPTED_UNVERIFIED;
- UNLEARNING_VALIDATED_WITHIN_SCOPE;
- MODEL_RETRAINED_WITHOUT_SOURCE;
- PARTICIPANT_SPECIFIC_RECOVERABILITY_BLOCKED;
- CONTRIBUTION_EFFECT_INSEPARABLE_OR_UNKNOWN.

## 7. Unlearning evidence

A claim of unlearning should specify:
- target;
- method;
- validation;
- scope;
- residual recoverability;
- uncertainty.

> **Unlearning Procedure != Demonstrated Unlearning**

## 8. Proportionality

Whether retraining/unlearning is required should consider:
- original consent/authority terms;
- sensitivity;
- participant-specific memorisation/recoverability;
- consequence;
- scale of contribution;
- technical feasibility;
- cost/resource burden;
- available mitigations;
- future use.

No universal automatic retraining rule is assumed.

## 9. Published findings

Legitimately published aggregate knowledge does not become false merely because a participant later withdraws.

But if withdrawal materially changes statistical validity, cohort sufficiency or a participant-specific claim, the research object should be reviewed.

## 10. Future-use firewall

Where model knowledge cannot be removed, Research can still:
- block participant-specific querying;
- remove identifiers/linking keys;
- prevent future source retrieval;
- prevent future training;
- prohibit specified uses;
- constrain deployment context.

## 11. Participant communication

Do not promise “your data is completely gone” unless that is actually established.

A truthful withdrawal response should distinguish what was:
- deleted;
- retained;
- sealed;
- already published;
- already learned;
- excluded from future use;
- subject to unlearning/retraining;
- technically uncertain.

## 12. Central rule

> **Research Withdrawal Must Change The Authorities And Data States That Can Actually Be Changed, Preserve Honest Provenance About What Already Occurred, And Never Use Model Complexity As A Fictional Escape From A Legitimate Withdrawal Right.**
