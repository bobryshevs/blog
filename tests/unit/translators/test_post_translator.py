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
    post = Post()
    post.title = "title"
    post.content = "content"
    post.author_id_id = ObjectId()
    document = {
        "title": post.title,
        "author_id": post.author_id,
        "content": post.content
    }

    result = post_translator.to_document(post)

    assert isinstance(result, dict) is True
    assert document["title"] == result["title"]
    assert document["author_id"] == result["author_id"]
    assert document["content"] == result["content"]


def test_from_document_valid(post_translator):
    document = {
        "_id": ObjectId("6112f2704808cefd2cf9ccfb"),
        "title": "Text from document valid",
        "author_id": "Sviatoslav",
        "content": "content",
        "comment_ids": []
    }

    result = post_translator.from_document(document)

    assert isinstance(result, Post) is True
    assert document["_id"] == result.id
    assert document["title"] == result.title
    assert document["author_id"] == result.author_id
    assert document["content"] == result.content
    assert document["comment_ids"] == result.comment_ids
