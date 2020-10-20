import pytest
from project import create_app


@pytest.fixture(scope='module')
def test_client():
    flas_app = create_app('flask_test.cfg')
    fkas_app.config.from_object('config.TestingConfig')

    #create a test client using the flask app configured for testing
    testing_client = flask_app.test_client()

    return testing_client