# src/networking/northbound_bus.py
from src.config import MODEL_PATHS
from src.networking.gateway.llm.llm_client import LLMClient
from src.networking.error_handling.logs.nb_logging import NorthboundLogger

# TODO: Set up process for dynamic model selection


class NorthboundBus:
    """Handles telemetry and upward data flow."""
    def __init__(self):
        # Initialize any necessary resources, like network connections or queues
        # Specify the model path here to use it throughout the class.
        self.model_path = MODEL_PATHS['athena_q4']
        self.llm_client = LLMClient(MODEL_PATHS['athena_q4'])

    def send_telemetry(self, data):
        # Process and format the telemetry data
        # Send the data to the relevant endpoint or system
        pass

    def report_error(self, error_data):
        # Format and send error data to the monitoring system
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

    def report_error(self, error_data):
        # Log the error
        NorthboundLogger.log_error(error_data)
