import streamlit as st
from streamlit_tags import st_tags
from generate_prompt import generate_prompt
from generate_image import generate_image
from PIL import Image
import time

favicon = Image.open('favicon.ico')
st.set_page_config(page_title="Magic Brush", page_icon=favicon, layout='wide')

col1, col2 = st.columns(2)
with col1:
    keyword_form = st.form("keyword form")
    prompt_form = st.form("prompt form")

if 'prompts_state' not in st.session_state:
    st.session_state['prompts_state'] = []
    
if 'image_state' not in st.session_state:
    st.session_state['image_state'] = []
    
prompt_index = ["Prompt 1", "Prompt 2", "Prompt 3"]

def image_block():
    with col2:
        with st.spinner("Generating Image..."):
            ind = prompt_index.index(st.session_state['selectbox_status'])
            prompt = st.session_state['prompts_state'][ind]
            # image_gen = {"image_generated":False}
            image_gen = generate_image(prompt)
            st.session_state['image_state'] = image_gen

def prompt_block():
    with prompt_form:
        with st.spinner("Generating Prompts ..."):
            keywords = st.session_state['keyword_status']
            prompts = generate_prompt(keywords)
            st.session_state['prompts_state'] = prompts


def check_keyword():
    keywords = st.session_state['keyword_status']
    if keywords:
        st.session_state['prompts_state'] = []
        st.session_state['image_state'] = []
        prompt_block()
    else:
        keyword_form.warning("Please Enter Keywords")


with keyword_form:
    keywords = st_tags(label="## Enter Keywords ...",
                        text="Press Enter to add more (max 5)", maxtags=5, key='keyword_status')
    if st.form_submit_button("Generate Prompts"):
        check_keyword()
        
if st.session_state['prompts_state'] :
    with prompt_form:
        prompts = st.session_state['prompts_state']
        for i, prompt in enumerate(prompts):
            st.markdown(f"#### Prompt **{i+1}** ⤵️")
            st.markdown(f"##### {prompt}")
            
        st.selectbox("Select Prompt", ("Prompt 1", "Prompt 2", "Prompt 3"), key='selectbox_status')
        st.form_submit_button("Generate Image", on_click=image_block)
        
if st.session_state['image_state'] :
    with col2 :
        ind = prompt_index.index(st.session_state['selectbox_status'])
        prompt = st.session_state['prompts_state'][ind]
        image_gen = st.session_state['image_state']
        
        st.write(prompt)
        if image_gen['image_generated']:
            st.image(image_gen['image'])
        else:
            st.error("Hugging Face's Stable Diffusion Inference API is BUSY !!!")       