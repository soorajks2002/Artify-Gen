import requests
from api_key import hugging_face_api_key
import io
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"Bearer {hugging_face_api_key}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

def generate_image (prompt) :
    image_bytes = query({"inputs": prompt})
    image = Image.open(io.BytesIO(image_bytes))
    return image