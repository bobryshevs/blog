from validators import PositiveIntValidator
from random import randint


class TestContentPositiveIntValidator:

    def test_valid_non_positive_int(self):
        key = 'page'
        args = {key: randint(-1000, 0)}
        validator = PositiveIntValidator(key)

        assert validator.valid(args) is False

    def test_valid_positive_int(self):
        key = 'page'
        args = {key: randint(1, 1000)}
        validator = PositiveIntValidator(key)

        assert validator.valid(args) is True
