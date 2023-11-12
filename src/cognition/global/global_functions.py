# src/cognition/global/global_functions.py
L1_prompt_path = "src/cognition/global/global_prompts/L01_aspiration.md"
L2_prompt_path = "src/cognition/global/global_prompts/L02_global_strategy.md"


def read_markdown_prompt(file_path):
    with open(file_path, 'r') as f:
        markdown_string = f.read()
    return markdown_string


def generate_global_prompt(prompt_path, input_text):
    # Use the input_text and layer prompts to generate a tailored prompt
    global_prompt = read_markdown_prompt(prompt_path)
    prompt = global_prompt + input_text
    return prompt


class GlobalFunctions:

    @staticmethod
    def make_decision(*args, **kwargs):
        # Logic to make decisions aligned with the ACE's global values and goals
        pass

    @staticmethod
    def ethical_evaluation(*args, **kwargs):
        # Logic to evaluate decisions on ethical grounds
        pass


class GlobalCommunication:

    @staticmethod
    def trigger_ethical_concern(*args, **kwargs):
        # If a request or thought violates the agent's code of ethics,
        # trigger an alert for the agent to review the cause and run `ethical_evaluation`
        pass

    @staticmethod
    def trigger_personal_concern(*args, **kwargs):
        # If a request or thought might contradict the agent's unique perspective,
        # trigger an alert for the agent to review the cause
        # May require running:
        # `ethical_evaluation` (Global)
        # `self_assessment` (Independent) or
        # `review_current_agenda` (Focus)
        pass
