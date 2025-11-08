from flask import Blueprint, request, jsonify
from services.ai_utils import ai_build_resume

resume_bp = Blueprint('resume_builder', __name__)

@resume_bp.route('/api/resume/build', methods=['POST'])
def build_resume():
    try:
        # Parse JSON data safely
        data = request.get_json(force=True)

        if not data:
            return jsonify({"error": "No input data provided"}), 400

        # Build resume summary using AI helper
        resume_text = ai_build_resume(data)

        if not resume_text:
            return jsonify({"error": "AI did not return any summary"}), 500

        return jsonify({"resume_text": resume_text})

    except Exception as e:
        # Log for debugging
        print(f"Error in /api/resume/build: {e}")
        return jsonify({"error": str(e)}), 500
