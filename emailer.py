# emailer.py

import smtplib
from email.mime.text import MIMEText
from config import (
    EMAIL_FROM, EMAIL_TO, SMTP_SERVER, SMTP_PORT,
    SMTP_USER, SMTP_PASSWORD
)

def send_incident_email(subject: str, body: str):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_FROM
    msg["To"] = ", ".join(EMAIL_TO)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
