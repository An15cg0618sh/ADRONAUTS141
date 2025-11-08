import streamlit as st
from utils.api_utils import call_api
from utils.ui_helpers import display_loading
import re

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Contact - Mastersolis Infotech", layout="wide")

# ---- STYLES ----
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 25%, #2a1f4a 50%, #1a1f3a 75%, #0a0e27 100%);
        background-attachment: fixed;
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        color: white;
    }

    @keyframes gradientShift {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }

    #MainMenu, footer, header {visibility: hidden;}

    h1 {
        text-align: center;
        color: #ffffff;
        font-weight: 900;
        text-shadow: 0 0 25px rgba(0, 212, 255, 0.6);
        margin-bottom: 20px;
        font-size: 3rem;
    }

    p {
        color: #cce6ff;
        text-align: center;
        font-size: 16px;
    }

    .form-container {
        background: linear-gradient(145deg, rgba(0, 212, 255, 0.08), rgba(123, 47, 247, 0.08));
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 40px 50px;
        width: 60%;
        margin: auto;
        box-shadow: 0 15px 45px rgba(0, 212, 255, 0.2);
        border: 1px solid rgba(0, 212, 255, 0.3);
        animation: fadeInUp 1.2s ease-out;
    }

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(50px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .stTextInput input, .stTextArea textarea, .stSelectbox select {
        background: rgba(255, 255, 255, 0.08) !important;
        border: 1px solid rgba(0,212,255,0.3) !important;
        border-radius: 12px !important;
        color: #ffffff !important;
        padding: 12px 14px !important;
        font-size: 16px !important;
        caret-color: #00d4ff !important;
        transition: all 0.3s ease !important;
    }

    .stTextInput input:focus, .stTextArea textarea:focus, .stSelectbox select:focus {
        border-color: #00d4ff !important;
        box-shadow: 0 0 15px rgba(0,212,255,0.6) !important;
        background: rgba(0, 0, 0, 0.4) !important;
    }

    .stTextInput input::placeholder, .stTextArea textarea::placeholder {
        color: rgba(200, 220, 255, 0.6) !important;
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
        width: 100%;
    }

    .stButton button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 10px 30px rgba(0,212,255,0.5) !important;
    }

    .success-box {
        background: rgba(0, 212, 255, 0.1);
        border-left: 5px solid #00d4ff;
        padding: 15px;
        margin-top: 20px;
        border-radius: 10px;
        color: #e6f2ff;
        animation: slideIn 0.5s ease-out;
    }

    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-20px); }
        to { opacity: 1; transform: translateX(0); }
    }

    .contact-info {
        display: flex;
        justify-content: space-around;
        margin: 40px auto;
        max-width: 900px;
        flex-wrap: wrap;
    }

    .info-card {
        background: linear-gradient(145deg, rgba(0, 212, 255, 0.1), rgba(123, 47, 247, 0.1));
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 25px;
        margin: 10px;
        flex: 1;
        min-width: 250px;
        border: 1px solid rgba(0, 212, 255, 0.2);
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .info-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0, 212, 255, 0.3);
    }

    .info-card h3 {
        color: #00d4ff;
        margin-bottom: 10px;
        font-size: 1.2rem;
    }

    .info-card p {
        color: #cce6ff;
        font-size: 14px;
    }

    .char-counter {
        text-align: right;
        color: rgba(200, 220, 255, 0.6);
        font-size: 12px;
        margin-top: 5px;
    }

    .error-text {
        color: #ff6b6b;
        font-size: 14px;
        margin-top: 5px;
    }

    @media (max-width: 768px) {
        .form-container {
            width: 90%;
            padding: 30px 25px;
        }
        
        h1 {
            font-size: 2rem;
        }
        
        .contact-info {
            flex-direction: column;
        }
    }
</style>
""", unsafe_allow_html=True)

# ---- HELPER FUNCTIONS ----
def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_name(name):
    """Validate name (at least 2 characters, only letters and spaces)"""
    return len(name.strip()) >= 2 and all(c.isalpha() or c.isspace() for c in name)

# ---- HEADER ----
st.markdown("<h1>✉️ Get in Touch</h1>", unsafe_allow_html=True)
st.markdown("<p>We'd love to hear from you! Send us your queries, ideas, or feedback below.</p>", unsafe_allow_html=True)

# ---- CONTACT INFO CARDS ----
st.markdown("""
<div class='contact-info'>
    <div class='info-card'>
        <h3>📧 Email Us</h3>
        <p>info@mastersolis.com</p>
        <p>support@mastersolis.com</p>
    </div>
    <div class='info-card'>
        <h3>📞 Call Us</h3>
        <p>+1 (555) 123-4567</p>
        <p>Mon-Fri: 9AM - 6PM EST</p>
    </div>
    <div class='info-card'>
        <h3>📍 Visit Us</h3>
        <p>123 Tech Street</p>
        <p>Innovation City, IC 12345</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ---- CONTACT FORM ----
with st.container():
    st.markdown("<div class='form-container'>", unsafe_allow_html=True)

    with st.form("contact_form"):
        # Name field with validation
        name = st.text_input("Full Name*", placeholder="Enter your name")
        
        # Email field with validation
        email = st.text_input("Email Address*", placeholder="Enter your email")
        
        # Subject/Category selector
        subject = st.selectbox(
            "Subject*",
            ["General Inquiry", "Technical Support", "Sales", "Partnership", "Feedback", "Other"]
        )
        
        # Message field with character counter
        message = st.text_area("Message*", placeholder="Type your message here...", height=150, max_chars=1000)
        
        # Show character count
        if message:
            char_count = len(message)
            st.markdown(f"<div class='char-counter'>{char_count}/1000 characters</div>", unsafe_allow_html=True)
        
        # Phone (optional)
        phone = st.text_input("Phone Number (Optional)", placeholder="+1 (555) 123-4567")
        
        submitted = st.form_submit_button("Send Message 🚀")

        if submitted:
            # Validation
            errors = []
            
            if not name.strip():
                errors.append("Name is required")
            elif not validate_name(name):
                errors.append("Please enter a valid name (at least 2 letters)")
            
            if not email.strip():
                errors.append("Email is required")
            elif not validate_email(email):
                errors.append("Please enter a valid email address")
            
            if not message.strip():
                errors.append("Message is required")
            elif len(message.strip()) < 10:
                errors.append("Message must be at least 10 characters long")
            
            if errors:
                for error in errors:
                    st.markdown(f"<div class='error-text'>⚠️ {error}</div>", unsafe_allow_html=True)
            else:
                display_loading()
                data = {
                    "name": name.strip(),
                    "email": email.strip(),
                    "subject": subject,
                    "message": message.strip(),
                    "phone": phone.strip() if phone else None
                }
                
                result = call_api("/api/contact", method="POST", data=data)

                if not result:
                    st.error("❌ No response from server. Please try again later.")
                elif "error" in result:
                    st.error(f"❌ Backend Error: {result['error']}")
                else:
                    st.success("✅ Message sent successfully! We'll get back to you soon.")
                    st.markdown(
                        f"""<div class='success-box'>
                            <strong>📨 Auto-reply:</strong><br>
                            {result.get('auto_reply', 'Thank you for contacting us. Our team will reach out soon!')}
                        </div>""",
                        unsafe_allow_html=True
                    )
                    st.balloons()
    
    st.markdown("</div>", unsafe_allow_html=True)

# ---- FOOTER INFO ----
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: rgba(200, 220, 255, 0.5); font-size: 14px;'>All fields marked with * are required</p>", unsafe_allow_html=True)