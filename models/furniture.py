from dataclasses import dataclass


@dataclass
class Furniture:
    id: int
    model: str
    common_name: str
    designer: str
    production_years: str
    category: str
    manufacturer: str
    visual_features: str
    construction_features: str
    similar_models: str
    model_family: str
    sources: str
    confidence: float