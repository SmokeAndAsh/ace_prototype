# src/networking/clients/llm_utils.py
from transformers import pipeline

class LanguageModelClient:
    def __init__(self, model_name="distilbert-base-uncased"):
        self.pipeline = pipeline("text-classification", model=model_name)

    def classify_text(self, text):
        return self.pipeline(text)