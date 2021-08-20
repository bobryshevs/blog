

class PositiveIntValidator():
    def __init__(self, key: str) -> None:
        self.key = key

    def valid(self, args: dict) -> bool:
        return int(args.get(self.key)) > 0
