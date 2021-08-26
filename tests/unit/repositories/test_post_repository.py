from datetime import datetime
from bson.objectid import ObjectId
from mock import Mock

from repositories.post_repository import PostRepository
from translators import PostTranslator
from models import Post


class TestPostRepository:
    def setup(self):
        self.repository = PostRepository(
            collection=Mock(),
            translator=PostTranslator())
        self.collection = self.repository.collection

    def teardown(self):
        pass

    def test_get_by_id_without_post(self):
        post_id = ObjectId()
        self.collection.find_one.return_value = None

        result = self.repository.get_by_id(post_id)

        assert result is None
        self.collection.find_one.assert_called_once_with({"_id": post_id})

    def test_get_by_id_exists_post(self):
        post_id = ObjectId()
        post = Post()
        post.id = ObjectId()
        post.title = "title"
        post.content = "content"
        post.author_id = ObjectId()
        post.comment_ids = [ObjectId() for _ in range(5)]
        document = {
            "_id": post.id,
            "title": post.title,
            "content": post.content,
            "author_id": post.author_id,
            "comment_ids": post.comment_ids
        }
        self.collection.find_one.return_value = document

        result = self.repository.get_by_id(post_id)
        assert result.id == post.id
        assert result.title == post.title
        assert result.content == post.content
        assert result.author_id == post.author_id
        self.collection.find_one.assert_called_once_with({"_id": post_id})

    def test_update(self):
        post = Post()
        post.id = ObjectId()
        post.title = "title"
        post.content = "content"
        post.author_id = ObjectId()
        post.comment_ids = [ObjectId() for _ in range(5)]

        document = {
            "title": post.title,
            "author_id": post.author_id,
            "content": post.content
        }
        self.repository.update(post)
        self.collection.update_one.assert_called_once_with(
            {"_id": post.id},
            {"$set": document}
        )

    def test_delete(self):
        post_id = ObjectId()
        self.repository.delete(post_id)
        self.collection.delete_one.assert_called_once_with({"_id": post_id})

    def test_create(self):
        post = Post()
        post.title = "title"
        post.content = "content"
        post.author_id = ObjectId()
        document = {
            "title": post.title,
            "content": post.content,
            "author_id": post.author_id
        }
        self.repository.create(post)
        self.collection.insert_one.assert_called_once_with(document)
