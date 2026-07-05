from models.furniture import Furniture


def build_keywords(features: dict) -> list[str]:
    """
    Converts Vision JSON into a simple list of keywords
    used to search the knowledge base.
    """

    keywords = []

    if features.get("category") == "armchair":
        keywords.append("fotel")

    if features.get("category") == "chair":
        keywords.append("krzesło")

    if features.get("has_armrests"):
        keywords.append("podłokietniki")

    if features.get("wooden_frame"):
        keywords.append("drewn")

    if features.get("seat_type") == "upholstered":
        keywords.append("tapicer")

    if features.get("backrest_type") == "upholstered":
        keywords.append("oparcie")

    return keywords


def calculate_score(
    keywords: list[str],
    furniture: Furniture,
) -> int:

    score = 0

    text = furniture.search_features.lower()

    for keyword in keywords:

        if keyword.lower() in text:
            score += 1

    return score


def find_candidates(
    features: dict,
    furniture_list: list[Furniture],
    top_k: int = 5,
):

    keywords = build_keywords(features)

    results = []

    for furniture in furniture_list:

        score = calculate_score(
            keywords,
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