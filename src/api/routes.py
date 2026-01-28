from fastapi import APIRouter
from src.core.loader import load_all_logs
from src.core.correlate import find_error_clusters
from src.core.emailer import send_incident_email
from src.llm.provider import analyze_with_llm
from src.llm.formatter import format_cluster

router = APIRouter()


@router.get("/")
def health():
    return {"status": "ok"}

@router.get("/owner")
def owner():
    return {
        "app": "log-analyzer",
        "deployed_by": "Johnson Jayaraj",
        "github": "https://github.com/jjayaraj-09/log-analyzer",
        "timestamp": "2026-01-28"
    }



@router.post("/analyze",summary="Run log analysis",
    description="jjayaraj log analyzer grabs logs from five different microservice componentts of a same application, analyse the real root cause and summarize them." \
    " Future - @Tool Agents can be created to take action automatically.")
def analyze_logs():
    entries = load_all_logs()
    clusters = find_error_clusters(entries)

    results = []

    for i, cluster in enumerate(clusters, start=1):
        analysis = analyze_with_llm(cluster)

        subject = f"[Incident] Error Cluster #{i}"
        body = (
            f"Cluster #{i}\n\n"
            f"Raw log lines:\n{format_cluster(cluster)}\n\n"
            f"LLM Analysis:\n{analysis}"
        )

        send_incident_email(subject, body)

        results.append(
            {
                "cluster_index": i,
                "cluster": cluster,
                "analysis": analysis,
            }
        )

    return {"count": len(results), "results": results}
