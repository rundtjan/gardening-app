import os
import sqlite3

def get_db_connection():
    dirname = os.path.dirname(__file__)
    conn = sqlite3.connect(os.path.join(dirname, "..", "data", "db.sqlite"))
    conn.row_factory = sqlite3.Row
    return conn
    