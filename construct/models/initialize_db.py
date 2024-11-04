import sqlite3
from config import Config

def initialize_database():
    conn = sqlite3.connect(Config.DATABASE_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS User (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Project (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            name TEXT NOT NULL,
            location TEXT,
            timeline TEXT,
            FOREIGN KEY (user_id) REFERENCES User(id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cost (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER,
            material_cost REAL,
            labor_cost REAL,
            equipment_cost REAL,
            FOREIGN KEY (project_id) REFERENCES Project(id)
        )
    ''')

    conn.commit()
    conn.close()