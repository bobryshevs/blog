from _pytest.recwarn import T
from validators import ContentNonZeroStrValidator
from exceptions import BadRequest
import pytest


class TestContentNonZeroStrValidator:

    def test_valid_author_invalid(self):
        key = 'author'
        args = {key: ''}
        validator = ContentNonZeroStrValidator(key=key)

        with pytest.raises(BadRequest):
            validator.valid(args)

    def test_valid_author_valid(self):
        key = 'author'
        args = {key: 'Vasian'}
        validator = ContentNonZeroStrValidator(key=key)

        assert validator.valid(args) is True
