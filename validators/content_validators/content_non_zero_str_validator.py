from exceptions import BadRequest
from validators import ContentValidator


class ContentNonZeroStrValidator(ContentValidator):
    def __init__(self, key: str) -> None:
        super().__init__(key)

    def valid(self, args: dict) -> bool:

        value = args.get(self.key)

        if len(value) < 1:
            raise BadRequest()

        return True
