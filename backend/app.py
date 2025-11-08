from flask import Flask
from flask_cors import CORS
from routes.home import home_bp
from routes.about import about_bp
from routes.services import services_bp
from routes.projects import projects_bp
from routes.contact import contact_bp
from routes.careers import careers_bp
from routes.admin import admin_bp
from routes.blog import blog_bp 
from routes.chatbot import chatbot_bp# ✅ new import

app = Flask(__name__)
CORS(app)

# Register all blueprints
app.register_blueprint(home_bp)
app.register_blueprint(about_bp)
app.register_blueprint(chatbot_bp)  # ✅ new chatbot blueprint
app.register_blueprint(services_bp)
app.register_blueprint(projects_bp)
app.register_blueprint(contact_bp)
app.register_blueprint(careers_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(blog_bp)  # ✅ new blog blueprint

if __name__ == "__main__":
    app.run(debug=True)
