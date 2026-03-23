def lambda_handler(event, context):
    transformed = event.get("transformed", {})

    required_fields = ["customerId", "email", "amount"]
    missing_fields = [
        field for field in required_fields
        if transformed.get(field) in (None, "", [])
    ]

    if missing_fields:
        raise ValueError(f"Validation failed. Missing fields: {', '.join(missing_fields)}")

    if transformed.get("amount", 0) <= 0:
        raise ValueError("Validation failed. Amount must be greater than 0.")

    event["validationStatus"] = "passed"
    return event