import requests
from django.http import JsonResponse
from datetime import datetime, timezone
import logging
import os

logger = logging.getLogger(__name__)

USER_EMAIL = os.getenv("USER_EMAIL", "your_email@example.com")
USER_NAME = os.getenv("USER_NAME", "Abraham Eriba")
USER_STACK = os.getenv("USER_STACK", "Python/Django")

CAT_FACTS_API = "https://catfact.ninja/fact"

def me(request):
    """
    GET /me endpoint
    Returns profile info + random cat fact
    """
    # Get current UTC timestamp in ISO 8601 format
    timestamp = datetime.now(timezone.utc).isoformat()

    cat_fact = None
    try:
        response = requests.get(CAT_FACTS_API, timeout=5)
        response.raise_for_status()  # Raises HTTPError if not 200
        data = response.json()
        cat_fact = data.get("fact", "Cats are amazing creatures.")
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch cat fact: {e}")
        cat_fact = "Could not fetch cat fact at this time."

    payload = {
        "status": "success",
        "user": {
            "email": USER_EMAIL,
            "name": USER_NAME,
            "stack": USER_STACK,
        },
        "timestamp": timestamp,
        "fact": cat_fact
    }

    return JsonResponse(payload, content_type="application/json", status=200)
