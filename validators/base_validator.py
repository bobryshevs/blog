class BaseValidator:
    def __init__(self, key: str) -> None:
        self.key = key

    def valid(self, args: dict) -> bool:
        raise NotImplementedError()
