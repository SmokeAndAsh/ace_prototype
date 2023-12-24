# network/src/gateway/clients/comm_clients/comm_cli.py
from src.gateway.clients.base_cli import BaseClient

class CommunicationClient(BaseClient):
    def __init__(self, name, language_client=None):
        super().__init__(name)
        self.language_client = language_client  # Handles language operations, if any

    def test_connection(self):
        # Communication-specific test, perhaps a connection or echo test
        # Raise an exception if `test_connection` method still needs to be implemented by the subclass
        raise ClientImplementationError(self.name, "test_connection", self.__class__.__name__)

    def test_client(self):
        # Implement communication client specific test logic
        return self.test_connection()

    def start_client(self):
        # Implement communication client specific start logic
        print(f"Starting {self.name}...")
        # Insert Communication-specific startup logic here
        return True

    def get_routes(self):
        # Implement communication client specific list of route definitions
        return [
            {
                'methods': ['GET'],
                'endpoint': '/health',
            },
        ]