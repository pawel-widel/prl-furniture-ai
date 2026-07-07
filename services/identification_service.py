import json

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

    print("\n" + "=" * 60)
    print("VISION FEATURES")
    print("=" * 60)
    print(json.dumps(features, indent=2))
    print("=" * 60 + "\n")

    uploaded_file.seek(0)

    # ----------------------------------
    # Stage 2 - Database
    # ----------------------------------

    furniture = db.get_all_furniture()

    print("=" * 60)
    print("DATABASE")
    print("=" * 60)

    print(f"Furniture loaded: {len(furniture)}")
    print(f"Type: {type(furniture)}")

    if furniture:
        print(f"First object type: {type(furniture[0])}")

    for item in furniture:
        print(
            f"{item.model} | "
            f"reference_id={item.reference_id}"
        )

    print("=" * 60 + "\n")

    # ----------------------------------
    # Stage 3 - Search
    # ----------------------------------

    candidates = find_candidates(
        features,
        furniture,
    )

    print("=" * 60)
    print("SEARCH RESULTS")
    print("=" * 60)

    print(f"Candidates found: {len(candidates)}")

    for candidate in candidates:

        print(
            f"{candidate['furniture'].model:<25}"
            f" Score: {candidate['score']}"
        )

    print("=" * 60 + "\n")

    # ----------------------------------
    # Stage 4 - Verification
    # ----------------------------------

    verification_results = []

    for candidate in candidates:

        furniture = candidate["furniture"]

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