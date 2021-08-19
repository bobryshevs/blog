from ast import Str
from validators import StrLenValidator
import pytest

import validators


class TestStrLenValidator:

    def test_check_args_invalid(self):
        key = 'string'
        _min = -1
        _max = -4

        validator = StrLenValidator(key=key)

        assert validator._check_args_for_valid(_min, _max) is False

    def test_check_args_valid(self):
        key = 'string'
        _min = 1
        _max = 2

        validator = StrLenValidator(key=key)

        assert validator._check_args_for_valid(_min, _max) is True

    def test_valid_negative_min(self):
        key = 'string'
        _min = -1  # invalid value
        _max = 4
        args = {key: 'value'}

        validator = StrLenValidator(key=key)

        with pytest.raises(ValueError):
            validator.valid(args, _min=_min, _max=_max)

    def test_valid_negative_max(self):
        key = 'string'
        _min = 1
        _max = -4  # invalid value
        args = {key: 'value'}

        validator = StrLenValidator(key=key)

        with pytest.raises(ValueError):
            validator.valid(args, _min, _max)

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
