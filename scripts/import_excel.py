from openpyxl import load_workbook
import sqlite3

# Otwórz bazę danych
conn = sqlite3.connect("database/prl_furniture.db")
cursor = conn.cursor()

# Otwórz Excel
workbook = load_workbook("data/furniture.xlsx")
sheet = workbook["Katalog"]
cursor.execute("DELETE FROM furniture")

# Pomiń pierwszy wiersz (nagłówki)
for row in sheet.iter_rows(min_row=2, values_only=True):

    _, model, common_name, designer, year, type_, manufacturer, characteristics, construction, confused_with, family, sources, confidence = row

    cursor.execute("""
        INSERT INTO furniture (
            model,
            common_name,
            designer,
            year,
            type,
            manufacturer,
            characteristics,
            construction,
            confused_with,
            family,
            sources,
            confidence
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        model,
        common_name,
        designer,
        year,
        type_,
        manufacturer,
        characteristics,
        construction,
        confused_with,
        family,
        sources,
        confidence
    ))

conn.commit()
conn.close()

print("Furniture imported successfully!")

...

# tutaj Twój obecny kod importu

print("\n===== HEADERS =====")

headers = [cell.value for cell in sheet[1]]

for i, header in enumerate(headers):
    print(i, header)

print("\n===== FIRST ROW =====")

first = next(sheet.iter_rows(min_row=2, values_only=True))

for i, value in enumerate(first):
    print(i, value)