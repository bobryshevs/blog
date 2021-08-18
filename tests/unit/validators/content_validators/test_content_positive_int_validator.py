from _pytest.recwarn import T
import py
from exceptions import BadRequest
from validators import ContentPositiveIntValidator
from random import randint
import pytest


class TestContentPositiveIntValidator:

    def test_valid_non_positive_int(self):
        key = 'page'
        args = {key: randint(-1000, 0)}
        validator = ContentPositiveIntValidator(key)

        with pytest.raises(BadRequest):
            validator.valid(args)

    def test_valid_positive_int(self):
        key = 'page'
        args = {key: randint(1, 1000)}
        validator = ContentPositiveIntValidator(key)

        assert validator.valid(args) is True
