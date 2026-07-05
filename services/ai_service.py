import os
import base64

from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
    
)
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
    
def analyze_image(uploaded_file, prompt):

    image_bytes = uploaded_file.read()
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    content = [
        {
            "type": "input_text",
            "text": prompt,
        },
        {
            "type": "input_image",
            "image_url": f"data:image/png;base64,{image_base64}",
        },
    ]
    photos_root = Path("photos")

    for model_folder in sorted(photos_root.iterdir()):

      if not model_folder.is_dir():
        continue

    content.append(
        {
            "type": "input_text",
            "text": f"REFERENCE MODEL: {model_folder.name}"
        }
    )

    for image_path in sorted(model_folder.iterdir()):

        if image_path.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
            continue

        encoded = encode_image(image_path)

        content.append(
            {
                "type": "input_image",
                "image_url": f"data:image/jpeg;base64,{encoded}"
            }
        )


    response = client.responses.create(
    model="gpt-5.5",
    input=[
    {
        "role": "user",
        "content": content,
    }
]
)
    return response.output_text