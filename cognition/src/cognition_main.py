# cognition/src/cognition_main.py

"""
The purpose of the `Cognition` module is to handle language model functions and prompts at a more abstract level, directing higher processes for the agent and providing guidance based on the agent's specific code of ethics (global), persona (individual), and task (focus).
"""


def read_file_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def test_global_layer():
    global_mission_path = "global_mod/global_prompts/GLOBAL_MISSION.md"
    global_mission = read_file_contents(global_mission_path)
    return global_mission


def test_independent_layer():
    independent_mission_path = "independent_mod/independent_prompts/INDEPENDENT_MISSION.md"
    independent_mission = read_file_contents(independent_mission_path)
    return independent_mission


def test_focus_layer():
    focus_mission_path = "focus_mod/focus_prompts/FOCUS_MISSION.md"
    focus_mission = read_file_contents(focus_mission_path)
    return focus_mission


def run_diagnostics():
    print("Running Cognition Module Diagnostics...")
    global_test = test_global_layer()
    independent_test = test_independent_layer()
    focus_test = test_focus_layer()

    if global_test and independent_test and focus_test:
        print("All layers operational.")
        print("Global Layer Mission:", global_test)
        print("Independent Layer Mission:", independent_test)
        print("Focus Layer Mission:", focus_test)
        return True
    else:
        print("Diagnostics failed. One or more layers are not operational.")
        return False


def main():
    if run_diagnostics():
        # Proceed with normal operation
        print("Cognition Module starting...")
    else:
        # Handle the failure, possibly retry or exit
        print("Cognition Module failed to start.")


if __name__ == "__main__":
    main()
