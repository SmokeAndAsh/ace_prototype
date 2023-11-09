# src/tools/agent_cli.py
from src.networking.northbound_bus import NorthboundBus
from src.networking.southbound_bus import SouthboundBus


def main():
    # Initialize buses
    northbound_bus = NorthboundBus()
    southbound_bus = SouthboundBus()

    # Greet the user
    print("Welcome to the ACE Command Line Interface.")
    print("Type 'exit' to leave the CLI.")

    while True:
        # Get input from user
        user_input = input("You: ")

        # Exit the loop if the user wants to exit
        if user_input.lower() == 'exit':
            break

        # Process the command through the SouthboundBus
        response = southbound_bus.process_control_message(user_input)

        # Print the response to the user
        print("ACE:", response.strip())

        # Optionally, print any telemetry data received from the NorthboundBus

    print("Goodbye!")


if __name__ == '__main__':
    main()
