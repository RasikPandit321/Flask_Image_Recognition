"""Tests for the Flask application's homepage."""


def test_homepage_loads(client):
    """Verify that the homepage loads successfully."""
    response = client.get("/")

    assert response.status_code == 200
    assert b"Hand Sign Digit" in response.data
