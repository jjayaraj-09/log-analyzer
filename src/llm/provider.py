#provider

from src.llm.formatter import format_cluster
from src.core.config import LLM_PROVIDER
from src.llm.groq_client import analyze_with_groq
from src.llm.openai_client import analyze_with_openai
from src.llm.ollama_client import analyze_with_ollama


def analyze_with_llm(cluster):
    text = format_cluster(cluster)

    if LLM_PROVIDER == "groq":
        return analyze_with_groq(text)
    elif LLM_PROVIDER == "openai":
        return analyze_with_openai(text)
    elif LLM_PROVIDER == "ollama":
        return analyze_with_ollama(text)
    else:
        raise RuntimeError(f"Unsupported LLM provider: {LLM_PROVIDER}")
