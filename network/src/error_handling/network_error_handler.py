# network/src/error_handling/network_error_handler.py
class NetworkError(Exception):
    """Base class for general Network exceptions."""
    pass

class NetworkConfigError(NetworkError):
    """Exception raised for network configuration errors."""

    def __init__(self, message="Network configuration error"):
        self.message = message
        super().__init__(self.message)

class NetworkInitError(NetworkError):
    """Exception raised for network initialization errors."""

    def __init__(self, message="Network initialization error"):
        self.message = message
        super().__init__(self.message)

class NetworkTimeoutError(NetworkError):
    """Exception raised for network timeout errors."""

    def __init__(self, endpoint, timeout, message="Network request timed out"):
        self.endpoint = endpoint
        self.timeout = timeout
        self.message = f"{message}. Endpoint: {endpoint}, Timeout: {timeout}s"
        super().__init__(self.message)