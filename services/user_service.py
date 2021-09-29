from bcrypt import (
    hashpw,
    gensalt
)

from repositories import UserRepository
from models import User
from .validate_service import ValidateService
from exceptions import Conflict


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
        created_id = self.repository.create(user)
        if created_id is None:
            raise Conflict(
                {"msg": "A user with such mail already exists in the system"})
        user.id = created_id
        return user

    def _add_password_hash(self, args: dict) -> None:
        args["password_hash"] = hashpw(
            args["password"].encode(),
            self._gensalt()
        )

    def _gensalt(self) -> bytes:
        return gensalt()
