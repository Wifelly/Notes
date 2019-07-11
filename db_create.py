import sqlite3

conn = sqlite3.connect("db.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Notes (
                    id TEXT UUID PRIMARY KEY UNIQUE NOT NULL,
                    title TEXT NOT NULL,
                    text TEXT,
                    date_create INTEGER NOT NULL,
                    date_update INTEGER NOT NULL
                    );
               """)