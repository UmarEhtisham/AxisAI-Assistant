import streamlit as st

def chat_with_pdf():
    st.header("Chat With PDFs", anchor=False)
    st.write("Please provide your credentials. You can use any of the following:")
    st.selectbox("Select your file type",["json","yaml","yml"])
    st.file_uploader("Upload your credentials",type="json")
    submit=st.button("Submit")
    if submit:
        pass
    st.info(st.session_state["api_key"])
chat_with_pdf()