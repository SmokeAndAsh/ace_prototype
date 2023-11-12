# src/networking/gateway/clients/terminal.py
from src.networking.northbound_bus import NorthboundBus
from src.networking.southbound_bus import SouthboundBus
from src.cognition.independent.agent_persona import Personality


def start_cli():
    # Initialize buses
    northbound_bus = NorthboundBus()
    southbound_bus = SouthboundBus()

    # Initialize persona
    persona = Personality()

    # Greet the user
    print("Welcome to the ACE Command Line Interface.")
    print("Type 'exit' to leave the CLI.")

    while True:
        # Get input from user
        user_input = input("You: ")

        # Exit the loop if the user wants to exit
        if user_input.lower() == 'exit':
            break

        generated_prompt = persona.generate_prompt(user_input)

        # Send the generated prompt to the language model through the SouthboundBus
        agent_response = southbound_bus.process_control_message(generated_prompt)

        # Process any telemetry information (for demonstration purposes, we use a placeholder)
        # In a real scenario, this could include metrics like response times, etc.
        northbound_bus.send_telemetry("User interacted with the CLI")

        # Print the "in-character" response to the user
        print("ACE:", agent_response.strip())

    print("Goodbye!")


if __name__ == '__main__':
    main()
