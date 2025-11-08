import streamlit as st
from utils.api_utils import call_api
from utils.ui_helpers import display_loading

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Projects - Mastersolis Infotech", layout="wide")

# ---- STYLES ----
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 25%, #2a1f4a 50%, #1a1f3a 75%, #0a0e27 100%);
        background-attachment: fixed;
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
    }

    @keyframes gradientShift {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }

    h1, h2, h3, h4, p { color: #e6f2ff; text-align: center; }
    #MainMenu, footer, header { visibility: hidden; }

    .filter-box {
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(0,212,255,0.3);
        border-radius: 15px;
        padding: 20px;
        color: white;
        margin-bottom: 25px;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 25px rgba(0,212,255,0.1);
    }

    .project-card {
        background: linear-gradient(145deg, rgba(0, 212, 255, 0.08), rgba(123, 47, 247, 0.08));
        backdrop-filter: blur(15px);
        border: 1px solid rgba(0,212,255,0.3);
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        color: #e0e7ff;
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        transition: all 0.4s ease;
    }

    .project-card:hover {
        transform: translateY(-8px) scale(1.01);
        border-color: #00d4ff;
        box-shadow: 0 20px 50px rgba(0,212,255,0.4);
    }

    .tag {
        background-color: #00bfff;
        color: white;
        font-size: 13px;
        padding: 5px 10px;
        border-radius: 12px;
        margin-right: 8px;
        display: inline-block;
        text-shadow: 0 0 8px rgba(0,0,0,0.4);
    }

    /* ---- FIXED INPUT FIELD VISIBILITY ---- */
    .stMultiSelect div[data-baseweb="select"] > div {
        background: rgba(255,255,255,0.08) !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        border: 1px solid rgba(0,212,255,0.3) !important;
    }

    .stMultiSelect div[data-baseweb="select"]:focus-within {
        border: 1px solid #00d4ff !important;
        box-shadow: 0 0 15px rgba(0,212,255,0.4) !important;
    }

    .stButton button {
        background: linear-gradient(135deg, #00d4ff 0%, #7b2ff7 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 15px !important;
        padding: 10px 35px !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        transition: all 0.3s ease !important;
    }

    .stButton button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 25px rgba(0,212,255,0.5) !important;
    }

</style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.markdown("<h1>🧱 Our Projects</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#cce6ff;'>Explore our AI-driven projects and innovations.</p>", unsafe_allow_html=True)

# ---- FETCH PROJECTS ----
if "projects_all" not in st.session_state:
    display_loading()
    response = call_api("/api/projects")
    st.session_state["projects_all"] = response.get("projects", [])
    st.session_state["projects_filtered"] = st.session_state["projects_all"]
    st.session_state["summaries"] = {}

projects = st.session_state["projects_filtered"]

# ---- FILTER ----
all_tags = sorted({tag for p in st.session_state["projects_all"] for tag in p["tags"]})
selected_tags = st.multiselect("🔍 Filter by Tags", all_tags, placeholder="Select tags to filter")

if st.button("Apply Filters", use_container_width=True):
    if selected_tags:
        st.session_state["projects_filtered"] = [p for p in st.session_state["projects_all"] if any(tag in p["tags"] for tag in selected_tags)]
    else:
        st.session_state["projects_filtered"] = st.session_state["projects_all"]
    projects = st.session_state["projects_filtered"]

# ---- DISPLAY PROJECTS ----
if projects:
    for p in projects:
        st.markdown(f"""
        <div class='project-card'>
            <h3>{p['title']}</h3>
            <p>{p['desc']}</p>
            {"".join([f"<span class='tag'>{t}</span>" for t in p['tags']])}
        </div>
        """, unsafe_allow_html=True)

        if st.button(f"🧠 AI Summary for {p['title']}", key=f"summary_{p['title']}"):
            display_loading()
            response = call_api("/api/projects/summarize", method="POST", data={"text": p["desc"]})
            summary = response.get("summary", "Unable to generate summary.")
            st.session_state["summaries"][p['title']] = summary

        if p['title'] in st.session_state["summaries"]:
            st.success(st.session_state["summaries"][p['title']])
else:
    st.warning("No projects found. Try selecting different tags.")
