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

def generate_prompt (style, keywords) :
    
    prompt = '''write 3 short and simple {style} like image prompt for a diffusion based image generation model using these words {keywords}'''

    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": '''write 3 short and simple anime like image prompt for a diffusion based image generation model using these words ["kids", "healthy food", "cereal"]'''},
                {"role": "assistant", "content": '''An anime scene featuring joyful kids gathered around a vibrant picnic blanket loaded with colorful, healthy food options like fruits and vegetables, with a cereal box as the centerpiece.\n An adorable anime character, dressed in a chef's outfit, preparing a delicious and nutritious breakfast using cereal as a key ingredient while teaching a group of kids about the importance of balanced meals.\n A heartwarming anime moment where children in a daycare setting engage in a fun, educational activity involving planting and growing their own cereal crops, symbolizing the connection between healthy food and growth.'''},
                {"role": "user", "content": prompt.format(keywords=keywords, style=style)}
            ]
        )

    generated_sentences = response["choices"][0]["message"]["content"]
    
    return extract_sentences(generated_sentences)