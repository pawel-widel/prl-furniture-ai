from pathlib import Path

from services.vision_service import extract_features

image_path = Path("photos/300-123/300-123_1.png")

with open(image_path, "rb") as image:
    features = extract_features(image)

print(features)