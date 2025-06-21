# db.py (Place this inside your project folder)
import sqlite3
from datetime import datetime

# Initialize or connect to SQLite database
def init_db():
    conn = sqlite3.connect("health_predictions.db")
    c = conn.cursor()
    
    # Create a table to log predictions
    c.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            disease TEXT,
            inputs TEXT,
            result TEXT,
            timestamp TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

# Insert prediction record
def store_prediction(disease, inputs, result):
    conn = sqlite3.connect("health_predictions.db")
    c = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO predictions (disease, inputs, result, timestamp) VALUES (?, ?, ?, ?)",
              (disease, str(inputs), result, timestamp))
    conn.commit()
    conn.close()

# Fetch all records (for admin panel or dashboard)
def fetch_all_predictions():
    conn = sqlite3.connect("health_predictions.db")
    c = conn.cursor()
    c.execute("SELECT * FROM predictions")
    data = c.fetchall()
    conn.close()
    return data

# Initialize the DB when module is imported
init_db()