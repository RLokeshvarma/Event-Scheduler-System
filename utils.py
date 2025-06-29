import json
import os
from dotenv import load_dotenv
from datetime import datetime
from os.path import exists
import smtplib
from email.message import EmailMessage

# Load environment variables
load_dotenv()

# These should be set in your .env file (DO NOT hardcode them)
FROM_EMAIL = os.getenv("FROM_EMAIL")             # e.g., your_email@gmail.com
FROM_PASSWORD = os.getenv("FROM_PASSWORD")       # e.g., your Gmail App Password

EVENT_FILE = 'events.json'

def load_events():
    if not exists(EVENT_FILE):
        return []
    with open(EVENT_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_events(events):
    with open(EVENT_FILE, 'w') as f:
        json.dump(events, f, indent=2)

def parse_datetime(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d %H:%M')

def send_email_reminder(to_email, subject, content):
    msg = EmailMessage()
    msg.set_content(content)
    msg['Subject'] = subject
    msg['From'] = FROM_EMAIL
    msg['To'] = to_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(FROM_EMAIL, FROM_PASSWORD)
            smtp.send_message(msg)
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
