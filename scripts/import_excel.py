from openpyxl import load_workbook
import sqlite3


# Connect to SQLite database
connection = sqlite3.connect("database/prl_furniture.db")
cursor = connection.cursor()

# Load Excel workbook
workbook = load_workbook(
    "data/furniture.xlsx",
    data_only=True,
)
sheet = workbook["Katalog"]

# Clear existing data
cursor.execute("DELETE FROM furniture")

# Import rows
for row in sheet.iter_rows(min_row=2, values_only=True):

    (
        _,
        model,
        common_name,
        designer,
        production_years,
        category,
        manufacturer,
        visual_features,
        construction_features,
        similar_models,
        model_family,
        sources,
        confidence,
        search_features,
    ) = row

    cursor.execute(
        """
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
            confidence,
            search_features
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            model,
            common_name,
            designer,
            production_years,
            category,
            manufacturer,
            visual_features,
            construction_features,
            similar_models,
            model_family,
            sources,
            confidence,
            search_features,
        ),
    )

connection.commit()
connection.close()

print("Furniture imported successfully.")