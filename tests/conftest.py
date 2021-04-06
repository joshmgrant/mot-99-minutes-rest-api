import pytest
from api_helper import API

@pytest.fixture
def saucelog():
    return API("")