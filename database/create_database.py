import sqlite3

connection = sqlite3.connect("database/prl_furniture.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS furniture")

cursor.execute("""
CREATE TABLE furniture (

    id INTEGER PRIMARY KEY,

    model TEXT NOT NULL,
    common_name TEXT,
    designer TEXT,
    year TEXT,
    type TEXT,
    manufacturer TEXT,

    characteristics TEXT,
    construction TEXT,

    confused_with TEXT,
    family TEXT,

    sources TEXT,

    confidence REAL,

    search_features TEXT
)
""")

connection.commit()
connection.close()

print("Database created successfully!")