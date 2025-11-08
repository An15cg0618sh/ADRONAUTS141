from openai import OpenAI
import random

# -------------------------------------
# Initialize OpenAI client (local key)
# -------------------------------------
client = OpenAI(api_key="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")

# ===========================================================
# =============== GENERAL AI UTILITIES ======================
# ===========================================================

# ---- Tagline Generator (GPT-based) ----
def ai_tagline_gpt():
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": "Generate a catchy tagline for Mastersolis Infotech, an AI-powered company."}
            ],
            max_tokens=50,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"AI Tagline error: {e}")
        return "Mastersolis Infotech – Empowering Intelligence."


# ---- Text Summarizer ----
def ai_summarize(text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": f"Summarize this text concisely: {text}"}
            ],
            max_tokens=120,
            temperature=0.6,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"AI Summarize error: {e}")
        return "Unable to summarize at the moment."


# ---- Resume Parser ----
def ai_parse_resume(resume_text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": f"Extract skills, experience, and education from this resume: {resume_text}"}
            ],
            max_tokens=200,
            temperature=0.5,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"AI Resume Parse error: {e}")
        return "Could not parse resume."


# ---- Job Fit Evaluator ----
def ai_job_fit(resume_text, job_desc):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": f"Compare this resume to the job description and give a fit score (0–100%) and notes:\nResume: {resume_text}\nJob: {job_desc}"}
            ],
            max_tokens=200,
            temperature=0.6,
        )

        content = response.choices[0].message.content.strip()
        lines = content.split('\n')
        score = int(lines[0].split('%')[0]) if '%' in lines[0] else 50
        notes = '\n'.join(lines[1:])
        return score, notes
    except Exception as e:
        print(f"AI Job Fit error: {e}")
        return 0, "Unable to evaluate job fit."


# ---- Chatbot ----
def ai_chatbot(question):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": f"Answer as a company chatbot for Mastersolis Infotech: {question}"}
            ],
            max_tokens=200,
            temperature=0.6,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"AI Chatbot error: {e}")
        return "I'm currently unavailable. Please try again later."


# ---- Resume Builder ----
def ai_build_resume(data):
    try:
        education = data.get("education", "")
        skills = data.get("skills", "")
        experience = data.get("experience", "")

        if not any([education, skills, experience]):
            return "Please provide some details to build the resume."

        prompt = f"""
        Create a professional resume summary based on the following details:
        Education: {education}
        Skills: {skills}
        Experience: {experience}
        """

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=250,
            temperature=0.6,
        )

        return completion.choices[0].message.content.strip()

    except Exception as e:
        print(f"AI Resume Builder error: {e}")
        return "Error generating resume. Please try again."


# ---- Admin Digest ----
def ai_admin_digest():
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": "Summarize recent activity for Mastersolis admin dashboard."}
            ],
            max_tokens=150,
            temperature=0.5,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"AI Admin Digest error: {e}")
        return "No recent updates found."


# ===========================================================
# =============== HOMEPAGE UTILITIES =========================
# ===========================================================

def ai_tagline_local():
    """Fallback/local tagline generator"""
    taglines = [
        "Building the Future with Intelligent Innovation.",
        "Empowering Businesses through AI-Driven Solutions.",
        "Transforming Ideas into Intelligent Experiences.",
        "Smart Tech. Smarter Tomorrow."
    ]
    return random.choice(taglines)


def ai_highlights():
    """Static homepage highlights"""
    highlights = [
        "🌐 Full-stack Web & App Development",
        "🤖 AI & Machine Learning Integration",
        "📈 Data Analytics & Automation Tools",
        "💼 Career and Resume Intelligence"
    ]
    return highlights


# ===========================================================
# =============== ABOUT PAGE UTILITIES =======================
# ===========================================================

