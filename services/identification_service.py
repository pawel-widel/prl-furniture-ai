import database.database as db

from services.search_service import find_candidates
from services.vision_service import extract_features


def identify(uploaded_file):

    # Stage 1
    features = extract_features(uploaded_file)

    # Stage 2
    furniture = db.get_all_furniture()

    candidates = find_candidates(
        features,
        furniture,
    )

    return {
        "features": features,
        "candidates": candidates,
    }