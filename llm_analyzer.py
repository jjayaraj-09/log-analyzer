# llm_analyzer.py

from log_parser import LogEntry
from llm_local import analyze_logs_with_mistral

def format_cluster(cluster):
    return "\n".join(
        f"{e.timestamp.isoformat()} [{e.app}] {e.level}: {e.message}"
        for e in cluster
    )

def analyze_cluster_with_llm(cluster):
    logs_text = format_cluster(cluster)
    return analyze_logs_with_mistral(logs_text)
