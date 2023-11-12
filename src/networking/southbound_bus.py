# src/networking/southbound_bus.py
from src.config import MODEL_PATHS
from src.networking.gateway.llm.llm_client import LLMClient

# TODO: Set up process for dynamic model selection


class SouthboundBus:
    """Handles control commands and downward directives."""
    def __init__(self):
        # Initialize any necessary resources, like network connections or command queues
        # Specify the model path here to use it throughout the class.
        self.model_path = MODEL_PATHS['athena_q4']
        self.llm_client = LLMClient(MODEL_PATHS['athena_q4'])

    def receive_command(self):
        # Logic for receiving a command from an external system
        # Possibly involve parsing or validating the command format
        pass

    def execute_command(self, command):
        # Perform the actions needed based on the received command
        # Could involve calling methods on other parts of the ACE
        pass

    def update_configuration(self, configuration):
        # Update the ACE's configuration based on external inputs
        pass

    def process_nlp_request(self, text_input):
        # Instantiate the LLMClient with the model
        model_client = LLMClient(self.model_path)

        # Send the text input to the model and get a response
        response = model_client.predict(text_input)

        # Take action based on the response
        # TODO: Implement command execution based on the model's response

        # Return any relevant information or acknowledgment
        return True  # Placeholder acknowledgment

    def process_control_message(self, text_input):
        # Option to set max_tokens or pass in via method arguments
        max_response_tokens = 100

        # Option to set stop tokens if the model supports it
        stop = None

        # Send the text input to the model and get a response
        response = self.llm_client.predict(text_input, max_tokens=max_response_tokens, stop=stop)

        # Extract the text response after the model processes the persona prompt
        text_response = response.get('choices', [{}])[0].get('text', '').strip()

        # Take action based on the response
        # TODO: Implement command execution based on the response text

        # Return the actual response or formatted response
        return text_response
