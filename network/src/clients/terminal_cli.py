# network/src/clients/terminal_cli.py
from system.northbound_bus import NorthboundBus
from system.southbound_bus import SouthboundBus
from cognition.src.global_mod.global_functions import generate_global_prompt, L1_prompt_path, L2_prompt_path
from cognition.src.independent_mod.independent_functions import generate_independent_prompt, L3_prompt_path, L4_prompt_path
from cognition.src.focus_mod.focus_functions import generate_focus_prompt, L5_prompt_path, L6_prompt_path

def start_cli():
    # Initialize buses
    northbound_bus = NorthboundBus()
    southbound_bus = SouthboundBus()

    # Greet the user
    print("Welcome to the ACE Command Line Interface.")
    print("Type 'exit' to leave the CLI.")

    while True:
        # Get input from user
        user_input = input("You: ")

        # Agent Prompts
        aspirational_prompt = generate_global_prompt(L1_prompt_path, user_input)
        strategy_prompt = generate_global_prompt(L2_prompt_path, user_input)
        agent_prompt = generate_independent_prompt(L3_prompt_path, user_input)
        function_prompt = generate_independent_prompt(L4_prompt_path, user_input)
        control_prompt = generate_focus_prompt(L5_prompt_path, user_input)
        action_prompt = generate_focus_prompt(L6_prompt_path, user_input)

        # Exit the loop if the user wants to exit
        if user_input.lower() == 'exit':
            break

        # Send the generated prompt to the language model through the SouthboundBus
        agent_response = southbound_bus.process_control_message(agent_prompt)

        # Process any telemetry information (for demonstration purposes, we use a placeholder)
        # In a real scenario, this could include metrics like response times, etc.
        northbound_bus.send_telemetry("User interacted with the CLI")

        # Print the "in-character" response to the user
        print("ACE:", agent_response.strip())

    print("Goodbye!")
