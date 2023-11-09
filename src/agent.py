# src/agent.py
class Agent:
    def __init__(self):
        self.cognition = Cognition()
        self.memory = Memory()
        self.networking = Networking()