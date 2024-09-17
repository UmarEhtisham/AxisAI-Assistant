import streamlit as st
st.set_page_config(
    page_title="AxisAI",
    page_icon=":material/robot:",
    layout="wide",
    initial_sidebar_state="expanded",
)
def load_css():
    with open("static/css/style.css") as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

load_css()
# Page setup
home_page=st.Page(
    title="Home",
    page="views/home.py",
    icon=":material/home:",
    default=True,
    
)
credentials_page=st.Page(
    title="Credentials",
    page="views/credentials.py",
    icon=":material/lock:",
    default=False,
    
)

# pg=st.navigation(pages=[home_page,credentials_page])
# Navigation with sections
pg=st.navigation(
    {
        "Home": [home_page],
        "Credentials": [credentials_page]
    }
)
st.logo("assets/images/logo.png")
pg.run()

