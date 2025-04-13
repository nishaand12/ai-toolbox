import sqlite3
import os

# Create database directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# Connect to SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect('data/ai_tools.db')

# Create a cursor object
cursor = conn.cursor()

# Create the ai_resources table
cursor.execute('''
CREATE TABLE IF NOT EXISTS ai_resources (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    url TEXT,
    category TEXT,
    pricing TEXT,
    regulations TEXT,
    use_case TEXT,
    industries TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully!") 