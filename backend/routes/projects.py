from flask import Blueprint, jsonify, request
from services.ai_utils import ai_projects_content, ai_summarize

projects_bp = Blueprint("projects", __name__, url_prefix="/api/projects")

@projects_bp.route("", methods=["GET"])
def get_projects():
    """Return all projects with tags."""
    projects = ai_projects_content()
    return jsonify({"projects": projects})

@projects_bp.route("/filter", methods=["POST"])
def filter_projects():
    """Filter projects by tags."""
    data = request.get_json()
    selected_tags = data.get("tags", [])
    all_projects = ai_projects_content()

    if not selected_tags:
        return jsonify({"projects": all_projects})

    filtered = [
        p for p in all_projects if any(tag in p["tags"] for tag in selected_tags)
    ]
    return jsonify({"projects": filtered})

@projects_bp.route("/summarize", methods=["POST"])
def summarize_project():
    """Generate AI summary for a given project description."""
    data = request.get_json()
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "Missing text"}), 400

    summary = ai_summarize(text)
    return jsonify({"summary": summary})
