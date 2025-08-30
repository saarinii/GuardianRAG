async def run(context):
    ev = context["evidence"]       # aggregated evidence list
    risk = 0.2 if "MFA" in str(ev) else 0.8
    context["risk_score"] = risk
    return risk
