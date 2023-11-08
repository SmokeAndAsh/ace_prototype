# src/cognition.py
class Cognition:
    def __init__(self):
        self.ace_prompts = ACEPrompts()
        self.memory_prompts = MemoryPrompts()
        self.task_prompts = TaskPrompts()