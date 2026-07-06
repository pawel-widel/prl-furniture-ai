from openpyxl import load_workbook
import sqlite3


connection = sqlite3.connect("database/prl_furniture.db")
cursor = connection.cursor()


workbook = load_workbook(
    "data/furniture.xlsx",
    data_only=True,
)

sheet = workbook["Katalog"]


cursor.execute("DELETE FROM furniture")


for row in sheet.iter_rows(min_row=2, values_only=True):

    (
        _,
        model,
        common_name,
        reference_id,
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
            reference_id,

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

            search_features

        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            model,
            common_name,
            reference_id,

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