import streamlit as st
from utils.api_utils import call_api

# -------------------------------------------
# PAGE CONFIG
# -------------------------------------------
st.set_page_config(page_title="Admin Dashboard - Mastersolis Infotech", layout="wide")

# -------------------------------------------
# GLOBAL STYLES
# -------------------------------------------
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

    #MainMenu, footer, header {visibility: hidden;}

    h1, h2, h3, h4, h5 {
        color: #ffffff !important;
        text-align: center !important;
    }

    .metric-box {
        background: linear-gradient(145deg, rgba(0, 212, 255, 0.1), rgba(123, 47, 247, 0.1));
        border-radius: 15px;
        border: 1px solid rgba(0, 212, 255, 0.3);
        box-shadow: 0 8px 25px rgba(0, 212, 255, 0.2);
        padding: 20px;
        margin: 10px;
        text-align: center;
    }

    .stButton button {
        background: linear-gradient(135deg, #00d4ff 0%, #7b2ff7 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 15px !important;
        padding: 12px 40px !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        transition: all 0.3s ease !important;
    }

    .stButton button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 10px 30px rgba(0,212,255,0.5) !important;
    }

    .expander {
        background: rgba(0, 0, 0, 0.3);
        border-radius: 12px;
        border: 1px solid rgba(0, 212, 255, 0.3);
        color: #e0e7ff;
        box-shadow: 0 5px 15px rgba(0,212,255,0.2);
    }

    .logout-btn {
        text-align: right;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🧠 Admin Dashboard")

# -------------------------------------------
# LOGIN SECTION
# -------------------------------------------
if "admin_token" not in st.session_state:
    st.subheader("🔐 Admin Login")
    username = st.text_input("Username", placeholder="Enter admin username")
    password = st.text_input("Password", placeholder="Enter admin password", type="password")

    if st.button("Login"):
        result = call_api("/api/admin/login", method="POST", data={"username": username, "password": password})
        if not result:
            st.error("No response from server. Try again later.")
        elif "token" in result:
            st.session_state["admin_token"] = result["token"]
            st.success("✅ Login successful!")
            st.rerun()
        else:
            st.error(f"Backend error: {result.get('error', 'Invalid credentials')}")
    st.stop()

# -------------------------------------------
# LOGOUT BUTTON
# -------------------------------------------
with st.container():
    col1, col2 = st.columns([6, 1])
    with col2:
        if st.button("🚪 Logout"):
            del st.session_state["admin_token"]
            st.experimental_rerun()

# -------------------------------------------
# ANALYTICS SECTION
# -------------------------------------------
st.markdown("---")
st.subheader("📊 Site Analytics")

summary = call_api("/api/admin/summary", method="GET")

if not summary or "error" in summary:
    st.error(summary.get("error", "Failed to fetch analytics."))
else:
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='metric-box'><h3>📄 Resumes</h3><h2>{}</h2></div>".format(summary.get("resume_count", 0)), unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='metric-box'><h3>📬 Contacts</h3><h2>{}</h2></div>".format(summary.get("contact_count", 0)), unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='metric-box'><h3>💼 Applications</h3><h2>{}</h2></div>".format(summary.get("applications_count", 0)), unsafe_allow_html=True)

    if st.button("🧠 Generate AI Digest"):
        st.subheader("📈 AI System Insights")
        ai_response = call_api("/api/admin/ai_digest", method="GET")
        if ai_response and "digest" in ai_response:
            st.info(ai_response["digest"])
        else:
            st.warning("No AI digest available or request failed.")

# -------------------------------------------
# CAREER APPLICATIONS VIEW
# -------------------------------------------
st.markdown("---")
st.subheader("💼 Candidate Applications")

apps = call_api("/api/admin/applications")

if not apps or "error" in apps:
    st.error(apps.get("error", "Failed to fetch candidate applications."))
else:
    applications = apps.get("applications", [])
    if not applications:
        st.info("No job applications found.")
    else:
        for app in applications:
            with st.expander(f"👤 {app['name']} ({app['email']}) — Score: {app['score']}%", expanded=False):
                st.markdown(f"**AI Fit Score:** {app['score']}%")
                st.markdown(f"**Notes:** {app['notes']}")
                st.markdown(f"**Submitted On:** {app['created_at']}")
                st.markdown(f"**Job ID:** {app.get('job_id', 'N/A')}")
