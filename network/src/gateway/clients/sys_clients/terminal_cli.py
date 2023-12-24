# network/src/clients/terminal_cli.py
from src.error_handling.client_error_handler import (
    ClientError, ClientAuthenticationError, ClientConnectionError, ClientRequestError
)

class TerminalClient:
    def __init__(self):
        print("Terminal client initialized.")
        print("Welcome to the ACE Command Line Interface!")

    def test_client(self):
        return self.test_terminal()

    def start_client(self):
        return self.start_terminal()

    def test_terminal(self, test_message="ping"):
        try:
            print("Testing Terminal Client...")
            self.send_message(test_message)  # Simulate sending a message
            # Simulate receiving the same message (replace this with actual logic if needed)
            simulated_received_message = test_message
            if simulated_received_message == test_message:
                print("Terminal test successful.")
                return True
            else:
                print("Terminal test failed.")
                return False
        except Exception as e:
            print(f"Terminal's echo test failed with exception: {e}")
            return False

    def start_terminal(self):
        try:
            # Start any necessary processes or configurations
            print("Starting Terminal Client...")
            self.run()
        except Exception as e:
            print(f"Start failed: {e}")
            return False

    def send_message(self, message):
        # For a terminal client, sending might just mean printing to stdout
        print(f"ACE Agent: {message}")

    def receive_message(self):
        # For receiving messages, you might just take input from stdin
        return input("You: ")

    def run(self):
        # Example of a simple loop to send and receive messages
        print("Terminal client running. Type 'exit' to quit.")
        while True:
            message = self.receive_message()
            if message.lower() == 'exit':
                print("Goodbye!")
                break
            self.send_message(f"You said: {message}")

if __name__ == "__main__":
    # If running this script directly, instantiate and use the terminal client
    client = TerminalClient()
    client.run()