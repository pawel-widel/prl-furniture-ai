from models.furniture import Furniture


def build_prompt(furniture_list: list[Furniture]) -> str:

    prompt = """
You are performing a visual verification task.

This is NOT an identification task.

Ignore your own knowledge about furniture, designers, manufacturers,
countries of origin and historical styles.

You MUST use ONLY the images provided in this request.

----------------------------------------

Image #1

This is the QUERY image uploaded by the user.

----------------------------------------

All remaining images

These are REFERENCE images.

All reference images show the SAME furniture model photographed from
different angles.

Your task is ONLY to determine whether the furniture shown in Image #1
is the SAME physical design as the furniture shown in the reference images.

Compare ONLY visible geometry.

Pay attention to:

- proportions
- silhouette
- frame construction
- armrests
- legs
- seat shape
- backrest shape
- visible wooden elements
- upholstery geometry
- connection points
- angles
- overall construction

Ignore:

- upholstery color
- wood color
- fabric
- lighting
- camera angle
- background
- restoration differences
- wear
- production year

----------------------------------------

Answer ONLY in this format:

MATCH: YES

or

MATCH: NO

Reason:
(maximum 3 short sentences explaining the visual comparison)

Do NOT identify the furniture.

Do NOT guess the model.

Do NOT use your own knowledge.

Only compare the images.

"""

    for furniture in furniture_list:

        prompt += f"""
--------------------------------

MODEL:
{furniture.model}

COMMON NAME:
{furniture.common_name}

DESIGNER:
{furniture.designer}

MANUFACTURER:
{furniture.manufacturer}

CATEGORY:
{furniture.category}

VISUAL FEATURES:
{furniture.visual_features}

CONSTRUCTION:
{furniture.construction_features}

SIMILAR MODELS:
{furniture.similar_models}

MODEL FAMILY:
{furniture.model_family}

"""

    return prompt