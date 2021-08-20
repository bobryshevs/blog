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

    def test_skip(self):
        key = 'page'
        arg_list = [
            {key: 1.4},
            {key: ()},
            {key: PositiveIntValidator(key)}
        ]
        validator = PositiveIntValidator(key)

        for args in arg_list:
            assert validator.valid(args) is True
