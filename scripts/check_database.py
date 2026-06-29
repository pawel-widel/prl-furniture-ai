import sqlite3

connection = sqlite3.connect("database/prl_furniture.db")
cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM furniture")

count = cursor.fetchone()[0]

print(f"Furniture in database: {count}")

connection.close()