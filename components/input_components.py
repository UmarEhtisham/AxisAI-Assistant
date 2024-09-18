import streamlit as st
from utils.constants import PROVIDERS
def model_key(llm_choice: str):
    
    key = None
    for company in PROVIDERS:
        if llm_choice == company:
            key = st.text_input(PROVIDERS[company], type="password")
    return llm_choice, key