# src/memory.py
class Memory:
    def __init__(self):
        self.short_term_data = ShortTermData()
        self.long_term_data = LongTermData()
        self.qualitative_data = QualitativeData()