

class PositiveIntValidator():
    def __init__(self, key: str) -> None:
        self.key = key

    def valid(self, args: dict) -> bool:
        if not isinstance(args.get(self.key), int):
            return self.__skip()
        return int(args.get(self.key)) > 0

    def __skip(self):
        return True
