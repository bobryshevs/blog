import pytest
from bson import ObjectId
from mock import Mock, MagicMock
from models.token_pair import TokenPair
from services import UserService
from models import User
from exceptions import BadRequest


class TestUserService:

    def setup(self):
        self.repository = Mock()
        self.create_validate_service = Mock()
        self.login_validate_service = Mock()
        self.refresh_validate_service = Mock()
        self.bcrypt_wrapper = MagicMock()
        self.jwt_wrapper = Mock()
        self.user_service = UserService(
            repository=self.repository,
            bcrypt_wrapper=self.bcrypt_wrapper,
            jwt_wrapper=self.jwt_wrapper,
            create_validate_service=self.create_validate_service,
            login_validate_service=self.login_validate_service,
            refresh_validate_service=self.refresh_validate_service
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

    def test_find_and_remove_token_pair_empty_list(self):
        user = User()
        user.tokens = []

        result = self.user_service.find_and_remove_token_pair(
            user=user,
            refresh="refresh_token"
        )

        assert result is False
        assert user.tokens == []

    def test_find_and_remove_token_pair_false(self):
        user = User()
        user.tokens = [
            {
                "access": "access_token_1",
                "refresh": "refresh_token_1"
            },
            {
                "access": "access_token_2",
                "refresh": "refresh_token_2"
            },
        ]
        start_len = len(user.tokens)

        result = self.user_service.find_and_remove_token_pair(
            user=user,
            refresh="refresh_token_3"
        )

        assert result is False
        assert len(user.tokens) == start_len

    def test_find_and_remove_token_pair_false(self):
        user = User()
        user.tokens = [
            {
                "access": "access_token_1",
                "refresh": "refresh_token_1"
            },
            {
                "access": "access_token_2",
                "refresh": "refresh_token_2"
            },
            {
                "access": "access_token_3",
                "refresh": "refresh_token_3"
            },
        ]
        start_len = len(user.tokens)

        result = self.user_service.find_and_remove_token_pair(
            user=user,
            refresh="refresh_token_2"
        )

        assert result is True
        assert len(user.tokens) == start_len - 1
        assert user.tokens == [
            {
                "access": "access_token_1",
                "refresh": "refresh_token_1"
            },
            {
                "access": "access_token_3",
                "refresh": "refresh_token_3"
            },
        ]
