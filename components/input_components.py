# components/input_components.py
import time
import streamlit as st
from utils.constants import PROVIDERS
from utils.save_credentials import save_credentials
def model_key(llm_choice: str):
    
    key = None
    for company in PROVIDERS:
        if llm_choice == company:
            key = st.text_input(PROVIDERS[company], type="password")
    return llm_choice, key


@st.dialog("Sign In to get touch in AxisAI")
def get_credentials():
    st.session_state['username'] = st.text_input("Username")
    st.session_state['llm_choice'] = st.selectbox("LLM", ["OpenAI", "Google Gemini", "HuggingFace", "ChatGroq", "Antropic"])
    _, st.session_state['api_key'] = model_key(st.session_state['llm_choice'])

    # Check if all fields are filled to enable the submit button
    if st.session_state['username'] and st.session_state['llm_choice'] and st.session_state['api_key']:
        st.session_state['signed_in'] = True
    else:
        st.session_state['signed_in'] = False

    submit = st.button("Submit", disabled=not st.session_state['signed_in'])

    if submit:
        # if save_credentials(st.session_state['llm_choice'], st.session_state['api_key']):
        st.success(f"Nice to have you {st.session_state['username'].title()}!")
        st.session_state['signed_in'] = True
        time.sleep(1.5)
        st.switch_page("views/axis_ai.py")
        
    else:
        return 
    
    
def get_chatbot_choice():
    st.session_state.chatbot_choice=st.selectbox(label="Talk to an Axis AI Chatbot",
                         options=["PDF","CSV","Excel","Word","Powerpoint","Database","Website"],
                         index=0,key="chotbot_choice",
                         help="Select the type of chatbot you want to talk to")
    return st.session_state.chatbot_choice