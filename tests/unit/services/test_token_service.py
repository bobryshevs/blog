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
        bool_values = [True, True, False, True, False, False]
        token_pairs = [
            TokenPair("", refresh=index)
            for index in range(len(bool_values))
        ]

        self.token_validator.valid = Mock(side_effect=bool_values)

        result = self.service.get_alive_token_pairs(token_pairs)
        assert len(result) == bool_values.count(True)
        for token_pair in result:
            assert bool_values[token_pair.refresh] is True
