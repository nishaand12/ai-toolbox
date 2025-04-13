import sqlite3
import csv
import os

def import_from_csv(csv_file):
    # Connect to SQLite database
    conn = sqlite3.connect('data/ai_tools.db')
    cursor = conn.cursor()

    # Read the CSV file
    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        
        # Prepare the insert statement
        columns = ['name', 'description', 'url', 'category', 'pricing', 'regulations', 'use_case', 'industries']
        placeholders = ', '.join(['?' for _ in columns])
        insert_query = f"INSERT INTO ai_resources ({', '.join(columns)}) VALUES ({placeholders})"
        
        # Insert each row
        for row in csv_reader:
            values = [row.get(col, '') for col in columns]
            cursor.execute(insert_query, values)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print(f"Data imported successfully from {csv_file}!")

if __name__ == "__main__":
    csv_file = "ai_resources_rows.csv"
    if os.path.exists(csv_file):
        import_from_csv(csv_file)
    else:
        print(f"Error: File {csv_file} not found!") 