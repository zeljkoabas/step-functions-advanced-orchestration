def lambda_handler(event, context):
    transformed = event.get("transformed", {})
    enriched = event.get("enriched", {})

    api_request = {
        "externalCustomerId": transformed.get("customerId"),
        "name": transformed.get("fullName"),
        "email": transformed.get("email"),
        "transaction": {
            "amount": transformed.get("amount"),
            "currency": transformed.get("currency")
        },
        "metadata": {
            "segment": enriched.get("segment"),
            "region": enriched.get("region"),
            "emailDomain": enriched.get("emailDomain")
        }
    }

    event["apiRequest"] = api_request
    event["apiRequestStatus"] = "built"
    return event