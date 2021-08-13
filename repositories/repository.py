from bson import ObjectId
from bson.errors import InvalidId


class Repository:
    def __init__(self, translator) -> None:
        self.translator = translator