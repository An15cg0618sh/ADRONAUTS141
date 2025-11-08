import streamlit as st
from utils.api_utils import call_api

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Resume Builder - Mastersolis Infotech",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---- CUSTOM STYLES ----
st.markdown("""
<style>
    /* ---- GLOBAL ---- */
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

    /* ---- FLOATING PARTICLES ---- */
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(180deg); }
    }
    
    .particle {
        position: fixed;
        width: 4px;
        height: 4px;
        background: rgba(0, 212, 255, 0.3);
        border-radius: 50%;
        pointer-events: none;
        z-index: 1;
    }

    /* ---- TITLE ---- */
    h1 {
        color: #ffffff !important;
        text-align: center;
        background: linear-gradient(135deg, #00d4ff 0%, #7b2ff7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 900 !important;
        letter-spacing: 1px;
        font-size: 52px !important;
        margin: 40px 0 20px 0 !important;
        animation: glow 2s ease-in-out infinite;
    }
    
    @keyframes glow {
        0%, 100% { filter: drop-shadow(0 0 20px rgba(0, 212, 255, 0.5)); }
        50% { filter: drop-shadow(0 0 40px rgba(123, 47, 247, 0.8)); }
    }

    /* ---- SUBTITLE ---- */
    .subtitle {
        text-align: center;
        color: #e0e7ff;
        font-size: 20px;
        margin-bottom: 50px;
        font-weight: 500;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.8);
    }

    /* ---- SECTION HEADERS ---- */
    h3 {
        color: #00d4ff !important;
        font-size: 28px !important;
        font-weight: 800 !important;
        margin: 30px 0 20px 0 !important;
        text-shadow: 0 2px 10px rgba(0, 212, 255, 0.5);
    }

    /* ---- FORM CONTAINER ---- */
    .form-container {
        background: linear-gradient(145deg, rgba(0, 212, 255, 0.08), rgba(123, 47, 247, 0.08));
        backdrop-filter: blur(15px);
        border: 1px solid rgba(0, 212, 255, 0.3);
        border-radius: 25px;
        padding: 40px;
        margin: 30px 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
        animation: fadeInUp 1s ease-out;
    }
    
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(50px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* ---- FORM LABELS ---- */
    .stTextInput label, .stTextArea label {
        color: #00d4ff !important;
        font-size: 18px !important;
        font-weight: 700 !important;
        margin-bottom: 10px !important;
        text-shadow: 0 2px 8px rgba(0, 212, 255, 0.4);
    }

    /* ---- INPUT FIELDS ---- */
    .stTextInput input, .stTextArea textarea {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(0, 212, 255, 0.3) !important;
        border-radius: 15px !important;
        color: #ffffff !important;
        padding: 18px !important;
        font-size: 16px !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #00d4ff !important;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.4) !important;
        background: rgba(255, 255, 255, 0.08) !important;
    }
    
    .stTextInput input::placeholder, .stTextArea textarea::placeholder {
        color: rgba(255, 255, 255, 0.4) !important;
    }
    
    .stTextArea textarea {
        min-height: 120px !important;
        line-height: 1.6 !important;
    }

    /* ---- BUTTONS ---- */
    .stButton button {
        background: linear-gradient(135deg, #00d4ff 0%, #7b2ff7 100%) !important;
        border: none !important;
        border-radius: 15px !important;
        padding: 16px 50px !important;
        font-weight: 700 !important;
        font-size: 18px !important;
        color: white !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        box-shadow: 0 8px 25px rgba(0, 212, 255, 0.3) !important;
    }
    
    .stButton button:hover {
        transform: translateY(-5px) !important;
        box-shadow: 0 15px 40px rgba(0, 212, 255, 0.6) !important;
    }

    /* ---- DOWNLOAD BUTTON ---- */
    .stDownloadButton button {
        background: linear-gradient(135deg, #7b2ff7 0%, #00d4ff 100%) !important;
        border: none !important;
        border-radius: 15px !important;
        padding: 14px 40px !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        color: white !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
    }
    
    .stDownloadButton button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 10px 30px rgba(123, 47, 247, 0.6) !important;
    }

    /* ---- RESULT CONTAINER ---- */
    .result-container {
        background: linear-gradient(145deg, rgba(123, 47, 247, 0.08), rgba(0, 212, 255, 0.08));
        backdrop-filter: blur(15px);
        border: 1px solid rgba(123, 47, 247, 0.3);
        border-radius: 25px;
        padding: 40px;
        margin: 30px 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
        animation: fadeInUp 1.2s ease-out;
    }

    /* ---- GENERATED RESUME TEXT AREA ---- */
    .result-container .stTextArea textarea {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(123, 47, 247, 0.3) !important;
        color: #e0e7ff !important;
        font-family: 'Courier New', monospace !important;
        font-size: 15px !important;
        line-height: 1.8 !important;
        min-height: 400px !important;
    }

    /* ---- INFO CARDS ---- */
    .info-card {
        background: linear-gradient(145deg, rgba(0, 212, 255, 0.08), rgba(123, 47, 247, 0.08));
        backdrop-filter: blur(10px);
        border: 1px solid rgba(0, 212, 255, 0.3);
        border-radius: 20px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
    }
    
    .info-card:hover {
        transform: translateY(-5px);
        border-color: #00d4ff;
        box-shadow: 0 12px 35px rgba(0, 212, 255, 0.4);
    }
    
    .info-card h4 {
        color: #00d4ff !important;
        font-size: 20px !important;
        font-weight: 800 !important;
        margin-bottom: 10px !important;
    }
    
    .info-card p {
        color: #e0e7ff !important;
        font-size: 15px !important;
        line-height: 1.6 !important;
        margin: 0 !important;
        font-weight: 500 !important;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.8);
    }

    /* ---- TIPS SECTION ---- */
    .tips-section {
        background: linear-gradient(145deg, rgba(123, 47, 247, 0.08), rgba(0, 212, 255, 0.08));
        backdrop-filter: blur(15px);
        border: 1px solid rgba(123, 47, 247, 0.3);
        border-radius: 25px;
        padding: 30px;
        margin: 40px 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    }
    
    .tips-section h3 {
        color: #a78bfa !important;
        margin-top: 0 !important;
    }
    
    .tips-section ul {
        list-style: none;
        padding-left: 0;
    }
    
    .tips-section li {
        color: #e0e7ff !important;
        font-size: 16px !important;
        line-height: 1.8 !important;
        margin: 12px 0 !important;
        padding-left: 30px !important;
        position: relative;
        font-weight: 500 !important;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.8);
    }
    
    .tips-section li::before {
        content: "✦";
        position: absolute;
        left: 0;
        color: #a78bfa;
        font-size: 20px;
        font-weight: bold;
    }
</style>

<script>
    // Create floating particles
    function createParticles() {
        const colors = ['rgba(0, 212, 255, 0.3)', 'rgba(123, 47, 247, 0.3)', 'rgba(255, 255, 255, 0.2)'];
        for(let i = 0; i < 30; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.top = Math.random() * 100 + '%';
            particle.style.background = colors[Math.floor(Math.random() * colors.length)];
            particle.style.animation = `float ${3 + Math.random() * 4}s ease-in-out infinite`;
            particle.style.animationDelay = Math.random() * 2 + 's';
            document.body.appendChild(particle);
        }
    }
    
    setTimeout(createParticles, 100);
</script>
""", unsafe_allow_html=True)

