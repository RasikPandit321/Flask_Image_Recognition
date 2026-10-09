"""Tests for the Flask application's homepage."""


def test_homepage_loads(client):
    """Verify that the homepage loads successfully."""
    response = client.get("/")

    assert response.status_code == 200
    assert b"Hand Sign Digit" in response.data

def test_intentional_failure():
    """Demonstrate that CI detects a failing pytest test."""
    assert 1 == 2
