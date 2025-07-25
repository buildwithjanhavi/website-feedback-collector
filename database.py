import sqlite3

conn = sqlite3.connect('feedback.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')

# Create feedback table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        feedback TEXT NOT NULL,
        rating INTEGER NOT NULL,
        category TEXT NOT NULL
    )
''')

conn.commit()
conn.close()
print("Database setup complete.")
