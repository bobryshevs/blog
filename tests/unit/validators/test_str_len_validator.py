from validators import StrLenValidator
import pytest

import validators


class TestStrLenValidator:

    def test_validmin_len_andmax_len_more_thanmax_len(self):
        key = 'string'
        min_len = 1
        max_len = 4
        args = {key: '12345'}  # length of value always more than max

        validator = StrLenValidator(key=key, min_len=min_len, max_len=max_len)

        assert validator.valid(args) is False

    def test_valid_without_min_false(self):
        key = 'string'
        max_len = 2
        args = {key: '123'}

        validator = StrLenValidator(key=key, max_len=max_len)

        assert validator.valid(args) is False

    def test_valid_without_min_true(self):
        key = 'string'
        max_len = 1024
        args = {key: '123456'}

        validator = StrLenValidator(key=key, max_len=max_len)

        assert validator.valid(args) is True

    def test_valid_without_max_false(self):
        key = 'string'
        min_len = 1
        args = {key: ''}
        validator = StrLenValidator(key=key, min_len=min_len)

        assert validator.valid(args) is False

    def test_valid_without_max_true(self):
        key = 'string'
        min_len = 2
        args = {key: '123'}
        validator = StrLenValidator(key=key, min_len=min_len)

        assert validator.valid(args) is True

    def test_without_min_max(self):
        key = 'string'

        args = {key: 's'}

        validator = StrLenValidator(key=key)

        assert validator.valid(args) is True

    def test_valid_valid(self):
        key = 'string'
        min_len = 2
        max_len = 5
        args = {key: 'ss'}
        validator = StrLenValidator(key=key, min_len=min_len, max_len=max_len)

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
