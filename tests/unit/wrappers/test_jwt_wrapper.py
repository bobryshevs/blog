from mock import Mock

from wrappers import JWTWrapper
from enums import (
    TimeConstants,
    TokenType
)


class TestJWTWrapper:
    def setup(self):
        self.jwt = JWTWrapper(
            encryption_algorithm="HS256",
            key="SECRET_KEY",
            access_token_expiration=TimeConstants.QUARTER_OF_AN_HOUR,
            refresh_token_expiration=TimeConstants.MOUNTH
        )

    def test_set_service_params_access(self):
        NOW = 100
        start_payload_data = "data"
        payload = {"payload": start_payload_data}

        self.jwt.now = Mock(side_effect=[NOW])

        self.jwt.set_service_params(
            token_type=TokenType.ACCESS,
            payload=payload
        )

        self.jwt.now.assert_called_once()
        assert payload["exp"] == self.jwt.ACCESS_TOKEN_EXPIRATION + NOW
        assert payload["purpose"] == "access"
        assert payload["iat"] == NOW
        assert payload["payload"] == start_payload_data

    def test_set_service_params_refresh(self):
        NOW = 100
        start_payload_data = "data"
        payload = {"payload": start_payload_data}

        self.jwt.now = Mock(side_effect=[NOW])

        self.jwt.set_service_params(
            token_type=TokenType.REFRESH,
            payload=payload
        )

        self.jwt.now.assert_called_once()
        assert payload["exp"] == self.jwt.REGRESH_TOKEN_EXPIRATION + NOW
        assert payload["purpose"] == "refresh"
        assert payload["iat"] == NOW
        assert payload["payload"] == start_payload_data

    def test_encode_access(self):
        payload = {}
        self.jwt.set_service_params = Mock()

        result = self.jwt.encode(
            token_type=TokenType.ACCESS,
            payload=payload
        )

        assert isinstance(result, str)
        self.jwt.set_service_params.assert_called_once_with(
            token_type=TokenType.ACCESS,
            payload=payload
        )

    def test_encode_refresh(self):
        payload = {}
        self.jwt.set_service_params = Mock()

        result = self.jwt.encode(
            token_type=TokenType.REFRESH,
            payload=payload
        )

        assert isinstance(result, str)
        self.jwt.set_service_params.assert_called_once_with(
            token_type=TokenType.REFRESH,
            payload=payload
        )

    def test_decode(self):
        # https://jwt.io/
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9" \
            ".eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI" \
            "6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDI" \
            "yfQ.4DvTG7o-6dgSnQWPwYOmPNnM6Kdmv30_WHIk2cXVc_8"

        payload = {
            "sub": "1234567890",
            "name": "John Doe",
            "iat": 1516239022
        }

        result = self.jwt.decode(token)

        assert isinstance(result, dict)
        assert result == payload
