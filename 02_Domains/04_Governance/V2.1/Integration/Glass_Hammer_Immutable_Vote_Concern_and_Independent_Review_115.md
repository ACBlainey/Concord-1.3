# Glass Hammer — Immutable Vote, Subsequent Concern and Independent Review 115

**Status:** authorial clarification and correction to the Stage 113–114 revocation framing; integration candidate, not a new power.

## Authorial clarification

A Steward deliberates in isolation and exercises a single-use decision authority. Once the Steward commits a valid ballot, the authority for that ballot is consumed and the ballot **stands**. The Steward cannot recall, revoke, revise or replace that vote by invoking the already-consumed authority.

Permitting post-commit withdrawal risks disclosure of other votes, peer pressure, coercion and loss of independent deliberation. The three-room isolation model is intended to prevent exactly that.

## Separate objects and authority

1. **Committed ballot:** immutable, independently attributable, single-use record. A committed vote remains a fact of the decision history.
2. **Subsequent concern:** an additional record with author, time, explanation and supporting evidence. It is neither a second ballot nor a revocation; it does not change the original tally.
3. **Review:** separately initiated and authorised process, with bounded scope and independent evaluation. The original Steward's concern can trigger consideration but does not itself decide the review.
4. **Replacement decision:** if legitimate review requires a new decision, it has a new decision ID, newly established authority and independently selected eligible Stewards. The original Steward whose vote is under review is excluded from the replacement panel where the independence safeguard applies. Review must avoid revealing ballots to decision-makers before their own commitments.
5. **Implementation authority:** a downstream execution grant or still-unexercised contextual authority may expire, be revoked or become invalid on independent lawful grounds. This does not erase a committed vote or retroactively uncast it.

## Exception: validity versus withdrawal

An alleged unauthorised ballot, forged attribution or corrupted record is a challenge to whether a valid commitment occurred, not a permission for a Steward to withdraw a valid vote. Preserve the original evidence and challenge outcome in an append-only provenance chain. The proper authority determines consequences and remedies; do not silently overwrite history.

## Correction to prior stages

- Stage 113 and Stage 114 discussed owner revocation near decision acceptance. **Clarify the target**: revocation applies to a live unexercised grant or downstream execution authority, never to a legitimately committed Steward ballot.
- Stages 108, 110 and 112 already model one-use voting and no outcome reversal by the late third vote. They should be extended with explicit post-vote concern, review referral and replacement-decision tests, rather than adding ballot-revocation methods.
- The contextual early-acceptance rule remains unchanged: two matching votes determine the result; justified contexts may permit early progression; the third Steward may independently record their remaining vote while their contextual eligibility persists.
- CRSTL, BTA, ESCP and Historical retain provenance; none may rewrite a committed ballot or mint review authority.

## Adversarial tests required

- A Steward attempts to change a ballot after learning the other two votes: reject.
- The same Steward resubmits under a new event ID: reject.
- The Steward files a subsequent justified concern: append a separate record, no tally change.
- Concern is withdrawn or corrected: append a new record; do not erase history.
- Peer pressure is reported: retain protected provenance, refer through independent review without exposing sealed ballots.
- Review accepts a case: require fresh, independently established authority and a new decision identity for any replacement ballot.
- Replacement selection excludes the original Steward where required; prevent identity aliases from defeating exclusion.
- A downstream host grant expires or is revoked: stop the unexecuted action, retain the original vote.
- A forged or invalid ballot is discovered: preserve evidence and refer for validity adjudication rather than silently modifying the recorded vote.

## Open integration questions

Exact eligibility/exclusion scope for replacement panels, protected handling of concern evidence, threshold for initiating review, and interaction with a completed implementation require reconciliation with existing Governance, Judiciary, Contextual Wrapper and Historical sources. Do not invent a unilateral veto or a blanket replacement rule.
