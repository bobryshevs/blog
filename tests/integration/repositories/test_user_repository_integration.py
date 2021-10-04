from bson import ObjectId

from tests.factories import user_factory
from structure import (
    user_repository,
    user_translator
)


class TestUserRepositoryExistsMethod:

    def teardown(self):
        user_repository.collection.delete_many({})

    def test_exists_email_false(self):
        email = "test_email@example.com"
        result = user_repository.exists_email(email)

        assert result is False

    def test_exists_email_true(self):
        document = user_factory.get_doc()
        user_repository.collection.insert_one(document)
        result = user_repository.exists_email(document["email"])

        assert result is True

    def test_create_doesnt_exist(self):
        user = user_factory.get()
        result = user_repository.create(user)

        assert isinstance(result, ObjectId)

    def test_create_exists(self):
        user = user_factory.get()
        document = user_translator.to_document(user)
        user_repository.collection.insert_one(document)
        result = user_repository.create(user)
        assert result is None
