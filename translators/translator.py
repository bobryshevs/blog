from models import Model


class Translator:

    def from_document(self, data: dict) -> Model:
        raise NotImplementedError

    def to_document(self, model: Model) -> dict:
        raise NotImplementedError
