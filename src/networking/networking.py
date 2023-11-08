# src/networking.py
class Networking:
    def __init__(self):
        self.input_output = InputOutput()
        self.northbound_bus = NorthboundBus()
        self.southbound_bus = SouthboundBus()