from email_validator import (
    validate_email,
    EmailNotValidError
)


class EmailValidator:
    def __init__(self, key: str) -> None:
        self.key = key

    def valid(self, args: dict) -> bool:
        try:
            validate_email(args.get(self.key))
            return True
        except EmailNotValidError:
            return False

    def error(self):
        return f"Error in {self.key}. Invalid email"
