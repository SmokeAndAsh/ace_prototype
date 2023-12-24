# src/network/gateway/handlers/client_handler.py
import os
from src.error_handling.client_error_handler import (
    ClientError, ClientAuthenticationError, ClientConnectionError, ClientRequestError
)
from src.gateway.clients.terminal_cli import TerminalClient
from src.gateway.clients.web_cli import WebClient
from src.gateway.clients.discord_cli import DiscordClient
from src.gateway.clients.novelai_cli import NovelAIClient

CLIENTS = {
    'terminal': TerminalClient,
    'web': WebClient,
    'discord': DiscordClient,
    'novelai': NovelAIClient,
}

class ClientHandler:
    def __init__(self, name):
        self.name = name
        self.clients = {}

    def get_client(self, client_type):
        # Logic to retrieve or initialize a client of a specific type
        client_class = CLIENTS.get(client_type)
        if client_class:
            return client_class()  # or manage an existing instance
        else:
            print(f"No client found for {client_type}")
            return None

class SystemHandler(ClientHandler):
    def __init__(self, base_url):
        super().__init__(base_url)

class CommunicationHandler(ClientHandler):
    def __init__(self, base_url):
        super().__init__(base_url)
        self.primary_client = self.select_comm_client('PRIMARY_COMMUNICATION_CLIENT')

    def select_comm_client(self, client_var):
        client_name = os.getenv(client_var)
        client_class = CLIENTS.get(client_name)
        if client_class:
            return client_class()
        else:
            print(f"No client found for {client_var}")
            return None

    def test_comm_client(self):
        if self.primary_client and hasattr(self.primary_client, 'test_client'):
            return self.primary_client.test_client()
        else:
            print("No test method available or no primary client set.")
            return False

    def start_comm_client(self):
        if self.primary_client and hasattr(self.primary_client, 'start_client'):
            return self.primary_client.start_client()
        else:
            print("No start function available or no primary client set.")
            return False

class LanguageHandler(ClientHandler):
    def __init__(self, base_url):
        super().__init__(base_url)
        self.primary_client = self.select_lang_client('PRIMARY_LANGUAGE_CLIENT')

    def select_lang_client(self, client_var):
        client_name = os.getenv(client_var)
        client_class = CLIENTS.get(client_name)
        if client_class:
            return client_class()
        else:
            print(f"No client found for {client_var}")
            return None

    def test_lang_client(self):
        if self.primary_client and hasattr(self.primary_client, 'test_client'):
            return self.primary_client.test_client()
        else:
            print("No test method available or no primary client set.")
            return False

class WebHandler(ClientHandler):
    def __init__(self, base_url):
        super().__init__(base_url)
