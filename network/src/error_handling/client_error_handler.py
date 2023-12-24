# network/src/error_handling/client_error_handler.py
class ClientError(Exception):
    """Base class for Client related exceptions."""
    def __init__(self, message="A client error occurred"):
        super().__init__(message)

class ClientAuthenticationError(ClientError):
    """Exception raised for client authentication failures."""

    def __init__(self, client_name, message="Client authentication failed"):
        self.client_name = client_name
        self.message = f"{message}. Client: {client_name}"
        super().__init__(self.message)

class ClientConfigError(ClientError):
    """Exception raised for client configuration errors."""

    def __init__(self, client_name, request_info, message="Client request error"):
        self.client_name = client_name
        self.message = f"{message}. Client: {client_name}"
        super().__init__(self.message)

class ClientConnectionError(ClientError):
    """Exception raised for client connection issues."""

    def __init__(self, client_name, message="Client connection failed"):
        self.client_name = client_name
        self.message = f"{message}. Client: {client_name}"
        super().__init__(self.message)

class ClientCredentialsError(ClientError):
    """Exception raised for error with client credentials."""

    def __init__(self, client_name, message="Client credentials error"):
        self.client_name = client_name
        self.message = f"{message}. Client: {client_name}"
        super().__init__(self.message)

class ClientImplementationError(ClientError):
    """Exception raised for client implementation errors."""

    def __init__(self, client_name, method, client_type, message="Client implementation error"):
        self.client_name = client_name
        self.method = method
        self.client_type = client_type
        self.message = f"{message}. Client: {client_name}, Method: {method} must be implemented in {client_class} subclasses."
        super().__init__(self.message)

class ClientInitError(ClientError):
    """Exception raised for client initialization errors."""

    def __init__(self, client_name, message="Client initialization error"):
        self.client_name = client_name
        self.message = f"{message}. Client: {client_name}"
        super().__init__(self.message)

class ClientRequestError(ClientError):
    """Exception raised for errors during client requests."""

    def __init__(self, client_name, request_info, message="Client request error"):
        self.client_name = client_name
        self.request_info = request_info
        self.message = f"{message}. Client: {client_name}, Request Info: {request_info}"
        super().__init__(self.message)