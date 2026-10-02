#!/usr/bin/env python3
"""CTP structural + semantic validation harness.

Run from a checkout of ACBlainney/Concord-1.3 (repository root):
    python "02_Domains/03_Research/Active_Development/Participation_and_Intelligence/ctp_validate_001.py"

Requires:
    jsonschema >= 4 with Draft202012Validator support.

This harness deliberately keeps structural JSON Schema results separate from
Concord deterministic semantic conformance results.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent
SCHEMA_PATH = ROOT / "Concord Contextual Trust Progression — JSON Schema 001.json"
FIXTURE_DIR = ROOT / "CTP_Schema_001_Fixtures"
RESULT_PATH = FIXTURE_DIR / "CTP Combined Executable Validation Results 001.json"

EXPECTED = {
1: True, 2: True, 3: False, 4: False, 5: False, 6: False, 7: False,
8: False, 9: False, 10: False, 11: True, 12: True, 13: False, 14: True,
}

def semantic_errors(x):
    e=[]; r=x["record"]
    if x["recordType"]=="ERR":
        if r.get("projectionState")=="PROJECTED" and (not r.get("sourceProviderRef") or not r.get("evidenceProjectedAt")): e.append("V-ERR-01")
        if r.get("correctionState") in ("CORRECTED","PARTIALLY_CORRECTED") and not r.get("correctionRef"): e.append("V-ERR-02")
        if r.get("correctionState")=="SUPERSEDED" and not r.get("supersedesRef"): e.append("V-ERR-03")
        if r.get("disputeState") in ("OPEN","RESOLVED") and not r.get("disputeRef"): e.append("V-ERR-04")
        if r.get("evidenceType")=="NON_EVENT_OBSERVATION" and r.get("observationCoverage")=="NOT_APPLICABLE": e.append("V-ERR-05")
        if r.get("reviewState")=="REQUIRED" and not r.get("reviewOrExpiry"): e.append("V-ERR-06")
    else:
        ps=["resourcePrerequisite","selfStewardshipPrerequisite","authorityPrerequisite","compositionPrerequisite","contestabilityPrerequisite"]
        ds=[d.get("disposition") for d in r.get("dimensionTransitions",[])]
        approved=lambda d: d in ("APPROVED","APPROVED_WITH_CONTROLS")
        if r.get("decisionState")=="PARTIALLY_APPROVED_BOUNDED" and (not any(map(approved,ds)) or not any(not approved(d) for d in ds)): e.append("V-ETR-02")
        if r.get("decisionState")=="APPROVED_WITH_ADDITIONAL_CONTROLS" and not r.get("addedControls"): e.append("V-ETR-03")
        if any(d.get("disposition")=="APPROVED_WITH_CONTROLS" and not d.get("addedControls") and not r.get("addedControls") for d in r.get("dimensionTransitions",[])): e.append("V-ETR-04")
        for p in ps:
            q=r.get(p,{})
            if q.get("applicability")=="NOT_REQUIRED_FOR_FUNCTION" and q.get("state")!="NOT_APPLICABLE": e.append("V-ETR-05")
            if q.get("applicability")=="REQUIRED" and q.get("state")=="NOT_APPLICABLE": e.append("V-ETR-06")
        if r.get("decisionState") in ("APPROVED_BOUNDED","APPROVED_WITH_ADDITIONAL_CONTROLS") and any(r.get(p,{}).get("applicability")=="REQUIRED" and r.get(p,{}).get("state") in ("UNKNOWN","NOT_SATISFIED","DISPUTED") for p in ps): e.append("V-ETR-07")
        if r.get("reviewState")=="REQUIRED" and (not r.get("reviewTime") or not r.get("reviewFailureDisposition") or r.get("reviewFailureDisposition")=="NOT_APPLICABLE"): e.append("V-ETR-10")
        if r.get("reviewState")=="NOT_REQUIRED" and r.get("reviewFailureDisposition") and r.get("reviewFailureDisposition")!="NOT_APPLICABLE": e.append("V-ETR-11")
        if r.get("decisionState")=="ENDED" and not r.get("endReason"): e.append("V-ETR-12")
        if r.get("decisionState")=="PARTIALLY_APPROVED_BOUNDED" and len(set(ds))<2: e.append("V-ETR-16")
    return sorted(set(e))

def main():
    schema=json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    validator=Draft202012Validator(schema)
    files=sorted(FIXTURE_DIR.glob("CTP Fixture *.json"))
    rows=[]
    for i,p in enumerate(files,1):
        x=json.loads(p.read_text(encoding="utf-8"))
        structural=[{"path":"/".join(map(str,z.absolute_path)),"message":z.message} for z in sorted(validator.iter_errors(x),key=lambda z:list(z.absolute_path))]
        semantic=semantic_errors(x)
        sem_pass=not semantic
        rows.append({
            "fixture":i,"file":p.name,"expected_semantic_pass":EXPECTED.get(i),
            "structural_pass":not structural,"structural_errors":structural,
            "semantic_pass":sem_pass,"semantic_errors":semantic,
            "semantic_expectation_matched":sem_pass==EXPECTED.get(i),
        })
    result={
        "schema_draft":"2020-12",
        "engine":"python-jsonschema Draft202012Validator",
        "schema_file":SCHEMA_PATH.name,
        "fixture_count":len(rows),
        "all_structurally_valid":all(r["structural_pass"] for r in rows),
        "semantic_expected_matched":sum(r["semantic_expectation_matched"] for r in rows),
        "all_semantic_expected_matched":all(r["semantic_expectation_matched"] for r in rows),
        "results":rows,
    }
    RESULT_PATH.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2))
    return 0 if result["all_semantic_expected_matched"] else 1

if __name__=="__main__":
    sys.exit(main())
