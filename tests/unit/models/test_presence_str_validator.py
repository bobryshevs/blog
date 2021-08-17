from validators import PresenceStrValidator


class TestPresenceStrValidator:

    def test_validate_invalid_arg(self):
        key = 'key_arg'
        args = [None, [], 'str', (), set()]
        validator = PresenceStrValidator(key)

        for arg in args:
            assert validator.validate(arg) is False

    def test_validate_no_key(self):
        key = 'key_arg'
        args = {'first_key': 123, 'second_key': 321}
        validator = PresenceStrValidator(key)

        assert validator.validate(args) is False

    def test_validate_invalid_type_value(self):
        key = 'key_arg'
        args = {key: 123}
        validator = PresenceStrValidator(key)

        assert validator.validate(args) is False

    def test_validate_empty_value(self):
        key = 'key_arg'
        args = {key: None}
        validator = PresenceStrValidator(key)

        assert validator.validate(args) is False

    def test_validate_right_data(self):
        key = 'key_arg'
        args = {key: 'string_arg'}
        validator = PresenceStrValidator(key)

        assert validator.validate(args) is True
