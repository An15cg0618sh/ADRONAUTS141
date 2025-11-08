from flask import Blueprint, request, jsonify
from services.email_utils import generate_auto_reply
from services.db_utils import save_contact

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/api/contact', methods=['POST'])
def handle_contact():
    try:
        data = request.get_json(force=True)

        if not data:
            return jsonify({"error": "No input data provided"}), 400

        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        message = data.get('message', '').strip()

        if not all([name, email, message]):
            return jsonify({"error": "All fields (name, email, message) are required"}), 400

        # Save to database (wrap in try/except in db_utils too)
        try:
            save_contact(name, email, message)
        except Exception as e:
            print(f"Database save error: {e}")
            return jsonify({"error": "Failed to save contact."}), 500

        # Generate AI auto reply (safe fallback)
        try:
            auto_reply = generate_auto_reply(name, message, email)
        except Exception as e:
            print(f"Auto-reply generation error: {e}")
            auto_reply = "Thank you for reaching out! We’ll get back to you soon."

        return jsonify({"auto_reply": auto_reply})

    except Exception as e:
        print(f"Contact API error: {e}")
        return jsonify({"error": str(e)}), 500