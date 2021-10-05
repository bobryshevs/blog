import jwt

from enum import IntEnum
from time import time


class TimeConstants(IntEnum):
    SECOND = 1
    MINUTE = 60
    QUARTER_OF_AN_HOUR = 900
    HOUR = 3600
    DAY = 86400
    MOUNTH = 2592000  # 30 days


class JWTWrapper:
    def __init__(
            self,
            encryption_algorithm: str,
            key: str,
            token_config: dict) -> None:
        """
        Parameters
        ----------
        encryption_algorithm: str
            Encryption algorithm name

        key: str
            encryption key

        token_config: dict
            must include:
                iss: str
                aud: str
        """

        self.encryption_algorithm: str = encryption_algorithm
        self.key: str = key
        self.token_config: dict = token_config

    def decode_payload(self, token: str) -> dict:
        return jwt.decode(
            jwt=token,
            key=self.key,
            algorithms=[self.encryption_algorithm]
        )

    def emit_access_token(self, payload: dict) -> str:
        self.set_access_token_params(payload)
        return jwt.encode(
            payload=payload,
            key=self.key,
            algorithm=self.encryption_algorithm
        )

    def emit_refresh_token(self, payload: dict) -> str:
        self.set_refresh_token_params(payload)
        return jwt.encode(
            payload=payload,
            key=self.key,
            algorithm=self.encryption_algorithm
        )

    def set_access_token_params(self, payload: dict) -> None:
        payload["exp"] = self.now() + TimeConstants.QUARTER_OF_AN_HOUR
        self.set_service_params(payload)

    def set_refresh_token_params(self, payload: dict) -> None:
        payload["exp"] = self.now() + TimeConstants.MOUNTH
        self.set_service_params(payload)

    def set_service_params(self, payload: dict) -> None:
        now: int = self.now()

        payload["nbf"] = now
        payload["iat"] = now
        payload["iss"] = self.token_config.get("iss")
        payload["aud"] = self.token_config.get("aud")

    def now(self) -> int:
        return int(time())
