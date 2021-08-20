from validators import StrLenValidator
import pytest

import validators


class TestStrLenValidator:

    def test_valid_min_and_max_more_than_max(self):
        key = 'string'
        _min = 1
        _max = 4
        args = {key: 's' * (_max + 1)}  # length of value always more than max

        validator = StrLenValidator(key=key)

        assert validator.valid(args, _min, _max) is False

    def test_valid_min_and_max_less_than_min(self):
        key = 'string'
        _min = 1
        args = {key: ''}

        validator = StrLenValidator(key=key)

        assert validator.valid(args, _min) is False

    def test_valid_valid(self):
        key = 'string'
        _min = 2
        _max = 5
        args = {key: 's' * (_max - 1)}

        validator = StrLenValidator(key=key)

        assert validator.valid(args, _min, _max) is True

    def test_without_min_max(self):
        key = 'string'

        args = {key: 's'}

        validator = StrLenValidator(key=key)

        assert validator.valid(args) is True

    def test_skip(self):
        key = 'string'
        arg_list = [
            {key: 123},
            {key: 1.23},
            {key: StrLenValidator(key)}
        ]
        validator = StrLenValidator(key)

        for args in arg_list:
            assert validator.valid(args) is True
