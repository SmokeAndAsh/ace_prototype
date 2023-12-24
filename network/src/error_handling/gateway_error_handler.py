# network/src/error_handling/gateway_error_handler.py
class GatewayError(Exception):
    """Base class for Gateway related exceptions."""
    pass

class GatewayConnectionError(GatewayError):
    """Exception raised for errors in the gateway connection."""

    def __init__(self, endpoint, message="Gateway connection failed"):
        self.endpoint = endpoint
        self.message = f"{message}. Endpoint: {endpoint}"
        super().__init__(self.message)

class GatewayRequestError(GatewayError):
    """Exception raised for errors in processing requests in the gateway."""

    def __init__(self, request_info, message="Error processing request"):
        self.request_info = request_info
        self.message = f"{message}. Request Info: {request_info}"
        super().__init__(self.message)

class GatewayResponseError(GatewayError):
    """Exception raised for unexpected responses from the gateway."""

    def __init__(self, status_code, response=None, message="Unexpected gateway response"):
        self.status_code = status_code
        self.response = response
        self.message = f"{message}. Status Code: {status_code}, Response: {response}"
        super().__init__(self.message)
