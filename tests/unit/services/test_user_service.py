import pytest
from bson import ObjectId
from mock import Mock, MagicMock
from services import UserService
from models import User
from exceptions import BadRequest


class TestUserService:

    def setup(self):
        self.repository = Mock()
        self.create_validate_service = Mock()
        self.login_validate_service = Mock()
        self.bcrypt_wrapper = MagicMock()
        self.jwt_wrapper = Mock()
        self.user_service = UserService(
            repository=self.repository,
            bcrypt_wrapper=self.bcrypt_wrapper,
            jwt_wrapper=self.jwt_wrapper,
            create_validate_service=self.create_validate_service,
            login_validate_service=self.login_validate_service
        )

    def test_create_new_email(self):
        args = {
            "email": "vasya@gmail.com",
            "password": "password",
            "first_name": "first_name",
            "last_name": "last_name"
        }
        expected_id = ObjectId()
        self.repository.create.return_value = expected_id
        self.create_validate_service.validate.return_value = True
        self.bcrypt_wrapper.gen_passwd_hash.return_value = "123"

        result = self.user_service.create(args)

        assert isinstance(result, User)
        assert result.id == expected_id
        assert result.email == args["email"]
        assert result.first_name == args["first_name"]
        assert result.last_name == args["last_name"]
        self.create_validate_service.validate.assert_called_once_with(args)

    def test_create_exists_email(self):
        args = {
            "email": "vasya@gmail.com",
            "password": "password",
            "first_name": "first_name",
            "last_name": "last_name"
        }
        bad_request = Mock(side_effect=BadRequest({"msg": "mock"}))
        self.create_validate_service.validate = bad_request
        with pytest.raises(BadRequest):
            self.user_service.create(args)
        self.create_validate_service.validate.assert_called_once_with(args)
