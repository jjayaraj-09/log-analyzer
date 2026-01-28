# main.py

from loader import load_all_logs
from correlate import find_error_clusters
from llm_analyzer import analyze_cluster_with_llm
from emailer import send_incident_email

def main():
    entries = load_all_logs()
    print(f"Loaded {len(entries)} log entries")

    clusters = find_error_clusters(entries)
    print(f"Found {len(clusters)} correlated error clusters")


    if not clusters:
        print("No correlated error clusters found.")
        return

    for i, cluster in enumerate(clusters, start=1):
        analysis = analyze_cluster_with_llm(cluster)
        subject = f"[Incident] Correlated errors across services (cluster {i})"
        body = f"Correlated error cluster {i} detected.\n\nLLM Analysis:\n\n{analysis}"
        print(f"Email body:\n{body}")

        #send_incident_email(subject, body)
        print(f"Sent incident email for cluster {i}")

if __name__ == "__main__":
    main()
