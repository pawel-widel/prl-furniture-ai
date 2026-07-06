import sqlite3

from models.furniture import Furniture


def get_all_furniture() -> list[Furniture]:

    connection = sqlite3.connect("database/prl_furniture.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM furniture")
    rows = cursor.fetchall()

    connection.close()

    furniture = []

    for row in rows:

        furniture.append(
            Furniture(
                id=row[0],
                model=row[1],
                common_name=row[2],
                reference_id=row[3],
                designer=row[4],
                production_years=row[5],
                category=row[6],
                manufacturer=row[7],
                visual_features=row[8],
                construction_features=row[9],
                similar_models=row[10],
                model_family=row[11],
                sources=row[12],
                confidence=row[13],
                search_features=row[14],
            )
        )

    return furniture