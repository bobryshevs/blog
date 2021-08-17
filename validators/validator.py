class Validator:
    VALID = 1
    INVALID_TYPE_CODE = 2
    INVALID_VALUE_CODE = 3

    def __init__(self, key: str, exceptions: dict) -> None:
        self.key = key

    def validate(self, args: dict):
        raise NotImplementedError()
