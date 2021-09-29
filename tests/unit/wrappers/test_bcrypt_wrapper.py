from bcrypt import hashpw, gensalt
from mock import Mock
from wrappers import BcryptWrapper


class TestBcryptWrapper:
    def test_gen_password_hash_default_salt(self):
        password = "password"
        salt = gensalt()

        wrapper = BcryptWrapper()
        wrapper.gen_salt = Mock()
        wrapper.gen_salt.return_value = salt

        result = wrapper.gen_password_hash(password)

        assert isinstance(result, bytes)
        wrapper.gen_salt.assert_called_once()
        assert result == hashpw(password.encode(), salt)

    def test_gen_password_hash_user_salt(self):
        password = "password"
        salt = gensalt()
        wrapper = BcryptWrapper()

        result = wrapper.gen_password_hash(password, salt)

        assert isinstance(result, bytes)
        assert result == hashpw(password.encode(), salt)
