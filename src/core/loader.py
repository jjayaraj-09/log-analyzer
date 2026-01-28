# loader.py

import os
from src.core.config import LOGS_DIR
from src.core.log_parser import parse_log_line


def load_all_logs():
    entries = []

    if not os.path.exists(LOGS_DIR):
        print(f"[WARN] Logs directory not found: {LOGS_DIR}")
        return entries

    print(f"[INFO] Loading logs from: {LOGS_DIR}")

    for filename in os.listdir(LOGS_DIR):
        if not filename.endswith(".log"):
            continue

        file_path = os.path.join(LOGS_DIR, filename)
        print(f"[INFO] Reading {file_path}")

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    entry = parse_log_line(line)
                    if entry:
                        entries.append(entry)
        except Exception as e:
            print(f"[ERROR] Failed to read {file_path}: {e}")

    print(f"[INFO] Loaded {len(entries)} structured log entries")
    return entries
