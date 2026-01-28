# log_parser.py

from datetime import datetime
from dataclasses import dataclass

@dataclass
class LogEntry:
    timestamp: datetime
    level: str
    app: str
    message: str


def parse_log_line(line: str) -> LogEntry | None:
    """
    Expected format:
    2024-01-01T12:00:00Z ERROR [APP_A] Something bad happened
    """
    try:
        ts_str, level, app_part, *msg_parts = line.strip().split(" ", 3)
        timestamp = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
        app = app_part.strip("[]").replace("APP_", "")
        message = msg_parts[0] if msg_parts else ""
        return LogEntry(timestamp, level, app, message)
    except Exception:
        return None
