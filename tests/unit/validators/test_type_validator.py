from validators import TypeValidator


class TestTypeValidator:

    def test_invalid_value_type(self):
        key = "key"
        args = {key: '1.2'}
        validator = TypeValidator(key=key, type_=int)

        assert validator.valid(args) is False

    def test_valid_value_type(self):
        key = "key"
        args = {key: 123}
        validator = TypeValidator(key=key, type_=int)

        assert validator.valid(args) is True
