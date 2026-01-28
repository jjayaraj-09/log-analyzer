def format_cluster(cluster):
    return "\n".join(
        f"{e.timestamp.isoformat()} [{e.app}] {e.level}: {e.message}"
        for e in cluster
    )
