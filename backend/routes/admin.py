from flask import Blueprint, request, jsonify
from models import Session, Resume, Contact

admin_bp = Blueprint("admin", __name__, url_prefix="/api/admin")

# ✅ Define static credentials (you can change these)
ADMIN_USERNAME = "ananya"   # all lowercase for consistent matching
ADMIN_PASSWORD = "admin123"
ADMIN_TOKEN = "mastersolis_admin_token_2025"

# ---------------------------------------------------
# 🔐 LOGIN ROUTE
# ---------------------------------------------------
@admin_bp.route("/login", methods=["POST"])
def admin_login():
    try:
        data = request.get_json(force=True)

        username = data.get("username", "").strip().lower()   # force lowercase
        password = data.get("password", "").strip()

        print(f"DEBUG: Received username={username}, password={password}")  # helpful debug line

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            return jsonify({"token": ADMIN_TOKEN})
        else:
            print("DEBUG: Invalid credentials entered")
            return jsonify({"error": "Invalid credentials"}), 401

    except Exception as e:
        print(f"Admin Login Error: {e}")
        return jsonify({"error": str(e)}), 500


# ---------------------------------------------------
# 📊 ADMIN SUMMARY ROUTE
# ---------------------------------------------------
@admin_bp.route("/summary", methods=["GET"])
def admin_summary():
    try:
        session = Session()
        resume_count = session.query(Resume).count()
        contact_count = session.query(Contact).count()
        session.close()

        digest = (
            f"📄 Total Resumes: {resume_count}\n"
            f"📬 Total Contacts: {contact_count}\n"
            f"✅ System running smoothly."
        )

        return jsonify({
            "resume_count": resume_count,
            "contact_count": contact_count,
            "digest": digest
        })
    except Exception as e:
        print(f"Admin Summary Error: {e}")
        return jsonify({"error": str(e)}), 500
