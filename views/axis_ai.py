import time
import streamlit as st
from components.input_components import get_chatbot_choice

CHATBOTS={}
def chatbots():
    st.header("Axis AI",anchor=False)
    cols=st.columns(4,gap='small',vertical_alignment="top")
    st.session_state.chatbot_choice=get_chatbot_choice()
    st.info(st.session_state.chatbot_choice)
    
    
if st.session_state.signed_in:
    chatbots()
else:
    st.warning("Please sign in to continue... Redirecting to credentials page...")
    time.sleep(1.5)
    st.switch_page("views/credentials.py")