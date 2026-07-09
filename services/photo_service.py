from pathlib import Path


PHOTOS_DIR = Path("photos")


def get_reference_images(reference_id: str | None) -> list[Path]:
    """
    Returns all reference images for a furniture model.

    Expected structure:

    photos/
        366/
            winner.jpg
            front.jpg
            side.jpg
            back.jpg
    """

    if not reference_id:
        return []

    model_dir = PHOTOS_DIR / reference_id

    if not model_dir.exists():
        return []

    images = []

    for extension in ("*.jpg", "*.jpeg", "*.png", "*.webp"):

        images.extend(model_dir.glob(extension))

    images.sort()

    return images


def get_main_reference_image(reference_id: str | None) -> Path | None:
    """
    Returns the preferred image for display.

    Priority:

    1. winner.*
    2. front.*
    3. first available image
    """

    if not reference_id:
        return None

    model_dir = PHOTOS_DIR / reference_id

    if not model_dir.exists():
        return None

    preferred_images = [

        # Winner
        model_dir / "winner.jpg",
        model_dir / "winner.jpeg",
        model_dir / "winner.png",
        model_dir / "winner.webp",

        # Front
        model_dir / "front.jpg",
        model_dir / "front.jpeg",
        model_dir / "front.png",
        model_dir / "front.webp",
    ]

    for image in preferred_images:

        if image.exists():
            return image

    images = get_reference_images(reference_id)

    if images:
        return images[0]

    return None