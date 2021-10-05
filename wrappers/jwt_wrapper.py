import jwt

from time import time

from enums import TokenType


class JWTWrapper:
    def __init__(
            self,
            encryption_algorithm: str,
            key: str,
            access_token_expiration: int,
            refresh_token_expiration: int) -> None:

        self.ENCRYPTION_ALGORITHM: str = encryption_algorithm
        self.KEY: str = key
        self.ACCESS_TOKEN_EXPIRATION: int = access_token_expiration
        self.REGRESH_TOKEN_EXPIRATION: int = refresh_token_expiration

    def decode(self, token: str) -> dict:
        payload = jwt.decode(
            jwt=token,
            key=self.KEY,
            algorithms=[self.ENCRYPTION_ALGORITHM]
        )
        return payload

    def encode(self, token_type: TokenType, payload: dict) -> str:
        self.set_service_params(
            token_type=token_type,
            payload=payload
        )

        token = jwt.encode(
            payload=payload,
            key=self.KEY,
            algorithm=self.ENCRYPTION_ALGORITHM)

        return token

    def set_service_params(self, token_type: TokenType, payload: dict):
        payload = payload if payload else {}
        NOW = self.now()
        if token_type == TokenType.ACCESS:
            payload["exp"] = NOW + self.ACCESS_TOKEN_EXPIRATION
            payload["purpose"] = "access"

        if token_type == TokenType.REFRESH:
            payload["exp"] = NOW + self.REGRESH_TOKEN_EXPIRATION
            payload["purpose"] = "refresh"
        payload["iat"] = NOW

    def now(self) -> int:
        return int(time())
