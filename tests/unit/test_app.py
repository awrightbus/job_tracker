import pytest
from app import app


def test_index_page():
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        responce = client.get('/')
        assert responce.status_code == 200
        assert b'Home Page' in responce.data


