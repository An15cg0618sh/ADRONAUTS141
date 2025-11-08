from flask import Blueprint, jsonify
from services.ai_utils import ai_services_content

services_bp = Blueprint('services', __name__, url_prefix='/api/services')

@services_bp.route('', methods=['GET'])
def get_services():
    data = ai_services_content()
    return jsonify(data)
