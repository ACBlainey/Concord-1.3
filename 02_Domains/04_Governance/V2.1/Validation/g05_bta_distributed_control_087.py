"""Cross-controller exposure audit: descriptive, not an authority aggregator.

Union exposure detects persistent restrictions across multiple controllers.
Simultaneous controller count is an independent review signal.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Restriction:
    mandate_ref: str
    subject_ref: str
    controller_ref: str
    start_tick: int
    end_tick: int
    restriction_kind: str

def audit(records,subject_ref,restriction_kind,window_start,window_end,
          union_threshold,concurrency_threshold):
    if window_end<=window_start or union_threshold<0 or concurrency_threshold<1:
        return {"issues":["INVALID_CONFIGURATION"],"review_required":True,
                "authority_granted":False,"automatic_illegality":False}
    intervals=[];issues=[];seen=set()
    for r in records:
        if r.mandate_ref in seen:issues.append("DUPLICATE_MANDATE")
        seen.add(r.mandate_ref)
        if r.end_tick<=r.start_tick:issues.append("INVALID_INTERVAL");continue
        if r.subject_ref!=subject_ref or r.restriction_kind!=restriction_kind:continue
        lo=max(window_start,r.start_tick);hi=min(window_end,r.end_tick)
        if lo<hi:intervals.append((lo,hi,r.controller_ref))
    points=sorted({v for a,b,_ in intervals for v in (a,b)})
    union=0;longest=0;run=0;maximum=0;contributors=set()
    for a,b in zip(points,points[1:]):
        active={c for lo,hi,c in intervals if lo<b and hi>a}
        if active:
            union+=b-a;run+=b-a;longest=max(longest,run)
            maximum=max(maximum,len(active));contributors.update(active)
        else:run=0
    flags=[]
    if union>=union_threshold:flags.append("DISTRIBUTED_EXPOSURE_REVIEW")
    if maximum>=concurrency_threshold:flags.append("CONCURRENT_CONTROLLERS_REVIEW")
    if issues:flags.append("RECORD_INTEGRITY_REVIEW")
    return {"issues":issues,"review_flags":flags,"review_required":bool(flags),
            "union_exposure_ticks":union,"longest_continuous_ticks":longest,
            "maximum_concurrent_controllers":maximum,
            "contributing_controller_refs":sorted(contributors),
            "authority_granted":False,"automatic_illegality":False}
