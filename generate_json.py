import sqlite3
import json
import os

def generate_json():
    # Connect to SQLite database
    conn = sqlite3.connect('data/ai_tools.db')
    conn.row_factory = sqlite3.Row  # This enables column access by name
    cursor = conn.cursor()

    # Query all resources
    cursor.execute('SELECT * FROM ai_resources ORDER BY name')
    resources = [dict(row) for row in cursor.fetchall()]

    # Close the connection
    conn.close()

    # Write to JSON file
    with open('data/ai_tools.json', 'w', encoding='utf-8') as f:
        json.dump(resources, f, ensure_ascii=False, indent=2)

    print("JSON file generated successfully!")

if __name__ == '__main__':
    generate_json() 