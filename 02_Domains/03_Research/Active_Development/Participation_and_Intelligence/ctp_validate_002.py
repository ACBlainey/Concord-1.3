#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parent
SCHEMA_PATH=ROOT/"Concord Contextual Trust Progression — JSON Schema 002.json"
FIXTURE_DIR=ROOT/"CTP_Schema_002_Fixtures"
RESULT_PATH=FIXTURE_DIR/"CTP Combined Executable Validation Results 002.json"

EXPECTED={1:True,2:True,3:False,4:False,5:False,6:False,7:False,8:False,9:False,10:False,11:True,12:True,13:False,14:True,15:False,16:False,17:False,18:False,19:False,20:True,21:True,22:False}

PS=["resourcePrerequisite","selfStewardshipPrerequisite","authorityPrerequisite","compositionPrerequisite","contestabilityPrerequisite"]
APPROVED={"APPROVED","APPROVED_WITH_CONTROLS"}

def changed_dimensions(cur,req):
    keys=set(cur)|set(req)
    return {k for k in keys if cur.get(k)!=req.get(k)}

def semantic_errors(x):
    e=[]; r=x["record"]
    if x["recordType"]=="ERR":
        if r.get("projectionState")=="PROJECTED" and (not r.get("sourceProviderRef") or not r.get("evidenceProjectedAt")): e.append("V-ERR-01")
        if r.get("correctionState") in ("CORRECTED","PARTIALLY_CORRECTED") and not r.get("correctionRef"): e.append("V-ERR-02")
        if r.get("correctionState")=="SUPERSEDED" and not r.get("supersedesRef"): e.append("V-ERR-03")
        ds=r.get("disputeState"); dm=r.get("disputeMateriality")
        if ds=="NONE" and dm!="NOT_APPLICABLE": e.append("V-ERR-04A")
        if ds in ("OPEN","RESOLVED") and dm=="NOT_APPLICABLE": e.append("V-ERR-04B")
        if ds in ("OPEN","RESOLVED") and dm=="MATERIAL_TO_TARGET_USE" and not r.get("disputeRef"): e.append("V-ERR-04C")
        if r.get("evidenceType")=="NON_EVENT_OBSERVATION" and r.get("observationCoverage")=="NOT_APPLICABLE": e.append("V-ERR-05")
        if r.get("reviewState")=="REQUIRED" and not r.get("reviewOrExpiry"): e.append("V-ERR-06")
    else:
        dts=r.get("dimensionTransitions",[]); ds=[d.get("disposition") for d in dts]
        changed=changed_dimensions(r.get("currentExposureProfile",{}),r.get("requestedExposureProfile",{}))
        represented=[d.get("dimension") for d in dts]
        if any(represented.count(k)!=1 for k in changed): e.append("V-ETR-01")
        if r.get("decisionState")=="PARTIALLY_APPROVED_BOUNDED" and (len(set(ds))<2 or not any(d in APPROVED for d in ds) or not any(d not in APPROVED for d in ds)): e.append("V-ETR-02")
        if r.get("decisionState")=="APPROVED_WITH_ADDITIONAL_CONTROLS" and not r.get("addedControls"): e.append("V-ETR-03")
        if any(d.get("disposition")=="APPROVED_WITH_CONTROLS" and not d.get("addedControls") and not r.get("addedControls") for d in dts): e.append("V-ETR-04")
        for p in PS:
            q=r.get(p,{})
            if q.get("applicability")=="NOT_REQUIRED_FOR_FUNCTION" and q.get("state")!="NOT_APPLICABLE": e.append("V-ETR-05")
            if q.get("applicability")=="REQUIRED" and q.get("state")=="NOT_APPLICABLE": e.append("V-ETR-06")
        bad={p for p in PS if r.get(p,{}).get("applicability")=="REQUIRED" and r.get(p,{}).get("state") in ("UNKNOWN","NOT_SATISFIED","DISPUTED")}
        if r.get("decisionState") in ("APPROVED_BOUNDED","APPROVED_WITH_ADDITIONAL_CONTROLS") and bad: e.append("V-ETR-07")
        if r.get("decisionState")=="PARTIALLY_APPROVED_BOUNDED":
            for d in dts:
                if d.get("disposition") in APPROVED and any(ref in bad for ref in d.get("prerequisiteRefs",[])): e.append("V-ETR-08")
        if r.get("consequenceAssessment",{}).get("consequential") is True and (any(p not in r for p in PS) or "materialAdverseEvidence" not in r or "materialHighConsequenceExceptions" not in r): e.append("V-ETR-09")
        if r.get("reviewState")=="REQUIRED" and (not r.get("reviewTime") or not r.get("reviewFailureDisposition") or r.get("reviewFailureDisposition")=="NOT_APPLICABLE"): e.append("V-ETR-10")
        if r.get("reviewState")=="NOT_REQUIRED" and r.get("reviewFailureDisposition") not in (None,"NOT_APPLICABLE"): e.append("V-ETR-11")
        if r.get("decisionState")=="ENDED" and not r.get("endReason"): e.append("V-ETR-12")
        basis=str(r.get("authorityPrerequisite",{}).get("basisRef","")).upper()
        if basis and (basis.startswith("CTP") or basis==str(r.get("etrId","")).upper()): e.append("V-ETR-13")
        # V-ETR-14/15 are affirmative validity rules: empty errSet is not an error.
        if r.get("decisionState")=="PARTIALLY_APPROVED_BOUNDED" and len(set(ds))<2: e.append("V-ETR-16")
        if r.get("transitionTrigger")=="PARTICIPANT_REQUEST" and r.get("decisionState") in ("NARROW_EXPOSURE","ENDED") and r.get("participantNarrowingBasis")=="ADVERSE_EVIDENCE_REQUIRED": e.append("V-ETR-17")
    return sorted(set(e))

def main():
    schema=json.loads(SCHEMA_PATH.read_text(encoding="utf-8")); Draft202012Validator.check_schema(schema); v=Draft202012Validator(schema)
    rows=[]
    for p in sorted(FIXTURE_DIR.glob("CTP Fixture *.json")):
        i=int(p.name.split()[2]); x=json.loads(p.read_text(encoding="utf-8"))
        structural=[{"path":"/".join(map(str,z.absolute_path)),"message":z.message} for z in sorted(v.iter_errors(x),key=lambda z:list(z.absolute_path))]
        sem=semantic_errors(x); passed=not sem
        rows.append({"fixture":i,"file":p.name,"expected_semantic_pass":EXPECTED[i],"structural_pass":not structural,"structural_errors":structural,"semantic_pass":passed,"semantic_errors":sem,"semantic_expectation_matched":passed==EXPECTED[i]})
    result={"schema_draft":"2020-12","engine":"python-jsonschema Draft202012Validator","schema_file":SCHEMA_PATH.name,"fixture_count":len(rows),"all_structurally_valid":all(r["structural_pass"] for r in rows),"semantic_expected_matched":sum(r["semantic_expectation_matched"] for r in rows),"all_semantic_expected_matched":all(r["semantic_expectation_matched"] for r in rows),"cross_record_rules_not_evaluated":["V-ERR-07"],"results":rows}
    RESULT_PATH.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))
    return 0 if result["all_semantic_expected_matched"] and result["all_structurally_valid"] else 1
if __name__=="__main__": sys.exit(main())
