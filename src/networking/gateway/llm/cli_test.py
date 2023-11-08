# src/networking/gateway/clients/cli_test.py
import json
from llm_client import LLMClient

model_path = "./models/athena-v4.Q4_K_M.gguf"


def main():
    print("Welcome to the ACE Language Model CLI. Type 'exit' to leave the CLI.")
    model_client = LLMClient(model_path)

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        # Send the input to the model and get a response
        response = model_client.predict(user_input)

        # Print the text response
        if response and "choices" in response and len(response["choices"]) > 0:
            print("ACE:", response["choices"][0]["text"])
        else:
            print("ACE: Error in generating response.")


if __name__ == '__main__':
    main()
