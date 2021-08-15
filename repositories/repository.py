from bson import ObjectId
from bson.errors import InvalidId
from translators.translator import Translator


class Repository:
    def __init__(self, translator: Translator) -> None:
        self.translator = translator
