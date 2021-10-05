from mock import Mock

from wrappers import JWTWrapper
from enums import TimeConstants


class TestJWTWrapper:
    def setup(self):
        self.jwt = JWTWrapper(
            encryption_algorithm="HS256",
            key="SECRET_KEY",
            access_token_expiration=TimeConstants.QUARTER_OF_AN_HOUR,
            refresh_token_expiration=TimeConstants.MOUNTH
        )

    def test_set_service_params(self):
        ...
