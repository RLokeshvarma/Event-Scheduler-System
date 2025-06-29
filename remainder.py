from utils import load_events, parse_datetime, send_email_reminder
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

FROM_EMAIL = os.getenv("FROM_EMAIL")
TO_EMAIL = FROM_EMAIL  # Same email for sending and receiving in your case

print("Email loaded:", FROM_EMAIL)
print("Password loaded:", os.getenv("FROM_PASSWORD"))
print("Reminder service started. Checking upcoming events...\n")

sent_event_ids = set()  # Track sent events

def check_reminders():
    events = load_events()
    now = datetime.now()
    one_hour_later = now + timedelta(hours=1)

    found = False

    for event in events:
        start_time = parse_datetime(event["start_time"])
        recurrence = event.get("recurrence")

        # Adjust recurring events to today
        if recurrence == "daily":
            start_time = start_time.replace(year=now.year, month=now.month, day=now.day)
        elif recurrence == "weekly":
            while start_time.weekday() != now.weekday():
                start_time += timedelta(days=1)
        elif recurrence == "monthly":
            start_time = start_time.replace(year=now.year, month=now.month)

        if now <= start_time <= one_hour_later and event["id"] not in sent_event_ids:
            found = True
            sent_event_ids.add(event["id"])

            # Prepare email
            subject = f"⏰ Reminder: {event['title']}"
            content = (
                f"📅 Title       : {event['title']}\n"
                f"🕒 Time        : {event['start_time']} to {event['end_time']}\n"
                f"📝 Description : {event['description']}\n"
                f"🔁 Recurrence  : {recurrence or 'None'}"
            )

            # Send email
            send_email_reminder(TO_EMAIL, subject, content)

            # Terminal output
            print("🔔 Reminder Sent:")
            print(content)
            print("--------------------------------------------------")
            print(f"✅ Email sent to: {TO_EMAIL} for event: {event['title']}\n")

    if not found:
        print("✅ No upcoming events in the next hour.\n")

# Run once then exit
check_reminders()
