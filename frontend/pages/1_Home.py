import streamlit as st
from utils.api_utils import call_api
from utils.ui_helpers import display_loading

# ---- NAVIGATION FUNCTION ----
def go_to_about():
    st.switch_page("pages/2_About.py")

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Mastersolis Infotech", layout="wide", initial_sidebar_state="collapsed")

# ---- CUSTOM CSS ----
st.markdown(
    """
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
        
        body { margin: 0; padding: 0; }
        #MainMenu, footer, header {visibility: hidden;}
        
        /* ---- HIDE SIDEBAR COMPLETELY ---- */
        [data-testid="stSidebar"] {
            display: none !important;
        }
        
        section[data-testid="stSidebar"] {
            display: none !important;
        }
        
        .css-1d391kg, .css-1lcbmhc {
            display: none !important;
        }
        
        /* Adjust main content to use full width */
        .main .block-container {
            max-width: 100% !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
        }

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

        /* ---- NAVBAR ---- */
        .navbar {
            position: fixed;
            top: 0; left: 0; right: 0;
            background: rgba(10, 14, 39, 0.85);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(0, 212, 255, 0.2);
            padding: 18px 50px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 1000;
            color: white;
            box-shadow: 0 8px 32px rgba(0, 212, 255, 0.1);
            animation: slideDown 0.6s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        }

        @keyframes slideDown {
            from {transform: translateY(-100%); opacity: 0;}
            to {transform: translateY(0); opacity: 1;}
        }

        .nav-left h2 {
            font-size: 28px; margin: 0;
            background: linear-gradient(135deg, #00d4ff 0%, #7b2ff7 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 900;
            letter-spacing: 1px;
            text-shadow: 0 0 30px rgba(0, 212, 255, 0.5);
        }

        /* ---- STREAMLIT BUTTON NAVBAR FIX ---- */
        div[data-testid="stHorizontalBlock"] button {
            background: transparent;
            border: 2px solid transparent;
            color: #ffffff;
            font-weight: 600;
            font-size: 14px;
            text-transform: uppercase;
            padding: 12px 24px;
            border-radius: 25px;
            transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            letter-spacing: 0.5px;
            position: relative;
            overflow: hidden;
        }
        
        div[data-testid="stHorizontalBlock"] button::before {
            content: '';
            position: absolute;
            top: 0; left: -100%;
            width: 100%; height: 100%;
            background: linear-gradient(90deg, transparent, rgba(0, 212, 255, 0.3), transparent);
            transition: left 0.5s;
        }

        div[data-testid="stHorizontalBlock"] button:hover {
            color: #00d4ff;
            border-color: #00d4ff;
            transform: translateY(-3px);
            box-shadow: 0 5px 20px rgba(0, 212, 255, 0.4);
        }
        
        div[data-testid="stHorizontalBlock"] button:hover::before {
            left: 100%;
        }

        div[data-testid="stHorizontalBlock"] button:focus {
            outline: none;
        }

        /* ---- HERO ---- */
        .hero {
            margin-top: 120px;
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.05), rgba(123, 47, 247, 0.05));
            backdrop-filter: blur(15px);
            border: 1px solid rgba(0, 212, 255, 0.3);
            border-radius: 30px;
            text-align: center;
            padding: 100px 40px;
            color: white;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5), inset 0 0 80px rgba(0, 212, 255, 0.05);
            animation: fadeInUp 1s ease-out, pulse 3s ease-in-out infinite;
            position: relative;
            overflow: hidden;
        }
        
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(50px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        @keyframes pulse {
            0%, 100% { box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5), inset 0 0 80px rgba(0, 212, 255, 0.05); }
            50% { box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5), inset 0 0 100px rgba(123, 47, 247, 0.08); }
        }
        
        .hero::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(0, 212, 255, 0.1) 0%, transparent 70%);
            animation: rotate 20s linear infinite;
        }
        
        @keyframes rotate {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }

        .hero h1 {
            position: relative;
            z-index: 1;
            background: linear-gradient(135deg, #ffffff 0%, #00d4ff 50%, #7b2ff7 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 900;
            font-size: 64px;
            margin-bottom: 20px;
            animation: glow 2s ease-in-out infinite;
        }
        
        @keyframes glow {
            0%, 100% { filter: drop-shadow(0 0 20px rgba(0, 212, 255, 0.5)); }
            50% { filter: drop-shadow(0 0 40px rgba(123, 47, 247, 0.8)); }
        }
        
        .hero p {
            position: relative;
            z-index: 1;
            font-size: 26px;
            opacity: 0.95;
            font-weight: 500;
            letter-spacing: 1px;
        }

        /* ---- CONTENT ---- */
        .tagline {
            font-size: 34px;
            color: #ffffff;
            text-align: center;
            font-weight: 700;
            margin: 50px 0;
            padding: 30px;
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.1), rgba(123, 47, 247, 0.1));
            border-radius: 20px;
            backdrop-filter: blur(15px);
            border: 1px solid rgba(0, 212, 255, 0.3);
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
            animation: fadeInUp 1.2s ease-out;
        }

        h3 {
            color: #ffffff !important;
            font-size: 42px !important;
            font-weight: 900 !important;
            text-align: center;
            margin: 60px 0 40px 0 !important;
            background: linear-gradient(135deg, #00d4ff 0%, #7b2ff7 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: 1px;
        }

        .highlight-card {
            text-align: center;
            padding: 40px 25px;
            border-radius: 25px;
            background: linear-gradient(145deg, rgba(0, 212, 255, 0.08), rgba(123, 47, 247, 0.08));
            backdrop-filter: blur(15px);
            border: 1px solid rgba(0, 212, 255, 0.3);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
            margin: 15px;
            transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            position: relative;
            overflow: hidden;
        }
        
        .highlight-card::before {
            content: '';
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: linear-gradient(135deg, transparent, rgba(0, 212, 255, 0.1), transparent);
            transform: translateX(-100%);
            transition: transform 0.6s;
        }

        .highlight-card:hover {
            transform: translateY(-15px) scale(1.05);
            box-shadow: 0 20px 50px rgba(0, 212, 255, 0.5);
            border-color: #00d4ff;
        }
        
        .highlight-card:hover::before {
            transform: translateX(100%);
        }

        .highlight-card h4 {
            color: #ffffff;
            font-size: 20px;
            font-weight: 700;
            margin: 0;
            position: relative;
            z-index: 1;
        }

        .contact-info {
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.08), rgba(123, 47, 247, 0.08));
            backdrop-filter: blur(15px);
            border: 1px solid rgba(0, 212, 255, 0.3);
            border-radius: 25px;
            padding: 40px;
            margin-top: 30px;
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.4);
            animation: fadeInUp 1.4s ease-out;
        }

        .contact-info p {
            color: #ffffff;
            font-size: 19px;
            margin: 20px 0;
            transition: all 0.3s ease;
        }
        
        .contact-info p:hover {
            transform: translateX(10px);
            color: #00d4ff;
        }

        .contact-info a {
            color: #00d4ff;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .contact-info a:hover {
            color: #7b2ff7;
            text-shadow: 0 0 10px rgba(123, 47, 247, 0.5);
        }
        
        /* ---- SCROLL INDICATOR ---- */
        .scroll-indicator {
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            animation: bounce 2s infinite;
            z-index: 999;
        }
        
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% { transform: translateX(-50%) translateY(0); }
            40% { transform: translateX(-50%) translateY(-20px); }
            60% { transform: translateX(-50%) translateY(-10px); }
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
        
        // Smooth scroll function
        function smoothScroll(targetId) {
            const element = document.getElementById(targetId);
            if(element) {
                element.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }
        
        setTimeout(createParticles, 100);
    </script>
    """,
    unsafe_allow_html=True
)

