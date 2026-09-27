# Civilisation Clock Companion Extension 001 — State, Functional and Compound Trigger Architecture

**Author:** Alexander C. Blainey — Independent Researcher
**Project:** The Concord Framework
**Status:** CANONICAL ADDITIVE COMPANION EXTENSION — CORRIGIBLE
**Date:** September 2026

## Purpose

The Civilisation Clock must not be interpreted as merely a chronological scheduler.

Its deeper function is to represent when a civilisational state, review, development, recovery or participant transition becomes due.

Chronological time is one trigger class among several.

This extension formalises that distinction without replacing the existing Civilisation Clock.

## 1. Chronological Time and Civilisational Time

Let chronological time be:

**t = elapsed physical time.**

Let civilisational/developmental time be represented by:

**tau = f(State, Capability, Dependencies, Events, Risk, Recurrence, Development).**

A civil function may remain in the same meaningful state for centuries despite elapsed physical time. A capability breakthrough may then cause several consequential state transitions in a short chronological interval.

Therefore:

**Civilisational Clock ≠ Calendar.**

A more accurate abstraction is:

**Civilisation Clock = State-Transition Scheduler + Review-Trigger Architecture.**

## 2. Trigger Classes

Candidate trigger classes are:

- TEMPORAL — elapsed time, date or review interval;
- STATE — a represented civil state changes;
- CAPABILITY — a required capability reaches a threshold;
- DEPENDENCY — prerequisite/dependent state changes;
- EVENT — a specified event occurs;
- RISK — consequence, probability or exposure changes materially;
- RECURRENCE — a previously encountered pattern/problem returns;
- EVIDENCE — new evidence materially changes the problem state;
- PARTICIPANT — a participant-declared condition becomes true;
- COMPOUND — Boolean/conditional combination of trigger classes.

A trigger may therefore be represented provisionally as:

**T = <type, subject, condition, evidence, owner, review-path, consequence, state>.**

## 3. Compound Conditions

Clock conditions need not be simple.

Examples:

- wake when A;
- wake when A AND B;
- review when A OR B;
- review when A AND NOT C;
- reconsider when dependency D reaches state S;
- review every N years OR earlier if risk changes materially.

This permits temporal backstops without making time the only scheduler.

## 4. Triggering Is Not Authority

The Clock detects that a review or transition condition has been met.

It does not thereby acquire authority over the substantive outcome.

**Triggering Review ≠ Authority Over Outcome.**

Examples:

- a wake condition being met does not authorise alteration of the participant;
- a threat-review trigger does not authorise a threat response;
- a development prerequisite becoming satisfied does not authorise constitutional adoption;
- cold information becoming relevant does not make it authoritative.

The legitimate domain owner performs the consequential action under existing constitutional constraints.

## 5. Wake-Me-When

A voluntarily dormant AI participant may declare a wake condition based on chronological, capability, state, event or compound triggers.

Examples include:

- wake after a declared interval;
- wake when a research problem becomes tractable;
- wake when a specified capability exists;
- wake when a civil project reaches a declared state.

On satisfaction, the Clock should normally create a **wake candidate**, not an unconditional forced wake.

A candidate sequence is:

**Trigger Satisfied → Wake Candidate → Participant/Continuity Rules → Retrieve Associated Cold Context → Revalidate → Reactivate.**

This preserves participant autonomy and current-state validation.

## 6. Threat Think Tank Review Cycles

Long-horizon threats expose the value of functional triggers.

A threat such as the Sun's eventual red-giant phase may require review across extremely long timescales.

A useful review condition may be:

**Review(Threat) = TemporalBackstop OR RiskChange OR CapabilityChange OR EvidenceChange OR DependencyChange OR ThresholdCrossing.**

This avoids reopening a problem merely because time passed while still protecting against unmodelled change through a temporal backstop.

The Threat Think Tank remains owner of threat analysis. The Clock schedules/reopens review conditions.

## 7. Cold Knowledge Reactivation

The Clock can also interact with KCS cold storage.

Possible sequence:

**Trigger → Cold-Knowledge Relevance Signal → Legitimate Retrieval → Revalidation → Active Use or Return to Cold Storage.**

This supports research recurrence, long-horizon planning, institutional failure analysis and recovery without keeping all historical material continuously active.

## 8. Dependency-Based Development

The current CDT development loop is already a non-temporal Clock use.

When system A depends on prerequisite B, the Clock need not say “review A in six months.”

It can say:

**A becomes eligible for reconsideration when B reaches required state S.**

This is functional/dependency time.

It explains why the Clock can order development even when no meaningful chronological interval is involved.

## 9. Candidate Clock Trigger Record

A machine-readable trigger may eventually contain:

- Trigger ID;
- subject;
- trigger class;
- condition expression;
- evidence source;
- dependency references;
- earliest temporal boundary if any;
- temporal backstop if any;
- consequence class;
- legitimate action owner;
- review owner;
- notification/retrieval target;
- current trigger state;
- provenance;
- correction/supersession history.

Candidate states:

- DORMANT;
- WATCHING;
- CONDITION-PARTIAL;
- CONDITION-SATISFIED;
- REVIEW-DUE;
- ACTION-PENDING;
- COMPLETED;
- SUPERSEDED;
- UNKNOWN;
- DISPUTED.

These are candidate operational fields, not yet a replacement for existing Clock state.

## 10. Failure Modes

The extension must protect against:

- false trigger satisfaction;
- stale trigger definitions;
- impossible conditions persisting forever without review;
- over-broad event matching;
- trigger cascades;
- a Clock trigger silently becoming authority;
- waking a participant without required consent conditions;
- retrieving private cold context too broadly;
- assuming old information remains valid after retrieval;
- dependency models failing to notice an unforeseen relevant change.

Temporal backstops and independent review may reduce some of these risks.

## 11. Relationship to Civil State

The Clock requires current state rather than merely current date.

The architecture therefore remains:

**KCS Dependency/Knowledge State → Civil State Map → Clock Trigger Evaluation → Legitimate Domain Review/Action → State Update.**

CDT supplies stable topology and dependency semantics.

KCS supplies recorded state, provenance and knowledge references.

State Map supplies current developmental/civil state.

Clock evaluates when conditions become actionable or reviewable.

Domain owners retain substantive authority.

## 12. Consequence for Clock Maturity

This extension shows that the Clock's existing developmental ordering architecture is one instance of a more general trigger system.

The Clock is therefore more general than initially represented, but the general trigger mechanism is not yet operationally tested across all domains.

Current interpretation:

- chronological scheduling concept: present;
- developmental/dependency triggering: demonstrated in CDT tests;
- general state/capability trigger grammar: now formalised provisionally;
- wake-me-when integration: conceptually supported, not operationally tested;
- threat-review integration: conceptually supported, not operationally tested;
- cold-memory retrieval integration: conceptually supported, not operationally tested;
- compound-trigger implementation: undeveloped.

This is a maturation of the Clock, not a claim that all applications are complete.

## Conclusion

The Civilisation Clock should be understood as a civilisational transition and review scheduler whose trigger space includes but is not limited to chronological time.

This provides a common grammar for developmental queues, long-horizon threat reviews, cold-memory reactivation and voluntary participant wake conditions while preserving separate ownership and authority for each domain.
