import streamlit as st
st.header("Credentials")
st.write("Please provide your credentials. You can use any of the following:")
submit=st.button("Submit")
@st.experimental_dialog("Credentials")
def credentials():
    username=st.text_input("Username")
credentials()