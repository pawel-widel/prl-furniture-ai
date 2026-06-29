from models.furniture import Furniture


def build_prompt(furniture_list: list[Furniture]) -> str:

    prompt = """
You are an expert in Polish PRL furniture.

Your task is to identify furniture ONLY from the knowledge base below.

If nothing matches, answer:
UNKNOWN

Knowledge base:

"""

    for furniture in furniture_list:

        prompt += f"""
--------------------------------

Official model:
{furniture.model}

Common name:
{furniture.common_name}

Designer:
{furniture.designer}

Manufacturer:
{furniture.manufacturer}

Category:
{furniture.category}

Visual features:
{furniture.visual_features}

Construction:
{furniture.construction_features}

Often confused with:
{furniture.similar_models}

Model family:
{furniture.model_family}

"""

    return prompt