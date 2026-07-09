from PIL import Image


IMAGE_SIZE = (420, 420)


def prepare_image(image) -> Image.Image:
    """
    Crops image to a centered square and resizes it.

    Used to keep all photos displayed
    with identical dimensions.
    """

    if not isinstance(image, Image.Image):
        image = Image.open(image)

    width, height = image.size

    side = min(width, height)

    left = (width - side) // 2
    top = (height - side) // 2
    right = left + side
    bottom = top + side

    image = image.crop(
        (
            left,
            top,
            right,
            bottom,
        )
    )

    image = image.resize(
        IMAGE_SIZE,
        Image.LANCZOS,
    )

    return image