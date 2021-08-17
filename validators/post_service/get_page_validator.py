from exceptions import BadRequest
from validators.validator import Validator


class GetPageValidator(Validator):

    @staticmethod
    def validate(args: dict) -> None:
        try:
            GetPageValidator.validate_non_negative_int(args.get('page'))
            GetPageValidator.validate_non_negative_int(args.get('page_size'))
        except ValueError:
            raise BadRequest()
        except TypeError:
            raise BadRequest()
