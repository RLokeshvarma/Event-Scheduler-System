# 📅 Event Scheduler System (Python + Flask + Email Reminders)

A simple yet powerful event scheduling system built with Python and Flask. This project helps users manage their events with features like reminders, recurring events, and email notifications — making time management more efficient and automated.

---

## 🚀 Key Features

- ✅ Add, view, update, and delete events using REST APIs
- ✅ Automatically stores all events in a JSON file (`events.json`)
- ✅ Sends **email reminders** for events starting within the next hour
- ✅ Supports **recurring events**: daily, weekly, and monthly
- ✅ Includes a Postman Collection for testing all APIs
- ✅ Cleanly separated code: `app.py` for API and `remainder.py` for reminders

---

## 🛠️ How the Project Works

### 🔹 1. Start the Flask API Server

This handles all the CRUD operations for events.

```bash
python app.py
```

Visit the API at:  
`http://127.0.0.1:5000/events`

Use the included **Postman Collection** to:
- Create new events
- List all events
- Update any event
- Delete specific events

---

### 🔹 2. Schedule Email Reminders

Runs a background task every minute to check for events starting in the next hour and sends an email reminder.

```bash
python remainder.py
```

Terminal will show the reminder output. If a reminder is triggered, an email will be sent to the user.

---

## ⚙️ Setup Instructions

### 🔸 Clone the Repo

```bash
git clone https://github.com/<your-username>/Event-Scheduler-System.git
cd Event-Scheduler-System
```

### 🔸 Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔸 Configure Email Credentials

Create a `.env` file (or rename `.env.example`) with your Gmail and app password:

```
FROM_EMAIL=your_email@gmail.com
FROM_PASSWORD=your_app_password
```

> Note: Use a Gmail App Password if you have 2FA enabled.

---

## 📂 Files Overview

- `app.py` – Flask API for event operations  
- `remainder.py` – Background email reminder service  
- `utils.py` – Shared functions (load/save events, email, datetime parsing)  
- `events.json` – Stores all event data  
- `.env.example` – Sample environment configuration  
- `Event-Scheduler-System.postman_collection.json` – Postman file to test APIs

---

## ✅ Sample Reminder Output

```bash
🔔 Reminder Sent:
📅 Title       : Doctor Appointment
🕒 Time        : 2025-06-29 15:00 to 2025-06-29 16:00
📝 Description : Routine check-up
🔁 Recurrence  : daily
--------------------------------------------------
✅ Email sent to: your_email@gmail.com for event: Doctor Appointment
```

---

## 📎 Git Ignore Setup

Ensure sensitive files are not pushed:

```
.env
__pycache__/
*.pyc
venv/
```

---

## 🙌 Final Notes

- Fully functional and ready to integrate into larger apps
- Easily extendable (e.g., add SMS, authentication, UI)
- Works great for both personal and small team use cases

---

