from validators import Validator
import validators


class ValidateService:
    def __init__(self, validators: list[Validator]) -> None:
        self.validators = validators
        self.errors_dict = {
            # error_type (str or int): exception
        }

    def validate(self, args: dict) -> bool:
        for validator in self.validators:
            if not validator.validate(args):
                
