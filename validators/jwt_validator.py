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
        self.key: str = dict_key
        self.encryption_key: str = encryption_key
        self.exception_cooment: str = ""

    def valid(self, args: dict) -> bool:
        try:
            jwt.decode(
                args[self.key],
                key=self.encryption_key,
                algorithms=["HS256"]
            )
        except InvalidTokenError:
            self.exception_cooment = "Decoder fails on a token"
            return False
        except DecodeError:
            self.exception_cooment = "JWT token failed validation"
            return False
        except InvalidSignatureError:
            self.exception_cooment = "JWT signature doesn't match"
            return False
        except ExpiredSignatureError:
            self.exception_cooment = "Token expired"
            return False
        except InvalidAudienceError:
            self.exception_cooment = "AUD claid doesn't match"
            return False
        except InvalidIssuerError:
            self.exception_cooment = "ISS claim doesn't match"
            return False
        except InvalidIssuedAtError:
            self.exception_cooment = "IAT claim is in the future"
            return False
        except ImmatureSignatureError:
            self.exception_cooment = "NVF claim time in the future"
            return False
        except MissingRequiredClaimError:
            self.exception_cooment = "Required claim not conatined"
            return False
        return True

    def error(self) -> str:
        return f"Error in [{self.key}]. {self.exception_cooment}"
