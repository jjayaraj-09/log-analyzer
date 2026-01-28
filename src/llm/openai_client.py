#openai_py

from openai import OpenAI
from src.core.config import OPENAI_KEY


def analyze_with_openai(cluster_text: str) -> str:
    if not OPENAI_KEY:
        raise RuntimeError("jj_OPENAI_API_KEY not set")

    client = OpenAI(api_key=OPENAI_KEY)

    prompt = (
        "You are an expert SRE. Analyze the following log cluster, "
        "summarize the incident, probable root cause, and suggested next steps.\n\n"
        f"{cluster_text}"
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message["content"]

