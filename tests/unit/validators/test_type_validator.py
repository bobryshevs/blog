from validators import TypeValidator
import validators


class TestTypeValidator:

    def test_invalid_value_type(self):
        key = "key"
        args = {key: '1.2'}
        validator = TypeValidator(key=key, value_type=int)

        assert validator.valid(args) is False

    def test_valid_value_type(self):
        key = "key"
        args = {key: 123}
        validator = TypeValidator(key=key, value_type=int)

        assert validator.valid(args) is True
