import streamlit as st
from utils.api_utils import call_api
from utils.ui_helpers import display_loading

# ---- NAVIGATION FUNCTIONS ----
def go_to_home():
    st.switch_page("1_Home.py")

def go_to_about():
    st.switch_page("pages/2_About.py")

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Services - Mastersolis Infotech",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---- CUSTOM STYLES ----
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

        /* ---- SECTION HEADERS ---- */
        h3 {
            color: #ffffff !important;
            font-size: 42px !important;
            font-weight: 900 !important;
            text-align: center;
            margin-top: 120px !important;
            margin-bottom: 40px !important;
            background: linear-gradient(135deg, #00d4ff 0%, #7b2ff7 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: 1px;
            animation: fadeInUp 1.2s ease-out;
        }
        
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(50px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* ---- SERVICE CARDS ---- */
        .service-card {
            background: linear-gradient(145deg, rgba(0, 212, 255, 0.08), rgba(123, 47, 247, 0.08));
            backdrop-filter: blur(15px);
            border: 1px solid rgba(0, 212, 255, 0.3);
            border-radius: 25px;
            padding: 35px 30px;
            color: white;
            margin: 20px 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
            transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            position: relative;
            overflow: hidden;
        }
        
        .service-card::before {
            content: '';
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: linear-gradient(135deg, transparent, rgba(0, 212, 255, 0.1), transparent);
            transform: translateX(-100%);
            transition: transform 0.6s;
        }
        
        .service-card:hover {
            transform: translateY(-15px) scale(1.02);
            box-shadow: 0 20px 50px rgba(0, 212, 255, 0.5);
            border-color: #00d4ff;
        }
        
        .service-card:hover::before {
            transform: translateX(100%);
        }
        
        .service-card h4 {
            font-size: 26px;
            color: #00d4ff;
            font-weight: 800;
            margin-bottom: 15px;
            text-shadow: 0 2px 10px rgba(0, 212, 255, 0.5);
        }
        
        .service-card p {
            font-size: 17px;
            line-height: 1.8;
            color: #e0e7ff;
            font-weight: 500;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.8);
        }

        /* ---- CHATBOT SECTION ---- */
        .chat-intro {
            color: #e0e7ff;
            text-align: center;
            font-size: 18px;
            margin-bottom: 30px;
            font-weight: 500;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.8);
        }

        .chatbox {
            background: linear-gradient(145deg, rgba(0, 212, 255, 0.08), rgba(123, 47, 247, 0.08));
            backdrop-filter: blur(15px);
            border-radius: 20px;
            border: 1px solid rgba(0, 212, 255, 0.3);
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
            margin-top: 30px;
            animation: fadeInUp 1.4s ease-out;
        }
        
        .chatbox p {
            color: #e0e7ff;
            font-size: 17px;
            margin: 15px 0;
            line-height: 1.8;
            font-weight: 500;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.8);
        }
        
        .chatbox strong {
            color: #00d4ff;
            font-weight: 700;
            font-size: 18px;
        }

        /* ---- FIXED INPUT FIELD VISIBILITY ---- */
        .stTextInput input {
            background: rgba(255, 255, 255, 0.08) !important;
            border: 1px solid rgba(0, 212, 255, 0.3) !important;
            border-radius: 12px !important;
            color: #ffffff !important;
            padding: 14px 16px !important;
            font-size: 16px !important;
            caret-color: #00d4ff !important;
            transition: all 0.3s ease !important;
        }

        .stTextInput input:focus {
            border-color: #00d4ff !important;
            box-shadow: 0 0 15px rgba(0, 212, 255, 0.6) !important;
            background: rgba(0, 0, 0, 0.4) !important;
        }

        .stTextInput input::placeholder {
            color: rgba(200, 200, 255, 0.6) !important;
            font-weight: 400 !important;
        }

        .stTextInput input:focus::placeholder {
            color: rgba(0, 212, 255, 0.5) !important;
        }

        /* ---- FORM BUTTON ---- */
        .stButton button[kind="primary"] {
            background: linear-gradient(135deg, #00d4ff 0%, #7b2ff7 100%) !important;
            border: none !important;
            border-radius: 15px !important;
            padding: 12px 40px !important;
            font-weight: 700 !important;
            font-size: 16px !important;
            transition: all 0.3s ease !important;
        }
        
        .stButton button[kind="primary"]:hover {
            transform: translateY(-3px) !important;
            box-shadow: 0 10px 30px rgba(0, 212, 255, 0.5) !important;
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

# ---- NAVIGATION BUTTONS ----
nav1, nav2, nav3, nav4, nav5 = st.columns([1, 1, 1, 1, 1])
with nav1:
    if st.button("🏠 Home", use_container_width=True, key="nav_home"):
        go_to_home()
with nav2:
    if st.button("👥 About", use_container_width=True, key="nav_about"):
        go_to_about()
with nav3:
    st.button("🛠️ Services", use_container_width=True, key="nav_services")
with nav4:
    st.button("💼 Career", use_container_width=True, key="nav_career")
with nav5:
    st.button("📞 Contact", use_container_width=True, key="nav_contact")

# ---- HEADER ----
st.markdown("<h3>💼 Our Services</h3>", unsafe_allow_html=True)

# ---- FETCH SERVICES (Auto-Load Once) ----
if "services" not in st.session_state:
    display_loading()
    response = call_api("/api/services")
    st.session_state["services"] = response.get("services", [])

services = st.session_state["services"]

if services:
    for s in services:
        st.markdown(
            f"""
            <div class='service-card'>
                <h4>{s['title']}</h4>
                <p>{s['desc']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
else:
    st.warning("No services found. Try reloading the page.")

# ---- CHATBOT SECTION ----
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h3>💬 Chat With Us</h3>", unsafe_allow_html=True)
st.markdown("<p class='chat-intro'>Ask about our services or get instant info through our AI chatbot.</p>", unsafe_allow_html=True)

with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Your Message:", placeholder="Type your question here...")
    submitted = st.form_submit_button("Send")
    if submitted and user_input.strip():
        display_loading()
        response = call_api("/api/chatbot", data={"question": user_input})
        bot_reply = response.get("response", "I'm currently unavailable. Please try again later.")
        st.markdown(
            f"<div class='chatbox'><p><strong>You:</strong> {user_input}</p><p><strong>Bot:</strong> {bot_reply}</p></div>",
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
