# correlate.py

from src.core.log_parser import LogEntry

def find_error_clusters(entries: list[LogEntry]):
    clusters = []
    current = []

    for entry in entries:
        if entry.level == "ERROR":
            current.append(entry)
        else:
            if current:
                clusters.append(current)
                current = []

    if current:
        clusters.append(current)

    print(f"[INFO] Found {len(clusters)} error clusters")
    return clusters
