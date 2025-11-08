import streamlit as st

st.set_page_config(page_title="Mastersolis", layout="wide")

# Theme switch (bonus)
if st.sidebar.checkbox("Dark Mode"):
    st.markdown("""
    <style>
    body { background-color: #121212; color: white; }
    </style>
    """, unsafe_allow_html=True)

# Page navigation
pages = {
    "Home": "pages/1_Home.py",
    "About": "pages/2_About.py",
    "Services": "pages/3_Services.py",
    "Projects": "pages/4_Projects.py",
    "Careers": "pages/5_Careers.py",
    "Blog": "pages/6_Blog.py",
    "Contact": "pages/7_Contact.py",
    "Admin": "pages/8_Admin.py",
    "Chatbot": "pages/9_Chatbot.py",
    "Resume Builder": "pages/10_Resume_Builder.py"
}

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", list(pages.keys()))

# Load page
exec(open(pages[page], encoding='utf-8').read())