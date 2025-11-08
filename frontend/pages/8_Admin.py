import streamlit as st
from utils.api_utils import call_api
import time

st.set_page_config(page_title="Admin - Mastersolis Infotech", layout="wide")

# -------------------- STYLING --------------------
st.markdown("""
<style>
    .stApp {background: linear-gradient(135deg, #001f3f 0%, #003d7a 50%, #0056b3 100%);}
    h1, h2, h3 {color: #f0f8ff; text-align: center;}
    .metric-box {background: rgba(255,255,255,0.15); padding: 20px;
                 border-radius: 15px; text-align: center; color: white;}
</style>
""", unsafe_allow_html=True)

st.title("🧠 Admin Dashboard")

# -------------------- LOGIN FORM --------------------
if "admin_token" not in st.session_state:
    st.subheader("🔐 Admin Login")

    with st.form("admin_login"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            result = call_api("/api/admin/login", method="POST",
                              data={"username": username, "password": password})

            if "error" in result:
                st.error(f"❌ {result['error']}")
            elif result.get("token"):
                st.session_state["admin_token"] = result["token"]
                st.success("✅ Login successful! Loading dashboard...")
                time.sleep(1.2)
                st.rerun()   # 🔁 force reload to show dashboard


# -------------------- DASHBOARD CONTENT --------------------
else:
    st.success("✅ Logged in as Admin")

    summary = call_api("/api/admin/summary")

    if "error" in summary:
        st.error(summary["error"])
    else:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"<div class='metric-box'><h2>{summary['resume_count']}</h2><p>📄 Total Resumes</p></div>",
                        unsafe_allow_html=True)
        with col2:
            st.markdown(f"<div class='metric-box'><h2>{summary['contact_count']}</h2><p>📬 Total Contacts</p></div>",
                        unsafe_allow_html=True)

        st.markdown("---")
        st.text_area("📊 AI Digest", summary["digest"], height=150)

    # Logout button
    if st.button("🚪 Logout"):
        del st.session_state["admin_token"]
        st.rerun()
