import smtplib
from email.mime.text import MIMEText

FROM_EMAIL = "lokkipvt@gmail.com"
FROM_PASSWORD = "bvmmjnfmdxlswxlk"
TO_EMAIL = "lokkipvt@gmail.com"

msg = MIMEText("This is a test email from your Python script.")
msg["Subject"] = "EventScheduler Test Email"
msg["From"] = FROM_EMAIL
msg["To"] = TO_EMAIL

try:
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.starttls()
    smtp.login(FROM_EMAIL, FROM_PASSWORD)
    smtp.send_message(msg)
    smtp.quit()
    print("✅ Email sent successfully!")
except smtplib.SMTPAuthenticationError as e:
    print("❌ Authentication failed:", e)
except Exception as e:
    print("❌ Something else went wrong:", e)
