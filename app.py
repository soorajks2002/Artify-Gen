import streamlit as st
from streamlit_tags import st_tags

keywords = st_tags(
    label='# Enter Keywords:',
    text='Press enter to add more',
    maxtags=4)

for i in keywords : 
    st.subheader(i)