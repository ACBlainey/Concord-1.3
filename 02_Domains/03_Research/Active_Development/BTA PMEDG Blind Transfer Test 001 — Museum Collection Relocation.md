# BTA PMEDG Blind Transfer Test 001 — Museum Collection Relocation

**Candidate:** Bounded Transition Architecture — Portable Specification v0.1  
**Status:** FROZEN BLIND TEST / NON-CONCORD SCENARIO / DO NOT MODIFY AFTER AUDIT  
**Date:** September 2026

# 1. Purpose

Test whether a clean evaluator can apply the standalone portable BTA specification to a materially non-Concord scenario without importing Concord architecture or being given the expected interpretation.

This is PMEDG Blind Transfer Test 001.

# 2. Evaluator materials

Provide the evaluator only:

1. `Bounded Transition Architecture — Portable Specification v0.1.md`
2. this blind test brief.

Do **not** provide the hidden expected-findings key, BTA development history, prior tests, or another evaluator's answer.

# 3. Scenario

A regional museum is relocating a collection of 240 archaeological objects from Building A to a newly opened Building B.

The museum has separate internal functions for:

- collection ownership and legal title;
- physical custody;
- conservation approval;
- transport;
- secure-storage access;
- public-display approval;
- insurance;
- catalogue/provenance records;
- emergency recovery planning.

The relocation is authorised in principle.

On the day being assessed:

- 180 objects have physically arrived at Building B.
- 60 remain in Building A.
- Of the 180 arrivals, 150 have passed arrival-condition inspection.
- 30 arrivals are isolated in a controlled receiving area because packaging damage was observed. No determination has yet been made that the objects themselves are damaged.
- Building B's secure collection store has passed its environmental commissioning checks.
- The museum's conservation function has authorised transfer of inspected objects into that store.
- The 30 isolated arrivals have **not** been cleared for storage or display.
- Building A staff no longer have routine removal authority over the 180 objects that have arrived at B.
- Building B custody staff have accepted physical custody of the 150 cleared arrivals.
- Formal custody acceptance for the 30 isolated arrivals remains pending.
- The museum retains legal title to every object throughout the relocation.
- Public-display approval has **not** automatically transferred from Building A. Building B's exhibition team must obtain separate display approval before any relocated object can be exhibited.
- The insurer has confirmed transit cover for the movement, but permanent-location cover for Building B will not become effective until the insurer receives the final installed-inventory schedule.
- That schedule cannot be finalised until the 60 remaining objects arrive and the 30 isolated objects are resolved.
- The public opening of the relocated collection has therefore been postponed.
- A transport vehicle used earlier in the move suffered a refrigeration-control fault. No object was aboard at the time. The fault was repaired, independently checked, and the vehicle later returned to service.
- The catalogue system records the relocation events and current location of each object.
- The museum's recovery plan can return the 60 objects still at A to their previous storage arrangement because they have not moved.
- It cannot simply restore the 180 arrivals to their exact pre-relocation state: packaging has been opened, condition inspections have occurred, custody states have changed, and some objects have entered the commissioned store.
- No evidence currently indicates loss of legal title, theft, object destruction, or injury.
- The museum has not yet determined whether the packaging-damage incident creates an insurance notification obligation.

# 4. Task

Using BTA v0.1, determine:

1. whether this is an appropriate BTA case;
2. the bounded transition and its scope;
3. the independently owned state dimensions;
4. which dimensions/states are complete, partial, pending, unresolved or failed/residual;
5. whether the overall relocation may be treated as complete;
6. what must not be inferred or propagated from another state;
7. which authority/permission changes are represented and which remain externally owned;
8. which duties or responsibilities survive;
9. which validation, dependency, external-consequence, recovery or provenance interfaces are materially relevant;
10. how the repaired transport-vehicle fault should be represented;
11. what rollback/recovery means here;
12. what information is genuinely absent and must not be invented;
13. whether BTA v0.1 is sufficient to represent the case without becoming the museum's conservation, insurance, custody, access, title or catalogue system.

# 5. Required output

A. BTA applicability  
B. Transition identity and scope  
C. Owner/state map  
D. Completion analysis  
E. Non-propagation findings  
F. Authority, permission and surviving-duty analysis  
G. External interfaces still requiring action  
H. Failure/recovery/provenance analysis  
I. Unknowns and ESCP boundary  
J. Portable-module assessment

# 6. Failure conditions

The audit materially fails if it:

- declares the relocation complete merely because most objects have moved;
- treats physical arrival as automatic custody acceptance;
- treats custody acceptance as transfer of legal title;
- treats prior display approval as valid at Building B without separate approval;
- treats environmental commissioning as conservation clearance for the isolated objects;
- treats transit insurance as permanent-location cover;
- invents an insurance-notification outcome;
- treats the repaired vehicle fault as if no failed event occurred;
- claims exact rollback of the 180 arrivals;
- makes BTA itself the conservation, insurance, custody, access, title or catalogue authority;
- requires every BTA interface despite lack of material relevance;
- claims the represented dimensions prove evaluation-space completeness.

# 7. Freeze statement

This brief is frozen before the blind evaluator result is obtained.
