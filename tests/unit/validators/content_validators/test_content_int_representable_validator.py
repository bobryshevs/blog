from _pytest.recwarn import T
import py
from validators import ContentIntRepresentableValidator
from exceptions import BadRequest
import pytest


class TestContentIntRepresentableValidator:

    def test_valid_value_invalid(self):
        key = "page"
        args = {key: "1.3"}
        validator = ContentIntRepresentableValidator(key=key)

        with pytest.raises(BadRequest):
            validator.valid(args)

    def test_valid_value_valid(self):
        key = "page"
        args = {key: "123"}
        validator = ContentIntRepresentableValidator(key=key)

        assert validator.valid(args) is True
