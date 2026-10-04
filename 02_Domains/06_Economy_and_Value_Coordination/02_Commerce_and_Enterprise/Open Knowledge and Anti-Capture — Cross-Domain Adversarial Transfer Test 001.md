# Open Knowledge and Anti-Capture — Cross-Domain Adversarial Transfer Test 001

**Project:** The Concord
**Date:** 4 October 2026
**Status:** DEVELOPMENT TEST / NON-CANONICAL
**Candidate:** Open Knowledge, Functional Qualification and Anti-Capture Commerce Architecture 001
**Source case:** Pharmaceuticals
**Test domains:** vehicle/equipment repair; software interoperability; energy equipment; food production; construction systems; communications infrastructure

## 1. Test question

Does the candidate preserve legitimate competition and civil resilience across unlike domains without erasing genuine safety, privacy, security, authorship, investment or resource constraints?

A transfer passes only if it can distinguish legitimate functional restriction from incumbent-controlled exclusion.

## 2. Vehicle and equipment repair

A manufacturer withholds diagnostic codes, interface specifications, service procedures and component-pairing information so only its authorised network can repair a product.

The candidate successfully separates ownership/use, diagnostic information, repair knowledge, technician competence, safety-critical calibration, replacement-part conformity, warranty/contract and IP.

Safety-critical repairs may require competence and output conformity without requiring manufacturer exclusivity.

> **Safety-Critical Repair != Manufacturer-Exclusive Repair**

Authentication keys, anti-theft secrets and security controls may justify bounded access. They do not justify withholding ordinary repair information.

**Result: PASS WITH BOUNDED SECURITY EXCEPTION**

## 3. Software interoperability

A dominant service uses a proprietary protocol and competitors cannot interoperate without reverse engineering.

The architecture supports access to the interface boundary needed for legitimate interoperability without requiring disclosure of user data, authentication secrets, unrelated source code or dangerous vulnerabilities.

> **Interface Knowledge != Source-Code Ownership**

A useful refinement follows:

> **Interoperability Requirement Should Target The Boundary Needed For Interaction, Not Automatically The Whole Implementation**

**Result: PASS**

## 4. Energy equipment

A supplier controls inverters/controllers used throughout an energy system, including maintenance software and replacement interfaces, then exits the market.

Civil dependency and continuity support durable access to maintenance specifications, interface standards, replacement requirements and safe operating constraints. High-voltage/grid work may still require specialist competence.

> **Essential-System Dependency Strengthens Continuity Need Without Removing Safety Requirements**

Operational credentials, live topology and security configuration may remain controlled.

**Result: PASS WITH SECURITY/INFRASTRUCTURE WRAPPER**

## 5. Food production — limiting case

A producer develops a popular food recipe/process and seeks to keep it private. Other producers can supply safe, nutritionally/microbiologically equivalent substitutes.

Food safety, allergen disclosure and contamination controls are legitimate. But the test does **not** establish that every privately developed non-essential recipe must be disclosed merely because competitors would benefit.

Where interoperability is unnecessary, civil dependency is low, substitutes exist, and no civil-funding condition required openness, private commercial knowledge may remain private.

> **Commercial Value Alone Does Not Create A Duty To Disclose; Exclusion Risk, Civil Dependency, Funding Basis, Interoperability And Functional Necessity Matter**

**Result: PARTIAL PASS / IMPORTANT LIMIT**

The candidate must not become a universal abolition of trade secrecy.

## 6. Construction systems

A proprietary building component requires manufacturer documentation for inspection, replacement or integration, while the building may outlive the supplier by decades.

Long-lived consequential products support durable access to structural/performance specifications, inspection requirements, safe installation/removal, interface dimensions/loads, maintenance and end-of-life handling.

> **Long-Lived Product Dependency Can Outlast The Producer**

Unrelated aesthetic or private design information need not become open where it is unnecessary for safety, maintenance, interoperability, replacement or continuity.

**Result: PASS**

## 7. Communications infrastructure

An infrastructure provider controls essential network interfaces and device approval.

The candidate separates spectrum/resource allocation, protocol/interface standards, device conformity, network security, service contract, market participation and incumbent preference.

Independent conformity testing can replace incumbent permission where it protects the same legitimate function.

> **Network Conformity != Incumbent Permission**

Security-sensitive operational material may remain controlled.

**Result: PASS WITH SECURITY EXCEPTION**

## 8. Strongly transferable kernel

Across all tests the following survive:

1. distinguish knowledge, competence, safety, authority, output conformity, commercial obligations and IP;
2. keep licences/approvals bounded to legitimate purpose;
3. do not substitute incumbent permission for independent functional qualification where independent qualification is feasible;
4. open entry does not waive safety/output conformity;
5. civilly funded knowledge may legitimately carry openness conditions;
6. high-dependency systems justify stronger continuity/interoperability scrutiny;
7. tax/debt enforcement should not masquerade as competence/safety enforcement;
8. required standards should not be unnecessarily proprietary;
9. enterprise failure should not automatically destroy essential civil capability;
10. restrictions require function-specific justification.

## 9. Important limits

The tests reject overbroad interpretations:
- not all commercially valuable knowledge must be public;
- not all source code must be open to require interoperability;
- security secrets need not be public to support repair;
- private recipes/processes do not automatically create a civil disclosure duty;
- essential-system openness does not imply public release of live security information;
- right to repair does not waive competence.

## 10. Three knowledge states

The candidate should distinguish:

### OPEN
Generally discoverable and usable information.

### BOUNDED-ACCESS
Information necessary for a legitimate function but carrying privacy, security or safety sensitivity. Eligible parties can access it under contextual controls.

### PRIVATE
Information for which no independent access duty exists and which may remain private.

> **Necessary Access != Necessarily Public Access**

This maps naturally to Contextual Wrapper Architecture and the Concord Information Black Box.

## 11. Dependency and substitutability

The strength of a legitimate access obligation should consider:
- civil dependency;
- substitutability;
- duration of dependency;
- consequence of failure;
- interoperability necessity;
- repair/maintenance necessity;
- public/civil funding;
- whether dependency can outlive the producer;
- availability of independent conformity testing;
- privacy/security risk.

> **Greater Dependency And Lower Substitutability -> Stronger Continuity And Access Obligation, Subject To Independent Safety/Security Constraints**

This is not an automatic single-score formula.

## 12. Innovation and investment

The test does not establish a universal reward mechanism for privately funded innovation.

It does establish that reward and functional access are separate questions.

> **Innovation Reward Question != Functional Access Question**

Possible rewards can be designed without assuming permanent exclusion from essential interoperability, repair or continuity is always necessary.

## 13. Gate topology

An apparent multi-gate system may still be captured if one incumbent writes the standard, owns the required information, controls testing and issues the licence.

> **Nominally Separate Gates != Independently Bounded Gates**

The topology of authority therefore matters as much as the labels.

## 14. Verdict

**TRANSFER RESULT: PASS WITH REFINEMENT**

The architecture is not pharmaceutical-specific, but the transferable kernel is narrower than universal open knowledge:

> **Open Where Legitimately Required; Bounded-Access Where Functionally Necessary But Sensitive; Private Where No Independent Access Duty Exists**

## 15. PMEDG status

**PMEDG CANDIDATE — DO NOT EXTRACT YET**

Before portable extraction:
- integrate the three-state knowledge model;
- integrate dependency/substitutability;
- integrate independent-gate topology;
- source-resolve the Law/IP interface;
- retain innovation/reward as a separate interface;
- run focused regression after revision.
