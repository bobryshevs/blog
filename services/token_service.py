from models import User, TokenPair
import repositories
from wrappers import JWTWrapper
from exceptions import BadRequest
from .user_service import UserService
from .validate_service import ValidateService
from validators import JWTValidator
from repositories import UserRepository


class TokenService:
    def __init__(
            self,
            jwt_wrapper: JWTWrapper,
            user_service: UserService,
            token_validate_service: ValidateService,
            token_validator: JWTValidator) -> None:

        self.jwt_wrapper = jwt_wrapper
        self.user_service = user_service
        self.token_validate_service = token_validate_service
        self.token_validator = token_validator

    def get_principle(self, headers: dict) -> User:
        token: str = self._get_token(headers)
        if token is None:
            return
        self.token_validate_service.validate({"token": token})
        principle: User = self.user_service.get_by_token(token)
        return principle

    def _get_token(self, headers: dict) -> str:
        bearer: str = headers.get("Authorization")
        if bearer is None:
            return

        if not bearer.startswith("Bearer "):
            raise BadRequest({"msg": "Invalid Authorization header"})

        token: str = bearer.split(" ")[1]

        if not token:
            raise BadRequest({"msg": "Token not found"})
        return token

    def proccess_user_pages(self, repository: UserRepository, page_size: int):
        for page in range(repository.get_number_of_pages()):
            users: list[User] = repository.get_user_token(page, page_size)
            self.process_users(users)
            self.update_database_values(repository, users)

    def update_db_values(self, users: list[User]):
        for user in users:
            self.user_service.repository.update_user_token(user)

    def process_users(self, users: list[User]):
        for user in users:
            user.tokens = self.get_alive_token_pairs(user.tokens)

    def get_alive_token_pairs(self, token_pairs: list[TokenPair]):
        alive_tokens: list[TokenPair] = []
        for token_pair in token_pairs:
            is_alive = self.token_validator.valid(token_pair.refresh)
            if not is_alive:
                continue
            alive_tokens.append(token_pair)
        return alive_tokens
