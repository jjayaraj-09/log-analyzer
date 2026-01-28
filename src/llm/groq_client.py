# groq_client.py

from groq import Groq
from src.core.config import GROQ_KEY


def analyze_with_groq(cluster_text: str) -> str:
    if not GROQ_KEY:
        raise RuntimeError("JJ_TEST_GROQ_LOG_ANALYZER_API_KEY not set")

    client = Groq(api_key=GROQ_KEY)

    prompt = f"""
You are an expert Site Reliability Engineer (SRE) analyzing logs from a 
5‑service microservice chain: A → B → C → D → E.

You will receive multiple error clusters combined into one text block. 
Your task is to produce ONE unified root‑cause analysis.

Follow these rules strictly:

1. Identify the SINGLE root cause of the entire incident.
2. Identify which component (A, B, C, D, or E) caused the failure.
3. Explain how the failure propagated across the chain.
4. Provide the business impact.
5. Provide recommended fixes.
6. Produce ONE final consolidated incident summary.
7. Do NOT analyze each cluster separately.
8. Do NOT produce multiple summaries.
9. Do NOT repeat the same information for each service.

Here are the clustered logs:

{cluster_text}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content
