import openai
import requests
from PIL import Image
import io
from api_key import open_ai_api_key

openai.api_key = open_ai_api_key

def get_image_url(prompt) :
    response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="512x512"
                # size="1024x1024"
                )
    return response

def generate_image(prompt) :
    
    dalle_response = get_image_url(prompt)
    image_url = dalle_response['data'][0]['url']  
                
    image_response = requests.get(image_url)
    image = Image.open(io.BytesIO(image_response.content))
    
    return {"image_generated":True, "image":image}