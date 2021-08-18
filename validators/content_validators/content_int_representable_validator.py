from validators import ContentValidator
from exceptions import BadRequest


class ContentIntRepresentableValidator(ContentValidator):
    def __init__(self, key: str) -> None:
        super().__init__(key)

    def valid(self, args: dict) -> bool:
        try:
            # argument must be a string:
            #           // int("1.3") -> Exception
            #           // int(1.3)   ->  1
            # check it in type_validators
            int(args.get(self.key))
            return True
        except (TypeError, ValueError):
            raise BadRequest()

