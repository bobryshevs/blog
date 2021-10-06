from models import User
from .translator import Translator


class UserTranslator(Translator):
    def to_document(self, user: User) -> dict:
        return {
            "email": user.email,
            "password_hash": user.password_hash,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "access_tokens": user.access_tokens,
            "refresh_tokens": user.refresh_tokens
        }

    def from_document(self, data: dict) -> User:
        user = User()
        user.id = data.get("_id")
        user.email = data.get("email")
        user.password_hash = data.get("password_hash")
        user.first_name = data.get("first_name")
        user.last_name = data.get("last_name")
        user.access_tokens = self.__get_tokens(
            tokens_key="access_tokens",
            data=data
        )
        user.refresh_tokens = self.__get_tokens(
            tokens_key="refresh_tokens",
            data=data
        )

        return user

    def __get_tokens(self, tokens_key: str, data: dict) -> list[str]:
        tokens = data.get(tokens_key)
        return tokens if tokens is not None else []
