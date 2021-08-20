from exceptions import BadRequest


class ValidateService:
    def __init__(self, validators: list) -> None:
        self.validators = validators

    def validate(self, args: dict) -> bool:
        for validator in self.validators:
            if validator.valid(args):
                continue
            raise BadRequest(f'{str(type(validator))} - {validator.key}')
        return True
