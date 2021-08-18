from bson import ObjectId
from validators import ContentValidator


class ContentObjectIdValidator(ContentValidator):
    def __init__(self, key: str) -> None:
        super().__init__(key)

    def valid(self, args: dict) -> bool:

        return ObjectId.is_valid(args.get(self.key))
