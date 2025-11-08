from flask import Blueprint, jsonify
from services.ai_utils import ai_tagline_gpt, ai_tagline_local, ai_highlights

home_bp = Blueprint('home', __name__)

@home_bp.route('/api/home_content', methods=['GET'])
def get_home_content():
    try:
        # Try AI tagline
        tagline = ai_tagline_gpt()
    except Exception as e:
        print(f"Falling back to local tagline due to: {e}")
        tagline = ai_tagline_local()

    highlights = ai_highlights()
    return jsonify({
        'tagline': tagline,
        'highlights': highlights
    })
