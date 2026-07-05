import base64
import os

from dotenv import load_dotenv
from openai import OpenAI

from services.image_loader import get_reference_images

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def encode_image(image_path):

    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def build_prompt():

    return """
You are performing a visual verification task.

This is NOT an identification task.

Image #1 is the user photo.

All remaining images are reference images of ONE furniture model.

Determine ONLY whether the furniture shown in Image #1
is the SAME design as the reference images.

Compare ONLY:

- silhouette
- proportions
- frame construction
- armrests
- legs
- seat
- backrest

Ignore:

- upholstery colour
- wood colour
- fabric
- lighting
- background
- restoration
- production year

Return ONLY this JSON:

{
    "match": true,
    "confidence": 0.95,
    "reason": "One short sentence."
}
"""
    

def verify_candidate(
    uploaded_file,
    furniture,
):

    image_bytes = uploaded_file.read()
    uploaded_file.seek(0)

    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    content = [
        {
            "type": "input_text",
            "text": build_prompt(),
        },
        {
            "type": "input_image",
            "image_url": f"data:image/png;base64,{image_base64}",
        },
    ]

    reference_images = get_reference_images(
        furniture.model
    )

    for image_path in reference_images:

        encoded = encode_image(image_path)

        content.append(
            {
                "type": "input_image",
                "image_url": f"data:image/jpeg;base64,{encoded}",
            }
        )

    response = client.responses.create(
        model="gpt-5.5",
        input=[
            {
                "role": "user",
                "content": content,
            }
        ],
    )

    return response.output_text