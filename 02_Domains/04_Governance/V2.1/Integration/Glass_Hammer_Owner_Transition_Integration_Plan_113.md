# Glass Hammer — Owner Transition and Emergency Reconciliation 113

**Status:** integration plan and explicit non-graduation register, not an implementation or new authority source.

## Confirmed architecture

- The individual Steward ballot is a context-bound single-use exercise (glass hammer).
- Two matching votes determine the result; contextual early acceptance may allow progression before the third vote. Emergency urgency is an example, not an exhaustive list of allowable contexts.
- Third Steward evidence remains separately attributable; late voting does not retrospectively alter a determined majority.
- Acceptance of a decision is not authorisation of a subsequent host effect.
- Civilisation Clock and CRSTL describe transitions and provenance; an operational emergency must not wait for a Clock tick.

## Cross-owner transition boundary

A local SQLite transaction in Stage 112 cannot guarantee atomicity across a separate authority owner, revocation service, custody owner, host execution system, or a distributed state machine.

A production owner integration needs:
1. An authoritative context-state owner with a revision, provenance and explicitly identified scope.
2. A bounded acceptance operation with a current owner-issued proof or owner-local decision that binds the decision ID, Steward positions, permitted timing, rights/necessity/proportionality and the state revision.
3. A state-consuming commit with replay protection **across different request IDs**, not just idempotency for the same request ID.
4. An auditable acceptance receipt and an independent later execution gate.
5. A conservative response when authority owner state is unavailable, stale, contested, revoked, or cannot be reconciled. Emergency operation must use an already legitimate, bounded emergency route, never a fabricated default permission.
6. Explicit handling of uncertain commit outcome: reconcile before attempting another consequential transition.
7. Non-blocking asynchronous CRSTL / State Map updates, including causal and uncertainty markers, without treating the Clock as a global timestamp authority.

## Adversarial validation matrix (not yet executed end-to-end)

| Scenario | Expected principle |
| --- | --- |
| Owner revokes before acceptance | Reject early acceptance |
| Owner revision changes between preflight and commit | Reject or revalidate against new revision |
| Owner changes while local acceptance transaction is open | Do not assume SQLite protects a remote owner |
| Owner service unreachable | Fail closed or use a separately justified bounded emergency route |
| Duplicate decision with a different event/request ID | No second authority exercise |
| Commit acknowledged after network timeout | Reconcile outcome before retrying |
| Paused Civilisation Clock | Local legitimate emergency response remains possible |
| Third ballot arrives after contextual early acceptance | Preserve independent evidence without outcome reversal |
| Accepted result followed by host action | Fresh host-side authority required |
| Cross-scale GTP coordination | Spatial mesh coordination does not mint hierarchical authority |

## Evidence and limitations

Stage 108 CI passed 16 tests; Stage 109 15; Stage 110 16; Stage 111 19. Stage 112 first run failed one guard-order test; a corrected commit triggered a new run. Do not claim 112 verified until the corrected run succeeds.

The owner attestation in Stage 111 and Stage 112 is externally asserted fixture data. The local owner-state table in Stage 112 is not a real cross-domain authority source. Graduation requires actual source-owned integration and negative tests, not additional simulated booleans alone.

## Immediate next implementation candidate

A Stage 114 adversarial **cross-owner state-machine simulator** should model independent owner revocation, uncertain acknowledgements and paused Clock without pretending to provide distributed atomicity. Before production integration, identify the exact Governance owner-state and emergency state-machine documents from V1.2/V1.2a and current V1.3 by full path, reconcile any migration omissions, and retain their provenance.
