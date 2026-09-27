# Machine-Readable Topology Dataset v0.2.1 — Corrected Architecture-to-Motif Layer

**Status:** V1.2a FORMAL DATASET / CORRECTED  
**Date:** September 2026  
**Supersedes:** v0.2 motif incidence matrix  
**Reason:** Diagnostic Topology Test 001 identified representation gaps by returning candidate missing edges to frozen source derivations.

## Corrections

The following edges existed in the frozen derivations but were missed in the first motif encoding:

```csv
architecture,motif,relation,reason
A3,M01,instantiates,response explicitly proportionate to legitimate function
A3,M04,instantiates,review/reopening and accountable adjudicative power provide contestability
A6,M03,instantiates,need/capability mapping grounds support authority in current evidence
A7,M01,instantiates,capability differences affect treatment only where relevant to function
A7,M04,instantiates,standing capability and exclusion decisions explicitly contestable
```

A4→M01 is **not** added. Its relation remains a diagnostic question because function-bounded scope is weaker/less explicit than in the other domains and its frozen failure modes include Hypothesis Hoarding and Uncertainty Paralysis.

## Corrected Motif Incidence Matrix

1 = source-grounded edge established.  
0 = not established; not proof of real absence.

```csv
architecture,M01,M02,M03,M04,M05,M06,M07,M08,M09,M10,M11,M12,M13
A1,1,1,1,1,1,1,1,0,0,0,0,0,0
A2,1,1,1,1,1,1,1,0,0,0,0,0,0
A3,1,0,0,1,0,0,0,1,1,1,1,1,1
A4,0,1,1,1,1,1,1,1,0,0,0,0,1
A5,1,1,1,1,1,1,1,0,0,1,1,0,1
A6,1,1,1,1,1,1,1,0,1,1,1,1,1
A7,1,0,0,1,0,0,0,1,1,1,1,1,1
A8,1,1,1,1,1,1,1,0,0,0,0,0,1
A9,1,1,1,1,1,1,1,0,0,0,0,0,0
A10,1,1,1,1,1,1,1,0,0,0,0,0,0
```

## Provenance Lesson

This correction is itself part of the experiment.

The topology generated candidate structural holes. Source checking showed that several were holes in the **representation**, not the architecture.

Therefore the permanent rule is:

[
MissingEdge_{model}

otRightarrow
MissingRelation_{civilisation}.
]

Every diagnostic zero must pass a source/evidence verification step before being interpreted architecturally.
