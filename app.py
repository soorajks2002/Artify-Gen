import streamlit as st
from streamlit_tags import st_tags
from generate_prompt import generate_prompt
from generate_image import generate_image
from PIL import Image

favicon = Image.open('favicon.ico')
st.set_page_config(page_title='Customize Background', page_icon=favicon)

form = st.form("main form")
prompt_form = st.form("prompt form")
image_container = st.container()

form_submitted = None
prompt_form_submitted = None

prompt_list = ["Prompt 1", "Prompt 2", "Prompt 3"]

with form : 
    keywords = st_tags(
        label='### Enter Keywords:',
        text='Press enter to add more',
        maxtags=4)
    
    form_submitted = st.form_submit_button("Generate Image Prompt") 

if form_submitted :        
    if not keywords :
        st.warning("Please enter keywords")
    
    else :
        with st.spinner("Generating Prompts...") :
            prompts = generate_prompt(keywords)
            
            with prompt_form :
                for i,prompt in enumerate(prompts) :
                    st.markdown(f"#### Prompt **{i+1}** ⤵️")
                    st.markdown(f"##### {prompt}")
                    
                prompt = st.radio("Select Prompt ..", prompt_list)
                prompt_form_submitted = st.form_submit_button("Generate Prompt")
                
if prompt_form_submitted :   
    with st.spinner ("Generating Images...") :
        image_generation_result = generate_image(prompt_list.index(prompt))
        
        if image_generation_result["image_generated"] :
            
            image_container.image(image_generation_result['image'])
        else :
            image_container.error("Hugging Face Stable Diffusion Model is BUSY !!!")
