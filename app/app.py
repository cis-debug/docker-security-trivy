"""
Flask API (simple) - Mission 15

Objectif:
- Avoir une app minimale à tester et à dockeriser.
- On utilise une "app factory" (create_app) pour faciliter les tests.
"""

from flask import Flask, jsonify


def create_app() -> Flask:
    """Crée et configure l'application Flask."""
    app = Flask(__name__)

    @app.get("/")
    def index():
        # Endpoint simple pour vérifier que l'API tourne
        return jsonify(message="Hello from secure CI pipeline")

    return app


if __name__ == "__main__":
    # IMPORTANT en Docker: écouter sur 0.0.0.0
    create_app().run(host="0.0.0.0", port=5000)
