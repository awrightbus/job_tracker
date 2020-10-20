import pytest
from app import app


def test_addJob_page():
    """
    GIVEN a flask application
    When  the '/addjob' page is requested (GET)
    THEN check if the responce is valid 
    """
    with app.test_client() as client:
        responce = client.get('/addjob')
        assert responce.status_code == 200
        assert b'Company Name' in responce.data
        assert b'Position' in responce.data
        assert b'Follow Up Steps' in responce.data
        assert b'Date Applied' in responce.data



def test_post_addJob_page():
    """
    Given a flask application
    Wheen the '/addjob' page is requested (POST)
    THEN check that the user is redirected to '/applied'

    """
    with app.test_client() as client:
        responce = client.post('/addjob',
        
        data={
            'cname': 'apple',
            'position': 'software engineer',
            'followUp': 'call them back on Monday',
            'appliedDate': '12/12/2018',
        }, follow_redirects=True)

        assert responce.status_code == 200
        assert b'apple' in responce.data



