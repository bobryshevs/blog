from repositories.post_repository import PostRepository
import mock
from datetime import datetime
from bson.objectid import ObjectId
from pymongo import MongoClient
from models import Post
from translators import PostTranslator
from mock import (
    Mock, 
    MagicMock
)
import pytest
# from repositories import PostRepository 

@pytest.fixture(scope="function")
def client():
    mock = Mock()
    # coll.find_one = MagicMock(side_effect=["mocked once", "mocked twice!"])
    return mock


@pytest.fixture(scope="function")
def get_by_id_documents(client):
    coll = client.blog_database.posts
    documents = [
        {
            "_id": ObjectId("6111371a6e34b54502afbf3d"),
            "text": "first_document",
            "author": "Sviat",
            "date_of_creation": datetime(2021, 8, 9, 17, 11, 37, 200000)
        },
        {
            "_id": ObjectId("61113c30950e7e9fe536770e"),
            "text": "second_document",
            "author": "Nick",
            "date_of_creation": datetime(2021, 8, 9, 16, 10, 37, 200000)
        },
    ]
    coll.find_one = MagicMock(side_effect=documents)
    return documents


@pytest.fixture(scope='function')
def repository(client):
    return PostRepository(client=client, translator=PostTranslator())

def test_get_by_id(repository, get_by_id_documents):
    expected = get_by_id_documents
    result = []
    

