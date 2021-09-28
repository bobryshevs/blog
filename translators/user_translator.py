from models import User
from .translator import Translator


class UserTranslator(Translator):
    def to_document(self, user: User) -> dict:
        return {
            "email": user.email,
            "password_hash": user.password_hash,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }

    def from_document(self, data: dict) -> User:
        user = User()
        user.id = data.get("_id")
        user.email = data.get("email")
        user.password_hash = data.get("password_hash")
        user.first_name = data.get("first_name")
        user.last_name = data.get("last_name")
        user.access_token = data.get("access_token")
        user.refresh_token = data.get("refresh_token")
        return user
