import ollama

def main():
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
