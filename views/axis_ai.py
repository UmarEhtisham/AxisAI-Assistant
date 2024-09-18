import streamlit as st

st.header("Axis AI",anchor=False)
st.write("Please provide your credentials. You can use any of the following:")

with st.expander("Upload file"):
    st.selectbox("Select your file type",["json","yaml","yml"])
    st.file_uploader("Upload your credentials",type="json")
    submit=st.button("Submit")
    if submit:
        pass