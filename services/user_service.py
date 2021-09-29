from wrappers import BcryptWrapper
from repositories import UserRepository
from models import User
from .validate_service import ValidateService
from exceptions import Conflict


class UserService:
    def __init__(self,
                 repository: UserRepository,
                 bcrypt_wrapper: BcryptWrapper,
                 create_validate_service: ValidateService
                 ) -> None:
        self.repository: UserRepository = repository
        self.create_validate_service = create_validate_service
        self.bcrypt_wrapper = bcrypt_wrapper

    def create(self, args: dict) -> User:
        self.create_validate_service.validate(args)
        args["password_hash"] = self.bcrypt_wrapper.gen_password_hash(
                                                        args["password"])
        user = User.from_request(args)
        created_id = self.repository.create(user)
        if created_id is None:
            raise Conflict(
                {"msg": "A user with such mail already exists in the system"})
        user.id = created_id
        return user
