#config
import os

# Base paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# src/ -> go up one, then logs/
LOGS_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "logs"))

# LLM provider: "groq", "openai", "ollama"
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "groq").lower()

# LLM keys (custom names as you wanted)
GROQ_KEY = os.getenv("JJ_TEST_GROQ_LOG_ANALYZER_API_KEY")
OPENAI_KEY = os.getenv("jj_OPENAI_API_KEY")

# Email configuration
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")  # comma-separated list