# ---- TITLE ----
st.title("📄 Resume Builder")
st.markdown("<p class='subtitle'>✨ Create a professional resume powered by AI in minutes</p>", unsafe_allow_html=True)

# ---- INFO CARDS ----
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
        <div class='info-card'>
            <h4>🎓 Education</h4>
            <p>Add your academic background and qualifications</p>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div class='info-card'>
            <h4>💼 Experience</h4>
            <p>Highlight your work history and achievements</p>
        </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
        <div class='info-card'>
            <h4>⚡ Skills</h4>
            <p>Showcase your technical and soft skills</p>
        </div>
    """, unsafe_allow_html=True)

# ---- FORM SECTION ----
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<div class='form-container'>", unsafe_allow_html=True)
st.markdown("<h3>📝 Enter Your Details</h3>", unsafe_allow_html=True)

education = st.text_area(
    "🎓 Education",
    placeholder="e.g., Bachelor of Technology in Computer Science, XYZ University (2018-2022)",
    height=120,
    help="Include your degree, institution, and graduation year"
)

skills = st.text_area(
    "⚡ Skills",
    placeholder="e.g., Python, JavaScript, React, Machine Learning, Data Analysis, Leadership",
    height=120,
    help="List your technical and soft skills separated by commas"
)

experience = st.text_area(
    "💼 Experience",
    placeholder="e.g., Software Engineer at ABC Corp (2022-2024) - Developed web applications, Led team of 5 developers",
    height=150,
    help="Describe your work experience, internships, or projects"
)

st.markdown("</div>", unsafe_allow_html=True)

# ---- GENERATE BUTTON ----
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    generate_clicked = st.button("🤖 Generate AI-Powered Resume", use_container_width=True)

# ---- RESULT SECTION ----
if generate_clicked:
    if not education.strip() or not skills.strip() or not experience.strip():
        st.warning("⚠️ Please fill in all fields before generating your resume.")
    else:
        with st.spinner("🤖 AI is crafting your professional resume..."):
            data = {'education': education, 'skills': skills, 'experience': experience}
            result = call_api('/api/resume/build', method='POST', data=data)
            
            if "error" in result:
                st.error(f"❌ Error: {result['error']}")
            else:
                resume_text = result.get('resume_text', '')
                
                # Store in session state
                st.session_state['resume_text'] = resume_text
                st.success("✅ Your resume has been generated successfully!")

# Display generated resume if exists
if 'resume_text' in st.session_state:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div class='result-container'>", unsafe_allow_html=True)
    st.markdown("<h3>📋 Your Generated Resume</h3>", unsafe_allow_html=True)
    
    st.text_area(
        "Resume Preview",
        st.session_state['resume_text'],
        height=400,
        label_visibility="collapsed"
    )
    
    # Download buttons
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.download_button(
            label="📥 Download as TXT",
            data=st.session_state['resume_text'],
            file_name="professional_resume.txt",
            mime="text/plain",
            use_container_width=True
        )
    
    st.markdown("</div>", unsafe_allow_html=True)

# ---- TIPS SECTION ----
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
    <div class='tips-section'>
        <h3>💡 Pro Tips for a Great Resume</h3>
        <ul>
            <li>Keep it concise and relevant - aim for 1-2 pages maximum</li>
            <li>Use action verbs like "developed", "managed", "led" to describe your achievements</li>
            <li>Quantify your accomplishments with numbers and metrics when possible</li>
            <li>Tailor your resume for each job application</li>
            <li>Proofread carefully for grammar and spelling errors</li>
            <li>Use a clean, professional format with consistent styling</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

# ---- FOOTER ----
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    """
    <div style='text-align:center; padding:40px; color:rgba(255,255,255,0.6); font-size:14px;'>
        <p style='font-size:16px; font-weight:600; background: linear-gradient(135deg, #00d4ff 0%, #7b2ff7 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;'>
            © 2024 Mastersolis Infotech. All Rights Reserved.
        </p>
        <p>AI-Powered Resume Building 📄</p>
    </div>
    """,
    unsafe_allow_html=True
)