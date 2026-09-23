"""
Tests unitaires pytest pour l'API Flask.
"""

from app.app import create_app


def test_index_returns_200():
    app = create_app()
    client = app.test_client()

    res = client.get("/")
    assert res.status_code == 200
    assert res.get_json()["message"] == "Hello from secure CI pipeline"
