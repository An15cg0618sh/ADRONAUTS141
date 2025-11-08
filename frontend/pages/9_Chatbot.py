import streamlit as st
from utils.api_utils import call_api

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Chatbot - Mastersolis Infotech",
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

    /* ---- SECTION HEADERS ---- */
    h3 {
        color: #00d4ff !important;
        font-size: 28px !important;
        font-weight: 800 !important;
        margin: 40px 0 25px 0 !important;
        text-shadow: 0 2px 10px rgba(0, 212, 255, 0.5);
    }

    /* ---- INPUT CONTAINER ---- */
    .input-container {
        background: linear-gradient(145deg, rgba(0, 212, 255, 0.08), rgba(123, 47, 247, 0.08));
        backdrop-filter: blur(15px);
        border: 1px solid rgba(0, 212, 255, 0.3);
        border-radius: 25px;
        padding: 30px;
        margin: 30px 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
        animation: fadeInUp 1s ease-out;
    }
    
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(50px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* ---- FORM STYLING ---- */
    .stTextInput input {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(0, 212, 255, 0.3) !important;
        border-radius: 15px !important;
        color: #ffffff !important;
        padding: 18px !important;
        font-size: 17px !important;
    }
    
    .stTextInput input:focus {
        border-color: #00d4ff !important;
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.4) !important;
    }
    
    .stTextInput input::placeholder {
        color: rgba(255, 255, 255, 0.4) !important;
    }

    /* ---- BUTTONS ---- */
    .stButton button {
        background: linear-gradient(135deg, #00d4ff 0%, #7b2ff7 100%) !important;
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
    
    .stButton button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 10px 30px rgba(0, 212, 255, 0.5) !important;
    }

    /* ---- SUGGESTED QUERIES ---- */
    .suggestion-btn {
        background: linear-gradient(145deg, rgba(0, 212, 255, 0.08), rgba(123, 47, 247, 0.08)) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(0, 212, 255, 0.3) !important;
        border-radius: 15px !important;
        padding: 12px 20px !important;
        color: #e0e7ff !important;
        font-size: 14px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        text-align: left !important;
        height: auto !important;
        white-space: normal !important;
        line-height: 1.5 !important;
    }
    
    .suggestion-btn:hover {
        background: linear-gradient(145deg, rgba(0, 212, 255, 0.15), rgba(123, 47, 247, 0.15)) !important;
        border-color: #00d4ff !important;
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 25px rgba(0, 212, 255, 0.4) !important;
    }

    /* ---- CHAT HISTORY ---- */
    .chat-history {
        background: linear-gradient(145deg, rgba(0, 212, 255, 0.05), rgba(123, 47, 247, 0.05));
        backdrop-filter: blur(15px);
        border: 1px solid rgba(0, 212, 255, 0.2);
        border-radius: 25px;
        padding: 30px;
        margin: 20px 0;
        max-height: 600px;
        overflow-y: auto;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    }
    
    /* Custom scrollbar */
    .chat-history::-webkit-scrollbar {
        width: 8px;
    }
    
    .chat-history::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
    }
    
    .chat-history::-webkit-scrollbar-thumb {
        background: rgba(0, 212, 255, 0.3);
        border-radius: 10px;
    }
    
    .chat-history::-webkit-scrollbar-thumb:hover {
        background: rgba(0, 212, 255, 0.5);
    }

    /* ---- CHAT MESSAGES ---- */
    .user-message {
        background: linear-gradient(145deg, rgba(0, 212, 255, 0.12), rgba(0, 212, 255, 0.08));
        border-left: 4px solid #00d4ff;
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
        box-shadow: 0 4px 15px rgba(0, 212, 255, 0.2);
        animation: slideInRight 0.4s ease-out;
    }
    
    @keyframes slideInRight {
        from { opacity: 0; transform: translateX(50px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    .user-message strong {
        color: #00d4ff !important;
        font-size: 18px !important;
        font-weight: 800 !important;
        display: block;
        margin-bottom: 8px;
    }
    
    .user-message p {
        color: #e0e7ff !important;
        font-size: 16px !important;
        line-height: 1.6 !important;
        margin: 0 !important;
        font-weight: 500 !important;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.8);
    }
    
    .bot-message {
        background: linear-gradient(145deg, rgba(123, 47, 247, 0.12), rgba(123, 47, 247, 0.08));
        border-left: 4px solid #7b2ff7;
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
        box-shadow: 0 4px 15px rgba(123, 47, 247, 0.2);
        animation: slideInLeft 0.4s ease-out;
    }
    
    @keyframes slideInLeft {
        from { opacity: 0; transform: translateX(-50px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    .bot-message strong {
        color: #a78bfa !important;
        font-size: 18px !important;
        font-weight: 800 !important;
        display: block;
        margin-bottom: 8px;
    }
    
    .bot-message p {
        color: #e0e7ff !important;
        font-size: 16px !important;
        line-height: 1.6 !important;
        margin: 0 !important;
        font-weight: 500 !important;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.8);
    }

    /* ---- EMPTY STATE ---- */
    .empty-state {
        text-align: center;
        padding: 60px 20px;
        color: rgba(255, 255, 255, 0.4);
        font-size: 18px;
        font-style: italic;
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
st.title("💬 Mastersolis Infotech Chatbot")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Predefined suggested queries
suggested_queries = [
    "What services does Mastersolis Infotech provide?",
    "How can I apply for an internship?",
    "Do you offer web development solutions?",
    "Tell me about AI projects at Mastersolis Infotech.",
    "How can I contact your support team?"
]

# ---- INPUT SECTION ----
st.markdown("<div class='input-container'>", unsafe_allow_html=True)
col1, col2 = st.columns([4, 1])
with col1:
    question = st.text_input("Ask a question", placeholder="Type your question here...", label_visibility="collapsed")
with col2:
    send_clicked = st.button("🚀 Send", use_container_width=True)

if send_clicked:
    if not question.strip():
        st.warning("⚠️ Please enter a question before sending.")
    else:
        with st.spinner("🤖 Thinking..."):
            response = call_api("/api/chatbot", method="POST", data={"question": question})
            if "error" in response:
                st.error(f"❌ Backend Error: {response['error']}")
            else:
                answer = response.get("response", "No response received.")
                st.session_state.chat_history.append((question, answer))
        st.rerun()
st.markdown("</div>", unsafe_allow_html=True)

# ---- SUGGESTED QUERIES ----
st.markdown("### 💡 Suggested Questions")
cols = st.columns(3)
for i, query in enumerate(suggested_queries):
    with cols[i % 3]:
        if st.button(query, key=f"suggest_{i}", help=query):
            with st.spinner("🤖 Thinking..."):
                response = call_api("/api/chatbot", method="POST", data={"question": query})
                if "error" in response:
                    st.error(f"❌ Backend Error: {response['error']}")
                else:
                    answer = response.get("response", "No response received.")
                    st.session_state.chat_history.append((query, answer))
            st.rerun()

# ---- CHAT HISTORY ----
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 🗨️ Chat History")

if st.session_state.chat_history:
    st.markdown("<div class='chat-history'>", unsafe_allow_html=True)
    for q, r in reversed(st.session_state.chat_history):  # Show newest first
        st.markdown(
            f"""
            <div class='user-message'>
                <strong>🧑 You:</strong>
                <p>{q}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            f"""
            <div class='bot-message'>
                <strong>🤖 Bot:</strong>
                <p>{r}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Clear history button
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()
else:
    st.markdown(
        "<div class='chat-history'><div class='empty-state'>💬 No messages yet. Start a conversation!</div></div>",
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
        <p>AI-Powered Customer Support 🤖</p>
    </div>
    """,
    unsafe_allow_html=True
)