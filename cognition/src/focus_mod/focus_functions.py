# src/cognition/focus/focus_functions.py
L5_prompt_path = "src/cognition/focus/focus_prompts/L5_cognitive_control.md"
L6_prompt_path = "src/cognition/focus/focus_prompts/L6_task_prosecution.md"


def read_markdown_prompt(file_path):
    with open(file_path, 'r') as f:
        markdown_string = f.read()
    return markdown_string


def generate_focus_prompt(prompt_path, input_text):
    # Use the input_text and layer prompts to generate a tailored prompt
    focus_prompt = read_markdown_prompt(prompt_path)
    prompt = focus_prompt + input_text
    return prompt


class FocusFunctions:

    @staticmethod
    def perform_task(task_id, *args, **kwargs):
        # Logic to initiate and monitor task execution
        # Utilizes `ActionPerform` class in `focus_actions`
        pass

    @staticmethod
    def review_current_agenda(*args, **kwargs):
        # Review current task agenda
        pass

    @staticmethod
    def evaluate_task_success(*args, **kwargs):
        # Determine if a task has been successfully completed
        # Utilizes `ActionPerform` class in `focus_actions`
        pass


class FocusCommunication:

    @staticmethod
    def report_task_status(*args, **kwargs):
        # Report results of `evaluate_task_success`
        pass
