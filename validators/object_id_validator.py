from bson import ObjectId
from .base_validator import BaseValidator


class ObjectIdValidator(BaseValidator):

    def valid(self, args: dict) -> bool:
        return ObjectId.is_valid(args.get(self.key))
