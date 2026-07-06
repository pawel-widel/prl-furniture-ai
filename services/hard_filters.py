from models.furniture import Furniture


def apply_hard_filters(
    score: int,
    features: dict,
    furniture: Furniture,
) -> int:

    text = furniture.search_features.lower()

    # -----------------------------------------
    # WOODEN FRAME
    # -----------------------------------------

    if features.get("wooden_frame"):

        if "metal" in text or "stal" in text:
            score -= 5

    else:

        if "drewn" in text or "buk" in text:
            score -= 5

    return score