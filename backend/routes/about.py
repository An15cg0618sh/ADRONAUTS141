from flask import Blueprint, jsonify
from services.ai_utils import ai_about_content   # ✅ correct function name

about_bp = Blueprint('about', __name__, url_prefix='/api/about')

@about_bp.route('', methods=['GET'])
def get_about_data():
    """Return AI-generated About page content (team, milestones, mission, vision, values)."""
    data = ai_about_content()
    return jsonify(data)
