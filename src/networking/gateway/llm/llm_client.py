# src/networking/gateway/clients/llm_client.py
import torch
from transformers import AutoModel, AutoTokenizer
from llama_cpp import Llama


class HuggingFaceClient:
    def __init__(self, model_directory):
        self.model_directory = model_directory
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_directory)
        self.model = AutoModel.from_pretrained(self.model_directory)
        self.device = "cuda"

    def predict(self, inputs):
        # Tokenize the input text
        tokens = self.tokenizer(inputs, padding=True, truncation=True, return_tensors="pt")
        tokens = tokens.to(self.device)

        # Get model predictions
        with torch.no_grad():
            outputs = self.model(**tokens)
            # Handle the outputs, e.g. extract the last hidden states

        # Return appropriate data based on the model's outputs
        return outputs


class LLMClient:
    def __init__(self, model_directory):
        self.model = Llama(model_path=model_directory)

    def predict(self, prompt, max_tokens=128, stop=None, echo=False):
        response = self.model(prompt, max_tokens=max_tokens, stop=stop, echo=echo)
        return response