def ai_about_content():
    """Generate company mission, vision, values, and team info."""
    try:
        mission = "To harness the power of Artificial Intelligence and innovation to create intelligent solutions that redefine industries."
        vision = "To be a global leader in AI-driven technology, enabling smarter, more efficient, and more connected businesses."
        values = [
            "💡 Innovation — Pushing the boundaries of technology.",
            "🤝 Integrity — Building trust through transparency.",
            "🚀 Excellence — Delivering high-quality solutions every time.",
            "🌍 Impact — Empowering society through meaningful AI applications."
        ]
        team = [
            {"name": "Arjun Mehta", "role": "Founder & CEO", "bio": "Visionary leader driving AI transformation across industries."},
            {"name": "Priya Sharma", "role": "Head of Engineering", "bio": "Specialist in scalable AI systems and full-stack architecture."},
            {"name": "Ravi Patel", "role": "Data Scientist", "bio": "Passionate about deep learning and data-driven innovation."},
            {"name": "Sneha Iyer", "role": "UI/UX Designer", "bio": "Designs intuitive interfaces blending creativity with function."}
        ]
        milestones = [
            {"year": "2020", "event": "Founded Mastersolis Infotech with a mission to revolutionize AI-driven software."},
            {"year": "2022", "event": "Launched first AI-powered resume analysis platform."},
            {"year": "2023", "event": "Partnered with top tech firms for intelligent automation solutions."},
            {"year": "2025", "event": "Expanding globally with next-gen AI infrastructure."}
        ]
        return {"mission": mission, "vision": vision, "values": values, "team": team, "milestones": milestones}
    except Exception as e:
        print(f"AI About Content Error: {e}")
        return {"mission": "", "vision": "", "values": [], "team": [], "milestones": []}


def ai_services_content():
    try:
        services = [
            {
                "title": "🌐 Full-Stack Web & App Development",
                "desc": "We build responsive, secure, and high-performance web and mobile apps using Flask, Streamlit, and React."
            },
            {
                "title": "🤖 AI & Machine Learning Solutions",
                "desc": "We create intelligent models for NLP, automation, and analytics that enhance decision-making."
            },
            {
                "title": "📈 Data Analytics & Visualization",
                "desc": "We turn data into actionable insights using dashboards and visual reports."
            },
            {
                "title": "⚙️ Intelligent Automation",
                "desc": "Our automation systems simplify business operations with seamless AI-driven process optimization."
            },
            {
                "title": "💼 Career & Recruitment Automation",
                "desc": "Smart resume analysis and job-fit predictions to help businesses recruit faster and better."
            },
            {
                "title": "🚀 SEO & Digital Optimization",
                "desc": "Boost your online presence with AI-powered SEO strategies and performance monitoring."
            }
        ]
        return {"services": services}
    except Exception as e:
        print(f"AI Services Content Error: {e}")
        return {"services": []}


# ===========================================================
# =============== PROJECTS PAGE UTILITIES ===================
# ===========================================================

def ai_projects_content():
    """List of company projects with tags and short descriptions."""
    try:
        projects = [
            {
                "title": "AI-Powered Resume Builder",
                "desc": "An intelligent system that generates professional resumes using NLP and GPT models.",
                "tags": ["AI", "NLP", "Automation"]
            },
            {
                "title": "Recruitment Automation Dashboard",
                "desc": "Streamlined hiring with job-fit prediction models and resume parsing.",
                "tags": ["Automation", "Analytics", "Flask"]
            },
            {
                "title": "Data Visualization Suite",
                "desc": "Interactive data dashboards built using Streamlit and Plotly for business insights.",
                "tags": ["Data", "Visualization", "Streamlit"]
            },
            {
                "title": "SEO Analytics Platform",
                "desc": "AI-driven SEO analyzer for performance tracking and optimization recommendations.",
                "tags": ["AI", "SEO", "Web"]
            },
            {
                "title": "Chatbot for Business Automation",
                "desc": "Conversational AI chatbot that automates FAQs and lead engagement.",
                "tags": ["Chatbot", "AI", "Web"]
            },
            {
                "title": "Smart Attendance System",
                "desc": "Face-recognition attendance tracker using computer vision and ML.",
                "tags": ["AI", "Vision", "ML"]
            }
        ]
        return projects
    except Exception as e:
        print(f"AI Projects Content Error: {e}")
        return []
