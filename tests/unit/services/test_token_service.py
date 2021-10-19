from mock import Mock

from services import TokenService
from models import TokenPair


class TestTokenCleanerFunctions:
    def setup(self):
        self.jwt_wrapper = Mock()
        self.user_service = Mock()
        self.token_validate_service = Mock()
        self.token_validator = Mock()

        self.service = TokenService(
            jwt_wrapper=self.jwt_wrapper,
            user_service=self.user_service,
            token_validate_service=self.token_validate_service,
            token_validator=self.token_validator
        )

    def test_get_alive_token_pairs(self):
        # bool values ​​are used for clarity of the algorithm
        token_validator_side_effect = [True, True, False, True, False, False]
        token_pairs = [TokenPair("", "")for _ in token_validator_side_effect]

        self.token_validator.valid.side_effect = token_validator_side_effect

        result = self.service.get_alive_token_pairs(token_pairs)
        assert len(result) == token_validator_side_effect.count(True)
