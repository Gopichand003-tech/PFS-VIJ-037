import os
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
APP_PASSWORD = os.getenv("APP_PASSWORD")

print("Email:", repr(EMAIL_USER))
print("Password length:", len(APP_PASSWORD))

try:
    msg = EmailMessage()
    msg["From"] = EMAIL_USER
    msg["To"] = EMAIL_USER
    msg["Subject"] = "Voice Assistant Test"
    msg.set_content("Testing Gmail from Python.")

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()

        print("Logging into Gmail...")

        server.login(EMAIL_USER, APP_PASSWORD)

        print("Login successful!")

        server.send_message(msg)

    print("✅ EMAIL SENT!")

except Exception as e:
    print("❌ ERROR:")
    print(e)
