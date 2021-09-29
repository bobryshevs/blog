import pytest
from mock import Mock
from exceptions import BadRequest
from services import ValidateService, validate_service
from structure import create_user_validate_service
from loggers_factory import loggers_factory
logger = loggers_factory.get()


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


class TestCreateUserValidateService:
    def test_validate_without_email(self):
        args = {
            "password": "password",
            "first_name": "first_name",
            "last_name": "last_name"
        }
        validate_service = create_user_validate_service

        with pytest.raises(BadRequest) as error:
            validate_service.validate(args)

        assert isinstance(error.value.value, dict)
        assert error.value.code == 400
        #    pytest | excption | exception_field
        assert error.value.value["key"] == "email"

    def test_validate_without_password(self):
        args = {
            "email": "wstswsb@gmail.com",
            "first_name": "first_name",
            "last_name": "last_name"
        }
        validate_service = create_user_validate_service

        with pytest.raises(BadRequest) as error:
            validate_service.validate(args)

        assert isinstance(error.value.value, dict)
        assert error.value.code == 400
        #    pytest | excption | exception_field
        assert error.value.value["key"] == "password"

    def test_validate_without_first_name(self):
        args = {
            "email": "wstswsb@gmail.com",
            "password": "password",
            "last_name": "last_name"
        }
        validate_service = create_user_validate_service

        with pytest.raises(BadRequest) as error:
            validate_service.validate(args)

        assert isinstance(error.value.value, dict)
        assert error.value.code == 400
        #    pytest | excption | exception_field
        assert error.value.value["key"] == "first_name"

    def test_validate_without_last_name(self):
        args = {
            "email": "wstswsb@gmail.com",
            "password": "password",
            "first_name": "first_name"
        }
        validate_service = create_user_validate_service

        with pytest.raises(BadRequest) as error:
            validate_service.validate(args)

        assert isinstance(error.value.value, dict)
        assert error.value.code == 400
        #    pytest | excption | exception_field
        assert error.value.value["key"] == "last_name"

    def test_validate_incorrect_email_type(self):
        args = {
            "email": 123,
            "password": "password",
            "first_name": "first_name",
            "last_name": "last_name"
        }
        validate_service = create_user_validate_service

        with pytest.raises(BadRequest) as error:
            validate_service.validate(args)

        assert isinstance(error.value.value, dict)
        assert error.value.code == 400
        assert error.value.value["key"] == "email"

    def test_validate_incorrect_password_type(self):
        args = {
            "email": "wstswsb@gmail.com",
            "password": set(),
            "first_name": "first_name",
            "last_name": "last_name"
        }
        validate_service = create_user_validate_service

        with pytest.raises(BadRequest) as error:
            validate_service.validate(args)

        assert isinstance(error.value.value, dict)
        assert error.value.code == 400
        assert error.value.value["key"] == "password"

    def test_validate_incorrect_firstname_type(self):
        args = {
            "email": "wstswsb@gmail.com",
            "password": "password",
            "first_name": ("first_name",),
            "last_name": "last_name"
        }
        validate_service = create_user_validate_service

        with pytest.raises(BadRequest) as error:
            validate_service.validate(args)

        assert isinstance(error.value.value, dict)
        assert error.value.code == 400
        assert error.value.value["key"] == "first_name"

    def test_validate_incorrect_lastname_type(self):
        args = {
            "email": "wstswsb@gmail.com",
            "password": "password",
            "first_name": "first_name",
            "last_name": {"last_name"}
        }
        validate_service = create_user_validate_service

        with pytest.raises(BadRequest) as error:
            validate_service.validate(args)

        assert isinstance(error.value.value, dict)
        assert error.value.code == 400
        assert error.value.value["key"] == "last_name"
