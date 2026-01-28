# loader.py

from typing import List
from log_parser import LogEntry, parse_log_line
from config import LOG_FILES

def load_all_logs() -> List[LogEntry]:
    entries = []
    for app, path in LOG_FILES.items():
        try:
            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    entry = parse_log_line(line)
                    if entry:
                        entries.append(entry)
        except FileNotFoundError:
            continue

    entries.sort(key=lambda e: e.timestamp)
    return entries
