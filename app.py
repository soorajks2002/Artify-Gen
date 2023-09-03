import streamlit as st
from streamlit_tags import st_tags
from generate_prompt import generate_prompt
from generate_image import generate_image
from PIL import Image

favicon = Image.open('favicon.ico')
st.set_page_config(page_title='Customize Background', page_icon=favicon)

with st.form("main form") : 
    keywords = st_tags(
        label='### Enter Keywords:',
        text='Press enter to add more',
        maxtags=4)
    
    if st.form_submit_button("Generate Image Prompt") :
        
        if not keywords :
            st.warning("Please enter keywords")
        
        else :
            with st.spinner("Generating Prompts...") :
                prompts = generate_prompt(keywords)
                
                for i,prompt in enumerate(prompts) :
                    st.markdown(f"#### Prompt **{i+1}** ⤵️")
                    st.markdown(f"#### {prompt}")
                    
            with st.spinner ("Generating Images...") :
                image_generation_result = generate_image(prompts[0])
                
                if image_generation_result["image_generated"] :
                    st.image(image_generation_result['image'])
                else :
                    st.error("Hugging Face Stable Diffusion Model is BUSY !!!")
