from flask import Blueprint, request, jsonify
from services.ai_utils import ai_parse_resume, ai_job_fit
from services.db_utils import save_resume
from services.email_utils import generate_auto_reply
from models import Session
from models import Resume
from datetime import datetime

careers_bp = Blueprint('careers', __name__, url_prefix='/api/careers')

# --- Mock Job Listings (in real case, from DB or admin control) ---
JOBS = [
    {"id": 1, "title": "AI Engineer", "desc": "Develop AI-powered solutions and models for enterprise clients."},
    {"id": 2, "title": "Full-Stack Developer", "desc": "Build scalable web platforms using Flask, React, and Streamlit."},
    {"id": 3, "title": "Data Analyst", "desc": "Interpret data and generate actionable business insights."},
]

@careers_bp.route('/jobs', methods=['GET'])
def get_jobs():
    """Fetch dynamic job listings."""
    return jsonify({"jobs": JOBS})


@careers_bp.route('/apply', methods=['POST'])
def apply_job():
    """Handle candidate job applications and AI auto-replies."""
    try:
        data = request.get_json(force=True)
        name = data.get("name", "").strip()
        email = data.get("email", "").strip()
        job_id = int(data.get("job_id", 0))
        resume_text = data.get("resume", "").strip()

        # Validate input
        if not all([name, email, resume_text, job_id]):
            return jsonify({"error": "All fields are required."}), 400

        # Get job description from mock data
        job = next((j for j in JOBS if j["id"] == job_id), None)
        if not job:
            return jsonify({"error": "Invalid job selected."}), 404

        # AI Analysis
        parsed = ai_parse_resume(resume_text)
        score, notes = ai_job_fit(resume_text, job["desc"])

        # Save in database
        save_resume(name, email, resume_text, score, notes)

        # AI-powered email reply
        ai_reply = generate_auto_reply(name, f"Application for {job['title']}", email)

        return jsonify({
            "message": "Application submitted successfully.",
            "parsed": parsed,
            "score": score,
            "notes": notes,
            "auto_reply": ai_reply
        })

    except Exception as e:
        print(f"Career Apply Error: {e}")
        return jsonify({"error": str(e)}), 500


@careers_bp.route('/applications', methods=['GET'])
def admin_get_applications():  # ✅ renamed here
    """Return all candidate applications for admin dashboard."""
    try:
        session = Session()
        resumes = session.query(Resume).all()
        session.close()

        data = [
            {
                "id": r.id,
                "name": r.name,
                "email": r.email,
                "score": r.score,
                "notes": r.notes,
                "created_at": r.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            }
            for r in resumes
        ]

        return jsonify({"applications": data})
    except Exception as e:
        print(f"Error fetching applications: {e}")
        return jsonify({"error": str(e)}), 500