# ---- NAVBAR ----
st.markdown(
    """
    <div class="navbar">
        <div class="nav-left">
            <h2>⚡ Mastersolis Infotech</h2>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

nav1, nav2, nav3, nav4, nav5 = st.columns([1, 1, 1, 1, 1])
with nav1:
    st.button("🏠 Home", use_container_width=True, key="nav_home")
with nav2:
    if st.button("👥 About", use_container_width=True, key="nav_about"):
        go_to_about()
with nav3:
    st.button("🛠️ Services", use_container_width=True, key="nav_services")
with nav4:
    st.button("💼 Career", use_container_width=True, key="nav_career")
with nav5:
    st.button("📞 Contact", use_container_width=True, key="nav_contact")

# ---- HERO SECTION ----
st.markdown(
    """
    <div class='hero' id='home'>
        <h1>Mastersolis Infotech</h1>
        <p>✨ Innovating Tomorrow, Empowering Today ✨</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ---- TAGLINE SECTION ----
st.markdown("<div id='tagline'></div>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.subheader("💡 Dynamic AI Tagline")
    if st.button("✨ Regenerate Tagline", use_container_width=True, key="regen_tagline"):
        display_loading()
        content = call_api('/api/home_content')
        st.session_state['tagline'] = content.get('tagline', "Empowering the Future with AI-Driven Innovation")
        st.session_state['highlights'] = content.get('highlights', [])

tagline = st.session_state.get('tagline', "🚀 Empowering the Future with AI-Driven Innovation")
highlights = st.session_state.get('highlights', [
    "🌐 Full-stack Web & App Development",
    "🤖 AI & Machine Learning Integration",
    "📈 Data Analytics & Automation Tools",
    "💼 Career and Resume Intelligence"
])

st.markdown(f"<div class='tagline'>{tagline}</div>", unsafe_allow_html=True)

# ---- HIGHLIGHTS SECTION ----
st.markdown("<div id='services'></div>", unsafe_allow_html=True)
st.markdown("<br><h3>🚀 Our Core Services</h3>", unsafe_allow_html=True)
cols = st.columns(len(highlights))
for i, h in enumerate(highlights):
    with cols[i]:
        st.markdown(f"<div class='highlight-card'><h4>{h}</h4></div>", unsafe_allow_html=True)

# ---- CONTACT SECTION ----
st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.markdown("<br><h3>📞 Get In Touch</h3>", unsafe_allow_html=True)
st.markdown(
    """
    <div class='contact-info'>
        <p>📧 <strong>Email:</strong> <a href='mailto:contact@mastersolisinfotech.com'>contact@mastersolisinfotech.com</a></p>
        <p>🌐 <strong>Website:</strong> <a href='#'>www.mastersolisinfotech.com</a></p>
        <p>🏢 <strong>Location:</strong> Bengaluru, Karnataka, India</p>
        <p>📱 <strong>Phone:</strong> +91 98765 43210</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ---- FOOTER ----
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    """
    <div style='text-align:center; padding:40px; color:rgba(255,255,255,0.6); font-size:14px;'>
        <p style='font-size:16px; font-weight:600; background: linear-gradient(135deg, #00d4ff 0%, #7b2ff7 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;'>
            © 2024 Mastersolis Infotech. All Rights Reserved.
        </p>
        <p>Innovating the Future, One Solution at a Time 🚀</p>
    </div>
    """,
    unsafe_allow_html=True
)