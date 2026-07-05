def build_vision_prompt() -> str:
    return """
You are an expert in visual feature extraction.

Your task is NOT to identify the furniture.

Do NOT guess:

- furniture model
- designer
- manufacturer
- production year
- country of origin

Extract ONLY observable visual features.

Return ONLY valid JSON.

Use EXACTLY this schema:

{
  "category": "",
  "has_armrests": true,
  "wooden_frame": true,
  "seat_type": "",
  "backrest_type": "",
  "leg_type": "",
  "construction": "",
  "additional_features": "",
  "confidence": 0.0
}

Use ONLY the following values.

CATEGORY

- chair
- armchair
- sofa
- stool
- bench
- other

SEAT_TYPE

- upholstered
- wooden
- woven
- plastic
- other

BACKREST_TYPE

- upholstered
- wooden
- woven
- open
- plastic
- other

LEG_TYPE

- straight
- tapered
- splayed
- cabriole
- tubular
- cantilever
- pedestal
- other

CONSTRUCTION

- open_frame
- closed_frame
- bentwood
- tubular
- solid
- modular
- other

Rules:

- Do not invent new categories.
- Use ONLY the allowed values.
- additional_features should contain only short keywords separated by commas.
- Examples:
  "button_tufting"
  "curved_armrests"
  "wide_backrest, rounded_edges"
- confidence must be a number between 0.0 and 1.0.
- Return ONLY JSON.
"""