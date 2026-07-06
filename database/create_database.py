import sqlite3

connection = sqlite3.connect("database/prl_furniture.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS furniture")

cursor.execute("""
CREATE TABLE furniture (

    id INTEGER PRIMARY KEY,

    model TEXT NOT NULL,
    common_name TEXT,
    reference_id TEXT,

    designer TEXT,
    production_years TEXT,
    category TEXT,
    manufacturer TEXT,

    visual_features TEXT,
    construction_features TEXT,

    similar_models TEXT,
    model_family TEXT,

    sources TEXT,

    confidence REAL,

    search_features TEXT
)
""")

connection.commit()
connection.close()

print("Database created successfully!")