# 12 — Civil Attention

**Project:** The Concord
**Status:** CONCORD SYSTEM INTEGRATION / CORRIGIBLE
**Source Architecture:** Civil Attention, Reporting, Petition and Resolution Module v1.0
**Date:** 25 September 2026

## Purpose

Civil Attention is the Concord's common participant-facing mechanism for causing the civilisation to notice, preserve, route, examine and respond to possible problems, improvements and collective concerns.

Its participant-facing principle is:

> **Tell the Concord once; the Concord determines who needs to deal with it.**

A participant should not need to understand the Concord's internal institutional topology before raising a legitimate concern.

Civil Attention centralises intake, provenance, routing visibility, resolution status and feedback. It does **not** centralise substantive decision authority.

> **Central Visibility ≠ Central Control**

## Core Architecture

**Participant → Common Civil Attention Intake → Receipt / Original Submission Preservation → Provisional Classification → Issue Matching / Issue Object → Multi-Domain Resolution → Domain Action Object(s) → Domain-Specific Examination / Action → Domain Status / Disposition Return → Central Resolution Record → Participant Feedback / Reviewability**

## Participant Inputs

The first common input classes are:

- **Problem Reports** — a possible defect, harm, failure or undesirable condition;
- **Suggestions** — a possible improvement, solution or opportunity;
- **Petitions** — collective concern or requested action.

Each input type has its own subfolder, explanation and standard participant-facing pro forma.

Submission creates legitimate attention. It does not manufacture truth, priority, authority or outcome.

## Domain Processing

Civil Attention determines which Concord function or functions need to receive an Issue. The legitimate domain then examines and acts using its own authority and specialist methodology.

Each domain integration must append a **Civil Attention Domain Companion Methodology** to the graduated core rather than rewrite the core.

**Civil Attention Core Method v1.0 + Domain Companion + Bound Concord Services → Domain Implementation**

> **Domain Requirement ≠ Core Method Amendment**

> **Companion Extension ≠ Core Override**

> **Local Adaptation Must Preserve Core Invariants**

A domain-specific conflict with the core must be escalated for controlled core review rather than silently patched locally.

## Return Path

Every routed Domain Action Object requires a return path to Civil Attention.

The central system maintains enough bounded information to answer:

- what Issue exists;
- where it has been routed;
- who currently owns each required action;
- what the current response state is;
- what material action last occurred;
- what dependency or review condition exists;
- whether all necessary domain work has reached legitimate disposition;
- what can legitimately be communicated back to the participant.

> **Every Outbound Route Requires a Return Path.**

> **Domain Completion ≠ Issue Resolution.**

## Root Structure

- `01_Problem_Reports/` — participant problem-report interface and form.
- `02_Suggestions/` — participant suggestion interface and form.
- `03_Petitions/` — participant petition interface and form.
- `04_Central_Resolution_and_Feedback/` — common resolution record, return-path and feedback architecture.
- `05_Domain_Companion_Methodology/` — rules for binding the immutable portable core to individual Concord domains.
- `06_Domain_Interfaces/` — Concord-domain routing/return interfaces and companion specifications.

## Source of Truth

The authoritative portable method remains:

`06_Portable_Modules/Civil Attention Reporting Petition and Resolution Module v1.0.md`

This Concord system **uses** that core. It does not create a divergent local copy.

Future improvements that appear universal must follow the portable module's controlled revision/back-propagation process before the core changes.

## Scope Note

The separate internal/recursive Civil Attention application — workers, managers, departments, AI agents and workflow exception reporting — remains an Active Development candidate. It is not silently treated as validated merely because the Concord now adopts the public/participant-facing architecture.
