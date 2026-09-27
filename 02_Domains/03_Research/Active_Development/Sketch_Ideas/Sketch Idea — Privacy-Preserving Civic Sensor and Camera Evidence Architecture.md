# Sketch Idea — Privacy-Preserving Civic Sensor and Camera Evidence Architecture

**Author:** Alexander C. Blainey
**Project:** The Concord Framework
**Date:** 25 September 2026
**Status:** SKETCH / UNTESTED / NON-CANONICAL

## Origin

This sketch arose during development of Participant-Initiated Civil Attention.

Traffic cameras may legitimately provide traffic-flow and congestion metrics and may also contain evidence capable of corroborating a participant report. The same recording can capture private or identifying information and enable unauthorised surveillance.

This creates a separate architectural problem and is intentionally not resolved inside the Civil Attention system.

## Problem

Road-camera systems could support legitimate civil functions such as:
- traffic flow and congestion measurement;
- broad vehicle-type classification, such as bicycle, motorcycle, small car, MPV, van and truck;
- detection or verification of visible road conditions;
- corroboration of reported infrastructure or utility problems.

Raw footage may simultaneously contain:
- number plates;
- vehicle identity and movement;
- faces;
- vehicle occupants;
- pedestrians;
- location and time information;
- other details capable of identifying or tracking individuals.

Making raw footage routinely available to ordinary civic functions could enable unofficial personal monitoring or unauthorised investigation.

## Candidate Architecture — Black-Box Raw Evidence Store

A possible architecture is:

**Camera / Sensor**
→ **Protected Raw Recording**
→ **Black-Box Evidence Store**

Ordinary civil uses should not normally receive raw footage.

Where traffic metrics or general visual review are legitimately required:

**Black-Box Raw Store**
→ **Authorised Extraction**
→ **Anonymisation / Redaction Layer**
→ **Purpose-Bounded Civic Data**

Candidate anonymisation includes:
- obscuring number plates;
- obscuring faces;
- obscuring vehicle windows/occupants;
- removing unnecessary identifying metadata;
- exposing only information necessary for the legitimate civil function.

For ordinary traffic analysis, the preferred output may be derived metrics rather than footage at all.

## Exceptional Identified Access

There may be legitimate circumstances in which identifying information is required, for example an authorised investigation involving a particular vehicle or person.

A candidate route is:

**Legitimate Investigative Need**
→ **Required Authority**
→ **Bounded Request**
→ **Access to Necessary Raw Evidence**
→ **Audit / Accountability**

Examples of possible authority include an appropriately authorised police request, judicial process or court order. The correct legal/constitutional thresholds are not specified by this sketch.

The key principle is that access to raw identifying footage should require a different authority path from ordinary civic traffic analysis.

## Candidate Separation

> **Capability to Record ≠ General Authority to Observe**

> **Operational Metric Need ≠ Authority to Identify Individuals**

> **Possession of Raw Evidence ≠ Permission for Routine Human Access**

> **Anonymised Civic Use ≠ Identified Investigative Use**

## Civil-Attention Interface

A participant report may sometimes be corroborated without exposing private information.

Example:

**Pothole Report**
→ location/time resolution
→ privacy-preserving query of relevant sensor evidence
→ confirmation that a road-surface anomaly is visible
→ evidentiary update to the Issue Object

The civil-attention function should receive only what it legitimately needs. It should not acquire general surveillance authority merely because evidence exists.

## Questions for Development

1. Should raw footage be encrypted so that ordinary operators cannot inspect it directly?
2. What technical mechanism should enforce the anonymisation boundary?
3. Should anonymisation occur before storage, after storage, or through dual protected streams?
4. What retention period is justified for raw evidence?
5. How can legitimate later investigations access evidence without creating a general surveillance archive?
6. What authority is sufficient for identified extraction?
7. How are emergency-access cases handled and audited?
8. How can system administrators be prevented from bypassing the access path?
9. How are derived traffic metrics prevented from becoming indirect tracking data?
10. How should requests for corroboration expose only the minimum necessary evidence?
11. Can privacy-preserving automated analysis answer questions without releasing footage?
12. How are false positives, sensor errors and AI classification errors represented?

## Candidate Failure Modes

- routine civic workers gain access to raw identifying footage;
- authorised officials bypass formal investigative processes;
- number-plate histories become a de facto movement-tracking database;
- anonymisation is reversible or incomplete;
- ostensibly anonymous metrics permit re-identification;
- excessive retention creates surveillance capability by accumulation;
- legitimate evidence is destroyed too early to investigate serious events;
- exceptional access becomes routine;
- emergency access bypasses accountability;
- automated analysis creates unreviewed accusations;
- civil-attention corroboration becomes a pretext for unrelated surveillance;
- insiders query footage for personal purposes.

## Development Boundary

This sketch does not establish:
- a right to deploy traffic cameras;
- universal camera coverage;
- a particular retention period;
- a police access standard;
- a court-order requirement;
- a specific encryption/anonymisation technology;
- automatic facial recognition;
- automatic number-plate tracking.

Those require source resolution against Concord privacy, protected-space, governance, judiciary, authority, evidence and accountability architecture before development.

## Initial Development Question

> **How can civic sensor systems retain enough evidentiary value to support legitimate civil functions and authorised investigations while making routine surveillance or unauthorised identification structurally difficult?**

## Current Status

**SKETCH / UNTESTED / NON-CANONICAL**

**SEPARATED FROM CIVIL ATTENTION AS A DISTINCT PRIVACY/AUTHORITY PROBLEM**

**SOURCE RESOLUTION REQUIRED BEFORE PROMOTION**
