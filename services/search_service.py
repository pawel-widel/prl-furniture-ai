from models.furniture import Furniture

from services.hard_filters import apply_hard_filters


FEATURE_KEYWORDS = {

    "construction": {

        "open_frame": [
            "open wooden side frame",
            "open wooden frame",
            "open frame",
            "open structural frame",
            "open frame construction",
            "open space under seat",
            "exposed wooden structure",
        ],

        "closed_frame": [
            "closed lower frame",
            "closed upholstered body",
            "closed upholstered back",
            "one piece body",
            "one_piece_body",
        ],

        "bentwood": [
            "bentwood frame construction",
            "bentwood",
        ],

        "tubular": [
            "metal frame",
            "steel frame",
            "tubular legs",
            "tubular frame",
        ],

        "solid": [
            "solid wooden frame",
            "solid construction",
            "solid upholstered plinth",
        ],

        "modular": [
            "modular construction",
        ],
    },

    "armrest_shape": {

        "flat_plank": [
            "flat plank armrests",
            "flat wooden armrests",
            "flat armrests",
            "wide wooden armrests",
            "rectangular wooden armrests",
            "paddle-shaped armrests",
        ],

        "round_dowel": [
            "rounded wooden armrests",
            "round profile wooden rails",
            "round dowel armrests",
        ],

        "curved_wood": [
            "curved wooden armrests",
            "curved armrests",
            "sloping armrests",
        ],

        "integrated_shell": [
            "integrated shell",
            "integrated armrests",
            "continuous armrests",
            "continuous_armrests",
            "wrapped armrests",
            "wrapped_armrests",
        ],
    },

    "backrest_shape": {

        "rounded_rectangle": [
            "rounded rectangular backrest",
            "rounded backrest corners",
        ],

        "rectangular": [
            "rectangular backrest",
            "tall rectangular backrest",
        ],

        "bucket": [
            "bucket seat",
            "bucket_seat",
            "rounded shell",
            "wide rounded backrest",
            "wide_rounded_backrest",
            "rounded top backrest",
            "rounded_top_backrest",
        ],

        "winged": [
            "wing shaped backrest",
            "flared upper collar",
        ],

        "trapezoid": [
            "trapezoidal backrest",
            "tapered rectangular backrest",
        ],
    },

    "frame_geometry": {

        "a_frame": [
            "a-frame side construction",
            "inverted v-frame side construction",
        ],

        "rectangular_frame": [
            "rectangular side frame",
            "straight side rails",
        ],

        "triangular_frame": [
            "triangular side frame",
            "triangular side geometry",
        ],

        "shell": [
            "rounded shell",
            "rounded_shell",
            "integrated shell",
            "integrated_shell",
            "floating shell",
            "floating_shell",
            "upholstered shell",
            "upholstered_shell",
            "organic shell silhouette",
        ],

        "cantilever": [
            "cantilever frame",
        ],
    },

    "front_support": {

        "angled": [
            "angled front support",
            "angled support",
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
            "straight tapered legs",
            "tapered legs",
        ],

        "splayed_legs": [
            "splayed legs",
            "splayed tapered legs",
            "slightly splayed legs",
            "slightly_splayed_legs",
        ],

        "open_frame": [
            "open wooden side frame",
            "open wooden frame",
            "open frame",
            "open space under seat",
        ],

        "rounded_edges": [
            "rounded edges",
            "rounded backrest corners",
            "organic shape",
            "organic_shape",
        ],

        "flat_armrests": [
            "flat plank armrests",
            "flat wooden armrests",
        ],

        "curved_armrests": [
            "curved armrests",
            "wrapped armrests",
            "wrapped_armrests",
        ],

        "wide_backrest": [
            "wide backrest",
            "wide rounded backrest",
            "wide_rounded_backrest",
            "high rounded backrest",
        ],

        "side_stretcher": [
            "side stretcher",
            "lower side stretcher",
        ],

        "visible_bolts": [
            "visible side bolts",
            "visible screw joints",
            "visible side screws",
            "visible rear bolts",
        ],

        "floating_seat": [
            "floating seat",
            "floating seat appearance",
            "floating upholstered seat",
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
                "solid wooden frame",
                "exposed wooden structure",
                "visible wooden side rails",
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
                "tubular frame",
                "metal legs",
            ],
        ):
            score += 5

    # --------------------------------------------------
    # SEAT
    # --------------------------------------------------

    seat_type = features.get("seat_type")

    if seat_type == "upholstered":

        if "upholstered" in text:
            score += 2

    elif seat_type == "plastic":

        if contains_any(
            text,
            [
                "plastic",
                "shell",
                "composite",
                "molded",
            ],
        ):
            score += 6

    # --------------------------------------------------
    # BACKREST
    # --------------------------------------------------

    backrest_type = features.get("backrest_type")

    if backrest_type == "upholstered":

        if "backrest" in text:
            score += 2

    elif backrest_type == "plastic":

        if contains_any(
            text,
            [
                "plastic",
                "shell",
                "composite",
                "molded",
            ],
        ):
            score += 6

    # --------------------------------------------------
    # CONSTRUCTION
    # --------------------------------------------------

    construction = features.get("construction")

    if construction in FEATURE_KEYWORDS["construction"]:

        if contains_any(
            text,
            FEATURE_KEYWORDS["construction"][construction],
        ):

            if construction == "closed_frame":
                score += 8
            else:
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

            if armrest == "integrated_shell":
                score += 10
            else:
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

            if backrest == "bucket":
                score += 9
            else:
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

            if geometry == "shell":
                score += 12
            else:
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
                "floating seat appearance",
                "open space under seat",
                "lower stretcher",
                "side stretcher",
            ],
        ):
            score += 5

    # --------------------------------------------------
    # ADDITIONAL FEATURES
    # --------------------------------------------------

    extra = features.get(
        "additional_features",
        "",
    )

    if isinstance(
        extra,
        str,
    ):

        for tag in extra.split(","):

            tag = tag.strip()

            if (
                tag
                not in FEATURE_KEYWORDS[
                    "additional_features"
                ]
            ):
                continue

            if contains_any(
                text,
                FEATURE_KEYWORDS[
                    "additional_features"
                ][tag],
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