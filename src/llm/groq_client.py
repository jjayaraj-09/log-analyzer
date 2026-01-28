#groq_client

from groq import Groq
from src.core.config import GROQ_KEY


def analyze_with_groq(cluster_text: str) -> str:
    if not GROQ_KEY:
        raise RuntimeError("JJ_TEST_GROQ_LOG_ANALYZER_API_KEY not set")

    client = Groq(api_key=GROQ_KEY)

    prompt = (
        "You are an expert SRE. Analyze the following log cluster, "
        "summarize the incident, probable root cause, and suggested next steps.\n\n"
        f"{cluster_text}"
    )

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content
