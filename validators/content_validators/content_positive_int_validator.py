from exceptions import BadRequest
from validators import ContentValidator


class ContentPositiveIntValidator(ContentValidator):
    def __init__(self, key: str) -> None:
        super().__init__(key)

    def valid(self, args: dict) -> bool:
        if int(args.get(self.key)) < 1:
            raise BadRequest
        return True
