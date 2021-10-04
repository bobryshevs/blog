from wrappers import BcryptWrapper
from repositories import UserRepository
from models import User
from .validate_service import ValidateService


class UserService:
    def __init__(self,
                 repository: UserRepository,
                 bcrypt_wrapper: BcryptWrapper,
                 create_validate_service: ValidateService,
                 login_validate_service: ValidateService
                 ) -> None:
        self.repository: UserRepository = repository
        self.create_validate_service = create_validate_service
        self.login_validate_service = login_validate_service
        self.bcrypt_wrapper = bcrypt_wrapper

    def create(self, args: dict) -> User:
        self.create_validate_service.validate(args)
        args["password_hash"] = self.bcrypt_wrapper \
            .gen_passwd_hash(args["password"])
        user = User.from_request(args)
        user.id = self.repository.create(user)
        return user

    def login(self, args: dict) -> User:
        """
        Parameters
        ----------
        args: dict[str, str]
            login: str
            password: str
        """

        self.login_validate_service.validate(args)
        args["password_hash"] = self.bcrypt_wrapper \
            .gen_passwd_hash(args["password"])

        is_right_password: bool = self.repository.password_hash_verification(
            email=args["email"],
            password_hash=args["password_hash"]
        )

        if is_right_password:
            # TODO: generate tokens and return using python_dict
