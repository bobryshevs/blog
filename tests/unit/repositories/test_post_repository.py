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
        self.collection.find_one.assert_called_once_with({'_id': post_id})

    def test_get_by_id_exists_post(self):
        post_id = ObjectId()
        post = Post(
            text='text',
            author='author',
            date_of_creation=datetime.now(),
            m_id=post_id
        )
        document = {
            'text': post.text,
            'author': post.author,
            'date_of_creation': post.date_of_creation,
            '_id': post.id
        }
        self.collection.find_one.return_value = document

        result = self.repository.get_by_id(post_id)
        assert result.id == post.id
        assert result.text == post.text
        assert result.author == post.author
        assert result.date_of_creation == post.date_of_creation
        self.collection.find_one.assert_called_once_with({'_id': post_id})

    def test_update(self):
        post = Post('text_update', 'author_update', datetime.now())
        document = {
            "text": post.text,
            "author": post.author,
            "date_of_creation": post.date_of_creation
        }
        self.repository.update(post)
        self.collection.update_one.assert_called_once_with(
            {'_id': post.id},
            {'$set': document}
        )

    def test_delete(self):
        post_id = ObjectId()
        self.repository.delete(post_id)
        self.collection.delete_one.assert_called_once_with({'_id': post_id})

    def test_create(self):
        post = Post('text', 'author', datetime.now())
        document = {
            'text': post.text,
            'author': post.author,
            'date_of_creation': post.date_of_creation
        }
        self.repository.create(post)
        self.collection.insert_one.assert_called_once_with(document)
