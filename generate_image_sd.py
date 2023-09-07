import requests
from api_key import hugging_face_api_key
import io
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
# API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
# API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-refiner-1.0"

headers = {"Authorization": f"Bearer {hugging_face_api_key}"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response


def generate_image(prompt):
    image_bytes = query({"inputs": prompt})

    if image_bytes.status_code == 200 :
        return {"image_generated":True, "image":Image.open(io.BytesIO(image_bytes.content))}

    return {"image_generated":False}