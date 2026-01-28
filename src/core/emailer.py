#emailer
import smtplib
from email.mime.text import MIMEText
from src.core.config import (
    SMTP_SERVER,
    SMTP_PORT,
    SMTP_USER,
    SMTP_PASSWORD,
    EMAIL_FROM,
    EMAIL_TO,
)


def send_incident_email(subject: str, body: str):
    if not all([SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, EMAIL_FROM, EMAIL_TO]):
        print("[WARN] Email not fully configured. Skipping send.")
        return

    recipients = [email.strip() for email in EMAIL_TO.split(",") if email.strip()]

    if not recipients:
        print("[WARN] EMAIL_TO is empty after parsing. Skipping send.")
        return

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_FROM
    msg["To"] = ", ".join(recipients)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(EMAIL_FROM, recipients, msg.as_string())

        print(f"[INFO] Email sent to: {recipients}")

    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")
