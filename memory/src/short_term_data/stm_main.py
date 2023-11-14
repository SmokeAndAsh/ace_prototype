# src/memory/stm_main.py
import time
from collections import deque
from src.cognition.independent.agent_persona import AgentPersona


class ShortTermMemory:
    def __init__(self, agent_persona, retention_period=3600):
        self.agent_persona = agent_persona  # Instance of AgentPersona
        self.retention_period = retention_period
        self.memory = deque()
        self.platform_context = ""  # Current platform (e.g., Discord)

    def add_data(self, data):
        timestamp = time.time()
        self.memory.append((timestamp, data))
        self._cleanup()

    def update_platform_context(self, platform):
        self.platform_context = platform

    def get_recent_data(self):
        return [data for _, data in self.memory]

    def _cleanup(self):
        current_time = time.time()
        while self.memory and current_time - self.memory[0][0] > self.retention_period:
            self.memory.popleft()


# Usage Example
agent_persona = AgentPersona(name="ACE", pronouns="they/them")
short_term_memory = ShortTermMemory(agent_persona, retention_period=3600)

# Updating platform context
short_term_memory.update_platform_context("Discord")

# Adding data
short_term_memory.add_data({"sender": "Alice", "message": "Hello!"})
short_term_memory.add_data({"sender": "Bob", "message": "Hi there!"})

# Retrieving recent data
recent_conversations = short_term_memory.get_recent_data()
print(recent_conversations)
