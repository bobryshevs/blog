from _pytest.config import main
from pymongo import MongoClient
from mock import Mock
import pytest
# from repositories import PostRepository 

@pytest.fixture(scope="function")
def client():
    mock = Mock()
    mock.str.return_value = '123'
    return mock


def test_first_mock(client):
    print(client.str())
    assert 0
