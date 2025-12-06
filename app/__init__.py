# app/__init__.py
import os
from flask import Flask


def create_app():
    """Factory function to create and configure the Flask app."""
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static"
    )
    
    # Ensure storage directory exists
    storage_dir = os.path.join(os.path.dirname(__file__), "storage")
    os.makedirs(storage_dir, exist_ok=True)
    
    # Ensure data.json exists
    data_file = os.path.join(storage_dir, "data.json")
    if not os.path.exists(data_file):
        with open(data_file, "w", encoding="utf-8") as f:
            f.write("{}")
    
    # Register routes and error handlers
    from app.app import register_routes, register_error_handlers
    register_routes(app)
    register_error_handlers(app)
    
    return app


# Create app instance for Gunicorn
app = create_app()

