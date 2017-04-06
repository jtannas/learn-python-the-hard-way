"""Testing bin/app.py"""

### IMPORTS ###################################################################
from nose.tools import *
from bin.app import app
from tests.tools import assert_response


### TESTS #####################################################################
def test_index():
    """Tests the index page"""

    # Check that we get a 404 on the / URL
    resp = app.request("/")
    assert_response(resp, status="404")

    # Test our first GET request to /hello
    resp = app.request("/hello")
    assert_response(resp)

    # Make sure default values work for the form
    data = {'name': "Zed", 'greet': "Hola"}
    resp = app.request("/hello", method="POST", data=data)
    assert_response(resp, contains="Zed")
