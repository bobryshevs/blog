import bcrypt
from repositories import UserRepository
from models import User
from bcrypt import (
    hashpw,
    gensalt
)


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository: UserRepository = repository

    def create(self, args: dict) -> User:
        # Todo: validators
        self._add_password_hash(args)
        user = User.from_request(args)
        user.id = self.repository.create(user)
        return user

    def _add_password_hash(self, args: dict) -> None:
        args["password_hash"] = hashpw(args["password"], gensalt())
