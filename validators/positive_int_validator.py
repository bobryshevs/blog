

class PositiveIntValidator():
    def __init__(self, key: str) -> None:
        self.key = key

    def valid(self, args: dict) -> bool:
        if not isinstance(args.get(self.key), int):
            return self.__skip()
        return int(args.get(self.key)) > 0

    def error(self) -> str:
        return \
            f"Error in [{self.key}]." \
            f"The passed number is not a positive integer"

    def __skip(self):
        return True
