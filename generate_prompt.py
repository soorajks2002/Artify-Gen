import openai
import re
from api_key import open_ai_api_key

openai.api_key = open_ai_api_key

def extract_sentences(input_text):
    # Split the input text into sentences based on both "\n\n" and "\n"
    sentences = re.split(r'(\n\n|\n)', input_text)
    
    # Remove leading numbers and periods from sentences
    sentences = [re.sub(r'^\d+\.\s*', '', sentence.strip()) for sentence in sentences if sentence.strip()]
    
    return sentences

def generate_prompt (keywords) :
    
    prompt = '''write 3 short, simple and detailed image prompt for DALL-E using these words {keywords}'''

    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": '''write 3 short, simple and detailed image prompt for DALL-E using these words ["kids", "healthy food", "cereal"]'''},
                {"role": "assistant", "content": '''Illustrate a vibrant scene where kids of various ages are gathered around a picnic table, eagerly enjoying a colorful spread of healthy food. The table is adorned with fresh fruits, vegetables, and whole-grain cereal bowls, while the children's faces radiate joy and excitement.\nCreate an image that showcases a classroom filled with enthusiastic children, each holding a unique, imaginative creation made from healthy ingredients. Some kids might have crafted cereal art sculptures, while others have designed nutritious snacks, fostering creativity and nutritious eating habits.\nDepict an inviting kitchen setting with a parent and child teaming up to prepare a delightful breakfast. The focus should be on the duo as they pour cereal into a bowl, surrounded by containers of fresh fruits, yogurt, and whole-grain options. The atmosphere should exude warmth and togetherness, highlighting the importance of family and nutritious choices.'''},
                {"role": "user", "content": prompt.format(keywords=keywords)}
            ]
        )
    
    generated_sentences = response["choices"][0]["message"]["content"]
    
    return extract_sentences(generated_sentences)