# src/networking/networking_main.py
from gateway.llm.llm_config import MODEL_PATHS, conversational_llm
from gateway.llm.llm_client import LLMClient


def test_language_model_client():
    try:
        model_path = MODEL_PATHS[conversational_llm]
        llm_client = LLMClient(model_path)
        test_prompt = "Hello, world!"
        response = llm_client.predict(test_prompt, max_tokens=100, stop=None)
        if response:
            print("Language model client operational. Response:", response)
            return True
        else:
            print("Language model client failed to respond.")
            return False
    except Exception as e:
        print(f"Error testing language model client: {e}")
        return False


def run_diagnostics():
    print("Running Networking Module Diagnostics...")
    llm_client_ok = test_language_model_client()

    if llm_client_ok:
        print("Networking Module diagnostics successful.")
        return True
    else:
        print("Networking Module diagnostics failed.")
        return False


def main():
    if run_diagnostics():
        # Proceed with normal operation
        print("Networking Module starting...")
    else:
        # Handle the failure
        print("Networking Module failed to start.")


if __name__ == "__main__":
    main()
