# src/networking/northbound_bus.py
import requests

from src.networking.gateway.llm.llm_client import LLMClient
from src.networking.gateway.llm.llm_config import conversational_llm
from src.networking.error_handling.client_error_handler import ClientError
from src.networking.error_handling.gateway_error_handler import GatewayError
from src.networking.error_handling.llm_error_handler import LLMError
from src.networking.error_handling.network_error_handler import NetworkError
from src.networking.error_handling.logs.nb_logging import NorthboundLogger


def report_error(error_data):
    # Log the error
    NorthboundLogger.log_error(error_data)


class NorthboundBus:
    """Handles telemetry and upward data flow."""
    def __init__(self):
        self.llm_client = LLMClient(conversational_llm)

    def initialize_network_connections(self):
        # Initialize HTTP or other network clients
        self.http_client = requests.Session()  # Example for HTTP requests
        # Additional network initialization as needed

    def send_telemetry(self, data):
        try:
            # Process and format the telemetry data
            formatted_data = self.format_telemetry_data(data)

            # Send the data to the relevant endpoint or system
            self.send_to_monitoring_system(formatted_data)

            # Log the successful telemetry transmission
            NorthboundLogger.log_message(f"Telemetry data sent: {formatted_data}")

        except (ClientError, GatewayError, LLMError, NetworkError) as e:
            # Log the error
            NorthboundLogger.log_error(str(e))

    def format_telemetry_data(self, data):
        # Implement the logic to format the telemetry data
        # Example: Convert to JSON, summarize, etc.
        return formatted_data

    def send_to_monitoring_system(self, formatted_data):
        # Implement the logic to send data to a monitoring system or database
        pass

    def get_nlp_inference(self, text_input):
        # Instantiate the LLMClient with the model
        model_client = LLMClient(self.model_path)

        # Send the text input to the model and get a response
        response = model_client.predict(text_input)

        # Log this interaction
        NorthboundLogger.log_message(f"Prompt: {text_input}")
        NorthboundLogger.log_message(f"Response: {response}")

        # Return the formatted response
        return response


