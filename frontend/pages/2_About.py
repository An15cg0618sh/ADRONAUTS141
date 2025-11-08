import streamlit as st
from utils.api_utils import call_api
from utils.ui_helpers import display_loading

# ---- NAVIGATION FUNCTION ----
def go_to_home():
    st.switch_page("Home.py")

# ---- PAGE CONFIG ----
st.set_page_config(page_title="About - Mastersolis Infotech", layout="wide", initial_sidebar_state="collapsed")

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
            padding: 80px 40px;
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
            font-size: 58px;
            margin-bottom: 15px;
            animation: glow 2s ease-in-out infinite;
        }
        
        @keyframes glow {
            0%, 100% { filter: drop-shadow(0 0 20px rgba(0, 212, 255, 0.5)); }
            50% { filter: drop-shadow(0 0 40px rgba(123, 47, 247, 0.8)); }
        }
        
        .hero p {
            position: relative;
            z-index: 1;
            font-size: 22px;
            opacity: 0.95;
            font-weight: 500;
            letter-spacing: 1px;
        }

        /* ---- SECTION TITLE ---- */
        .section-title {
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
            animation: fadeInUp 1.2s ease-out;
        }

        /* ---- CARDS ---- */
        .card {
            background: linear-gradient(145deg, rgba(0, 212, 255, 0.08), rgba(123, 47, 247, 0.08));
            backdrop-filter: blur(15px);
            border: 1px solid rgba(0, 212, 255, 0.3);
            border-radius: 25px;
            padding: 35px 25px;
            margin: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
            transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            position: relative;
            overflow: hidden;
            height: 100%;
        }
        
        .card::before {
            content: '';
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: linear-gradient(135deg, transparent, rgba(0, 212, 255, 0.1), transparent);
            transform: translateX(-100%);
            transition: transform 0.6s;
        }

        .card:hover {
            transform: translateY(-15px) scale(1.03);
            box-shadow: 0 20px 50px rgba(0, 212, 255, 0.5);
            border-color: #00d4ff;
        }
        
        .card:hover::before {
            transform: translateX(100%);
        }

        .card h3 {
            color: #00d4ff !important;
            font-size: 28px !important;
            font-weight: 800 !important;
            margin-bottom: 15px !important;
            position: relative;
            z-index: 1;
        }

        .card p, .card li {
            color: #e0e7ff !important;
            font-size: 18px !important;
            line-height: 2 !important;
            position: relative;
            z-index: 1;
            font-weight: 500;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.8);
        }
        
        .card ul {
            list-style: none;
            padding-left: 0;
        }
        
        .card ul li::before {
            content: "✦ ";
            color: #00d4ff;
            font-weight: bold;
            margin-right: 10px;
            font-size: 20px;
            text-shadow: 0 0 10px rgba(0, 212, 255, 0.8);
        }

        /* ---- TEAM CARD ---- */
        .team-card {
            background: linear-gradient(145deg, rgba(0, 212, 255, 0.08), rgba(123, 47, 247, 0.08));
            backdrop-filter: blur(15px);
            border: 1px solid rgba(0, 212, 255, 0.3);
            border-radius: 25px;
            padding: 30px 20px;
            margin: 15px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
            transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            position: relative;
            overflow: hidden;
        }
        
        .team-card::before {
            content: '';
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: linear-gradient(135deg, transparent, rgba(123, 47, 247, 0.15), transparent);
            transform: translateX(-100%);
            transition: transform 0.6s;
        }

        .team-card:hover {
            transform: translateY(-12px) scale(1.05);
            box-shadow: 0 20px 50px rgba(123, 47, 247, 0.5);
            border-color: #7b2ff7;
        }
        
        .team-card:hover::before {
            transform: translateX(100%);
        }

        .team-card h4 {
            color: #00d4ff !important;
            font-size: 24px !important;
            font-weight: 800 !important;
            margin-bottom: 8px !important;
            position: relative;
            z-index: 1;
        }

        .team-card p {
            color: #ffffff !important;
            font-size: 17px !important;
            margin: 8px 0 !important;
            position: relative;
            z-index: 1;
            font-weight: 600;
            text-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
        }
        
        .team-card p b {
            color: #c4b5fd !important;
            font-size: 19px !important;
            font-weight: 800;
            text-shadow: 0 2px 10px rgba(123, 47, 247, 0.6);
        }

        /* ---- MILESTONE ---- */
        .milestone {
            background: linear-gradient(145deg, rgba(0, 212, 255, 0.08), rgba(123, 47, 247, 0.08));
            backdrop-filter: blur(15px);
            border-left: 5px solid #00d4ff;
            border-radius: 15px;
            padding: 20px 25px;
            margin-bottom: 20px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
            border: 1px solid rgba(0, 212, 255, 0.3);
            transition: all 0.4s ease;
            position: relative;
            overflow: hidden;
        }
        
        .milestone::before {
            content: '';
            position: absolute;
            left: 0; top: 0;
            width: 5px; height: 100%;
            background: linear-gradient(180deg, #00d4ff, #7b2ff7);
            box-shadow: 0 0 15px rgba(0, 212, 255, 0.8);
        }

        .milestone:hover {
            transform: translateX(10px);
            box-shadow: 0 10px 35px rgba(0, 212, 255, 0.4);
            border-color: #00d4ff;
        }

        .milestone b {
            color: #00d4ff !important;
            font-size: 20px !important;
            font-weight: 900 !important;
            text-shadow: 0 2px 10px rgba(0, 212, 255, 0.6);
        }
        
        .milestone {
            color: #ffffff !important;
            font-size: 18px !important;
            font-weight: 600;
            text-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
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

nav1, nav2, nav3, nav4, nav5 = st.columns([1, 1, 1, 1, 1])
with nav1:
    if st.button("🏠 Home", use_container_width=True, key="nav_home"):
        go_to_home()
with nav2:
    st.button("👥 About", use_container_width=True, key="nav_about")
with nav3:
    st.button("🛠️ Services", use_container_width=True, key="nav_services")
with nav4:
    st.button("💼 Career", use_container_width=True, key="nav_career")
with nav5:
    st.button("📞 Contact", use_container_width=True, key="nav_contact")

# ---- HERO SECTION ----
st.markdown(
    """
    <div class="hero">
        <h1>About Mastersolis Infotech</h1>
        <p>🚀 Driving innovation through AI, data, and human creativity</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ---- FETCH BACKEND DATA ----
if "about_data" not in st.session_state:
    display_loading()
    st.session_state["about_data"] = call_api("/api/about")

about_data = st.session_state["about_data"]

mission = about_data.get("mission", "No mission available.")
vision = about_data.get("vision", "No vision available.")
values = about_data.get("values", [])
team = about_data.get("team", [])
milestones = about_data.get("milestones", [])

# ---- MISSION / VISION / VALUES ----
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>🌍 Our Mission, Vision & Values</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(
        f"""
        <div class='card'>
            <h3>🚀 Mission</h3>
            <p>{mission}</p>
        </div>
        """, unsafe_allow_html=True
    )
with col2:
    st.markdown(
        f"""
        <div class='card'>
            <h3>🎯 Vision</h3>
            <p>{vision}</p>
        </div>
        """, unsafe_allow_html=True
    )
with col3:
    st.markdown("<div class='card'><h3>💡 Values</h3><ul>", unsafe_allow_html=True)
    for v in values:
        st.markdown(f"<li>{v}</li>", unsafe_allow_html=True)
    st.markdown("</ul></div>", unsafe_allow_html=True)

# ---- TEAM SECTION ----
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>🤖 Meet Our Team</div>", unsafe_allow_html=True)
if team:
    cols = st.columns(2)
    for i, member in enumerate(team):
        with cols[i % 2]:
            st.markdown(
                f"""
                <div class='team-card'>
                    <h4>{member['name']}</h4>
                    <p><b>{member['role']}</b></p>
                    <p>{member['bio']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
else:
    st.info("No team data available. Please check the backend response.")

# ---- MILESTONES SECTION ----
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>🏆 Company Milestones</div>", unsafe_allow_html=True)
if milestones:
    for m in milestones:
        st.markdown(f"<div class='milestone'><b>{m['year']}</b> — {m['event']}</div>", unsafe_allow_html=True)
else:
    st.info("No milestones available at the moment.")

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