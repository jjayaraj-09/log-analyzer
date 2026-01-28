#ollama_client.py

import requests

def analyze_with_ollama(cluster_text: str) -> str:
    prompt = (
        "You are an expert SRE. Analyze the following log cluster, "
        "summarize the incident, probable root cause, and suggested next steps.\n\n"
        f"{cluster_text}"
    )

    resp = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "mistral",
            "stream": False,  # IMPORTANT: disable streaming
            "messages": [
                {"role": "user", "content": prompt}
            ]
        },
        timeout=120,
    )

    resp.raise_for_status()
    data = resp.json()

    return data["message"]["content"]

