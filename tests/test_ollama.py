# tests/test_ollama.py

import ollama

def main():
    print("Testing Ollama Mistral model...")

    response = ollama.chat(
        model="mistral",
        messages=[
            {
                "role": "user",
                "content": "Explain this error: Timeout calling downstream service"
            }
        ]
    )

    print("\nLLM Response:\n")
    print(response["message"]["content"])

if __name__ == "__main__":
    main()


