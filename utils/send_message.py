from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Twilio credentials
ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')
WHATSAPP_NUMBER = os.getenv('WHATSAPP_NUMBER')
YOUR_NUMBER = os.getenv('YOUR_NUMBER')

# Initialize Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_whatsapp_message(message):
    """
    Sends a WhatsApp message using Twilio.
    """
    msg = client.messages.create(
        body=message,
        from_=WHATSAPP_NUMBER,
        to=YOUR_NUMBER
    )
    print(f"Message sent with SID: {msg.sid}")
