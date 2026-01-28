# Log Analyzer

- FastAPI-based log analyzer
- Supports multiple LLM providers (Groq, OpenAI, Ollama)
- Sends incident emails based on clustered errors

## Run locally

```bash
pip install -r requirements.txt
uvicorn src.main:app --reload
