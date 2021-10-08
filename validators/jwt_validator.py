import jwt
from jwt.exceptions import (
    DecodeError,
    ExpiredSignatureError,
    ImmatureSignatureError,
    InvalidSignatureError,
    InvalidAudienceError,
    InvalidIssuerError,
    InvalidTokenError,
    InvalidIssuedAtError,
    MissingRequiredClaimError
)


class JWTValidator:
    def __init__(self, dict_key: str, encryption_key: str) -> None:
        self.dict_key: str = dict_key
        self.encryption_key: str = encryption_key

    def valid(self, args: dict) -> bool:
        try:
            jwt.decode(
                args[self.dict_key],
                key=self.encryption_key,
                algorithms=["HS256"]
            )
        except (
                InvalidTokenError,         # jwt.decode fails on a token
                DecodeError,               # jwt token failed validation
                InvalidSignatureError,     # jwt signature doesn't match
                ExpiredSignatureError,     # token expired
                InvalidAudienceError,      # aud claim doesn't match
                InvalidIssuerError,        # iss claim doesn't match
                InvalidIssuedAtError,      # iat claim is in the future
                ImmatureSignatureError,    # nvf claim time in the future
                MissingRequiredClaimError  # required claim not conatined
        ):
            return False
        return True
