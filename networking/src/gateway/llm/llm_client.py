# src/networking/gateway/clients/llm_client.py
from llama_cpp import Llama


class LLMClient:
    def __init__(self, model_directory):
        self.model = Llama(model_path=model_directory, n_ctx=2048)

    def predict(self, prompt, max_tokens, stop, echo=False):
        # Formatting prompt
        formatted_prompt = f"{prompt}"

        response = self.model(formatted_prompt, max_tokens=max_tokens, stop=stop, echo=echo)

        return response
