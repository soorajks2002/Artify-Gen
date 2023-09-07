import openai
import re
from api_key import open_ai_api_key

openai.api_key = open_ai_api_key


def extract_sentences(input_text):
    # Split the input text into sentences based on both "\n\n" and "\n"
    sentences = re.split(r'(\n\n|\n)', input_text)

    # Remove leading numbers and periods from sentences
    sentences = [re.sub(r'^\d+\.\s*', '', sentence.strip())
                 for sentence in sentences if sentence.strip()]

    return sentences


def generate_prompt(style, keywords):

    prompt = '''write 3 short, simple and {style} art like image prompt for a diffusion based image generation model using these words {keywords}'''

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user","content": '''write 3 short and simple digital art like image prompt for a diffusion based image generation model using these words ["kids", "healthy food", "cereal"]'''},
            {"role": "assistant", "content": '''Create a digital artwork that portrays kids in a colorful, abstract world made entirely of vibrant, oversized cereal pieces and nutritious ingredients.\n Craft a digital painting of children happily engaged in a friendly cereal eating competition, showcasing their enjoyment of wholesome, nutritious breakfast choices.\n Design a digital art scene where kids embark on a magical adventure inside a cereal box, discovering a miniature universe filled with talking cereal characters and fantastical landscapes made of healthy food.'''},
            {"role": "user","content": '''write 3 short and simple anime art like image prompt for a diffusion based image generation model using these words ["ramen shop", "humans", "enjoying food"]'''},
            {"role": "assistant", "content": '''An anime scene depicting a bustling ramen shop filled with humans savoring steaming bowls of ramen, their faces lit up with joy as they enjoy every slurp of the delicious noodles.\n Create an anime-style illustration of a group of friends sitting at a cozy ramen shop, bonding over their shared love for food, with warm smiles and animated expressions as they savor the flavors.\n An anime artwork showcasing a skilled ramen chef preparing a bowl with precision and passion, while the patrons, a diverse group of humans, eagerly watch in anticipation, ready to enjoy their perfectly crafted meals.'''},
            {"role": "user", "content": prompt.format(
                keywords=keywords, style=style)}
        ]
    )

    generated_sentences = response["choices"][0]["message"]["content"]

    return extract_sentences(generated_sentences)