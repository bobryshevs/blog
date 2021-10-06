from enums import TokenType
from wrappers import (
    BcryptWrapper,
    JWTWrapper
)
from models import (
    User,
    TokenPair
)
from repositories import UserRepository
from exceptions import BadRequest
from .validate_service import ValidateService
from loggers_factory import loggers_factory

logger = loggers_factory.get()


class UserService:
    def __init__(self,
                 repository: UserRepository,
                 bcrypt_wrapper: BcryptWrapper,
                 jwt_wrapper: JWTWrapper,
                 create_validate_service: ValidateService,
                 login_validate_service: ValidateService
                 ) -> None:
        self.repository: UserRepository = repository
        self.create_validate_service: ValidateService = create_validate_service
        self.login_validate_service: ValidateService = login_validate_service
        self.bcrypt_wrapper: BcryptWrapper = bcrypt_wrapper
        self.jwt_wrapper: JWTWrapper = jwt_wrapper

    def create(self, args: dict) -> User:
        self.create_validate_service.validate(args)
        args["password_hash"] = self.bcrypt_wrapper \
            .gen_passwd_hash(args["password"])
        user = User.from_request(args)
        user.id = self.repository.create(user)
        return user

    def login(self, args: dict) -> TokenPair:
        """
        Parameters
        ----------
        args: dict[str, str]
            email: str
            password: str
        """

        self.login_validate_service.validate(args)

        user: User = self.repository.get_one_by_field(
            field_name="email",
            value=args["email"]
        )

        if user is None:
            raise BadRequest(value={"msg": "User with given email no exists"})

        is_right_passwd: bool = self.bcrypt_wrapper.check_passwd(
            passwd=args["password"],
            passwd_hash=user.password_hash
        )

        if not is_right_passwd:
            raise BadRequest(value={"msg": "Wrong password"})

        token_pair: TokenPair = TokenPair(
            access=self.jwt_wrapper.encode(
                token_type=TokenType.ACCESS,
                payload={"id": str(user.id)}
            ),
            refresh=self.jwt_wrapper.encode(
                token_type=TokenType.REFRESH,
                payload={"id": str(user.id)}
            )
        )

        user.access_tokens.append(token_pair.access)
        user.refresh_tokens.append(token_pair.refresh)

        self.repository.update(user)

        return token_pair
