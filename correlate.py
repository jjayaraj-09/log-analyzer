# correlate.py

from datetime import timedelta
from typing import List
from log_parser import LogEntry
from config import TIME_WINDOW_SECONDS

def find_error_clusters(entries: List[LogEntry]) -> List[List[LogEntry]]:
    error_entries = [e for e in entries if e.level == "ERROR"]
    clusters = []

    if not error_entries:
        return clusters

    current = [error_entries[0]]

    for e in error_entries[1:]:
        last = current[-1]
        if (e.timestamp - last.timestamp) <= timedelta(seconds=TIME_WINDOW_SECONDS):
            current.append(e)
        else:
            if len(current) > 1:
                clusters.append(current)
            current = [e]

    if len(current) > 1:
        clusters.append(current)

    return clusters
