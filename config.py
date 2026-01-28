# config.py

LOG_FILES = {
    "A": "logs/app_a.log",
    "B": "logs/app_b.log",
    "C": "logs/app_c.log",
    "D": "logs/app_d.log",
    "E": "logs/app_e.log",
}

TIME_WINDOW_SECONDS = 60  # correlation window

EMAIL_FROM = "alerts@jjayaraj.com"
EMAIL_TO = ["oncall@jjayaraj.com"]
SMTP_SERVER = "smtp.jjayaraj.com"
SMTP_PORT = 587
SMTP_USER = "alerts@jjayaraj.com"
SMTP_PASSWORD = "SMTP_PASSWORD"
