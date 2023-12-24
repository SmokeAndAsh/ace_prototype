# network/src/gateway/clients/base_cli.py
from src.error_handling.client_error_handler import ClientError, ClientInitError

class BaseClient:
    def __init__(self, name):
        self.name = name

    def test_client(self):
        # Raise an exception if `test_client` method still needs to be implemented by the subclass
        raise ClientImplementationError(self.name, "test_client", self.__class__.__name__)

    def start_client(self):
        # Raise an exception if `start_client` method still needs to be implemented by the subclass
        raise ClientImplementationError(self.name, "start_client", self.__class__.__name__)

    def get_routes(self):
        # Raise an exception if `get_routes` method still needs to be implemented by the subclass
        raise ClientImplementationError(self.name, "get_routes", self.__class__.__name__)