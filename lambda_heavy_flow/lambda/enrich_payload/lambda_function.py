def lambda_handler(event, context):
    transformed = event.get("transformed", {})

    enriched = {
        "segment": "premium" if transformed.get("amount", 0) > 1000 else "standard",
        "emailDomain": transformed.get("email", "").split("@")[-1] if "@" in transformed.get("email", "") else "unknown",
        "region": "EU" if transformed.get("country") in ["RS", "DE", "FR", "IT", "ES"] else "OTHER"
    }

    event["enriched"] = enriched
    event["enrichmentStatus"] = "done"
    return event