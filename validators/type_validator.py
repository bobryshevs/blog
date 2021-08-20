

class TypeValidator():
    def __init__(self, key: str, type_: type) -> None:
        self.key = key
        self.value_type = type_

    def valid(self, args: dict) -> bool:
        return isinstance(args.get(self.key), self.value_type)
