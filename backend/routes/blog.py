from flask import Blueprint, jsonify, request
from datetime import datetime
from services.ai_utils import ai_summarize

blog_bp = Blueprint("blog", __name__, url_prefix="/api/blog")

# Temporary in-memory store
BLOG_POSTS = []

# -------------------------------------------------
# Get All Blog Posts
# -------------------------------------------------
@blog_bp.route("", methods=["GET"])
def get_blogs():
    return jsonify({"blogs": BLOG_POSTS})


# -------------------------------------------------
# Add a New Blog Post (Admin only)
# -------------------------------------------------
@blog_bp.route("/add", methods=["POST"])
def add_blog():
    try:
        data = request.get_json(force=True)
        title = data.get("title")
        author = data.get("author", "Mastersolis Team")
        content = data.get("content")

        if not title or not content:
            return jsonify({"error": "Title and content required"}), 400

        summary = ai_summarize(content)

        blog_entry = {
            "id": len(BLOG_POSTS) + 1,
            "title": title,
            "author": author,
            "content": content,
            "summary": summary,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        BLOG_POSTS.append(blog_entry)

        return jsonify({"message": "Blog added successfully!", "summary": summary})

    except Exception as e:
        print(f"Blog add error: {e}")
        return jsonify({"error": str(e)}), 500


# -------------------------------------------------
# Summarize a Specific Blog Post
# -------------------------------------------------
@blog_bp.route("/summarize", methods=["POST"])
def summarize_blog():
    try:
        data = request.get_json(force=True)
        text = data.get("text", "")
        if not text:
            return jsonify({"error": "No text provided"}), 400

        summary = ai_summarize(text)
        return jsonify({"summary": summary})
    except Exception as e:
        print(f"Blog summarize error: {e}")
        return jsonify({"error": str(e)}), 500
