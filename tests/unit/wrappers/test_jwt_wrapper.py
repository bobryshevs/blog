from mock import Mock

from wrappers import (
    JWTWrapper,
    TimeConstants
)


class TestJWTWrapper:
    def setup(self):
        self.jwt = JWTWrapper(
            encryption_algorithm="HS256",
            key="SECRET_KEY",
            token_config={
                "iss": "ISS",
                "aud": "AUD"
            }
        )

    def test_set_service_params(self):
        jwt = self.jwt
        NOW = 100
        to_check: dict = {}

        jwt.now = Mock(side_effect=[NOW])
        jwt.set_service_params(payload=to_check)

        assert to_check["nbf"] == NOW
        assert to_check["iat"] == NOW
        assert to_check["iss"] == jwt.token_config["iss"]
        assert to_check["aud"] == jwt.token_config["aud"]

        jwt.now.assert_called_once()

    def test_set_access_token_params(self):
        jwt = self.jwt
        NOW = 100
        to_check: dict = {}

        jwt.now = Mock()
        jwt.now.return_value = NOW

        jwt.set_access_token_params(payload=to_check)

        assert to_check["exp"] == NOW + TimeConstants.QUARTER_OF_AN_HOUR
        assert to_check["nbf"] == NOW
        assert to_check["iat"] == NOW
        assert to_check["iss"] == jwt.token_config["iss"]
        assert to_check["aud"] == jwt.token_config["aud"]

        # 1 - set_access_token_params, 2 - set_service_params
        assert jwt.now.call_count == 2

    def test_set_refresh_token_params(self):
        jwt = self.jwt
        NOW = 100
        to_check: dict = {}

        jwt.now = Mock()
        jwt.now.return_value = NOW

        jwt.set_refresh_token_params(payload=to_check)

        assert to_check["exp"] == NOW + TimeConstants.MOUNTH
        assert to_check["nbf"] == NOW
        assert to_check["iat"] == NOW
        assert to_check["iss"] == jwt.token_config["iss"]
        assert to_check["aud"] == jwt.token_config["aud"]

        # 1 - set_access_token_params, 2 - set_service_params
        assert jwt.now.call_count == 2

    def test_emit_access_token_test_call(self):
        jwt = self.jwt
        NOW = 100

        jwt.now = Mock(side_effect=[NOW, NOW])

        start_value = "start_value"
        to_check = {"start_value": start_value}

        result = jwt.emit_access_token(payload=to_check)

        assert isinstance(result, str)

        assert to_check["start_value"] == start_value
        assert to_check["exp"] == NOW + TimeConstants.QUARTER_OF_AN_HOUR
        assert to_check["nbf"] == NOW
        assert to_check["iat"] == NOW
        assert to_check["iss"] == jwt.token_config["iss"]
        assert to_check["aud"] == jwt.token_config["aud"]

        assert jwt.now.call_count == 2

    def test_emit_refresh_token_call(self):
        jwt = self.jwt
        NOW = 100

        jwt.now = Mock(side_effect=[NOW, NOW])

        start_value = "start_value"
        to_check = {"start_value": start_value}

        result = jwt.emit_refresh_token(payload=to_check)

        assert isinstance(result, str)

        assert to_check["start_value"] == start_value
        assert to_check["exp"] == NOW + TimeConstants.MOUNTH
        assert to_check["nbf"] == NOW
        assert to_check["iat"] == NOW
        assert to_check["iss"] == jwt.token_config["iss"]
        assert to_check["aud"] == jwt.token_config["aud"]

        assert jwt.now.call_count == 2

    def test_decode_payload(self):
        jwt = self.jwt

        access_payload = {"access_payload": 123}
        refresh_payload = {"refresh_payload": 234}

        access_token = jwt.emit_access_token(access_payload)
        refresh_token = jwt.emit_refresh_token(refresh_payload)

        assert isinstance(access_token, str)
        assert isinstance(refresh_token, str)

        result_access_payload = jwt.decode_payload(access_token)
        resutl_refresh_payload = jwt.decode_payload(refresh_token)

        assert access_payload == result_access_payload
        assert refresh_payload == resutl_refresh_payload
