import bcrypt
from repositories import UserRepository
from models import User
from bcrypt import (
    hashpw,
    gensalt
)
from .validate_service import ValidateService


class UserService:
    def __init__(self,
                 repository: UserRepository,
                 create_validate_service: ValidateService
                 ) -> None:
        self.repository: UserRepository = repository
        self.create_validate_service = create_validate_service

    def create(self, args: dict) -> User:
        self.create_validate_service.validate(args)
        self._add_password_hash(args)
        user = User.from_request(args)
        user.id = self.repository.create(user)
        return user

    def _add_password_hash(self, args: dict) -> None:
        args["password_hash"] = hashpw(args["password"].encode(), gensalt())
