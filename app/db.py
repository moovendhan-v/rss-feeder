import sqlite3
import os

# Define the path to the database
DB_PATH = os.path.join(os.path.dirname(__file__), '../rss_sent.db')  # Adjust path based on project structure

def initialize_db():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sent_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                link TEXT UNIQUE
            )
        ''')
        conn.commit()
        print("Database initialized successfully.")
    except sqlite3.Error as e:
        print(f"Error initializing the database: {e}")
    finally:
        if conn:
            conn.close()

def store_sent_link(link):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('INSERT OR IGNORE INTO sent_items (link) VALUES (?)', (link,))
        conn.commit()
        print(f"Link stored successfully: {link}")
    except sqlite3.Error as e:
        print(f"Error storing the link '{link}': {e}")
    finally:
        if conn:
            conn.close()

def has_been_sent(link):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT 1 FROM sent_items WHERE link = ?', (link,))
        result = cursor.fetchone()
        return result is not None
    except sqlite3.Error as e:
        print(f"Error checking if link has been sent '{link}': {e}")
        return False
    finally:
        if conn:
            conn.close()

