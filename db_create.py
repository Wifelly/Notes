import sqlite3

conn = sqlite3.connect("db.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    title TEXT NOT NULL,
                    text TEXT UNIQUE,
                    “date_create” TEXT UNIQUE,
                    “date_update” TEXT NOT NULL
                    );
               """)