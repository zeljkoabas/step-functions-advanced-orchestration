from datetime import datetime, timezone
import time

def lambda_handler(event, context):
    data = event.get("data", {})
    token = event.get("token", "")

    if not token:
        raise ValueError("Missing bearer token.")

    api_request = data.get("apiRequest", {})
    time.sleep(2)  # Simulate external API call delay

    response = {
        "statusCode": 200,
        "calledAt": datetime.now(timezone.utc).isoformat(),
        "endpoint": "https://api.example.com/customers",
        "authorizationUsed": token.startswith("demo-access-token"),
        "requestEcho": api_request,
        "responseBody": {
            "externalId": "ext-987654",
            "status": "accepted"
        }
    }

    data["externalApiResponse"] = response
    data["externalApiStatus"] = "success"
    return data