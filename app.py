import streamlit as st
from streamlit_tags import st_tags
from generate_prompt import generate_prompt
from generate_image import generate_image

with st.form("main form") : 
    keywords = st_tags(
        label='# Enter Keywords:',
        text='Press enter to add more',
        maxtags=4)
    
    if st.form_submit_button("Generate Image Prompt") :
        
        with st.spinner("Generating Prompts...") :
            prompts = generate_prompt(keywords)
            prompts = prompts.split("\n")
            
            for prompt in prompts :
                st.markdown(f"#### {prompt}")
                
        with st.spinner ("Generating Images...") :
            image = generate_image("Astronaut riding a dog in antartica")
            st.image(image)

