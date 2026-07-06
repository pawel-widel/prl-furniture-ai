import database.database as db

from services.search_service import find_candidates
from services.vision_service import extract_features
from services.verification_service import verify_candidate


VERIFICATION_THRESHOLD = 0.90


def identify(uploaded_file):

    # ----------------------------------
    # Stage 1 - Vision
    # ----------------------------------

    features = extract_features(uploaded_file)

    # Vision przeczytał plik do końca.
    uploaded_file.seek(0)

    # ----------------------------------
    # Stage 2 - Search
    # ----------------------------------

    furniture = db.get_all_furniture()

    candidates = find_candidates(
        features,
        furniture,
    )

    # ----------------------------------
    # Stage 3 - Verification
    # ----------------------------------

    verification_results = []

    for candidate in candidates:

        furniture = candidate["furniture"]

        # Pomijamy modele bez zdjęć referencyjnych
        if not furniture.reference_id:
            continue

        result = verify_candidate(
            uploaded_file,
            furniture,
        )

        verification_results.append(
            {
                "furniture": furniture,
                "search_score": candidate["score"],
                "verification": result,
            }
        )

        if (
            result["match"]
            and result["confidence"] >= VERIFICATION_THRESHOLD
        ):

            return {
                "features": features,
                "winner": furniture,
                "verification": result,
                "candidates": candidates,
                "verification_results": verification_results,
            }

    # ----------------------------------
    # Fallback
    # ----------------------------------

    return {
        "features": features,
        "winner": candidates[0]["furniture"] if candidates else None,
        "verification": None,
        "candidates": candidates,
        "verification_results": verification_results,
    }