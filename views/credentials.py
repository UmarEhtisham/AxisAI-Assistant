import streamlit as st
from components.input_components import model_key
from utils.save_credentials import save_credentials
st.header("Axis AI Credentials", anchor=False)

# Initialize session states for credentials
if 'llm_choice' not in st.session_state:
    st.session_state['llm_choice'] = None
if 'username' not in st.session_state:
    st.session_state['username'] = 'AxisAI'
if 'api_key' not in st.session_state:
    st.session_state['api_key'] = None
if 'signed_in' not in st.session_state:
    st.session_state['signed_in'] = False

# HTML content with bulleted list and clickable links
st.markdown("""
    <div class="api-container">
        <p>Before you get started, kindly get your API Keys from any of the following providers:</p>
        <ul>
            <li><a href="https://platform.openai.com/signup" target="_blank">OpenAI</a></li>
            <li><a href="https://cloud.google.com/gemini/" target="_blank">Google Gemini</a></li>
            <li><a href="https://groq.com/" target="_blank">Groq</a></li>
            <li><a href="https://huggingface.co/" target="_blank">HuggingFace</a></li>
            <li><a href="https://claude.ai/" target="_blank">Claude</a></li>
        </ul>
    </div>
    <br>
    """, unsafe_allow_html=True)



# Main function to get credentials

@st.experimental_dialog("Sign In to get touch in AxisAI")
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
        if save_credentials(st.session_state['llm_choice'], st.session_state['api_key']):
            st.success(f"Nice to have you {st.session_state['username']}!")
        else:
            st.error("Error saving credentials.")

# Main app layout
cols = st.columns(3)
with cols[1]:
    sign_in = st.button("Sign In", key="submit")
    if sign_in:
        # st.switch_page("views/home.py")
        
        get_credentials()
