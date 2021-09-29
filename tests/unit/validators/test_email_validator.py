from validators import EmailValidator


class TestEmailValidator:
    def test_valid_true(self):
        validator = EmailValidator(key="email")
        args = {"email": "wstswsb@gmail.com"}

        result = validator.valid(args)

        assert isinstance(result, bool)
        assert result is True

    def test_valid_false(self):
        validator = EmailValidator(key="email")
        args = {"email": "asdkflj;afj;ljsdkk#592()$$@!$@gmail.com"}

        result = validator.valid(args)

        assert isinstance(result, bool)
        assert result is False
