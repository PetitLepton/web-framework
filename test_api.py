import pytest
from api import API


@pytest.fixture
def api():
    return API()


def test_add_route(api):
    @api.route("/home")
    def home(request, response):
        response.text = "Test for adding a route"

    with pytest.raises(AssertionError):

        @api.route("/home")
        def home(request, response):
            response.text = "Test for adding a route"
