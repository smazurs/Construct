import sqlite3
from config import Config

def get_db_connection():
    return sqlite3.connect(Config.DATABASE_PATH)