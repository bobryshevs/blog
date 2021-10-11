from bson.objectid import ObjectId
from enums import TokenType
from wrappers import (
    BcryptWrapper,
    JWTWrapper
)
from models import (
    User,
    TokenPair,
)
from repositories import UserRepository
from exceptions import (
    BadRequest,
    Unauthorized
)
from .validate_service import ValidateService
from loggers_factory import loggers_factory
from enums import TokenType


logger = loggers_factory.get()


class UserService:
    def __init__(self,
                 repository: UserRepository,
                 bcrypt_wrapper: BcryptWrapper,
                 jwt_wrapper: JWTWrapper,
                 create_validate_service: ValidateService,
                 login_validate_service: ValidateService,
                 refresh_validate_service: ValidateService,
                 logout_validate_service: ValidateService
                 ) -> None:
        self.repository: UserRepository = repository
        self.create_validate_service = create_validate_service
        self.login_validate_service = login_validate_service
        self.refresh_validate_service = refresh_validate_service
        self.logout_validate_service = logout_validate_service
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

        user.tokens.append(token_pair)
        self.repository.update(user)
        return token_pair

    def refresh(self, args: dict):
        """
        Parameters
        ----------
        args: dict
            refresh: str
        """
        self.refresh_validate_service.validate(args)
        refresh: str = args["refresh"]
        user: User = self.get_by_token(refresh)

        if not self.remove_token_pair(user, TokenType.REFRESH, refresh):
            raise Unauthorized({"msg": "token expired"})

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
        user.tokens.append(token_pair)
        self.repository.update(user)
        return token_pair

    def logout(self, args: dict[str, str]) -> bool:
        """
        Parameters
        ----------
        args: dict
            access: str
        """
        self.logout_validate_service.validate(args)
        access: str = args["access"]
        user: User = self.get_by_token(access)

        if not self.remove_token_pair(user, TokenType.ACCESS, access):
            raise Unauthorized({"msg": "token expired"})

        self.repository.update(user)

    def get_by_token(self, token: str) -> User:
        user_id: str = self.jwt_wrapper.decode(token).get("id")
        if user_id is None:
            raise Unauthorized({"msg": "no id found in token"})

        user: User = self.repository.get_by_id(ObjectId(user_id))
        if user is None:
            raise Unauthorized({"msg": "no user with given id"})

        return user

    def remove_token_pair(
            self,
            user: User,
            token_type: TokenType,
            token: str) -> bool:
        """
        Returns
            True: token pair was found and removed
            False: token pair is not in the collection
        """
        for index, token_pair in enumerate(user.tokens):
            if token_pair.get_token_by_type(token_type) == token:
                del user.tokens[index]
                return True
        return False
