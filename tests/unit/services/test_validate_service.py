from exceptions import BadRequest
from services import ValidateService
from mock import Mock
import pytest


class TestValidateService:

    def test_validate_with_error(self):
        validator = Mock()
        validator.valid.return_value = False

        args = {}
        validators = [validator]
        validate_service = ValidateService(validators=validators)

        with pytest.raises(BadRequest):
            validate_service.validate(args)

        validator.valid.assert_called_once_with(args)

    def test_validate_valid_data(self):
        validator = Mock()
        validator.valid.return_value = True

        args = {}
        validators = [validator]
        validate_service = ValidateService(validators=validators)

        assert validate_service.validate(args) is True
        validator.valid.assert_called_once_with(args)
