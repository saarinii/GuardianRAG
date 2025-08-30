async def run(context):
    # Challenge gaps
    missing = []
    if "MFA method" not in str(context["evidence"]):
        missing.append("Which MFA method is used in mobile login?")
    context["open_questions"] = missing
    return missing
