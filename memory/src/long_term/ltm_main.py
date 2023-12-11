# memory/src/ltm_main.py
import psycopg2
import psycopg2.extras

class LongTermMemory:
    def __init__(self, db_params):
        self.conn = psycopg2.connect(**db_params)
        self.create_table()

    def create_table(self):
        query = '''CREATE TABLE IF NOT EXISTS chat_history (
                    message_id SERIAL PRIMARY KEY,
                    conversation_id INTEGER NOT NULL,
                    platform TEXT NOT NULL,
                    timestamp TIMESTAMP NOT NULL,
                    recipients TEXT NOT NULL,
                    sender TEXT NOT NULL,
                    message TEXT NOT NULL
                  );'''
        with self.conn.cursor() as cursor:
            cursor.execute(query)
            self.conn.commit()

    def add_chat(self, conversation_id, platform, timestamp, recipients, sender, message):
        query = '''INSERT INTO chat_history (conversation_id, platform, timestamp, recipients, sender, message)
                   VALUES (%s, %s, %s, %s, %s, %s);'''
        with self.conn.cursor() as cursor:
            cursor.execute(query, (conversation_id, platform, timestamp, recipients, sender, message))
            self.conn.commit()

    def get_chat_history(self, conversation_id=None):
        with self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            if conversation_id:
                cursor.execute('SELECT * FROM chat_history WHERE conversation_id = %s', (conversation_id,))
            else:
                cursor.execute('SELECT * FROM chat_history')
            return cursor.fetchall()

# Database connection parameters
db_params = {
    'dbname': 'ace_ltm',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost'
}

# Example usage
ltm = LongTermMemory(db_params)

# Adding data
ltm.add_chat(1, 'Discord', '2021-01-01 10:00:00', 'Alice,Bob', 'Alice', 'Hello!')
ltm.add_chat(1, 'Discord', '2021-01-01 10:05:00', 'Alice,Bob', 'Bob', 'Hi there!')

# Retrieving data for a specific conversation
chat_history = ltm.get_chat_history(conversation_id=1)
print(chat_history)
