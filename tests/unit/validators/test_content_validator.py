import py
from validators import ContentValidator
import pytest


class TestContentValidator:

    def test_valid_abstract_method(self):
        key = "key"
        args = {key: "value"}
        validator = ContentValidator(key=key)

        with pytest.raises(NotImplementedError):
            validator.valid(args)
