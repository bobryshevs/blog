import pytest
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
from translators import PostTranslator
from models import Post


@pytest.fixture(scope="function")
def post_translator():
    return PostTranslator()


def test_to_document_valid(post_translator):
    post = Post(
        text="Text for post",
        author="Sviatoslav Bobryshev",
        date_of_creation=datetime(2021, 8, 11, 16, 52, 25, 551959)
    )

    document = {
        "text": "Text for post",
        "author": "Sviatoslav Bobryshev",
        "date_of_creation": datetime(2021, 8, 11, 16, 52, 25, 551959)
    }

    result = post_translator.to_document(post)

    assert isinstance(result, dict) is True
    assert document['text'] == result['text']
    assert document['author'] == result['author']
    assert document['date_of_creation'] == result['date_of_creation']


def test_from_document_valid(post_translator):
    document = {
        "_id": ObjectId('6112f2704808cefd2cf9ccfb'),
        "text": "Text from document valid",
        "author": "Sviatoslav",
        "date_of_creation": datetime(2021, 8, 11, 0, 41, 4, 327873)}

    result = post_translator.from_document(document)

    assert isinstance(result, Post) is True
    assert document['_id'] == result.id
    assert document['text'] == result.text
    assert document['author'] == result.author
    assert document['date_of_creation'] == result.date_of_creation
