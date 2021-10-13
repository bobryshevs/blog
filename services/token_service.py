from models import User
from wrappers import JWTWrapper
from exceptions import (
    BadRequest
)
from .user_service import UserService
from .validate_service import ValidateService


class TokenService:
    def __init__(
            self,
            jwt_wrapper: JWTWrapper,
            user_service: UserService,
            token_validate_service: ValidateService) -> None:

        self.jwt_wrapper = jwt_wrapper
        self.user_service = user_service
        self.token_validate_service = token_validate_service

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
