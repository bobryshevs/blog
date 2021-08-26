from models import Model


class JsonSerializer:

    def to_json(self, model: Model) -> dict:
        raise NotImplementedError()

    def from_json(self, value: dict) -> Model:
        raise NotImplementedError()
