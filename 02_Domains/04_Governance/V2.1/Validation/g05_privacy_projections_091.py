"""Privacy-safe G05 public projection, deliberately no protected identifiers."""
def public_duty_projection(duty_id,continuity,orphans,succession):
    duty=continuity.duties.get(duty_id)
    orphan=orphans.records.get(duty_id)
    custody=succession.records.get(duty_id)
    if not duty and not orphan and not custody:
        return {"found":False,"review_required":False}
    return {"found":True,
            "obligation_open":bool(duty and duty.state=="OPEN"),
            "orphan_referral_pending":bool(orphan),
            "custody_projection_present":bool(custody),
            "review_required":not (duty and custody) or bool(orphan),
            "authority_granted":False}
def privileged_duty_projection(duty_id,continuity,orphans,access_verified=False):
    if not access_verified:return {"access_denied":True}
    duty=continuity.duties.get(duty_id)
    orphan=orphans.records.get(duty_id)
    return {"access_denied":False,
            "beneficiary_ref":duty.beneficiary_ref if duty else
                (orphan.protected_beneficiary_ref if orphan else None)}
