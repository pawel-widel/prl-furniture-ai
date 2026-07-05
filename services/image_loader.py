from pathlib import Path


PHOTOS_DIR = Path("photos")


def get_reference_images(model_name: str) -> list[Path]:
    """
    Returns all reference images for a given furniture model.
    """

    model_folder = PHOTOS_DIR / model_name

    if not model_folder.exists():
        return []

    images = []

    for extension in ("*.png", "*.jpg", "*.jpeg", "*.webp"):
        images.extend(model_folder.glob(extension))

    return sorted(images)