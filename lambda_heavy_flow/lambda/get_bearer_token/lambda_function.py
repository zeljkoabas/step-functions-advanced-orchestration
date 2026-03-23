from datetime import datetime, timedelta, timezone
import time

def lambda_handler(event, context):
    token_url = event.get("token_url", "unknown")
    client_id = event.get("client_id", "unknown")
    time.sleep(1)  # Simulate processing delay
    expires_at = datetime.now(timezone.utc) + timedelta(hours=1)

    return {
        "access_token": "demo-access-token-123456",
        "token_type": "Bearer",
        "expires_in": 3600,
        "expires_at": expires_at.isoformat(),
        "issued_for": client_id,
        "token_url": token_url
    }