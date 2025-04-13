# AI Tools Database

This repository contains scripts to manage an SQLite database of AI tools and serve them through a Cloudflare Worker.

## Setup

1. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Create the database and table:
   ```bash
   python setup_database.py
   ```

3. Import data from a CSV file:
   ```bash
   python import_data.py
   ```
   When prompted, enter the path to your CSV file.

4. Generate the JSON file for the Cloudflare Worker:
   ```bash
   python generate_json.py
   ```

5. Commit and push the changes to GitHub:
   ```bash
   git add data/ai_tools.json
   git commit -m "Update AI tools data"
   git push origin main
   ```

The Cloudflare Worker will automatically fetch the latest data from the JSON file in the repository.

## Database Structure

The `ai_resources` table has the following columns:
- id (INTEGER, PRIMARY KEY)
- name (TEXT, NOT NULL)
- description (TEXT)
- url (TEXT)
- category (TEXT)
- pricing (TEXT)
- regulations (TEXT)
- use_case (TEXT)
- industries (TEXT)
- created_at (TIMESTAMP)

## Workflow

1. Make changes to the SQLite database locally
2. Run `generate_json.py` to create/update the JSON file
3. Commit and push the changes to GitHub
4. The Cloudflare Worker will automatically serve the latest data
