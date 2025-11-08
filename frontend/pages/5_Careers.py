import streamlit as st
from utils.api_utils import call_api
from utils.ui_helpers import display_loading

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Careers - Mastersolis Infotech", layout="wide")

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

    #MainMenu, footer, header {visibility: hidden;}

    h1, h2, h3, h4 {
        color: #ffffff !important;
        text-align: center !important;
    }

    p { color: #cce6ff; text-align: center; }

    .job-card {
        background: linear-gradient(145deg, rgba(0,212,255,0.08), rgba(123,47,247,0.08));
        border: 1px solid rgba(0,212,255,0.3);
        border-radius: 20px;
        padding: 25px;
        margin: 15px 0;
        color: #e0e7ff;
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        transition: all 0.4s ease;
    }
    .job-card:hover {
        transform: translateY(-8px);
        border-color: #00d4ff;
        box-shadow: 0 20px 50px rgba(0,212,255,0.4);
    }

    .stSelectbox div[data-baseweb="select"] > div {
        background: rgba(255,255,255,0.08) !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        border: 1px solid rgba(0,212,255,0.3) !important;
    }

    .stTextInput input, .stTextArea textarea {
        background: rgba(255,255,255,0.08) !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        border: 1px solid rgba(0,212,255,0.3) !important;
        padding: 12px 14px !important;
        font-size: 16px !important;
        caret-color: #00d4ff !important;
    }

    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #00d4ff !important;
        box-shadow: 0 0 15px rgba(0,212,255,0.6) !important;
        background: rgba(0, 0, 0, 0.4) !important;
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

    .section {
        margin-top: 60px;
        animation: fadeInUp 1s ease-out;
    }

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.markdown("<h1>🚀 Careers at Mastersolis Infotech</h1>", unsafe_allow_html=True)
st.markdown("<p>Join our growing AI-driven team. Browse open roles and apply below!</p>", unsafe_allow_html=True)

# ---- FETCH JOB LISTINGS ----
display_loading()
jobs_response = call_api("/api/careers/jobs")

if not jobs_response or "error" in jobs_response:
    st.error("Failed to fetch job listings. Please try again later.")
    st.stop()

jobs = jobs_response.get("jobs", [])

if not jobs:
    st.warning("⚠️ No open positions currently available.")
else:
    st.markdown("<div class='section'><h3>💼 Open Positions</h3></div>", unsafe_allow_html=True)
    for job in jobs:
        st.markdown(f"""
        <div class='job-card'>
            <h4>{job['title']}</h4>
            <p>{job['desc']}</p>
            <p><strong>Location:</strong> {job.get('location', 'Remote')}</p>
            <p><strong>Experience:</strong> {job.get('experience', 'Not Specified')}</p>
        </div>
        """, unsafe_allow_html=True)

    job_titles = [f"{job['id']} - {job['title']}" for job in jobs]
    selected_job = st.selectbox("Select a Job Role", job_titles, index=0)

    # ---- APPLICATION FORM ----
    st.markdown("<div class='section'><h3>📝 Submit Your Application</h3></div>", unsafe_allow_html=True)
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    resume_text = st.text_area("Paste Your Resume Text Here")

    if st.button("Submit Application 🚀"):
        if not all([name.strip(), email.strip(), resume_text.strip(), selected_job]):
            st.warning("⚠️ Please fill all fields before submitting.")
        else:
            display_loading()
            try:
                job_id = int(selected_job.split(" - ")[0])
                payload = {
                    "name": name,
                    "email": email,
                    "resume": resume_text,
                    "job_id": job_id
                }
                response = call_api("/api/careers/apply", method="POST", data=payload)

                if not response:
                    st.error("No response from server. Try again later.")
                elif "error" in response:
                    st.error(response["error"])
                else:
                    st.success(response.get("message", "✅ Application submitted successfully!"))
                    st.markdown("<br>", unsafe_allow_html=True)

                    st.markdown("### 💬 AI Auto-Reply")
                    st.info(response.get("auto_reply", "Thank you for applying!"))

                    st.markdown("### 🧠 Resume Insights")
                    st.write(f"**AI Fit Score:** {response.get('score', 'N/A')}%")
                    st.write(f"**Notes:** {response.get('notes', 'No insights available.')}")

                    # Reset fields
                    st.session_state["name"] = ""
                    st.session_state["email"] = ""
                    st.session_state["resume_text"] = ""
            except Exception as e:
                st.error(f"Unexpected error: {e}")
