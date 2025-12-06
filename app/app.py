# app/app.py
import os
import json
from datetime import datetime
from flask import render_template, request, redirect, url_for


def get_storage_path():
    """Get the path to storage/data.json."""
    return os.path.join(os.path.dirname(__file__), "storage", "data.json")


def load_messages():
    """Load messages from storage/data.json."""
    storage_path = get_storage_path()
    try:
        with open(storage_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_messages(messages):
    """Save messages to storage/data.json."""
    storage_path = get_storage_path()
    with open(storage_path, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)


def register_routes(app):
    """Register all routes."""
    
    @app.route("/")
    def index():
        """Render the index page."""
        return render_template("index.html")
    
    @app.route("/message", methods=["GET", "POST"])
    def message():
        """Handle GET (show form) and POST (save message)."""
        if request.method == "POST":
            username = request.form.get("username", "").strip()
            message_text = request.form.get("message", "").strip()
            
            if username and message_text:
                messages = load_messages()
                timestamp = str(datetime.now())
                messages[timestamp] = {
                    "username": username,
                    "message": message_text
                }
                save_messages(messages)
                return redirect(url_for("read"))
            else:
                # If validation fails, show form again (could add error message)
                return render_template("message.html")
        
        return render_template("message.html")
    
    @app.route("/read")
    def read():
        """Render the read page with all messages."""
        messages = load_messages()
        
        # Sort by timestamp (descending, newest first)
        sorted_messages = sorted(
            messages.items(),
            key=lambda x: x[0],
            reverse=True
        )
        
        return render_template("read.html", messages=sorted_messages)


def register_error_handlers(app):
    """Register error handlers."""
    
    @app.errorhandler(404)
    def not_found(error):
        """Handle 404 errors."""
        return render_template("error.html"), 404


if __name__ == "__main__":
    from app import create_app
    app = create_app()
    app.run(host="0.0.0.0", port=3000, debug=True)

