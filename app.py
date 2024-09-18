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

axis_ai_page=st.Page(
    title="Axis AI",
    page="views/axis_ai.py",
    icon=":material/robot:",
    default=False,
)

# pg=st.navigation(pages=[home_page,credentials_page,axis_ai_page])
# Navigation with sections
pg=st.navigation(
    {
        "Home": [home_page],
        "Sign In": [credentials_page],
        "Axis AI Assitant":[axis_ai_page]
    }
)
st.logo("static/assets/images/logo.png")

pg.run()

