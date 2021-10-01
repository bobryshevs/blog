
from structure import (
    bcrypt_wrapper,
    user_translator
)
from models import User


class UserFactory:
    @staticmethod
    def get() -> User:
        user = User()
        user.email = "unique_email@example.com"
        user.password_hash = bcrypt_wrapper.gen_password_hash("password")
        user.first_name = "first_name"
        user.last_name = "last_name"
        return user

    @staticmethod
    def get_doc() -> dict:
        return user_translator.to_document(UserFactory.get())