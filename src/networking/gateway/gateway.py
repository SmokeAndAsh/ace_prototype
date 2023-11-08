# src/networking/gateway.py
import requests


class Gateway:
    def __init__(self):
        self.clients = Clients()


class Clients:
    def __init__(self):
        self.language_model_client = LanguageModelClient()