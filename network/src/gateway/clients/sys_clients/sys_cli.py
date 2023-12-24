# network/src/gateway/clients/sys_clients/sys_cli.py
from src.gateway.clients.base_cli import BaseClient

class SystemClient(BaseClient):
    def __init__(self, name):
        super().__init__(name)
        # Initialize system-specific attributes here

    def test_client(self):
        # Implement system client specific test logic
        return self.test_sys()

    def start_client(self):
        # Implement system client specific start logic
        print(f"Starting {self.name}...")
        # Insert System-specific startup logic here
        return True