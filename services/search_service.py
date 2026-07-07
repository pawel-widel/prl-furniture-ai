from models.furniture import Furniture

from services.hard_filters import apply_hard_filters


FEATURE_KEYWORDS = {

    "construction": {
        "open_frame": [
            "open frame",
            "exposed wooden structure",
        ],
        "rounded_shell": [
            "rounded shell",
            "shell construction",
            "bucket shell",
        ],
    },

    "armrest_shape": {
        "flat_plank": [
            "flat plank armrests",
            "wide wooden armrests",
        ],
        "round_dowel": [
            "rounded wooden armrests",
            "round dowel armrests",
        ],
        "integrated_shell": [
            "integrated armrests",
        ],
    },

    "backrest_shape": {
        "rounded_rectangle": [
            "rounded rectangular backrest",
        ],
        "rectangular": [
            "rectangular backrest",
        ],
        "bucket": [
            "bucket backrest",
            "rounded shell",
        ],
    },

    "frame_geometry": {
        "a_frame": [
            "a-frame side construction",
            "triangular side frame",
        ],
        "rectangular_frame": [
            "rectangular side frame",
        ],
        "shell": [
            "shell construction",
        ],
    },

    "front_support": {
        "angled": [
            "angled front support",
        ],
        "vertical": [
            "vertical front support",
        ],
    },

    "additional_features": {

        "button_tufting": [
            "button tufting",
        ],

        "angled_backrest": [
            "slightly reclined backrest",
            "angled backrest",
        ],

        "tapered_legs": [
            "tapered wooden legs",
        ],

        "splayed_legs": [
            "splayed legs",
        ],

        "open_frame": [
            "open frame",
            "open space under seat",
            "exposed wooden structure",
        ],

        "rounded_edges": [
            "organic armrest shape",
            "rounded edges",
        ],
    },
}


def contains_any(text: str, keywords: list[str]) -> bool:

    text = text.lower()

    return any(
        keyword.lower() in text
        for keyword in keywords
    )


def calculate_score(
    features: dict,
    furniture: Furniture,
) -> int:

    text = furniture.search_features.lower()

    score = 0

    # --------------------------------------------------
    # CATEGORY
    # --------------------------------------------------

    if (
        features.get("category") == "armchair"
        and "armchair" in text
    ):
        score += 5

    if (
        features.get("category") == "chair"
        and "chair" in text
    ):
        score += 5

    # --------------------------------------------------
    # ARMRESTS
    # --------------------------------------------------

    if (
        features.get("has_armrests")
        and "armrests" in text
    ):
        score += 3

    # --------------------------------------------------
    # MATERIAL
    # --------------------------------------------------

    if features.get("wooden_frame"):

        if contains_any(
            text,
            [
                "wooden frame",
                "wooden structure",
                "exposed wooden structure",
            ],
        ):
            score += 5

    else:

        if contains_any(
            text,
            [
                "metal frame",
                "steel frame",
                "steel structure",
            ],
        ):
            score += 5

    # --------------------------------------------------
    # SEAT
    # --------------------------------------------------

    if (
        features.get("seat_type") == "upholstered"
        and "upholstered" in text
    ):
        score += 2

    # --------------------------------------------------
    # BACKREST
    # --------------------------------------------------

    if (
        features.get("backrest_type") == "upholstered"
        and "backrest" in text
    ):
        score += 2

    # --------------------------------------------------
    # CONSTRUCTION
    # --------------------------------------------------

    construction = features.get("construction")

    if construction in FEATURE_KEYWORDS["construction"]:

        if contains_any(
            text,
            FEATURE_KEYWORDS["construction"][construction],
        ):
            score += 6

    # --------------------------------------------------
    # ARMREST SHAPE
    # --------------------------------------------------

    armrest = features.get("armrest_shape")

    if armrest in FEATURE_KEYWORDS["armrest_shape"]:

        if contains_any(
            text,
            FEATURE_KEYWORDS["armrest_shape"][armrest],
        ):
            score += 6

    # --------------------------------------------------
    # BACKREST SHAPE
    # --------------------------------------------------

    backrest = features.get("backrest_shape")

    if backrest in FEATURE_KEYWORDS["backrest_shape"]:

        if contains_any(
            text,
            FEATURE_KEYWORDS["backrest_shape"][backrest],
        ):
            score += 5

    # --------------------------------------------------
    # FRAME GEOMETRY
    # --------------------------------------------------

    geometry = features.get("frame_geometry")

    if geometry in FEATURE_KEYWORDS["frame_geometry"]:

        if contains_any(
            text,
            FEATURE_KEYWORDS["frame_geometry"][geometry],
        ):
            score += 7

    # --------------------------------------------------
    # FRONT SUPPORT
    # --------------------------------------------------

    support = features.get("front_support")

    if support in FEATURE_KEYWORDS["front_support"]:

        if contains_any(
            text,
            FEATURE_KEYWORDS["front_support"][support],
        ):
            score += 5

    # --------------------------------------------------
    # LOWER STRETCHER
    # --------------------------------------------------

    if features.get("lower_stretcher"):

        if contains_any(
            text,
            [
                "floating seat",
                "open space under seat",
            ],
        ):
            score += 5

    # --------------------------------------------------
    # ADDITIONAL FEATURES
    # --------------------------------------------------

    extra = features.get("additional_features", "")

    if isinstance(extra, str):

        for tag in extra.split(","):

            tag = tag.strip()

            if tag not in FEATURE_KEYWORDS["additional_features"]:
                continue

            if contains_any(
                text,
                FEATURE_KEYWORDS["additional_features"][tag],
            ):
                score += 4

    return score


def find_candidates(
    features: dict,
    furniture_list: list[Furniture],
    top_k: int = 5,
):

    results = []

    for furniture in furniture_list:

        score = calculate_score(
            features,
            furniture,
        )

        score = apply_hard_filters(
            score,
            features,
            furniture,
        )

        results.append(
            {
                "furniture": furniture,
                "score": score,
            }
        )

    results.sort(
        key=lambda item: item["score"],
        reverse=True,
    )

    return results[:top_k]