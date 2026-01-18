import sqlite3

DB_NAME = "quiz.db"

def save_attempt(name, answers, character):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            answers TEXT,
            character TEXT
        )
    """)
    cursor.execute(
        "INSERT INTO attempts (name, answers, character) VALUES (?, ?, ?)",
        (name, answers, character)
    )
    conn.commit()
    conn.close()
