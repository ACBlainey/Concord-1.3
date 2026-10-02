# CBPR — PMEDG Candidate and Extraction Audit 001

**Date:** 2 October 2026
**Status:** PMEDG CANDIDATE / NOT GRADUATED / NOT CANONICAL

## Candidate

**Candidate name:** Concord Bounded Participant Runtime (CBPR)

**Candidate class:** Portable bounded-execution and scheduled-activation architecture.

**Problem addressed:** How a participant-associated process may receive bounded compute, activation, storage/tool/network access and credential invocation while preventing technical capability, persistence, infrastructure possession or partial permissions from silently becoming external-action or civil authority.

## Extraction Audit

### Portable core

The candidate portable core consists of:
- capability / permission / authority separation;
- explicit runtime state and integrity state;
- bounded resources;
- scoped storage, tool and network permissions;
- bounded credential bindings;
- action grants;
- output-interface consequence classification;
- proposal / revalidation / commit separation;
- commit-state uncertainty and retry safety;
- checkpoint/recovery without authority restoration;
- participant/operator controls;
- composition evaluation;
- temporal evidence;
- protected provenance;
- succession/service-registry interfaces.

### Concord-specific dependencies

CBPR interoperates with, but should not absorb:
- Contextual Wrapper Architecture;
- Bounded Contextual Authority;
- CIBB;
- VER;
- CMSS;
- BSR;
- BSuR;
- Civil Contact;
- constitutional/participation status architecture.

A portable module may describe these as external interfaces or generic equivalents rather than requiring a Concord deployment.

### Non-portable implementation choices

Not part of the portable core:
- specific OS/container/hypervisor;
- cloud provider;
- programming language;
- cryptographic suite;
- scheduler product;
- specific key store;
- specific network stack;
- exact quota values;
- jurisdiction-specific legal rules.

### Extraction risks

1. Converting Concord authority terms into generic access-control terminology and losing legitimate-authority distinction.
2. Treating output as harmless because the final actuator is downstream.
3. Omitting composition evaluation.
4. Treating a valid schema as execution permission.
5. Treating recovered runtime state as recovered authority.
6. Treating credentials as authority merely because they are technically usable.
7. Treating operator technical control as legitimate general authority.
8. Treating runtime persistence as personhood.
9. Folding secure key custody into runtime hosting.
10. Folding protected storage/CMSS into runtime entitlement.

## Candidate invariants requiring transfer preservation

- CAP != PERM != AUTH.
- Runtime Access != Authority.
- Execution Capability != Permission For External Action.
- Credential Availability != Permission To Use Credential.
- Network Reachability != Permission To Contact/Act On Destination.
- Prepared Action != Committed Action.
- Authority At Proposal != Authority At Commit.
- Unknown Commit State != Permission To Retry Blindly.
- Output Content != Output Channel Consequence.
- Authorised Parts != Authorised Composition.
- READ(A) + SEND(B) != automatically authorised transfer A→B.
- Recovered State != Recovered Authority.
- Technical Control Precedence != Legitimate Authority Precedence.
- Schema Validity != Execution Authority.
- Function Continuity != Authority Continuity.

## Evidence state

Architectural discovery: closed for current evidence.
Formal Model 002: stable.
Schema 002: stable for current formal scope.
Internal regression/composition tests: passed.
Schema002 structural/semantic fixture expectations: passed.
Independent blind transfer test: NOT YET RUN.

## PMEDG disposition

**Candidate suitable for frozen independent transfer testing.**

**Graduation:** NOT YET PERMITTED.

A clean evaluator should receive only the frozen candidate material and test brief, without development conclusions or prior Concord context.
