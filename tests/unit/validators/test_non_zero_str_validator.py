from validators import NonZeroStrValidator


class TestNonZeroStrValidator:
    def test_valid_author_invalid(self):
        key = 'author'
        args = {key: ''}
        validator = NonZeroStrValidator(key=key)

        assert validator.valid(args) is False

    def test_valid_author_valid(self):
        key = 'author'
        args = {key: 'Vasian'}
        validator = NonZeroStrValidator(key=key)

        assert validator.valid(args) is True
