import sqlite3
from models.furniture import Furniture


def get_all_furniture():

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
    designer=row[3],
    production_years=row[4],
    category=row[5],
    manufacturer=row[6],
    visual_features=row[7],
    construction_features=row[8],
    similar_models=row[9],
    model_family=row[10],
    sources=row[11],
    confidence=row[12]
)
        )

  
    return furniture