from bson import ObjectId

from tests.factories.user_factory import UserFactory
from structure import user_repository


class TestUserRepositoryExistsMethod:
    def setup(self):
        user = UserFactory.get()
        user_repository.collection.insert_one(
            {
                "email": user.email,
                "password_hash": user.password_hash,
                "first_name": user.first_name,
                "last_name": user.last_name
            }
        )
        self.user = user

    def teardown(self):
        user_repository.collection.delete_many({})

    def test_exists_email_false(self):
        email = "#..$(@"
        result = user_repository.exists_email(email)

        assert isinstance(result, bool)
        assert result is False

    def test_exists_email_true(self):
        email = self.user.email
        result = user_repository.exists_email(email)

        assert isinstance(result, bool)
        assert result is True

    def test_create_doesnt_exist(self):
        self.user.email *= 2  # make email unique
        result = user_repository.create(self.user)

        assert isinstance(result, ObjectId)

    def test_create_exists(self):
        result = user_repository.create(self.user)

        assert result is None
