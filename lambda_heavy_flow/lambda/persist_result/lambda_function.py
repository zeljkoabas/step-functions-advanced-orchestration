from datetime import datetime, timezone

def lambda_handler(event, context):
    persisted_record = {
        "saved": True,
        "savedAt": datetime.now(timezone.utc).isoformat(),
        "recordId": event.get("requestId", "unknown"),
        "externalId": event.get("externalApiResponse", {}).get("responseBody", {}).get("externalId")
    }

    event["persistence"] = persisted_record
    event["finalStatus"] = "completed"
    return event