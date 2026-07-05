import database.database as db

from services.search_service import find_candidates


features = {
    "category": "armchair",
    "has_armrests": True,
    "wooden_frame": True,
    "seat_type": "upholstered",
    "backrest_type": "upholstered",
    "construction": "open_frame",
}

furniture = db.get_all_furniture()

results = find_candidates(
    features,
    furniture,
)

print()

print("===== SEARCH RESULTS =====")

print()

for result in results:

    print(
        f"{result['furniture'].model:<20} Score: {result['score']}"
    )