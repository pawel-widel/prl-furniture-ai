from models.furniture import Furniture


FEATURE_TRANSLATIONS = {

    "rounded_shell": [
        "muszel",
        "kubeł",
        "skorup",
        "zaokrąglone oparcie",
        "jednolita tapicerowana bryła",
    ],

    "integrated_armrests": [
        "muszel",
        "kubeł",
        "zintegrowane podłokietniki",
    ],

    "flat_armrests": [
        "płaskie drewniane podłokietniki",
        "płaskie podłokietniki",
    ],

    "curved_armrests": [
        "gięte drewniane podłokietniki",
        "gięte podłokietniki",
    ],

    "button_tufting": [
        "guziki",
        "pikowanie",
    ],

    "angled_backrest": [
        "pochylone oparcie",
        "lekko odchylone oparcie",
    ],

    "angled_legs": [
        "skośnie rozstawione nogi",
        "zwężające się ku dołowi nogi",
        "smukłe metalowe nogi",
        "smukłe nogi",
    ],

    "exposed_wood_frame": [
        "odsłonięta drewniana konstrukcja",
        "widoczne elementy drewniane",
        "drewniana rama",
        "otwarta konstrukcja",
        "drewniany stelaż",
    ],

    "open_frame": [
        "otwarta konstrukcja",
        "duży prześwit",
    ],
}


def calculate_score(
    features: dict,
    furniture: Furniture,
) -> int:

    text = furniture.search_features.lower()

    score = 0

    # ---------- CATEGORY ----------

    if features.get("category") == "armchair":
        if "fotel" in text:
            score += 5

    if features.get("category") == "chair":
        if "krzesło" in text:
            score += 5

    # ---------- ARMRESTS ----------

    if features.get("has_armrests"):
        if "podłokiet" in text:
            score += 3

    # ---------- WOOD ----------

    if features.get("wooden_frame"):

        if "drewn" in text or "buk" in text:
            score += 4

    else:

        if "metal" in text or "stal" in text:
            score += 4

        if "drewn" in text:
            score -= 2

    # ---------- SEAT ----------

    if features.get("seat_type") == "upholstered":

        if "tapicer" in text:
            score += 2

    # ---------- BACKREST ----------

    if features.get("backrest_type") == "upholstered":

        if "oparcie" in text:
            score += 2

    # ---------- CONSTRUCTION ----------

    construction = features.get("construction")

    if construction in FEATURE_TRANSLATIONS:

        for keyword in FEATURE_TRANSLATIONS[construction]:

            if keyword.lower() in text:
                score += 4

    # ---------- EXTRA FEATURES ----------

    extra = features.get("additional_features", "")

    if isinstance(extra, str):

        for tag in extra.split(","):

            tag = tag.strip()

            if tag not in FEATURE_TRANSLATIONS:
                continue

            for keyword in FEATURE_TRANSLATIONS[tag]:

                if keyword.lower() in text:
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