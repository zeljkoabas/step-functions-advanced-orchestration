def lambda_handler(event, context):

    transformed = {
        "customerId": event.get("customerId", "unknown"),
        "fullName": f"{event.get('firstName', '')} {event.get('lastName', '')}".strip(),
        "email": event.get("email", ""),
        "amount": event.get("amount", 0),
        "currency": event.get("currency", "EUR"),
        "country": event.get("country", "RS")
    }

    event["transformed"] = transformed
    event["transformStatus"] = "done"
    return event