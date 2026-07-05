import os
import json
import base64

from dotenv import load_dotenv
from openai import OpenAI

from services.vision_prompt import build_vision_prompt

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def extract_features(uploaded_file) -> dict:

    image_bytes = uploaded_file.read()

    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    response = client.responses.create(
        model="gpt-5.5",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": build_vision_prompt(),
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/png;base64,{image_base64}",
                    },
                ],
            }
        ],
    )

    return json.loads(response.output_text)