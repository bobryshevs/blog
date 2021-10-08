from models import User, TokenPair
from .translator import Translator


class UserTranslator(Translator):
    def to_document(self, user: User) -> dict:
        return {
            "email": user.email,
            "password_hash": user.password_hash,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "tokens": self.to_doc_tokens(user)
        }

    def from_document(self, data: dict) -> User:
        user = User()
        user.id = data.get("_id")
        user.email = data.get("email")
        user.password_hash = data.get("password_hash")
        user.first_name = data.get("first_name")
        user.last_name = data.get("last_name")
        user.tokens = self.from_doc_tokens(data)

        return user

    def to_doc_tokens(self, user: User) -> list[dict[str, str]]:
        if user.tokens is None:
            return []

        return [token.json() for token in user.tokens]

    def from_doc_tokens(self, data: dict) -> list[TokenPair]:
        data["tokens"] = data["tokens"] if data["tokens"] is not None else []
        result = [
            TokenPair(
                access=token["access"],
                refresh=token["refresh"]
            )
            for token in data["tokens"]
        ]
        return result
