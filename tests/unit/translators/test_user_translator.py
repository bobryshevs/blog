import pytest
from translators import UserTranslator
from models import User


class TestUserTranslator:
    def test_to_document(self):
        translator = UserTranslator()
        user = User()
        user.email = "email"
        user.password_hash = b"password_hash"
        user.first_name = "firstname"
        user.last_name = "lastname"

        result = translator.to_document(user)

        assert isinstance(result, dict)
        assert user.email == result.get("email")
        assert user.password_hash == result.get("password_hash")
        assert user.first_name == result.get("first_name")
        assert user.last_name == result.get("last_name")

    def test_from_document(self):
        translator = UserTranslator()
        document = {
            "_id": "id",
            "email": "email",
            "password_hash": b"password_hash",
            "first_name": "first_name",
            "last_name": "last_name",
            "access_token": "access_token",
            "refresh_token": "refresh_token"
        }

        model = translator.from_document(document)

        assert isinstance(model, User)
        assert model.id == document.get("_id")
        assert model.email == document.get("email")
        assert model.password_hash == document.get("password_hash")
        assert model.first_name == document.get("first_name")
        assert model.last_name == document.get("last_name")
        assert model.access_token == document.get("access_token")
        assert model.refresh_token == document.get("refresh_token")