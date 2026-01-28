# llm_local.py

import ollama

def analyze_logs_with_mistral(log_text: str) -> str:
    prompt = f"""
You are a senior SRE.

Analyze the following logs from multiple applications (A → B → C → D → E).
Identify:
1. The most likely root cause (which app and why)
2. How the error propagated
3. Which team should act first
4. A short incident summary (2–3 sentences)

Logs:
{log_text}
"""

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]
