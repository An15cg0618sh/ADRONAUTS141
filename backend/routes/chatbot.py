from flask import Blueprint, jsonify, request
from openai import OpenAI

chatbot_bp = Blueprint("chatbot", __name__, url_prefix="/api/chatbot")

# ✅ Directly use your OpenAI API key here (since you’re not using .env)
client = OpenAI(api_key="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")

# Company context for smarter replies
company_context = """
You are the Mastersolis Infotech AI assistant.
Mastersolis Infotech is an AI-driven software company specializing in web development,
machine learning, data analytics, and intelligent automation.

Your role:
- Help users learn about company services, internships, and AI products.
- Always respond politely and professionally.
- If a question is irrelevant, redirect them to company-related topics politely.
"""

@chatbot_bp.route("", methods=["POST"])
def chatbot_reply():
    data = request.get_json()

    if not data or "question" not in data:
        return jsonify({"error": "Missing 'question' field"}), 400

    question = data["question"].strip()
    if not question:
        return jsonify({"response": "Please ask a question."})

    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": company_context},
                {"role": "user", "content": question},
            ],
            max_tokens=200,
            temperature=0.6,
        )
        reply = completion.choices[0].message.content.strip()
        return jsonify({"response": reply})

    except Exception as e:
        print(f"Chatbot error: {e}")
        return jsonify({
            "error": str(e),
            "response": "Sorry, I’m currently unavailable. Please try again later."
        }), 500