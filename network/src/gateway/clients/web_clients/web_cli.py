# network/src/gateway/clients/web_clients/web_cli.py
from flask import Flask
from src.gateway.clients.base_cli import BaseClient

class WebClient(BaseClient):
    def __init__(self, name):
        super().__init__(name)
        # Initialize Flask app here or pass it as a parameter
        self.web_app = Flask(__name__)

    def test_web(self):
        # Implement meaningful test for web client
        # This could include making a test HTTP request or checking server status
        raise ClientImplementationError(self.name, "test_web", self.__class__.__name__)

    def test_client(self):
        # Implement web client specific test logic
        print(f"Testing {self.name}...")
        return self.test_web()

    def start_web(self):
        # Implement meaningful start for web client
        # This could include setting up web server, defining routes, etc.
        raise ClientImplementationError(self.name, "start_web", self.__class__.__name__)

    def start_client(self):
        # Implement web client specific start logic
        print(f"Starting {self.name}...")
        return self.start_web()

    def get_routes(self):
        # Implement web client specific list of route definitions
        return [
            {
                'methods': ['GET'],
                'endpoint': '/health',
            },
        ]