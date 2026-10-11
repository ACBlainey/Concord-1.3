"""Cumulative emergency control exposure: descriptive audit, not authority.

Windows are half-open [start,end); overlapping windows merge for exposure.
Thresholds are configurable review triggers, not constitutional law.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Intervention:
    mandate_ref: str
    subject_ref: str
    controller_ref: str
    start_tick: int
    end_tick: int

def exposure(records,subject_ref,controller_ref,window_start,window_end,
             review_threshold,consecutive_threshold):
    issues=[]
    if window_end<=window_start or review_threshold<0 or consecutive_threshold<0:
        return {"issues":["INVALID_CONFIGURATION"],"requires_independent_review":True,
                "authority_granted":False,"automatic_illegality":False}
    selected=[]
    seen=set()
    for item in records:
        if item.mandate_ref in seen:issues.append("DUPLICATE_MANDATE_REF")
        seen.add(item.mandate_ref)
        if item.end_tick<=item.start_tick:issues.append("INVALID_INTERVAL")
        if item.subject_ref==subject_ref and item.controller_ref==controller_ref:
            lo=max(window_start,item.start_tick);hi=min(window_end,item.end_tick)
            if hi>lo:selected.append((lo,hi))
    selected.sort()
    merged=[]
    for start,end in selected:
        if merged and start<=merged[-1][1]:
            merged[-1]=(merged[-1][0],max(end,merged[-1][1]))
        else:merged.append((start,end))
    total=sum(end-start for start,end in merged)
    longest=max((end-start for start,end in merged),default=0)
    flags=[]
    if total>=review_threshold:flags.append("CUMULATIVE_EXPOSURE_REVIEW")
    if longest>=consecutive_threshold:flags.append("CONTINUOUS_CONTROL_REVIEW")
    if issues:flags.append("RECORD_INTEGRITY_REVIEW")
    return {"issues":issues,"review_flags":flags,"total_exposure_ticks":total,
            "longest_continuous_ticks":longest,"merged_intervals":merged,
            "requires_independent_review":bool(flags),
            "authority_granted":False,"automatic_illegality":False}
