import os

import requests
from dotenv import load_dotenv

load_dotenv()

NTFY_TOPIC = os.getenv("NTFY_TOPIC")
NTFY_SERVER = os.getenv("NTFY_SERVER", "https://ntfy.sh")
REQUEST_TIMEOUT_SECONDS = 15


def send_message(message):
    """
    Sends a message using ntfy, a free push-notification service.
    """
    if not NTFY_TOPIC:
        raise RuntimeError("Missing required environment variable: NTFY_TOPIC")

    response = requests.post(
        f"{NTFY_SERVER.rstrip('/')}/{NTFY_TOPIC}",
        data=message.encode("utf-8"),
        headers={
            "Title": "CodeBuddy",
            "Tags": "computer",
        },
        timeout=REQUEST_TIMEOUT_SECONDS,
    )
    response.raise_for_status()
    print("Message sent successfully.")
