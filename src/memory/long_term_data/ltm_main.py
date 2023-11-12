# src/memory/ltm_main.py
import sqlite3


class LongTermMemory:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS chat_history (
            message_id INTEGER PRIMARY KEY, 
            conversation_id INTEGER,
            platform TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            recipients TEXT NOT NULL,
            sender TEXT NOT NULL,
            message TEXT NOT NULL
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def add_chat(self, conversation_id, platform, timestamp, recipients, sender, message):
        query = '''
        INSERT INTO chat_history (conversation_id, platform, timestamp, recipients, sender, message) 
        VALUES (?, ?, ?, ?, ?, ?)
        '''
        self.conn.execute(query, (conversation_id, platform, timestamp, recipients, sender, message))
        self.conn.commit()

    def get_chat_history(self, conversation_id=None):
        cursor = self.conn.cursor()
        if conversation_id:
            cursor.execute('SELECT * FROM chat_history WHERE conversation_id = ?', (conversation_id,))
        else:
            cursor.execute('SELECT * FROM chat_history')
        return cursor.fetchall()


# Usage Example
db_file = 'long_term_memory.db'
ltm = LongTermMemory(db_file)

# Adding data
ltm.add_chat(1, 'Discord', '2021-01-01 10:00:00', 'Alice,Bob', 'Alice', 'Hello!')
ltm.add_chat(1, 'Discord', '2021-01-01 10:05:00', 'Alice,Bob', 'Bob', 'Hi there!')

# Retrieving data for a specific conversation
chat_history = ltm.get_chat_history(conversation_id=1)
print(chat_history)
