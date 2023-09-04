import streamlit as st
from streamlit_tags import st_tags
from generate_prompt import generate_prompt
from generate_image import generate_image
from PIL import Image

import time

favicon = Image.open('favicon.ico')
st.set_page_config(page_title='Customize Background',
                   page_icon=favicon, layout='wide')

col1, col2 = st.columns(2)
with col1:
    keywords_form = st.form('keyword form')
    prompts_form = st.form('prompt form')
with col2:
    images_form = st.form('Stable Diffusion Image Generation')

form_submitted = None
prompt_form_submitted = None
st.session_state['generated_prompts'] = []

prompt_list = ["Prompt 1", "Prompt 2", "Prompt 3"]

def image_form_block():
    
    with images_form:
        with st.spinner("Generating Images..."):

            prompts = st.session_state['generated_prompts']
            prompt_no = st.session_state['prompt-radio']
            prompt = prompts[prompt_list.index(prompt_no)]
            st.write(prompt)

            image_generation_result = generate_image(prompt)

            if image_generation_result['image_generated'] :
                st.image(image_generation_result['image'])
            else :
                st.error("Hugging Face Stable Diffusion Model is BUSY !!!")
        
        vlue = st.form_submit_button("UNCLIKABLE BUTTON", disabled=True)


def prompt_form_block():
    
    with prompts_form:
        with st.spinner("Generating Prompts..."):
            keywords = st.session_state['prompt-keywords']

            st.session_state['generated_prompts'] = generate_prompt(keywords)

        prompts = st.session_state['generated_prompts']
        
        for i, prompt in enumerate(prompts):
            st.markdown(f"#### Prompt **{i+1}** ⤵️")
            st.markdown(f"##### {prompt}")

        prompt_radio_button = st.radio(
            "# Select Prompt ..", prompt_list, key='prompt-radio')
        prompt_form_submitted = st.form_submit_button(
            "Generate Image", on_click=image_form_block)


with keywords_form:
    keywords = st_tags(
        label='### Enter Keywords:',
        text='Press enter to add more',
        maxtags=4, key='prompt-keywords')

    form_submitted = st.form_submit_button(
        "Generate Image Prompt")

    if form_submitted:
        if not keywords:
            st.warning("Please enter keywords")

        else:
            prompt_form_block()
