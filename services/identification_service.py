import database.database as db

from services.prompt_builder import build_prompt
from services.ai_service import analyze_image


def identify(uploaded_file):

    furniture = db.get_all_furniture()

    prompt = build_prompt(furniture)

    result = analyze_image(
        uploaded_file,
        prompt,
    )

    return result